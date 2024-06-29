
import os
from custom.functs.math_functs import s_add_square , s_sub_square
import pathlib



def __main__():
    print("## from main method")
    print(s_add_square(10,30))
    print(s_sub_square(40,50))
    current_dir = pathlib.Path(__file__).parent.resolve()
    print(f"### {current_dir}")
    print(type(current_dir))


if __name__ == "__main__" :
    __main__()
