
class CustomError(Exception):
    pass

def safe_divide(a,b):
    if b == 0:
        raise CustomError("Division durch 0")
    return a/b

class MethodNotImplementiertError(Exception):
    pass
