def Input():
    while -1:
        inputString = input('Please enter two numbers.(Num1 Num2):') 
        inputStringSplite = inputString.split(' ')
        inputNumber = []
        for num in inputStringSplite:
            if num.isdecimal():
                inputNumber.append(int(num))
        if len(inputNumber) >= 2 and inputNumber[1] != 0:
            return inputNumber