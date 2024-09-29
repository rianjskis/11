import json
import sys

def convert_to_srs(input_file, output_file):
    # 从 input_file 读取规则
    with open(input_file, 'r') as f:
        rules = f.readlines()

    all_domain = []
    # 假设这里是从响应中读取的数据（你可能需要更改为实际获取数据的方法）
    hosts_data = rules  # 修改为从 rules 中读取

    for line in hosts_data:
        # 跳过注释和空行
        if line.startswith('#') or not line.strip() or '127.0.0.1' in line:
            continue
        parts = line.split()
        if len(parts) >= 2:  # 只取前两列，忽略多余的列
            ip, domain = parts[:2]
            all_domain.append(domain)

    # 创建最终的配置文件格式
    srs_rules = {
        "version": 2,
        "rules": [{"domain": domain} for domain in all_domain],  # 确保每个域名都是单独的字典
    }

    # 将转换后的规则写入 output_file
    with open(output_file, 'w') as f:
        json.dump(srs_rules, f, indent=2)

if __name__ == "__main__":
    convert_to_srs(sys.argv[1], sys.argv[2])
