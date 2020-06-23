

def get_optimal_value(capacity, weights, values):
    value = 0.
    index = list(range(len(values)))
    ratio = [v/w for v, w in zip(values, weights)]
    index.sort(key=lambda i: ratio[i], reverse=True)
    for i in index:
        if weights[i] <= capacity:
            value += values[i]
            capacity -= weights[i]
        else:
            value += values[i]*capacity/weights[i]
            break
    return value


n, capacity = map(int,input().split())
values = [0]*n
weights = [0]*n
for i in range(n):
    values[i],weights[i] = map(int,input().split())
opt_value = get_optimal_value(capacity, weights, values)
print("{:.4f}".format(opt_value))
