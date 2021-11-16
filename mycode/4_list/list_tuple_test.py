# list : 대괄호
my_list1 = [20,30,40] # 이렇게 모으는 것을 packing 이라고 함
n1,n2,n3 = my_list1 # 이렇게 자르는 것을 un-packing 이라고 함
print(n1,n2,n3)
my_list2 = list()

# 맨 뒤에 추가
my_list1.append(10)
print(my_list1)
# 맨 뒤에 확장
my_list1.extend([50,60])
print(my_list1)
# 0번자리에 추가
my_list1.insert(0,10)
print(my_list1)
# 인덱스로 값 치환 가능
my_list1[2] = 100
print(my_list1)
print(my_list1[0:3]) # 0,1,2 출력 (문자열과 동일)

# set : 중복 허용하지 않기 (but list에서 변환 시 순서가 유지되지 않음)
my_set1 = set(my_list1)
print(my_set1)

# tuple은 read only 타입으로 변경 불가 (최초에 세팅 가능) / 속도가 빠름
# tuple : 소괄호
my_tuple1 = ()
my_tuple2 = tuple()
print(type(my_tuple1))
print(my_tuple1)
# my_tuple1[0] = 50

# int 와 tuple 차이
num1 = (3)
num2 = (3,)
print(type(num1), type(num2))

# tuple usage 용도 : 함수의 return 타입으로 많이 사용됨
def swap(a,b):
    return (b,a)

# tuple 리턴하는 함수에서 각 개별 변수로 받기 가능
a,b= swap(10,20)
print(a)
print(b)

# 문자열 타입 list 생성
cat_list = list('cat')
print(cat_list) # ['c', 'a', 't']

# 문자열 split 후 리스트에 저장
birth_day = "2021/11/16"
birth_list = birth_day.split('/')
print(birth_list)

# 값 포함하고 있는지 없는지
print('2021' in birth_list)
print('2021' not in birth_list)

if '2021' not in birth_list:
    print('not found')

