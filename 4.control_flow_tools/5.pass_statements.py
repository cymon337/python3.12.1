# 4.5. pass Statements

# pass 문은 아무것도 하지 않는다....
# 문법적으로 필요한 경우 사용한다.

# 아래의 경우 while 이 동작하지만 아무것도 하지 않는다... Ctrl + C 를 사용하여 멈출때 까지
while True:
    pass  # Busy-wait for keyboard interrupt (Ctrl+C)

# 일반적으로 최소한의 클래스 생성시 사용된다.
class MyEmptyClass:
    pass

# 함수, 조건문 등을 새로 작성할 때 place-holder 로서 추상적으로 사용된다. 구체적으로 작성하지 않고 넘어갈때
def initlog(*args):
    pass   # Remember to implement this!

