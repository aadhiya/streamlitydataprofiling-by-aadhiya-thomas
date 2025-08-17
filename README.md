# Streamlitydataprofiling-by-aadhiya-thomas


This is a Streamlit application that allows you to profile large datasets efficiently using [ydata-profiling](https://github.com/ydataai/ydata-profiling). The app supports loading a random sample of rows directly from a large CSV file stored in an Amazon S3 bucket, avoiding the need to download the entire file. Users can select which columns to include in the profiling report to speed up analysis and focus on relevant data.

## Features

- Connect to an S3 bucket and sample a subset of rows from a large CSV file.
- Preview the sampled data directly in the app.
- Select columns to include in the data profiling report.
- Generate a detailed and interactive profiling report using ydata-profiling.
- Lightweight and efficient sampling to handle large datasets.

## Getting Started

### Prerequisites

- Python 3.8+
- AWS credentials set up via environment variables or AWS CLI to access S3 buckets.
- Streamlit and required Python packages installed.

### Installation

1. Clone the repository:

   git clone https://github.com/yourusername/your-repo-name.git
cd your-repo-name

2. (Optional) Create and activate a virtual environment:

python -m venv .venv

Windows
.venv\Scripts\activate

macOS/Linux
source .venv/bin/activate

3. Install dependencies:

pip install -r requirements.txt

### Setup AWS Credentials

The app requires access to your S3 buckets. You can provide AWS credentials in one of the following ways:

- Configure AWS CLI (`aws configure`) so `boto3` can pick up credentials automatically.
- Set environment variables:

export AWS_ACCESS_KEY_ID=your-access-key
export AWS_SECRET_ACCESS_KEY=your-secret-key
export AWS_DEFAULT_REGION=your-region

- Alternatively, create a `.env` file in the project root with:

AWS_ACCESS_KEY_ID=your-access-key
AWS_SECRET_ACCESS_KEY=your-secret-key
AWS_DEFAULT_REGION=your-region

and the app will load it using `python-dotenv`.

## Usage

Run the Streamlit app locally:

streamlit run app.py


### How to use the app:

1. Enter your S3 bucket name and the key (file path) of the CSV file in the sidebar.
2. Specify the sample size (number of random rows to load).
3. Click the **Profile S3 data sample** button to load a data sample.
4. Preview the sampled data shown in the app.
5. Select the columns you want to include in the profiling report using the multiselect box.
6. Click **Generate Profile Report** to generate and view the ydata-profiling report.

## Deployment

The app can be deployed on [Render.com](https://render.com) or similar cloud platforms using:

- Python 3 environment.
- The `requirements.txt` file for dependency installation.
- A start command similar to:

streamlit run app.py --server.port 10000 --server.address 0.0.0.0

Make sure to configure AWS credentials securely in the environment variables on the server.

---

## How it works

- The app streams a random sample of rows from your large CSV file in S3 to avoid downloading the entire file.
- Uses Polars for fast CSV reading.
- Converts to pandas DataFrame for compatibility with ydata-profiling.
- Lets you choose columns and create an interactive profile report for exploratory data analysis.

---
## The deliverables achieved here

-Viewing the profiling report.  

I have used S3 feature in AWS to upload my large dataset of 154mb,"https://www.kaggle.com/datasets/mishra5001/credit-card?select=application_data.csv".

Then I have just sampled random 1000 rows from this s3 bucket in this project, The free tier of render.com doesn't allow me to upload file more than 100mb to s3 i get axisos 502 error,so i uploaded the file manually to S3. Also note that we made ydataprofiling separate because the Streamlitcommunity cloud has python version 3.13 and we are not able to change that version,the version reset option is disabled from july 2025,so we used render.com to make a live URL of this.

Live URL : https://streamlit-ydataprofiling-by-aadhiya.onrender.com/
## License

MIT License

---

## Contact

Created by Aadhiya Maria Thomas  

GitHub: [aadhiya](https://github.com/aadhiya)

