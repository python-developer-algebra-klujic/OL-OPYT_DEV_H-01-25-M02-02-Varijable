'''
Zatražite od korisnika unos dva broja.
Nakon unosa brojeva, ispišite:
    zbroj, razliku, umnožak, količnik (rezultat djeljnja),
    potenciranje te modulo unesenih brojeva
'''

# first_number = input('Upisite prvi broj: ') # 5 -> '5'
# second_number = input('Upisite drugi broj: ') # 3 -> '3'

# first_number = int(first_number) # '5' -> 5
# second_number = int(second_number) # '3' -> 3


# 1. izvrsi se funkcija input()
# 2. rezultat izvrsavanja funkcije input() se odmah proslijedi u funkciju int()
#           na konverziju u cijeli broj
# 3. rezultat konverzije se pohrani u varijablu first_number
# Sve se ponovi i za varijablu second_number
first_number = int(input('Upisite prvi broj: '))
second_number = int(input('Upisite drugi broj: '))


# '5' + '3' = '53'
# !!!NIJE broj 53 nego brojke petica i trojka jedna pored druge
sum = first_number + second_number

difference = first_number - second_number
multiplication = first_number * second_number
division = first_number / second_number
power = first_number ** second_number
modulo = first_number % second_number

# print('Prvi uneseni broj:', first_number)
# print('Drugi uneseni broj:', second_number)
print('Suma brojeva je:', sum)
print('Razlika brojeva je:', difference)
print('Umnozak brojeva je:', multiplication)
print('Rezultat dijeljenja brojeva je:', division)
print('Potencija brojeva je:', power)
print('Modulo brojeva je:', modulo)
