def choose_best_sum(t,k,ls):
    f = sorted(ls)
    d = {}
    sum = 0
    for i in range(len(f)-k+1):
        temp_l = []
        sum = 0
        for p in range(k):            
            q=i+p
            sum += f[q]
            temp_l.append(f[q])
        d[sum] = temp_l

    near = {}
    for key in d:
        diff = t-key
        near[diff] = key

    lowest = min(near.keys())
    sum_dist = near[lowest]
    return sum_dist


xs = [100, 76, 56, 44, 89, 73, 68, 56, 64, 123, 2333, 144, 50, 132, 123, 34, 89]
print(choose_best_sum(230, 4, xs))
print(choose_best_sum(430, 5, xs))
print(choose_best_sum(430, 8, xs))