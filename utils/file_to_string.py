def file_to_string(file_name: str) -> str:
    """
    Transferring the contents of a file to a string
    :param file_name:
    :return: str
    """
    if type(file_name) != str:
        raise TypeError

    file_string = ''

    try:
        with open(file_name, 'r') as file:
            for line in file:
                file_string += line

    except FileNotFoundError:
        raise FileNotFoundError

    return file_string
