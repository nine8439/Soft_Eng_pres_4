
def fibonacci(x,y,userInput):
    value = y
    while value <= 10 :
        if value < userInput:
            print value
        x,y = y,x+y
        value = y
            
    return value

def main():
    userInput = raw_input("Give me a value to read to: ")
    x,y = 1,1
    answer = fibonacci(x,y,userInput)
    print answer


main()
        