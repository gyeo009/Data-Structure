# chapter 1
# 자료구조를 배우기 위한 준비
# 클래스 생성과 리스트 기본

# 클래스 생성
class Student:                      # stdent 객체 생성자
    def __init__(self, name, id):   # self는 키워드가 아니라 걍 관례임, 어떤 이름이든 생성자의 첫 번째 인수 자리는 생성자 이름기능을 함
        # 인스턴스 변수
        self.name = name
        self.id = id

    def get_name(self):             # 게터 메소드
        return self.name
        
    def get_id(self):               # 게터 메소드
        return self.id


best = Student('Lee', 101)
print(best.get_name())
print(best.get_id())



# 리스트
# 파이썬은 리스트가 동적 배열로 구현되어있어 크기조절이 핏(fit)하게 자유자재다.

a = []
b = [None]*10
c = [40, 10, 70, 60]
print(c[0])
print(c[-1])    # 60 출력
c.pop()         # 리스트의 마지막 항목 제거
c.pop(0)        # 리스트의 첫 번째 인수(index 0) 제거
c.append(90)    # 리스트의 맨 뒤에 90 추가
                # 현재 리스트 상태 : {10, 70, 90}
print(len(c))   # 내장 함수인 len()은 리스트의 크기 리턴

# for문

# range의 형식
# range(N)                  # 10번
# range(시작(m), N)         # m에서 시작하여 10번
# range(시작(m), N, 증감(l))   # m에서 시작하여 l만큼 등차로 10번


# 의사 난수(Pseudo-random Number) 생성을 이용해 리스트 만들기와 프로그램의 실행시간을 측정하기

# 난수 생성
import random
import time

random.seed(time.time())
a = []
for i in range(100):
    a.append(random.randint(1, 1000))



# 프로그램의 실행시간 측정
# time.time()은 1970년 1월 1일 0시 0분 0초부터 현재 시작을 몇 초인지를 리턴
start_time = time.time()

for i in range(100):
    print(a[i])

print("--- %s seconds ---" % (time.time() - start_time))





## 내장함수

# ord('[char]') : 문자의 유니코드값을 리턴
# list(reversed([list])) : 역순으로 된 리스트를 리턴
# [list].reverse() : 리스트를 역순으로 만듬


## lambda 함수 : 함수의 리턴도없이 수행되는 함수, 1줄로 작성할 수 있을 때만 사용하는게 좋다.
# lambda 인자 : 식
# filter나 map 함수의 인자로 많이 사용된다.

c = [1, 5, 4, 6, 8, 11, 3, 12]
even = list(filter(lambda x: (x%2 == 0), c)) # c에서 짝수만 선택하여 리스트로 리턴
print(even)

ten_times = list(map(lambda x: x*10 , c)) # c의 각 숫자를 10배로 만들어 리턴
print(ten_times)

d = [[0,1,8], [7,2,2], [5,3,10], [1,4,5]]
d.sort(key = lambda x: x[2])            # d의 각 리스트의 마지막 숫자로 정렬
print(d)



# 함수의 마지막 부분에서 순환하는 것을 꼬리 순환(Tail Recursion)이라 하며, 꼬리 순환은 반복문으로 변환하는 것이 수행 속도
# 메모리 사용 측면에서 효율적이다(스택 메모리를 안쓰거등.)