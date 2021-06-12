input = "abadabac"
def find_not_repeating_character(string):
    alphabet_occurrence_array = [0] * 26
    for char in string:
        if not char.isalpha():
            continue
        arr_index = ord(char) - ord('a')
        alphabet_occurrence_array[arr_index] += 1
    not_repeating_character_array = []
    for index in range(len(alphabet_occurrence_array)):
        alphabet_occurrence = alphabet_occurrence_array[index]
        if alphabet_occurrence == 1: #한번만 있었던 값
            not_repeating_character_array.append(chr(index+ord('a')))
    print(not_repeating_character_array)#[c,d] alphabet_occurrence_array에서 불러오니까 값이 알파벳 순으로 담김 so 아래 for문으로 문자열 순으로 확인해줘야함
    "abacabad"
    print(not_repeating_character_array[0])
    for char in string: #string에서 값을 찾아야한다.
        if char in not_repeating_character_array:
            return char

result = find_not_repeating_character(input)
print(result)