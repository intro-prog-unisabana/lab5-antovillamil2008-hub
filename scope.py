int = None
str = None

def set_globals(some_int, some_str):
    global int, str
    int=some_int
    str=some_str

def get_globals():
    return(int,str)
       
