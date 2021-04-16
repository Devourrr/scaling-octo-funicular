'''파이썬 300제 84~98 딕셔너리'''

# 비어있는 딕셔너리
temp = {}

ice = {"메로나": 1000, "폴라포":1200, "빵빠레":1800}
ice["죠스바"] = 1200
ice["월드콘"] = 1500 # 딕셔너리 추가는 대괄호[]= 자료값
print(ice)

ice = {'메로나': 1000,
       '폴로포': 1200,
       '빵빠레': 1800,
       '죠스바': 1200,
       '월드콘': 1500}

print(ice["메로나"])  #딕셔너리 인덱싱 획득은 i[자료명]

ice["메로나"] = 1300 # 딕셔너리 수정 i[]=자료값
print(ice)

del ice["메로나"]   # 딕셔너리 인덱스 삭제 del i[]
print(ice)

# icecream = {'폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
# icecream['누가바']  # 딕셔너리에 없는 키 인덱싱은 에러발생


inventory = {"메로나":[300,20], "비비빅":[400,3], "죠스바":[250,100]}
print(inventory["메로나"][0])   # 딕셔너리 인덱싱 출력은 print(i[][])  대괄호로
print(inventory["메로나"][1])

inventory["월드콘"] = [500,7]   # 딕셔너리 수정
print(inventory)

icecream = {"탱크보이":1200, "폴라포":1200, "빵빠레":1800,"월드콘":1500,"메로나":1000}
print(list(icecream.keys()))    #keys()메서드
print(list(icecream.values()))  #values()메서드
print(sum(icecream.values()))   # sum(values())메서드

new_product = {'팥빙수':2700,'아맛나':1000}
icecream.update(new_product) # update 메서드 update(keys +values)
print(icecream)

