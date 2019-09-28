import json

digito = ['1','2','3','4','5','6','7','8','9','0']
teminais = ['1','2','3','4','5','6','7','8','9','0','/']
naoTerminais = ['Data','Dia','Mes','Ano']
tokenL = []
data = input('Digite a Data para analixe: ')
erro = None
cont = 0
while cont<len(data):
    if data[cont] in teminais:
        tokenL.append(data[cont])
        cont+=1
    else:
        erro = 'Erro Lexico, token: "'+data[cont]+'" possição: (0,'+str(cont)+')'
        cont = len(data)
if erro == None:
    arvore = []
    arvore.append('Data')
    aux = ['Dia','/','Mes','/','Ano']
    arvore.append(aux)
    i = 0
    cont = 0
    while i<5:
        if aux[i] == 'Dia':
            aux2 = ['Digito','Digito']
            for j in range(2):
                if tokenL[cont] in digito:
                    aux3 = [tokenL[cont]]
                    aux2.append(aux3)
                    cont+=1
                else:
                    erro = 'Erro Sintatico, token: "'+tokenL[cont]+'" possição: (0,'+str(cont)+')'+'Esperavace um numero de 0 a 9'
                    i = 5
            arvore.append(aux2)
        elif aux[i] == 'Mes':
            aux2 = ['Digito','Digito']
            for j in range(2):
                if tokenL[cont] in digito:
                    aux3 = [tokenL[cont]]
                    aux2.append(aux3)
                    cont+=1
                else:
                    erro = 'Erro Sintatico, token: "'+tokenL[cont]+'" possição: (0,'+str(cont)+')'+'Esperavace um numero de 0 a 9'
                    i = 5
            arvore.append(aux2)
        elif aux[i] == 'Ano':
            aux2 = ['Digito','Digito','Digito','Digito']
            for j in range(4):
                if tokenL[cont] in digito:
                    aux3 = [tokenL[cont]]
                    aux2.append(aux3)
                    cont+=1
                else:
                    erro = 'Erro Sintatico, token: "'+tokenL[cont]+'" possição: (0,'+str(cont)+')'+'Esperavace um numero de 0 a 9'
                    i = 5
            arvore.append(aux2)
        else:
            if tokenL[cont] != '/':
                erro = 'Erro Sintatico, token: "'+tokenL[cont]+'" possição: (0,'+str(cont)+')'+'Esperavace o token "/"'
                i = 5
            cont+=1
        i+=1
    print(arvore)

if erro != None:
    tabela = []
    tabela.append(arvore)
    tabela.append(erro)
    with open("analizador.json", 'w', encoding="utf8") as f:
        json.dump(tabela, f, ensure_ascii=False)
else:
    with open("analizador.json", 'w', encoding="utf8") as f:
        json.dump(arvore, f, ensure_ascii=False)
