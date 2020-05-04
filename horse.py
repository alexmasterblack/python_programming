def check(all_steps):
    new_steps = []
    nums = {1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E', 6: 'F', 7: 'G', 8: 'H'}
    for i, j in all_steps:
        if i >= 1 and i <= 8 and j >= 1 and j <= 8:
            new_steps.append(str(nums.get(i)) + str(j))
    return sorted(new_steps)

def str_to_num(letter, num):
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    return (letters.index(letter) + 1, num)

def list_of_turns(step):
    step_letter, step_num = str_to_num(step[0], int(step[1]))

    all_steps = []
    all_steps.append((step_letter + 2, step_num + 1))
    all_steps.append((step_letter + 2, step_num - 1))
    all_steps.append((step_letter - 2, step_num + 1))
    all_steps.append((step_letter - 2, step_num - 1))
    all_steps.append((step_letter + 1, step_num + 2))
    all_steps.append((step_letter - 1, step_num + 2))
    all_steps.append((step_letter + 1, step_num - 2))
    all_steps.append((step_letter - 1, step_num - 2))
    return check(all_steps)

step = ' '.join(input()).split()

print(list_of_turns(step))