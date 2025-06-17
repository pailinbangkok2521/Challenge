import os
import mmap

def memory_map(filename, access=mmap.ACCESS_READ):
    size = os.path.getsize(filename)
    fd = os.open(filename, os.O_RDONLY)
    return mmap.mmap(fd, size, access=access)

with memory_map("mystery.png") as b:
    flag = b[-26:]
    for i in range(6):
        print(chr(flag[i]), end='')
    for i in range(6, 15):
        print(chr(flag[i] - 5), end='')
    print(chr(flag[15] + 3), end='')
    for i in range(16, 26):
        print(chr(flag[i]), end='')
    print ("")
