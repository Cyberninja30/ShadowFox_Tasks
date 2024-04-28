import random
six_count = 0
one_count = 0
two_sixes_in_a_row_count = 0

# Simulate rolling a six-sided die at least 20 times
rolls = []
for _ in range(20):
    roll = random.randint(1, 6)
    rolls.append(roll)

# Count occurrences
for i in range(len(rolls)):
    if rolls[i] == 6:
        six_count += 1
        if i > 0 and rolls[i - 1] == 6:
            two_sixes_in_a_row_count += 1
    elif rolls[i] == 1:
        one_count += 1

# Print result
print("Number of times rolled a 6:", six_count)
print("Number of times rolled a 1:", one_count)
print("Number of times rolled two 6s in a row:", two_sixes_in_a_row_count)
