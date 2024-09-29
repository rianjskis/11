import json
import sys

def convert_to_srs(input_file, output_file):
    # 从 input_file 读取规则
    with open(input_file, 'r') as f:
        rules = f.readlines()

    # 将规则转换为 sing-box .srs 格式
    srs_rules = {"version": 2, "rules": []}
    for rule in rules:
        # 根据规则格式调整以下逻辑
        srs_rules["rules"].append(rule.strip())

    # 将转换后的规则写入 output_file
    with open(output_file, 'w') as f:
        json.dump(srs_rules, f, indent=2)

if __name__ == "__main__":
    convert_to_srs(sys.argv[1], sys.argv[2])
