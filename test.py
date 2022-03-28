from translate import Translator



translator = Translator(to_lang="en")
result = translator.translate('кто')
print(result)