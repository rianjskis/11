import json
import sys

def convert_to_srs(input_file, output_file):
    # 从 input_file 读取规则
    with open(input_file, 'r') as f:
        rules = f.readlines()

    all_domain = []
    hosts_data = response.text.splitlines()  # 逐行读取
    for line in hosts_data:
        # 跳过注释和空行
        if line.startswith('#') or not line.strip() or line.find('127.0.0.1') :
            continue
        parts = line.split()
        if len(parts) >= 2:  # 只取前两列，忽略多余的列
            ip, domain = parts[:2]
            all_domain.append(domain)

    # 打印提取的域名列表
    all_domain.pop(0)
    # 创建最终的配置文件格式
    srs_rules = {
        "version": 2,
        "rules": [{"domain": all_domain, }],
    }

    # 将转换后的规则写入 output_file
    with open(output_file, 'w') as f:
        json.dump(srs_rules, f, indent=2)

if __name__ == "__main__":
    convert_to_srs(sys.argv[1], sys.argv[2])
