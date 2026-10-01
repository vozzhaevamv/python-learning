##Дополните метод/функцию так, чтобы она преобразовывала слова, разделенные дефисом или подчеркиванием, в верблюжий регистр. Первое слово в выводе должно быть написано с заглавной буквы только в том случае, если исходное слово было написано с заглавной буквы (так называемый верхний верблюжий регистр, который также часто называют регистром Паскаля). Следующие слова всегда должны начинаться с заглавной буквы.

##Примеры
##"the-stealth-warrior" преобразуется в "theStealthWarrior"

##"The_Stealth_Warrior" преобразуется в "TheStealthWarrior"

##"The_Stealth-Warrior" преобразуется в "TheStealthWarrior"

##Мое решение
def to_camel_case(text):
    text = text.replace("-","_")
    text = text.split("_")
    tx = []
    tx0=[text[0]]
    for word in text[1:]:
        tx.append(word.capitalize())
    return str("".join(tx0 + tx))


##Классное решение
def to_camel_case(text):
    removed = text.replace('-', ' ').replace('_', ' ').split()
    if len(removed) == 0:
        return ''
    return removed[0]+ ''.join([x.capitalize() for x in removed[1:]])