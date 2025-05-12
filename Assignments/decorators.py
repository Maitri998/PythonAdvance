def decoratorExample(func):
    def otherFunction():
        print(f"Function '{func.__name__}' is called")
        func()
    return otherFunction

@decoratorExample
def greet():
    print("Hello!")

greet()
