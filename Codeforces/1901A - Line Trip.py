t = int(input())
for _ in range(t):
    n, x = map(int, input().split())
    stations = list(map(int, input().split()))

    # Full route: 0 → ... → x → ... → 0
    route = [0] + stations + [x] + stations[::-1] + [0]

    max_distance = 0
    for i in range(1, len(route)):
        max_distance = max(max_distance, abs(route[i] - route[i-1]))

    print(max_distance)
