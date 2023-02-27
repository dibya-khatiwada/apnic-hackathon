
import os
import pandas as pd
import csv
from ripe.atlas.cousteau import Probe
from ipaddress import ip_address, IPv4Address


def validIPAddress(IP: str) -> str:
    try:
        return "IPv4" if type(ip_address(IP)) is IPv4Address else "IPv6"
    except ValueError:
        return "Invalid"

def main():
    countries_dict = {
    'apnic':['AF', 'AE', 'AM', 'AZ', 'BD', 'BH', 'BN', 'BT', 'CN', 'GE', 'HK', 'ID', 'IN', 'IR', 'IQ', 'IL', 'JO', 'JP', 'KZ', 'KG', 'KH', 'KR', 'KW', 'LA', 'LB', 'LK', 'MO', 'MV', 'MM', 'MN', 'MY', 'NP', 'OM', 'PK', 'PH', 'KP', 'PS', 'QA', 'SA', 'SG', 'SY', 'TH', 'TJ', 'TM', 'TL', 'TR', 'TW', 'UZ', 'VN', 'YE'],
    'ripe': ['AX', 'AL', 'AD', 'AT', 'BE', 'BG', 'BA', 'BY', 'CH', 'CY', 'CZ', 'DE', 'DK', 'ES', 'EE', 'FI', 'FR', 'FO', 'GB', 'GG', 'GI', 'GR', 'HR', 'HU', 'IM', 'IE', 'IS', 'IT', 'JE', 'XK', 'LI', 'LT', 'LU', 'LV', 'MC', 'MD', 'MK', 'MT', 'ME', 'NL', 'NO', 'PL', 'PT', 'RO', 'RU', 'SJ', 'SM', 'RS', 'SK', 'SI', 'SE', 'UA', 'VA'],
    'lacnic':['AR', 'BO', 'BR', 'CL', 'CO', 'EC', 'FK', 'GF', 'GY', 'PE', 'PY', 'SR', 'UY', 'VE'],
    'arin': ['BM', 'CA', 'GL', 'MX', 'PM', 'UM', 'US'],
    'afrinic':['ZA', 'EG', 'DZ', 'MA', 'ZM', 'AO', 'TZ', 'KE', 'BW', 'SD', 'GH', 'CM', 'GA', 'NG', 'MU', 'ZW', 'SZ', 'SC', 'UG', 'NA','LY', 'ML', 'RW', 'ET', 'GM', 'BF', 'LS', 'NE', 'BJ', 'MR', 'CI', 'MZ', 'TG', 'ER', 'DJ', 'TN', 'CD', 'MW', 'SS', 'SL', 'KM', 'RE', 'CG', 'MG', 'GN','CF', 'LR', 'GQ', 'SN', 'SO', 'BI', 'TD', 'CV', 'GW', 'YT', 'ST']
    }


    for file in os.listdir('./data-sets'):
        if 'ping' in file:
            with open("./data-sets/{}".format(file), 'r') as f:
                data = f.read()
                df = pd.DataFrame(eval(data))
                df.drop(df.index[df['min'] == -1], inplace=True)
                new_df = df[["prb_id","src_addr", "result", "min", "max", "avg"]]
                new_df.to_csv('ping.csv',mode='a', index=False, header=False)

    f = open('ping_final.csv', 'w')
    writer = csv.writer(f)

    with open('ping.csv') as csv_file:
        data = csv_file.readlines()
        try:
            for line in data:
                splitted_line = line.split(',')
                prb_id = int(line.split(',')[0])
                src_addr = line.split(',')[1]
                type_addr = validIPAddress(src_addr)
                print(type_addr)
                rtt_1 = (line.split(',')[2].replace('"[{\'rtt\': ', ' ').replace('}',''))
                rtt_2 = (line.split(',')[3].replace(' {\'rtt\': ', ' ').replace('}', ''))
                rtt_3 = (line.split(',')[4].replace('{\'rtt\': ', ' ').replace(']', '').replace('}"',''))
                probe = Probe(id=prb_id)
                for key,values in countries_dict.items():
                    if probe.country_code in values:
                        probe_region = key
                writer.writerow([prb_id, src_addr, type_addr, probe_region, probe.country_code,probe.asn_v4, probe.asn_v6, probe.prefix_v4, probe.prefix_v6,rtt_1, splitted_line[5].strip(), splitted_line[6].strip(), splitted_line[7].replace('"','').strip()])
                writer.writerow([prb_id, src_addr, type_addr, probe_region, probe.country_code,probe.asn_v4, probe.asn_v6, probe.prefix_v4, probe.prefix_v6,rtt_2, splitted_line[5].strip(), splitted_line[6].strip(), splitted_line[7].replace('"','').strip()])
                writer.writerow([prb_id, src_addr, type_addr, probe_region, probe.country_code,probe.asn_v4, probe.asn_v6, probe.prefix_v4, probe.prefix_v6,rtt_3, splitted_line[5].strip(), splitted_line[6].strip(), splitted_line[7].replace('"','').strip()])
        except IndexError:
            pass
    print("\n\n")


if __name__ == '__main__' :
    main()