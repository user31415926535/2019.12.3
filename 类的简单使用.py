class MyClass:
    i = 12345
    def f(self):
        return 'hello world'
 
x = MyClass()
print("MyClass 类的属性 i 为：", x.i)
print("MyClass 类的方法 f 输出为：", x.f())

class complex:
    def __init__(self,realpart,imagpart):#注意init前后的‘_’是两个
        self.r=realpart
        self.i=imagpart
s=complex(3.0,-4.5)
print(s.r,s.i)
