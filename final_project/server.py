import machinetranslation
from machinetranslation import translator
from flask import Flask, render_template, request
import json
from deep_translator import MyMemoryTranslator


app = Flask("Web Translator")


@app.route("/frenchToEnglish")
def frenchToEnglish(french_text):#  \n
    """Function printing python version."""
    english_text = MyMemoryTranslator(source="french", target="english").translate(french_text)
    return english_text# \r\nEOF

@app.route("/")
def englishToFrench(english_text):#  \n
    """Function printing python version."""
    french_text = MyMemoryTranslator(source="english", target="french").translate(english_text)
    return french_text# \nEOF

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
