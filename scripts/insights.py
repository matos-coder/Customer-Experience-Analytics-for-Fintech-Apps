import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def load_cleaned_data(file_path):
    """
    Load the cleaned review dataset for analysis.

    Parameters:
        file_path (str): Path to the cleaned review data.

    Returns:
        pd.DataFrame: Loaded DataFrame with cleaned data.
    """
    try:
        data = pd.read_csv(file_path)
        logging.info(f"Loaded data with {len(data)} records from {file_path}.")
        return data
    except Exception as e:
        logging.error(f"Error loading data: {e}")
        return pd.DataFrame()

def calculate_insights(data):
    """
    Derive key insights: drivers, pain points, and bank comparison.

    Parameters:
        data (pd.DataFrame): DataFrame with review, sentiment, and themes.

    Returns:
        dict: Insights organized by drivers, pain points, and bank comparison.
    """
    try:
        insights = {}
        for bank in data['bank'].unique():
            bank_data = data[data['bank'] == bank]
            drivers = bank_data[bank_data['sentiment_label'] == 'POSITIVE']['theme'].value_counts().head(2).index.tolist()
            pain_points = bank_data[bank_data['sentiment_label'] == 'NEGATIVE']['theme'].value_counts().head(2).index.tolist()
            insights[bank] = {
                "Drivers": drivers,
                "Pain Points": pain_points
            }
        logging.info("Insights calculated successfully.")
        return insights
    except Exception as e:
        logging.error(f"Error calculating insights: {e}")
        return {}

def generate_wordcloud(data, column, output_path):
    """
    Generate a word cloud for a specific column in the dataset.

    Parameters:
        data (pd.DataFrame): DataFrame containing text data.
        column (str): Column name for word cloud generation.
        output_path (str): Path to save the generated word cloud image.

    Returns:
        None
    """
    try:
        text = " ".join(data[column].dropna())
        wordcloud = WordCloud(background_color='white', max_words=200).generate(text)
        plt.figure(figsize=(10, 6))
        plt.imshow(wordcloud, interpolation="bilinear")
        plt.axis("off")
        plt.title("Word Cloud", fontsize=14)
        plt.savefig(output_path)
        plt.close()
        logging.info(f"Word cloud saved to {output_path}.")
    except Exception as e:
        logging.error(f"Error generating word cloud: {e}")

def visualize_sentiment_distribution(data, output_path):
    """
    Visualize the sentiment distribution across banks.

    Parameters:
        data (pd.DataFrame): DataFrame with sentiment data.
        output_path (str): Path to save the sentiment distribution plot.

    Returns:
        None
    """
    try:
        plt.figure(figsize=(10, 6))
        sns.countplot(data=data, x='bank', hue='sentiment_label', palette='coolwarm')
        plt.title("Sentiment Distribution by Bank")
        plt.xlabel("Bank")
        plt.ylabel("Count")
        plt.legend(title="Sentiment")
        plt.savefig(output_path)
        plt.close()
        logging.info(f"Sentiment distribution plot saved to {output_path}.")
    except Exception as e:
        logging.error(f"Error visualizing sentiment distribution: {e}")

def save_insights(insights, output_path):
    """
    Save insights as a text file.

    Parameters:
        insights (dict): Derived insights.
        output_path (str): Path to save insights.

    Returns:
        None
    """
    try:
        with open(output_path, "w") as file:
            for bank, details in insights.items():
                file.write(f"Bank: {bank}\n")
                file.write(f"  Drivers: {', '.join(details['Drivers'])}\n")
                file.write(f"  Pain Points: {', '.join(details['Pain Points'])}\n\n")
        logging.info(f"Insights saved to {output_path}.")
    except Exception as e:
        logging.error(f"Error saving insights: {e}")
