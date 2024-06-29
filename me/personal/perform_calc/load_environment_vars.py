from dotenv import load_dotenv
import pathlib
import os


def main():
    print("### from load_environment_vars file")
    current_dir = pathlib.Path(__file__).parent.resolve()
    print(f" current_dir value is ::: {current_dir}")
    PROJ_BASE_DIRECTORY = os.getenv("PROJ_BASE_DIR")
    print(f"env value of PROJ_BASE_DIR is :::: ")
    print(os.getenv("PROJ_BASE_DIR"))
    print(f"   ::::::::::::::::::::::::::::::::::::::::   ")
    load_dotenv(f"{PROJ_BASE_DIRECTORY}/.env_dev")
    print(os.getenv("VAR_A"))
    print(os.getenv("VAR_B"))
    print(os.getenv("VAR_C"))


if __name__ == "__main__":
    main()
