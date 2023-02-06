# This code calculates the sum of all numbers that are divisible by 3 or 5 below 1000

total_x = 0
total_y = 0
total_z = 0

# Loop through all numbers that are divisible by 3
for i in range(334):
    x = 3 * i
    total_x += x

# Loop through all numbers that are divisible by 5
for k in range(200):
    y = 5 * k
    total_y += y

# Loop through all numbers that are divisible by 15
for j in range(67):
    z = 15 * j
    total_z += z

# The total sum is the sum of all numbers that are divisible by 3 or 5, minus the sum of all numbers that are divisible by 15
total = total_x + total_y - total_z
print(total)
