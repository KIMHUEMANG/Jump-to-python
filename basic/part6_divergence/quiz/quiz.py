# 당신은 Cocoa 서비스를 이용하는 택시기사입니다.
# 50명의 승객과 매칭 기회가 있을 때, 총 탑승 승객 수를 구하는 프로그램을 작성하시오

# 조건 1 : 승객별 운행 소요 시간은 5 ~ 50분 사이의 난수
# 조건 2 : 당신은 소요 시간 5분 ~ 15분 사이의 승객만 매칭해야함

# 출력문 예제
# 1번째 손님 (소요시간 : 15분)
# 2번째 손님 (소요시간 : 50분)
# 3번째 손님 (소요시간 : 5분)
# ...
# 50번째 손님 (소요시간 : 16분)

# 총 탑승 승객 : 2분


#나의 풀이
from random import randint 

count = 0
for client_num in range(1 , 51) :
  randTime = randint(1,45)
  if 15 >= randTime >= 5 : # 탑승허용
    print("[O] {0}번째 손님 (소요시간 : {0}분".format(client_num , randTime))
    count += 1;
  else : # 탑승거절
    print("[ ] {0}번째 손님 (소요시간 : {0}분".format(client_num , randTime))

print("총 탑승 승객 : {0}".format(count))