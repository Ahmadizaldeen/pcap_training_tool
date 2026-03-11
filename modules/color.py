
def colored_class(default_color):
    RESET = '\033[0m'
    def decorator(cls):
        original_str = cls.__str__ if hasattr(cls, "__str__") else lambda self: f"{self.__class__.__name__}"

        def new_str(self):
            return f"{default_color}{original_str(self)}{RESET}"

        cls.__str__ = new_str
        return cls

    return decorator