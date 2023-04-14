from queue import PriorityQueue
def solution(program):
    answer = [0] * 11
    program = sorted(program, key= lambda x: (x[1],x[0]))
    queue = PriorityQueue()
    queue.put(program[0])
    cnt_time =program[0][1]
    idx = 1
    len_program = len(program)
    duration = 0
    while idx<len_program or queue.empty() ==False:
        if queue.empty() == True:
            queue.put(program[idx])
            cnt_time = program[idx][1]
            idx+=1
            continue
        pri, start_time, duration = queue.get()
        answer[pri] += cnt_time-start_time
        cnt_time += duration
        while idx<len_program and program[idx][1] <= cnt_time:
            queue.put(program[idx])
            idx+=1
    answer[0]=cnt_time
    return answer