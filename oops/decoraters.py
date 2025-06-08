
def greet(fx):
    def mfx():
        print("good morning")
        fx()    
        print("thanx for using this function")
    return mfx

@greet  #decorater
def hello():
    print("hello world") 

hello()
greet(hello)()
