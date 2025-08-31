max_palindrome = 0
a = 0
b = 0

for i in range(100, 1000):
    for j in range(i, 1000):
        num = i * j
        if str(num) == str(num)[::-1]:  # check if palindrome
            if num > max_palindrome:
                max_palindrome = num
                a = i
                b = j

print(max_palindrome)
print(a, "*", b)
