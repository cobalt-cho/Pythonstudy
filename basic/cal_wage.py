"""
근무 시간과 시급을 물어본 뒤,
주당 근무 시간이 40시간이 초과하면 1.5배의 임금을 더 지급
"""

time = int(input("근무 시간: "))
wage = int(input("시급 :"))

if time>40 :
    totalWage = 40*wage + (time-40)*wage*1.5
    print(totalWage)
else :
    totalWage = time*wage
    print(totalWage)