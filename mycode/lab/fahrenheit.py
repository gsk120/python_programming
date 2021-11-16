# 섭씨를 화씨로 변환하는 함수
def fah_convert(celsius):
    return ((9/5)*float(celsius)) + 32

print("변환하고 싶은 섭씨 온도를 입력하세요.")
user_input = input()
print(type(user_input), user_input)
fah = fah_convert(user_input)

# print("섭씨온도 : " + float(user_input)) -> 에러 발생
print("섭씨온도 :", float(user_input))
print("화씨온도 : {0:.2f}".format(fah)) # format 함수를 사용하여 정적인 문자열을 치환 하는 방법
print(f"섭씨온도 : {user_input}")  # format 함수가 뒤에 쭉 늘어나는것이 불편하니 변수 형태로 치환하는 방법 (진화된 방법)
print(f"화씨온도 :{round(fah,2)}")
