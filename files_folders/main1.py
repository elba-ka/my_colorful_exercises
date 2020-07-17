import glob

def get_child_to_parent(name_file, matne_file):
    path_files = f"{name_file}/.*.{matne_file}"
    list_of_files = glob.glob('./files/*.txt')

    child_to_parent = {}
    for path_files in list_of_files:
        start = len(name_file) + 1
        stop = len(matne_file) + 1
        child = path_files[start: - stop]
        with open(path_files) as f:
            parent = f.read()
    return child_to_parent
result = get_child_to_parent

print(result)
