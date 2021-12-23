import random 

# 6개의 숫자 입력받기

# 6개의 숫자가 담길 list 생성
my_num_list = []


# for로 6번 반복하면서 숫자를 넣어주기
# for i in range(6):
    
#     # 알맞은 숫자가 올 때까지, 해당 위치의 숫자를 계속 반복해서 입력받아야함
#     # 무한 반복 => 제대로 된 숫자면 break   
#     while True:    
#         input_num = int(input(f'{i+1}번째 숫자 입력 : '))
        
#         # 받은 숫자가 목록에 추가해도 되는 숫자인가? 검사해보고 => 통과하면 추가해주는걸로 변경
#         # 검사 1 : 1~45 이내의 숫자?
#         is_range_ok = input_num in range(1, 46)    # bool값이 나올텐데, 그 값을 is_range_ok변수에 담아두자
        
#         # 검사 2 : 이미 등록된 숫자? => 중복이 아니여야만 목록에 추가되게끔 코드 추가
#         # my_num_list 내부의 숫자들을 하나씩 꺼내서
#         # input_num과 같은 숫자를 발견하면 중복검사에서 빠꾸시키기
#         is_duplicated = input_num in my_num_list        # 목록안에 입력한 숫자가 있냐
                
#         # is_range_ok가 True이고, is_duplicated도 True일때만 목록에 추가
#         if is_range_ok and not is_duplicated:
#             # 입력받은 숫자를 목록에 추가
#             my_num_list.append(input_num)            
#             # 알맞은 숫자가 입력되었으면 탈출하고, 다음 숫자 받으러 가게끔
#             break

# 임시 - 고정된 6개 숫자를, 내 번호로 활용하자
my_num_list = [5,1,16,4,42,23]
    
# 목록에 잘 들어갔는지 test
print(my_num_list)

# 파이썬 list의 기능으로 정렬
my_num_list.sort()
            
# 정렬된 결과한번 확인해보자
print(my_num_list)

# 당첨번호 6개를 생성 (랜덤생성)

win_num_list = random.sample( range(1, 46), 6 )

win_num_list.sort()

print(f'당첨번호들 : {win_num_list}')

# 내 번호와 / 당첨번호 비교해서 같은 숫자가 몇개가 있나 확인해보자
# 반복문 중첩 활용

correct_count = 0

for my_num in my_num_list:
    
    for win_num in win_num_list:
        
        # 내 번호 하나를 들고 당첨번호랑 하나씩 보다가, 같은 걸 발견했다는 이야기
        if my_num == win_num:
            
            # 구해야할것 : 발견할때마다 맞춘 갯수 1개씩 증가
            correct_count += 1       
            
# correct_count에는 찾아낸 같은 숫자의 갯수가 담겨있다
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