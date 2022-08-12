numbers = [1,2,3,4,5,6,7,8,9,0]

reverseOrder = numbers[::-1]
primeNumbers = []
isPrime = True

for num in reverseOrder:                            
    if num % 2 == 1 and num > 1:
        
        primeNumbers.append(num)

        for x in range(2, numb):
            if x % numb == 0:
                primeNumbers.append(num)

    
print(primeNumbers)