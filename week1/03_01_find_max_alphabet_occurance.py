
'''
input = "hello my name is sparta"

def find_max_occurred_alphabet(string):
    array = [0] * 26
    cnt = 0
    max=0
    for i in string:
        if not i.isalpha():
            continue
        arr_index = ord(i)-ord('a')
        array[arr_index] += 1
    for i in range(26):
        if array[i] > max:
            max = array[i]
            arr_indx = i
        max_index = cnt
    print(chr(ord('a')+arr_index))
    return array[max_index]


result = find_max_occurred_alphabet(input)
print(result)
'''

input = "hello my name is sparta"
#각 알파벳을 하나하나 비교하며 결과를 검사
def find_max_occurred_alphabet(string):
    alphabet_array = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    max_occurance = 0
    max_alphabet = alphabet_array[0]

    for alphabet in alphabet_array:
        occurance = 0
        for char in string:
            if char == alphabet:
                occurance += 1
        if occurance > max_occurance:
            max_occurance = occurance
            max_alphabet = alphabet
    return max_alphabet

result = find_max_occurred_alphabet(input)
print(result)


