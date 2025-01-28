import os
import cython
from Cython.Build.BuildExecutable import build

def en():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('Code By JINN \n----------------')
    print('\033[1;37m 1 -> Compile Cython \n 2 -> Compile ELF (ex: \033[1;32m./run\033[1;37m)\n 0 -> Exit ')
    x = input(' -> Opt: ')
    if x == '1':
        os.system('cls' if os.name == 'nt' else 'clear')
        file = input('Put File: ')
        try:
            with open(file, 'r') as f:
                f.read()
        except FileNotFoundError:
            print('File Location Not Found')
            return
        subprocess.run(['cythonize', '-i', '-2', file], stdout=subprocess.DEVNULL)
        input('Your File Compile Done Enjoy ')
        en()
    elif x == '2':
        os.system('cls' if os.name == 'nt' else 'clear')
        file = input('Put File: ')
        try:
            with open(file, 'r') as f:
                f.read()
        except FileNotFoundError:
            print('File Location Not Found')
            return
        build(file)
        input('Your File Compile Done Enjoy ')
        en()
    else:
        print('Successful exit')

en()