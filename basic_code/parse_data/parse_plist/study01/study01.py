import datetime
import plistlib


def make_plist():
    pl = dict(
        aString="Doodah",
        aList=["A", "B", 12, 32.1, [1, 2, 3]],
        aFloat=0.1,
        anInt=728,
        aDict=dict(
            anotherString="<hello & hi there!>",
            aThirdString="M\xe4ssig, Ma\xdf",
            aTrueValue=True,
            aFalseValue=False,
        ),
        someData=b"<binary gunk>",
        someMoreData=b"<lots of binary gunk>" * 10,
        aDate=datetime.datetime.now()
    )
    print(plistlib.dumps(pl).decode())


def parse_plist():
    f = open("test.plist", "rb")
    plist = f.read()
    pl = plistlib.loads(plist)
    print(pl["foo"])


if __name__ == '__main__':
    # make_plist()
    parse_plist()
