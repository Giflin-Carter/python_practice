#task1
# student_type=int(input("enter 1 for hostler and enter 2 for dayscholer :"))
# if student_type==1:
#     hostel_fee=int(input("hostel fee="))
#     tution_fee=int(input("tution fee="))
#     print("total fee is",hostel_fee+tution_fee)
# elif student_type==2:
#     tution_fee=int(input("tution fee="))
#     bus_fee=int(input("bus fee"))
#     print("total fee is",tution_fee+bus_fee)
# else:
#     print("invalid input")

#task2
# account_balance=int(input("account balance is :"))
# withdrawal_amt=int(input("withfrawal amount is:"))
# if withdrawal_amt > 10000:
#     print("limit exceeded")
# elif account_balance < withdrawal_amt:
#     print("insufficient fund")
# else:
#     print("allow withdrawal")

#task3
# account_balance=30000
# ATM_pin=2345
# enter_pin=int(input("enter the pin:"))
# if ATM_pin==enter_pin:
#     print("continue")
# else:
#     print("wrong pin!!")

# withdrawal_amount=int(input("enter withdrawal amount:"))
# if withdrawal_amount <=0:
#     print("invalid withdrawl amt")
# elif withdrawal_amount<= account_balance:
#     print("vaild withdrawal amt")
#     print("withdrawal succesful")
# else:
#     print("balance was insufficient")

# remaining_balance=account_balance-withdrawal_amount
# if withdrawal_amount<=account_balance:
#     print("remaining balance is",remaining_balance)
# else:
#     print("invalid input amount")

#task4
# age=int(input("enter age:"))
# if age<=5:
#     print("free entry")
# elif 5<= age <= 17:
#     print("child ticket price is ₹150")
# elif 18 <= age <= 59:
#     print("adult ticket price is ₹250 ")
# elif age>60:
#     print("senior citizen 30% discount")
# else:
#     print("no entry")
# show_time=input("enter 1 for morning show and enter 2 for eve show:")
# if show_time==1:
#     print("₹50 discount for morning show")
# else:
#     print("normal price")
# if child==150:
    

#LOOP
#Task5
# sum=0
# for i in range(1,100,2):
#     print(i)
#     sum=i+sum
# print(sum)

# sum=0
# for i in range (2,100,2):
#     print(i)
#     sum=i+sum
# print(sum)

# n=int(input())
# for i in range (1,10):
#     print(i+n)

# maths=int(input("maths="))
# sci=int(input("sci="))
# ss=int(input("ss="))
# tam=int(input("tam="))
# eng=int(input("eng="))
# tot=maths+sci+ss+tam+eng
# print("total=",tot)
# average=tot/2
# print("average=",average)


# for i in range (5):
#     print("*",end="")
# print()
# for i in range (4):
#     print("*",end="")
# print()
# for i in range (3):
#     print("*",end="")
# print()
# for i in range (2):
#     print("*",end="")
# print()
# for i in range (1):
#     print("*",end="")
# print()


# for i in range (1):
#     print("*",end="")
# print()
# for i in range (2):
#     print("*",end="")
# print()
# for i in range (3):
#     print("*",end="")
# print()
# for i in range (4):
#     print("*",end="")
# print()
# for i in range (5):
#     print("*",end="")
# print()

# for i in range(5,0,-1):
#     print("*"*i)
# for i in range(2,6):
#     print("*"*i)

# while i>=10:
#     if i/2==0:
#         print(i)
#     i+=1


# i=1
# odd=0
# while i<=10:
#     odd +=1
#     i+=1
# print(odd)

# i=0
# while i<=10:
#     if i%2==0:
#         print(i)
#     i+=1

# total_seats=20
# seat_number=1
# while seat_number<=total_seats:
#     name=(input("enter your name:"))
#     print(f"seat {seat_number}booked for{name}/n")
# seat_number+=1
# print("all seats are booked")