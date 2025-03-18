import os

path = r'C:\Rithesh_B\Projects\Behav'

def print_path(path):
    # try:
    if not os.path.exists(path):
        raise FileNotFoundError("File missing") from e
    # except Exception as e:
    #     print(f'>>> {e}')

    print("function control here")


try:
    print_path(path)
    print("Control here")
except Exception as e:
    print(f'=== {e}')