import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from b2sdk.v1 import B2Api, InMemoryAccountInfo
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
