'''파이썬 300제'''
# 문자열 인덱싱
letters = 'python'
print(letters[0],letters[2])

license_plate = "24가 2210" #[]로 슬라이싱
print(license_plate[-4:])

string = "홀짝홀짝홀짝" 
print(string[::2]) # 슬라이싱 할 때 시작인덱스:끝인덱스:오프셋 을 지정할 수 있습니다

string = "python"
print(string[::-1]) # 오프셋이 -1이면 역순

# 문자열 치환 replace
phone_number = "010-1111-2222"
print(phone_number.replace("-","")) 
#  replace 메서드를 사용하면 문자열을 일부를 치환할 수 있습니다
# 문자열은 수정할 수 없는 자료형이므로 기존 문자열은 그대로 두고 치환된 새로운 문자열이 리턴
phone_number = "010-1111-2222"
phone_number1 = phone_number.replace("-","")
print(phone_number1)

#split 분리
url = "http://sharebook.kr"
url_split = url.split('.') #문자열로 표현된 url에서 .을 기준으로 분리합니다
print(url_split[-1])   # 분리된 url 중 마지막을 인덱싱하면 도메인만 출력할 수 있습니다.

lang = 'python'
# lang[0] = 'p'
print(lang) # str' object does not support item assignment # 문자열은 수정할 수 없습니다

string = 'abcdfe2a354a32a'
print(string.replace('a','A')) # replace 메서드

string = 'abcd'
string.replace('b',"B") # abcd가 그대로 출력됩니다. 왜냐하면 문자열은 변경할 수 없는 자료형이기 때문입니다
print(string) # replace 메서드를 사용하면 원본은 그대로 둔채로 변경된 새로운 문자열 객체를 리턴해줍니다.
 # 문자열 합치기
a = '3'
b = '4'
print (a+b)

#문자열 곱하기
t1 = 'python'
t2 = 'java'
t3 = t1+" " + t2 + " "
print(t3*4)

# 문자열 출력 
# % formating 사용
name1 = '김민수'
age1 = 10
name2 = "이철희" 
age2 = 13

print( "이름: %s 나이: %d"% (name1, age1) ) #   %s는 문자열 데이터 타입의 값
print( "이름: %s 나이: %d"% (name2, age2) ) #   %d는 정수형 데이터 타입의 값

# fotmat()메서드를 사용
print("이름 : {} 나이 :  {}".format(name1, age1))
print("이름: {}나이:{}".format(name2, age2))

# f string 사용 # 제일 편함
print(f"이름:{name1} 나이 : {age1}")
print(f"이름:{name2} 나이 : {age2}")

상장주식수 = "5,969,782,550" # 컴마제거후 정수 타입으로 변환
del_comma = 상장주식수.replace(",","")
types = int(del_comma) # 문자열 정수형으로 변환함수는 int
print(types,(type))

분기 = "2020/03(E) (IFRS연결"
print(분기[:7]) # 슬라이싱

data = "        삼성전자        "
print(data.strip())     # 공백제거메서드는 strip()

ticker = "btc_krw"  # upper()
print(ticker.upper()) #대문자로 치환하는 upper()메소드 호출 
ticker1 = "BTC_KRW"
print(ticker.lower()) # 소문자로 치환하는 lower()메소드 호출

word = "hello"
print(word.capitalize())    # capitalize() 메서드

file_name = "보고서.xlsx"
print(file_name.endswith("xlsx"))   # endswith("문자열") 판단메서드

file_name = "2020_보고서.xlsx"
print(file_name.startswith("2020")) # startswith("문자열") 판단메서드

a = "hello world"
print(a.split())    # split()메서드 사용 => 문자열에서 공백 기준으로 분리해줌

ticker = "btc_krw"
print(ticker.split("_"))

data = "039490  "
print(data.rstrip())   # rstrip() 메서드를 사용하면 오른쪽 공백이 제거된 새로운 문자열 객체가 반환됩니다.
#  그 값을 data라는 변수가 새로 바인딩합니다. 
#  기존의 공백이 포함된 문자열은 메모리에서 자동으로 삭제됩니다.


