new_steps = []

def num_to_str(letter_num, num):
    nums = {1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E', 6: 'F', 7: 'G', 8: 'H'}
    new_steps.append(str(nums.get(letter_num)) + str(num))

def check(all_steps):
    for i, j in all_steps:
        if i >= 1 and i <= 8 and j >= 1 and j <= 8:
            num_to_str(i, j)

def str_to_num(letter, num):
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    return (letters.index(letter) + 1, num)

def list_of_turns(letter, num):
    step_letter, step_num = str_to_num(letter, num)

    all_steps = []
    all_steps.append((step_letter + 2, step_num + 1))
    all_steps.append((step_letter + 2, step_num - 1))
    all_steps.append((step_letter - 2, step_num + 1))
    all_steps.append((step_letter - 2, step_num - 1))
    all_steps.append((step_letter + 1, step_num + 2))
    all_steps.append((step_letter - 1, step_num + 2))
    all_steps.append((step_letter + 1, step_num - 2))
    all_steps.append((step_letter - 1, step_num - 2))
    check(all_steps)

step = ' '.join(input()).split()

list_of_turns(step[0], int(step[1]))

print(sorted(new_steps))