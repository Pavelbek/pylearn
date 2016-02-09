def my_first_decorator(func):
    def wrap_func():
        print "this is the first line of text"
        func()
        print "this is the las line of text"
    return wrap_func()
    
@my_first_decorator    
def some_func():
    print "this text should be in the middle"

