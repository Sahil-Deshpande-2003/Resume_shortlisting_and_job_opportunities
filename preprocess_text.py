import import_nlp

nlp = import_nlp.nlp

def is_token_allowed(token):
     return bool(
         token
         and str(token).strip()
         and not token.is_stop
         and not token.is_punct
     )

def preprocess_token(token):
     return token.lemma_.strip().lower()

