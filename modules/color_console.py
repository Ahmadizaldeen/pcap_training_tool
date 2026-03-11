# BLUE = '\033[94m'
# GREEN = '\033[92m'
# YELLOW = '\033[93m'
# RED = '\033[0;31m'
# CYAN = '\033[96m'
# MAGENTA = '\033[95m'
# ENDC = '\033[0m'
#
# def colorize(value):
#
#     if isinstance(value, int):
#         color = BLUE
#     elif isinstance(value, float):
#         color = MAGENTA
#     elif isinstance(value, str):
#         color = GREEN
#     elif isinstance(value, list):
#         color = CYAN
#     elif isinstance(value, dict):
#         color = YELLOW
#     elif isinstance(value, tuple):
#         color = RED
#     else:
#         color = ENDC
#
#     return f"{color}{value}{ENDC}"
#
# def type_color_decorator(func):
#     print(f"{BLUE}int {GREEN}str {YELLOW}dict {RED}list {CYAN}list {MAGENTA}float{ENDC}")
#
#     def wrapper(*args, **kwargs):
#
#         result = func(*args, **kwargs)
#
#         return colorize(result)
#
#     return wrapper
#
# def debug(func):
#
#     def wrapper(*args, **kwargs):
#
#         print(f"[DEBUG] Function: {func.__name__}")
#         print(f"[DEBUG] args: {args}")
#         print(f"[DEBUG] kwargs: {kwargs}")
#
#         result = func(*args, **kwargs)
#
#         print(f"[DEBUG] result: {result}")
#
#         return result
#
#     return wrapper
#
# if __name__ == "__main__":
#
#     print(f"{BLUE}int {GREEN}str {YELLOW}dict {RED}list {CYAN}list {MAGENTA}float{ENDC}")
