#首先先定义一个类
class people:
    #下面是定义基本属性（在外部可以直接进行访问）
    name=''
    age=0
    #下面是定义私有属性（在外部不能直接进行访问）
    __weight=0
    #定义构造方法
    def __init__(self,n,a,w):
        self.name=n
        self.age=a
        self.__weight=w
    def speak(self):
        print("%s说：我%d岁，体重%d公斤"%(self.name,self.age,self.__weight))
        
#单继承
class student(people):
    grade=''
    def __init__(self,n,a,w,g):
    #调用父类的构造函数
        people.__init__(self,n,a,w)
        self.grade=g
    #下面是覆写父类的方法
    def speak(self):
        print("%s说：我%d岁,在读大学%d年级"%(self.name,self.age,self.grade))#这里我在写的时候犯了一个错误，我增加了“体重%d公斤”和“self.__weight”
                                                                            #然而__weight属于私有属性，不能被外部直接调用因此报了错

#让我们再定义一个类
class speaker():
    topic=''
    name=''
    def __init__(self,n,t):
        self.name=n
        self.topic=t
    def speaker(self):
        print("我叫%s，是一个怪盗，今天我演讲的主题是%s"%(self.name,self.topic))

#发动魔法卡！！！！秘技-多重继承！！！
class sample(speaker,student):
    a=''
    def __init__(self,n,a,w,g,t):
        student.__init__(self,n,a,w,g)
        speaker.__init__(self,n,t)

test=sample("黑羽快斗",19,65,1,"《如何调戏柯南以及如何哄青山开心》")
test.speak()
test.speaker()