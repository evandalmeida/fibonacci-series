def fibonacci(num):

    if num == 0:
        return 0

    elif num == 1:
        return 1

    else:
        a = 0
        b = 1
        
        for i in range(2, num +1):
            next_num = a + b
            a = b
            b = next_num
        
        return b
    

print(fibonacci(10))  # Output: 55
print(fibonacci(5))   # Output: 5
print(fibonacci(-1))  # Output: Invalid input