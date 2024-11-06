#The authors are Olivia and Elizabeth
def count_character(string,target):
    total = 0
    index = 0
    while index < len(string):
        if string[index : index + len(target)] == target:
            total +=1
        index +=1
    return total
print(count_character("bonobos","o"))
