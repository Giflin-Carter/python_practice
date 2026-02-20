
# 217
# class Solution:
#     def containsDuplicate(self, nums):
#         return len(nums) != len(set(nums))


# if __name__ == "__main__":
#     s = Solution()
#     print(s.containsDuplicate([1, 2, 3, 1]))  # True
#     print(s.containsDuplicate([1, 2, 3, 4]))  # False


#77
# def combine(n, k):
#     result = []

#     def backtrack(start, path):
#         if len(path) == k:
#             result.append(path[:])
#             return

#         for i in range(start, n + 1):
#             path.append(i)
#             backtrack(i + 1, path)
#             path.pop()

#     backtrack(1, [])
#     return result


# print(combine(4, 2))


#342,231,326


# def isPowerOfFour(n):
#     if n <= 0:
#         return False
    
#     while n % 4 == 0:
#         n = n // 4
    
#     return n == 1
# def isPowerOfTwo(n):
#     if n <= 0:
#         return False
    
#     while n % 2 == 0:
#         n = n // 2
    
#     return n == 1
# def isPowerOfThree(n):
#     if n <= 0:
#         return False
    
#     while n % 3 == 0:
#         n = n // 3
    
#     return n == 1


# Test
# num = int(input("Enter number: "))
# print(isPowerOfThree(num))


# Test
# num = int(input("Enter number: "))
# print(isPowerOfTwo(num))


# Test
# num = int(input("Enter number: "))
# print(isPowerOfFour(num))

# 121
# prices = list(map(int, input("Enter stock prices separated by space: ").split()))

# if not prices:
#     print(0)
# else:
#     min_price = prices[0]
#     max_profit = 0

#     for price in prices:
#         if price < min_price:
#             min_price = price
#         else:
#             max_profit = max(max_profit, price - min_price)

#     print("Maximum profit:", max_profit)


# class student:
#     def details(self,name,marks):
#         if marks>40:
#             result="pass"
#             print(result)
#             print(name,marks)
#         else:
#             print("fail")
# s1=student()
# s2=student()
# s1.details("AAA",100)


#syntax
# class classname:
#     def method_name(self):
#         print("message")


#with constructor


# class student:
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks
#     def show_result(self):
#         if self.marks>=40:
#             result="pass"
#         else:
#             result="fail"
#         print("\nStudent name:",self.name)
#         print("Marks",self.marks)
#         print("result",result)
# name=input("Enter name:")
# marks=int(input("Enter marks"))
# s1=student(name,marks)
# s1.show_result()   

#Celsius to Fahrenheit

# class Celsius:
#     arr = [10, 20, 30, 40, 50]

#     def show_result(self):
#         for i in self.arr:
#             f = (i * 9/5) + 32
#             print(f)

# s1 = Celsius()
# s1.show_result()
