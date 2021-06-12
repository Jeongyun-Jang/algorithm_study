#str.isalpha()
#문자를 아스키코드로 변환 python char to ascii code ord()
def find_alphabet_occurrence_array(string):
    alphabet_occurrence_array = [0] * 26
    for i in string:
        if not i.isalpha():
            continue
        else:
            arr_index = ord(i)-ord('a')
            alphabet_occurrence_array[arr_index] += 1

    return alphabet_occurrence_array

print(find_alphabet_occurrence_array("hello my name is sparta"))