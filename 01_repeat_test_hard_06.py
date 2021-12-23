### 1 : 필요한 변수 셋팅
# ex) 두 개의 정수 입력
# ex) 최소공배수를 저장해 둘 변수

num1 = int(input('첫 숫자 입력 : '))
num2 = int(input('두번째 숫자 입력 : '))

# 최소공배수 (least common multiple)
lcm = num1   # 둘 중 하나의 숫자에서 출발(연산횟수 줄이기)

# 최대공약수 (greatest common factor)
gcf = 0

### 2 : 결과변수에 답을 저장하기 위한 로직
# ex) for / while 등 반복, if / elif / else 조건

# 최소공배수 로직 먼저
# 공배수 : 공통된 배수 -> 숫자 % num1 == 0 and 숫자 % num2 == 0이면 num1과 num2의 배수
# 최소 : 공배수 중 제일 작은 수 -> 숫자를 늘려가면서 발견한 최초의 숫자

# 반복문을 몇번 돌려야할 지 모르겠다
# num1 * num2 값은 무조건 공배수란 이야기
# 몇번돌릴지 모른다 => 언제까지 돌려야할 지 발견 = 반복 범위가 명확한 반복문 => for로 변경
for i in range(num1, num1*num2+1):     
    # lcm += 1    로직 변경하자 lcm = num1로 설정시, lcm += 1 하면 num+1부터 검사하니까 오류발생
    
    if (i % num1 == 0) and (i % num2 == 0):
        # i가 늘어나다가, 공배수를 발견시 이 안으로 들어옴
        # 최초 발견된 공배수가 제일 작으니까 반복문 탈출하자
        # 발견한 공배수 i값을 lcm에 저장하자
        lcm = i
        break
    
### 3 : 결과 출력
# 상황에 따라 조건/반복 이용 출력

# lcm에는 발견된 최소공배수가 저장되어있다
print(f'최소 공배수 : {lcm}')