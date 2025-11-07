class Cal(object):
    @staticmethod
    def add(x, y):
        return x + y

    @staticmethod
    def mul(x, y):
        return x * y


print(Cal.mul(1, 2))
c = Cal()
print(c.add(10, 20))
