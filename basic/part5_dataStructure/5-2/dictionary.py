# 사전
# key value 형식 -> map과 같은 기능인듯?
cabinet = {3:"유재석" , 100:"김태호"} # 3번키에 "유재석" key:value

print(cabinet[3]) # 유재석
print(cabinet[100]) # 김태호

print(cabinet.get(3)) # 유재석
# print(cabinet[5]) 없는 키 값을 호출하면 오류를 발생 -> 프로그램 종료  
print(cabinet.get(5 , "사용가능")) # get을 사용하면 값이 없으면 none을 출력 , 뒤에 인자는 키의 값이 없으면 뒤의 인자값을 호출

print("hi")

# in을 사용하여 키값이 있는지 여부 판단가능
print(3 in cabinet) # True
print(5 in cabinet) # False

cabinet = {"A-3" : "유재석" , "B-100" : "김태호"}
# 키를 여러가지 자료형으로도 사용 가능

# 새손님
print(cabinet)
cabinet["c-20"] = "조세호" # c-20이라는 키가 없으면 새로 생성
cabinet["A-3"] = "김종국" # 키가 이미 있으면 업데이트

# 간 손님 del
del cabinet["A-3"] # A-3 에 대한 값을 삭제
print(cabinet)

# key들만 출력
print(cabinet.keys())

# value들만 출력
print(cabinet.values())

# key, value 쌍으로 출력
print(cabinet.items())

# 목욕탕 폐점
cabinet.clear() # 모든 값 삭제
print(cabinet) # {}