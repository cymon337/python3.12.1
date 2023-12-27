# comment
# 한줄주석
var = 1 # 변수 할당 및 코드 옆 주석
var_text = '문자열' + "문자열2" # 문자열 따옴표 ', "

# 3.1.1. 숫자
print('=== 3.1.1. 숫자 ===')
# 4칙연산
print('4 basic operations = ', 2 + 2 - 50 + 5*6 + (32 + 2*1) / 4) # 더하기 + 빼기 - 곱 * 나누기 /
# division always returns a floating point number
# 정수형 int , 소수형 float 

# 나누기 / 
print(17 / 3)  # classic division returns a float
# return: 5.666666666666667
print(17 // 3)  # floor division discards the fractional part
# return: 5
print(17 % 3)  # the % operator returns the remainder of the division
# return: 2
print(5 * 3 + 2)  # floored quotient * divisor + remainder
# return: 17

# 거듭제곱 **
print(5**2) # 5 squared
# return: 25

# 변수에 값 대입 = 등호 사용
width = 10
height = 5 * 5
print(width * height) # 변수로 4칙연산
# return: 250

# 실수지원 서로다른 형 계싼시 정수를 실수로 변환
print(4 * 3.75 -1)
# return: 14.0

# 3.1.2. Text
print('=== 3.1.2. 문자 ===')

# type str, strings 이라고 부름
str1 = '문자열 tesxt :) !' + "text test"  # single & double qoutes
print(str1)
str2 = "2023" # 숫자도 '," 로 감싸져 있으면 문자
print(str2)

# escape \
escapeStr = "doesn\' \" \"" # \뒤에 qoutes 사용 가능
print(escapeStr)
newLine = '1 first line\n2 second line' # 개행, 줄바꿈 \n
print(newLine)  
print(r'C:\nasd\nasd\nasd') # r'' 붙여서 사용하면 raw string 으로 escape 적용 안되고 그대로 출력
    # return: C:\nasd\nasd\nasd
    
print("""
이렇게 ''' 따옴표 3개씩 ''' 사용하면
줄바꿔서 문자열 입력 가능
1줄
2줄
3줄
""")
print('문자열' + '더하기' + '이어붙이기') # return: 문자열더하기이어붙이기
print('#문자열곱하기반복'*3) # return: #문자열곱하기반복#문자열곱하기반복#문자열곱하기반복

print('문' '자' "이어" 
      "붙이기")
    # return: 문자이어붙이기 
    # 두개 이상의 연속 문자열 자동으로 이어붙여짐
var3 = '변수3'
print(var3 + '+문자') # return: 변수3+문자

stringIndex = '일이삼사오'
print(stringIndex[0], stringIndex[1], stringIndex[2], stringIndex[3], stringIndex[4])
    # return: 일 이 삼 사 오
    # 문자열 인덱스 가능 0부터시작
print(stringIndex[-1]) 
    # return: 오  
    # 음수는 끝에서부터 시작
print(stringIndex[-1]) 
print(stringIndex[0:3]) 
    # return: 일이삼
    # 0부터 3 (미포함) 전까지 / 입력 안하면 디폴트 [:] 0 부터 끝까지
print(stringIndex[-2:]) 
    # return: 사오
    # -2 부터 끝까지

#  +---+---+---+---+---+---+
#  | P | y | t | h | o | n |
#  +---+---+---+---+---+---+
#  0   1   2   3   4   5   6
# -6  -5  -4  -3  -2  -1

# 인덱스를 벗어나면 에러 IndexError: string index out of range
# print(stringIndex[38])
# slicing은 가능하다 해당 인덱스에 문자열이 없으면 공백출력
print(stringIndex[38:]) 
# 파이썬 문자열은 변경할 수 없다 TypeError: 'str' object does not support item assignment
# stringIndex[2] = '칠'
print(len(stringIndex)) # return: 5 # 문자열 길이 반환


# 3.1.3. List
print('=== 3.1.3. 리스트 ===')

# 대괄호 [] 사이에 쉼표 , 로 구분된 값 목록
strList = ['일','이','삼'] 
# 인덱싱, 슬라이싱 가능
print(strList[2], strList[1:3], strList[-1]) # return: 삼 ['이', '삼'] 삼
# 리스트 이어붙이기 가능
print(strList[1:3] + [1,2,3,4,5]) # return: ['이', '삼', 1, 2, 3, 4, 5]
# 리스트 가변, 내용 변경할 수 있음
strList[2] = 7
print(strList) # return: ['일', '이', 7]
# 리스트 끝에 원소 추가
strList.append('append')
print(strList) # return: ['일', '이', 7, 'append']
# 슬라이스에 대입, 삭제, 길이변경
대입 = [1,2,3,4,5]
대입[2:5] = ['이', '삼', '사'] # [1, 2, '이', '삼', '사'] 
삭제 = [1,2,3,4,5]
삭제[2:5] = [] # [1, 2]
길이변경 = [1,2,3,4,5]
길이변경[3:10] = [6,7,8,9,10,22,33,44,55,77,88] # [1, 2, 3, 6, 7, 8, 9, 10, 22, 33, 44, 55, 77, 88] 
# 슬라이싱은 인덱스에서 벗어나도 유연하게 대처하는게 특징
print(대입, 삭제, 길이변경)

# 다중 리스트 중첩 가능
matrix = [[[0,0,0],[0,0,1]],[[1,1,0],[1,1,1]]]
print(matrix[0],matrix[1])
print(matrix[0][0],matrix[0][1],matrix[1][0],matrix[1][1])

