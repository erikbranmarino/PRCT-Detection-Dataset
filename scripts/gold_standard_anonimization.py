import pandas as pd
import re
from datetime import datetime
import hashlib
import numpy as np


def anonymize_text(text):
    """
    Anonymize text content by removing/replacing sensitive information
    """
    if pd.isna(text):
        return text

    # Replace usernames (common patterns)
    text = re.sub(r'@[\w\d_]+', '@[USER]', text)

    # Replace URLs
    text = re.sub(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', '[URL]', text)

    # Replace common time patterns
    text = re.sub(r'\d{1,2}:\d{2}(?::\d{2})?(?:\s*[AaPp][Mm])?', '[TIME]', text)

    # Replace email patterns
    text = re.sub(r'[\w\.-]+@[\w\.-]+\.\w+', '[EMAIL]', text)

    return text


def generate_consistent_id(original_id, salt="PRCT2025"):
    """
    Generate a consistent but anonymized ID using hashing
    """
    if pd.isna(original_id):
        return None

    # Create a hash of the original ID with a salt
    hash_object = hashlib.md5((str(original_id) + salt).encode())
    # Take first 8 characters of the hash
    return f"COMMENT_{hash_object.hexdigest()[:8]}"


def anonymize_timestamp(timestamp):
    """
    Convert timestamp to YYYY-MM format
    """
    if pd.isna(timestamp):
        return None

    try:
        # Parse the timestamp (adjust the format string as needed)
        dt = pd.to_datetime(timestamp)
        return dt.strftime('%Y-%m')
    except:
        return None


def anonymize_dataset(file_path, output_path):
    """
    Anonymize the gold standard dataset
    """
    # Read the dataset
    print("Reading dataset...")
    df = pd.read_excel(file_path)

    # Create a copy for anonymization
    anon_df = df.copy()

    # Columns to drop
    columns_to_drop = ['AuthorName', 'ParentCommentID', 'VideoID', 'ThreadID']
    anon_df = anon_df.drop(columns=columns_to_drop, errors='ignore')

    print("Anonymizing data...")

    # Anonymize CommentID
    anon_df['CommentID'] = df['CommentID'].apply(generate_consistent_id)

    # Anonymize text content
    anon_df['CommentText'] = df['CommentText'].apply(anonymize_text)
    if 'ParentCommentText' in anon_df.columns:
        anon_df['ParentCommentText'] = df['ParentCommentText'].apply(anonymize_text)

    # Anonymize timestamp
    if 'Timestamp' in anon_df.columns:
        anon_df['Timestamp'] = df['Timestamp'].apply(anonymize_timestamp)

    # Save anonymized dataset
    print("Saving anonymized dataset...")
    anon_df.to_csv(output_path, index=False)

    # Print summary
    print("\nAnonymization Summary:")
    print(f"Original columns: {list(df.columns)}")
    print(f"Anonymized columns: {list(anon_df.columns)}")
    print(f"Number of records processed: {len(df)}")
    print(f"\nAnonymized dataset saved to: {output_path}")


if __name__ == "__main__":
    input_path = "/Users/bran/Downloads/Youtube_PRCT_classification_gold_standard.xlsx"
    output_path = "/Users/bran/Downloads/anonymized_gold_standard.csv"

    try:
        anonymize_dataset(input_path, output_path)
        print("\nAnonymization completed successfully!")
    except Exception as e:
        print(f"Error during anonymization: {str(e)}")