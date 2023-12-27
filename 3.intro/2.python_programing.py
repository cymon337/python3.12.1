# 3.2. 프로그래밍으로의 첫걸음
print('3.2. 프로그래밍으로의 첫걸음')

# 다중대입
a, b, c = 1, 2, 3

# 반복문

    # 판별식 a < 10 이 참인동안 반복 실행됨
while a < 10:
    # while loop body 들여쓰기
    print(a)
    a += b
    b += c
    print(a,b,c)

for i in range(10):
    print(i, end=',') # end 인자는 개행문자 제거, 출력을 다른문자열로 끝나게
# return: 0,1,2,3,4,5,6,7,8,9,