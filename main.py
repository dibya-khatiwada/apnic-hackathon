



from datetime import datetime
from ripe.atlas.cousteau import (
  Ping,
  Traceroute,
  Dns,
  AtlasSource,
  AtlasCreateRequest
)

ATLAS_API_KEY = "YOUR-RIPE_API_KEY"


apnic_prb = []
ripe_prb = []
arin_prb = []
lacnic_prb = []
afrinic_prb = []

all_probes_list=[apnic_prb,ripe_prb,arin_prb,lacnic_prb,afrinic_prb]
countries_dict = {
'apnic':['AF', 'AE', 'AM', 'AZ', 'BD', 'BH', 'BN', 'BT', 'CN', 'GE', 'HK', 'ID', 'IN', 'IR', 'IQ', 'IL', 'JO', 'JP', 'KZ', 'KG', 'KH', 'KR', 'KW', 'LA', 'LB', 'LK', 'MO', 'MV', 'MM', 'MN', 'MY', 'NP', 'OM', 'PK', 'PH', 'KP', 'PS', 'QA', 'SA', 'SG', 'SY', 'TH', 'TJ', 'TM', 'TL', 'TR', 'TW', 'UZ', 'VN', 'YE'],
'ripe': ['AX', 'AL', 'AD', 'AT', 'BE', 'BG', 'BA', 'BY', 'CH', 'CY', 'CZ', 'DE', 'DK', 'ES', 'EE', 'FI', 'FR', 'FO', 'GB', 'GG', 'GI', 'GR', 'HR', 'HU', 'IM', 'IE', 'IS', 'IT', 'JE', 'XK', 'LI', 'LT', 'LU', 'LV', 'MC', 'MD', 'MK', 'MT', 'ME', 'NL', 'NO', 'PL', 'PT', 'RO', 'RU', 'SJ', 'SM', 'RS', 'SK', 'SI', 'SE', 'UA', 'VA'],
'lacnic':['AR', 'BO', 'BR', 'CL', 'CO', 'EC', 'FK', 'GF', 'GY', 'PE', 'PY', 'SR', 'UY', 'VE'],
'arin': ['BM', 'CA', 'GL', 'MX', 'PM', 'UM', 'US'],
'afrinic':['ZA', 'EG', 'DZ', 'MA', 'ZM', 'AO', 'TZ', 'KE', 'BW', 'SD', 'GH', 'CM', 'GA', 'NG', 'MU', 'ZW', 'SZ', 'SC', 'UG', 'NA','LY', 'ML', 'RW', 'ET', 'GM', 'BF', 'LS', 'NE', 'BJ', 'MR', 'CI', 'MZ', 'TG', 'ER', 'DJ', 'TN', 'CD', 'MW', 'SS', 'SL', 'KM', 'RE', 'CG', 'MG', 'GN','CF', 'LR', 'GQ', 'SN', 'SO', 'BI', 'TD', 'CV', 'GW', 'YT', 'ST']
}



def filter_probe_list():
    with open('atlas-probes-all.txt') as file:
        lines = file.readlines()
        for line in lines:
            result = list(filter(lambda item: item, line.split(' ')))
            if len(result) == 6:
                for key,value in countries_dict.items():
                    if result[3].upper() in value:
                        if key == 'apnic':
                            apnic_prb.append(result[0])
                        elif key == 'ripe':
                            ripe_prb.append(result[0])
                        elif key == 'lacnic':
                            lacnic_prb.append(result[0])
                        elif key == 'afrinic':
                            afrinic_prb.append(result[0])
                        else:
                            arin_prb.append(result[0])


def main():
    filter_probe_list()
    ping_4 = Ping(af=4, target="anyns.pch.net", description="IPv4 ping to anyns.pch.net - {} ".format(datetime.today()))
    ping_6 = Ping(af=6, target="anyns.pch.net", description="IPv6 ping to anyns.pch.net - {} ".format(datetime.today()))
    traceroute_4 = Traceroute(af=4,target="anyns.pch.net",description="IPv4 traceroute to anyns.pch.net - {} ".format(datetime.today()),protocol="ICMP",)
    traceroute_6 = Traceroute(af=6, target="anyns.pch.net",description="IPv6 traceroute to anyns.pch.net - {} ".format(datetime.today()),protocol="ICMP", )
    dns_4 = Dns(af=4, target="anyns.pch.net", description="IPv4 DNS lookup to anyns.pch.net - {}".format(datetime.today()), query_class="CHAOS", query_type="TXT", query_argument = "id.server")
    dns_6 = Dns(af=6, target="anyns.pch.net", description="IPv6 DNS lookup to anyns.pch.net - {}".format(datetime.today()), query_class="CHAOS", query_type="TXT", query_argument="id.server")
    for region_probe_list in all_probes_list:
        probes = ','.join(np.random.choice(region_probe_list, size=25))
        source = AtlasSource(
            type="probes",
            value="{}".format(probes),
        )
        msm_list = [ping_4, ping_6,traceroute_4,traceroute_6,dns_4,dns_6]
        for msm in msm_list:
            atlas_request = AtlasCreateRequest(
            start_time=datetime.utcnow(),
            key=ATLAS_API_KEY,
            measurements=[msm],
            sources= [source],
            is_oneoff=True
        )
            response = atlas_request.create()
            print(response)

if __name__ == '__main__':
    main()


