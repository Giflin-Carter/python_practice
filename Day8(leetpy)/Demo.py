# print("Pizza Categories")
# print("1. Normal")
# print("2. Deluxe")
# category = int(input("Enter your choice (1 or 2): "))

# print("\nPizza Type")
# print("1. Veg")
# print("2. Non-Veg")
# ptype = int(input("Enter pizza type (1 or 2): "))

# cheese_price = 0
# topping_price = 0
# water_price = 0
# ketchup_price = 0
# softdrink_price = 0
# takeaway_price = 0
# base_price = 0

# if category == 1:  
#     if ptype == 1:
#         base_price = 300
#     else:
#         base_price = 400
# elif category == 2:  
#     if ptype == 1:
#         base_price = 500
#     else:
#         base_price = 600
# if int(input("Extra Cheese? (1.Yes 2.No): ")) == 1:
#     cheese_price = 100

# if int(input("Extra Toppings? (1.Yes 2.No): ")) == 1:
#     topping_price = 100

# if int(input("Water Bottles? (1.Yes 2.No): ")) == 1:
#     bottles = int(input("How many bottles?: "))
#     water_price = bottles * 20

# if int(input("Ketchup? (1.Yes 2.No): ")) == 1:
#     packets = int(input("How many packets?: "))
#     ketchup_price = packets * 5

# if int(input("Soft Drinks? (1.Yes 2.No): ")) == 1:
#     cans = int(input("How many cans?: "))
#     softdrink_price = cans * 75

# if int(input("Take Away? (1.Yes 2.No): ")) == 1:
#     takeaway_price = 20

# total = (base_price + cheese_price + topping_price +
#          water_price + ketchup_price +
#          softdrink_price + takeaway_price)

# print("\n----- BILL -----")
# print("Base Price:", base_price)
# print("Extra Cheese:", cheese_price)
# print("Extra Toppings:", topping_price)
# print("Water Bottle:", water_price)
# print("Ketchup:", ketchup_price)
# print("Soft Drinks:", softdrink_price)
# print("Take Away:", takeaway_price)
# print("Total:", total)


# stack=[]

# while True:
#      print("\n1.Push 2.Pop 3.peek 4.Display 5.exit")
#      choice=int(input("enter choice:"))
#      if choice == 1:
#           val=int(input("enter value"))
#           stack.append(val)
#           print("pushed",val)
#      elif choice == 2:
#           if not stack:
#                print("stack is empty")
#           else:
#                print("poped",stack.pop())
#      elif choice==3:
#           if not stack:
#                print("stack empty")
#           else:
#                print("top")
#      elif choice == 4:
#           print("stack",stack)
#      else:
#           print("invaid choice ")


# queue=[]

# while True:
#      print("\n1.enqueue 2.dequeue 3.peek 4.Display 5.exit")
#      choice=int(input("enter choice:"))
#      if choice == 1:
#           val=int(input("enter value"))
#           queue.append(val)
#           print("added",val)
#      elif choice == 2:
#           if not queue:
#                print("queue is empty")
#           else:
#                print("poped",queue.pop())
#      elif choice==3:
#           if not queue:
#                print("queue empty")
#           else:
#                print("top")
#      elif choice == 4:
#           print("Queue",queue)
#      else:
#           print("invaid choice ")




# | Type           | Insert      | Delete      | Special Feature       |
# | -------------- | ----------- | ----------- | --------------------- |
# | Simple Queue   | Rear        | Front       | FIFO                  |
# | Circular Queue | Rear        | Front       | Reuses space          |
# | Priority Queue | By priority | By priority | Important items first |
# | Deque          | Both ends   | Both ends   | Flexible              |
        


# size = 5
# queue = [None] * size
# front = -1
# rear = -1

# def enqueue(value):
#     global front, rear
    
#     if (rear + 1) % size == front:
#         print("Queue Full")
#         return
    
#     if front == -1:
#         front = 0
    
#     rear = (rear + 1) % size
#     queue[rear] = value
#     print(value, "inserted")

# def dequeue():
#     global front, rear
    
#     if front == -1:
#         print("Queue Empty")
#         return
    
#     removed = queue[front]
    
#     if front == rear:
#         front = rear = -1
#     else:
#         front = (front + 1) % size
    
#     print(removed, "removed")

# def display():
#     if front == -1:
#         print("Queue Empty")
#         return
    
#     i = front
#     print("Queue elements:")
    
#     while True:
#         print(queue[i], end=" ")
#         if i == rear:
#             break
#         i = (i + 1) % size
#     print()

# while True:
#     print("\n1.Enqueue")
#     print("2.Dequeue")
#     print("3.Display")
#     print("4.Exit")

#     choice = int(input("Enter choice: "))

#     if choice == 1:
#         value = int(input("Enter value: "))
#         enqueue(value)

#     elif choice == 2:
#         dequeue()

#     elif choice == 3:
#         display()

#     elif choice == 4:
#         break

#     else:
#         print("Invalid choice")