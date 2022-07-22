# -*- coding: utf-8 -*-

# 读取 wx.dat文件并处理
def read_wxdat(path):
    f = open(path, 'rb')
    # n = 0
    s = f.read(1)
    result = ""
    while s:
        byte = ord(s)
        # n = n+1
        # print('%02x'%(byte),end='')
        result += '%02x' % (byte)
        # if n%16==0:
        #         print('')
        s = f.read(1)
    # print(result)
    # print('\n\ntotal bytes: %d'%n)
    return result


# 将处理后的内容写回去
def write_handlefile(path, data):
    with open(path, 'w') as f:  # 如果文件不存在会自动创建， 'w'表示写数据，写之前会清空文件中的原有数据！
        f.write(data)


if __name__ == "__main__":
    path = 'wx.dat'
    result = read_wxdat(path)
    # print(result)
    target_path = "wx.txt"
    write_handlefile(target_path, result)
