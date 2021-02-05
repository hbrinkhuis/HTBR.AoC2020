def open_file_lines(path):
    data_file = open(path, 'r')
    return data_file.readlines()

def open_file_split(path):
    data_file = open(path, 'r')
    return data_file.read().splitlines()