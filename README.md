# Python 技术资料

## 指定 python 解释器

python script.py 
#!/usr/bin/python 被忽略，等同于注释
./script.py 
#!/usr/bin/python 指定解释器的路径

#!/usr/bin/python3 告诉操作系统执行这个脚本的时候，调用 /usr/bin 下的 python3 解释器；
#!/usr/bin/env python3 这种用法是为了防止操作系统用户没有将 python3 装在默认的 /usr/bin 路径里。当系统看到这一行的时候，首先会到 env 设置里查找 python3 的安装路径，再调用对应路径下的解释器程序完成操作。
#!/usr/bin/python3 相当于写死了 python3 路径;
#!/usr/bin/env python3 会去环境设置寻找 python3 目录，推荐这种写法。
