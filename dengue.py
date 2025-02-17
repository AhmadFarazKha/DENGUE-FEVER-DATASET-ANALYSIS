import os
import pandas as pd
import numpy as np
import sweetviz as sv
from autoviz.AutoViz_Class import AutoViz_Class

# Define file path
FILE_PATH = '/kaggle/input/dengue-fever-dataset/Mosquito.csv'

# Display available files
print("Available files in input directory:")
for root, _, files in os.walk('/kaggle/input'):
    for file in files:
        print(os.path.join(root, file))

# Load dataset
df = pd.read_csv(FILE_PATH)
print(f"Dataset Loaded: {df.shape[0]} rows, {df.shape[1]} columns")
print("First Few Records:")
print(df.head())

# Generate and save Sweetviz report
print("Creating Sweetviz report...")
report = sv.analyze(df)
report.show_html("sweetviz_output.html")

# Generate and visualize data using AutoViz
print("Executing AutoViz analysis...")
av = AutoViz_Class()
av.AutoViz(FILE_PATH)