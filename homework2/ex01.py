'''
Name: Pun VireakRoth
Class M3
'''
def subtract(a , b):
    answer = a - b
    return answer

firstInput = int(input("a: "))
secondInput = int(input("b: "))

# call the substract function
print(f"{firstInput} - {secondInput} = {subtract(firstInput, secondInput)}")