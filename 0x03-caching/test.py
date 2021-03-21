class increment():
    i = 10
    def incrmentx(self):

        self.__class__.i = self.__class__.i +1

a = increment()
print(a.i)


a.incrmentx()

print(a.i)
print(increment.i)