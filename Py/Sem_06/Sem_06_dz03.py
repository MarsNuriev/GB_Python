# zip, filter, enumerate

arr = [i for i in range(10)]
print (arr)

arr_filter = list(filter(lambda x: x % 2 != 0, arr))
print(arr_filter)

arr_enum = list(enumerate(arr))
print(arr_enum)

arr_zip = list(zip(arr,arr_enum))
print(arr_zip)

