import numpy as np
import os
def load_feature(id_and_folder_path):
    id, folder_path = id_and_folder_path
    file_path = os.path.join(folder_path, str(id))
    data_f = np.load(file_path)
    result = np.array(list(data_f.values()))
    data_f.close()
    return result, id
