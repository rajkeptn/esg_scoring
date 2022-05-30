import re
from nltk.stem import WordNetLemmatizer, PorterStemmer
from gensim.utils import simple_preprocess
from gensim.parsing.preprocessing import STOPWORDS


def load_nltk(path):
    import nltk
    nltk.data.path.append("{}/wordnet".format(path))
    nltk.data.path.append("{}/punkt".format(path))


def load_spacy(path):
    import spacy
    return spacy.load(path)


def clean_org_name(text):
    import re
    text = text.lower()
    name = []
    stop_words = {'group', 'inc', 'ltd', 'ag', 'plc', 'limited', 'sa', 'holdings'}
    stop_words = set(STOPWORDS.union(stop_words))
    for t in re.split('\\W', text):
        if len(t) > 0 and t not in stop_words:
            name.append(t)
    if len(name) > 0:
        return ' '.join(name).strip()
    else:
        return ''


def extract_organizations(text, nlp):
    doc = nlp(text)
    orgs = [X.text for X in doc.ents if X.label_ == 'ORG']
    return [clean_org_name(org) for org in orgs]


def lemmatize_text(text):
    results = []
    lemmatizer = WordNetLemmatizer()
    stemmer = PorterStemmer()
    for token in simple_preprocess(text):
        stem = stemmer.stem(lemmatizer.lemmatize(token))
        matcher = re.match('\w+', stem)
        if matcher:
            part = matcher.group(0)
            if len(part) > 3:
                results.append(part)
    return ' '.join(results)


def get_stopwords(organisations, path):
    load_nltk(path)
    org_stop_words = []
    for organisation in organisations:
        for t in re.split('\\W', organisation):
            l = lemmatize_text(t)
            if len(l) > 0:
                org_stop_words.append(l)
    stop_words = STOPWORDS.union(org_stop_words)
    return stop_words