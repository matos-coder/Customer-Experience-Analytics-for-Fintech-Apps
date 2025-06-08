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
