'''

대칭수(palindrome)인 585는 2진수로 나타내도 1001001001(2)가 되어 여전히 대칭수입니다.

10진법과 2진법으로 모두 대칭수인 1,000,000 이하 숫자의 합을 구하세요.

(주의: 첫번째 자리가 0이면 대칭수가 아님)

'''

def check_pal(s):
    s = str(s)
    low =0
    high = len(s) -1

    while True :
        if low > high :
            return True
        a = s[low]
        b = s[high]
        if a!=b :
            return False
        low +=1
        high -=1

li = []
for i in range(1,1000001):
    a = bin(i)
    a = a.replace("0b","")
    if a[0]!=0 :
        if( check_pal(i) and check_pal(a) ):
            li.append(i)

print(sum(li))