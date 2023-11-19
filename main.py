import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from b2sdk.v1 import B2Api, InMemoryAccountInfo

st.set_option('deprecation.showPyplotGlobalUse', False)
# Initialize Backblaze B2 API
b2_api = B2Api(InMemoryAccountInfo())
application_key_id = "e32a82c5e507"
application_key = "005442324ab409360d7634e5f1017a9b2f60a58c4f"
b2_api.authorize_account("production", application_key_id, application_key)

# Backblaze B2 bucket and file information
bucket_name = "foodreviews"
file_name = "Reviews.csv"

# Download data from Backblaze B2
with open(file_name, "wb") as file:
    b2_api.download_file_by_name(bucket_name, file_name, file)
    # Load data into a DataFrame
df = pd.read_csv(file_name)
# Your visualization (e.g., histogram)
plt.figure(figsize=(10, 6))
sns.countplot(x='Score', data=df, palette='viridis')
plt.title('Distribution of Review Scores')
plt.xlabel('Score')
plt.ylabel('Count')
st.pyplot()

# Display a subset of your data
subset_size = st.slider("Select subset size", min_value=1, max_value=len(df), value=10)
st.dataframe(file_name.head(subset_size))
