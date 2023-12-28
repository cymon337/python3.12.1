# 4.4. break and continue Statements, and else Clauses on Loops


for n in range(2, 10):
    print('상위 for문 진행중')
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            
            print('break')
            break # 현재 진행중인 반복문이 종료된다.
            print('after break') # 출력되지 않는다.
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')
        
        
print('continue 테스트')

for num in range(2, 10):
    if num % 2 == 0:
        print("Found an even number", num)
        continue # 이 아래 skip 하고 진행중인 반복문 다음단계로 계속 진행, 다음 num 수행
        print('after continue') # 출력되지 않는다. 
    print("Found an odd number", num)
    
# break 반복문이 종료되어 모든 범위를 순회하지 않는다.
# continue 반복문이 다음단계부터 지속된다. 모든 범위를 순회한다.