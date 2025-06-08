# Customer Experience Analytics for Fintech Apps

This project aims to collect, preprocess, and analyze customer reviews from the Google Play Store for major Ethiopian fintech banking apps. The goal is to uncover user satisfaction drivers, pain points, and actionable insights for product improvement using modern data science and NLP techniques.

## Project Structure

- `notebooks/` – Jupyter notebooks for data collection, preprocessing, and analysis
- `scripts/` – Python scripts for scraping and analysis pipelines
- `data/raw/` – Raw review data (CSV files per bank)
- `data/processed/` – Processed and analyzed datasets
- `src/` – Additional source code modules
- `requirements.txt` – Python dependencies

## Tasks Overview

### Task 1: Data Collection and Preprocessing
- Scrape 400+ reviews per bank (Commercial Bank of Ethiopia, Bank of Abyssinia, Dashen Bank) using `google-play-scraper`.
- Preprocess data: remove duplicates, handle missing values, normalize dates.
- Save clean, combined dataset for analysis.
- All code and methodology in [`notebooks/web_scraping.ipynb`](notebooks/web_scraping.ipynb) and [`src/web_scraping.py`](src/web_scraping.py).

### Task 2: Sentiment and Thematic Analysis
- Compute sentiment scores for each review using DistilBERT (Hugging Face Transformers).
- Extract keywords and group them into 3–5 themes per bank (e.g., Account Access Issues, Transaction Performance).
- Save results with sentiment and theme annotations.
- All code and methodology in [`notebooks/analysis.ipynb`](notebooks/analysis.ipynb) and [`scripts/analysis.py`](scripts/analysis.py).

## How to Run

1. **Install dependencies:**
   ```powershell
   pip install -r requirements.txt
   ```
2. **Run web scraping:**
   - Use the notebook [`notebooks/web_scraping.ipynb`](notebooks/web_scraping.ipynb) or run the script in `src/web_scraping.py` to collect and preprocess reviews.
3. **Run analysis:**
   - Use [`notebooks/analysis.ipynb`](notebooks/analysis.ipynb) to perform sentiment and thematic analysis.

## Key Outputs
- `data/raw/all_banks_reviews.csv` – Cleaned, combined review dataset
- `data/processed/review_analysis.csv` – Reviews with sentiment and theme annotations

## Git Workflow
- Use feature branches for each task (e.g., `task-1`, `task-2`)
- Commit frequently with clear messages
- Merge via pull request for review and traceability

## References
- [google-play-scraper PyPI](https://pypi.org/project/google-play-scraper/)
- [Hugging Face Transformers](https://huggingface.co/transformers/)
- [spaCy](https://spacy.io/)
- [scikit-learn](https://scikit-learn.org/)
- [Pandas](https://pandas.pydata.org/)

## Next Steps
- Expand analysis to more banks or fintech apps
- Add advanced topic modeling or dashboarding
- Integrate user feedback for continuous improvement

For detailed methodology and results, see the README files in the `notebooks/` directory for each task.
