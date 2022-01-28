# （4）请编程对输入的明文进行加密处理。加密方法是每个明文'字母'变成其后的第5个字母，如果超过Z或者z，则循环进行，即Z或z后接A或a。测试数据可使用个人的名字拼音。

a = input("请输入字符串：")
x = list(a)
for i in x:
    if ord(i) < ord("A") or ord(i) > ord("z") or ord("Z") < ord(i) < ord("a"):
        pass

    elif ord("a") <= ord(i) <= ord("z") or ord("A") <= ord(i) <= ord("Z"):
        i = chr(ord(i) + 5)

        if ord(i) < ord("A") or ord(i) > ord("z") or ord("Z") < ord(i) < ord("a"):
            i = chr(ord(i) - 26)
    print(i, end="")
