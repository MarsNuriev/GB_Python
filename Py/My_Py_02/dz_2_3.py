#3: Дан список заполненный произвольными целыми числами.
#Получите новый список, элементами которого будут только уникальные элементы исходного.
#    Примечание. Списки создайте вручную, например так:
my_list_1 = [2, 2, 5, 12, 8, 2, 12]
print(my_list_1)

#В этом случае ответ будет:
#[5, 8]

uniq_my_list = set(my_list_1)
print(list(uniq_my_list))

result = []
for i in my_list_1:
    if my_list_1.count(i)==1:
        result.append(i)
print(result)        