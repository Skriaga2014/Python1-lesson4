'''
# Задание-3 (Ферзи):
# Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били
# друг друга. Вам дана расстановка 8 ферзей на доске.
# Определите, есть ли среди них пара бьющих друг друга.
# Программа получает на вход восемь пар чисел,
# каждое число от 1 до 8 — координаты 8 ферзей.
# Если ферзи не бьют друг друга, выведите слово NO, иначе выведите YES.
'''


from random import randint

def positions(x,y):
    poss = []
    for i in range(0,7):
        poss.append([x + i, y + i])
        poss.append([x - i, y - i])
        poss.append([x + i, y - i])
        poss.append([x - i, y + i])
        poss.append([x - i, y])
        poss.append([x - i, y])
        poss.append([x, y - i])
        poss.append([x, y - i])
    poss = list(set([str(i) for i in poss if 0<i[0]<9 and 0<i[1]<9]))

    return poss

list = [[randint(1,8),randint(1,8)] for i in range(8)]
print (list[0])

print (positions(list[0][0],list[0][1]))







