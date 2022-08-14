# -*- coding: utf-8 -*-

import wda
import time

uuid = "58dad54ccf463a7cf3752365408d766808f40ffd"
port = 8100
wda_bundle_id = "com.facebook.WebDriverAgentRunner.xctrunner"
c = wda.USBClient(uuid, port=port, wda_bundle_id=wda_bundle_id)
