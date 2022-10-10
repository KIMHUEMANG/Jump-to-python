# 자료구조의 변경

#커피숍
menu = {"커피" , "우유" , "주스"}
print(menu , type(menu)) # {} class 'set'

menu = list(menu)
print(menu, type(menu)) # [] class "list"

menu = tuple(menu)
print(menu, type(menu)) # () class "tuple"

# 자료구조의 형을 괄호로 감싸줌으로써 변경 가능하다.