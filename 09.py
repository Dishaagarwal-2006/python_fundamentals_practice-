# 11.py → Armstrong number
# 12.py → Strong number
# 13.py → Harshad number
# 14.py → Spy number
# 15.py → Perfect number
#  question 11
n = int(input("enter the number "))

org_num = n 
arm_num =0 
while n > 0 :
    digit = n%10 
    arm_num += digit**3
    n = n//10 

if(arm_num == org_num):
        print("armstrong number ")
else:
        print("not armstrong number.")

