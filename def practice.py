def unique(list_): #функция выводит уникальные значения из списка
    new_list = []
    for i in list_:
        if i not in new_list:
            new_list.append(i)

    return new_list

print(unique([1,2,3,4,5,5,4]))

def find_max(list_): #функция ищет максимальное значение в списке
    max_ = list_[0]
    for i in list_:
        if i > max_:
            max_ = i
    return max_
print(find_max([100,200,123123,412231,412231.7,123,12,45,12,3,12,512,4,125,12,31,312,31]))
def find_min(list2_): #Функция ищет минимальное значение в списке
    min_ = list2_[0]
    for i in list2_:
        if i < min_:
            min_ = i
    return min_
print(find_min([213,2312,1,1,-2,1,4,12,4,1,3525,2342,523,12,213]))

def count_even(list_): #функция достаёт количество чётных чисел из списка
    counter = 0
    for i in list_:
        if i == 0:
            continue
        if i % 2 == 0:
            counter += 1
    return counter

print(count_even([1,2,3,4,5,6,8,10,22,213,421,41,25,1,23,222]))

a = []
b = {}
c = 1
d = 1.1
e = True
print(type.(a, b, c))

