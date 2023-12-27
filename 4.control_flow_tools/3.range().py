# 4.3. The range() Function


# range(start, end, step)
print(list(range(5,10))) # [5, 6, 7, 8, 9]
print('3의 배수', list(range(3 , 10, 3))) # [0, 3, 6, 9]
print(list(range(-10, -100, -10))) # [-10, -20, -30, -40, -50, -60, -70, -80, -90]
print('홀수', list(range(1, 10, 2)))
print('짝수', list(range(2, 10, 2)))

# 반복문 활용 인덱스 순회
numList = [100, 200, 300, 400, 500]
for i in range(len(numList)):
    print('index =',i, 'value =',numList[i])
# return
    # 0 100
    # 1 200
    # 2 300
    # 3 400
    # 4 500

# range(10) 와 range(0,10) 은 같다

print(sum(range(4))) # 0 + 1 + 2 + 3 = 6