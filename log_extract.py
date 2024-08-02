import os
import re
import csv

# 正则表达式
log_pattern = re.compile(r'^(\S+) - - \[(.*?)\] "(\S+) (\S+) \S+" (\d+) \d+ "(.*?)" "(.*?)"')

# 指定日志文件夹路径
log_folder = 'logs/'  # 替换为你的日志文件夹路径

# 创建一个CSV文件并写入标题行
output_file = 'log_data.csv'
with open(output_file, mode='w', newline='', encoding='utf-8') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(["IP Address", "Timestamp", "Request Method", "URL", "Status Code", "Referer", "User Agent"])

    # 遍历日志文件夹中的所有文件
    for filename in os.listdir(log_folder):
        if filename.endswith(".log"):  # 只处理以.log结尾的文件
            with open(os.path.join(log_folder, filename), 'r', encoding='latin-1') as log_file:  # 使用 'latin-1' 编码
                for line in log_file:
                    match = log_pattern.match(line)
                    if match:
                        ip_address = match.group(1)
                        timestamp = match.group(2)
                        request_method = match.group(3)
                        url = match.group(4)
                        status_code = match.group(5)
                        referer = match.group(6)
                        user_agent = match.group(7)
                        # 将匹配到的结果写入CSV文件
                        csv_writer.writerow([ip_address, timestamp, request_method, url, status_code, referer, user_agent])

print(f"Log data has been written to {output_file}")