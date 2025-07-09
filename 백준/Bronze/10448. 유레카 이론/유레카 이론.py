tri = [n*(n+1)//2 for n in range(1, 45)]  # T44=990 < 1000, T45=1035>1000

T = int(input())
for _ in range(T):
    K = int(input())
    found = 0
    for i in tri:
        for j in tri:
            for k in tri:
                if i + j + k == K:
                    found = 1
                    break
            if found:
                break
        if found:
            break
    print(found)