# instalar Pywhatkit em https://pypi.org/project/pywhatkit/

import pywhatkit as kt

print("+---------------------------------------+")
print("|     Envio de Mensagem automatizado    |")
print("+---------------------------------------+")
print("|       -Enviar a mensagem para:        |")
print("|         > G para Grupo                |")
print("|         > C para Contato              |")
grupoOucontato = str(input("| > Resposta: "))
gCCorreto = grupoOucontato.upper()

if gCCorreto == "G":

    print("+---------------------------------------+")
    print("|   Envio de Mensagem para um grupo     |")
    print("+---------------------------------------+")
    grupo = str(input('| > Id do grupo que deseja enviar a Mensagem: '))
    mensagemParaGrupo = str(input('| > Qual a mensagem: ').strip())
    hora = int(input('| > Qual a hora de envio sem os minutos: '))
    minuto = int(input('| > Qual(is) o(s) minuto(s) de envio: '))
    print("+---------------------------------------+")
    print('|            Será Enviado               |')
    print("+---------------------------------------+")
    kt.sendwhatmsg_to_group(grupo, mensagemParaGrupo, hora, minuto)

elif gCCorreto == "C":

    print("| > Enviar a mensagem agora ou em outro momento | ")
    print("+-----------------------------------------------+")
    opcao = str(input('| A para agora e D para depois: '))
    opcaoIndependenteDaForma = opcao.upper()
    
    if opcao == 'a':
        telefone = str(input('| > Qual numero deseja enviar a Mensagem (sem espaços e com +55 ex: +5511123434567 ): '))
        mensagem = str(input('| > Qual a mensagem: ').strip())
        print('Enviando...')
        kt.sendwhatmsg_instantly(telefone, mensagem)
    elif opcao == 'd':
        telefone = str(input('| > Qual numero deseja enviar a Mensagem: '))
        mensagem = str(input('| > Qual a mensagem: ').strip())
        hora = int(input('| > Qual a hora de envio sem os minutos: '))
        minuto = int(input('| > Qual(is) o(s) minuto(s) de envio: '))
        print("+---------------------------------------+")
        print('|                Enviando               |')
        print("+---------------------------------------+")
        kt.sendwhatmsg(telefone, mensagem, hora, minuto)

