input = "011110"
#특정 규칙을 발견해 코드로 구현하는 문제
#모두다 1로 바꾸는건 두번 작업해야하는데, 모두다 영으로 바꾸는 것은 한번 작업하면 됨
#모두 0으로 만드는 방법에서 최소로 뒤집는 숫자: count_to_all_zero => 0->1로 전환되는 순간 count_to_all_one +=1
#모두 1으로 만드는 방법에서 최소로 뒤집는 숫자: count_to_all_one => 1->0로 전환되는 순간 count_to_all_zero +=1

#1)뒤집어질 때 즉 0-> 1, 1->0 때
#2)첫번째 원소가 0인지 1인지에 따라 숫자를 추가해줘야함
def find_count_to_turn_out_to_all_zero_or_all_one(string):
    count_to_all_zero = 0
    count_to_all_one = 0
    if string[0] == '0':
        count_to_all_one += 1
    if string[0] == '1':
        count_to_all_zero += 1

    for i in range(len(string)-1):
        if string[i] != string[i+1]: #1->0, 0->1
            if string[i+1] == '0':
                count_to_all_one += 1
            if string[i+1] == '1':
                count_to_all_zero += 1
    #print(count_to_all_one,count_to_all_zero)
    return min(count_to_all_one, count_to_all_zero) #count_to_all_one: 2, count_to_all_zero:1

result = find_count_to_turn_out_to_all_zero_or_all_one(input)
print(result)
