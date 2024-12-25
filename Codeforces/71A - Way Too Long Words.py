def abrevate(word):
    if len(word) <= 10:
        return word
    else:
        return word[0] + str(len(word[1:-1])) + word[-1]
    
if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        word = input()
        res = abrevate(word)
        print(res)