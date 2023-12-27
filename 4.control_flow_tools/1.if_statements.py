# 4.2. for Statements

x = 10

if x < 0:
    print('x는 0보다 작다')
    
elif x == 0:   # elif 는 전의 if 또는 elif 문이 거짓인 경우 진행됨
    print('x는 0이다') # 참인 경우 body 문 실행하고 밑의 elif, else 는 진행되지 않는다.
    
elif x >= 100:
    print('x는 100보다 크거나 같다')
    
elif x != 10:
    print('x는 10이 아니다')
    
else:
    print('위의 조건중 참이 없다')
    
    

# 다중 조건문, 들여쓰기 주의하여 볼것
x = 2

if x != 1:
    
    print('x는 1이 아니다')
    
    if x != 2:
        print('x는 1 또는 2 가 아니다')
        
        if x == 0:
            print('x는 1 또는 2 가 아닌 0 이다.')
            
        else:
            print('x는 1 또는 2 또는 0 이 아니다.')
            
    else:
        print('x는 1이 아닌 2다')
        
else:
    print('x는 1이 맞다')