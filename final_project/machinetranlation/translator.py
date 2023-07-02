"""Module providingFunction printing python version."""
from deep_translator import MyMemoryTranslator
def englishToFrench(english_text):#  \n
    """Function printing python version."""
    french_text = MyMemoryTranslator(source="english", target="french").translate(english_text)
    return french_text# \nEOF
def frenchToEnglish(french_text):#  \n
    """Function printing python version."""
    english_text = MyMemoryTranslator(source="french", target="english").translate(french_text)
    return english_text# \r\nEOF