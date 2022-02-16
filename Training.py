# region  数字交换
import copy
from typing import List

a = 3
b = 5
(a, b) = (b, a)
print(a, b)
# endregion

# region 猜数字游戏
import random as randdat

gusee = randdat.randint(0, 9)

count = 0
while count < 3:

    guseedat = int(input('请输入一个10以内的数字：，一共有3次机会\n'))

    if guseedat < gusee:
        print('猜小了,还剩' + str(3 - 1 - count) + '次机会')

    elif guseedat > gusee:
        print('猜大了，还剩' + str(3 - 1 - count) + '次机会')
    else:
        print('猜对了，牛逼')
        break
    count += 1

print('游戏结束！')
# endregion

# region 循环
for i in range(0, 4):
    print(i)
# endregion

# region 给任意一个的正整数，要求：一、求它是几位数，二、逆序打印出各位数字
while 1:
    getDat = int(input('请输入一个正整数：'))
    count1 = len(str(getDat))
    a = getDat
    count = 0
    while 1:
        count += 1
        if a < 10:
            print(a)
            break
        (a, b) = divmod(a, 10)
        print(b)

    print('是%d位数字' % count1)

# endregion

# region 有数字:1、2、3、4，能组成多少个互不相同且无重复数字的三位数？都是多少？
numList = []
count = 0
for ii in range(1, 5):
    for jj in range(1, 5):
        for kk in range(1, 5):
            if ii != jj and jj != kk and kk != ii:
                numList.append(ii * 100 + jj * 10 + kk)
                count += 1
                print(ii, jj, kk)
print('共%d个三位数，分别是:' % count)
print(numList)
# endregion

# region 输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数，正则表达式
import re

teststr = input('请输入一个字符串：')
countAZ = len(re.findall('[A-Z]|[a-z]]', teststr))
countEmp = len(re.findall(' ', teststr))
countNum = len(re.findall('[0-9]', teststr))
countOther = len(teststr) - (countNum + countAZ + countEmp)

print('字母数量:%d' % countAZ)
print('空格数量:%d' % countEmp)
print('数字数量:%d' % countNum)
print('其他数量:%d' % countOther)
# endregion

# region 两个乒乓球队进行比赛，各出三人。甲队为a,b,c三人，乙队为x,y,z三人。已抽签决定
# 比赛名单。有人向队员打听比赛的名单。a说他不和x比，c说他不和x,z比，请编程序找出三队赛手的名单。
team1 = [str('z'), str('x'), str('y')]
# endregion

# region 企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，奖金可提10%；利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；20万到40万之间时，高于20
# 万元的部分，可提成5%；40万到60万之间时高于40万元的部分，可提成3%；60万到100万之间时，高于60万元的部分，可提成1.5%；高于100万元时，超过100万元的部分按1%提成。输入当月利润，求出应发放奖金总数？
profitNum = float(input('当月利润为：'))
proFitDesk = [100.0, 60.0, 40.0, 20.0, 10.0, 0.0]
ratDesk = [0.1, 0.075, 0.05, 0.03, 0.015, 0.01]
bonusNum = 0
bonusCount = profitNum
for ii in range(0, 6):
    ii = int(ii)
    if profitNum > proFitDesk[ii]:
        bonusNum += (bonusCount - proFitDesk[ii]) * ratDesk[-ii - 1]
        bonusCount = proFitDesk[ii]
print(bonusNum)

# endregion

# region  一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？
import math

x = int(0)
while 1:
    a = math.sqrt(x + 100)
    b = math.sqrt(x + 100 + 168)
    if (a - int(a)) == 0 and (b - int(b)) == 0:
        print('数据是：%d' % x)
        break
    x += 1
# endregion

# region 输入某年某月某日，判断这一天是这一年的第几天？
import datetime
x = int(input('year:'))
y = int(input('month:'))
z = int(input('day:'))
a = datetime.datetime(x, y, z, 0, 0, 0)
b = datetime.datetime(x-1, 12, 31)
c = a - b
print(c.days)

# endregion

# region 输入三个整数x,y,z，请把这三个数的最大值。
def sorta(raw):
    raw1 = raw
    for ii in range(len(raw)-1):
        for jj in range(ii+1, len(raw)):
            # print(len(raw))
            a = raw1[ii]
            b = raw1[jj]
            # print(raw1[ii], raw1[jj])
            if a < b:
                raw1[ii], raw1[jj] = raw1[jj], raw1[ii]
    return raw1

rawData = []
for ii in range(5):
    x = int(input('输入整数：'))
    rawData.append(x)
raw1 = sorta(rawData)
print(raw1)

# endregion

# region 输出9*9口诀表，注意输出形式为直角三角形。
for ii in range(1,10):
    for jj in range(1,ii+1):
        count = ii * jj
        # print('%d' %jj, '*',  '%d' %ii , '= %d '   %count, end = '')
        print('%d * %d = %d ' %(jj,ii,count),end='')
    print('\n')
# endregion

# region 有一对兔子，从出生后第3个月起每个月都生一对兔子，小兔子长到第三个月后每个月又生一对兔子， 假如兔子都不死，问每个月的兔子总数为多少？ 斐波那契数列
month1 = 1
month2 = 0
month3 = 0
monthUP = 0
for ii in range(100):
    month1,month2,month3,monthUP = monthUP + month3, month1, month2, monthUP + month3
    print('%d,%d,%d,%d' % (monthUP,month1,month2,month3))

# endregion

# region 对10个随机个位数进行排序（从小到大）
import  random
import copy
def sorta(raw):
    raw1 = raw
    for ii in range(len(raw)-1):
        for jj in range(ii+1, len(raw)):
            # print(len(raw))
            a = raw1[ii]
            b = raw1[jj]
            # print(raw1[ii], raw1[jj])
            if a > b:
                raw1[ii], raw1[jj] = raw1[jj], raw1[ii]
    return raw1
daList = [random.randint(0,10) for i in range(10)]
print(daList)
daList1 = copy.copy(daList)

daListSort = sorta(daList1)
print(daList)
print(daList1)
print(daListSort)

# endregion