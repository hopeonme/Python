# 导入re
import re

def test1():
    content = '(az/rb/.*?.jpg)(az/hprichbg/rb/.*?.jpg)(az/hprichbg/rb/.*?.jpg)'
    reg = r'(az/hprichbg/rb/.*?.jpg)'
    a = re.findall(reg, content, re.S)
    print(a)


if __name__ == '__main__':
    test1()
    test1()
    test1()