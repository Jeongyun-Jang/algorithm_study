#최대 빈도수 알파벳 찾기
#ord() 사용
input = "hello my name is sparta"
def find_max_occurrence_alphabet(string):
    alphabet_occurrence_array = [0] * 26
    for i in string:
        if not i.isalpha():
            continue
        arr_index = ord(i)-ord('a')
        alphabet_occurrence_array[arr_index] += 1
    max_occurence = 0 #가장 많이 나온 알파벳
    max_alphabet_index = 0 ##alphabet_occurrence_array에서 가장 많이 나온 알파벳의 인덱스
    for index in range(len(alphabet_occurrence_array)):
        #index 0 -> alphabet_occurrence 3
        alphabet_occurrence = alphabet_occurrence_array[index]

        if alphabet_occurrence > max_occurence:
            max_alphabet_index = index #index를 가장 큰 인덱스 판단했기 때문
            max_occurence = alphabet_occurrence_array[max_alphabet_index]
    '''
        a->0
        a-> ord(a)-> 97-ord(a) = 0 (인덱스로 사용)
        
        0->a
        0->0(인덱스)+ord(a)->97(아스키 코드)->chr(97)->a  
    '''
    return chr(max_alphabet_index + ord('a'))
result = find_max_occurrence_alphabet(input)

print(result)
