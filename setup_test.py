import pandas as pd
import os

data = {
    "topfolder": ["HR", "IT", None, None, None],
    "topfolder/layer2": ["Level 4", "Level 5", None, None],
    "topfolder/Level 4/layer3": ["1", "2", None, None],
    "topfolder/Level 5/layer3": ["7", "8", None, None],
    "topfolder/layer2/layer3/layer4": ["X", "Y", None, None]
}

df = pd.DataFrame(data)
# Adjust lengths to match (pandas requires equal length arrays)

output_path = r"C:\Users\User\Downloads\test_nest_v2.xlsx"
df.to_excel(output_path, index=False)
print(f"Created {output_path}")
