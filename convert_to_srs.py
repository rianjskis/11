import requests
import json

def fetch_and_convert_github_hosts(github_raw_url):
    # 从GitHub获取文件内容
    response = requests.get(github_raw_url)
    if response.status_code != 200:
        raise Exception(f"Failed to fetch file from GitHub: {response.status_code}")

    all_domain = []
    hosts_data = response.text.splitlines()  # 逐行读取
    for line in hosts_data:
        # 跳过注释和空行
        if line.startswith('#') or not line.strip() or '127.0.0.1' in line:
            continue
        parts = line.split()
        if len(parts) >= 2:  # 只取前两列，忽略多余的列
            ip, domain = parts[:2]
            all_domain.append(domain)

    # 创建最终的配置文件格式
    singbox_config = {
        "version": 2,
        "rules": [{"domain": domain} for domain in all_domain],  # 确保每个域名都是单独的字典
    }

    return singbox_config

# 示例GitHub hosts文件链接
github_raw_url = "https://raw.githubusercontent.com/lingeringsound/10007_auto/master/reward"

# 获取并转换hosts文件
singbox_rules = fetch_and_convert_github_hosts(github_raw_url)

# 将结果输出为.srs格式文件
with open('rules.srs', 'w') as outfile:
    # 将数据格式化为 .srs 需要的格式
    for rule in singbox_rules["rules"]:
        outfile.write(f"domain: {rule['domain']}\n")  # 假设每个规则是 domain

print("Successfully fetched and converted the GitHub hosts file to rules.srs.")
