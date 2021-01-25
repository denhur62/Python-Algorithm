import sys

skill = 'CBD'
skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]
all_count = len(skill_trees)
seat = 0
count = 0
for i in skill_trees:
    for val in i:
        if val in skill and val == skill[seat]:
            seat += 1
        elif val in skill and val != skill[seat]:
            count += 1
            break
    seat = 0
print(all_count-count)
