import random

d={
    1: "Eagle",
    2: "Back"
}

sequence = []

count_E=0
count_B=0
turns = 0

while count_E!=3 and count_B!=3:
    trial = random.randint(1, 2)
    sequence.append(d[trial])
    turns +=1
    if trial == 1:
        count_E +=1
        count_B = 0
    else:
        count_E = 0
        count_B +=1
print(f'turns {turns} and sequence: {sequence}')
print(f'count_E: {count_E} and count_B: {count_B}')