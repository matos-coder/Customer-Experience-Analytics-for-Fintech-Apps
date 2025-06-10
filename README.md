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


## 3. Sentiment & Thematic Analysis

### Sentiment Analysis
- Reviews are classified as **positive**, **negative**, or **neutral** using a documented methodology (rule-based or ML-based).
- Sentiment scores are stored for each review.

### Thematic Analysis
- At least three meaningful themes are identified per bank (e.g., Transaction Performance, App Reliability, Customer Support).
- Themes are assigned using keyword matching and clustering.
- Results are saved in structured CSVs and integrated into the database.

**Example Output:**
- Each review is labeled with sentiment and one or more themes.
- Top themes and sentiment distributions are computed per bank.

---

## 4. Insights & Visualizations

### Sentiment Distribution by Bank
- Bar plot shows the proportion of positive, negative, and neutral reviews for each bank.
- **Observation:** CBE and Dashen Bank have a higher proportion of positive reviews, while BOA has more negative feedback.

### Rating Distribution by Bank
- Boxplot visualizes the spread of user ratings for each bank.
- **Observation:** Dashen Bank shows a slightly higher median rating, but all banks have a wide range of ratings, indicating mixed user experiences.

### Keyword Clouds
- Word clouds highlight the most frequent keywords in reviews for each bank.
- **Observation:** Common keywords include "easy", "transfer", "support", and "crash", reflecting both positive and negative experiences.

### Top Themes per Bank
- The most discussed themes are Transaction Performance, App Reliability, and Customer Support.
- **Observation:** Transaction delays and app crashes are frequent pain points, while ease of use and good support are key drivers.

### Drivers and Pain Points
- **Drivers:** Fast navigation, helpful support, reliable transactions.
- **Pain Points:** App crashes, transaction failures, login/access issues.
- Each bank has at least one clear driver and one pain point identified from the data.

### Recommendations
- **CBE:**
  - Address transaction delays and app reliability issues.
  - Enhance user interface for easier navigation.
- **BOA:**
  - Improve app stability and reduce login problems.
  - Expand customer support channels.
- **Dashen Bank:**
  - Continue to improve transaction speed and reliability.
  - Address biometric login and update issues.

---

## 5. Ethics & Limitations

- **Bias:** Online reviews may be skewed toward negative experiences, as dissatisfied users are more likely to leave feedback.
- **Representativeness:** The sample may not represent the entire user base.
- **Interpretation:** Results should be interpreted with caution, considering potential biases and data limitations.

---

## 6. Code Modularity & Repository Structure

- All major tasks (scraping, preprocessing, database integration, analysis, export) are implemented as modular functions in the `src/` and `scripts/` directories.
- Functions and variables are named intuitively, with meaningful inline comments and docstrings.
- The repository uses a clear, modular folder structure.
- The `README.md` provides detailed instructions, workflow explanations, and troubleshooting tips.
- All ancillary files (requirements, SQL dump, etc.) are present and well-documented.

---

## 7. Conclusion & Next Steps

- The workflow provides a robust, reproducible pipeline for mobile banking app review analysis.
- Actionable insights and recommendations are generated for each bank.
- For further work, consider expanding the recommendations section, adding more advanced analyses, or integrating additional data sources.
- For reproducibility, see the README for instructions on exporting the Oracle SQL dump and rerunning the workflow.

---

**Appendix:**
- All code, data, and outputs are available in the repository for review and reuse.
- Plots and visualizations are saved in the `notebooks/` directory.
- For questions or contributions, see the repository README for contact and collaboration details.
