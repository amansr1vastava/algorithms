def compute_min_refills(distance,onFullTank,stop):
    refil = 0
    current = 0
    n = len(stop)
    stop.insert(0,0)
    stop.append(distance)
    while(current <= n):
        last = current
        while(current <= n and (stop[current +1]-stop[last])<= onFullTank):
            current +=1
        if(current == last):
            return -1
        if(current <= n):
            refil += 1
    return refil
distance = int(input())
onFullTank = int(input())
nGasStation = int(input())
stop = list(map(int, input().split()))
print(compute_min_refills(distance, onFullTank, stop))
