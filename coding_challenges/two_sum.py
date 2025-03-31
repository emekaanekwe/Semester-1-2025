'''
given an array of ints and a target int, 
return the indices that sum up to the target.

--CONSTRAINT--
cannot use the same indexed element twice 
'''
# Note: funct prog aims to avoid state mutation

def twoSum(target, nums):
    try:
        arr = []
        type(arr) == type(nums) 
    except: TypeError
    try:
        type(target) == int
    except: TypeError
    
    if len(nums) == 0:
        print("no solution")
        return
    else:                                                  # range(start, stop) 
        pairs = [(i,j) for i in range(len(nums)) for j in range(i+1, len(nums)) if nums[i]+nums[j] == target]
        print(pairs)
        return list(pairs[0] if pairs else [])
    
sol = twoSum(8, [1,3,5])
print("sol",sol)
# what am i operating on?
arr = [1,3,5]
n = 7
x = [(a,b) for a in range(len(arr)) for b in range(a+1,len(arr))]
'''
what is happening is:

 the length of arr is 3
 so check 3 times stating at index 0 using range
 then check 2 times starting at x[1] using range:
 1+3    3+5
 1+5
 
  a  b
  |  |
[ 1  3  5] [7]
'''