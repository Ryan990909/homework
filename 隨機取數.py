import random
num1=random.randint(1,20) 
max=20
min=1
score=20
time=20
time2=0
while 1:
   if score<=0:
       print('很遗憾，你沒有答題機會了！') 
       break
   while 5:
       try:
           
         guess=int(input('猜一個%d~%d的整数:'%(min,max)))
         break
       except:
         print('请输入数字') 
   if guess==num1:
        time=time+1
        print('恭喜你猜對了,此次得%d分,共答题%d次,警告%d次'%(score,time,time2))
        break
   elif guess>max or guess<min:
         score=score-4
         time=time+1
         time2=time2+1
         print('警告%d次：不在提示範圍内,扣除4分，剩餘%d'%(time2,score))
     
   else:
        if guess>num1:
            score=score-2
            time=time+1
            print('很遗憾，你答错了,扣除2分，剩餘%d'%(score))
            max=guess-1            
        else:
            score=score-2
            time=time+1
            print('很遗憾，你答错了,扣除2分，剩餘%d'%(score))




