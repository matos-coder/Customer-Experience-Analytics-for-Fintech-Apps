import pandas as pd
import os
import numpy as np
from transformers import pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
import spacy
from collections import Counter
import logging

# Initialize logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Load spaCy English model
try:
    nlp = spacy.load("en_core_web_sm")
except Exception as e:
    logging.error(f"Error loading spaCy model: {e}")
    raise

# Initialize DistilBERT Sentiment Analyzer
try:
    sentiment_analyzer = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")
except Exception as e:
    logging.error(f"Error initializing DistilBERT pipeline: {e}")
    raise

def preprocess_text(text):
    """
    Preprocesses text data by tokenizing, removing stopwords, and lemmatizing.

    Parameters:
        text (str): Raw review text.

    Returns:
        str: Preprocessed text.
    """
    try:
        doc = nlp(text.lower())
        tokens = [token.lemma_ for token in doc if not token.is_stop and token.is_alpha]
        return " ".join(tokens)
    except Exception as e:
        logging.warning(f"Error during text preprocessing: {e}")
        return text  # Return raw text if preprocessing fails

def analyze_sentiment(reviews):
    """
    Performs sentiment analysis on a list of reviews.

    Parameters:
        reviews (pd.Series): A pandas Series of review texts.

    Returns:
        pd.DataFrame: A DataFrame with sentiment scores and labels.
    """
    try:
        sentiments = sentiment_analyzer(list(reviews))
        return pd.DataFrame(sentiments)
    except Exception as e:
        logging.error(f"Sentiment analysis failed: {e}")
        return pd.DataFrame()

def extract_keywords(reviews, top_n=20):
    """
    Extracts top keywords from reviews using TF-IDF.

    Parameters:
        reviews (pd.Series): A pandas Series of preprocessed review texts.
        top_n (int): Number of top keywords to return.

    Returns:
        list: List of top keywords.
    """
    try:
        vectorizer = TfidfVectorizer(max_features=top_n, ngram_range=(1, 2))
        X = vectorizer.fit_transform(reviews)
        feature_names = vectorizer.get_feature_names_out()
        return feature_names
    except Exception as e:
        logging.error(f"Keyword extraction failed: {e}")
        return []

def cluster_keywords(keywords):
    """
    Groups keywords into themes.

    Parameters:
        keywords (list): List of keywords.

    Returns:
        dict: A dictionary of themes with keywords grouped under them.
    """
    try:
        themes = {
            "Account Access Issues": [],
            "Transaction Performance": [],
            "User Interface & Experience": [],
            "Customer Support": [],
            "Feature Requests": []
        }
        # Example rule-based grouping
        for keyword in keywords:
            if "login" in keyword or "access" in keyword:
                themes["Account Access Issues"].append(keyword)
            elif "transfer" in keyword or "speed" in keyword:
                themes["Transaction Performance"].append(keyword)
            elif "UI" in keyword or "design" in keyword:
                themes["User Interface & Experience"].append(keyword)
            elif "support" in keyword or "help" in keyword:
                themes["Customer Support"].append(keyword)
            else:
                themes["Feature Requests"].append(keyword)
        return themes
    except Exception as e:
        logging.error(f"Clustering keywords failed: {e}")
        return {}

def save_analysis_results(df, output_path):
    """
    Saves the analysis results to a CSV file.

    Parameters:
        df (pd.DataFrame): DataFrame containing analysis results.
        output_path (str): File path for saving the results.

    Returns:
        None
    """
    try:
        # Ensure the output directory exists
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        df.to_csv(output_path, index=False)
        logging.info(f"Results saved to {output_path}")
    except Exception as e:
        logging.error(f"Failed to save results: {e}")
