from random import uniform
def mutate_number(number):
    return number + uniform(-number, number)
