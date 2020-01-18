# palindrome(회문)

def check_pal(s):
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

s = input("문자열 입력")
s = s.replace(" ","")

if(check_pal(s) == True):
    print("palindrome")
else :
    print("Not palindrome")
