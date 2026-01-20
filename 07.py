# Take a number and print sum of its digits

# Take a number and print count of digits

# Take a number and print reverse of the number

# Take a number and check if it is palindrome

# Take a number and print product of its digits

# question 1 

n = int(input("enter the number:"))
sum_of_digit =0 
while n > 0 :  
   digit= n%10 
sum_of_digit+=digit
n = n//10  
print("the su  of digits ", sum_of_digit ) 

# question 2 

n = int(input("enter the number:"))
count =0 
while n > 0 :  
   digit= n%10 
count+=1
n = n//10  
print("the count of digits ", count  ) 

#question 3 
n = int(input("enter the number:"))
rev_num=0
while n > 0 :  
 digit= n%10 
rev_num = rev_num*10+digit 
n = n//10  
print("the reverse   of digits ", rev_num  ) 

# question 4 
n = int(input("enter the number:"))
org_num =n 
rev_num=0
while n > 0 :  
 digit= n%10 
rev_num = rev_num*10+digit
n=n//10
if(rev_num==org_num ):
  print("palindrome number ")
else:
  print("no palindrome ")

#   question 5 
n = int(input("enter the number:"))
product_of_digit =1 
while n > 0 :  
   digit= n%10 
product_of_digit*=digit
n = n//10  
print("the product  of digits ", product_of_digit )
  
  


    

