'''

1 ~ 20 사이의 어떤 수로도 나누어 떨어지는 가장 작은 수
시간이 너무 오래 걸린다 다른 방법을 찾아보자
'''

n=0
while True :
   n+=1
   if(n%1==0 and n%2==0 and n%3==0 and n%4==0 and n%5==0 and n%6==0 and n%7==0 and n%8==0 and n%9==0 and n%10==0 and
   n%11==0 and n%12==0 and n%13==0 and n%14==0 and n%15==0 and n%16==0 and n%17==0 and n%18==0 and n%19==0 ) :
        print(n)
        break