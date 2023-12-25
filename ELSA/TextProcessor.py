import spacy

class TextProcessor:
    
    def __init__(self):
        self.nlp = spacy.load("en_core_web_sm")
        pass
    
    def phrase_similarity_extractor(self,phrase1,phrase2):
        phrase1,phrase2 = self.nlp(phrase1), self.nlp(phrase2)
        return phrase1.similarity(phrase2)
        
    