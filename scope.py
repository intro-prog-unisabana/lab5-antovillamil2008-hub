global_int=None
global_str=None

def set_globals(some_int, some_str):
    global global_int, global_str
    global_int=some_int
    global_str=some_str

def get_globals():
    return(global_int,global_str)
       
print(get_globals())     
set_globals(10, "Hello")
print(get_globals())  