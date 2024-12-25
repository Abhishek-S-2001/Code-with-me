def divide_in_two(w):
    if w < 4:
        return "NO"
    elif w % 2 == 0:
        return "Yes"
    return "NO"

if __name__ == "__main__":
    i = int(input())
    res = divide_in_two(i)
    print(res)