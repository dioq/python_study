# Flask 生产环境

Flask 的内置服务器不适合生产环境，因为它不能很好地扩展并且默认情况下一次只处理一个请求。部署线上需要使用WSGI替代。

pip3 install gevent
