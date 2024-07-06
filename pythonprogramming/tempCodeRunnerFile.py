count =0
sum =0
for num in range(100,200):
    if num % 7==0:
        count += 1
        sum += num
print(f"The number of integers greater than 100 and less than 200 that are divisible by 7 is: {count}")
print(f"The sum of all integers greater than 100 and less than 200 that are divisible by 7 is: {sum}")    