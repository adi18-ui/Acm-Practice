def result(a):
    count = 0
    for i in range(1, len(a)-1):
        if (a[i] == 'i' and a[i-1] == 'p' and a[i+1] == 'e') or (a[i] == 'a' and a[i-1] == 'm' and a[i+1] == 'p'):
            count += 1
            i += 2
    return count

if __name__ == "__main__":
    test_cases = int(input())
    for i in range(test_cases):
        n = int(input())
        a = input()
        print(result(a))