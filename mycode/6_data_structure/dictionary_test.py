"""
dictionary는 key:value 형태로 이루어진 데이터를 저장하는 자료구조
"""
# 딕셔너리는 중괄호 / 생성하기
my_dict = dict()
my_dict = {'name':'홍길동', 'age':20}

# 딕셔너리 값 조회 key로 조회
print(type(my_dict))
print(my_dict['name'])
# print(my_dict['hey']) # 없으면 컴파일 에러 발생

# 새로운 키값 추가
my_dict['address'] = '서울시'
for key, value in my_dict.items():
    print(key, value)

# get 함수로 조회하기 -> T/F로 리턴하기에 좀더 안전하다
result = my_dict.get('name1')
if result:
    print(result)
else:
    print("Key does not exist.")

# in은 key 존재여부 확인하는 방법
if 'name1' in my_dict:
    print('name key가 있습니다.')
else:
    print('name key가 없습니다.')
    