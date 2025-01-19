import pandas as pd
import numpy as np
import os
from sklearn.preprocessing import MinMaxScaler

def create_npy_from_xls(folder_path, output_file_path):
    combined_data = []
    for filename in os.listdir(folder_path):
        if filename.endswith('.xls') or filename.endswith('.xlsx'):
            filepath = os.path.join(folder_path, filename)
            data = pd.read_excel(filepath)
            # Optional: Preprocess the data
            scaler = MinMaxScaler()
            data_normalized = scaler.fit_transform(data)
            combined_data.append(data_normalized)
    
    if combined_data:  # Check if combined_data is not empty
        all_data = np.concatenate(combined_data, axis=0)
        np.save(output_file_path, all_data)
    else:
        print("No data to concatenate and save.")

def create_csv_from_xls(folder_path, output_file_path):
    combined_data = pd.DataFrame()
    for filename in os.listdir(folder_path):
        if filename.endswith('.xls') or filename.endswith('.xlsx'):
            filepath = os.path.join(folder_path, filename)
            data = pd.read_excel(filepath)
            # Optional: Preprocess the data
            combined_data = pd.concat([combined_data, data])

    if not combined_data.empty:  # Check if combined_data is not empty
        combined_data.to_csv(output_file_path, index=False)
    else:
        print("No data to process and save.")

# Replace with your actual folder paths and desired output file paths
network_folder_path = 'E:/SWAT/Network/'
physical_folder_path = 'E:/SWAT/Physical/'
output_npy_file = 'E:/SWAT/Network_O/Network.npy'  # Change to your desired path
output_csv_file = 'E:/SWAT/Physical_O/physical_data.csv'  # Change to your desired path

create_npy_from_xls(network_folder_path, output_npy_file)
create_csv_from_xls(physical_folder_path, output_csv_file)
