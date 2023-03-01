import copy
def main():
    N, x, y = list(map(int, input().split(' ')))
    A = list(map(int, input().split(' ')))
    now_x = 0
    now_y = 0
    gusu = [n for i, n in enumerate(A, start=1) if i%2 == 0]
    kisu = [n for i, n in enumerate(A, start=1) if i%2 == 1]

    max_kisu = max(kisu) * 1000
    max_gusu = max(gusu) * 1000
    x_dp = {i: False for i in range(-max_kisu, max_kisu+1, 1)}
    emp_dp = copy.copy(x_dp)
    x_dp[kisu[0]] = True
    for n in kisu[1:]:
        nxtdp = copy.copy(emp_dp)
        for k,v in x_dp.items():
            if v == True:
                if k+n in x_dp:
                    nxtdp[k + n] = True
                if k-n in x_dp:
                    nxtdp[k - n] = True
        x_dp = nxtdp
    y_dp = {i: False for i in range(-max_gusu, max_gusu+1, 1)}
    emp_dp = copy.copy(y_dp)
    y_dp[0] = True
    for n in gusu:
        nxtdp = copy.copy(emp_dp)
        for k,v in y_dp.items():
            if v == True:
                if k+n in y_dp:
                    nxtdp[k + n] = True
                if k-n in y_dp:
                    nxtdp[k - n] = True
        y_dp = nxtdp
    if x_dp[x] and y_dp[y]:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()

