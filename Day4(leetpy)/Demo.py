'''
#242
def isAnagram(s,t):
    if len(s)!=len(t):
        return False
    return sorted (s)==sorted(t)
s=input("Enter 1st string :")
t=input("Enter 2bd string :")
print("Are they anagram ?",isAnagram(s,t))


#70
def climbStairs(n: int) -> int:
    if n <= 2:
        return n
    
    prev2 = 1
    prev1 = 2
    
    for _ in range(3, n + 1):
        curr = prev1 + prev2
        prev2 = prev1
        prev1 = curr
    
    return prev1


#412
n = int(input("Enter number of steps: "))
print("Number of ways:", climbStairs(n))

def fizzbuzz(n):
    for i in range(1, n + 1):
        if i % 15 == 0:
            print("fizzbuzz")
        elif i % 3 == 0:
            print("fizz")
        elif i % 5 == 0:
            print("buzz")
        else:
            print(i)


n = int(input("Enter a number: "))
fizzbuzz(n)

#169
nums=[2,2,1,1,1,2,2]
count={}
for num in nums:
    count[num]=count.get(num,0)+1
majority=max (count,key=count.get)
print("majority element is :",majority)    

#1822
n=int(input("Enter n Value :"))
if n >0:
    print("positive")
elif n<0:
    print("negative")
else:
    print("Zero")


#58
def lengthOfLastWord(s: str) -> int:
    words = s.strip().split()
    if not words:
        return 0
    return len(words[-1])

s = input("Enter a string: ")
print("Length of last word:", lengthOfLastWord(s))


#349

nums1 = [4, 9, 5]
nums2 = [9, 4, 9, 8, 4]

print(list(set(nums1) & set(nums2)))


nums1 = [4, 9, 5]
nums2 = [9, 4, 9, 8, 4]

union_list = []

for num in nums1 + nums2:
    if num not in union_list:
        union_list.append(num)

print(union_list)

#21,88

def merge_sorted_lists(list1, list2):
    i, j = 0, 0
    result = []

    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            result.append(list1[i])
            i += 1
        else:
            result.append(list2[j])
            j += 1

    result.extend(list1[i:])
    result.extend(list2[j:])
    
    return result

# Test the program
nums1 = [1, 3, 5]
nums2 = [2, 4, 6]
print(merge_sorted_lists(nums1, nums2))

#14
def longestCommonPrefix(strs):
    if not strs:
        return ""
    
    prefix = strs[0]
    
    for s in strs[1:]:
        while not s.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""
    
    return prefix

if __name__ == "__main__":
    print(longestCommonPrefix(["flower","flow","flight"]))
    print(longestCommonPrefix(["dog","racecar","car"]))
    print(longestCommonPrefix(["interview","internet","internal"]))
 #258
def addDigits(num):
    if num == 0:
        return 0
    return 1 + (num - 1) % 9


if __name__ == "__main__":
    print(addDigits(38))
    print(addDigits(0))

#136

def singleNumber(nums):
    result = 0
    for num in nums:
        result ^= num   # XOR cancels duplicates
    return result


if __name__ == "__main__":
    nums = [4, 1, 2, 1, 2]
    answer = singleNumber(nums)
    print("Single number is:", answer)


#283


def moveZeroes(nums):
    insert_pos = 0

    for i in range(len(nums)):
        if nums[i] != 0:
            nums[insert_pos] = nums[i]
            insert_pos += 1

    while insert_pos < len(nums):
        nums[insert_pos] = 0
        insert_pos += 1


if __name__ == "__main__":
    nums = [0, 1, 0, 3, 12]
    moveZeroes(nums)
    print("After moving zeroes:", nums)'''












