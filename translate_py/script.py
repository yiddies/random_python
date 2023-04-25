from translate import Translator
translator = Translator(to_lang="ja")
#translation = translator.translate("My name is chris")
#print(translation)
try:
    with open('text.txt', mode='r') as t:
        text = t.read()
        translation = translator.translate(text)
        print(translation)
except FileNotFoundError as e:
    print('No file found')
    