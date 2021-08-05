import pandas as pd
from datetime import datetime
def captura_coluna_e_retorna_lista(planilha:str,nome_da_coluna) -> list:
    '''
    planilha = Entrada caminho da planilha/planilha
    nome_da_coluna = coluna da extração 
    ############################################################
    # FUNÇÃO RESPONSÁVEL POR PEGAR UMA PLANILHA EXCEL E EXTRAIR#
    #OS DADOS DA COLUNA ESPECIFICADA FORMANDO UMA LISTA DE DA- #
    #DOS.                                                      #
    ############################################################
    except: Retorna uma lista vazia
    '''
    try:
        alunos = pd.read_excel(planilha)
        nm_alunos = list(alunos[nome_da_coluna].to_dict().values())
        return nm_alunos
    except:
        return []
 
def gera_retorno(lista_final:list, nome_planilha_final=False)->bool:
    '''
    ############################################################
    # FUNÇÃO RESPONSÁVEL POR PEGAR A LISTA RETORNADA DOS GRUPOS#
    # E GERAR UMA PLANILHA ONDE CADA SUB-LISTA É UMA LINHA DOS #
    # GRUPOS.                                                  #
    ############################################################

    except: retorna boolean False
    '''
    pr = pd.DataFrame()
    try:
        for grupo in lista_final:
            i2,i3 = "",""
            i1 = grupo[0] if grupo[0] else ""
            if len(grupo) > 1:
                i2 = grupo[1] if grupo[1] else ""
            if len(grupo) > 2:
                i3 = grupo[2] if grupo[2] else ""
            pr = pr.append(
                {
                    'integrante 1':i1,
                    'integrante 2':i2,
                    'integrante 3':i3
                },
            ignore_index=True)
        if not nome_planilha_final:
            nm_pl_fn = datetime.now().strftime("%d-%m-%Y") + ".xlsx"
            pr.to_excel(nm_pl_fn, index = False)
        else:
            pr.to_excel(nome_planilha_final, index = False)
        return True

    except Exception as err:
        return False