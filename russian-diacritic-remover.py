input_text = input('Input text to be stripped of diacritics: '); 
print(input_text)  

character_dict = {
    'ý' : 'э',
    'Ý': 'Э',
    'î': 'o',
    'Î': 'O', 
    'å': 'e',
    'Å': 'E',  
    'à': 'а',
    'À': 'А', 
    'û': 'ы',
    'Û': 'Ы',  
    'è': 'и',
    'ÿ': 'я',
    'Ÿ': 'Я', 
    'ó': 'у',
    'Ó': 'У',
    'È': 'И', 
    'þ ': 'ю', 
    'Þ': 'ю'

}
text = input_text 
for char in character_dict: 
    text = text.replace(char, character_dict[char]) 
print('\n ' + text + '\n')   

