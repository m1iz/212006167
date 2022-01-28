# （3）编写一个函数，判断输入的年份是否为闺年，要求输入的年份大于1800（函数要能够处理年份不为数字和输入的年份不大于1800的情形）。年份通过键盘输入。


y = input("请输入年份：")


def runnian(year):
    if not year.isdigit():
        print("年份不为数字")
    elif int(year) <= 1800:
        print("年份小于1800")
    else:
        year1 = int(year)
        if year1 % 4 == 0 and year1 % 100 != 0:
            print("%d年是闰年" % year1)
        elif year1 % 400 == 0:
            print("%d年是闰年" % year1)
        else:
            print("%d年不是闰年" % year1)


if __name__ == '__main__':
    runnian(y)
