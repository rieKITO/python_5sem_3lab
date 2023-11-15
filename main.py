# LOGS
from config import logger

# UTILS
from utils.file_to_string import file_to_string

# TASK
from task.dictionary.dictionary import Dictionary


def main() -> None:
    logger.info("Program is start")
    file_name = str(input("\nEnter the file name\n-> "))
    file_string = file_to_string(file_name)
    dictionary = Dictionary(file_string)
    sorted_dictionary = dictionary.sort_dictionary(True)

    print(
        f"Word count: {dictionary.count_of_words}\n" +
        f"Symbol count: {dictionary.count_of_symbols}\n"
    )

    if sorted_dictionary:
        print(f"Catchphrase: {sorted_dictionary[0]}")


if __name__ == '__main__':
    main()
