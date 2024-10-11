import os
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.tag import pos_tag

class TextAnalyzer:
    def __init__(self, stopwords_dir, master_dict_dir):
        self.custom_stop_words = self.load_stopwords(stopwords_dir)
        self.nltk_stop_words = set(stopwords.words('english'))
        self.all_stop_words = self.custom_stop_words.union(self.nltk_stop_words)
        self.positive_words, self.negative_words = self.load_word_dicts(master_dict_dir)
        self.lemmatizer = WordNetLemmatizer()

    def load_stopwords(self, stopwords_dir):
        stop_words = set()
        for filename in os.listdir(stopwords_dir):
            filepath = os.path.join(stopwords_dir, filename)
            with open(filepath, 'r') as file:
                stop_words.update(file.read().lower().splitlines())
        return stop_words

    def load_word_dicts(self, master_dict_dir):
        positive_dict_file = os.path.join(master_dict_dir, 'positive-words.txt')
        negative_dict_file = os.path.join(master_dict_dir, 'negative-words.txt')
        
        with open(positive_dict_file, 'r') as file:
            positive_words = set(file.read().lower().splitlines()) - self.all_stop_words
        
        with open(negative_dict_file, 'r') as file:
            negative_words = set(file.read().lower().splitlines()) - self.all_stop_words
        
        return positive_words, negative_words

    def count_syllables(self, word):
        vowels = 'aeiou'
        word = word.lower()
        syllable_count = 0
        if word[0] in vowels:
            syllable_count += 1
        for index in range(1, len(word)):
            if word[index] in vowels and word[index - 1] not in vowels:
                syllable_count += 1
        if word.endswith('es') or word.endswith('ed'):
            syllable_count -= 1
        if syllable_count == 0:
            syllable_count = 1
        return syllable_count

    def analyze_text(self, article_text):
        words = word_tokenize(article_text.lower())
        words = [re.sub(r'[^\w\s]', '', word) for word in words if word.isalpha()]
        lemmatized_words = [self.lemmatizer.lemmatize(word) for word in words]
        cleaned_words = [word for word in lemmatized_words if word not in self.all_stop_words]
        sentences = sent_tokenize(article_text)

        positive_score = sum(1 for word in cleaned_words if word in self.positive_words)
        negative_score = sum(1 for word in cleaned_words if word in self.negative_words)
        polarity_score = (positive_score - negative_score) / ((positive_score + negative_score) + 0.000001)
        subjectivity_score = (positive_score + negative_score) / (len(cleaned_words) + 0.000001)
        avg_sentence_length = len(cleaned_words) / len(sentences) if sentences else 0

        complex_words = [word for word in cleaned_words if self.count_syllables(word) > 2]
        complex_word_count = len(complex_words)
        percentage_complex_words = complex_word_count / len(cleaned_words) if cleaned_words else 0

        fog_index = 0.4 * (avg_sentence_length + percentage_complex_words)
        word_count = len(cleaned_words)
        syllable_count_per_word = sum(self.count_syllables(word) for word in cleaned_words) / len(cleaned_words) if cleaned_words else 0

        pos_tags = pos_tag(words)
        personal_pronoun_tags = ['PRP', 'PRP$']
        personal_pronouns_count = sum(1 for word, tag in pos_tags if tag in personal_pronoun_tags)

        avg_word_length = sum(len(word) for word in cleaned_words) / len(cleaned_words) if cleaned_words else 0

        return {
            'POSITIVE_SCORE': positive_score,
            'NEGATIVE_SCORE': negative_score,
            'POLARITY_SCORE': polarity_score,
            'SUBJECTIVITY_SCORE': subjectivity_score,
            'AVG_SENTENCE_LENGTH': avg_sentence_length,
            'PERCENTAGE_OF_COMPLEX_WORDS': percentage_complex_words,
            'FOG_INDEX': fog_index,
            'WORD_COUNT': word_count,
            'SYLLABLE_PER_WORD': syllable_count_per_word,
            'PERSONAL_PRONOUNS': personal_pronouns_count,
            'AVG_WORD_LENGTH': avg_word_length
        }

