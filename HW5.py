# Задача 1. Задайте список случайных чисел от 1 до 10, выведите все элементы больше 5. Используйте для решения лямбда-функцию.
# 2, 3, 4, 6, 7, 8 -> 6, 7, 8

import random

# lenght = int(input("Задайте длинну списка\n"))
# numbers = list(random.randint(1,10) for x in range(lenght))
# newlist = list(filter(lambda x: x>5, numbers))


# print(numbers)
# print(newlist)


# Задача 2. Дан список случайных чисел. Создайте список, в который попадают числа, 
# описывающие случайную возрастающую последовательность. Порядок элементов менять нельзя.
# [1, 5, 2, 3, 4, 6, 1, 7] = [1, 2, 3] или [2, 7] или [4, 6, 7] и т.д.


# lenght = int(input("Задайте длинну списка\n"))
# numbers = list(random.randint(1,10) for x in range(lenght))
# print(numbers)
# new_lenght = random.randint(2, lenght)
# for_random = list(range(0, lenght))
# indexes = sorted(random.sample(for_random, new_lenght))
# new_numbers = list(numbers[i] for i in indexes)
# answer = [new_numbers[0]]
# count = 0
# for i in range(1, new_lenght):
#     if new_numbers[i] > answer[count]:
#         answer.append(new_numbers[i])
#         count +=1
# print(answer)



# Задача 3. Задайте список случайных чисел от 1 до 10. Посчитайте, сколько всего совпадающих элементов есть в списке. 
# Удалите все повторяющиеся элементы.
# [1, 4, 2, 3, 4, 6, 1, 7] => 4 элемента совпадают Список уникальных элементов
# [1, 4, 2, 3, 6, 7]

# numbers = list(random.randint(1,10) for x in range(10))
# print(numbers)
# not_uniq = 0
# for i in range(0,10):
#     if numbers.count(numbers[i]) > 1 :
#         not_uniq += 1
# print(f'{not_uniq} элемента/ов повторяются')
# print(list(set(numbers)))


# Задача 4*. Создайте игру в крестики-нолики.

board = list(range(1,10))

def draw_board(board):
    print ("-" * 13)
    for i in range(3):
        print ("|", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|")
        print ("-" * 13)

def take_input(player_token):
    valid = False
    while not valid:
        player_answer = input("Куда поставим " + player_token+"? ")
        try:
            player_answer = int(player_answer)
        except:
            print ("Некорректный ввод. Вы уверены, что ввели число?")
            continue
        if player_answer >= 1 and player_answer <= 9:
            if (str(board[player_answer-1]) not in "XO"):
                board[player_answer-1] = player_token
                valid = True
            else:
                print ("Эта клеточка уже занята")
        else:
            print ("Некорректный ввод. Введите число от 1 до 9 чтобы походить.")

def check_win(board):
    win_coord = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
    for each in win_coord:
        if board[each[0]] == board[each[1]] == board[each[2]]:
            return board[each[0]]
    return False

def main(board):
    counter = 0
    win = False
    while not win:
        draw_board(board)
        if counter % 2 == 0:
            take_input("X")
        else:
            take_input("O")
        counter += 1
        if counter > 4:
            tmp = check_win(board)
            if tmp:
                print (tmp, "выиграл!")
                win = True
                break
        if counter == 9:
            print ("Ничья!")
            break
    draw_board(board)

main(board)