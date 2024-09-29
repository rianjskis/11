import json

def format_domain(List):
    domain = []
    for line in List:
        domain_lines = f"{line.strip()}"
        domain.append(domain_lines)
    return domain

def format_regex(List):
    regex = []
    for line in List:
        regex_lines = f"{line.strip()}"
        regex.append(regex_lines)
    return regex

def build(rule):
    domain_list = format_domain(rule['domain_list'])  # 这里假设 rule 是一个字典
    regex_list = format_regex(rule['regex_list'])

    srs_rules = []
    for domain in domain_list:
        srs_rules.append(f"DOMAIN-SUFFIX,{domain},DIRECT")

    for regex in regex_list:
        srs_rules.append(f"DOMAIN-REGEX,{regex},DIRECT")

    srs_output = "\n".join(srs_rules)

    # 生成 output.srs 文件
    with open('output.srs', 'w') as f:
        f.write(srs_output)

    return {'list': srs_output, 'suffix': '.srs', 'comment': '//', 'total': len(srs_rules)}

# 示例使用
rule = {
    'domain_list': [
        'example.com',
        'test.com'
    ],
    'regex_list': [
        '^.*\\.example\\.com$'
    ]
}

result = build(rule)
print(result['list'])
