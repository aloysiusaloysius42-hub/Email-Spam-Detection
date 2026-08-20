import pandas as pd

# Create dataset
data = {
    "Message": [
        "Congratulations! You won a free prize",
        "Can we meet tomorrow?",
        "Win a free mobile phone now",
        "Your assignment is due tomorrow",
        "Claim your cash reward today",
        "Hello, how are you?"
    ],
    "Label": [
        "Spam",
        "Not Spam",
        "Spam",
        "Not Spam",
        "Spam",
        "Not Spam"
    ]
}

# Create DataFrame
df = pd.DataFrame(data)

print("Dataset:")
print(df)

print("\nFirst 5 rows:")
print(df.head())

print("\nDataset Shape:")
print(df.shape)

print("\nColumns:")
print(df.columns)

print("\nLabel Counts:")
print(df["Label"].value_counts())