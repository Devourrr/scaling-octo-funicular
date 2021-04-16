#반복문 131~140
과일 = ["사과","귤","수박"]
for i in 과일:   # 리스트에 들어있는 문자열이 순서대로 변수idp 대입되어 한 라인에 하나씩 출력됩니다.
    print(i)
#리스트의 첫 번째 요소인 '사과'가 먼저 i 변수에 대입된 후 print(i) 문장을 수행한다. 
# 다음에 두 번째 요소 'two'가 i 변수에 대입된 후 print(i) 문장을 수행하고
# 리스트의 마지막 요소까지 이것을 반복한다.

for i in 과일:
    print("####")   # 리스트내 문자열 수만큼 ####수행

#  for문의 핵심은 "들여쓰기된 코드가 자료구조에 저장된 데이터 개수만큼 반복된다"


for i in ["A", "B", "C"]: # 마찬가지
    print(i)

for i in ["A","B","C"]:
    print("print:", i)

for i in ["A","B","C"]:
    b= i.lower()
    print("변환 :",b)

for i in [10,20,30]:
    print(i)

num = [10,20,30]
for i in num:
    print(i)

for i in [10,20,30]:
    print(i)
    print("----"*20)

print("+++"*3)
for i in [10,20,30]:
    print(i)

for i in [1,2,3,4]:
    print("---"*20)

list = [100,200,300]
for i in list:
    print(i+10)
#파이썬 인터프리터가 코드를 실행하는 순서를 익혀서, 한 번에 for문으로 작성할 수 있어야합니다.
# (100 바인딩 - 들여쓰기 코드 실행)
# (200 바인딩 - 들여쓰기 코드 실행)
# (300 바인딩 - 들여쓰기 코드 실행)

list = ["김밥","라면","튀김"]
for i in list:
    print("오늘의 메뉴:" + i) # for문 + 문자열 덧셈

list = ["SK하이닉스","삼성전자","LG전자"]
for i in list:      # for문 + len(변수)
    print(len(i))   #len(변수) 문자열의 원소개수 출력하는 내장함수

list = ['dog','cat','parrot']
for i in list:
    print(i, len(i))

for i in list:
    print(i[0]) # for 문 + 인덱싱

for i in [1,2,3]:
    print("3x", i)
    print("3x"+str(i))  # str(변수)는 변수를 문자열로 바꿈

for i in [1,2,3]:
    print(f"3x{i}={3*i}")

list = ["가","나","다","라"]
for i in list[::2]:
    print(i)
    
for i in list[::-1]:
    print(i)

list = [3,-20,-3,44]
for i in list:
    if i < 0:
        print(i)
    
for i in [3,100,23,44]:
    if i%3 == 0:
        print(i)

for i in [13,21,12,14,30,18]:
    if i<20:
        if i%3==0:
            print(i)

list = ["I","study","python","lanaguage","!"]
for i in list:
    if len(i) >= 3:
        print(i)

list = ["A","b","c","D"]    # isupper() 메서드는 대문자 여부를 판별합니다.
for i in list:
    if i.isupper()==True:
        print(i)

for i in list:
    if i.isupper()!=True:
        print(i)

list = ['dog','cat','parrot']
for i in list:
    print(i.upper())    #i.upper() 대문자로 변환 함수

list = ['hello.py','ex01.py', 'intro.hwp']
for i in list:
    i.split('.')
    print(i.split('.')[0])

list = ['intra.h','intra.c','define.h','run.py']
for i in list:
    if (i.split('.')[1] == 'i') and (i.split('.')[1] == 'c'): # 비교연산자 이중괄호처리
        print(i) #들여쓰기