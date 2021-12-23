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
    # Bubble sort 코드 참고해보기..
    

    
    # 구해진 S/B의 갯수 출력
    print(f'{strike_count}S {ball_count}B 입니다.')