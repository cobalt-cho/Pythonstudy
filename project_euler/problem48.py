'''

1^1 + 22 + 33 + ... + 10^10 = 10405071317 입니다.
1^1 + 22 + 33 + ... + 1000^1000 의 마지막 10자리 숫자는 무엇입니까?

'''

sum = 0
for i in range(1,1000) :
    sum+=i**i

sum = str(sum)
print(sum)
print(sum[len(sum)-10:len(sum)])