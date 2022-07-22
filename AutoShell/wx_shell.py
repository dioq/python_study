# coding: utf-8
#
import uiautomator2 as u2

d = u2.connect('http://localhost:8100')

s = d.session('cn.jobs8')

d.xpath('//Window[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[2]/Button[2]').click()
d.xpath('//Window[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[2]/Button[1]').click()

