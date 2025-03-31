import os
import sys

# get the times when the deadcells app was used
timestamps = []

def capture_return(func, *args, **kwargs):
    value = func(*args, **kwargs)
    return value


data = os.open("/home/emeka/", os.O_RDONLY)
def extract(path, flags):

    return open(path, flags, data)


result = capture_return(extract("file.txt", "r"))


'''
def deadcells_extract(filepath: str):
        try:
            with open(filepath, 'r') as lines:
                return lines.read()
                
        except FileExistsError:
            print("file not found")


sol = deadcells_extract("usagestats.txt")
'''
'''
filepath = ""
with os.open(filepath, 'r') as lines:
    return lines.read()
'''
'''
for s in strings:
                    if "deadcells" in s:
                        timestamps.append(str(s))
'''