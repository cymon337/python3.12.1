# 4.7. Defining Functions

# 함수를 선언하여 임의 범위의 피보나치 수열 생성함수
def fib(n):    # write Fibonacci series up to n
    """Docstring: Print a Fibonacci series up to n."""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

# Now call the function we just defined:
fib(2000)
# return: 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597

# `def` 로 함수 정의 `함수이름(매개변수목록, 매개변수2, 매개변수3 ...)`
# 함수 본문의 첫 번째 열은 함수의 문서화 문자열(docstring)을 선택적으로 쓸 수 있다. docstring 쓰는 것이 좋은 습관!
# 함수 내에서 모든 변수 할당은 값을 로컬 심볼 테이블에 저장하며, 
# 변수 참조는 먼저 로컬 심볼 테이블을 찾은 다음, 둘러싼 함수의 로컬 심볼 테이블, 전역 심볼 테이블, 마지막으로 내장된 이름 테이블에서 찾습니다. 
# 전역 변수 및 둘러싸는 함수의 변수는 함수 내에서 직접 값에 할당될 수 없습니다 .
# 전역 변수의 경우 global 문으로 명명되거나, 둘러싸는 함수의 변수의 경우 nonlocal 문으로 명명되어야 함. 그러나 참조는 가능합니다.

# 함수 정의는 함수 이름을 현재 기호 테이블의 함수 개체와 연결합니다. 인터프리터는 해당 이름이 가리키는 객체를 사용자 정의 함수로 인식합니다.
print(fib)
# return: <function fib at 0x000001EA726FA2A0>

# 다른 이름도 동일한 함수 객체를 가리킬 수 있으며 함수에 액세스하는 데 사용될 수도 있습니다.
f = fib
f(100)
# return: 0 1 1 2 3 5 8 13 21 34 55 89

fib(0)

#  return 문이 없는 함수도 값은 반환: `None`
print(fib(0))

# 피보나치 수열을 return 하는 함수
def fib2(n):  # return Fibonacci series up to n
    """Return a list containing the Fibonacci series up to n."""
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)  # append() 메서드는 result = result + [a]와 동등하지만 더 효율적입니다.
        a, b = b, a+b
    return result

f100 = fib2(100)    # call it
f100                # write the result
# return: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]