from sample_call import call_turbo
import yaml
import os
from datetime import datetime


def main(gpt_input):
    gpt_output = {}
    res = call_turbo(
        s_txt=gpt_input["system"],
        u_txt=gpt_input["user"]
    )
    gpt_output["assistant"] = res['choices'][0]['message']['content']
    return gpt_output


def dump_result(inout):
    now_str = datetime.now().strftime("%Y%m%d%H%M%S")
    with open(os.path.join('./results', f"{now_str}.yaml"), 'w') as f:
        yaml.dump(inout, f)


if __name__ == "__main__":
    gpt_input = {
        "system": "あなたはレコメンドの研究者です。",
        "user": "ドキュメント内の専門用語を説明している別ドキュメントを探すアルゴリズムはありますか",
    }
    gpt_output = main(gpt_input)
    print(gpt_output)
    inout = dict(**gpt_input, ** gpt_output)
    dump_result(inout)
