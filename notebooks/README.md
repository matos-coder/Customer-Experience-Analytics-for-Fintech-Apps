# Task 1: Data Collection and Preprocessing – Google Play Store Reviews

This folder contains the code and notebooks for Task 1: scraping, preprocessing, and saving customer reviews from the Google Play Store for selected fintech banking apps.

## Objective

Collect, clean, and organize user reviews for three major Ethiopian banks' mobile apps from the Google Play Store. Prepare the data for downstream analysis and ensure all work is version-controlled via GitHub.

## Workflow Overview

The workflow is implemented in [`notebooks/web_scraping.ipynb`](web_scraping.ipynb) and supporting scripts in [`../src/web_scraping.py`](../src/web_scraping.py):

### 1. Git Setup
- Create a GitHub repository for the project.
- Include a `.gitignore` and `requirements.txt` for dependency management.
- Work on a dedicated `task-1` branch.
- Commit frequently with clear, descriptive messages after each logical chunk of work or work session.

### 2. Web Scraping
- Use the `google-play-scraper` Python package to collect reviews, ratings, dates, and app names for:
  - Commercial Bank of Ethiopia
  - Bank of Abyssinia
  - Dashen Bank
- Target at least 400 reviews per bank (1,200+ reviews total).
- Store raw reviews in CSV files, one per bank, in `data/raw/`.

### 3. Preprocessing
- Remove duplicate reviews.
- Handle missing data (drop or impute as appropriate).
- Normalize date formats to `YYYY-MM-DD`.
- Save the cleaned dataset as a CSV with columns: `review`, `rating`, `date`, `bank`, `source`.

### 4. Data Management
- All raw and processed data is saved in the `data/raw/` directory.
- The combined, cleaned dataset is saved as `all_banks_reviews.csv`.

## Key Performance Indicators (KPIs)
- **1,200+ reviews** collected with **less than 5% missing data**.
- Clean, well-structured CSV dataset for analysis.
- Organized Git repository with clear, frequent commits. 

## Minimum Essential Requirements
- Scrape at least 400 reviews per bank (1,200 total).
- Commit a preprocessing script to the repository.
- Update this README with a summary of the methodology and workflow.

## References
- [google-play-scraper PyPI](https://pypi.org/project/google-play-scraper/)
- [pandas Documentation](https://pandas.pydata.org/)
- [GitHub Docs: Getting Started](https://docs.github.com/en/get-started/quickstart)

## Example Output
- Individual CSV files for each bank in `data/raw/`.
- Combined, cleaned CSV: `data/raw/all_banks_reviews.csv`.

## Customization
- To add more banks, update the `BANK_APPS` dictionary in the scraping script.
- Adjust review targets or preprocessing steps as needed for your analysis.

# Task 2: Sentiment and Thematic Analysis – Google Play Store Reviews

This folder contains the code and notebooks for Task 2: quantifying review sentiment and identifying key themes in user feedback for fintech banking apps.

## Objective

Analyze user reviews to uncover satisfaction drivers and pain points by computing sentiment scores and extracting recurring themes from the data collected in Task 1.

## Workflow Overview

The workflow is implemented in [`notebooks/analysis.ipynb`](analysis.ipynb) and supporting scripts in [`../scripts/analysis.py`](../scripts/analysis.py):

### 1. Sentiment Analysis
- Use the `distilbert-base-uncased-finetuned-sst-2-english` model (via Hugging Face Transformers) to compute sentiment scores (positive, negative, neutral) for each review.
- Optionally, compare with simpler libraries like VADER or TextBlob if time permits.
- Aggregate sentiment by bank and rating (e.g., mean sentiment for 1-star reviews).

### 2. Thematic Analysis
- Extract significant keywords and n-grams using TF-IDF or spaCy (e.g., “login error”, “slow transfer”, “good UI”).
- Group related keywords and phrases into 3–5 overarching themes per bank (e.g., 'Account Access Issues', 'Transaction Performance', 'User Interface & Experience', 'Customer Support', 'Feature Requests').
- Document the logic used for grouping keywords into themes.

### 3. Pipeline & Preprocessing
- Preprocess review text (tokenization, stop-word removal, lemmatization) using Pandas and NLP libraries (spaCy, sklearn).
- Save results as CSV (e.g., review_id, review_text, sentiment_label, sentiment_score, identified_theme(s)).
- Modular code for easy extension and reproducibility.

### 4. Data Management
- All processed data and analysis results are saved in the `data/processed/` directory.
- The main output is `review_analysis.csv` containing sentiment and theme annotations for each review.

### 5. Git Workflow
- Use a dedicated `task-2` branch for all Task 2 work.
- Commit scripts and notebooks with clear, descriptive messages.
- Merge changes via pull request for review and traceability.

## Key Performance Indicators (KPIs)
- Sentiment scores computed for 90%+ of reviews.
- At least 3 themes identified per bank, with representative examples.
- Modular, well-documented pipeline code.

## Minimum Essential Requirements
- Sentiment scores for at least 400 reviews.
- At least 2 themes per bank, identified via keywords.
- Commit the analysis script to the repository.

## References
- [Hugging Face Transformers: distilbert-base-uncased-finetuned-sst-2-english](https://huggingface.co/distilbert-base-uncased-finetuned-sst-2-english)
- [spaCy Documentation](https://spacy.io/)
- [scikit-learn TF-IDF Vectorizer](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html)
- [Pandas Documentation](https://pandas.pydata.org/)
- [VADER Sentiment Analysis](https://github.com/cjhutto/vaderSentiment)
- [TextBlob Documentation](https://textblob.readthedocs.io/en/dev/)

## Example Output
- Processed CSV: `data/processed/review_analysis.csv` with columns for review text, sentiment label, sentiment score, and identified themes.
- Summary statistics and theme examples per bank.

## Customization
- To analyze additional banks or adjust theme grouping, update the relevant sections in the analysis script.
- The pipeline is modular and can be extended with new models or clustering techniques as needed.
