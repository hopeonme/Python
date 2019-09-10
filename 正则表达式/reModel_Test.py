# 导入re
import re

def test1():
    content = '(az/hprichbg/rb/jpg) az/hprichbg/rb/..jpg az/hprichbg/r/.jpg az/hprichbg/rb/  vv...jpg)'
    content1 = '(a)a)'
    reg = r'(az/hprichbg/rb/.*?\.jpg)'
    reg1 = r'a'
    print(content)
    a = re.findall(reg, content, re.S)
    print(a)
    print(re.S)


if __name__ == '__main__':
    test1()