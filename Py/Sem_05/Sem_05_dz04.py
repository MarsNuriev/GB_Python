# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
# На сжатие входные данные: WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW
# Выходные данные: 12W1B12W3B24W1B14W


with open('file_for_encode.txt', 'w') as data:
    data.write('ABBCCCDDDDEEEEEEF')

with open('file_for_encode.txt', 'r') as data:
    my_text = data.readline()

def rle_encode(value):
    char = value[0]
    count = 1
    tmp_text = ''
    for i in range(1,len(value)):
        if value[i] == char:
            count = count + 1
        else:
            tmp_text += str(count) + char
            char = value[i]
            count = 1
    tmp_text = tmp_text + str(count) + char
    return tmp_text

def rle_decode(value_text):
    decoded_text = ''
    char_count = ''
    for i in range(len(value_text)):
        if value_text[i].isdigit():
            char_count += value_text[i]
            decoded_text += value_text[i+1] * int(char_count)
        else:
            char_count = ''
    print(decoded_text)

    return decoded_text


with open('file_for_decode.txt', 'w') as file:
    my_encoded_text = rle_encode(my_text)
    file.write(my_encoded_text)

with open('file_for_encode.txt', 'r') as file:
    my_decoded_text = file.readline()

with open('file_for_encode.txt', 'w') as file:
    my_decoded_text = rle_decode(my_encoded_text)
    file.write(my_decoded_text)
