from gtts import gTTS

# Початковий текст
text = 'Привіт, світ!'

# Отримуємо результат
obj = gTTS(text, lang='ru')

# Зберігаємо в файл
obj.save('hw.mp3')