sum_3 = 0

for i in range(0, 1000, 3):
  sum_3 = sum_3 + i
  
print(sum_3)
  
sum_5 = 0

for j in range(0, 1000, 5):
  sum_5 = sum_5 + j

print(sum_5)

sum_15 = 0

for k in range(0, 1000, 15):
  sum_15 = sum_15 + k

print(sum_15)



total_sum = sum_3 + sum_5 - sum_15
print(total_sum)
