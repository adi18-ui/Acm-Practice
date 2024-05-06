def result(a):
    for i in range(1, len(a) - 1):
        if a[i - 1] <= a[i + 1] and a[i] >= 2 * a[i - 1]:
            a[i] -= 2 * a[i - 1]
            a[i + 1] -= a[i - 1]
            a[i - 1] = 0

    for i in range(len(a)):
        if a[i] != 0:
            return "NO"

    return "YES"

if __name__ == "__main__":
    testCase = int(input())
    for _ in range(testCase):
        n = int(input())
        a = list(map(int, input().split()))
        ans = result(a)
        print(ans)