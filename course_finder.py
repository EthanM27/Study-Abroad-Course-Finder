import requests as req
import json

# return courses that get transfer credit to UMD from sem 2 in edinburgh
def get():
    umd_payload = {
        "country": "",
        "host%5B%5D": "1436",
        "umdequiv": "",
        "hostcoursename": "",
        "coursestatus": "",
        "hostcoursenumber": "",
        "department": "",
        "genedcategory": "",
        "program": "",
        "language": "",
        "offset": "0",
        "limit": "25",
        "orderby": "courses"
    }

    e_payload = {
        "sEcho": "1",
        "iColumns": "11",
        "sColumns": "MOD,NAME,PSL,OCC,OCCNAME,LEV,MOA,LCA,CRD,UDF9,VIEW",
        "iDisplayStart": "0",
        "iDisplayLength": "10",
        "mDataProp_0": "MOD",
        "bSortable_0": "true",
        "mDataProp_1": "NAME",
        "bSortable_1": "true",
        "mDataProp_2": "PSL",
        "bSortable_2": "true",
        "mDataProp_3": "OCC",
        "bSortable_3": "true",
        "mDataProp_4": "OCCNAME",
        "bSortable_4": "true",
        "mDataProp_5": "LEV",
        "bSortable_5": "true",
        "mDataProp_6": "MOA",
        "bSortable_6": "true",
        "mDataProp_7": "LCA",
        "bSortable_7": "true",
        "mDataProp_8": "CRD",
        "bSortable_8": "true",
        "mDataProp_9": "UDF9",
        "bSortable_9": "true",
        "mDataProp_10": "VIEW",
        "bSortable_10": "false",
        "iSortCol_0": "0",
        "sSortDir_0": "asc",
        "iSortingCols": "1",
        "nkey": "GBSOGH52DFKPMFULvDfT0ONqZAKVGEDYyqhISxrGlD67SZNMyJN7aPi4Pro9I8-AT8Ty9iXBZp7RE1pBfohFKB3L0Ju_B4k38Hl3ZmvtGbBPpuKbYiEArtYyAl2nROA2FqY7vPAn52eaVcLxaRUK5hzAm6VirUpM0lBHUYsX4YXJbrUI-S7VHRfZwfiJx3CboSBFkBypPvRW7eT8-eXwNqSrk_q_muO0B3aFEVAVldGzW2rL-Co7TxcBdnc",
        "issCode": "A98664C8-360B-11EC-9C7D-F3CFACDA290C",
        "debugMode": "N",
        "mode": "START",
        "smeSeqn": "003",
    }
       
    resp_umd = json.loads(req.get("https://globaldb.umd.edu/global/server/search").text)
    resp_e = json.loads(req.post("https://www.star.euclid.ed.ac.uk/public/urd/sits.urd/run/siw_sme_b.load_grid_data", e_payload).text)
    return resp

if __name__ == "__main__":
    get()


