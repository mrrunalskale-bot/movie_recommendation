import spacy as sp
nlp = sp.load('en_core_web_sm')

def lower_replace(series):
    series = series.str.lower()
    series = series.str.replace(r"\[.*?\]", "", regex=True)
    series = series.str.replace(r"[^a-z0-9\s]", "", regex=True)
    return series

def important_words(text):
    doc = nlp(text)
    words = []
    for token in doc:
        if not token.is_stop:
            words.append(token.lemma_)    
    sentence = ' '.join(words)
    return sentence

def nlp_pipeline(series):
    series = lower_replace(series)
    series = series.apply(important_words)
    return series