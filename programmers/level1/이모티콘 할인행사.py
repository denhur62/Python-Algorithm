from itertools import product, permutations

def solution(users, emoticons):
    sales = [10, 20, 30, 40]
    li=[]
    for i in emoticons:
        temp=[]
        for j in sales:
            temp2= product([i],[j])
            temp.append(*temp2)
        li.append(temp)
    li = product(*li)
    user_item_list=[]
    for i in li:
        user= 0
        last_price=0
        for (sale,price) in users:
            sm = 0
            for j in i:
                if j[1] >= sale:
                    sm+= j[0]- int(j[0]*j[1]*0.01)
            if price <=sm:
                user+=1
            else:
                last_price+=sm
        user_item_list.append([user,last_price])
    user_item_list.sort(key=lambda x:(-x[0],-x[1]))
    return user_item_list[0]


users = [[40, 2900], [23, 10000], [11, 5200], [5, 5900], [40, 3100], [27, 9200], [32, 6900]]
emotic =[1300, 1500, 1600, 4900]

print(solution(users,emotic))