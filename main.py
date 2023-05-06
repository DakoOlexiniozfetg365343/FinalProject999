from translate import Translator

def translate_text(text, source_lang, target_lang):
    translator = Translator(to_lang=target_lang, from_lang=source_lang)
    translation = translator.translate(text)
    return translation

len = input("На яку мову перевести текст?(es, en, ja, fr, hr, ar, sk, pl, ky, de, bg)")

# Головна частина програми
text = input("Введіть текст для перекладу: ")
translated_text = translate_text(text, 'uk', len)
print("Переклад:")
print(translated_text)
