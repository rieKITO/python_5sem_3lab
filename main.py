# LOGS
from config import logger

# UTILS
from utils.FileToString import file_to_string

# TASK
from task.Dictionary import Dictionary


def main() -> None:
    logger.info("Program is start")

    correct = False
    while not correct:
        file_name = str(input("\nEnter the file name\n-> "))
        try:
            open(file_name, 'r')
            correct = True
        except FileNotFoundError:
            logger.exception("File not found")
        else:
            file_string = file_to_string(file_name)
            dictionary = Dictionary(file_string)
            dictionary.words_frequency = sorted(dictionary.words_frequency)
            print(
                f"Word count: {dictionary.count_of_words}\n" +
                f"Symbol count: {dictionary.count_of_symbols}\n" +
                f"Catchphrase: {dictionary.words_frequency[0]}"
            )


if __name__ == '__main__':
    main()
