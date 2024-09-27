def single_root_words(root_word,*other_words):
    same_words = list()
    for i in range(len(other_words)):
        if root_word.upper() in other_words[i].upper():
            same_words.append(other_words[i])
        elif other_words[i].upper() in root_word.upper():
            same_words.append(other_words[i])
    return same_words

print(single_root_words('Лес', 'лестница', 'Слезать', 'Лемник', 'лЕсок'))
print(single_root_words('Катализатор', 'За', 'Тор','Затор'))
