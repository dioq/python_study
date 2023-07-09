import re
import plistlib


# 在一堆数据中提取 xml 文件
def extract_data():
    f = open("device_crypto.xml", "rb")
    file_data = f.read()
    print(file_data)
    # print(type(lines))
    f.close()

    r = re.compile(b"<?xml", re.VERBOSE)
    matchObj = re.search(r, file_data)
    # print(matchObj)
    # print(matchObj.group())
    # print(matchObj.start())
    # print(matchObj.end())
    # print(matchObj.span())
    xml_start = matchObj.start() - 2

    print("=================")
    r1 = re.compile(b"</plist>", re.VERBOSE)
    matchObj = re.search(r1, file_data)
    # print(matchObj)
    # print(matchObj.group())
    # print(matchObj.start())
    # print(matchObj.end())
    # print(matchObj.span())

    xml_end = matchObj.end()

    xml_data = []
    for i in range(xml_start, xml_end):
        xml_data.append(file_data[i])

    f = open("device.plist", "wb")
    f.write(bytes(xml_data))
    f.close()


def parse_plist():
    f = open("device.plist", "rb")
    plist = f.read()
    f.close()
    pl = plistlib.loads(plist)
    IMEI = pl["IMEI"]
    print(IMEI)
    PRODUCT = pl["PRODUCT"]
    print(PRODUCT)
    UDID = pl["UDID"]
    print(UDID)
    VERSION = pl["VERSION"]
    print(VERSION)


if __name__ == '__main__':
    # extract_data()
    parse_plist()
