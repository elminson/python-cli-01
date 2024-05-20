import fnmatch
import os


def list_files(path, file_filter='*'):
    if file_filter == '*':
        return os.listdir(path)
    data = os.listdir(path)
    result = {}
    for item in data:
        if fnmatch.fnmatch(item, file_filter):
            print("Match: " + item)
            result[item] = os.path.isdir(os.path.join(path, item))
    return result
