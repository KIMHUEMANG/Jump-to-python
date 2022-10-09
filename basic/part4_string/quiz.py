# Quiz) 사이트 별로 비밀번호를 만들어 주는 프로그램

# 예) http://naver.com
# 규칙1 : http:// 부분은 제외 => naver.com
# 규칙2 : 처음 만나는 점(.) 이후 부분은 제외 => naver
# 규칙3 : 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e' 갯수 + "!" 로 구성

url = "http://naver.com"

password = url[7:]
password = password[:5]
passLen = len(password)
passEnumber = password.count('e')
password = password[:3] + str(passLen) + str(passEnumber) + "!"

print("생성된 비밀번호 : " + password)

# 다른 답안
url = "http://naver.com"
myStr = url.replace("http://" , "")
myStr = myStr[:myStr.index(".")]
password = myStr[:3] + str(len(myStr)) + str(myStr.count("e")) + "!" 

print(f"{url} 의 비밀번호는 {myStr} 입니다.")