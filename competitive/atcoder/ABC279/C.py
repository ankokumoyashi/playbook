dic = {".": 0, "#": 1}
H, W = list(map(int, input().split(' ')))
#S = [input().replace(".", "0").replace("#", "1") for i in range(H)]
#T = [input().replace(".", "0").replace("#", "1") for i in range(H)]
S = [list(map(int, list(input().replace(".", "0").replace("#", "1")))) for i in range(H)]
T = [list(map(int, list(input().replace(".", "0").replace("#", "1")))) for i in range(H)]
import numpy as np
S = sorted(np.array(S).T.tolist())
T = sorted(np.array(T).T.tolist())
print("Yes" if T == S else "No")
