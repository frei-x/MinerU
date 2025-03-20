from collections import defaultdict

data = [
    "姓名马建仓性 性别男民族汉出生 2013年5月27日  ",
    "![](images/1102846b7b150ebebb19531e1f2f4b9b4d7cd36c61b4f7c432b7345b530888ba.jpg)  ",
    "住址 深圳市福田区梅林街道梅都社区中康路136号深圳新一代产业园  ",
    "公民身份号码 XXXXXXXXXXXXXXXXXX  ",
    {
        "content": "姓名马建仓性 性别男民族汉出生 2013年5月27日  ",
        "index": 0
    },
    {
        "content": "![](images/1102846b7b150ebebb19531e1f2f4b9b4d7cd36c61b4f7c432b7345b530888ba.jpg)  ",
        "index": 0
    },
    {
        "content": "住址 深圳市福田区梅林街道梅都社区中康路136号深圳新一代产业园  ",
        "index": 0
    },
    {
        "content": "公民身份号码 XXXXXXXXXXXXXXXXXX  ",
        "index": 0
    },
    {
        "content": "这是下一页",
        "index": 1
    }
]

output_dict = []

# 提取列表中的字典, 合并 "index" 相同的数据, 以 \n\n 为分隔符。
# 使用 defaultdict 来按 index 分组
grouped_data = defaultdict(list)

for item in data:
    if isinstance(item, dict) and "content" in item and "index" in item:
        grouped_data[item["index"]].append(item["content"])

output_dict = [{"content": "\n\n".join(
    contents), "index": idx} for idx, contents in grouped_data.items()]

print(output_dict)
