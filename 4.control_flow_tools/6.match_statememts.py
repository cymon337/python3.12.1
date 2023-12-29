# 4.6. match Statements

# 일치하는 첫 번째 패턴만 실행되며 값에서 구성요소(시퀀스 요소 또는 객체 속성)를 변수로 추출할 수도 있습니다.
# switch 문과 유사함

# The simplest form compares a subject value(status) against one or more literals(400,404,418)

# literals : 프로그래밍에서 리터럴(literal)은 소스 코드에서 고정된 값을 나타내는 표기법입니다. 
    # 리터럴은 값 자체를 나타내며 변수나 표현식이 아닙니다. 리터럴은 변수를 초기화하거나 프로그램에 데이터를 제공하는 데 사용됩니다. 
    # 숫자, 문자, boolean, None, 딕셔너리, 튜블 등..
    
def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case 401 | 403 | 404: # | (or) 사용하여 패턴 생성 가능
            return "Not allowed"
        case _:  # “variable name” _ : 일치하는 케이스가 없으면 수행됨
            return "Something's wrong with the internet"
        
# 패턴의 변수 바인딩 가능 
def http_error(point):
    # point is an (x, y) tuple
    match point:
        case (0, 0): 
            print("Origin")
        case (0, y):
            print(f"Y={y}")
        case (x, 0):
            print(f"X={x}")
        case (x, y):    # 분해할당과 유사하다
            print(f"X={x}, Y={y}")
        case _:
            raise ValueError("Not a point")
        
# 클래스를 사용하여 데이터를 구조화하는 경우 
# 클래스 이름 뒤에 생성자와 유사한 인수 목록을 사용할 수 있지만 
# 속성을 변수로 캡처하는 기능이 있습니다.

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def where_is(point):
    match point:
        case Point(x=0, y=0):
            print("Origin")
        case Point(x=0, y=y):
            print(f"Y={y}")
        case Point(x=x, y=0):
            print(f"X={x}")
        case Point():
            print("Somewhere else")
        case _:
            print("Not a point")

# 다음과 같은 패턴으로 바인딩 가능
        # Point(1, var)
        # Point(1, y=var)
        # Point(x=1, y=var)
        # Point(y=var, x=1)
# 위와 같은 `var` 독립형 이름만 match 문에 의해 할당됩니다.
# 점 표기법(예: foo.bar), 속성 이름(위의 x= 및 y=) 또는 클래스 이름(위의 Point와 같이 옆에 '(...)')은 절대로 할당되지 않습니다.


# 패턴은 임의로 중첩될 수 있습니다. 예를 들어, __match_args__가 추가된 짧은 Point 목록이 있다면, 다음과 같이 매치할 수 있습니다
class Point:
    __match_args__ = ('x', 'y')
    def __init__(self, x, y):
        self.x = x
        self.y = y

match points:
    case []:
        print("No points")
    case [Point(0, 0)]:
        print("The origin")
    case [Point(x, y)]:
        print(f"Single point {x}, {y}")
    case [Point(0, y1), Point(0, y2)]:
        print(f"Two on the Y axis at {y1}, {y2}")
    case _:
        print("Something else")
        
# 패턴에 '가드'로 알려진 if 절을 추가할 수 있습니다. 
# 가드가 거짓이면, 매치는 다음 case 블록을 시도하게 됩니다. 가드가 평가되기 전에 값 캡처가 발생한다는 점에 주의하세요
# 위의 설명하는 문장에서 "캡처"는 패턴 매칭 중에 변수에 값을 할당하는 것을 의미합니다. 캡처는 패턴에 일치하는 부분을 추출하여 변수에 저장하는 역할을 합니다.

match point:
    case Point(x, y) if x == y:
        print(f"Y=X at {x}")
    case Point(x, y):
        print(f"Not on the diagonal")

# Like unpacking assignments, tuple and list patterns have exactly the same meaning and actually match arbitrary sequences. An important exception is that they don’t match iterators or strings.
# 튜플 언패킹
t = (1, 2, 3)
a, b, c = t
print(a, b, c)  # 출력: 1 2 3

# 리스트 언패킹
l = [4, 5, 6]
x, y, z = l
print(x, y, z)  # 출력: 4 5 6

# 튜플로 임의의 시퀀스 일치
s = "abc"
it = iter(s)
a, b, c = it
print(a, b, c)  # 출력: a b c

# 튜플로 임의의 시퀀스 일치
seq = [10, 20, 30]
t = (*seq,)
print(t)  # 출력: (10, 20, 30)

# Sequence patterns support extended unpacking: [x, y, *rest] and (x, y, *rest) work similar to unpacking assignments. The name after * may also be _, so (x, y, *_) matches a sequence of at least two items without binding the remaining items.
# '*' 를 사용하는 확장 언패킹(Extended Unpacking)은 시퀀스의 요소를 풀어서(Unpack) 여러 변수에 할당할 수 있습니다. 
# javascript 의 (1, 2, ...) 문법과 유사

# 리스트의 언패킹
numbers = [1, 2, 3, 4, 5]
first, *rest = numbers

print(first)  # 출력: 1
print(rest)   # 출력: [2, 3, 4, 5]

# 튜플의 언패킹
coordinates = (10, 20, 30)
x, y, *z = coordinates

print(x)  # 출력: 10
print(y)  # 출력: 20
print(z)  # 출력: [30]

# 문자열의 언패킹
word = "hello"
first, *rest = word

print(first)  # 출력: h
print(rest)   # 출력: ['e', 'l', 'l', 'o']
# Mapping patterns: {"bandwidth": b, "latency": l} captures the "bandwidth" and "latency" values from a dictionary. Unlike sequence patterns, extra keys are ignored. An unpacking like **rest is also supported. (But **_ would be redundant, so it is not allowed.)

# Subpatterns may be captured using the as keyword:
# case (Point(x1, y1), Point(x2, y2) as p2): ...
# will capture the second element of the input as p2 (as long as the input is a sequence of two points)

# Most literals are compared by equality, however the singletons True, False and None are compared by identity.

# Patterns may use named constants. These must be dotted names to prevent them from being interpreted as capture variable:
from enum import Enum
class Color(Enum):
    RED = 'red'
    GREEN = 'green'
    BLUE = 'blue'

color = Color(input("Enter your choice of 'red', 'blue' or 'green': "))

match color:
    case Color.RED:
        print("I see red!")
    case Color.GREEN:
        print("Grass is green")
    case Color.BLUE:
        print("I'm feeling the blues :(")
        
# For a more detailed explanation and additional examples, you can look into PEP 636 which is written in a tutorial format.