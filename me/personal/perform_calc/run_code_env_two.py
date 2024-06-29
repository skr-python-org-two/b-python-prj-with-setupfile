from dotenv import load_dotenv
import pathlib
import os


def main():
    print("### from run_code_env_two file")
    print(os.getenv("GH_BASE_DIR"))
    BDIR = os.getenv("GH_BASE_DIR")
    load_dotenv(f"{BDIR}/.env_dev")
    print(os.getenv("VAR_A"))
    print(os.getenv("VAR_B"))
    print(os.getenv("VAR_C"))


if __name__ == "__main__":
    main()
