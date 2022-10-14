import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import csv_reader
from utils import *
import jieba

import matplotlib.pyplot as plt

from wordcloud import WordCloud, STOPWORDS


def find_frequency(df):
    stop_words = set(stopwords.words("english"))
    stop_words.update({'http', 'https', 'google', 'com'})
    ps = PorterStemmer()
    searched_sentences = df['INFO']

    # print(searched_sentences)
    filtered_sentence = []
    for sentence in searched_sentences:
        if sentence.encode('utf-8').isalpha():
            tokenized_word = nltk.regexp_tokenize(sentence, r'\w+|\S\w')
        else:
            tokenized_word = list(jieba.cut_for_search(sentence))
        # tokenized_word = Text(sentence).words
        filtered_sentence += [w for w in tokenized_word if w not in stop_words]
    stemmed_sentence = [ps.stem(w) for w in filtered_sentence]
    # print(filtered_sentence)
    # print(stemmed_sentence)
    return " ".join(stemmed_sentence)


def plot_cloud(wordcloud):
    # Set figure size
    plt.figure(figsize=(40, 30))
    # Display image
    plt.imshow(wordcloud)
    # No axis details
    plt.axis("off")
    plt.show()


if __name__ == "__main__":
    df = csv_reader.read_from_csv(SEARCH_ACTIVITY_CSV_PATH)
    start_date = "2020-12-01"
    filtered_df = csv_reader.get_one_week_data(df, start_date)
    week_result = find_frequency(filtered_df)
    wordcloud = WordCloud(width=3000, height=2000, random_state=1, background_color='salmon', colormap='Pastel1',
                          collocations=False, stopwords=STOPWORDS).generate(week_result)
    plot_cloud(wordcloud)
