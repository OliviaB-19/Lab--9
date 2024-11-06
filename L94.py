#The authors are Olivia and Elizabeth

index = 0
s = "Mind the gap!"
while index < len(s) and s[index] != "":
    index += 1
print(s[:index])


index = 18
s = "This is a sentence. This is another sentence"
while index < len(s) and s[index] != ".":
    index +=1
print(s[:index])


def no_repeating():
    words =[]
    while True:
        word = input("Tell me a word: ")
        if word in words:
            print("You told me that word already!")
            break
        words.append(word)
    return words

def find_512():
    for x in range(100):
        for y in range(100):
            if x * y == 512:
                 break
    return f"{x} * {y} == 512"

print(find_512())

def find_512():
    for x in range(100):
        for y in range(100):
            if x * y == 512:
                 break
            break
    return f"{x} * {y} == 512"

print(find_512())

def find_512():
    for x in range(100):
        for y in range(100):
            if x * y == 512:
                return f"{x} * {y} == 512"

print(find_512())
