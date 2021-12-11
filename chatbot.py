import bs4 as bs
import urllib.request
import re
import nltk
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer


# function to answer a query
def querries(query):
    gett_data = urllib.request.urlopen("https://en.wikipedia.org/wiki/India").read()
    gett_data_paragraphs = bs.BeautifulSoup(gett_data, 'lxml').find_all('p')
    gett_text = ''
    for p in gett_data_paragraphs:
        gett_text += p.text.lower()
    # print(gett_text)

    gett_text = re.sub(r'\s+', ' ', re.sub(r'\[[0-9]*]', ' ', gett_text))

    nltk.download('punkt')
    gett_sentences = nltk.sent_tokenize(gett_text)



    def chatbot_answer(user_query):
        # Append the query to the sentences list
        gett_sentences.append(user_query)
        # Create the sentences vector based on the list
        vectorizer = TfidfVectorizer()
        sentences_vectors = vectorizer.fit_transform(gett_sentences)

        # Measure the cosine similarity and take the second closest index because the first index is the user query
        vector_values = cosine_similarity(sentences_vectors[-1], sentences_vectors)
        answer = gett_sentences[vector_values.argsort()[0][-2]]
        # Final check to make sure there are result present. If all the result are 0, means the text input by us are not captured in the corpus
        input_check = vector_values.flatten()
        input_check.sort()

        if input_check[-2] == 0:
            return "Please Try again"
        else:
            return answer

    while True:
        # query = input().lower()
        if query not in ['bye', 'good bye', 'take care']:
            lmnop = chatbot_answer(query)
            gett_sentences.remove(query)
            return lmnop
        else:
            return "See You Again"
            break
