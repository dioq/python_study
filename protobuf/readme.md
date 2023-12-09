# Protobuf 

## MacOS 安装 protobuf 编译器
brew install protobuf

## python 安装 protobuf 库
pip install protobuf

## 编译 protobuf 文件
protoc xxx.proto --python_out=[outpath]

--python_out        编译成 python 类
--objc_out          编译成 Objective-C 类
--java_out          编译成 java 类
