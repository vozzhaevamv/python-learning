##Панграмма — это предложение, в котором хотя бы раз встречается каждая буква алфавита. Например, предложение "Быстрая бурая лиса перепрыгивает через ленивую собаку" является панграммой, потому что в нем используются буквы A-Z по крайней мере один раз (регистр значения не имеет).

##Получив строку, определите, является ли она панграммой. Верните True, если это так, False,
# 
# если нет. Игнорируйте цифры и знаки препинания.
st =[ "The quick brown fox jumps over the lazy dog.",
                     "Cwm fjord bank glyphs vext quiz",
                     "Pack my box with five dozen liquor jugs.",
                     "How quickly daft jumping zebras vex.",
                     "ABCD45EFGH,IJK,LMNOPQR56STUVW3XYZ" ]
def is_pangram(st):
    st = st.lower()
    st1= set()
    for letter in st:
        if letter.isalpha():
            st1.add(letter)
    if len(st1) == 26:
        return True
    return False