#   练习

# 使用__slots__要注意，__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的：

class Student():
    __slots__ = ('name', 'age') # 用tuple定义允许绑定的属性名称


# 动态实例
class Node():
    pass


if __name__ == '__main__':
    # s = Student()  # 创建新的实例
    # s.name = 'AMJ'
    # s.age = 17
    # # s.score = 'aa'
    # print(s.name)
    node = Node()
    node.name = 'aaa'
    node.age = 15
    print(node.name)
    print(node.age)
