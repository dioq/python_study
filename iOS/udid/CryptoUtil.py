import re
import plistlib


# 在一堆数据中提取 xml 文件
def extract_data(file_data):
    r = re.compile(b"<?xml", re.VERBOSE)
    matchObj = re.search(r, file_data)
    xml_start = matchObj.start() - 2

    r1 = re.compile(b"</plist>", re.VERBOSE)
    matchObj = re.search(r1, file_data)

    xml_end = matchObj.end()

    xml_data = []
    for i in range(xml_start, xml_end):
        xml_data.append(file_data[i])

    return bytes(xml_data)


def parse_plist(plist):
    pl = plistlib.loads(plist)
    IMEI = ""
    if pl["IMEI"] is not None:
        IMEI = pl["IMEI"]
        print(IMEI)
    PRODUCT = pl["PRODUCT"]
    print(PRODUCT)
    UDID = pl["UDID"]
    print(UDID)
    VERSION = pl["VERSION"]
    print(VERSION)

    dict = {"PRODUCT": PRODUCT, "UDID": UDID, "VERSION": VERSION}
    if IMEI is not None:
        dict["IMEI"] = IMEI

    return dict
