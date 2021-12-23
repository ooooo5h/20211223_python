# 6개의 숫자 입력받기

# 6개의 숫자가 담길 list 생성
my_num_list = []


# for로 6번 반복하면서 숫자를 넣어주기
for i in range(6):
    input_num = int(input(f'{i+1}번째 숫자 입력 : '))
    
    # 받은 숫자가 목록에 추가해도 되는 숫자인가? 검사해보고 => 통과하면 추가해주는걸로 변경
    # 검사 1 : 1~45 이내의 숫자?
    if 1 <= input_num <= 45:
        # 입력받은 숫자를 목록에 추가
        my_num_list.append(input_num)
    
# 목록에 잘 들어갔는지 test
print(my_num_list)