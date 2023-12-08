import numpy as np
def process_file(file_id):
    """处理单个文件，返回合并后的array"""
    file_path = f'datas\\IMDB_hids_no_extra_prompt\\{file_id}'  # 指定文件夹路径
    data = np.load(file_path)
    # 合并所有arrays为一个array
    merged_array = np.array([data[f'arr_{i}'] for i in range(4096)])
    data.close()
    np.save(f'datas\\npdatas\\{file_id}.npy', merged_array)
    return merged_array
