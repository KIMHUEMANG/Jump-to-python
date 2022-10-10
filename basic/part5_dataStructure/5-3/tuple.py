# 튜플 key value 형식이지만 변경이 안됨

menu = ("돈까스" , "치즈까스")
print(menu[0])
print(menu[1])

# menu.add("생선까스") 튜플은 고정된 값이기 때문에 추가나 변경이 불가능

name = "김종국"
age = 20
hobby ="코딩"
print(name, age, hobby)

(name,age,hobby) = ("김종국" ,  20 , "코딩")
print(name , age ,hobby) # 김종국 20 코딩