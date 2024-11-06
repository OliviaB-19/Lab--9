# The authors are Olivia and Elizabeth

def total_length(x):
    total=0
    for ch in x:
        total+= len(ch)
    return total

print(total_length(['Queen','rules']))

s = "Tenochtitlan"
index = 0
while index < len(s):
    index += 1
    print(s[:index])
