# iOS ipa 在线安装

python代码 实现一个文件下载的接口
原理:把 manifest.plist 文件下载到客户端。 manifest.plist 通过文件下载接口 下载url指定的 ipa包

## manifest.plist 文件里下载ipa包

下载 ipa 包 使用 https
<dict>
<key>kind</key>
<string>software-package</string>
<key>url</key>
<string>https://jobs8.cn:9000/download/test.ipa</string>
</dict>

下载 manifest.plist 必须走 https 的协议,但是 ipa的下载 用 http 协议也可以
<dict>
<key>kind</key>
<string>software-package</string>
<key>url</key>
<string>http://45.11.46.61:9001/download/test.ipa</string>
</dict>

甚至可以 用局域网 ip 实现在手机上装 ipa包
<dict>
<key>kind</key>
<string>software-package</string>
<key>url</key>
<string>http://127.0.0.1:9001/download/test.ipa</string>
</dict>

## Safari 浏览器下载并安装ipa包

制作一个 html 网页, 从网页里下载一个 plist文件
<a class="blink ios" href="itms-services://?action=download-manifest&url=https://jobs8.cn:9000/download/manifest.plist">
iOS App 在线安装
</a>

## iOS app 内下载并安装ipa包

NSString *scheme = @"itms-services://?action=download-manifest&url=https://jobs8.cn:9000/download/manifest.plist";
NSURL *url = [NSURL URLWithString:scheme];
UIApplication *application = [UIApplication sharedApplication];
[application openURL:url options:@{} completionHandler:^(BOOL success) {
    if(success){
        NSLog(@"open %@",scheme);
    }else {
        NSLog(@"open fail");
    }
}];
