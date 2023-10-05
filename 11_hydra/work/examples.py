import os
import copy
import subprocess
import re
import pandas as pd
import numpy as np
from datetime import datetime
import yaml
import hydra


@hydra.main(version_base=None, config_path="config", config_name="template")
def main(cfg):
    input_table = pd.read_csv(cfg["input_csv"])
    conversations = []
    for _, one_conversation_data in input_table.iterrows():
        conversations.append(one_conversation(one_conversation_data, cfg["template"]))
    import ipdb;ipdb.set_trace()
    conversations_table = pd.concat([pd.DataFrame(col.tolist()) for col in np.array(conversations).T], axis=1)
    print(pd.concat([input_table, conversations_table], axis=1).to_csv("result.csv"))

def one_conversation(row, template):
    messages = []
    template = copy.deepcopy(template)
    while template:
        m = template.pop(0)
        role, message = m["role"], m["message"]

        # 入力csvを参照している場合は置換
        # テンプレートでは{csvの列名}で指定
        targets = re.findall("\{(.*?)\}", message)
        for t in targets:
            message = message.replace("{"+f"{t}"+"}", row[t])

        # chatgptの出力を利用する場合は一度投げて結果を入れる
        # テンプレートでは__RETURN__で指定
        if "__RETURN__" in message:
            res = call()
            # chatgptの出力に対してosコマンドを適用してから使用
            if "process" in m:
                path = "/tmp/buf.txt"
                with open(path, "w") as f:
                    f.write(res)
                res = subprocess.run(m["process"].format(path).split(), timeout=5, capture_output=True).stdout.decode()
            message = message.replace("__RETURN__", res)
        messages.append({m["role"]: message})
    return messages


def call():
    return "Q1\nA1\nQ2\nA2"


if __name__ == "__main__":
    main()
