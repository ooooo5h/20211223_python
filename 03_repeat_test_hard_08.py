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