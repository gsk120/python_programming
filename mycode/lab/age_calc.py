"""
나이 = 현재년도 - 태어난 년도 + 1
태어난 년도는 input() 함수를 사용하여 받는다.
"""
from datetime import datetime as dt
from datetime import date
print(dt.today().year)
print(dt.today().month)
cur_year = dt.today().year

print("태어난 년도를 입력하세요.")
birth_year = int(input())
age = cur_year - birth_year + 1
if 17 <= age < 20:
    print("고등학생 입니다.")
elif 20 <= age < 27:
    print("대학생 입니다.")
# PEP 8 파이썬 코드 가이드 (simplify) 연한 밑줄로 표시해줌
elif 20 <= age and age < 27:
    print("대학생 입니다.")
else:
    print("학생이 아닙니다.")