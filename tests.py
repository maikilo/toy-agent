from functions.get_file_content import get_file_content
from functions.get_files_info import get_files_info


def get_files_info_test():
    print("Result for current directory:")
    print(get_files_info("calculator", "."))

    print("\nResult for 'pkg' directory:")
    print(get_files_info("calculator", "pkg"))

    print("\nResult for current directory:")
    print(get_files_info("calculator", "/bin"))

    print("\nResult for 'pkg' directory:")
    print(get_files_info("calculator", "../"))


def get_file_content_test():
    result = get_file_content("calculator", "main.py")
    print(result)

    result = get_file_content("calculator", "pkg/calculator.py")
    print(result)

    result = get_file_content("calculator", "/bin/cat")
    print(result)


if __name__ == "__main__":
    get_files_info_test()
    get_file_content_test()
