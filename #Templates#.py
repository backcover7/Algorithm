#DP
dp = ...
# create dp array
# add padding if needed
dp[0][0] = ...
# init dp arrray
# base case
for i ...
    for j ...
        ...
        dp[i][j] = ...
        # transition
return dp[n][m]

# Recursion with memroization
mem = ...
# create mem dict or use __init__ to create
def dp(i, j, ...)
    if base_case(i, j): return ...
    # base_case
    if (i, j) not int mem:
        mem[(i,j)] = ...
        # transition
    return mem[(i, j)]
return dp(n, m)

# Backtrack
def backtrack(i,n, paramas...):
    if i == n:
        return ans
    else:
        backtrack()...
result = []
backtrack(i, n, params...)
return result

#Divide and conquer
def divide(array, ...):
    if least_condition: return sth
    mid = len(lists) // 2
    l = self.divide(lists[:mid])
    r = self.divide(lists[mid:])
    return self.subproblem()

def subproblem():
    ...

# slow runner and fast runner