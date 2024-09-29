import json
import struct

def read_json(file_path):
    # 读取 json 文件
    with open(file_path, 'r') as f:
        domains = json.load(f)
    return domains

def convert_to_srs(domains, output_file):
    # 假设 .srs 格式需要一个 header 和每个域名的长度和内容
    with open(output_file, 'wb') as f:
        # 写入 srs 版本 (比如: 2) 和其他必要的元数据
        version = 2
        f.write(struct.pack('!I', version))  # 版本号写入，假设为4字节的整数
        
        # 写入域名列表
        for domain in domains:
            # 将每个域名写入二进制文件
            domain_bytes = domain.encode('utf-8')
            domain_length = len(domain_bytes)
            # 先写入长度，再写入域名
            f.write(struct.pack('!I', domain_length))  # 写入域名长度
            f.write(domain_bytes)  # 写入域名内容

def main():
    json_file = 'singbox_rules.json'  # 输入的 json 文件
    srs_file = 'ad.srs'  # 输出的 srs 文件，改为 ad.srs
    
    # 读取 json 文件中的域名
    domains = read_json(json_file)
    
    # 将域名转换为 srs 二进制文件
    convert_to_srs(domains, srs_file)
    
    print(f"转换完成，已生成 {srs_file} 文件")

if __name__ == '__main__':
    main()
