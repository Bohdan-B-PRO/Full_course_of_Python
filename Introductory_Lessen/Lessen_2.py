# Data structure, variability

# TUPLE
# x = (int, float)
# print(type(x))
#
# numbers = (1, 2, 3, 9)
# print(numbers)
#
# words = ("hello", "world", "number")
# print(words)
#
# tuple_of_any = (1, 2, 3, "one", "two", "three", True, False)
# print(tuple_of_any)
#
# tuple_of_tuple = (numbers, words, tuple_of_any)
# print(tuple_of_tuple)
#
# print(len(numbers))
# print(numbers[2])
# print(numbers[2:4])
# print(numbers[:])
# print(numbers == numbers[:])
#
# print(words[1])
# word = words[1]
# print(word)
# print(word[2:4])
# print(words[1][2:5])
#
# print(tuple_of_tuple[2])
# print(tuple_of_tuple[1:2])
# print(tuple_of_tuple[2][5])
# print(tuple_of_tuple[2][2:5])
#
# a, b, c, d = numbers
# print(a, b, c, d)
# c, d = d, c
# print(c, d)
# a, b = c, d
# print(a, b)


# LIST
# list_of_string = ["abc", "def", "ghi"]
# print(list_of_string)
#
# t_of_s = tuple(list_of_string)
# print(t_of_s)
#
# print(list_of_string == t_of_s)
#
# # Присвоение последнего элемента
# print(list_of_string[2])
# list_of_string.append("jkl")
# print(list_of_string)
# print(id(list_of_string))
# list_of_string.append("mno")
# print(id(list_of_string))
#
# # Изменяемость происхдит по ссылке
# another_list = list_of_string
# print(another_list)
# another_list.append("pqr")
# print(another_list)
# print(list_of_string)
#
# # Проверка по id и сравнения
# print(id(list_of_string))
# print(id(another_list))
# print(another_list == list_of_string)
#
# # Удаление последнего элемента
# print(list_of_string.pop())
# print(list_of_string, another_list)
#
# # Корипрование элементов
# # Первый способ
# third_list = list_of_string[:]
# print(third_list)
#
# # Второй способ
# list4 = list(third_list)
# print(list4)
#
# # Сравение
# print(list_of_string is third_list)
# print(list4 == third_list)
# # Сравнения таждествености
# print(third_list == list_of_string)
# print(list4 is third_list)
#
#
# # Проверка по id, они должны быть разные!
# print(id(third_list), id(list_of_string))
#
# third_list.append("qwerty")
# list_of_string.append("spam")
# print(list_of_string, another_list)
# print(third_list)
#
# list4.append("abc")
# third_list.append("def")
# print(list4, third_list)
#
# # Умножения списка
# print(third_list * 2, third_list[3] * 3)
#
# # Измененик списка по индексам
# third_list[2] = ["Hello"]
# print(third_list)
# third_list[2:6] = ["spam", "eggs"]
# print(third_list)
#
# list_of_any = [1, 2, "a", "b", [1, 3], (5, 6), True]
# print(list_of_any)
# print(list_of_any[4], list_of_any[5])
# list_of_any[4].append(5)
# print(list_of_any)
#
# t_of_n = (1, 3, [5, 7], "word", "hello")
# print(type(t_of_n))
#
# t_of_n[2].append(9)
# print(t_of_n)
#
# list5 = third_list + list4
# print(list5)
# print(list5[::2])
# print(list5[::-1])
# print(list5[8:3:-1])
#
# hello_string = "hello world"
# print(hello_string[::-1])


# DICTIONARY
# numbers_dict = {
#     1: "one",
#     2: "two"
# }
# print(numbers_dict[1])
#
# # Добавление в список
# numbers_dict["one"] = 1
# print(numbers_dict)

# my_dict = {
#     (): "empty tuple",
#     1: "this is one",
#     "odin": "another one",
#     (1, 2): "a pair",
#     "data": {
#         "spam": "eggs"
#     },
#     "list_of_odds": [1, 3, 5],
#     "list_of_numbers": [1, 3, 5],
#     "numbers": [1, 3]
# }
# print(my_dict)
# print(my_dict[()])
# print(my_dict[1])
# print(my_dict[1, 2])
# print(my_dict["data"])
# print(my_dict["list_of_odds"].append(7))
# print(my_dict["list_of_numbers"].pop())
# print(my_dict["numbers"].append(0))
#
# my_dict["data"]["foo"] = "bar"
# print(my_dict["data"])
# my_dict["data"]["another_dict"] = {"spam and eggs": "yes please"}
# print(my_dict["data"]["another_dict"])


# Множество
# my_set = set()
# print(my_set, type(set()))
#
# my_set.add(1)
# print(my_set)
#
# my_set.add(2)
# print(my_set)
#
# my_set.add(0)
# print(my_set)
#
# my_set.add("spam")
# print(my_set)
#
# my_set.add((True, False))
# print(my_set)

print([s for s in "hello"])
print(list("hello"))
print({s: ord(s) for s in "hello"})

















