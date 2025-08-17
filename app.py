# app.py

import streamlit as st
import boto3
import random
import io
import polars as pl
import pandas as pd
from ydata_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report
from dotenv import load_dotenv
load_dotenv()

st.title("YData Profiling on S3 Sampled Data")

# ---- S3 config ----
st.sidebar.header("AWS S3 Data Source")
bucket = st.sidebar.text_input("S3 Bucket", value="your-bucket")
key = st.sidebar.text_input("S3 Key (file path in bucket)", value="your-data.csv")
sample_size = st.sidebar.number_input("Sample Size", value=1000, min_value=100, step=100)

if st.sidebar.button("Profile S3 data sample"):
    if bucket and key:
        try:
            s3 = boto3.client("s3")
            obj = s3.get_object(Bucket=bucket, Key=key)
            lines = (line.decode('utf-8') for line in obj['Body'].iter_lines())
            header = next(lines)
            sample = []
            for i, line in enumerate(lines):
                if i < sample_size:
                    sample.append(line)
                else:
                    r = random.randint(0, i)
                    if r < sample_size:
                        sample[r] = line
            csv_sample = "\n".join([header] + sample)
            csv_buffer = io.StringIO(csv_sample)
            df = pl.read_csv(csv_buffer).to_pandas()

            st.success(f"Sampled {len(df)} rows and {len(df.columns)} columns from S3 object '{key}' in bucket '{bucket}'.")
            st.dataframe(df.head(10), use_container_width=True)

            # COLUMN SELECTION FOR PROFILING
            st.markdown("#### Select columns to include in the profile report (optional):")
            selected_cols = st.multiselect(
                "Choose columns to send to ydata-profiling (default: all):",
                list(df.columns),
                default=list(df.columns)
            )
            if selected_cols:
                profile_df = df[selected_cols]
            else:
                profile_df = df

            if st.button("Generate Profile Report"):
                st.write("Running profiling...")
                profile = ProfileReport(profile_df, title="YData Profiling Report", explorative=True)
                st_profile_report(profile)

        except Exception as e:
            st.error(f"Error: {e}")
    else:
        st.warning("Please enter both S3 bucket and key.")

st.markdown(
"""
---
**How it works:**
- The app reads just a random sample of the large S3 file (not the whole file!).
- Lets you select columns to profile for faster results!
- Supports CSV files only. Adjust code for other formats if needed.
"""
)
