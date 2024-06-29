import os

def __main__():
    print("### from run_code_env_two file")
    os.environ['first_var'] = 'hello'

    for key , value in os.environ.items():
        print(f"{key}    {value}")

if __name__ == "__main__":
    __main__()
