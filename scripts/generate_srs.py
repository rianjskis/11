import requests

# 下载内容
url = 'https://raw.githubusercontent.com/lingeringsound/10007_auto/master/reward'
response = requests.get(url)

if response.status_code == 200:
    data = response.text
else:
    print(f"Failed to fetch data: {response.status_code}")
    exit()

# 构建 SRS 规则
srs_data = {
    "version": 2,
    "rules": []
}

# 逐行解析数据
for line in data.splitlines():
    if line.strip():  # 忽略空行
        parts = line.split()
        if len(parts) == 2:  # 确保有两个部分
            ip_address = parts[0]
            domain = parts[1]
            # 构建规则
            rule = {
                "ip": ip_address,
                "domain": domain  # 修正了此行中的变量名
            }
            srs_data['rules'].append(rule)

# 保存为 .srs 文件
with open('rules.srs', 'w', encoding='utf-8') as f:
    for rule in srs_data['rules']:
        f.write(f"{rule['ip']} {rule['domain']} \n")  # 修正了此行的写入格式

print("SRS file created successfully!")
