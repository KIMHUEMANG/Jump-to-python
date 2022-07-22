jumin = '060206-3456789'
print("성별 : " + jumin[7])
print("연 : " + jumin[0:2]) # 0 ~ 2 직전 까지
print("월 :" + jumin[2:4]) # 2 ~ 3 까지
print("일 :" + jumin[4:6]) # 4 ~ 5

print("생년월일 :" + jumin[:6]) # 처음부터 6 직전까지 (5까지)
print("뒤 7자리 :" + jumin[7:]) # 7 부터 끝까지
print('뒤 7자리 (뒤에서부터)' + jumin[-7:]) # 맨뒤에서 부터 끝까지