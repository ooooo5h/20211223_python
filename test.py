import random

my_num_list = []

for i in range(6):
    
    while True:
        input_num = int(input(f'{i+1}번째 숫자 :'))
        
        is_range_ok = input_num in range(1,46)
        is_duplicated = input_num in my_num_list
                  
        if not is_duplicated and is_range_ok:
            my_num_list.append(input_num)         
            break
        
# 정렬
my_num_list.sort()
print(my_num_list)

# 정답번호 6개 생성
win_num_list = random.sample ( range(1, 46), 6)
# win_num_list = win_num_list.sort()    # sort() 기능은 리턴값이 없이, 그냥 그 값들 자체만 바꿔줌. 그래서 변수에 저장할 수 없음. 그래서 none으로 나옴
win_num_list.sort()
print(win_num_list)

correct_count = 0

for my_num in my_num_list:
    for win_num in win_num_list:
        if my_num == win_num:
            correct_count += 1
            
if correct_count == 6:
    print('1등 당첨')
elif correct_count == 5:
    print('임시 3등')
elif correct_count == 4:
    print('4등 당첨')
elif correct_count == 3:
    print('5등 당첨')
else:
    print('다음 기회에..')