'''파이썬 300제 분기문 101~120'''
# True 혹은 False를 갖는 데이터 타입은 무엇인가?
# boolean 타입
print(3 == 5)

x = 4
print(1<x<5)

print((3==3)and (4!=3))

# print(3=>4) # 지원하지 않는 연산자

if 4<3:
    print("Hello World")
else:
    print("Hi,there.")

if True:
    print("1") # if True는 결과가 참이다
    print("2")
else:
    print("3")

print("4")

if True: 
    if False:
        print("1")
        print("2")
    else:
        print("3")

else:
    print("4")

print("5")

# user = input("입력:")
# print(user*2)

user = input("숫자를 입력하세요:")
print(int(user)+10)

# 사용자로부터 하나의 숫자를 입력 받고 짝수/홀수를 판별하라.
odd_even =input("입력:")
if int(odd_even) % 2 == 0: # 변수의 정수입력값%2 ==0이면
    print("짝수")   #"짝수"출력
else:
    print("홀수") # 아닌 경우엔 "홀수" 출력

#사용자로부터 값을 입력받은 후 해당 값에 20을 더한 값을 출력하라. 
# 단 사용자가 입력한 값과 20을 더한 계산 값이 255를 초과하는 경우 255를 출력해야 한다.

users = input("숫자입력:")
num = 20 + int(users)
if num > 255:
    print(255)
else:
    print(num)

#사용자로부터 하나의 값을 입력받은 후 해당 값에 20을 뺀 값을 출력하라. 단 출력 값의 범위는 0~255이다. 
# 예를 들어 결괏값이 0보다 작은 값이되는 경우 0을 출력하고 255보다 큰 값이 되는 경우 255를 출력해야 한다.

a= input("숫자입력-20:")
number = int(a) - 20
if number<0:
    print(0)
elif number>255:
    print(255)
else:
    print(number)

# 사용자로부터 입력 받은 시간이 정각인지 판별하라

clock = input("현재시간:")
if clock[-2:] == "00":
    print("정각입니다")
else:
    print("정각이 아닙니다")
 
# 사용자로 입력받은 단어가 아래 fruit 리스트에 포함되어 있는지를 확인하라. 
# 포함되었다면 "정답입니다"를 아닐 경우 "오답입니다" 출력하라.

fruit = ["사과", "포도", "홍시"]
user = input("좋아하는 과일은?")
if user in fruit:
    print("정답입니다.")

else:
    print("오답입니다.")


#  투자 경고 종목 리스트가 있을 때 사용자로부터 종목명을 입력 받은 후 
# 해당 종목이 투자 경고 종목이라면 '투자 경고 종목입니다'를 
# 아니면 "투자 경고 종목이 아닙니다."를 출력하는 프로그램을 작성하라.

warn_investment_list = ["Microsoft", "Google", "Naver", "Kakao","Samsung","LG화학"]
종목 = input("종목명:")
if 종목 in warn_investment_list:
    print("투자 경고 종목입니다.")

else:
    print("투자 경고 종목이 아닙니다.")

# 아래와 같이 fruit 딕셔너리가 정의되어 있다. 
# 사용자가 입력한 값이 딕셔너리 키 (key) 값에 포함되었다면 "정답입니다"를 
# 아닐 경우 "오답입니다" 출력하라.

fruit = {"봄": "딸기", "여름":"토마토", "가을":"사과"}
key = input("사용자가 좋아하는 계절은?:")
if key in fruit:
    print("정답입니다")
else:
    print("오답입니다")

#사용자로부터 문자 한 개를 입력 받고, 소문자일 경우 대문자로,
#  대문자 일 경우, 소문자로 변경해서 출력하라.
# 힌트-1 :islower() 함수는 문자의 소문자 여부를 판별합니다. 
# 만약 소문자일 경우 True, 대문자일 경우 False를 반환합니다. 
# 힌트-2 : upper() 함수는 대문자로, lower() 함수는 소문자로 변경합니다.
word = input("문자를 입력하세요:")
if word.islower():
    print(word.upper())
else :
    print(word.lower())

# 점수 구간에 해당하는 학점이 아래와 같이 정의되어 있다. 
# 사용자로부터 score를 입력받아 학점을 출력하라. score: 83 grade is A
score = input("score입력시 grade 출력:")
if 81<=int(score)<=100:
    print("A")
elif 61<=int (score)<=80:
    print("B")
elif 41<=int (score)<=60:
    print("C")
elif 21<=int (score)<=40:
    print("D")
elif 0<=int (score)<=20:
    print("E")

money = {"달러":1167,"엔":1.096,"유로":1268,"위안":171}
user = input("입력:")
num, currency = user.split() #공백,줄바꿈 split은 변수를 기준으로 문자열 분리
print(float(num)*money[currency],"원") # 다시 이해해보기

# 사용자로부터 세 개의 숫자를 입력 받은 후 가장 큰 숫자를 출력하라.
num1 = input("input number1:")
num2 = input("input number2:")
num3 = input("input number3:")
num1 = int(num1)
num2 = int(num2)
num3 = int(num3)
if num1> num2 and num1>num3: # if 조건 and 조건
    print(num1)               # 출력1
elif num2 > num1 and num2>num3: # elif 조건 and 조건
    print(num2)                 # 출력2
