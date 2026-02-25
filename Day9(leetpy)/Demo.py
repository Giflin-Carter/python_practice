
# import heapq

# pq = []
# heapq.heappush(pq, 3)
# heapq.heappush(pq, 1)
# heapq.heappush(pq, 2)

# print("priority queue:", pq)
# print("Removed:", heapq.heappop(pq))
# print("Removed:", heapq.heappop(pq))
# print("Removed:", heapq.heappop(pq))



# import heapq

# pq = []   

# heapq.heappush(pq, (2, "medium task"))
# heapq.heappush(pq, (1, "high task"))
# heapq.heappush(pq, (3, "low task"))

# while pq:
#     priority, task = heapq.heappop(pq)
#     print(priority, task)


#268
# nums = [3, 0, 1]
# n = len(nums)
# total = n * (n + 1) // 2
# array_sum = sum(nums)
# missing = total - array_sum
# print("Missing number is:", missing)


#83
# 83
# nums = [1, 1, 2, 3, 3]
# result = []
# for num in nums:
#     if num not in result:
#         result.append(num)
# print("After removing duplicates:", result)

 #557
# s = "Hello World"

# words = s.split(" ")

# result = ""

# for word in words:
#     result = result + word[::-1] + " "

# print(result.strip())