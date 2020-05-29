import os

ls = open('ls.txt', 'r').read().split('\n')

for x in ls:
    print('translating: ', x)
    com = 'python3 ./work.py --filePath=./files/' + x
    os.system(com)

