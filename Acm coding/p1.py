t = int(input())

while t > 0:
    a, b, c = map(int, input().split())
    ans = a
    r = b % 3

    if r == 0:
        ans += b // 3
        if c % 3 == 0:
            ans += c // 3
        else:
            ans += c // 3 + 1
        print(ans)

    elif c >= 3 - r:
        b += 3 - r
        c -= 3 - r
        ans += b // 3

        if c % 3 == 0:
            ans += c // 3
        else:
            ans += (c // 3) + 1
        print(ans)

    else:
        print(-1)
    t -= 1

