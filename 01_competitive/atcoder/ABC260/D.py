import bisect
from collections import defaultdict
#メイン
def main():
    #Nカードの枚数。Kマイたまったらそのターンでグループが消える。1ターンで1枚引く
    N, K = list(map(int, input().split(' ')))
    P = list(map(int, input().split(' ')))
    field = []
    field_batch = []
    field_batch_num = []
    card2turn = dict()
    turn2card = dict()
    card2remove_turn = defaultdict(lambda : "-1")
    for i,card in enumerate(P, start=1):
        ind = bisect.bisect_right(field, card)
        # cardを入れるとしたら2がでる[1,2,3(カード), 4]
        # fieldの長さと挿入予定箇所が同じなら、card以上の数字はフィールドにないとし、末尾にその値を追加する
        if ind == len(field):
            field_batch.append([card])
            field.append(card)
            field_batch_num.append(1)
        else:
            # X以上で最小の数字は、insert予定indexと等しい
            field_batch[ind].append(card)
            field[ind] = card
            field_batch_num[ind]+=1
        if field_batch_num[ind] == K:
            card2remove_turn.update({card:i for card in field_batch[ind]})
            field_batch_num.pop(ind)
            field_batch.pop(ind)
            field.pop(ind)
    for i in range(1,N+1):
        print(card2remove_turn[i])

if __name__ == "__main__":
    main()

