# （2）编写一个对列表进行从小到大排序的函数。

def sort(s):
    for j in range(0, len(s) - 1):
        for k in range(0, len(s) - 1 - j):
            if s[k] > s[k + 1]:
                t = s[k]
                s[k] = s[k + 1]
                s[k + 1] = t
    print(s)


if __name__ == '__main__':
    n = eval(input())
    a = []
    for i in range(0, n):
        a.append(eval(input()))
    sort(a)
