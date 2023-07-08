# iOS ipa包通过Safari在线安装
Safari 浏览器有下载并安装ipa的权限。
1. 先制作一个 html 网页, 从网页里下载一个 plist文件
<a class="blink ios" href="itms-services://?action=download-manifest&url=https://jobs8.cn:9000/download/download.plist">
    iOS App 在线安装
</a>
2. plist 文件里下载ipa包
<dict>
    <key>kind</key>
    <string>software-package</string>
    <key>url</key>
    <string>https://jobs8.cn:9000/download/test.ipa</string>
</dict>

注:python代码只需要返回一个网页,再实现一个文件下载的功能
