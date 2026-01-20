# 06.py  → Count even digits
# 07.py  → Count odd digits (you already did this)
# 08.py  → Find largest digit
# 09.py  → Find smallest digit
# 10.py  → Check if sum of digits is divisible by 3


# question 7 
num = int(input("enter the number :"))
count =0 
while num > 0 :
    digit = num%10 
  
    if digit %2 ==0 :

        count+=1 


    num = num//10  
      
    print("count even digit :" , count )
  
#   question 8 


n = int(input("enetr the number :"))
largest =0 
while n >0:
    digit = n%10
    
    if(digit > largest):
        largest = digit 
     
    n = n//10 
    print("the largest number is : " , largest )      


 #   question 9


n = int(input("enetr the number :"))
smallest  =0 
while n >0:
    digit = n%10
    
    if(digit < smallest ):
        smallest  = digit 
     
    n = n//10 
    print("the largest number is : " , smallest )    


    # question 10 
         


n = int(input("enter the number :"))
sum_of_digits = 0 
while n > 0 :
    digit = n % 10 

    sum_of_digits+=digit 
    n = n//10 
   
    if(sum_of_digits % 3 == 0):
        print ("can be divible ")
    else:
        print("cannot be divisible ")
