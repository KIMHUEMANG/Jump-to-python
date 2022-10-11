# while
customer = "토르"
index = 5

while index >= 1:
  print("{0}, 커피가 준비됨 {1} 번 남음".format(customer , index))
  index -= 1
  if index == 0:
    print("커피가 폐기처분 되었습니다.")


customer = "아이언맨"

# 무한루프
# while True :
#   print("{0}, 커피가 준비됨 호출 {1} 회".format(customer , index))
#   index += 1


customer = "토르"
person = "Unknown"

while person != customer :
  print("{0} 커피가 준비 되었습니다.".format(customer))
  person = input("이름이 어떻게 되세요?")

