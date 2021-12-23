import random

# 컴퓨터가 랜덤으로 3자리 숫자를 출력하자

# 3개의 숫자를 추가해주자
# 랜덤 1 ~ 9 + 중복은 허용하지 X

cpu_numbers = random.sample( range (1, 10), 3 ) 

# 테스트 : 출제되는 숫자들이 뭔지 확인해보자
print(cpu_numbers)

# 정답을 맞출 때 까지 계속 반복 입력
# 언제 맞출지 모르니까 while
while True:
    input_num = int( input('3자리 숫자 입력 : '))
    
    # 숫자를 3자리로 나눠서 저장해 줄 목록을 생성
    # 456 들어오면 => [4,5,6] => [100의 자리, 10의 자리, 1의 자리]
    
    user_numbers = [input_num // 100 , input_num // 10 % 10, input_num % 10]
    print(user_numbers)
    
    # S와 B의 개수를 구하자
    strike_count = 0
    ball_count = 0
    
    # 내 숫자들과 문제 숫자들을 비교해서, S/B의 갯수 구하기
    # 목록을 보는데, index가 몇인지도 파악하면서 확인해야 위치가 같은 지 다른 지 판단 가능
 
    # for문을 돌면서, index / 목록내용물을 한꺼번에 받아내기
    for i, user_num in enumerate(user_numbers):
        for j, cpu_num in enumerate(cpu_numbers):
            if user_num == cpu_num:
                if i == j :
                    strike_count + 1
                else:
                    ball_count += 1
    
    # 구해진 S/B의 갯수 출력
    print(f'{strike_count}S {ball_count}B 입니다.')
    
    # 3S라면 게임종료(축하합니다! 정답을 맞췄습니다.)
    if strike_count == 3:
        print(f'축하합니다! 정답을 맞췄습니다.')
        break