#modulos que precisa,
#requests e time

import requests as rq
from time import sleep

def numero(objeto):
    while True:
        try:
            num = int(input(f'numero do {objeto} da contagem: '))
            return num
        except: pass

def letra(objeto):
    while True:
        try:
            num = int(input(f'numero do {objeto} da contagem: '))
            return num
        except: pass

inicio = numero('inicio')
fim = numero('fim')
playload= {
    'content': "menssagem",
}
header={
    'authorization': 'autenticado'

}

chat= str(input('Digite o Id do chat: '))
header['authorization']= str(input('digite seu authorization: '))
if inicio == -1 and fim == 0:
    pvb = True

for c in range(inicio,fim+1):
    if pvb:
        cb = str(input('digite sua frase: '))
        if cb == '0stop':break
        playload['content'] = cb
        c-=1
    else: playload['content'] = c
    r = rq.post(f"https://discord.com/api/v8/channels/{chat}/messages", data=playload , headers=header)
    if str  (r) == '<Response [200]>':
        print('enviado com sucesso')
    else:
        print(f'erro {r}')
        c=-1
        break
        
    if c== fim: 
        break
    sleep(1.5) 