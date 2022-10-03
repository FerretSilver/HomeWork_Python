word = 'Напишите абв программу, удаляющую из текста все слова, содержащие ""абв"".'
col = word.split()
new_col = [item for item in col if 'абв' not in item]
print(col)
print(new_col)