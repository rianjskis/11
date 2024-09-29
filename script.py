def format_domain(List):
    domain = []
    for line in List:
        domain_lines = f"{line.strip()}"
        domain.append(domain_lines)
    return domain

def build(rule):
    domain_list = format_domain(rule['domain_list'])  # 假设 rule 是一个字典
    srs_rules = []

    for domain in domain_list:
        srs_rules.append(f"DOMAIN-SUFFIX,{domain},DIRECT")  # 使用 DOMAIN-SUFFIX 规则格式

    srs_output = "\n".join(srs_rules)
    
    # 返回以 .srs 格式输出
    return {'list': srs_output, 'suffix': '.srs', 'comment': '//', 'total': len(srs_rules)}

# 示例使用
rule = {
    'domain_list': [
        'example.com',
        'test.com'
    ]
}

result = build(rule)
print(result['list'])
