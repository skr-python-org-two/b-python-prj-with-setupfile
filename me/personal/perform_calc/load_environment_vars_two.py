from dotenv import load_dotenv
import pathlib
import os


def main():
    print("### from load_environment_vars_two file")
    print(os.getenv("GH_BASE_DIR"))
    BDIR_value = os.getenv("GH_BASE_DIR")
    env_value = os.getenv("env")
    load_dotenv(f"{BDIR_value}/.env_{env_value}")
    print(os.getenv("VAR_A"))
    print(os.getenv("VAR_B"))
    print(os.getenv("VAR_C"))


if __name__ == "__main__":
    main()
