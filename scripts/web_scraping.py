# Import necessary libraries
from google_play_scraper import reviews_all
import pandas as pd
import os

# Define constants for scraping
BANK_APPS = {
    "Commercial Bank of Ethiopia": "com.cbe.customer",
    "Bank of Abyssinia": "com.bankofabyssinia",
    "Dashen Bank": "com.dashenbank"
}
OUTPUT_DIR = "data/raw"
os.makedirs(OUTPUT_DIR, exist_ok=True)  # Create directory if it doesn't exist

def scrape_reviews(app_id, bank_name, reviews_limit=400):
    """
    Scrapes up to `reviews_limit` reviews for a given app from the Google Play Store.

    Parameters:
        app_id (str): The unique identifier for the bank's app in the Google Play Store.
        bank_name (str): The name of the bank for labeling purposes.
        reviews_limit (int): Maximum number of reviews to scrape.

    Returns:
        pd.DataFrame: A DataFrame containing all reviews with relevant fields.
    """
    try:
        print(f"Scraping up to {reviews_limit} reviews for {bank_name}...")
        reviews = reviews_all(
            app_id,
            sleep_milliseconds=0,
            lang='en',
            country='us',
        )
        # Limit to the first `reviews_limit` reviews
        reviews = reviews[:reviews_limit]
        print(f"Raw data for {bank_name} (first 5):\n", reviews[:5])
        reviews_df = pd.DataFrame(reviews)
        reviews_df = reviews_df[["content", "score", "at"]].rename(
            columns={
                "content": "review",
                "score": "rating",
                "at": "date"
            }
        )
        reviews_df["bank"] = bank_name
        reviews_df["source"] = "Google Play Store"
        return reviews_df
    except Exception as e:
        print(f"Error while scraping reviews for {bank_name}: {e}")
        return pd.DataFrame()


def save_reviews(df, bank_name):
    """
    Saves the scraped reviews to a CSV file.

    Parameters:
        df (pd.DataFrame): The DataFrame containing the scraped reviews.
        bank_name (str): The name of the bank for file naming purposes.
    """
    try:
        # Define the output path
        output_path = os.path.join(OUTPUT_DIR, f"{bank_name.replace(' ', '_').lower()}_reviews.csv")
        
        # Save the DataFrame to a CSV file
        df.to_csv(output_path, index=False)
        print(f"Reviews for {bank_name} saved successfully at {output_path}.")
    except Exception as e:
        print(f"Error saving reviews for {bank_name}: {e}")

def main():
    """
    Main function to scrape reviews for all bank apps and save them as CSV files.
    """
    all_reviews = []

    for bank_name, app_id in BANK_APPS.items():
        # Scrape reviews for the bank
        bank_reviews = scrape_reviews(app_id, bank_name, reviews_limit=400)
        
        if not bank_reviews.empty:
            # Save reviews to a CSV file
            save_reviews(bank_reviews, bank_name)

            # Append to the master list
            all_reviews.append(bank_reviews)

    # Combine all reviews into a single DataFrame
    if all_reviews:
        combined_df = pd.concat(all_reviews, ignore_index=True)
        combined_path = os.path.join(OUTPUT_DIR, "all_banks_reviews.csv")
        combined_df.to_csv(combined_path, index=False)
        print(f"All reviews combined and saved to {combined_path}.")
    else:
        print("No reviews scraped. Please check for errors.")

if __name__ == "__main__":
    main()
