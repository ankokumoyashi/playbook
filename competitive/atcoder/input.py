#メイン
def main():
    pass
if __name__ == "__main__":
    main()
# 単数字
N = int(input())
# 固定数の数字
N, M = list(map(int, input().split(' ')))
# 可変数の数字
A = list(map(int, input().split(' ')))
# 数字のタプルを改行区切りで複数
TXA = [list(map(int, input().split(' '))) for i in range(N)]

深さが無限になる時、深さ優先探索で枝刈りは悪手。
