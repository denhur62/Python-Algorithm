from heapq import heappush, heappop, heapify
def solution(menu, order, k):
    order_list =[]
    answer=0
    cur_answer =0
    wait_time =0
    for i in range(len(order)):
        if i==0:
            order_list.append([0,menu[order[i]]])
            wait_time = menu[order[i]]
            continue
        if i*k < wait_time:
            wait_time = wait_time + menu[order[i]]
            order_list.append([i*k, wait_time])
        else:
            wait_time = i*k+menu[order[i]]
            order_list.append([i*k,wait_time])
    heap = []
    print(order_list)
    for i in order_list:
        cur_answer = answer
        print(cur_answer, heap , i)
        if not heap:
            heappush(heap,[i[1],i[0]])
            answer = max( answer, 1)
            continue
        if heap[0][0] > i[0]:
            cur_answer+=1
        else:
            heappop(heap)
        heappush(heap,[i[1],i[0]])
        answer = max(cur_answer,answer)

    return answer

menu =[5,12,30]
order =	[2, 1, 0, 0, 0, 1, 0]
k =10
print(solution(menu,order, k))


