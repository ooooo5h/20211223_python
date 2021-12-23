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

win_num_list = []

for i in range(6):
    # 제대로 된 숫자가 나올 때 까지 무한 반복
    while True:
        
        # 조건1 : 1~45는 랜덤의 범위를 지정하면 해결됨
        # 조건2 : 중복은 여전히 검사를 해야하니까 조건문 필요
        
        # 조건1은 해결
        random_num = random.randint(1,45)
        
        # 조건2 
        # 이미 뽑힌 숫자 안에 없어야지 ok로 기본셋팅
        is_dupl_ok = random_num not in win_num_list
        
        if is_dupl_ok :
            # 통과했다면, 목록에 뽑아낸 랜덤값을 추가
            win_num_list.append(random_num)
            break   # 무한반복 탈출해서, 다음 숫자 뽑으러 가자
        
# 당첨 번호 목록을 확인해보자
print(f'당첨번호들 : {win_num_list}')