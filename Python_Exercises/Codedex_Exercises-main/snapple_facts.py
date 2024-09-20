import random

fun_fact_dict = {
    0 : 'Flamingos turn pink from eating shrimps',
    1 : 'The only food that doesn´t spoil is honey',
    2 : 'A shrimp can only swim backwards',
    3 : 'A taste bud´s life span is about 10 days',
    4 : 'It is impossible to sneeze while sleeping',
    5 : 'It is illegal to sing off-key in North Carolina'
}
num = random.randint(0,5)

if num == 5:
    print(fun_fact_dict[num])
elif num == 4:
    print(fun_fact_dict[num])
elif num == 3:
    print(fun_fact_dict[num])
elif num == 2:
    print(fun_fact_dict[num])
elif num == 1:
    print(fun_fact_dict[num])
elif num == 0:
    print(fun_fact_dict[num])