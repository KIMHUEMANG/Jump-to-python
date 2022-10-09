# 1. 문자열

sentence = '나는 소년입니다'
print(sentence)
sentence2 = "파이썬은 쉬워요"
print(sentence2)

sentence3 =""" 
나는 소년이고, 
파이썬은 쉬워요
"""
print(sentence3) # 줄바꿈 되어 다 출력됨

# 2. 슬라이싱

jumin = "990120-1234567"

print("성별 " + jumin[7]) # 1
print("연 : " + jumin[0:2]) # 99 0 ~ 2 전까지 ( 0 ~ 1 )
print("월 : " + jumin[2 : 4]) # 01
print("일 : " + jumin[4 : 6]) # 20

print("생년월일 : " + jumin[:6]) # 처음부터 6 전까지 ( 0 ~ 5 )
print("뒤 7자리 : " + jumin[7:]) # 7 ~ 끝까지
print("뒤 7자리 (뒤에 부터) : " + jumin[-7 : ]) # 맨 뒤에서 7번째부터 끝까지

# 3. 문자열 처리 함수
python = "Python is Amazing"

print(python.lower()) # python is amazing  << 소문자로 변경
print(python.upper()) # PYTHON IS AMAZING << 대문자료 변경
print(python[0].isupper()) # True (대문자면 True 아니면 False)
print(len(python)) # 17
print(python.replace("Python" , "Java")) # Java is Amazing (원하는 문자 변경)

index =python.index("n") 
print(index) # 인자로 주어진 값이 문자열 몇번째 있는지 알려줌(첫번째로 있는)
print("n" , index + 1) # 스타트 위치 정해줄 수도 있음
print(index) # 15

print(python.find("Java")) # 원하는 값이 없으면 -1
# print(python.index("Java"))  원하는 값이 없으면 오류
print("hi")

print(python.count("n")) # 인자 값이 문자열에 몇개 들어있는지 알려줌

# 문자열 포맷
print("a" + "b") # ab
print("a","b") # a b

# 방법 1 (c언어랑 똑같은데 뒤에 &가 아닌 % 차이인듯)
print("나는 %d살 입니다." % 20) # 나는 20살 입니다.
print("나는 %s을 좋아해요" % "파이썬") #나는 파이썬을 좋아해요
print("Apple 은 %c 로 시작해요" % "A") # Apple은 A로 시작해요


print("나는 %s 색과 %s색을 좋아해요" %("파란" , "빨간")) # 나는 파란색과 빨간색을 좋아해요

# 방법 2 (format괄호 안의 값을 중괄호에 넣어줌)
print("나는 {}살 입니다.".format(20))
print("나는 {0}색과 {1}색을 좋아해요" .format("파란" , "빨간")) # 값 지정 가능 명시 안하면 순서대로
print("나는 {1}색과 {0}색을 좋아해요" .format("파란" , "빨간"))

# 방법 3
print("나는 {age}살이며, {color}색을 좋아해요".format(age = 20 , color = "빨간")) # 변수처럼 사용도 가능
print("나는 {age}살이며, {color}색을 좋아해요".format(color = "빨간" , age = 20))

# 방법 4 (v3.6 이상~)
age = 20
color = "빨간"

print(f"나는 {age}살이며, {color}색을 좋아해요") # f옆에 쓰면 실제 변수에 사용된 값을 갖다 쓸 수 있다.

# 5. 탈출 문자
print("백문이 불여일견 \n 백견이 불여일타") # \n 줄바꿈 .. 근데 이건 너무기본

# 저는 "김희망" 입니다
print("저는 \"김희망\"입니다.") # \를 통해(탈출문자) 큰따옴표 허용 (작은 따옴표 대체해도 될듯) 

# \\ : 문장 내에서는 \
print("PS C:\\Users\\USER\\Desktop\\front-end\\python>") # 내 경로 출력

# \r : 커서를 맨 앞으로 이동
print("Red Apple\rPine") # PineApple Pine이 "Red "를 대체

# \b : 백스페이스 (한 글자 삭제)
print("Redd\bApple") # RedApple

# \t : 탭
print("Red\t Apple") # Red  Apple