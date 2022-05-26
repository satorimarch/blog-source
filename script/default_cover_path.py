import pathlib

# generate default cover path
def default_cover_path(s):
    str1 = ''
    path = pathlib.Path(s)
    for file in path.iterdir():
        str1 += " - " + str(file) + '\n'
    return str1

# minimalism(just one line)
# def default_cover_path(s):
#     return (' - ' + '\n - '.join([str(item) for item in pathlib.Path('.\\source\\img\\default_cover\\').iterdir()]))

if __name__ == '__main__':
    str1 = default_cover_path("./source/img/default_cover/")
    print(str1.replace('\\', '/'))