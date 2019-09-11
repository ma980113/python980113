

#1
a=float(input('请输入a：'))
b=float(input('请输入b：'))
c=float(input('请输入c：'))

r1=(-b+(b**2-4*a*c)**0.5)/2*a 
r2=(-b-(b**2-4*a*c)**0.5)/2*a 

f=float(b**2-4*a*c)

if  f>0:
    print('方程式有两个不相等的实根：分别为r1=%.2f,r2=%.2f'%(r1,r2))
elif f==0:
    print('方程式有两个相等的实数根：r1=r2=%.2f'%r1)
else:
    print('方程式无实根')



#2


#3没做出来
today=int(input('请输入今天是哪一天（星期日是0，星期一是1...星期六是6）：'))
future=int(input('请输入今天到未来的某一天的天数：'))
i=future%7
future1=today+i
print('未来这天是%day'%future1)
"Sunday","Monday","Tuesday","Wednesday","Thurday","Friday","Saturday"

 
#4
number1 = int(input('请输入第一个数：'))
number2 = int(input('请输入第二个数：'))
number3 = int(input('请输入第三个数：'))
if number1 >= number2:
    if number1 >= number3:
        if number2 >= number3:
            print(number3,number2,number1)
        else:
            print(number2,number3,number1)
    else:
        print(number2,number1,number3)
else:
    if number1 >= number3:
        print(number3,number1,number2)
    elif number2 >= number3:
        print(number1,number3,number2)
    else:
        print(number1,number2,number3)
 
#5

weight1=float(input('请输入第一种包装的重量：'))
money1=float(input('请输入第一种包装的价钱：'))
weight2=float(input('请输入第二种包装的重量：'))
money2=float(input('请输入第二种包装的价钱：'))
i1=money1/weight1
i2=money2/weight2
if weight1==weight2 and i1<i2:
    print('第一种包装的大米价格更好')
elif weight1==weight2 and i1>i2:
    print('第二种包装的大米价格更好')
elif weight1!=weight2 and i1<i2:
    print('第一种包装的大米价格更好')
elif weight1!=weight2 and i1>i2:
    print('第二种包装的大米价格更好')
else:
    print('两种包装都好')
 

#6
month=int(input('请输入月份：'))
year=int(input('请输入年份：'))


if (month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12):
    print('%d年%d月份有三十一天'%(year,month))
elif (month==4 or month==6 or month==9 or month==11 ):
    print('%d年%d月份有三十天'%(year,month))
elif  month==2  and  ((year%4==0 and year%100!=0) or year%400==0):
    print('%d年%d月份有二十九天'%(year,month))
else:
    print('%d年%d月份有二十八天'%(year,month))

#7
import random

guess=int(input('请输入抛硬币猜测的数值：（1为正面，2为反面）'))
coin=random.randint(1,2)
if coin==1:
    print('硬币为正面')
else:
    print('硬币为反面')
if guess==coin:
    print('猜测正确！')
else:
    print('猜测错误！')



 #8
import numpy as np 
computer=np.random.choice(['0','1','2'])
print(computer) 
user=input('请输入剪刀0，石头1，布2：')
if computer==user:
    print('平局')
elif computer=="0" and user=="2":
    print('输了')
elif computer=="1" and user=="0":
    print('输了')
elif computer=="2" and user=="1" :
    print('输了')
else:
    print('赢了')



 #9 没做出来
year=float(input('请输入年份：'))
month=input('请输入月份：')
day=input('请输入这个月的一天：')
k=float(year%100)
j=float(year/100)

h=str((day+26*(month+1)/10+k+k/4+j/4+5*j)%7)

while month==1:
     year-=1
while month==2:
    year-=1
for i in theday:
    if i==0:
        print('这天是这周的Saturday')
    elif i==1:
        print('这天是这周的Sunday')
    elif i==2:
        print('这天是这周的Monday')
    elif i==3:
        print('这天是这周的Tuesday')
    elif i==4:
        print('这天是这周的Wednesday')
    elif i==5:
        print('这天是这周的Thursday') 
    elif i==6:
        print('这天是这周的Friday')   
print('%.2f'%h)         



#11
number=int(input('请输入一个三位数：'))
n1=number%10         
n2=number//10  
n4=n2%10   
n3=n2//10   
print('%d %d %d'%(n1,n4,n3))
if n3==n1:
    print('是回文数')
else:
    print('不是回文数')



#12

s1=int(input('请输入三角形的任意一边：'))
s2=int(input('请输入三角形的任意一边：'))
s3=int(input('请输入三角形的任意一边：'))
d=s1+s2+s3
if (s1+s2>s3 and s1+s3>s2 and s2+s3>s1 ):
    print('该三角形的周长是=%d'%d)
else:
    print('构不成三角形')



#13
