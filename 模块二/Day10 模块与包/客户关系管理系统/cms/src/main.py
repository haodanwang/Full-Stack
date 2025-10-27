import loguru
import sys

logger = loguru.logger


def main():
    logger.info("程序启动\n")
    while 1:
        print(
            """
        1.添加客户
        2.删除客户
        3.修改客户
        4.查询一个客户
        5.查询所有客户
        6.保存
        7.退出
        """
        )
        choice = input("请输入你的选择:")
        if choice == "1":
            pass
        elif choice == "2":
            pass
        elif choice == "3":
            pass
        elif choice == "4":
            pass
        elif choice == "5":
            pass
        elif choice == "6":
            pass
        elif choice == "7":
            logger.info("感谢您的使用 已退出")
            sys.exit()
        else:
            print("请输入有效的数字")


main()
