
def main():
    N, P, Q, R = list(map(int, input().split(' ')))
    A = list(map(int, input().split(' ')))
    from_ind = 0
    to_ind = 0
    fix_from = False
    counter = 0
    while True:
        fix_from = False
        move_fix_from = False
        save_ind = from_ind
        for target in [P,Q,R]:
            a_sum = 0
            #import pdb;pdb.set_trace()
            while True:
                if a_sum == target:
                    fix_from = True
                    break
                elif a_sum > target:
                    if fix_from:
                        move_fix_from = True
                        break
                    if from_ind == len(A)-1:
                        print('No')
                        exit()
                    a_sum -= A[from_ind]
                    from_ind += 1
                elif a_sum < target:
                    if to_ind >= len(A):
                        print('No')
                        exit()
                    a_sum += A[to_ind]
                    to_ind += 1
            if move_fix_from:
                counter += 1
                if counter == 100:
                    print("Yes")
                    exit()
                from_ind = save_ind + 1
                to_ind = from_ind
                break
            else:
                to_ind = to_ind
                from_ind = to_ind
        if not move_fix_from:
            break
    print('Yes')

if __name__ == "__main__":
    main()
