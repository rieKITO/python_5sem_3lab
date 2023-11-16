import os


def file_to_string(file_name: str) -> str:
    """
    Transferring the contents of a file to a string
    :param file_name:
    :return: str
    """
    if type(file_name) is not str:
        raise TypeError

    file_string = ''

    if not os.path.isfile(file_name):
        raise FileNotFoundError

    if os.access(file_name, os.R_OK):
        with open(file_name, 'r') as file:
            for line in file:
                file_string += line
    else:
        raise PermissionError

    return file_string