else :                          #else 출력3
    print(num3)

# number = input("휴대전화 번호 입력:") # input()함수로 입력함수 생성
# num = number.split[0]("-") # 변수생성, 변수안에 split사용해서"-"문자열 구분 [:3]앞 세자리
# if num == "011":    #"num과 011"이 동일하다면
#     com = "skt"      # com = "skt"
# elif num == "016":
#     com = "KT"
# elif num == "019":
#     com = "LGU"
# else:
#     com = "알수없음"
# print(f"당신은 {com}사용자입니다")  # fstring"문자열{com}"

# 126우편번호는 5자리로 구성되는데, 앞의 세자리는 구를 나타낸다. 
# 예를들어, 강북구의 경우 010, 011, 012 세 자리로 시작한다.
# 사용자로 부터 5자리 우편번호를 입력받고 구를 판별하라
nums = input("우편번호 입력:")
nums = nums[:3]
if nums in ["010","011","012"]:
    print("강북구")
elif nums in ["013","014","015"]:
    print("도봉구")
elif nums in ["016","017","018","019"]:
    print("노원구")

#127 주민등록번호 뒷 자리 7자리 중 첫째 자리는 성별을 나타내는데, 
# 1, 3은 남자 2, 4는 여자를 의미한다. 
# 사용자로부터 13자리의 주민등록번호를 입력 받은 후 
# 성별 (남자, 여자)를 출력하는 프로그램을 작성하라.

number = input("주민등록번호 :")
number = number.split("-")[1]

if number[0] == "1" or number[0]=="3":
    print("male")
if number[0] == "2" or number[0]=="4":
    print("female")

#128주민등록번호의 뒷 자리 7자리 중 두번째와 세번째는 지역코드를 의미한다. 
# 주민 등록 번호를 입력 받은 후 출생지가 서울인지 아닌지 판단하는 코드를 작성하라
# 지역코드	출생지
# 00 ~ 08	서울
# 09 ~ 12	부산
주민번호 =input("주민등록번호:")
뒷자리 = 주민번호.split("-")[1]
if 0 <= int(뒷자리[1:3]) <= 8:
    print("서울입니다")
else : 
    print("서울이 아닙니다")

#129 주민등록번호는 13자리로 구성되는데 마지막 자리수는 주민등록번호의 유효성을 체크하는데 사용된다.
#먼저 앞에서부터 12자리의 숫자에 2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5를 차례로 곱한 뒤 그 값을 전부 더한다. 
#연산 결과 값을 11로 나누면 나머지가 나오는데 
#11에서 나머지를 뺀 값이 주민등록번호의 마지막 번호가 된다.
# 8 2 1 0 1 0 - 1 6 3 5 2 1 0
# x 2 3 4 5 6 7   8 9 2 3 4 5 
# -----------------------------
# 1차 계산: (8*2 + 2*3 + 1*4 + 0*5 + 1*6 + 0*7 + 1*8 + 6*9 + 3*2 + 5*3 + 2*4 + 1*5) = (128 % 11) = 7
# 2차 계산: 11 -7 = 4
# 다음과 같이 사용자로부터 주민등록번호를 입력받은 후 주민등록번호가 유효한지를 출력하는 프로그램을 작성하라.
num = input("주민등록번호 입력:")
math1 = int(num[0])*2 +int(num[1])*3 + int(num[2])*4 + int(num[3])*5 + int(num[4])*6 +\
int(num[5])*7  + int(num[7])*8 + int(num[8])*9 + int(num[9])*2 + int(num[10])*3 +\
int(num[11])*4 + int(num[12])*5

math2 = 11 - (math1 % 11)
math3 = str(math2) # 숫자를 문자열로 변환

if num[-1] == math3:
    print("유효한 주민등록번호입니다.")
else:
    print("유효하지 않은 주민등록번호입니다,")

#130 아래 코드는 비트코인의 가격 정보를 딕셔너리로 가져오는 코드이다.

import requests
btc = requests.get("https://api.bithumb.com/public/ticker/").json()['data']
# btc 딕셔너리 안에는 시가, 종가, 최고가, 최저가 등이 저장되어 있다. 
# 최고가와 최저가의 차이를 변동폭으로 정의할 때 
# (시가 + 변동폭)이 최고가 보다 높을 경우 "상승장", 그렇지 않은 경우 "하락장" 문자열을 출력하라.

# Key Name	Description
# opening_price	최근 24시간 내 시작 거래금액
# closing_price	최근 24시간 내 마지막 거래금액
# min_price	최근 24시간 내 최저 거래금액
# max_price	최근 24시간 내 최고 거래금액
최고가 = float(btc['max_price']) 
최저가 = float(btc['min_price']) # 변동폭 변수를 계산하기위해 float()함수를 이용하여 문자열을 실수로 변환
변동폭 = float(btc['max_price']) - float(btc['min_price']) # 변동폭 = 최고가 최저가 차이
# 80750000 - 78500000 = 2250000
시가 = float(btc['opening_price']) # 최고가 조건판단을 위해 문자열을 실수로 변환
# 시가 78880000
# (시가+ 변동폭) = 81130000 > 최고가 80750000
# 상승장 출력

if (시가 + 변동폭) > 최고가:
    print("상승장")
else:
    print("하락장")












