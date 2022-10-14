# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов
def open_file(f):
    val = open(f, 'r')
    ur = val.read()
    # print(ur)
    ur_split = ur.split(' + ')
    ur_list = []
    for elem in range(len(ur_split)):
        ur_list.append(ur_split[elem][0:2])
    ur_list = [int(i) for i in ur_list]
    return ur_list

def sum_ur(val1,val2):
    sum_list = []
    for i in range(len(val1)):
        sum_list.append(f'{val1[i]+val2[i]}*x^{len(val1)-1-i}')
    sum_list = ' + '.join(map(str,sum_list))
    sum_list = sum_list.replace('x^0','')
    sum_list = sum_list.replace('x^1','x')
    sum_list = f'{sum_list} = 0'
    return sum_list

list1 = open_file('urav1.txt')
list2 = open_file('urav2.txt')
# print(sum_ur(list1,list2))
f = open('sum_uravnenie.txt','w')
f.write(sum_ur(list1,list2))
f.close