import sys
import pandas as pd
from sklearn.model_selection import train_test_split

# 从命令行参数获取过滤关键字和随机数种子
filter_key = sys.argv[1]
filter_num = sys.argv[2]

# 读取 TSV 文件
file_path = 'final_merged_all_data.csv'
filtered_df = pd.read_csv(file_path, sep='\t')
label_key = 'score_level'

def get_label(x):
    if x == "0" or x == 0:
        return 0
    return 1

# 过滤数据
filtered_df = filtered_df[filtered_df['study_id'] == filter_key]
#filtered_df['binary_label'] = filtered_df[label_key].apply(get_label)
filtered_df['binary_label'] = pd.to_numeric(filtered_df['binary_label'], errors='coerce')


# 分层抽样按比例分割数据集
train_data, temp_data = train_test_split(
    filtered_df, test_size=0.3, stratify=filtered_df['binary_label'], random_state=int(float(filter_num))
)

dev_data, test_data = train_test_split(
    temp_data, test_size=0.5, stratify=temp_data['binary_label'], random_state=int(float(filter_num))
)

# 保存为 tsv 文件
train_output_path = 'task_place_text_img_train.tsv'
dev_output_path = 'task_place_text_img_dev.tsv'
test_output_path = 'task_place_text_img_test.tsv'

train_data.to_csv(train_output_path, sep='\t', index=False)
dev_data.to_csv(dev_output_path, sep='\t', index=False)
test_data.to_csv(test_output_path, sep='\t', index=False)

print(f"Data has been split and saved to {train_output_path}, {dev_output_path}, and {test_output_path}")
print('train:', len(train_data), 'dev:', len(dev_data), 'test:', len(test_data))