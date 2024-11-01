import googletrans as trans
import streamlit as st
import time

# Set page title
st.set_page_config(page_title="Translator App", page_icon="🌐")

# Title and Description
st.title("🌐 Translator App")
st.write("Translate text easily between multiple languages.")

# Translator Object
translator = trans.Translator()

# Text Area for User Input
text = st.text_area("Enter your text", placeholder="Type or paste your text here...")

# Language Dictionary
languages = {'afrikaans': 'af', 'albanian': 'sq', 'amharic': 'am', 'arabic': 'ar', 'armenian': 'hy',
             'azerbaijani': 'az', 'basque': 'eu', 'belarusian': 'be', 'bengali': 'bn', 'bosnian': 'bs',
             'bulgarian': 'bg', 'catalan': 'ca', 'cebuano': 'ceb', 'chichewa': 'ny', 'chinese (simplified)': 'zh-cn',
             'chinese (traditional)': 'zh-tw', 'corsican': 'co', 'croatian': 'hr', 'czech': 'cs', 'danish': 'da',
             'dutch': 'nl', 'english': 'en', 'esperanto': 'eo', 'estonian': 'et', 'filipino': 'tl', 'finnish': 'fi',
             'french': 'fr', 'frisian': 'fy', 'galician': 'gl', 'georgian': 'ka', 'german': 'de', 'greek': 'el',
             'gujarati': 'gu', 'haitian creole': 'ht', 'hausa': 'ha', 'hawaiian': 'haw', 'hebrew': 'he', 'hindi': 'hi',
             'hmong': 'hmn', 'hungarian': 'hu', 'icelandic': 'is', 'igbo': 'ig', 'indonesian': 'id', 'irish': 'ga',
             'italian': 'it', 'japanese': 'ja', 'javanese': 'jw', 'kannada': 'kn', 'kazakh': 'kk', 'khmer': 'km',
             'korean': 'ko', 'kurdish (kurmanji)': 'ku', 'kyrgyz': 'ky', 'lao': 'lo', 'latin': 'la', 'latvian': 'lv',
             'lithuanian': 'lt', 'luxembourgish': 'lb', 'macedonian': 'mk', 'malagasy': 'mg', 'malay': 'ms',
             'malayalam': 'ml', 'maltese': 'mt', 'maori': 'mi', 'marathi': 'mr', 'mongolian': 'mn',
             'myanmar (burmese)': 'my', 'nepali': 'ne', 'norwegian': 'no', 'odia': 'or', 'pashto': 'ps',
             'persian': 'fa', 'polish': 'pl', 'portuguese': 'pt', 'punjabi': 'pa', 'romanian': 'ro', 'russian': 'ru',
             'samoan': 'sm', 'scots gaelic': 'gd', 'serbian': 'sr', 'sesotho': 'st', 'shona': 'sn', 'sindhi': 'sd',
             'sinhala': 'si', 'slovak': 'sk', 'slovenian': 'sl', 'somali': 'so', 'spanish': 'es', 'sundanese': 'su',
             'swahili': 'sw', 'swedish': 'sv', 'tajik': 'tg', 'tamil': 'ta', 'telugu': 'te', 'thai': 'th',
             'turkish': 'tr', 'ukrainian': 'uk', 'urdu': 'ur', 'uyghur': 'ug', 'uzbek': 'uz', 'vietnamese': 'vi',
             'welsh': 'cy', 'xhosa': 'xh', 'yiddish': 'yi', 'yoruba': 'yo', 'zulu': 'zu'}

# Select Target Language
target_language = st.selectbox("Choose language to translate to", list(languages.keys()))

# Buttons
col1, col2 = st.columns(2)
with col1:
    translate_button = st.button("Translate")
with col2:
    clear_button = st.button("Clear")

# Translate Action
if translate_button:
    with st.spinner("Translating..."):
        time.sleep(1)
    try:
        if text:
            # Detect source language
            detected = translator.detect(text)
            source_language = detected.lang
            translated_text = translator.translate(text, src=source_language, dest=languages[target_language])
            st.write(f"**Detected Language:** {trans.LANGUAGES.get(source_language, 'Unknown').capitalize()}")
            st.success(f"**Translated Text:** {translated_text.text}")
        else:
            st.warning("Please enter some text to translate.")
    except Exception as e:
        st.error("An error occurred during translation. Please try again.")
        st.write(e)

# Clear Text
if clear_button:
    st.text_area("Enter your text", "", key="text_area_key")  # Clear text by resetting the text area
