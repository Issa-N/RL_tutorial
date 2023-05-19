def Calc(inputNumber):
    result = []

    #calc addition
    result_add = inputNumber[0] + inputNumber[1]

    #calc substraction
    result_sub = inputNumber[0] - inputNumber[1]

    #calc multiplication
    result_mul = inputNumber[0] * inputNumber[1]

    #calc division
    result_div = inputNumber[0] / inputNumber[1]

    #append result
    result.append(result_add)
    result.append(result_sub)
    result.append(result_mul)
    result.append(result_div)

    return result
