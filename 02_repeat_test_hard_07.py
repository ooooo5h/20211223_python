# 6개의 숫자 입력받기

# 6개의 숫자가 담길 list 생성
my_num_list = []


# for로 6번 반복하면서 숫자를 넣어주기
for i in range(6):
    
    # 알맞은 숫자가 올 때까지, 해당 위치의 숫자를 계속 반복해서 입력받아야함
    # 무한 반복 => 제대로 된 숫자면 break   
    while True:    
        input_num = int(input(f'{i+1}번째 숫자 입력 : '))
        
        # 받은 숫자가 목록에 추가해도 되는 숫자인가? 검사해보고 => 통과하면 추가해주는걸로 변경
        # 검사 1 : 1~45 이내의 숫자?
        is_range_ok = input_num in range(1, 46)    # bool값이 나올텐데, 그 값을 is_range_ok변수에 담아두자
        
        # 검사 2 : 이미 등록된 숫자? => 중복이 아니여야만 목록에 추가되게끔 코드 추가
        # my_num_list 내부의 숫자들을 하나씩 꺼내서
        # input_num과 같은 숫자를 발견하면 중복검사에서 빠꾸시키기
        is_duplicated = input_num in my_num_list        # 목록안에 입력한 숫자가 있냐
                
        # is_range_ok가 True이고, is_duplicated도 True일때만 목록에 추가
        if is_range_ok and not is_duplicated:
            # 입력받은 숫자를 목록에 추가
            my_num_list.append(input_num)            
            # 알맞은 숫자가 입력되었으면 탈출하고, 다음 숫자 받으러 가게끔
            break
    
# 목록에 잘 들어갔는지 test
print(my_num_list)


# 입력한 값들을 작은 수 ~ 큰 수 순서로 정리
# 파이썬 기능 대신, for문로 연습 => Bubble sort 작성

# 순서를 바꾸면서, 제일 큰 숫자를 뒤로 보내는 과정을 총 6번 반복한다(6개 자리 모두 정렬되게)
for i in range( len(my_num_list)):
    
    # 두 개의 숫자를 꺼내서 순서가 제대로 되었는지 확인하는 반복문
    # 순서가 반대라면, 그 둘의 위치를 서로 변경해주자
    
    # 돌려봤더니 프로그램이 죽는다 IndexError: list index out of range
    # j : 0 ~ 5까지   j+1 : 1 ~ 6 까지 간다    => 6칸짜리는 0~5만 존재함   따라서 j는 0 ~ 4 까지만 가라
    for j in range( len(my_num_list) - 1 ):
        if my_num_list[j] > my_num_list[j+1]:
            # 앞의 숫자가 더 큰 상황을 발견하면 순서를 바꿔줘야함
            back_up = my_num_list[j]
            my_num_list[j] = my_num_list[j+1]
            my_num_list[j+1] = back_up
            
# 정렬된 결과한번 확인해보자
print(my_num_list)