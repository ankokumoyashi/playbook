def main():
    N, x, y = list(map(int, input().split(' ')))
    A = list(map(int, input().split(' ')))
    now_x = -x
    now_y = -y
    goal = (0,0)
    gusu = [n for i, n in enumerate(A, start=1) if i%2 == 0]
    kisu = [n for i, n in enumerate(A, start=1) if i%2 == 1]
    # 初手はx+のみ
    now_x += kisu[0]
    kisu = kisu[1:]
    gusu = sorted(gusu)[::-1]
    kisu = sorted(kisu)[::-1]
    for n in kisu:
        if now_x <= 0:
            now_x += n
        elif now_x > 0:
            now_x -= n
    for n in gusu:
        if now_y <= 0:
            now_y += n
        elif now_y > 0:
            now_y -= n
    if (now_x, now_y) == goal:
        print('Yes')
    else:
        print('No')

if __name__ == "__main__":
    main()
