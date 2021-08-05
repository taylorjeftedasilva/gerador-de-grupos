#!/usr/bin/python3
import random
from planilhas import captura_coluna_e_retorna_lista, gera_retorno

def gera_grupo(alunos:list)->bool:
    '''
    Recebe uma lista de objetos para gerar grupos de três
    '''
    tamanhoDaLista = len(alunos)
    count = 0
    grupos = []
    while(count < tamanhoDaLista):
        if len(alunos) >= 3:
            random.shuffle(alunos)
            grupos.append([alunos[0],alunos[1],alunos[2]])
            alunos.remove(alunos[0])
            alunos.remove(alunos[0])
            alunos.remove(alunos[0])
        else:
            if alunos:
                remanecentes = list()
                for i in alunos:
                    remanecentes.append(i)
                grupos.append(remanecentes)
            break
        count+=1
    
    return gera_retorno(grupos)


# Chama função para gerar os grupos
if __name__ == "__main__":
    import sys
    args = sys.argv
    try:
        if args:
            planilha = args[1]
            nome_coluna = args[2]
    except:
        planilha = input("Caminho + nome da planilha ex: home/planilha: ")
        nome_coluna = input("Nome da coluna: ")
    if planilha == "" or nome_coluna == "":
        print("É necessário uma planilha e nome de coluna para executar o programa")
    else:        
        gera_grupo(captura_coluna_e_retorna_lista(planilha, nome_coluna))
   