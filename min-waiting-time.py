#%%
def minimumWaitingTime(queries):
    queries.sort()
    sum = 0
    for i in range(len(queries)):
        sum += queries[i] * (len(queries) - 1 - i)
    return sum

#%%
# driver code
queries = [3,2,1,2,6] # output should be 17
ans = minimumWaitingTime(queries)
print(ans)
# %%
