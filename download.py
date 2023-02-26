import time
from ripe.atlas.cousteau import AtlasResultsRequest, Measurement


ATLAS_API_KEY = "a073ef14-45a3-40d1-8479-b97f01481026"

msm_list = [50227813,50227814,50227815,50227816,50227818,50227819,50227820,50227821,50227822,50227823,50227824,50227827,50227828,50227829,50227830,50227831,50227832,50227834,50227835,50227836,50227845,50227846,50227849,50227850,50227851,50227852,50227853,50227854,50227857,50227859]

for msm in msm_list:
    measurement = Measurement(id=msm)
    print(measurement.description)
    file = open("{}.txt - {}".format(measurement.description, msm), "w")
    kwargs = {
        "msm_id":msm,
        "key":ATLAS_API_KEY,
    }

    is_success, results = AtlasResultsRequest(**kwargs).create()

    if is_success:
        file.write(str(results))

    # time.sleep(30)