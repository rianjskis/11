import requests

# 获取数据
def fetch_rules():
    url = 'https://raw.githubusercontent.com/lingeringsound/10007_auto/master/reward'
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        raise Exception("Failed to fetch rules")

# 转换为 Singbox .srs 格式
def convert_to_srs(rules_text):
    rules = []
    for line in rules_text.strip().splitlines():
        line = line.strip()
        if not line:
            # 跳过空行
            continue
        parts = line.split(' ')
        if len(parts) != 2:
            # 如果某行不符合 IP 和域名的格式，跳过该行
            print(f"Skipping invalid line: {line}")
            continue
        ip, domain = parts
        rule = {
            'type': 'domain',
            'value': domain,
            'ip': ip
        }
        rules.append(rule)
    
    # 生成二进制格式（假设你有特定的 .srs 格式处理逻辑）
    srs_data = format_to_srs_binary(rules)
    
    with open('converted_rules.srs', 'wb') as f:
        f.write(srs_data)

# 假设你有特定的格式转换为 .srs 二进制文件的逻辑
def format_to_srs_binary(rules):
    # 这里需要将规则转换为 Singbox 二进制格式的逻辑
    return b''  # 示例，返回空字节，实际应为转换后的二进制数据

if __name__ == "__main__":
    rules_text = fetch_rules()
    convert_to_srs(rules_text)
