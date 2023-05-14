
# 1 and 1') /////////////////////////
test = 'Test string'

def find_index(to_string, target):    
    for i, value in enumerate(to_string):
        if value == target:
            return i
    return -1
