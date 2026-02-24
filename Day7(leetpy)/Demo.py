#118
# Num_row=int(input())
# triangle=[]
# for i in  range (Num_row):
#     row=[1]*(i+1) 

#     for j in range(1,1):
#         row[j] = triangle[i-i][j - 1]+ triangle [i-1][j]
#     triangle.append(row)
# for row in triangle:



#13
# def romanToInt(s: str) -> int:
#     roman_map = {
#         'I': 1, 'V': 5, 'X': 10, 'L': 50,
#         'C': 100, 'D': 500, 'M': 1000
#     }
    
#     total = 0
#     for i in range(len(s)):
#         # If current value is less than the next, subtract it
#         if i + 1 < len(s) and roman_map[s[i]] < roman_map[s[i + 1]]:
#             total -= roman_map[s[i]]
#         else:
#             total += roman_map[s[i]]
            
#     return total

# # Test
# print(romanToInt("MCMXCIV")) # 1994




# #168
# def maximumProduct(nums: list[int]) -> int:
#     nums.sort()
#     option1 = nums[-1] * nums[-2] * nums[-3]
#     option2 = nums[0] * nums[1] * nums[-1]
#     return max(option1, option2)

# print(maximumProduct([-10, -10, 1, 3]))


#26
# def removeDuplicates(nums: list[int]) -> int:
#     if not nums:
#         return 0
    
#     i = 0
#     for j in range(1, len(nums)):
#         if nums[j] != nums[i]:
#             i += 1
#             nums[i] = nums[j]
            
#     return i + 1

# # Local testing
# if __name__ == "__main__":
#     test_nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
#     count = removeDuplicates(test_nums)
#     print(f"Unique count: {count}")
#     print(f"Modified array: {test_nums[:count]}") 


#520

def detectCapitalUse(word: str) -> bool:
    cap_count = sum(1 for char in word if char.isupper())
    
    if cap_count == len(word) or cap_count == 0:
        return True
    if cap_count == 1 and word[0].isupper():
        return True
    return False

if __name__ == "__main__":
    print(detectCapitalUse("USA"))      # True
    print(detectCapitalUse("leetcode")) # True
    print(detectCapitalUse("Google"))   # True
    print(detectCapitalUse("FlaG"))     # False




    