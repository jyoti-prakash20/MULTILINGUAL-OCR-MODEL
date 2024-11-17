import cv2
import pytesseract
import googletrans
import tkinter as tk
from tkinter import filedialog
from PIL import Image


def detect_text(image):
    return []  


def recognize_text(image, lang='eng'):
    text = pytesseract.image_to_string(image, lang=lang)
    return text


def translate_text(text, dest_lang):
    translator = googletrans.Translator()
    translated_text = translator.translate(text, dest=dest_lang)
    return translated_text.text


def process_image():

    image_path = filedialog.askopenfilename()

    
    image = cv2.imread(image_path)

    
    boxes = detect_text(image)


    recognized_text = recognize_text(image)

    
    selected_language = languages[lang_choice.get()]

    
    translated_text = translate_text(recognized_text, selected_language)

    
    text_storage.append({'Extracted': recognized_text, 'Translated': translated_text})

    
    update_text_storage_display()


def update_text_storage_display():
    storage_text.delete('1.0', tk.END)
    for idx, item in enumerate(text_storage, start=1):
        storage_text.insert(tk.END, f"Text {idx}:\nExtracted: {item['Extracted']}\nTranslated: {item['Translated']}\n\n")


window = tk.Tk()
window.title("OCR and Translation")
window.geometry("800x600")  


window.configure(background='purple')


browse_button = tk.Button(window, text="Browse Image", command=process_image)
browse_button.pack(pady=10)


languages = {
    'Afrikaans': 'af',
    'Albanian': 'sq',
    'Amharic': 'am',
    'Arabic': 'ar',
    'Armenian': 'hy',
    'Azerbaijani': 'az',
    'Basque': 'eu',
    'Belarusian': 'be',
    'Bengali': 'bn',
    'Bosnian': 'bs',
    'Bulgarian': 'bg',
    'Catalan': 'ca',
    'Cebuano': 'ceb',
    'Chichewa': 'ny',
    'Chinese (Simplified)': 'zh-cn',
    'Chinese (Traditional)': 'zh-tw',
    'Corsican': 'co',
    'Croatian': 'hr',
    'Czech': 'cs',
    'Danish': 'da',
    'Dutch': 'nl',
    'English': 'en',
    'Esperanto': 'eo',
    'Estonian': 'et',
    'Filipino': 'tl',
    'Finnish': 'fi',
    'French': 'fr',
    'Frisian': 'fy',
    'Galician': 'gl',
    'Georgian': 'ka',
    'German': 'de',
    'Greek': 'el',
    'Gujarati': 'gu',
    'Haitian Creole': 'ht',
    'Hausa': 'ha',
    'Hawaiian': 'haw',
    'Hebrew': 'iw',
    'Hindi': 'hi',
    'Hmong': 'hmn',
    'Hungarian': 'hu',
    'Icelandic': 'is',
    'Igbo': 'ig',
    'Indonesian': 'id',
    'Irish': 'ga',
    'Italian': 'it',
    'Japanese': 'ja',
    'Javanese': 'jw',
    'Kannada': 'kn',
    'Kazakh': 'kk',
    'Khmer': 'km',
    'Korean': 'ko',
    'Kurdish (Kurmanji)': 'ku',
    'Kyrgyz': 'ky',
    'Lao': 'lo',
    'Latin': 'la',
    'Latvian': 'lv',
    'Lithuanian': 'lt',
    'Luxembourgish': 'lb',
    'Macedonian': 'mk',
    'Malagasy': 'mg',
    'Malay': 'ms',
    'Malayalam': 'ml',
    'Maltese': 'mt',
    'Maori': 'mi',
    'Marathi': 'mr',
    'Mongolian': 'mn',
    'Myanmar (Burmese)': 'my',
    'Nepali': 'ne',
    'Norwegian': 'no',
    'Odia': 'or',
    'Pashto': 'ps',
    'Persian': 'fa',
    'Polish': 'pl',
    'Portuguese': 'pt',
    'Punjabi': 'pa',
    'Romanian': 'ro',
    'Russian': 'ru',
    'Samoan': 'sm',
    'Scots Gaelic': 'gd',
    'Serbian': 'sr',
    'Sesotho': 'st',
    'Shona': 'sn',
    'Sindhi': 'sd',
    'Sinhala': 'si',
    'Slovak': 'sk',
    'Slovenian': 'sl',
    'Somali': 'so',
    'Spanish': 'es',
    'Sundanese': 'su',
    'Swahili': 'sw',
    'Swedish': 'sv',
    'Tajik': 'tg',
    'Tamil': 'ta',
    'Telugu': 'te',
    'Thai': 'th',
    'Turkish': 'tr',
    'Ukrainian': 'uk',
    'Urdu': 'ur',
    'Uzbek': 'uz',
    'Vietnamese': 'vi',
    'Welsh': 'cy',
    'Xhosa': 'xh',
    'Yiddish': 'yi',
    'Yoruba': 'yo',
    'Zulu': 'zu'
}
lang_choice = tk.StringVar(window)
lang_choice.set('English')  
language_menu = tk.OptionMenu(window, lang_choice, *languages.keys())
language_menu.pack(pady=5)


text_storage = []


storage_text = tk.Text(window, width=100, height=120)
storage_text.pack(pady=10)


window.mainloop()