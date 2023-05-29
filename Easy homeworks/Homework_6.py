import random
x = 100
y = 200
z = 250
cost = 300
def subscription(x,y,z, cost):
    Arg: x(float)
    Arg: y(float) 
    Arg: z(float)
    Arg: cost(float)
    returns: tuple [float, float]
    nums = [x,y,z]
    nums.sort (reverse=True)
    best_sum = 0 
    result = None
    for i in range (len(nums)-1):
        for j in range (i+1, len(nums)):
            s = nums[i] + nums [j]
    if s >= cost and (result is None or s < best_sum):
        best_sum = s 
    result = (nums[i], nums [j])
    return result
print(subscription(x, y, z, cost))

    
