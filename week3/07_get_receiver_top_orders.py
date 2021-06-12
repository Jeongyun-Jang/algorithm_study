top_heights = [6, 9, 5, 7, 4]
#기본 [0,0,0,0,0]
#탑이 오른쪽에서 왼쪽으로 레이저를 쏨
#   <- <- <- <- <-
#    6  9  5  7  4
#[0,0,2,2,4] 레이저 신호를 받는 탑의 index 위치
#     9 9 7
#    6,9는 신호를 받지 못함 6의 왼쪽에 없고, 9는 가장 높아서

def get_receiver_top_orders(heights):
    answer = [0] * len(heights) #[0,0,0,0,0]
    while heights: #height가 빈상태가 아닐 때 까지 O(N^2)
        height = heights.pop()
        for idx in range(len(heights)-1,0,-1):
            if height[idx] > height:#왼쪽에 더 큰 값이 있는 경우
                answer[len(height)] = idx + 1 #answer[len(height)]즉 신호 보낸 index에 신호 받은게 몇번째에 있는지 값을 넣으면 됨
                break

    return


print(get_receiver_top_orders(top_heights))  # [0, 0, 2, 2, 4] 가 반환되어야 한다!