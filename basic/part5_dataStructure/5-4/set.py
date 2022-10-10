# 집합 (set)
# 중복 안됨, 순서 없음
my_set = {1,2,3,3,3}
print(my_set) # 1 2 3

java = {"유재석" , "김태호" , "양세형"}
python = set(["유재석" , "박명수"])

# 교집합 (java python 을 모두 할 수 있는 사람)

print(java & python)
print(java.intersection(python))

# 합집합 (java python 중 하나라도 할 수 있는 개발자)
print(java | python)
print(java.union(python)) # 김태호 박명수 유재석 양세형

# 차집합 (java는 할 수 있지만 파이쎤은 모르는 개발자)
print(java - python)
print(java.difference(python)) # 양세형 김태호

# python을 할 줄 아는 사람이 늘어남
python.add("김태호") # 값을 추가
print(python) # 박명수 김태호 유재석

# java 를 까먹음
java.remove("김태호") # 값을 빼는 것도 가능