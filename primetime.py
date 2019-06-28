def primetime(num1, num2):
    df = []
    for num in range (num1,num2):
        for i in range(2,num):
            if (num % i) == 0:
                    break
        else:
             df.append(str(num))

    return(df)