import argparse
from BaiduTrans import translate
import time


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--filePath', type=str)
    arguments = parser.parse_args()

file = open(arguments.filePath, 'r', encoding='utf-16')
data = file.read().split('\n')
file.close()
out = []

def removeRB(s):
    ret = ''
    i = 0
    while i < len(s):
        if s[i] != '[':
            ret = ret + s[i]
        else:
            j = i
            while s[j] != ']':
                j = j + 1
            s2 = s[i + 1:j - 1]
            ret = ret + s2.split(',')[1]
            i = j
        i = i + 1
    return ret


for x in data:
    if x != '' and x[0] != '％' and x[0] != '^' and x[0] != '@' and x[0] != '\\' and x[0] != '【':
        y = translate(removeRB(x)).replace('莲花', '莲华').replace('荷花', '莲华')
        print(y)
        out.append(y)
        time.sleep(0.1)
    else:
        out.append(x)

file = open(arguments.filePath, 'w', encoding='utf-16')
for x in out:
    file.write(x + '\n')