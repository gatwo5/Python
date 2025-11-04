start = int(input('Start: '))
end = int(input('End: '))
hayDivisor = False
divisor = 0

for i in range(start, end+1):
    divisor = i - 1
    hayDivisor = False

    while (not hayDivisor and divisor > 1):
        if (i % divisor == 0):
            hayDivisor = True
        divisor -= 1

    if (not hayDivisor):
        print(i)
