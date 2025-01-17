n = int(input())
x = 0
for i in range(n):
    s = input()
    if s == "Tetrahedron":
        x += 4
    elif s == "Cube":
        x += 6
    elif s == "Octahedron":
        x += 8
    elif s == "Dodecahedron":
        x += 12
    elif s == "Icosahedron":
        x += 20

print(x)