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
    # dict = {}
    # if pl["IMEI"] is not None:
    #     IMEI = pl["IMEI"]
    #     print(IMEI)
    #     dict["IMEI"] = IMEI
    #
    # if pl["PRODUCT"] is not None:
    #     PRODUCT = pl["PRODUCT"]
    #     print(PRODUCT)
    #     dict["PRODUCT"] = PRODUCT
    #
    # if pl["UDID"] is not None:
    #     UDID = pl["UDID"]
    #     print(UDID)
    #     dict["UDID"] = UDID
    #
    # if pl["VERSION"] is not None:
    #     VERSION = pl["VERSION"]
    #     print(VERSION)
    #     dict["VERSION"] = VERSION

    # return dict
    return pl


# if __name__ == '__main__':
#     f = open("/Users/lzd/Desktop/device.xml","rb")
#     file_data = f.read()
#     f.close()
#
#     plaintext_data = extract_data(file_data)
#     dict = parse_plist(plaintext_data)
#     print(dict)
