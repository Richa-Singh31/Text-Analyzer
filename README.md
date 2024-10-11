# Text Analyzer

## Description
A text analyzer that takes the URL of a website and performs web scraping and analysis providing the positive score, negative score, word frequency and more for the content.

## Key Components
- Web Scraper: The web scraper component automates the extraction of large amount of data from websites efficiently. It involves retrieving and parsing the HTML content to collect specific information.
- Text Analyzer: This component performs sentiment analysis and computes various linguistic metrics from a given text. It loads custom and NLTK stopwords, and uses dictionaries of positive and negative words to calculate sentiment scores. It measures polarity, subjectivity, average sentence length, percentage of complex words, fog index, word count, syllables per word, personal pronoun count, and average word length. The text is lemmatized for normalization.

## Install Dependencies
```bash
pip install -r requirements.txt
```
## Run the app
```bash
python main.py
```
## Conclusion
Text Analyzer provides a comprehensive text analysis tool that leverages natural language processing (NLP) techniques to derive meaningful insights from textual data. By incorporating sentiment analysis, syntactic metrics, and readability scores such as the Fog Index, the tool can assess the tone, complexity, and structure of the content. It utilizes custom stopwords and sentiment dictionaries to tailor the analysis, ensuring more accurate and contextually relevant results. This project is a valuable resource for applications in content analysis, sentiment detection, and readability improvement, and can be further extended for more advanced use cases like real-time text monitoring or integration with other NLP tools.
