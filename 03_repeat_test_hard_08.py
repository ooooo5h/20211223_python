import random

# 컴퓨터가 랜덤으로 3자리 숫자를 출력하자

# 3개의 숫자를 추가해주자
# 랜덤 1 ~ 9 + 중복은 허용하지 X

cpu_numbers = random.sample( range (1, 10), 3 ) 

# 테스트 : 출제되는 숫자들이 뭔지 확인해보자
print(cpu_numbers)