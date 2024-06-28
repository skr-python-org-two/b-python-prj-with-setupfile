from dotenv import load_dotenv
import pathlib
import os


def main():
    print("### from run_code_env file")
    current_dir = pathlib.Path(__file__).parent.resolve()
    print(f" current_dir value is ::: {current_dir}")
    load_dotenv(f"current_dir/.env_dev")
    print(os.getenv("VAR_A"))
    print(os.getenv("VAR_B"))
    print(os.getenv("VAR_C"))


if __name__ == "__main__":
    main()
