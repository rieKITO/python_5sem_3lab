from config import logger


def file_to_string(file_name: str) -> str:

    """
    Transferring the contents of a file to a string
    :param file_name:
    :return: str
    """

    file_string = ''
    try:
        with open(file_name, 'r') as file:
            for line in file:
                file_string += line

    except FileNotFoundError:
        logger.exception("File not found")

    return file_string
