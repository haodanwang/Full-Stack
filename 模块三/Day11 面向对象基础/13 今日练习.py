from loguru import logger

1


# class Circle(object):
#     def __init__(self, r):
#         self.r = r
#
#     def cal_area(self):
#         return 3.14 * self.r**2
#
#     def cal_cicumference(self):
#         return 3.14 * 2 * self.r
#
#
# cir1 = Circle(10)
# cir2 = Circle(5)
# print(cir1.cal_cicumference(), cir1.cal_area())
# print(cir2.cal_cicumference(), cir2.cal_area())

# 2


# class Person(object):
#     def __init__(self, name, health):
#         self.name = name
#         self.health = health
#
#     def kick_dog(self, dog):
#         logger.info(f"狗的名字是:{dog.name},狗的健康值为{dog.health}")
#         dog.decrease_health(20)
#         logger.info(f"{dog.name}的血量为{dog.health}")
#
#     def decrease_health(self, amount):
#         self.health -= amount
#
#
# class Dog(object):
#     def __init__(self, name, health):
#         self.name = name
#         self.health = health
#
#     def bite(self, person):
#         logger.info(f"人的名字是:{person.name},人的健康值为{person.health}")
#         person.decrease_health(10)
#         logger.info(f"{person.name}的血量为{person.health}")
#
#     def decrease_health(self, amount):
#         self.health -= amount
#
#
# shanks = Person("香克斯", 100)
# alex = Dog("李杰", 100)
#
# shanks.kick_dog(alex)
# alex.bite(shanks)
# shanks.kick_dog(alex)
# alex.bite(shanks)
# shanks.kick_dog(alex)
# alex.bite(shanks)


# # 3
#
#
# class BankAccount(object):
#     def __init__(self, account_number, balance=0):
#         self.account_number = account_number
#         self.balance = balance
#
#     def deposit(self, amount):
#         self.balance += amount
#         logger.info(f"{self.account_number}存入{amount}元")
#
#     def withdram(self, amount):
#         if amount <= self.balance:
#             self.balance -= amount
#         else:
#             logger.info("余额不足")
#
#     def get_balance(self):
#         logger.info(f"余额为{self.balance}")
#
#
# card1 = BankAccount("1001", 5000)
# card1.deposit(5000)
# card1.withdram(200)
# card1.get_balance()


class Book(object):
    booklist = []
    bookcount = 0

    def __init__(self, title, author, publiccation_year):
        self.title = title
        self.author = author
        self.publiccation_year = publiccation_year
        self.__class__.booklist.append(
            (self.title, self.author, self.publiccation_year)
        )
        self.__class__.bookcount += 1

    @classmethod
    def show_books(cls):
        logger.info(cls.booklist)


book1 = Book("悲惨世界", "shanks", "1995")
book2 = Book("悲惨世界2", "shanks", "1995")
book3 = Book("悲惨世界3", "shanks", "1995")
Book.show_books()
print(Book.bookcount)
