import time
import win32gui
import win32api
import win32con


# 查找windows窗口，返回窗口起始坐标
def find_window():
    hwnd = win32gui.FindWindow(None, "flutter_study")
    if (hwnd):
        rect = win32gui.GetWindowRect(hwnd)
        return rect[0], rect[1]
    return None


# 模拟鼠标点击
def mouse_click(x, y):
    win32api.SetCursorPos([x, y])
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)


# 模拟点击键盘
def keyboard_touch():
    win32api.keybd_event(0x11, 0, 0, 0)
    win32api.keybd_event(0x56, 0, 0, 0)
    win32api.keybd_event(0x56, 0, win32con.KEYEVENTF_KEYUP, 0)
    win32api.keybd_event(0x11, 0, win32con.KEYEVENTF_KEYUP, 0)
    # time.sleep(1)
    win32api.keybd_event(0x56, 0, 0, 0)
    win32api.keybd_event(0x56, 0, win32con.KEYEVENTF_KEYUP, 0)
    # time.sleep(1)
    win32api.keybd_event(65, 0, 0, 0)
    win32api.keybd_event(65, 0, win32con.KEYEVENTF_KEYUP, 0)


if __name__ == '__main__':
    origin_x, origin_y = find_window()
    x = origin_x + 50
    y = origin_y + 140
    # mouse_click(x, y)

    time.sleep(5)
    keyboard_touch()
