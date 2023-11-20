import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from b2sdk.v1 import B2Api, InMemoryAccountInfo

# Initialize B2Api and authorize the account
b2_api = B2Api(InMemoryAccountInfo())
application_key_id = "your_application_key_id"  # Replace with your Backblaze B2 application key ID
application_key = "your_application_key"        # Replace with your Backblaze B2 application key
b2_api.authorize_account("production", application_key_id, application_key)

# Load your data from Backblaze B2
bucket_name = "your_bucket_name"  # Replace with your Backblaze B2 bucket name
file_name = "path/to/your/Reviews.csv"  # Replace with the path to your file in the bucket

# Download the file from B2
with open("Reviews.csv", "wb") as f:
    b2_api.download_file_by_name(bucket_name, file_name, f)

# Load your data
df = pd.read_csv("Reviews.csv")  # Update with your actual data path
st.set_option('deprecation.showPyplotGlobalUse', False)

# Your visualization (e.g., histogram)
plt.figure(figsize=(10, 6))
sns.countplot(x='Score', data=df, palette='viridis')
plt.title('Distribution of Review Scores')
plt.xlabel('Score')
plt.ylabel('Count')
st.pyplot()

# Display a subset of your data
subset_size = st.slider("Select subset size", min_value=1, max_value=len(df), value=10)
st.dataframe(df.head(subset_size))
