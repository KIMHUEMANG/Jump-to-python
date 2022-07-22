from random import *

print(int(random() * 10)); # 0 ~ 10

print(randrange(1,46)) # 1 ~ 46 미만의 임의의 값 생성

print(randint(1,45)) # 1 ~ 45이하의 임의의 값 생성


# quiz ) 오프라인 스터디 모임 일수 정하기
# 조건 1 : 랜덤한 날짜 뽑기
# 조건 2 : 월별 날짜는 다름을 감안하여 최소 일수인 28일 이내로 정함.
# 조건 3 : 매월 1 ~ 3일은 스터디 준비때문에 제외
day = randint(4,28);

print('오프라인 스터디 모임 날짜는 매월' , str(day) , '일로 선정되었습니다.');