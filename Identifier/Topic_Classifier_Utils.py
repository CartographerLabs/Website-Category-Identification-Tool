# NLP Dependancies
import os

import spacy
import nltk
import pickle
import gensim

from spacy.lang.en import English
from nltk.corpus import wordnet as wn
from nltk.stem.wordnet import WordNetLemmatizer

spacy.load('en_core_web_sm')
nltk.download('wordnet')


# Tokenisation
# We use the following function to clean our texts and return a list of tokens:

def tokenize(text):
    parser = English()
    lda_tokens = []
    tokens = parser(text)
    for token in tokens:
        if token.orth_.isspace():
            continue
        elif token.like_url:
            lda_tokens.append('URL')
        elif token.orth_.startswith('@'):
            lda_tokens.append('SCREEN_NAME')
        else:
            lda_tokens.append(token.lower_)
    return lda_tokens


def get_lemma(word):
    lemma = wn.morphy(word)
    if lemma is None:
        return word
    else:
        return lemma


def get_lemma2(word):
    return WordNetLemmatizer().lemmatize(word)


def get_stop_words():
    '''
    Makes a set (unordered list) of all of the stop words NLTK recommends
    '''
    return set(nltk.corpus.stopwords.words('english'))


def prepare_text_for_lda(text):
    tokens = tokenize(text)
    tokens = [token for token in tokens if len(token) > 4]  # Removes words in list less than 5 characters
    tokens = [token for token in tokens if
              token not in get_stop_words()]  # Removes words in the list that are stop words
    tokens = [get_lemma(token) for token in
              tokens]  # Performs stemming and Stemming and lemmatization on all words in list
    return tokens


def get_tokens_from_csv(csv_file_name, pickle_file_name, force_new_file):
    pickle_file_name = pickle_file_name + ".pkl"

    # If token data already exists then it loads it instead
    if not os.path.exists(pickle_file_name) and force_new_file:
        token_data = []

        with open(csv_file_name) as f:
            for line in f:
                tokens = prepare_text_for_lda(line)
                # print(tokens)
                token_data.append(tokens)

        pickle.dump(token_data, open(pickle_file_name, 'wb'))

    else:
        token_data = pickle.load(open(pickle_file_name, 'rb'))

    return token_data


def create_dictionary_from_tokens(token_data, file_name, force_new_file):
    '''
    Dictionary encapsulates the mapping between normalized words and their integer ids
    '''

    file_name = file_name + ".gensim"

    # If file already exists use it, else make new one.
    if not os.path.exists(file_name) and force_new_file:
        dictionary = gensim.corpora.Dictionary(token_data)
        dictionary.save(file_name)  # Saves to storage so large objects don't have to be stored in memory.

    else:
        dictionary = gensim.corpora.Dictionary.load(file_name)

    return dictionary


def create_a_corpus(dictionary, token_data, file_name, force_new_file):
    """
    Converts each list of words (document) into a bag of words format
    The corpus is a bag of words from each document
    """

    file_name = file_name + ".pkl"

    # If the pickle file exists for the corpus then load it.
    if not os.path.exists(file_name) or force_new_file:
        corpus = [dictionary.doc2bow(text) for text in token_data]
        pickle.dump(corpus, open(file_name, 'wb'))
    else:
        corpus = pickle.load(open(file_name, 'rb'))

    return corpus


def train_lda_model(corpus, number_of_topics, dictionary, file_name, force_new_file):
    """
    Training an LDA model
    Identifying 5 topics in the data.
    """
    file_name = file_name + ".gensim"

    if not os.path.exists(file_name) or force_new_file:
        lda_model = gensim.models.ldamodel.LdaModel(corpus, num_topics=number_of_topics, id2word=dictionary, passes=15)
        lda_model.save(file_name)  # Saves to storage so large objects don't have to be stored in memory.

    else:
        lda_model = gensim.models.ldamodel.LdaModel.load(file_name)

    return lda_model


def get_topic_of_document(dictionary, lda_model, new_document_string_text):
    new_doc = new_document_string_text
    new_doc = prepare_text_for_lda(new_doc)
    new_doc_bow = dictionary.doc2bow(new_doc)

    # print("The stem '{}' is used {} times".format(word, quantity))

    # print(new_doc_bow)

    # Here we use the LDA object we've trained and provide the new document to get it's topics - These probabilities add up to 1
    list_of_topic_fit = lda_model.get_document_topics(new_doc_bow)

    return list_of_topic_fit


def get_topic_best_fit_human_readable_name(topic, lda_model, dictionary):
    list_of_tokens = lda_model.get_topic_terms(topic[0])

    token = get_highest_weighted(list_of_tokens)
    token = dictionary[token]

    return token


def get_highest_weighted(list_of_tokens):
    most_weighted_token = ''
    most_fitted_token_weight = 0

    # Loops through the individual tokens with high weightings in each topic
    for token_data in list_of_tokens:
        token = token_data[0]
        weight = token_data[1]

        # Finds the highest weighting and returns it
        if weight > most_fitted_token_weight:
            most_fitted_token_weight = weight
            most_weighted_token = token

    return most_weighted_token