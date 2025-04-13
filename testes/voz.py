from gtts import gTTS
from pygame import mixer

voz = gTTS("", lang = 'pt')
voz.save('voz.mp3')#salva o áudio na pasta do projeto
mixer.init()#inicializa o mixer para executar o som
mixer.music.load('voz.mp3')#carrega o áudio
mixer.music.play()#executa o áudio

fim = input("digite algo para finalizar")
