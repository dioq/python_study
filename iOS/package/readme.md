# iOS ipa 在线安装

python代码 实现一个文件下载的接口
原理:把 install.plist 文件下载到客户端。 install.plist 通过文件下载接口 下载url指定的 ipa包

## 配置 plist 文件,plist 文件里下载ipa包

<dict>
    <key>kind</key>
    <string>software-package</string>
    <key>url</key>
    <string>https://jobs8.cn:9000/download/test.ipa</string>
</dict>

## Safari 浏览器下载并安装ipa包

制作一个 html 网页, 从网页里下载一个 plist文件
<a class="blink ios" href="itms-services://?action=download-manifest&url=https://jobs8.cn:9000/download/install.plist">
    iOS App 在线安装
</a>

## iOS app 内下载并安装ipa包

NSString *scheme = @"itms-services://?action=download-manifest&url=https://jobs8.cn:9000/download/install.plist";
NSURL *url = [NSURL URLWithString:scheme];
UIApplication *application = [UIApplication sharedApplication];
[application openURL:url options:@{} completionHandler:^(BOOL success) {
        if(success){
            NSLog(@"open %@",scheme);
        }else {
            NSLog(@"open fail");
        }
}];
