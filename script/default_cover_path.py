import pathlib

# generate default cover path
def default_cover_path(s):
    path = pathlib.Path(s)
    for file in path.iterdir():
        print(" - " + file)

# minimalism(just one line)
# print(' - ' + '\n - '.join([str(item) for item in pathlib.Path('.\\source\\img\\default_cover\\').iterdir()]))

if __name__ == '__main__':
    default_cover_path(".\\source\\img\\default_cover\\")
