#1
celsius=float(input('请输入摄氏度：')) 
fathrenheit=1.8*celsius+32
print('%.1f华氏度'%fathrenheit) 
#输入：43
#结果：109.4

#2
import math
radius=float(input('请输入圆柱体的半径：>>')) 
length=float(input('请输入圆柱体的高：>>')) 
area=radius*radius*math.pi
volume=area*length
print('圆柱体底面积: %.2f' % area)
print('圆柱体体积: %.2f' % volume)
#输入：5.5  12
#结果：95.0331   1140.4

#3
foot=float(input('请输入要转换的英尺数：'))
m=float(foot*0.305)
print('%.1f英尺数=%.4f米数'%(foot,m)) 
#输入：16.5
#结果：5.0325



#4
M=float(input('请输入水量：'))
initialtemperature=float(input('请输入水的初始温度：')) 
finaltemperature=float(input('请输入水的最终温度：')) 
Q=M*(finaltemperature-initialtemperature)*4184 
print('水从%.1f初始温度到%.1f最终温度所消耗的能量=%.1f'%(initialtemperature,finaltemperature,Q)) 

#输入：55.5   3.5  10.5
#结果：1625484.0


#5
ce=float(input('请输入差额：'))
nll=float(input('请输入年利率：'))
lx=float(ce*(nll/1200)) 
print('下个月的利息%.5f'%lx)

#输入：1000  3.5
#结果：2.91667

#6
v0=float(input('请输入初始速度：'))
v1=float(input('请输入末速度：'))
t=float(input('请输入单位时间内所需的时间：'))
a=(v1-v0)/t
print('平均速度是：%.5f'%a) 


#输入：5.5   50.9  4.5
#结果：10.0889

#7
money=int(input('请输入存入的金额：'))
month=int(input('请输入要存入的月数：'))
yll=0.00417
zje=money*(1+yll)
zje=(money+zje)*(1+yll)
zje=(money+zje)*(1+yll)
zje=(money+zje)*(1+yll)
zje=(money+zje)*(1+yll)
zje=(money+zje)*(1+yll)
print('%d月后的总金额%.2f'%(month,zje)) 


#输入：100   6
#结果：608.81


#8
number=int(input('请输入0-1000之间的整数：'))
a=number%10
b=number//10
c=b%10
d=b//10
sum=(a+c+d)
print('各数字之和为：%d'%sum) 

#输入：999
#结果：27