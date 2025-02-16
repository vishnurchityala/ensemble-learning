import os
import pandas as pd

base_dir = "."
categories = ["benign", "normal", "malignant"]
data = []

for category in categories:
    folder_path = os.path.join(base_dir, category)
    if not os.path.exists(folder_path):
        print(f"Folder not found: {folder_path}")
        continue
    files = os.listdir(folder_path)
    for file in files:
        if "_mask" in file:
            continue  # Skip mask files
        base_name, ext = os.path.splitext(file)
        expected_mask = base_name + "_mask" + ext
        img_rel_path = os.path.join(category, file)
        mask_rel_path = os.path.join(category, expected_mask)
        full_img_path = os.path.join(base_dir, img_rel_path)
        full_mask_path = os.path.join(base_dir, mask_rel_path)
        if os.path.exists(full_img_path) and os.path.exists(full_mask_path):
            data.append((img_rel_path, mask_rel_path, category.capitalize()))
        else:
            if not os.path.exists(full_img_path):
                print(f"Missing image file: {full_img_path}")
            if not os.path.exists(full_mask_path):
                print(f"Missing mask file: {full_mask_path}")

# Sort the data by image filename
data.sort(key=lambda x: x[0])

df = pd.DataFrame(data, columns=["image_path", "mask_path", "label"])
df.to_csv("metadata.csv", index=False)
print("metadata.csv created successfully!")
