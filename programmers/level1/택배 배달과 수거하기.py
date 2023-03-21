def solution(cap, n, deliveries, pickups):
    answer = 0
    dn = n-1
    pn = n-1
    temp =0
    if deliveries.count(0) + pickups.count(0) == 2*n:
        return 0
    while (dn!=-1 or pn!=-1):
        print(dn,pn)
        start_dn = dn+1
        start_pn = pn+1
        temp= cap
        while dn!=-1 and temp-deliveries[dn]>= 0:
            
            temp-=deliveries[dn]
            dn-=1
        if temp > 0:
            deliveries[dn]-=temp
        
        temp= cap
        while pn!=-1 and temp-pickups[pn] >= 0:
            temp-= pickups[pn]
            pn-=1
        if temp > 0:
            pickups[pn]-=temp
        
        answer += 2* max(start_dn,start_pn)
        
    return answer


print(solution(1,2,		[1,0],[0,0]))


