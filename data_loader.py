import pandas as pd
import os

def convert_to_csv(input_path):
    parent_folder = os.path.dirname(input_path)
    output_folder = os.path.join(parent_folder, 'csv_data')
    os.makedirs(output_folder, exist_ok=True)

    df = pd.read_excel(input_path)

    filename = os.path.basename(input_path)
    base_name, _ = os.path.splitext(filename)
    new_path = os.path.join(output_folder, base_name + '.csv')
    df.to_csv(new_path, index=False)

    return df