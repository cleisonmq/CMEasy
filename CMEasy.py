# CMEasy
# Versão 0.1v
# Create By Cleison Máquina

import subprocess
import shutil
import os
import re
import shutil

#--------------------> Codigos mais usados <-----------------
# Botao para quando o utilisador clicar em enter o programa limpre a tela 
def enter_clear ():
    input("Pressione [ ENTER ] para continuar")
    os.system("cls" if os.name == "nt" else "clear")
# Caso o utilizador nao digite nada
def entrada_invalida1 ():
    print("|---------------- Entrada inválida, você deve escolher uma opção! ---------------------------|")
    input ("Presione [ ENTER ] para continuar... ")
# Se a conversão falhar (não for um número), exibe uma mensagem de erro
def entrada_invalida2 ():
    print("|---------------- Opção inválida! Por favor, insira um número. ---------------------------|")
    enter_clear()
# Este case captura qualquer entrada que não seja uma opção válida
def entrada_invalida3 ():
    print("|---------------- Opção inválida, tente novamente ---------------------------|")
    enter_clear ()
# Comandos dos programas
def comandos_menu ():
    print("+-----------------------------------------------------------------------------+")
    print("|                              C O M A N D O S                                |")
    print("+-----------------------------------------------------------------------------+")
    print("| 1. | Iniciar o serviço.                                                     |")
    print("+----+------------------------------------------------------------------------+")
    print("| 2. | Ativar o Serviço.                                                      |")
    print("+----+------------------------------------------------------------------------+")
    print("| 3. | Estado do serviço.                                                     |")
    print("+----+------------------------------------------------------------------------+")
    print("| 4. | Parar o serviço.                                                       |")
    print("+----+------------------------------------------------------------------------+")
    print("| 5. | Reiniciar o serviço.                                                   |")
    print("+----+------------------------------------------------------------------------+")
    print("| 6. | Versão do serviço.                                                     |")
    print("+----+------------------------------------------------------------------------+")
    print("| 7. | Voltar.                                                                |")
    print("+-----------------------------------------------------------------------------+")
    print("|                                - CMEasy -                                   |")
    print("+-----------------------------------------------------------------------------+")
#------------------------------------------------------------

######################################################################################################################
######################################################################################################################
######################################################################################################################

#-------------------------> CMEasy <-------------------------
# Menu Principal
def menu_principal ():
    print("+--------------------------------------------------------+")
    print("|                      - CMEasy -                        |")
    print("+--------------------------------------------------------+")
    print("|                       M E N U                          |")
    print("+------+-------------------------------------------------+")
    print("|  1.  | Promagramas                                     |")
    print("+------+-------------------------------------------------+")
    print("|  2.  | Executar Comandos                               |")
    print("+------+-------------------------------------------------+")
    print("|  3.  | Scripts para vulnerabildades                    |")
    print("+------+-------------------------------------------------+")
    print("|  4.  | Informação                                      |")
    print("+------+-------------------------------------------------+")
    print("|  5.  | Encerrar o programa                             |")
    print("+--------------------------------------------------------+")
#------------------------------------------------------------

#####################################################################################################################################
#####################################################################################################################################
#####################################################################################################################################

#----------------> 1. Instalar Promagramas <-----------------
# Menu sistemas 
def menu_programas_sO ():
    print("+--------------------------------------------------------+")
    print("|               --> SISTEMA OPERACIONAL <--              |")
    print("+--------------------------------------------------------+")
    print("|  1.  | Linux                                           |")
    print("+------+-------------------------------------------------+")
    print("|  2.  | Windows                                         |")
    print("+------+-------------------------------------------------+")
    print("|  3.  | Voltar                                          |")
    print("+--------------------------------------------------------+")
    print("|                       @cmeasy                          |")
    print("+--------------------------------------------------------+")
# Menu Principal (Tipos de distribuicao)
def menu_instalar_programas ():
    print("+--------------------------------------------------------+")
    print("|                  --> PROGRAMAS <--                     |")
    print("+--------------------------------------------------------+")
    print("|                  DISTRIBUÇÃO LINUX                     |")
    print("+--------------------------------------------------------+")
    print("|  1.  | Familia Debian (Ubunto, Kali, Linux...)         |")
    print("+------+-------------------------------------------------+")
    print("|  2.  | Familia Red Hat (Rocky Linux, Cent OS...)       |")
    print("+------+-------------------------------------------------+")
    #print("|      | Familia Arch (Arch Linux, Manjaro...)           |")
    #print("+------+-------------------------------------------------+")
    print("|  3.  | Voltar                                          |")
    print("+--------------------------------------------------------+")
    print("|                       @cmeasy                          |")
    print("+--------------------------------------------------------+")
#--- Menu Programas (Tipos de programas)
def menu_tipo_de_programa ():
    print("+--------------------------------------------------------+")
    print("|                --> TIPO DE SOFTWARE <--                |")
    print("+--------------------------------------------------------+")
    print("|  1.  | Cibersegurança                                  |")
    print("+------+-------------------------------------------------+")
    print("|  2.  | Programação                                     |")
    print("+------+-------------------------------------------------+")
    print("|  3.  | Outros                                          |")
    print("+------+-------------------------------------------------+")
    print("|  4.  | Voltar                                          |")
    print("+--------------------------------------------------------+")
    print("|                       @cmeasy                          |")
    print("+--------------------------------------------------------+")

def menu_programas_windows ():
    print("+--------------------------------------------------------+")
    print("|                 P R O G R A M A S                      |")
    print("+--------------------------------------------------------+")
    print("|  1.  | Active Directory                                |")
    print("+------+-------------------------------------------------+")
    print("|  2.  | Voltar                                          |")
    print("+--------------------------------------------------------+")
    print("|                       @cmeasy                          |")
    print("+--------------------------------------------------------+")
#-------------------------------------------------

#------------------------> Outros programas
# Comandos
def outro_programas_comandos ():
    print("+----------------------------------------------------+")
    print("|                      COMANDOS                      |")
    print("+----------------------------------------------------+")
    print("| 1. Ativar                                          |")
    print("| 2. Iniciar                                         |")
    print("| 3. Estado                                          |")
    print("| 4. Parar                                           |")
    print("| 5. Reiniciar                                       |")
    print("| 6. Versao                                          |")
    print("| 7. Sair                                            |")
    print("+------- --------------------------------------------+")
    print("|                   - CMEasy -                       |")
    print("+----------------------------------------------------+") 
#---> 1. SSH
# Menu Principal
def menu_outros_programas ():
    print("+--------------------------------------------------------------+")
    print("|                      OUTROS PROGRAMAS                        |")
    print("+--------------------------------------------------------------+")
    print("|  1.  | SSH (Secure Shell)                                    |")
    print("+------+-------------------------------------------------------+")
    print("|  2.  | Apache                                                |")
    print("+------+-------------------------------------------------------+")
    print("|  3.  | John the Ripper                                       |")
    print("+------+-------------------------------------------------------+")
    #print("| 4. | Parar                                                   |")
    #print("+----+---------------------------------------------------------+")
    #print("| 5. | Reiniciar                                               |")
    #print("+----+---------------------------------------------------------+")
    #print("| 6. | Versão                                                  |")
    #print("+----+---------------------------------------------------------+")
    #print("| 7. | Ver IP'S Banidos                                        |")
    #print("+----+---------------------------------------------------------+")
    #print("| 8. | Liberar IP                                              |")
    #print("+----+---------------------------------------------------------+")
    #print("| 8. | Banir Host                                              |")
    #print("+----+---------------------------------------------------------+")
    print("|  4.  | Sair                                                  |")
    print("+--------------------------------------------------------------+")
    print("|                        - CMEasy -                            |")
    print("+--------------------------------------------------------------+")
#---> ssh
def menu_ssh ():
    print("+----------------------------------------------------+")
    print("|                      S S H                         |")
    print("+----------------------------------------------------+")
    print("| SSH (Secure Shell) é um protocolo de rede utilizado|")
    print("|para acessar de forma segura e remota computadores  |")
    print("|ou servidores, permitindo a execução de comandos e a|")
    print("|transferência de arquivos criptografados.           |")
    print("+----------------------------------------------------+")
    print("| Teste: Ubunto, Debian, Kali, Rocky linux           |")
    print("+----------------------------------------------------+")
    print("|      1. Instalar         |     2. Desinstalar      |")
    print("+--------------------------+-------------------------+") 
    print("|      3. Comandos         |        4. Sair          |")
    print("+----------------------------------------------------+")
    print("|                   - CMEasy -                       |")
    print("+----------------------------------------------------+")
# Instalar ssh
def instalacao_ssh ():
    try:
        print("|---------------------------- Instalando o ssh  ------------------------------|")
        subprocess.run(["sudo", "dnf","install", "-y", "openssh-server"], check=True)
        print("|---------------------- SSH instalado com sucesso --------------------------------|")
        
        print("|-------------------------- ativando o ssh ------------------------------|")
        subprocess.run(["systemctl", "enable", "sshd"], check=True)
        print("|---------------------- SSH ativado com sucesso --------------------------------|")
        
        print("|---------------------------- Iniviando o ssh --------------------------------|")
        subprocess.run(["sudo", "systemctl", "start", "sshd"], check=True)
        print("|----------------------- ssh iniciado com sucesso ----------------------------|")
        print("|---------------------------- ssh instalado com sucesso ------------------------------|")
    except subprocess.CalledProcessError as e:
        print(f"Ocorreu um erro ao executar o comando: {e}")
        #-------------------- limpar a tela                                     
    enter_clear()
# Desinstalar ssh
def desinstalacao_ssh ():
    try:
        print("|---------------------------- Desinstalando o ssh  ------------------------------|")
        subprocess.run(["sudo", "systemctl", "stop", "ssh"], check=True) 
        subprocess.run(["sudo", "dnf", "remove", "--purge", "-y", "openssh-server"], check=True)
        subprocess.run(["sudo", "dnf", "autoremove", "-y"], check=True)
        subprocess.run(["sudo", "rm", "-rf", "/etc/ssh"], check=True) 
        subprocess.run(["sudo", "rm", "-rf", "/home/*/.ssh"], check=True)
        print("|----------------------- ssh desinstalado com sucesso ----------------------------|")
    except subprocess.CalledProcessError as e:
        print(f"Ocorreu um erro ao executar o comando: {e}")
        #-------------------- limpar a tela                                     
    enter_clear()
def comandos_ssh ():
    while True:
        subprocess.run(["clear"])
        outro_programas_comandos ()
        escolha = input ("Escolha uma das opções acima: ")
        if escolha == "":
            entrada_invalida1 ()
            continue
        else:
            try:
                opcao = int(escolha)
                match opcao:
                    case 1:
                        subprocess.run(["sudo", "systemctl", "enable", "sshd"], check=True) 
                        print ("|---------------- ssh Ativado com sucesso -----------------------|")
                        enter_clear ()
                        continue
                    case 2:
                        subprocess.run(["sudo", "systemctl", "start", "sshd"], check=True) 
                        print ("|---------------- ssh iniciado com sucesso -----------------------|")
                        enter_clear ()
                        continue
                    case 3:
                        subprocess.run(["sudo", "systemctl", "status", "sshd"]) 
                        enter_clear ()
                        continue
                    case 4:
                        subprocess.run(["sudo", "systemctl", "stop", "sshd"], check=True) 
                        print ("|---------------- ssh parado com sucesso -----------------------|")
                        enter_clear ()
                        continue
                    case 5:
                        subprocess.run(["sudo", "systemctl", "restart", "sshd"], check=True) 
                        print ("|---------------- ssh reiniciado com sucesso -----------------------|")
                        enter_clear ()
                        continue
                    case 6:
                        subprocess.run(["sshd", "-V"], check=True) 
                        enter_clear ()
                        continue
                    case 7:
                        break
                    case _:
                        entrada_invalida3 ()
                        continue 
            except ValueError:
                entrada_invalida2 ()
                continue 
def ssh_debian():
    while True: 
        os.system("cls" if os.name == "nt" else "clear")
        menu_ssh ()
        escolha = input ("Escolha uma das opções acima: ")
        if escolha == "":
            entrada_invalida1 ()
            continue
        else:
            try:
                opcao = int (escolha)
                match opcao: 
                    # Instalar
                    case 1:
                        instalacao_ssh ()
                        continue
                    # Desinstalar
                    case 2:
                        desinstalacao_ssh ()
                        continue
                    # Comandos
                    case 3:
                        comandos_ssh()
                        continue
                    # Voltar
                    case 4:
                        break
                    case _:
                        entrada_invalida3 ()
                        continue 
            except ValueError:
                entrada_invalida2 ()
def ssh_redHat():
    while True: 
        os.system("cls" if os.name == "nt" else "clear")
        menu_ssh ()
        escolha = input ("Escolha uma das opções acima: ")
        if escolha == "":
            entrada_invalida1 ()
            continue
        else:
            try:
                opcao = int (escolha)
                match opcao: 
                    # Instalar
                    case 1:
                        instalacao_ssh ()
                        continue
                    # Desinstalar
                    case 2:
                        desinstalacao_ssh ()
                        continue
                    # Comandos
                    case 3:
                        comandos_ssh()
                        continue
                    # Voltar
                    case 4:
                        break
                    case _:
                        entrada_invalida3 ()
                        continue 
            except ValueError:
                entrada_invalida2 ()
#---> 2. Apache
def menu_apache ():
    print("+----------------------------------------------------+")
    print("|                      APACHE                        |")
    print("+----------------------------------------------------+")
    print("| O Apache é um servidor web popular que recebe      |")
    print("|pedidos de páginas da internet e entrega o conteúdo |")
    print("|aos navegadores.                                    |")
    print("+----------------------------------------------------+")
    print("|      1. Instalar         |     2. Desinstalar      |")
    print("+--------------------------+-------------------------+") 
    print("|      3. Comandos         |        4. Sair          |")
    print("+----------------------------------------------------+")
    print("|                   - CMEasy -                       |")
    print("+----------------------------------------------------+")
# Instalar ssh
def instalacao_apache ():
    try:
        subprocess.run(["sudo", "apt","update"], check=True)
        print("|---------------------------- Instalando o apache  ------------------------------|")
        subprocess.run(["sudo", "apt","install", "apache2", "-y"], check=True)
        print("|---------------------- apache instalado com sucesso --------------------------------|")
        
        print("|-------------------------- ativando o apache ------------------------------|")
        subprocess.run(["sudo", "systemctl", "enable", "apache2"], check=True)
        print("|---------------------- SSH ativado com sucesso --------------------------------|")
        
        print("|---------------------------- Iniviando o apache --------------------------------|")
        subprocess.run(["sudo", "systemctl" "start", "apache2"], check=True)
        print("|----------------------- apache iniciado com sucesso ----------------------------|")
        print("|---------------------------- apache instalado com sucesso ------------------------------|")
    except subprocess.CalledProcessError as e:
        print(f"Ocorreu um erro ao executar o comando: {e}")
        #-------------------- limpar a tela                                     
    enter_clear()
# Desinstalar ssh
def desinstalacao_apache ():
    try:
        print("|---------------------------- Desinstalando o ssh  ------------------------------|")
        subprocess.run(["sudo", "systemctl", "stop", "apache2"], check=True) 
        subprocess.run(["sudo", "systemctl", "disable", "apache2"], check=True) 
        subprocess.run(["sudo", "apt", "purge", "apache2", "-y"], check=True)
        subprocess.run(["sudo", "apt", "remove", "apache2" , "-y"], check=True)
        subprocess.run(["sudo", "apt", "autoremove", "-y"], check=True)
        subprocess.run(["sudo", "rm", "-rf", "/etc/apache"], check=True) 
        subprocess.run(["sudo", "rm", "-rf", "/home/*/.apache"], check=True)
        print("|----------------------- ssh desinstalado com sucesso ----------------------------|")
    except subprocess.CalledProcessError as e:
        print(f"Ocorreu um erro ao executar o comando: {e}")
        #-------------------- limpar a tela                                     
    enter_clear()
# Comandos
def comandos_apache ():
    while True:
        subprocess.run(["clear"])
        outro_programas_comandos ()
        escolha = input ("Escolha uma das opções acima: ")
        if escolha == "":
            entrada_invalida1 ()
            continue
        else:
            try:
                opcao = int(escolha)
                match opcao:
                    case 1:
                        subprocess.run(["sudo", "systemctl", "enable", "apache2"], check=True) 
                        print ("|---------------- apache2 Ativado com sucesso -----------------------|")
                        enter_clear ()
                        continue
                    case 2:
                        subprocess.run(["sudo", "systemctl", "start", "apache2"], check=True) 
                        print ("|---------------- apache2 iniciado com sucesso -----------------------|")
                        enter_clear ()
                        continue
                    case 3:
                        subprocess.run(["sudo", "systemctl", "status", "apache2"]) 
                        enter_clear ()
                        continue
                    case 4:
                        subprocess.run(["sudo", "systemctl", "stop", "apache2"], check=True) 
                        print ("|---------------- apache2 parado com sucesso -----------------------|")
                        enter_clear ()
                        continue
                    case 5:
                        subprocess.run(["sudo", "systemctl", "restart", "apache2"], check=True) 
                        print ("|---------------- apache2 reiniciado com sucesso -----------------------|")
                        enter_clear ()
                        continue
                    case 6:
                        subprocess.run(["apache2", "-v"], check=True) 
                        enter_clear ()
                        continue
                    case 7:
                        break
                    case _:
                        entrada_invalida3 ()
                        continue 
            except ValueError:
                entrada_invalida2 ()
                continue 
def apache():
    while True: 
        os.system("cls" if os.name == "nt" else "clear")
        menu_apache ()
        escolha = input ("Escolha uma das opções acima: ")
        if escolha == "":
            entrada_invalida1 ()
            continue
        else:
            try:
                opcao = int (escolha)
                match opcao: 
                    # Instalar
                    case 1:
                        instalacao_apache()
                        continue
                    # Desinstalar
                    case 2:
                        desinstalacao_apache ()
                        continue
                    # Comandos
                    case 3:
                        comandos_apache()
                        continue
                    # Voltar
                    case 4:
                        break
                    case _:
                        entrada_invalida3 ()
                        continue 
            except ValueError:
                entrada_invalida2 ()
#---> 3. John the Ripper
def menu_johnRipper ():
    print("+----------------------------------------------------+")
    print("|                  John the Ripper                   |")
    print("+----------------------------------------------------+")
    print("| John the Ripper é uma ferramenta de segurança usada|")
    print("|para testar e recuperar senhas, tentando            |")
    print("|descobri-las através de métodos como força bruta e  |")
    print("|listas de palavras.                                 |")
    print("+----------------------------------------------------+")
    print("| Sistemas: Linux, Windows, MacOS.                   |")
    print("+----------------------------------------------------+")
    print("| Testes: Kali Linux                                 |")
    print("+----------------------------------------------------+")
    print("|      1. Instalar         |     2. Desinstalar      |")
    print("+--------------------------+-------------------------+") 
    print("|      3. Comandos         |        4. Sair          |")
    print("+----------------------------------------------------+")
    print("|                   - CMEasy -                       |")
    print("+----------------------------------------------------+")
# Instalar johnRipper
def instalacao_johnRipper ():
    try:
        print("|---------------------- Atualizando repositórios ----------------------|")
        subprocess.run(["sudo", "apt", "update"], check=True)
        print("|-------------------- Instalando o johnRipper -------------------------|")
        subprocess.run(["sudo", "apt", "install", "-y", "john"], check=True)
        subprocess.run(["john", "--version"], check=True)
        print("|---------------- johnRipper instalado com sucesso --------------------|") 
    except subprocess.CalledProcessError as e:
        print(f"Ocorreu um erro ao executar o comando: {e}")
        #-------------------- limpar a tela   
    except KeyboardInterrupt:
        print("\nCMEasy encerrado! ")                                  
    enter_clear()
# Desinstalar
def desinstalar_johnRipper ():
    try:
        print("|---------------------- Desinstalando o johnRipper  ----------------------|")
        subprocess.run(["sudo", "apt", "remove", "john"], check=True)
        subprocess.run(["sudo", "apt", "purge", "john"], check=True)
        subprocess.run(["sudo", "apt", "autoremove"], check=True)
        subprocess.run(["john", "--version"], check=True)
        print("|---------------- johnRipper instalado com sucesso --------------------|") 
    except subprocess.CalledProcessError as e:
        print(f"Ocorreu um erro ao executar o comando: {e}")
        #-------------------- limpar a tela   
    except KeyboardInterrupt:
        print("\nCMEasy encerrado! ")                                  
    enter_clear()
# Comandos
def menu_comandos_johnRipper ():
    print("+------------------------------------------------------------------------------+")
    print("|                               C O M A N D O S                                |")
    print("+------------------------------------------------------------------------------+")
    print("| 1.  | Verificar a versão.                                                    |")
    print("+-----+------------------------------------------------------------------------+")
    print("| 2.  | Quebrar arquivos ZIP.                                                  |")
    print("+-----+------------------------------------------------------------------------+")
    print("| 3.  | Quebrar senhas do Linux.                                               |")
    print("+-----+------------------------------------------------------------------------+")
    print("| 10. | Voltar.                                                                |")
    print("+------------------------------------------------------------------------------+")
    print("|                                 - CMEasy -                                   |")
    print("+------------------------------------------------------------------------------+")
def version_johnRipper ():
    try:
        subprocess.run(["john", "--version"], check=True)
        print("|---------------- Comando executado com sucesso --------------------|") 
    except subprocess.CalledProcessError as e:
        print(f"Ocorreu um erro ao executar o comando: {e}")  
    except KeyboardInterrupt:
        print("\nCMEasy encerrado! ")
    enter_clear () 
def quebrarzip_johnR ():
    try:
        arquizip = input("Indique o caminho ou nome do arquivo zipado: ")

        print("|---------------- Executando zip2john --------------------|")

        with open("zip.hashes", "w") as f:
            subprocess.run(["zip2john", arquizip], stdout=f, check=True)

        print("|---------------- Executando john ------------------------|")
        subprocess.run(["john", "zip.hashes"], check=True)

        print("|---------------- Comando executado com sucesso ---------|")

    except subprocess.CalledProcessError as e:
        print(f"[ERRO] Ocorreu um erro ao executar o comando: {e}")

    enter_clear () 
def quebraruser_johnR ():
    try:
        # Verificar permissões
        if os.geteuid() != 0:
            print("[ERRO] Este script precisa ser executado como root (sudo).")
            exit()

        print("|---------------- Extraindo hashes (unshadow) ---------|")

        # Executa unshadow e captura output
        result = subprocess.run(
            ["unshadow", "/etc/passwd", "/etc/shadow"],
            capture_output=True,
            text=True,
            check=True
        )

        linhas = result.stdout.splitlines()

        # Pega apenas os últimos 5 users
        ultimos_5 = linhas[-5:]

        # Salva no ficheiro
        with open("users.txt", "w") as f:
            f.write("\n".join(ultimos_5) + "\n")

        print("|---------------- Executando john ---------------------|")
        print("|---------------- Este Processo pode demorar ---------------------|")

        wordlist = "/usr/share/wordlists/rockyou.txt"

        if not os.path.exists(wordlist):
            print(f"[ERRO] Wordlist não encontrada: {wordlist}")
            exit()

        subprocess.run([
            "john",
            "--format=crypt",
            f"--wordlist={wordlist}",
            "users.txt"
        ], check=True)

        print("|---------------- Processo concluído ------------------|")

    except subprocess.CalledProcessError as e:
        print(f"[ERRO] Falha ao executar comando: {e}")

    except KeyboardInterrupt:
        print("\n[INFO] CMEasy encerrado pelo usuário.")
# Programa comandos jhon
def comandos_johnRipper ():
    while True: 
        os.system("cls" if os.name == "nt" else "clear")
        menu_comandos_johnRipper ()
        escolha = input ("Escolha uma das opções acima: ")
        if escolha == "":
            entrada_invalida1 ()
            continue
        else:
            try:
                opcao = int (escolha)
                match opcao: 
                    case 1:
                        version_johnRipper ()
                        continue
                    case 2:
                        quebrarzip_johnR ()
                        continue
                    case 3:
                        quebraruser_johnR ()
                        continue
                    case 10:
                        break
                    case _:
                        entrada_invalida3 ()
                        continue 
            except ValueError:
                entrada_invalida2 ()
# Programa
def johnRipper ():    
    while True: 
        os.system("cls" if os.name == "nt" else "clear")
        menu_johnRipper ()
        escolha = input ("Escolha uma das opções acima: ")
        if escolha == "":
            entrada_invalida1 ()
            continue
        else:
            try:
                opcao = int (escolha)
                match opcao: 
                    case 1:
                        instalacao_johnRipper ()
                        continue
                    case 2:
                        desinstalar_johnRipper ()
                        continue
                    case 3:
                        comandos_johnRipper ()
                        continue
                    case 4:
                        break
                    case _:
                        entrada_invalida3 ()
                        continue 
            except ValueError:
                entrada_invalida2 ()
#-----------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------
def ourtros_programas_debian ():
    while True: 
        os.system("cls" if os.name == "nt" else "clear")
        menu_outros_programas ()
        escolha = input ("Escolha uma das opções acima: ")
        if escolha == "":
            entrada_invalida1 ()
            continue
        else:
            try:
                opcao = int (escolha)
                match opcao: 
                    #-------- Programa SSH
                    case 1:
                        ssh_debian ()
                        continue
                    case 2:
                        apache ()
                        continue
                    case 3:
                        johnRipper ()
                        continue
                    case 4:
                        break
                    case _:
                        entrada_invalida3 ()
                        continue 
            except ValueError:
                entrada_invalida2 ()
def ourtros_programas_redHat ():
    while True: 
        os.system("cls" if os.name == "nt" else "clear")
        menu_outros_programas ()
        escolha = input ("Escolha uma das opções acima: ")
        if escolha == "":
            entrada_invalida1 ()
            continue
        else:
            try:
                opcao = int (escolha)
                match opcao: 
                    #-------- Programa SSH
                    case 1:
                        ssh_redHat ()
                        continue
                    case 2:
                        print ("Indisponivel no momento...")
                        enter_clear ()
                        continue
                    case 3:
                        print ("Indisponivel no momento...")
                        enter_clear ()
                        continue
                    case 4:
                        break
                    case _:
                        entrada_invalida3 ()
                        continue 
            except ValueError:
                entrada_invalida2 ()                                                                                   
######################################################################################################################

#------------------------> Ciberseguranca
#--- Menu programas Ciberseguranca
def menu_so_ciberseguranca ():
    print("+--------------------------------------------------------+")
    print("|               --> SO CIBERSEGURANCA <--                |")
    print("+--------------------------------------------------------+")
    print("|  1.  | Fail2Ban                                        |")
    print("+------+-------------------------------------------------+")
    print("|  2.  | Snort                                           |")
    print("+------+-------------------------------------------------+")
    print("|  3.  | Proxy Squid                                     |")
    print("+------+-------------------------------------------------+")
    print("|  4.  | Bwapp                                           |")
    print("+------+-------------------------------------------------+")
    print("|  5.  | Suricata                                        |")
    print("+------+-------------------------------------------------+")
    print("|  6.  | WireGuard Vpn                                   |")
    print("+------+-------------------------------------------------+")
    print("|  7.  | OpenVpn                                         |")
    print("+------+-------------------------------------------------+")
    print("|  8.  | Voltar                                          |")
    print("+--------------------------------------------------------+")
    print("|                       @cmeasy                          |")
    print("+--------------------------------------------------------+") 
#---> Fail2Ban <---
# Menu principal
def fail2ban_menu_principal ():
    print("+-----------------------------------------------------------------------------+")
    print("|                                FAIL2BAN                                     |")
    print("+-----------------------------------------------------------------------------+")
    print("| Oque é ? | O Fail2Ban é uma ferramenta que protege servidores contraataques.|")
    print("+----------+------------------------------------------------------------------+")
    print("|          | - Proteger SSH                                                   |")
    print("|          | - Proteger sites (Apache/Nginx)                                  |")
    print("| Funções  | - Proteger serviços de email                                     |")
    print("|          | - Bloquear IPs automaticamente                                   |")
    print("|          | - Monitorar atividades suspeitas                                 |")
    print("|----------+------------------------------------------------------------------+")
    print("|  Testes  | Ubunto (22.04), Debian (13).                                     |")
    print("|-----------------------------------------------------------------------------+")
    print("|       1. Instalar      |      2. Desinstalar       |      3. Comandos       |")
    print("+------------------------+---------------------------+------------------------+")
    print("|    4. Configuracoes    |         5. Logs           |        6. Sair         |")
    print("+-----------------------------------------------------------------------------+")
    print("|                                  @cmeasy                                    |")
    print("+-----------------------------------------------------------------------------+")
#---> 1. Comandos
# Menu Principal
def fail2ban_menu_comandos ():
    print("+-----------------------------------------------------------------------------+")
    print("|                                FAIL2BAN                                     |")
    print("+-----------------------------------------------------------------------------+")
    print("|                            C O M A N D O S                                  |")
    print("+-----------------------------------------------------------------------------+")
    print("| 1. | Ativar                                                                 |")
    print("+----+------------------------------------------------------------------------+")
    print("| 2. | Iniciar                                                                |")
    print("+----+------------------------------------------------------------------------+")
    print("| 3. | Estado                                                                 |")
    print("+----+------------------------------------------------------------------------+")
    print("| 4. | Parar                                                                  |")
    print("+----+------------------------------------------------------------------------+")
    print("| 5. | Reiniciar                                                              |")
    print("+----+------------------------------------------------------------------------+")
    print("| 6. | Versão                                                                 |")
    print("+----+------------------------------------------------------------------------+")
    print("| 7. | Ver IP'S Banidos                                                       |")
    print("+----+------------------------------------------------------------------------+")
    print("| 8. | Liberar IP                                                             |")
    print("+----+------------------------------------------------------------------------+")
    print("| 8. | Banir Host                                                             |")
    print("+----+------------------------------------------------------------------------+")
    print("| 10.| Sair                                                                   |")
    print("+-----------------------------------------------------------------------------+")
    print("|                                - CMEasy -                                   |")
    print("+-----------------------------------------------------------------------------+")
# Comandos
def enable_fail2ban ():
    # Ativação do serviço
    print("|-----------------------> Ativando o servico Fail2ban <------------------------------|")
    subprocess.run(["sudo", "systemctl", "enable", "fail2ban.service"], check=True)
    print("|-----------------------> Fail2ban ativado com sucesso <------------------------------|")
    enter_clear ()
def start_fail2ban ():
    # Iniciação do serviço
    print("|-----------------------> Iniciando o servico Fail2ban <------------------------------|")
    subprocess.run(["sudo", "systemctl", "start", "fail2ban.service"], check=True)
    print("|-----------------------> Fail2ban iniciado com sucesso <-----------------------------|")
    enter_clear ()
def status_fail2ban ():
    # Estado do servico
    subprocess.run(["sudo", "systemctl", "status", "fail2ban.service"])
    enter_clear ()
def stop_fail2ban ():
    # Ativação do serviço
    print("|-----------------------> Parando o servico Fail2ban <------------------------------|")
    subprocess.run(["sudo", "systemctl", "stop", "fail2ban.service"], check=True)
    print("|-----------------------> Fail2ban foi parado com sucesso <------------------------------|")
    enter_clear()
def restart_fail2ban ():
    # Reativacao do serviço
    print("|-----------------------> Reiniciando o servico Fail2ban <------------------------------|")
    subprocess.run(["sudo", "systemctl", "restart", "fail2ban.service"], check=True)
    print("|-----------------------> Fail2ban reiniciado com sucesso <----------------------------|")
def version_fail2ban ():
    # versao do serviço
    subprocess.run(["sudo", "fail2ban-client", "--version"], check=True)
    enter_clear ()
def fail2ban_banir_ip ():
    ip = input ("indique o ip que deseja banir: ")
    subprocess.run(["sudo", "fail2ban-client," "set", "sshd", "banip", ip], check=True)
    print (f"O Host {ip} Foi banido")
def ver_ip_banido ():
    print("|----------------------- IP'S Banidos ------------------------------|")
    subprocess.run(["sudo", "iptables", "-L", "-n", "--line"], check=True)
    enter_clear ()
def liberar_ip ():
    ip = input ("indique o ip que deseja liberar: ")
    id = input ("indique o id que deseja liberar: ")
    subprocess.run(["sudo", "iptables", "-D", "f2b-sshd", id], check=True)
    subprocess.run(["sudo", "fail2ban-client", "set", "sshd", "unbanip", ip], check=True)
    print('|--------------------------- Host liberado -------------------------|')
    enter_clear ()
def fail2ban_banir_ip ():
    ip = input ("indique o ip que deseja banir: ")
    subprocess.run(["sudo", "fail2ban-client," "set", "sshd", "banip", ip], check=True)
    print (f"O Host {ip} Foi banido")
#---> 2. Instalar
def fail2ban_instalacao():
    try:
        # Verificando se o fail2ban já está instalado
        print("|---------------------------- Verificando se o Fail2Ban já está instalado ---------------------------|")
        result = subprocess.run(["dpkg", "-l", "fail2ban"], capture_output=True, text=True)
        
        if "fail2ban" in result.stdout:
            print("|---------------------------- Fail2Ban já está instalado ----------------------------|")
        else:
            #--------------------- Atualizar pacotes
            print("|---------------------------- Atualizando os pacotes  ------------------------------|")
            subprocess.run(["sudo", "apt", "update"], check=True)
            subprocess.run(["sudo", "dpkg", "--configure", "-a"], check=True)
            subprocess.run(["sudo", "apt", "install", "-f"], check=True)
            print("|------------------------ Pacotes atualizados com sucesso --------------------------|")
            
            #--------------------- Instalando o iptables
            print("|-------------------------- Instalando Pre-requisitos ------------------------------|")
            subprocess.run(["sudo", "apt", "install", "-y", "iptables"], check=True)
            print("|--------------------- Pre-requisitos instalados com sucesso -----------------------|")
            
            #-------------------- Instalar fail2ban
            print("|---------------------------- Instalando o Fail2Ban --------------------------------|")
            subprocess.run(["sudo", "apt", "install", "-y", "fail2ban"], check=True)
            print("|----------------------- Fail2ban instalado com sucesso ----------------------------|")
            
            #-------------------- Copia do arquivo de configuracao 
            print("|----------------------- Preparando o arquivo de configuracao ----------------------|")
            subprocess.run(["sudo", "cp", "/etc/fail2ban/jail.conf", "/etc/fail2ban/jail.local"], check=True)
            print("|--------------------- Arquivo de configuracao preparado ---------------------------|")

    except subprocess.CalledProcessError as e:
        print(f"Ocorreu um erro ao executar o comando: {e}")
        #-------------------- limpar a tela                                     
    enter_clear () 
#---> 3. Desinstalar
def fail2ban_remove ():
    try:
        # Verifica se o fail2ban-client existe no sistema
        if shutil.which("fail2ban-client") is None:
            print("+-------------------------------------------------------------------------------+")
            print("|-------------------O fail2ban nao existe nesta maquina-------------------------|")
            print("+-------------------------------------------------------------------------------+")
            return  # Se o Fail2Ban não existir, não faz sentido continuar com a remoção
        else:
            try:
                print("|-----------------------> Parando o servico Fail2ban <------------------------------|")
                subprocess.run(["sudo", "systemctl", "stop", "fail2ban.service"], check=True)
                print("|-----------------------> Fail2ban foi parado com sucesso <------------------------------|")
                subprocess.run(["sudo", "dpkg", "--configure", "-a"], check=True)
                subprocess.run(["sudo", "apt", "remove", "--purge", "fail2ban", "-y"], check=True)
                subprocess.run(["sudo", "apt", "autoremove", "-y"], check=True)
                subprocess.run(["sudo", "rm", "-rf", "/etc/fail2ban"], check=True)
                subprocess.run(["sudo", "rm", "-rf", "/var/log/fail2ban*"], check=True)
                subprocess.run(["sudo", "rm", "-rf", "/var/lib/fail2ban"], check=True)
                subprocess.run(["sudo", "rm", "-rf", "/run/fail2ban"], check=True)
                subprocess.run(["sudo", "systemctl", "daemon-reload"], check=True)
                subprocess.run(["sudo", "apt", "install", "-f"], check=True)
                
           
                saida = subprocess.run(["fail2ban-client", "-V"], capture_output=True, text=True)
                
                # Se o comando for bem-sucedido (returncode == 0)
                if saida.returncode == 0:
                    print("+-------------------------------------------------------------------------------+")
                    print("|----------------------------Desinstalacao bem sucedida------------------------|")
                    print("+-------------------------------------------------------------------------------+")
                else:
                    # Se o código de retorno for diferente de 0, indica erro na execução
                    print(f"Ainda existem traços do programa. ERRO: {saida.stderr}")
                    
            except FileNotFoundError:
                # Caso o comando fail2ban-client não exista no sistema
                print("+-------------------------------------------------------------------------------+")
                print("|----------------------------Desinstalacao bem sucedida------------------------|")
                print("+-------------------------------------------------------------------------------+")            
    except FileNotFoundError:
        # Caso o comando fail2ban-client não exista no sistema
        print("+-------------------------------------------------------------------------------+")
        print("|-------------------O fail2ban nao existe nesta maquina-------------------------|")
        print("+-------------------------------------------------------------------------------+")
    enter_clear ()
#---> 4. Ver Logs
def fail2ban_logs ():
    print ("|------------ Viusalizaras as ultimas 20 linhas de log em tempo real ----------------|")
    subprocess.run(["sudo", "tail", "-f", "n20", "/var/log/fail2ban.log"], check=True)
#---> 5. Configuracoes
def fail2ban_menu_conf ():
    print("+----------------------------------------------------------------------------------+")
    print("|                                FAIL2BAN - Conf                                   |")
    print("+----------------------------------------------------------------------------------+")
    print("| 1. | Configuração do Fail2Ban para Proteção contra Ataques de Força Bruta no SSH.|")
    print("+----+-----------------------------------------------------------------------------+")
    print("| 2. | Entrar no arquivo de configuracao.                                          |")
    print("+----+-----------------------------------------------------------------------------+")
    print("| 3. | Verificar erro.                                                             |")
    print("+----+-----------------------------------------------------------------------------+")
    print("| 4. | Sair.                                                                       |")
    print("+----------------------------------------------------------------------------------+")
    print("|                                    - CMEasy -                                    |")
    print("+----------------------------------------------------------------------------------+")
#------- Tutorial de configuracoes
# Tutorial configuracao ssh
def fail2ban_conf_ssh ():
    print("+----------------------------------------------------------------------------------+")
    print("|                             CMEasy - FAIL2BAN - Conf                             |")
    print("+----------------------------------------------------------------------------------+")
    print("| 1. | Configuração do Fail2Ban para Proteção contra Ataques de Força Bruta no SSH.|")
    print("+----------------------------------------------------------------------------------+")
    print("[sshd]         ")
    print("enabled = true     ")
    print("port = ssh      ")
    print("filter = sshd     ")
    print("logpath = /var/log/auth.log  ")
    print("bantime = 900   ")
    print("banaction = iptables-allports")
    print("findtime = 900    ")
    print("maxretry = 3    ")
    print("|----------------------------------------------------------------------------------|")
    print("| Copie e cole o codigo no arquivo de configuracao.                                |")
    print("| ATENCAO: Só pode existir UMA seção [sshd] neste arquivo.                         |")
    print(r'| Verificar duplicação com: grep -n "\[sshd\]" /etc/fail2ban/jail.local           |')
    print("+----------------------------------------------------------------------------------+")
    print("|                            Clique <ENTER> para sair                              |")
    print("+----------------------------------------------------------------------------------+")
    enter_clear ()
#-------------------------------------------------
def fail2ban_arquivo_conf ():
    try:
    #--------------------- Editar o arquivo de configuracao
        subprocess.run(["sudo", "nano", "/etc/fail2ban/jail.local"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Ocorreu um erro ao executar o comando: {e}")
        enter_clear ()
# Verificar erros no arquivo de configuracao 
def fail2ban_erro_arquivo_conf ():
    print ("|------------------ Erros ----------------------------------|")
    subprocess.run(["sudo", "fail2ban-server", "-t"], check=True)
    enter_clear ()
# Programa Fail2Ban
def fail2ban ():
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        fail2ban_menu_principal ()
        escolha = input ("Escolha uma das opções acima: ")
        if escolha == "":
            entrada_invalida1 ()
            continue
        else:
            try:
                opcao = int (escolha)
                match opcao:
                    # Instalar o Fail2Ban  
                    case 1:
                        fail2ban_instalacao()
                        continue
                    # Desinstalar Fail2Ban
                    case 2:
                        fail2ban_remove ()
                        continue
                    # Comandos Fail2Ban
                    case 3:
                        while True:
                            os.system("cls" if os.name == "nt" else "clear")
                            fail2ban_menu_comandos ()
                            escolha = input ("Escolha uma das opções acima: ")
                            if escolha == "":
                                entrada_invalida1 ()
                                continue
                            else:
                                try:
                                    opcao = int (escolha)
                                    match opcao:
                                        # Ativar  
                                        case 1:
                                            enable_fail2ban ()
                                            continue
                                        # Iniciar
                                        case 2:
                                            start_fail2ban ()
                                            continue
                                        # Estado
                                        case 3:
                                            status_fail2ban ()                                                                                                                            
                                            continue                                                                                                                       
                                        # Parar
                                        case 4:
                                            stop_fail2ban ()
                                            continue   
                                        # Reiniciar                                                                                                                        
                                        case 5:
                                            restart_fail2ban ()
                                            continue
                                        # Versao
                                        case 6:
                                            version_fail2ban ()
                                            continue
                                        # Ver IP'S Banidos
                                        case 7:
                                            ver_ip_banido()
                                            continue
                                        # Liberar IP  
                                        case 8:
                                            liberar_ip ()
                                            compile
                                        # Banir Host
                                        case 9:
                                            fail2ban_banir_ip ()
                                            continue
                                        # Voltar ao menu anterior
                                        case 10:
                                            break
                                        case _:
                                            entrada_invalida3 ()
                                            continue
                                except ValueError:
                                    entrada_invalida2 ()
                                    continue
                    # Configuracoes Fail2Ban
                    case 4:
                        while True:
                            subprocess.run(["clear"])
                            fail2ban_menu_conf ()
                            escolha = input ("Escolha uma das opções acima: ")
                            if escolha == "":
                                entrada_invalida1 ()
                                continue
                            else:
                                try:
                                    opcao = int (escolha)
                                    match opcao:
                                        # turorial conf ssh  
                                        case 1:
                                            subprocess.run(["clear"])
                                            fail2ban_conf_ssh ()
                                            continue
                                        # Arquivo de configuracao
                                        case 2:
                                            fail2ban_arquivo_conf ()
                                            continue
                                        # Verificar erros
                                        case 3:
                                            fail2ban_erro_arquivo_conf ()
                                            continue
                                        #voltar 
                                        case 4:
                                            break
                                        case _:
                                            entrada_invalida3 ()
                                            continue
                                except ValueError:
                                    entrada_invalida2 ()
                                    continue
                    # Ver Logs Fail2Ban
                    case 5:
                        fail2ban_logs ()
                        continue
                    # Voltar ao menu anterior
                    case 6:
                        break
                    case _:
                        entrada_invalida3 ()
                        continue
            except ValueError:
                entrada_invalida2 ()
                continue
#-----------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------
#---> Snort <---
# Menu Principal
def snort_menu_principal ():
    print("+-----------------------------------------------------------------------------+")
    print("|                                   SNORT                                     |")
    print("+-----------------------------------------------------------------------------+")
    print("| Oque é ? | O Snort é um sistema de segurança de rede que detecta e bloqueia |")
    print("|          |ataques em tempo real.                                            |")
    print("+----------+------------------------------------------------------------------+")
    print("|          | - Detecção e prevenção de intrusões (IDS/IPS)                    |")
    print("|          | - Análise de Comportamento e Anomalias                           |")
    print("| Funções  | - Registro e Armazenamento de Logs                               |")
    print("|          | - Inspeção Profunda de Pacotes (DPI - Deep Packet Inspection)    |")
    print("|          | - Detecção de Explorações de Vulnerabilidades (Exploits)         |")
    print("+----------+------------------------------------------------------------------+")
    print("| Requisi- | RAM: 4GB (Minimo)                                                |")
    print("|tos       | CPU: Arquitetura Moderna                                         |")
    print("|-----------------------------------------------------------------------------|")
    print("| Site ofi-| Link: https://www.snort.org/downloads#snort3-downloads           |")
    print("|cial      | Link: www.snort.org                                              |")
    print("|-----------------------------------------------------------------------------|")
    print("|  Testes  | Ubunto (v22).                                                    |")
    print("|-----------------------------------------------------------------------------+")
    print("|       1. Instalar      |      2. Desinstalar       |      3. Comandos       |")
    print("+------------------------+---------------------------+------------------------+")
    print("|    4. Configurações    |          5. Logs          |        6. Sair         |")
    print("+-----------------------------------------------------------------------------+")
    print("|                                  @cmeasy                                    |")
    print("+-----------------------------------------------------------------------------+")
def snort_menu_conf_geral ():
    print("+-------------------------------------------------------------------------------------------------------------+")
    print("|                                            CONFIGURAÇÃO GERAL                                               |")
    print("+-------------------------------------------------------------------------------------------------------------+")
    print("| Ao abrir o arquivo modifique de acordo a orientação a baixo, cuidado com comandos repetidos.                |")  
    print("+-------------------------------------------------------------------------------------------------------------+")
    print("|   1.   | ipvar HOME_NET 192.168.1.0/24 ### sua rede interna ###                                             |")
    print("+--------+----------------------------------------------------------------------------------------------------+")
    print('|   2.   | ipvar EXTERNAL_NET any                                                                             |')  
    print("+--------+----------------------------------------------------------------------------------------------------+")
    print('|   3.   | var RULE_PATH /etc/snort/rules ou var RULE_PATH rules                                              |')
    print("+--------+----------------------------------------------------------------------------------------------------+")
    print('|   4.   | Commente de --preprocessor reputation-- até --blacklist $BLACK_LIST_PATH/black_list.rules--        |') 
    print("+--------+----------------------------------------------------------------------------------------------------+")
    print('|   5.   | OBS: Commente de --preprocessor reputation-- até --blacklist $BLACK_LIST_PATH/black_list.rules--   |') 
    print("+--------+----------------------------------------------------------------------------------------------------+")
    print('|   6.   | include $RULE_PATH/local.rules                                                                     |') 
    print("+--------+----------------------------------------------------------------------------------------------------+")
    print('|   7.   | include $RULE_PATH/snort3-community-rules                                                          |') 
    print("+--------+----------------------------------------------------------------------------------------------------+")
    print('|   8.   | OBS: Comente todos os includes restantes                                                           |')   
    print("+-------------------------------------------------------------------------------------------------------------+")
    print('|                                      Clique em [ ENTER ] para continuar                                     |') 
    print("+-------------------------------------------------------------------------------------------------------------+")
    print("|                                                 - CMEasy -                                                  |")
    print("+-------------------------------------------------------------------------------------------------------------+")
def snort_menu_conf_service ():
    print("+-------------------------------------------------------------------------------------------------------------+")
    print("|                                          CONFIGURAÇÃO DO SERVIÇO                                            |")
    print("+-------------------------------------------------------------------------------------------------------------+")
    print("| Ao abrir o arquivo modifique de acordo a orientação a baixo, cuidado com comandos repetidos.                |")  
    print("+-------------------------------------------------------------------------------------------------------------+")
    print("[Unit]")
    print("Description=Snort IDS Daemon")
    print("After=network.target")
    print("[Service]")
    print("ExecStart=/usr/local/bin/snort -c /etc/snort/snort.conf -i eth0")
    print("Restart=on-failure")
    print("[Install]")
    print("WantedBy=multi-user.target")   
    print("+-------------------------------------------------------------------------------------------------------------+")
    print('|                                      Clique em [ ENTER ] para continuar                                     |') 
    print("+-------------------------------------------------------------------------------------------------------------+")
    print("|                                                 - CMEasy -                                                  |")
    print("+-------------------------------------------------------------------------------------------------------------+")
#---> 1. Instalar
def snort_menu_instalacao ():
    print("+-----------------------------------------------------------------------------+")
    print("|                             INSTALACAO - SNORT                              |")
    print("+-----------------------------------------------------------------------------+")
    print("| Recomendacao: Inicie o CMEasy na diretoria de download para esta operacao.  |")
    print("+-----------------------------------------------------------------------------+")
    print("| 1. | Instalar Snort 3.                                                      |")
    print("+----+------------------------------------------------------------------------+")
    print("| 2. | Instalar Snort 2.                                                      |")
    print("+----+------------------------------------------------------------------------+")
    print("| 3. | Instalar a partir dos repositórios da distro (Ubunto/Debian).          |")
    print("+----+------------------------------------------------------------------------+")
    print("| 4. | Voltar.                                                                |")
    print("+-----------------------------------------------------------------------------+")
    print("|                                  @cmeasy                                    |")
    print("+-----------------------------------------------------------------------------+")
def snort_instalacao1():
    result = subprocess.run(["dpkg", "-l", "snort"], capture_output=True, text=True)        
    if "snort" in result.stdout:
        print("|---------------------------- snort já está instalado ----------------------------|")
    else:
        try:
            snort_link = input ("Cole o link de download do site oficial: ")
            # Atualizar os pacotes do so
            print ("|---------------------Atualizando pacotes------------------------|")
            subprocess.run(["sudo", "apt", "update"], check=True)
            subprocess.run(["sudo", "apt", "install", "wget"], check=True)
            print ("|--------------Pacotes actualizados com sucesso------------------|")
            # instalacao das dependencias
            print("|---------------------------- Instalando as dependencias necessarias ---------------------------|")
            subprocess.run(["sudo", "apt", "install", "-y", "build-essential", "libpcap-dev", "libpcre3-dev", "libdumbnet-dev", "bison", "flex", "zlib1g-dev"], capture_output=True, text=True)
            print("|---------------------------- Dependencias instaladas com sucesso ---------------------------|")
            # Download
            print("|---------------------------- Baixando o snort ---------------------------|")
            subprocess.run(["sudo", "wget", snort_link], check=True)
            print("|---------------------------- Download concluido ---------------------------|")
            # Extracao do arquivo
            snort_arquivo1 = input(r"Indique o nome do arquivo baixado -> 'nome.tar.gz' <-: ")
            print("|---------------------------- Extraindo o arquivo ---------------------------|")
            subprocess.run(["sudo", "tar", "-xvzf", snort_arquivo1], check=True)
            print("|---------------------------- Arquivo extraido ---------------------------|")
            snort_arquivo2 = input("Indique o nome do arquivo ja extraido: ")
            subprocess.run(["cd", snort_arquivo2], check=True)
            print("|---------------------------- Configurando a compilacao ---------------------------|")        
            subprocess.run(["sudo", "./configure"], check=True)
            print("|---------------------------- Compilacao Configurada ---------------------------|")
            print("|---------------------------- Compilando programa ---------------------------|")
            subprocess.run(["make"], check=True)
            print("|---------------------------- Programa Compilado ---------------------------|")
            print("|---------------------------- Instalando o programa no sistema ---------------------------|")
            subprocess.run(["sudo", "make", "install"], check=True)
            print("|---------------------------- Snort Instalado com sucesso ---------------------------|")
            print("|---------------------------- Criando os arquivos de configuracao ---------------------------|")
            subprocess.run(["sudo", "mkdir", "/etc/snort"], check=True)
            subprocess.run(["sudo", "mkdir", "/etc/snort/rules"], check=True)
            subprocess.run(["sudo", "mkdir", "/var/log/snort"], check=True)
            print("|---------------------------- Criando copias dos arquivos de configuracao ---------------------------|")
            subprocess.run(["sudo", "cp", "etc/*.conf*", "/etc/snort/"], check=True)
            subprocess.run(["sudo", "cp", "etc/*.map", "/etc/snort/"], check=True)
            print("|---------------------------- Snort pronto para ser utilizado ---------------------------|")
            subprocess.run(["snort", "-v"])
            enter_clear ()
        except subprocess.CalledProcessError as e:
            print(f"Ocorreu um erro ao executar o comando: {e}")
        #-------------------- limpar a tela                                     
    enter_clear () 
def snort_instalacao2():
    result = subprocess.run(["dpkg", "-l", "snort"], capture_output=True, text=True)        
    if "snort" in result.stdout:
        print("|---------------------------- snort já está instalado ----------------------------|")
    else:
        try:
            # Atualizando pacotes do SO
            print("|--------------------- Atualizando pacotes ------------------------|")
            subprocess.run(["sudo", "apt", "update"], check=True)
            subprocess.run(["sudo", "apt", "install", "wget", "-y"], check=True)
            print("|-------------- Pacotes atualizados com sucesso ------------------|")

            # Instalando dependências
            print("|---------------------------- Instalando as dependências necessárias ---------------------------|")
            subprocess.run(["sudo", "apt", "install", "-y", "libluajit-5.1-2", "libluajit-5.1-dev", "build-essential", "libpcap-dev", "libpcre3-dev", "libdumbnet-dev", "bison", "flex", "zlib1g-dev", "liblzma-dev", "openssl", "libssl-dev", "pkg-config", "libhwloc-dev", "cmake"], check=True)
            print("|---------------------------- Dependências instaladas com sucesso ---------------------------|")

            # Download do DAQ (Data Acquisition library)
            print("|---------------------------- Download do DAQ ---------------------------|")
            subprocess.run(["cd", "/tmp/"])
            subprocess.run(["sudo", "wget", "https://www.snort.org/downloads/snort/daq-2.0.7.tar.gz"], check=True)
            print("|---------------------------- Download concluído ---------------------------|")

            # Extração do arquivo DAQ
            print("|---------------------------- Extraindo o arquivo do DAQ ---------------------------|")
            subprocess.run(["sudo", "tar", "-xvzf", "daq-2.0.7.tar.gz"])
            subprocess.run(["cd","daq-2.0.7"])
            print("|---------------------------- Arquivo do DAQ extraído ---------------------------|")


            # Compilação e instalação do DAQ
            print("|---------------------------- Configurando o DAQ ---------------------------|")
            subprocess.run(["./configure"])
            print("|---------------------------- Compilação configurada para o DAQ ---------------------------|")
            subprocess.run(["make"])
            subprocess.run(["sudo", "make", "install"])
            print("|---------------------------- DAQ instalado com sucesso ---------------------------|")

            # Download do Snort
            print("|---------------------------- Download do Snort ---------------------------|")
            subprocess.run(["cd", "/tmp/"])
            subprocess.run(["sudo", "wget", "https://www.snort.org/downloads/snort/snort-2.9.20.tar.gz"], check=True)
            print("|---------------------------- Download concluído ---------------------------|")

            # Extração do arquivo Snort
            print("|---------------------------- Extraindo o arquivo do Snort ---------------------------|")
            subprocess.run(["sudo", "tar", "-xvzf", "snort-2.9.20.tar.gz"])
            subprocess.run(["cd","snort-2.9.20"])
            print("|---------------------------- Arquivo do Snort extraído ---------------------------|")
            
            print("|---------------------------- Compilação configurada do snort ---------------------------|")
            subprocess.run(["./configure", "--disable-open-appid", "CFLAGS=-I/usr/include/tirpc"], check=True)
            subprocess.run(["make"], check=True)
            subprocess.run(["sudo", "make", "install"], check=True)
            print("|---------------------------- Snort instalado com sucesso ---------------------------|")


            # Criando diretórios e configurando o Snort
            print("|---------------------------- Criando arquivos de configuração ---------------------------|")
            subprocess.run(["sudo", "touch", "/etc/snort/rules/local.rules"])
            subprocess.run(["sudo", "mkdir", "-p", "/etc/snort/rules"])
            subprocess.run(["sudo", "mkdir", "/var/log/snort"])
            subprocess.run(["sudo", "mkdir", "/usr/local/lib/snort_dynamicrules"])

            print("|---------------------------- Criando usuário do Snort ---------------------------|")
            subprocess.run(["sudo", "groupadd", "snort"], check=True)
            subprocess.run(["sudo", "useradd", "snort", "-r", "-s", "/sbin/nologin", "-c", "SNORT_IDS", "-g", "snort"], check=True)
            
            # Copiando arquivos de configuração
            print("|---------------------------- Copiando arquivos de configuração ---------------------------|")
            subprocess.run(["cd", "/tmp/snort-2.9.20/etc/"])
            subprocess.run(["sudo", "cp", "*.conf *.map", "/etc/snort"])
            
            
            print("|---------------------------- Descarregando as regras ---------------------------|")
            subprocess.run(["cd", "/etc/snort/rules"], check=True)
            subprocess.run(["wget", "https://www.snort.org/downloads/community/snort3-community-rules.tar.gz"], check=True)
            subprocess.run(["tar", "-xvzf", "snort3-community-rules.tar.gz"], check=True)
                      
            print("|------------------------------- Configuração do snort -----------------------------|")         
            print("|---------------------------- !!!!!!!!! ATENÇÃO !!!!!!!! ---------------------------|")         
            snort_menu_conf_geral ()        
            print("|---------------------------- Defina a interface de rede ---------------------------|")         
            input ("Clique enter para continuar...")
            subprocess.run(["sudo", "nano", "/etc/snort/snort.conf"], check=True)
            
            print("|---------------------------- Definindo a interface de rede ---------------------------|")
            subprocess.run(["ip", "a"])
            int_rede = input ("Indique a sua interface de rede: ")
            subprocess.run(["snort", "-i", int_rede, "-c", "/etc/snort/snort.conf", "-A", "console"])
            
            print("|---------------------------- Criando um serviço para facilitar reinício ---------------------------|")
            snort_menu_conf_service ()
            input ("Clique enter para continuar...")
            subprocess.run(["sudo", "nano", "/etc/systemd/system/snort.service"], check=True)
            
            print("|---------------------------- Snort pronto para ser utilizado ---------------------------|")
            print("|------------- De seguida configure o caminho das regras (RULE_PATH) e a nterface de rede (ex: eth0, ens33, etc.) e outros... ---------------------------|")
            subprocess.run(["snort", "-v"])
            enter_clear ()
        except subprocess.CalledProcessError as e:
            print(f"Ocorreu um erro ao executar o comando: {e}")
        #-------------------- limpar a tela                                     
    enter_clear () 
def snort_instalacao3():
    result = subprocess.run(["dpkg", "-l", "snort"], capture_output=True, text=True)        
    if "snort" in result.stdout:
        print("|---------------------------- snort já está instalado ----------------------------|")
    else:
        try:
            print("|---------------------------- Instalando dependências ----------------------------|")
            subprocess.run(["sudo", "apt-get", "install", "-y", "snort"], check=True)
            print("|---------------------------- Snort pronto para ser utilizado ---------------------------|")
            print("|---------------------------- Instalando o Snort ----------------------------|")
            subprocess.run(["sudo", "apt-get", "install", "-y", "snort"], check=True)
            print("|---------------------------- Snort pronto para ser utilizado ---------------------------|")
            print("|---------------------------- Ativando modo promisco ----------------------------|")
            subprocess.run(["ip", "a"])
            int_rede= input("Qaul e a sua interface de rede: ")
            subprocess.run(["sudo", "ip", "link", "set", int_rede, "promisc", "on"], check=True)
            print("|---------------------------- Modo promisco ativado ---------------------------|")
            # Criando diretórios e configurando o Snort
            print("|---------------------------- Criando arquivos de configuração ---------------------------|")
            subprocess.run(["sudo", "touch", "/etc/snort/rules/local.rules"])
            subprocess.run(["snort", "-V"])
            print("|---------------------------- Snort instalado com sucesso ----------------------------|")
            print("|---------------------------- De suida processa as devidas configurações da ferramenta ----------------------------|")
        except subprocess.CalledProcessError as e:
            print(f"Ocorreu um erro ao executar o comando: {e}")
        #-------------------- limpar a tela                                     
    enter_clear () 
def snort_instalacao ():
    while True:
        # Limpar a tela antes de iniciar o porgrama
        subprocess.run(["clear"])
        # Painel Principal (Menu Principal)
        snort_menu_instalacao ()
        escolha = input ("Escolha uma das opções acima: ")
        # Se o utilizador nao ditar nada 
        if escolha == "":
                entrada_invalida1 ()
                continue
        # Se o utilizador digitar alguma coisa diferente 
        else:  
            try:
                opcao = int(escolha)
                match opcao:
                    case 1:
                        print ("Indisponivel no momento...")
                        enter_clear ()
                        continue
                    case 2:
                        print ("Indisponivel no momento...")
                        enter_clear ()
                        continue
                    case 3:
                        snort_instalacao3 ()
                        continue
                    case 4:
                        break   
                    case _:
                        entrada_invalida3 ()
                        continue  
            except ValueError:
                # Se a conversão falhar (não for um número), exibe uma mensagem de erro
                entrada_invalida2 ()
                continue                    
#---> 2. Desinstalar
def snort_desintalar ():
    try:
        print ("|--------------------- Desinstalando o snort ------------------------|")
        subprocess.run(["sudo", "systemctl", "stop", "snort"], check=True)
        subprocess.run(["sudo", "apt", "remove", "--purge", "snort", "-y"], check=True)
        subprocess.run(["sudo", "apt-get", "remove", "--purge", "daq", "libpcap-dev", "libpcre3-dev", "libdumbnet-dev"], capture_output=True, text=True)
        subprocess.run(["sudo", "dpkg", "--remove", "snort"], capture_output=True, text=True)
        subprocess.run(["sudo", "dpkg", "--purge", "snort", "snort-common", "snort-doc"], capture_output=True, text=True)
        subprocess.run(["sudo", "dpkg", "--purge", "snort-rules-default"], capture_output=True, text=True)
        subprocess.run(["sudo", "apt", "autoremove", "-y"], capture_output=True, text=True)
        subprocess.run(["sudo", "apt", "clean", "-y"], capture_output=True, text=True)
        print ("|--------------------- Deletando todos os arquivos ------------------------|")
        subprocess.run(["sudo", "rm", "-rf", "/etc/snort"], check=True)
        subprocess.run(["sudo", "rm", "-rf", "/var/log/snort"], check=True)
        subprocess.run(["sudo", "rm", "-rf", "/var/lib/snort"], check=True)
        subprocess.run(["sudo", "rm", "-rf", "/usr/local/etc/snort"], check=True)
        subprocess.run(["sudo", "rm", "-rf", "/usr/local/bin/snort"], check=True)
        print("|---------------------------- Snort desinstalado com sucesso ---------------------------|")
        print("|-------------- Nao esqueca-se de desativar o modo promisc caso nao for preciso ---------|")
        enter_clear ()
    except subprocess.CalledProcessError as e:
        print(f"Ocorreu um erro ao executar o comando: {e}")
#---> 3. Comandos
def snort_menu_comandos ():
    print("+-----------------------------------------------------------------------------+")
    print("|                                  SNORT                                      |")
    print("+-----------------------------------------------------------------------------+")
    print("|                            C O M A N D O S                                  |")
    print("+-----------------------------------------------------------------------------+")
    print("| 1. | Ativar                                                                 |")
    print("+----+------------------------------------------------------------------------+")
    print("| 2. | Iniciar                                                                |")
    print("+----+------------------------------------------------------------------------+")
    print("| 3. | Estado                                                                 |")
    print("+----+------------------------------------------------------------------------+")
    print("| 4. | Parar                                                                  |")
    print("+----+------------------------------------------------------------------------+")
    print("| 5. | Reiniciar                                                              |")
    print("+----+------------------------------------------------------------------------+")
    print("| 6. | Versão                                                                 |")
    print("+----+------------------------------------------------------------------------+")
    print("| 7. | Monitorar uma interface                                                |")
    print("+----+------------------------------------------------------------------------+")
    print("| 8. | Sair                                                                   |")
    print("+-----------------------------------------------------------------------------+")
    print("|                                - CMEasy -                                   |")
    print("+-----------------------------------------------------------------------------+")
def enable_snort ():
    # Ativação do serviço
    print("|-----------------------> Ativando o servico Fail2ban <------------------------------|")
    subprocess.run(["sudo", "systemctl", "enable", "snort"], check=True)
    print("|-----------------------> snort ativado com sucesso <------------------------------|")
    enter_clear ()
def start_snort ():
    # Iniciação do serviço
    print("|-----------------------> Iniciando o servico Fail2ban <------------------------------|")
    subprocess.run(["sudo", "systemctl", "start", "snort"], check=True)
    print("|-----------------------> snort iniciado com sucesso <-----------------------------|")
    enter_clear ()
def status_snort ():
    # Estado do servico
    subprocess.run(["sudo", "systemctl", "status", "snort"])
    enter_clear ()
def stop_snort ():
    # Ativação do serviço
    print("|-----------------------> Parando o servico Snort <------------------------------|")
    subprocess.run(["sudo", "systemctl", "stop", "snort"], check=True)
    print("|-----------------------> snort foi parado com sucesso <------------------------------|")
    enter_clear()
def restart_snort ():
    # Reativacao do serviço
    print("|-----------------------> Reiniciando o servico Fail2ban <------------------------------|")
    subprocess.run(["sudo", "systemctl", "restart", "snort"], check=True)
    print("|-----------------------> snort reiniciado com sucesso <----------------------------|")
    enter_clear ()  
def restart_snort2 ():
    print("|-----------------------> Reiniciando o servico Fail2ban <------------------------------|")
    try:
        subprocess.run(["sudo", "pkill", "snort"], check=True)
        subprocess.run(["ip", "a"], check=True)
        int_rede = input ("Indique a sua interface de rede: ")
        subprocess.run(["sudo", "snort", "-c", "/etc/snort/snort.conf", "-i", int_rede, "&"], check=True)
    except subprocess.CalledProcessError as e:
        print (f"Aconteceu um erro na execução do comando: {e}")
    print("|-----------------------> snort reiniciado com sucesso <----------------------------|")
    enter_clear ()
def version_snort (): 
    subprocess.run(["snort", "-V"])
    enter_clear() 
def defInt_rede():
    subprocess.run(["ip", "a"])
    int_rede = input ("Indique a sua interface de rede: ")
    subprocess.run(["snort", "-i", int_rede, "-c", "/etc/snort/snort.conf", "-A", "console"])
def comandos_snort ():
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        snort_menu_comandos ()
        escolha = input ("Escolha uma das opções acima: ")
        if escolha == "":
            entrada_invalida1 ()
            continue
        else:
            try:
                opcao = int (escolha)
                match opcao:
                    case 1:
                        enable_snort ()
                        continue
                    case 2:
                        start_snort ()
                        continue
                    case 3:
                        status_snort ()
                        continue
                    case 4:
                        stop_snort ()
                        continue
                    case 5:
                        restart_snort ()
                        continue
                    case 6:
                        version_snort ()
                        continue
                    case 7:
                        defInt_rede ()
                        continue
                    case 8:
                        break
                    case _:
                        entrada_invalida3 ()
                        continue
            except ValueError:
                entrada_invalida2 ()
                continue
#---> 4. Configuracoes
def snort_menu_conf ():
    print("+-------------------------------------------------------------------------------------+")
    print("|                                     SNORT - Conf                                    |")
    print("+-------------------------------------------------------------------------------------+")
    print("|   1.   | Configuracão de alertas e regras.                                          |")
    print("+--------+----------------------------------------------------------------------------+")
    print("|   2.   | Configuracão geral.                                                        |")
    print("+--------+----------------------------------------------------------------------------+")
    print("|   3.   | Criando um serviço para facilitar reinício.                                |")
    print("+--------+----------------------------------------------------------------------------+")
    print("|   4.   | Sair.                                                                      |")
    print("+-------------------------------------------------------------------------------------+")
    print("|                                       - CMEasy -                                    |")
    print("+-------------------------------------------------------------------------------------+")
def snort_menu_conf_alerts ():
    print("+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+")
    print("|                                                                                 SNORT - Alerts                                                                                 |")
    print("+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+")
    print("| Copie e cole os alertas e as regras no arquivo de configuração e de seguida ative o alerta correspondente.                                                                     |")  
    print("+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+")
    print("| Título | Ativar a alerta de tentativa de coneccao FTP.                                                                                                                         |")
    print('| Alerta | alert tcp any any -> any 21 (msg:"[ALERT] Tentativa de Conexão FTP Detectada!"; sid:1000001;)                                                                         |')  
    print('| Regra  | drop tcp $EXTERNAL_NET any -> $HOME_NET 21 (msg:"[BLOCK] Tentativa de FTP bloqueada!"; sid:2000001; rev:1;)                                                           |')  
    print("+--------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+")
    print("| Título | Ativar a alerta de tentativa de coneccao TELNET                                                                                                                       |")
    print('| Alerta | alert tcp $EXTERNAL_NET any -> $HOME_NET 23 (msg:"[ALERTA] Tentativa de Conexão Telnet Detectada."; sid:1000002;)                                                     |')
    print('| Regra  | drop icmp any any -> any any (msg:"[BLOCK] Tentativa de Ping ICMP bloqueada!"; itype:8; sid:3001001; rev:1;)                                                          |')
    print("+--------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+")
    print("| Título | Ativar a alerta de tentativa de coneccao Ping.                                                                                                                        |")
    print('| Alerta | alert icmp $EXTERNAL_NET any -> $HOME_NET any (msg:"Ping ICMP Detectado!"; sid:1000004;)                                                                              |')
    print('| Regra  | drop icmp any any -> any any (msg:"[BLOCK] Tentativa de Ping ICMP bloqueada!"; itype:8; sid:3001001; rev:1;)                                                          |')
    print("+--------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+")
    print("| Título | Ativar a alerta de teste TCP (porta aberta).                                                                                                                          |")
    print('| Alerta | alert tcp any any -> any 80 (msg:"Acesso HTTP Detectado (Porta 80)"; sid:1000003; rev:1;)                                                                             |')
    print("+--------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+")
    print("| Título | Ativar a alerta de Injeção SQL.                                                                                                                                       |")
    print('| Alerta | alert tcp any any -> any 80 (msg:"Tentativa de Injeção SQL Detectada."; sid:1000005; rev:1;)                                                                          |')
    print("+--------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+")
    print("| Título | Ativar a alerta de exploração do wordpress.                                                                                                                           |")
    print('| Alerta | alert tcp any any -> any 80 (msg:"Exploração de WordPress Detectada."; content:"wp-config"; sid:1000102; rev:1;)                                                      |')
    print("+--------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+")
    print("| Título | Ativar a alerta de scan nmap.                                                                                                                                         |")
    print('| Alerta | alert tcp any any -> any any (msg:"Scan Nmap Detectado."; flags:S; sid:1000200; rev:1;)                                                                               |')
    print('| Regra  | drop tcp any any -> any any (msg:"[BLOCK] Nmap SYN Scan detectado"; flags:S; sid:2002001; rev:1;)                                                                     |')
    print("+--------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+")
    print("| Título | Ativar a alerta de scan ssh.                                                                                                                                          |")
    print('| Alerta | alert tcp any any -> any 22 (msg:"Scan SSH Detectado"; sid:1000202; rev:1;)                                                                                           |')
    print("+--------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+")
    print("| Título | Ativar a alerta de tentativa brute force ssh.                                                                                                                         |")
    print('| Alerta | alert tcp any any -> any 22 (msg:"Tentativa de Brute Force SSH Detectada."; flags:S; threshold:type both, track by_src,count 5, seconds 60; sid:1000500; rev:1;)      |')
    print("+--------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+")
    print("| Título | Ativar a alerta de tentativa brute force ftp.                                                                                                                         |")
    print('| Alerta | alert tcp any any -> any 21 (msg:"Tentativa de Brute Force FTP Detectada."; flags:S; threshold:type both, track by_src, count 5, seconds 60; sid:1000501; rev:1;)     |')
    print("+--------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+")
    print("| Título | Ativar a alerta de tentativa de Masscan.                                                                                                                              |")
    print('| Alerta | alert tcp any any -> any any (msg:"Scan Masscan Detectado."; flags:S; sid:1000201; rev:1;)                                                                            |')
    print("+--------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+")
    print("|   1.   | Aceder o arquivo de configuração.                                                                                                                                     |")
    print("+--------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+")
    print("|   2.   | Sair.                                                                                                                                                                 |")
    print("+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+")
    print("|                                                                                  - CMEasy -                                                                                    |")
    print("+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+")
def snort_conf_alerts ():
    while True:
        # Limpar a tela antes de iniciar o porgrama
        os.system("cls" if os.name == "nt" else "clear")
        # Painel Principal (Menu Principal)
        snort_menu_conf_alerts ()
        escolha = input ("Escolha uma das opções acima: ")
        # Se o utilizador nao ditar nada 
        if escolha == "":
                entrada_invalida1 ()
                continue
        # Se o utilizador digitar alguma coisa diferente 
        else:  
            try:
                opcao = int(escolha)
                match opcao:
                    case 1:
                        subprocess.run(["sudo", "nano", "/etc/snort/rules/local.rules"])
                        continue
                    case 2:
                        break   
                    case _:
                        entrada_invalida3 ()
                        continue  
            except ValueError:
                # Se a conversão falhar (não for um número), exibe uma mensagem de erro
                entrada_invalida2 ()
                continue
def configuracao_snort():
    while True:
        # Limpar a tela antes de iniciar o porgrama
        subprocess.run(["clear"])
        # Painel Principal (Menu Principal)
        snort_menu_conf ()
        escolha = input ("Escolha uma das opções acima: ")
        # Se o utilizador nao ditar nada 
        if escolha == "":
                entrada_invalida1 ()
                continue
        # Se o utilizador digitar alguma coisa diferente 
        else:  
            try:
                opcao = int(escolha)
                match opcao:
                    case 1:
                        subprocess.run(["clear"])
                        snort_conf_alerts ()
                        continue
                    case 2:
                        subprocess.run(["clear"])
                        snort_menu_conf_geral ()
                        enter_clear ()
                        subprocess.run(["sudo", "nano", "/etc/snort/snort.conf"], check=True)
                        continue
                    case 3:
                        subprocess.run(["clear"])
                        snort_menu_conf_service ()
                        enter_clear ()
                        subprocess.run(["sudo", "nano", "/etc/systemd/system/snort.service"], check=True)
                        continue
                    case 4:
                        break   
                    case _:
                        entrada_invalida3 ()
                        continue  
            except ValueError:
                # Se a conversão falhar (não for um número), exibe uma mensagem de erro
                entrada_invalida2 ()
                continue
#---> 5. Alertas
def snort_alertas ():
    # Função para validar o formato CIDR
    def validar_endereco_rede(endereco_rede):
        padrao = r"^\d{1,3}(\.\d{1,3}){3}/\d{1,2}$"
        return bool(re.match(padrao, endereco_rede))

    # Solicitar o endereço de rede ao usuário
    ind_rede = input("Indique o endereco de rede 'ex: 192.168.10.0/24': ")

    # Verificar se o endereço de rede é válido
    if not validar_endereco_rede(ind_rede):
        print("Endereço de rede inválido. Por favor, insira no formato correto 'xxx.xxx.xxx.xxx/xx'.")
    else:
        # Se o endereço de rede for válido, rodar o Snort
        print("|-----------------------> Alertas Snort <------------------------------|")
        try:
            subprocess.run(
                ["sudo", "snort", "-d", "-l", "/var/log/snort/", "-h", ind_rede, "-A", "console", "-c", "/etc/snort/snort.conf"],
                check=True
            )
        except subprocess.CalledProcessError as e:
            print(f"Ocorreu um erro ao executar o Snort: {e}")
# Programa Snort
def snort ():
    while True:
        # Limpar a tela antes de iniciar o porgrama
        os.system("cls" if os.name == "nt" else "clear")
        # Painel Principal (Menu Principal)
        snort_menu_principal ()
        escolha = input ("Escolha uma das opções acima: ")
        # Se o utilizador nao ditar nada 
        if escolha == "":
                entrada_invalida1 ()
                continue
        # Se o utilizador digitar alguma coisa diferente 
        else:  
            try:
                opcao = int(escolha)
                match opcao:
                    case 1:
                        snort_instalacao ()
                        continue
                    case 2:
                        snort_desintalar ()
                        continue
                    case 3:
                        comandos_snort ()
                        continue
                    case 4:
                        configuracao_snort ()
                        continue
                    case 5:
                        snort_alertas ()
                        continue
                    case 6:
                        enter_clear ()
                        break   
                    case _:
                        entrada_invalida3 ()
                        continue  
            except ValueError:
                # Se a conversão falhar (não for um número), exibe uma mensagem de erro
                entrada_invalida2 ()
                continue                
#-----------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------
#---> Proxy Squid <---
# Menu Principal
def squid_menu_principal ():
    print("+-----------------------------------------------------------------------------+")
    print("|                                 PROXY SQUID                                 |")
    print("+-----------------------------------------------------------------------------+")
    print("| Oque é ? | O proxy Squid é um intermediário que acede à internet por ti,    |")
    print("|          |podendo controlar, guardar e monitorizar os acessos.              |")
    print("+----------+------------------------------------------------------------------+")
    print("|          | - Cache: guarda páginas já visitadas para carregar mais rápido.  |")
    print("|          | - Controlo de acesso: permite bloquear ou autorizar sites.       |")
    print("| Funções  | - Filtragem: impede conteúdos indesejados.                       |")
    print("|          | - Aumento de segurança: esconde o IP dos utilizadores.           |")
    print("|          | - Monitorização: regista e acompanha o que é acedido na rede.    |")
    print("+----------+------------------------------------------------------------------+")
    print("| Requisi- | SO: Linux (Debian, Ubuntu, CentOS...) ou Windows (em Cygwin).    |")
    print("|tos       | Acesso root / administrador para instalar e configurar o serviço.|") 
    print("|          | Porta de rede livre (padrão: TCP 3128, mas pode ser alterada).   |")
    print("|-----------------------------------------------------------------------------|")
    print("| Site ofi-| Link: https://www.squid-cache.org/                               |")
    print("|cial      |                                                                  |")
    print("|-----------------------------------------------------------------------------|")
    print("|  Testes  | Ubunto (v22).                                                    |")
    print("|-----------------------------------------------------------------------------+")
    print("|       1. Instalar      |      2. Desinstalar       |      3. Comandos       |")
    print("+------------------------+---------------------------+------------------------+")
    print("|    4. Configuracoes    |          5. Logs          |        6. Sair         |")
    print("+-----------------------------------------------------------------------------+")
    print("|                                  @cmeasy                                    |")
    print("+-----------------------------------------------------------------------------+")
#---> 1. Instalar
def squid_instalacao():
    result = subprocess.run(["dpkg", "-l", "snort"], capture_output=True, text=True)        
    if "snort" in result.stdout:
        print("|---------------------------- snort já está instalado ----------------------------|")
    else:
        try:
            print("|---------------------------- Atualizando os pacotes  ------------------------------|")
            subprocess.run(["sudo", "apt", "update"], check=True)
            print("|------------------------ Pacotes atualizados com sucesso --------------------------|")
    
            print("|---------------------------- Instalando o Proxy Squid ----------------------------|")
            subprocess.run(["sudo", "apt", "install", "squid", "-y"], check=True)
            print("|---------------------------- Proxy squid instaldo com sucesso ---------------------------|")

            subprocess.run("echo '# Liste os sites que pretende (ex: .facebook.com)' >> /etc/squid/bad-sites.acl", shell=True)
            
            print("|-----------------------> Ativando o servico Squid <------------------------------|")
            subprocess.run(["sudo", "systemctl", "enable", "squid"], check=True)
            print("|-----------------------> squid ativado com sucesso <------------------------------|")
            
            print("|-----------------------> Iniciando o servico Squid <------------------------------|")
            subprocess.run(["sudo", "systemctl", "start", "squid"], check=True)
            print("|-----------------------> squid iniciado com sucesso <-----------------------------|")

            subprocess.run(["squid", "-v"])
        except subprocess.CalledProcessError as e:
            print(f"Ocorreu um erro ao executar o comando: {e}")
        #-------------------- limpar a tela                                     
    enter_clear ()                 
#---> 2. Desinstalar
def squid_desintalar ():
    try:
        print ("|--------------------- Desinstalando o squid ------------------------|")
        subprocess.run(["sudo", "systemctl", "stop", "squid"], check=True)
        subprocess.run(["sudo", "apt", "purge", "squid", "-y"], check=True)
        subprocess.run(["sudo", "apt", "autoremove", "-y"], capture_output=True, text=True)
        subprocess.run(["sudo", "rm", "-rf", "/var/spool/squid", "/var/log/squid", "/etc/squid"], capture_output=True, text=True)
        print("|---------------------------- Squid desinstalado com sucesso ---------------------------|")
        enter_clear ()
    except subprocess.CalledProcessError as e:
        print(f"Ocorreu um erro ao executar o comando: {e}")
        enter_clear ()
#---> 3. Comandos
def squid_menu_comandos ():
    print("+-----------------------------------------------------------------------------+")
    print("|                                  SQUID                                      |")
    print("+-----------------------------------------------------------------------------+")
    print("|                            C O M A N D O S                                  |")
    print("+-----------------------------------------------------------------------------+")
    print("| 1. | Ativar                                                                 |")
    print("+----+------------------------------------------------------------------------+")
    print("| 2. | Iniciar                                                                |")
    print("+----+------------------------------------------------------------------------+")
    print("| 3. | Estado                                                                 |")
    print("+----+------------------------------------------------------------------------+")
    print("| 4. | Parar                                                                  |")
    print("+----+------------------------------------------------------------------------+")
    print("| 5. | Reiniciar                                                              |")
    print("+----+------------------------------------------------------------------------+")
    print("| 6. | Versão                                                                 |")
    print("+----+------------------------------------------------------------------------+")
    print("| 7. | Sair                                                                   |")
    print("+-----------------------------------------------------------------------------+")
    print("|                                - CMEasy -                                   |")
    print("+-----------------------------------------------------------------------------+")
def enable_squid ():
    # Ativação do serviço
    print("|-----------------------> Ativando o servico Squid <------------------------------|")
    subprocess.run(["sudo", "systemctl", "enable", "squid"], check=True)
    print("|-----------------------> squid ativado com sucesso <------------------------------|")
    enter_clear ()
def start_squid ():
    # Iniciação do serviço
    print("|-----------------------> Iniciando o servico Squid <------------------------------|")
    subprocess.run(["sudo", "systemctl", "start", "squid"], check=True)
    print("|-----------------------> squid iniciado com sucesso <-----------------------------|")
    enter_clear ()
def status_squid ():
    # Estado do servico
    subprocess.run(["sudo", "systemctl", "status", "squid.service"])
    enter_clear ()
def stop_squid ():
    # Ativação do serviço
    print("|-----------------------> Parando o servico Squid <------------------------------|")
    subprocess.run(["sudo", "systemctl", "stop", "squid"], check=True)
    print("|-----------------------> squid foi parado com sucesso <------------------------------|")
    enter_clear()
def restart_squid ():
    # Reativacao do serviço
    print("|-----------------------> Reiniciando o servico squid <------------------------------|")
    subprocess.run(["sudo", "systemctl", "restart", "squid"], check=True)
    print("|-----------------------> squid reiniciado com sucesso <----------------------------|")
    enter_clear ()
def version_squid (): 
    subprocess.run(["squid", "-v"])
    enter_clear() 
def comandos_squid ():
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        squid_menu_comandos ()
        escolha = input ("Escolha uma das opções acima: ")
        if escolha == "":
            entrada_invalida1 ()
            continue
        else:
            try:
                opcao = int (escolha)
                match opcao:
                    case 1:
                        enable_squid ()
                        continue
                    case 2:
                        start_squid ()
                        continue
                    case 3:
                        status_squid ()
                        continue
                    case 4:
                        stop_squid ()
                        continue
                    case 5:
                        restart_squid ()
                        continue
                    case 6:
                        version_squid ()
                        continue
                    case 7:
                        break
                    case _:
                        entrada_invalida3 ()
                        continue
            except ValueError:
                entrada_invalida2 ()
                continue
#---> 4. Configuracoes
def squid_menu_cof1 ():   
    print("+-------------------------------------------------------------------------------------+")
    print("|                                     SQUID Conf                                      |")
    print("+-------------------------------------------------------------------------------------+")
    print("|   1.   | Arquivo de configuracao.                                                   |")
    print("+--------+----------------------------------------------------------------------------+")
    print("|   2.   | Boquei de Url's.                                                           |")
    print("+--------+----------------------------------------------------------------------------+")
    print("|   3.   | Sair.                                                                      |")
    print("+-------------------------------------------------------------------------------------+")
    print("|                                       - CMEasy -                                    |")
    print("+-------------------------------------------------------------------------------------+")
def squid_menu_cof2 ():
    print("+-------------------------------------------------------------------------------------+")
    print("|                                     SQUID Conf                                      |")
    print("+-------------------------------------------------------------------------------------+")
    print("| Altere estas configuracoes deacordo ao seu ambiente, e cuidado com duplicidade de   |")
    print("|codigo.                                                                              |")
    print("+-------------------------------------------------------------------------------------+")
    print("|   1.   | Definir a porta por defeito (Opcional, pos ja vem configurado).            |")
    print("| Codigo | port http_port 3128                                                        |")
    print("+--------+----------------------------------------------------------------------------+")
    print("|   2.   | Define a rede local permitida (toda a subnet 192.168.1.0/24).              |")
    print("| Codigo | acl localnet src 192.168.1.0/24                                            |")
    print("+--------+----------------------------------------------------------------------------+")
    print("|   a)   | Bloquer o acesso de um ip ao exterior.                                     |")
    print("+--------+----------------------------------------------------------------------------+")
    print("| Acl: acl ip_bloqueado src 192.168.1.100 | Info: Define o IP que queremos bloquear.  |")
    print("| Regra: http_access deny ip_bloqueado    | Info: Nega acesso ao IP bloqueado.        |")
    print("+--------+----------------------------------------------------------------------------+")
    print("|   b)   | Definir lista de sites para serem bloqueados.                              |")
    print("+--------+----------------------------------------------------------------------------+")
    print("| Acl: acl bad_url dstdomain “/etc/squid/bad-sites.acl”                               |")
    print("| Regra: http_access deny bad_url                                                     |")
    print("+-------------------------------------------------------------------------------------+")
    print("|   3.   | permite o acesso ao proxy para todos os IPs que estão na ACL localnet.     |")
    print("| Codigo | http_access allow localnet                                                 |")
    print("+-------------------------------------------------------------------------------------+")
    print("|   4.   | Nega tudo o resto (segurança — regra final).                               |")
    print("| Codigo | http_access deny all                                                       |")
    print("+-------------------------------------------------------------------------------------+")
    print("| No final reinicie o servico squid e configure o browser do host com o ip do         |")
    print("|servidor e e prta correspondente.                                                    |")
    print("+-------------------------------------------------------------------------------------+")
    print("|                          Precione [ E N T E R ] para continuar                      |")
    print("+-------------------------------------------------------------------------------------+")
    print("|                                       - CMEasy -                                    |")
    print("+-------------------------------------------------------------------------------------+")
def squid_menu_cof3 ():
    print("+-------------------------------------------------------------------------------------+")
    print("|                                SQUID - Conf - Sintaxe                               |")
    print("+-------------------------------------------------------------------------------------+")
    print("|1. Definir ACLs (Critérios usados para decidir quem ou o quê pode aceder ao proxy.). |")
    print("|2. Regras específicas.                                                               |")
    print("|3. Regra final (catch-all 'seguranca').                                              |")
    print("+-------------------------------------------------------------------------------------+")
    print("|                          Precione [ E N T E R ] para continuar                      |")
    print("+-------------------------------------------------------------------------------------+")
    print("|                                       - CMEasy -                                    |")
    print("+-------------------------------------------------------------------------------------+")
def squid_logs ():    
    while True:
        subprocess.run(["clear"])
        print("+-------------------------------------------------------------------------------------+")
        print("|                                     SQUID Logs                                      |")
        print("+-------------------------------------------------------------------------------------+")
        print("|   1.   | Monitorizar o trafego proxy.                                               |")
        print("+--------+----------------------------------------------------------------------------+")
        print("|   2.   | Monitorizar a cache.                                                       |")
        print("+--------+----------------------------------------------------------------------------+")
        print("|   3.   | Sair.                                                                      |")
        print("+-------------------------------------------------------------------------------------+")
        print("|                                       - CMEasy -                                    |")
        print("+-------------------------------------------------------------------------------------+")
        escolha = input ("Escolha uma das opções acima: ")
        # Se o utilizador nao ditar nada 
        if escolha == "":
                entrada_invalida1 ()
                continue
        # Se o utilizador digitar alguma coisa diferente 
        else:  
            try:
                opcao = int(escolha)
                match opcao:
                    case 1:
                        subprocess.run(["clear"])
                        print ("|------------- Registro de acesso ao exterior ----------------|")
                        subprocess.run(["sudo", "tail", "-f", "/var/log/squid/access.log"])
                        continue
                    case 2:
                        subprocess.run(["clear"])
                        print ("|------------- Registro de acesso ----------------|")
                        subprocess.run(["sudo", "tail", "-f", "/var/log/squid/cache.log"])
                        continue
                    case 3:
                        break   
                    case _:
                        entrada_invalida3 ()
                        continue  
            except ValueError:
                # Se a conversão falhar (não for um número), exibe uma mensagem de erro
                entrada_invalida2 ()
                continue              
def squid_cof ():
    while True:
        # Limpar a tela antes de iniciar o porgrama
        subprocess.run(["clear"])
        # Painel Principal (Menu Principal)
        squid_menu_cof1 ()
        escolha = input ("Escolha uma das opções acima: ")
        # Se o utilizador nao ditar nada 
        if escolha == "":
                entrada_invalida1 ()
                continue
        # Se o utilizador digitar alguma coisa diferente 
        else:  
            try:
                opcao = int(escolha)
                match opcao:
                    case 1:
                        subprocess.run(["clear"])
                        squid_menu_cof3 ()
                        input ("Clique < ENTER > para continuar")
                        subprocess.run(["clear"])
                        squid_menu_cof2 ()
                        input ("Clique < ENTER > para continuar")
                        subprocess.run(["sudo", "nano", "/etc/squid/squid.conf"])
                        continue
                    case 2:
                        subprocess.run(["sudo", "nano", "/etc/squid/bad-sites.acl"])
                        continue
                    case 3:
                        break   
                    case _:
                        entrada_invalida3 ()
                        continue  
            except ValueError:
                # Se a conversão falhar (não for um número), exibe uma mensagem de erro
                entrada_invalida2 ()
                continue                
# Programa Squid
def proxy_squid ():
    while True:
        # Limpar a tela antes de iniciar o porgrama
        os.system("cls" if os.name == "nt" else "clear")
        # Painel Principal (Menu Principal)
        squid_menu_principal ()
        escolha = input ("Escolha uma das opções acima: ")
        # Se o utilizador nao ditar nada 
        if escolha == "":
                entrada_invalida1 ()
                continue
        # Se o utilizador digitar alguma coisa diferente 
        else:  
            try:
                opcao = int(escolha)
                match opcao:
                    case 1:
                        squid_instalacao ()
                        continue
                    case 2:
                        squid_desintalar ()
                        continue
                    case 3:
                        comandos_squid ()
                        continue
                    case 4:
                        squid_cof ()
                        continue
                    case 5:
                        squid_logs ()
                        continue
                    case 6:
                        break   
                    case _:
                        entrada_invalida3 ()
                        continue  
            except ValueError:
                # Se a conversão falhar (não for um número), exibe uma mensagem de erro
                entrada_invalida2 ()
                continue                
#-----------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------
#---> Bwapp <---
# Menu Principal
def bwapp_menu_principal ():
    print("+-----------------------------------------------------------------------------+")
    print("|                                    BWAPP                                    |")
    print("+-----------------------------------------------------------------------------+")
    print("| Oque é ? | O bWAPP é um site com falhas de segurança criadas de propósito   |")
    print("|          |para aprender segurança informática.                              |")
    print("+----------+------------------------------------------------------------------+")
    print("|          | - Permitir praticar testes de segurança em aplicações web.       |")
    print("|          | - Simular vulnerabilidades reais (como SQL Injection e XSS).     |")
    print("| Funções  | - Ajudar a aprender hacking ético.                               |")
    print("|          | - Ambiente seguro para treino e estudo de cibersegurança.        |")
    print("+----------+------------------------------------------------------------------+")
    print("| Requisi- | Sistema operativo (Windows, Linux ou macOS).                     |")
    print("|tos       | Servidor local (ex: XAMPP ou WAMP).                              |") 
    print("|          | Navegador web (Chrome, Firefox, etc.).                           |")
    print("|-----------------------------------------------------------------------------|")
    print("| Site ofi-| Link: https://github.com/ajpalok/bWAPP                           |")
    print("|cial      |                                                                  |")
    print("|-----------------------------------------------------------------------------|")
    print("|  Testes  |                                                                  |")
    print("|-----------------------------------------------------------------------------+")
    print("|             1. Instalar               |          2. Desinstalar             |")
    print("+---------------------------------------+-------------------------------------+")
    print("|          3. Configuracoes             |            4. Voltar                |")
    print("+-----------------------------------------------------------------------------+")
    print("|                                  @cmeasy                                    |")
    print("+-----------------------------------------------------------------------------+")
def bwapp_instalacao_config ():
    print("+-----------------------------------------------------------------------------+")
    print("|      Cipie e cole estes comandos no arquivo de configuração do php          |")
    print("+-----------------------------------------------------------------------------+")
    print('$db_server = "localhost";')
    print('$db_username = "bwappuser";  // usuário criado no MariaDB')
    print('$db_password = "bwapp123";   // senha definida para esse usuário')
    print('$db_name = "bWAPP";')
    print("+-----------------------------------------------------------------------------+")
def bwapp_instalacao_conf2 ():
    print("+-----------------------------------------------------------------------------+")
    print("|      Cipie e cole estes comandos no arquivo de configuração do php          |")
    print("+-----------------------------------------------------------------------------+")
    print("CREATE USER 'bwappuser'@'localhost' IDENTIFIED BY 'bwapp123';")
    print("GRANT ALL PRIVILEGES ON bWAPP.* TO 'bwappuser'@'localhost';") 
    print("FLUSH PRIVILEGES;") 
    print("EXIT;") 
    print("+-----------------------------------------------------------------------------+")
def bwapp_instalacao():
    result = subprocess.run(["dpkg", "-l", "bwapp"], capture_output=True, text=True)        
    if "bwapp" in result.stdout:
        print("|---------------------------- Bwapp já está instalado ----------------------------|")
    else:
        try:
            subprocess.run(["sudo", "systemctl", "stop", "unattended-upgrades"], check=True)
            subprocess.run(["sudo", "systemctl", "disable", "unattended-upgrades"], check=True)
            print("|---------------------------- Atualizando os pacotes  ------------------------------|")
            subprocess.run(["sudo", "apt", "update"], check=True)
            subprocess.run(["sudo", "apt", "install", "wget"], check=True)
            print("|------------------------ Pacotes atualizados com sucesso --------------------------|")
            
            print("|---------------------------- Instalando o dependencias necessarias ----------------------------|")
            subprocess.run(["sudo", "apt", "install", "apache2", "mariadb-server", "-y"], check=True)
            subprocess.run(["sudo", "systemctl", "enable", "apache2"], check=True)
            subprocess.run(["sudo", "systemctl", "start", "apache2"], check=True)
            subprocess.run(["sudo", "apt", "install", "software-properties-common", "-y"], check=True)
            subprocess.run(["sudo", "add-apt-repository", "ppa:ondrej/php", "-y"], check=True)
            subprocess.run(["sudo", "apt", "install", "php7.4", "libapache2-mod-php7.4", "php7.4-mysqli", "php7.4-curl", "php7.4-gd", "php7.4-mbstring", "unzip", "-y"], check=True)
            subprocess.run(["php", "-v"], check=True)
            subprocess.run(["sudo", "a2enmod", "php7.4"], check=True)
            subprocess.run(["sudo", "systemctl", "restart", "apache2"], check=True)
            print("|---------------------------- Dependencias instaladas com sucesso ---------------------------|")
            
            print("|---------------------------- Realizando o download bwapp----------------------------|")
            subprocess.run(["wget", "https://deac-ams.dl.sourceforge.net/project/bwapp/bWAPP/bWAPPv2.2/bWAPPv2.2.zip"], check=True)
            print("|---------------------------- Download concluido ---------------------------|")
             
            print("|---------------------------- Preparando os arquivo ----------------------------|")
            subprocess.run(["unzip", "bWAPPv2.2.zip"], check=True)
            subprocess.run(["sudo", "mv", "bWAPP", "/var/www/html/"], check=True)
            subprocess.run(["sudo", "chmod", "-R", "777", "/var/www/html/bWAPP"], check=True)
            print("|---------------------------- Bwapp instaldo com sucesso ---------------------------|")
            
            print("|---------------------------- Agora processeda a configuração do php bwapp ---------------------------|")
            bwapp_instalacao_config ()
            input ("Precione entrer para continuar... ")
            subprocess.run(["sudo", "nano", "/var/www/html/bWAPP/admin/settings.php"], check=True)
            print("|---------------------------- Aceda ao link a baixo para Inicial a instalação pelo bwroser ---------------------------|")
            print("|User: bee    &     pass: bug ")
            print("Link: http://localhost/bWAPP/install.php")
            subprocess.run(["sudo", "systemctl", "enable", "unattended-upgrades"], check=True)
            subprocess.run(["sudo", "systemctl", "start", "unattended-upgrades"], check=True)
            
            bwapp_instalacao_conf2 ()
            input ("Precione entrer para continuar... ")
            subprocess.run(["sudo", "mariadb"], check=True)
            print("|---------------------------- Aceda ao link a baixo para Inicial a instalação pelo bwroser ---------------------------|")
            print("|User: bee    &     pass: bug ")
            print("Link: http://localhost/bWAPP/install.php")
            print("|---------------------------------------------------------------------------------------------------------------------|")
            subprocess.run(["sudo", "systemctl", "enable", "unattended-upgrades"], check=True)
            subprocess.run(["sudo", "systemctl", "start", "unattended-upgrades"], check=True)

        except subprocess.CalledProcessError as e:
            print(f"Ocorreu um erro ao executar o comando: {e}")
        #-------------------- limpar a tela                                     
    enter_clear () 
def bwapp_desinstalacao ():
    try:
        print ("|--------------------- Desinstalando o bwapp ------------------------|")
        subprocess.run(["sudo", "systemctl", "stop", "apache2"], check=True)
        subprocess.run(["sudo", "systemctl", "stop", "mariadb"], check=True)
        subprocess.run(["sudo", "rm", "-rf", "/var/www/html/bWAPP"], check=True)
        subprocess.run(["sudo", "rm", "-f", "/var/log/apache2/bWAPP*"], check=True)
        subprocess.run(["sudo", "systemctl", "restart", "apache2"], check=True)
        subprocess.run(["sudo", "systemctl", "restart", "mariadb"], check=True)
        print("|---------------------------- bwapp desinstalado com sucesso ---------------------------|")
        print("|---------------------------- Caso seje presiso elimine a base de dados ---------------------------|")
    except subprocess.CalledProcessError as e:
        print(f"Ocorreu um erro ao executar o comando: {e}")
    #-------------------- limpar a tela                                     
    enter_clear () 
# Programa bwapp
def bwapp ():
    while True:
        # Limpar a tela antes de iniciar o porgrama
        os.system("cls" if os.name == "nt" else "clear")
        # Painel Principal (Menu Principal)
        bwapp_menu_principal ()
        escolha = input ("Escolha uma das opções acima: ")
        # Se o utilizador nao ditar nada 
        if escolha == "":
                entrada_invalida1 ()
                continue
        # Se o utilizador digitar alguma coisa diferente 
        else:  
            try:
                opcao = int(escolha)
                match opcao:
                    case 1:
                        bwapp_instalacao ()
                        continue
                    case 2:
                        bwapp_desinstalacao ()
                        continue
                    case 3:
                        os.system("cls" if os.name == "nt" else "clear")
                        bwapp_instalacao_config ()
                        input ("Clique enter para continuar...")
                        subprocess.run(["sudo", "nano", "/var/www/html/bWAPP/admin/settings.php"], check=True)
                        continue
                    case 4:
                        break   
                    case _:
                        entrada_invalida3 ()
                        continue  
            except ValueError:
                # Se a conversão falhar (não for um número), exibe uma mensagem de erro
                entrada_invalida2 ()
                continue 
#-----------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------
#---> suricata <---
# Menu Principal
def suricata_menu_principal ():
    print("+-----------------------------------------------------------------------------+")
    print("|                                 SURICATA                                    |")
    print("+-----------------------------------------------------------------------------+")
    print("| Oque é ? | IDS (Sistema de Deteção de Intrusões) que analisa o tráfego de   |")
    print("|          |rede para encontrar atividades suspeitas ou ataques.              |")
    print("+----------+------------------------------------------------------------------+")
    print("|          | - Deteção de intrusões (IDS).                                    |")
    print("|          | - Prevenção de intrusões (IPS).                                  |")
    print("| Funções  | - Análise de tráfego.                                            |")
    print("|          | - Uso de regras.                                                 |")
    print("|          | - Identificação de protocolos.                                   |")
    print("+----------+------------------------------------------------------------------+")
    print("| Requisi- | CPU: pelo menos 2 núcleos.                                       |")
    print("|tos       | RAM: mínimo 4 GB (8 GB recomendado).                             |") 
    print("|          | Disco: cerca de 16 GB (ou mais).                                 |")
    print("|-----------------------------------------------------------------------------|")
    print("| Site ofi-| Link: https://suricata.io/                                       |")
    print("|-----------------------------------------------------------------------------|")
    print("|  Testes  |                                                                  |")
    print("|-----------------------------------------------------------------------------+")
    print("|       1. Instalar      |      2. Desinstalar       |      3. Comandos       |")
    print("+------------------------+---------------------------+------------------------+")
    print("|    4. Configuracoes    |          5. Logs          |        6. Sair         |")
    print("+-----------------------------------------------------------------------------+")
    print("|                                  @cmeasy                                    |")
    print("+-----------------------------------------------------------------------------+")    
def suricata_instalacao():
    result = subprocess.run(["dpkg", "-l", "suricata"], capture_output=True, text=True)        
    if "suricata" in result.stdout:
        print("|---------------------------- Surucata já está instalado ----------------------------|")
    else:
        try:
            subprocess.run(["sudo", "systemctl", "stop", "unattended-upgrades"], check=True)
            subprocess.run(["sudo", "systemctl", "disable", "unattended-upgrades"], check=True)
            print("|---------------------------- Atualizando os pacotes  ------------------------------|")
            subprocess.run(["sudo", "apt", "update"], check=True)
            subprocess.run(["sudo", "apt", "install", "curl"], check=True)
            print("|------------------------ Pacotes atualizados com sucesso --------------------------|")
            
            print("|---------------------------- Instalando o dependencias necessarias ----------------------------|")
            subprocess.run(["sudo", "apt", "install", "-y", "software-properties-common", "curl"], check=True)          
            subprocess.run(["sudo", "add-apt-repository", "ppa:oisf/suricata-stable"], check=True)
            subprocess.run(["sudo", "apt", "update"], check=True)
            print("|---------------------------- Dependencias instaladas com sucesso ---------------------------|")
            
            print("|---------------------------- Instalando o Suricata ---------------------------|")            
            subprocess.run(["sudo", "apt", "install", "-y", "suricata"], check=True)
            print("|---------------------------- Suricata Instalado com sucesso ---------------------------|")            
            
            print("|---------------------------- Criando arquivo paras regras ---------------------------|") 
            subprocess.run(["mkdir", "-p", "/etc/suricata/rules/"], check=True)
            subprocess.run(["curl", "-LO", "https://rules.emergingthreats.net/open/suricata-7.0.3/emerging.rules.tar.gz"], check=True)
            subprocess.run(["tar", "-xvzf", "emerging.rules.tar.gz"], check=True)                
            subprocess.run("sudo mv rules/*.rules /etc/suricata/rules/", shell=True, check=True)
            subprocess.run("sudo chown -R suricata:suricata /etc/suricata/rules/", shell=True, check=True)
            subprocess.run("sudo chmod 640 /etc/suricata/rules/*.rules", shell=True, check=True)
            print("|---------------------------- Arquivo criado com sucesso ---------------------------|")  
            
            
            print("|---------------------------- Ativando modo promisco ----------------------------|")
            subprocess.run(["ip", "a"])
            int_rede= input("Qaul e a sua interface de rede: ")
            subprocess.run(["sudo", "ip", "link", "set", int_rede, "promisc", "on"], check=True)
            print("|---------------------------- Modo promisco ativado ---------------------------|")          
            
            
            subprocess.run(["sudo", "systemctl", "start", "suricata"], check=True)
            subprocess.run(["sudo", "systemctl", "enable", "suricata"], check=True)
            
            print("|---------------------------- Suricata Pronto a ser utilizado ----------------------------|")     
            print("|---------------------------- Passe agora para configuração ----------------------------|")            
                        
            subprocess.run(["sudo", "systemctl", "enable", "unattended-upgrades"], check=True)
            subprocess.run(["sudo", "systemctl", "start", "unattended-upgrades"], check=True)

        except subprocess.CalledProcessError as e:
            print(f"Ocorreu um erro ao executar o comando: {e}")
        #-------------------- limpar a tela                                     
    enter_clear () 
#---> 2. Desinstalar
def suricata_desinstalar ():
    try:
        print ("|--------------------- Desinstalando o suricata ------------------------|")
        subprocess.run(["sudo", "systemctl", "stop", "suricata"], check=True)
        subprocess.run(["sudo", "systemctl", "disable", "suricata"], check=True)
        subprocess.run(["sudo", "apt-get", "purge", "suricata"], check=True)
        subprocess.run(["sudo", "apt-get", "autoremove"], check=True)
        print ("|--------------------- Deletando todos os arquivos ------------------------|")
        subprocess.run(["sudo", "rm", "-rf", "/etc/suricata"], check=True)
        subprocess.run(["sudo", "rm", "-rf", "/etc/suricata"], check=True)
        subprocess.run(["sudo", "rm", "-rf", "/usr/share/suricata"], check=True)
        subprocess.run(["sudo", "rm", "-rf", "/var/lib/suricata"], check=True)
        print("|---------------------------- suricata desinstalado com sucesso ---------------------------|")
        enter_clear ()
    except subprocess.CalledProcessError as e:
        print(f"Ocorreu um erro ao executar o comando: {e}")
# Comandos 
def suricata_menu_comandos ():
    print("+-----------------------------------------------------------------------------+")
    print("|                                SURICATA                                     |")
    print("+-----------------------------------------------------------------------------+")
    print("|                            C O M A N D O S                                  |")
    print("+-----------------------------------------------------------------------------+")
    print("| 1. | Ativar                                                                 |")
    print("+----+------------------------------------------------------------------------+")
    print("| 2. | Iniciar                                                                |")
    print("+----+------------------------------------------------------------------------+")
    print("| 3. | Estado                                                                 |")
    print("+----+------------------------------------------------------------------------+")
    print("| 4. | Parar                                                                  |")
    print("+----+------------------------------------------------------------------------+")
    print("| 5. | Reiniciar                                                              |")
    print("+----+------------------------------------------------------------------------+")
    print("| 6. | Versão                                                                 |")
    print("+----+------------------------------------------------------------------------+")
    print("| 7. | Sair                                                                   |")
    print("+-----------------------------------------------------------------------------+")
    print("|                                - CMEasy -                                   |")
    print("+-----------------------------------------------------------------------------+")
def enable_suricata ():
    # Ativação do serviço
    print("|-----------------------> Ativando o servico Suricata <------------------------------|")
    subprocess.run(["sudo", "systemctl", "enable", "suricata"], check=True)
    print("|-----------------------> suricata ativado com sucesso <------------------------------|")
    enter_clear ()
def start_suricata ():
    # Iniciação do serviço
    print("|-----------------------> Iniciando o servico Suricata <------------------------------|")
    subprocess.run(["sudo", "systemctl", "start", "suricata"], check=True)
    print("|-----------------------> suricata iniciado com sucesso <-----------------------------|")
    enter_clear ()
def status_suricata ():
    # Estado do servico
    subprocess.run(["sudo", "systemctl", "status", "suricata.service"])
    enter_clear ()
def stop_suricata ():
    # Ativação do serviço
    print("|-----------------------> Parando o servico Suricata <------------------------------|")
    subprocess.run(["sudo", "systemctl", "stop", "suricata"], check=True)
    print("|-----------------------> suricata foi parado com sucesso <------------------------------|")
    enter_clear()
def restart_suricata ():
    # Reativacao do serviço
    print("|-----------------------> Reiniciando o servico suricata <------------------------------|")
    subprocess.run(["sudo", "systemctl", "restart", "suricata"], check=True)
    print("|-----------------------> suricata reiniciado com sucesso <----------------------------|")
    enter_clear ()
def version_suricata (): 
    subprocess.run(["suricata", "-v"])
    enter_clear() 
def comandos_suricata ():
    while True:
        subprocess.run(["clear"])
        suricata_menu_comandos ()
        escolha = input ("Escolha uma das opções acima: ")
        if escolha == "":
            entrada_invalida1 ()
            continue
        else:
            try:
                opcao = int (escolha)
                match opcao:
                    case 1:
                        enable_suricata ()
                        continue
                    case 2:
                        start_suricata ()
                        continue
                    case 3:
                        status_suricata ()
                        continue
                    case 4:
                        stop_suricata ()
                        continue
                    case 5:
                        restart_suricata ()
                        continue
                    case 6:
                        version_suricata ()
                        continue
                    case 7:
                        break
                    case _:
                        entrada_invalida3 ()
                        continue
            except ValueError:
                entrada_invalida2 ()
                continue
#---> 4. Configuracoes
def suricata_menu_config ():   
    print("+-------------------------------------------------------------------------------------+")
    print("|                                   SURICATA Config                                   |")
    print("+-------------------------------------------------------------------------------------+")
    print("|   1.   | Arquivo de configuração.                                                   |")
    print("+--------+----------------------------------------------------------------------------+")
    print("|   2.   | Arquivos das regras.                                                       |")
    print("+--------+----------------------------------------------------------------------------+")
    print("|   3.   | Testar as configurações.                                                   |")
    print("+--------+----------------------------------------------------------------------------+")
    print("|   4.   | Voltar.                                                                    |")
    print("+-------------------------------------------------------------------------------------+")
    print("|                                     - CMEasy -                                      |")
    print("+-------------------------------------------------------------------------------------+")
def suricata_menu_config_geral ():   
    print("+-------------------------------------------------------------------------------------+")
    print("|                             SURICATA Configuração geral                             |")
    print("+-------------------------------------------------------------------------------------+")
    print("| Siga o guia de configuração e tenha atenção a comandos duplicados, espaços, e       |")
    print("|comandos mal escritos para evitar erros durante a inicialização do serviço.          |")
    print("+-------------------------------------------------------------------------------------+")
    print("| 1. | Rede interna monitorada                                                        |")
    print('|    | HOME_NET: "[192.168.15.0/24]"                                                  |')
    print("+----+--------------------------------------------------------------------------------+")
    print("| 2. | Rede externa (todo o resto)                                                    |")
    print('|    | EXTERNAL_NET: "any"                                                            |')
    print("+----+--------------------------------------------------------------------------------+")
    print("| 3. | Caminho das regras                                                             |")
    print('|    | default-rule-path: /etc/suricata/rules                                         |')
    print('|    | rule-files:                                                                    |')
    print('|    | - "*.rules"                                                                    |')
    print("+----+--------------------------------------------------------------------------------+")
    print("| 4. | Captura de pacotes em alta velocidade na interface enp0s3.                     |")
    print('|    | af-packet:                                                                     |')
    print('|    | - interface: enp0s3                                                            |')
    print("+----+--------------------------------------------------------------------------------+")
    print("| 2. | Ativação do modo promiscuo                                                     |")
    print('|    | disable-promisc: no                                                            |')
    print("+-------------------------------------------------------------------------------------+")
    print("|                                     - CMEasy -                                      |")
    print("+-------------------------------------------------------------------------------------+")
    input ("Clique enter para aceder o arquivo...")
def squid_menu_cof2 ():
    print("+-------------------------------------------------------------------------------------+")
    print("|                                     SQUID Conf                                      |")
    print("+-------------------------------------------------------------------------------------+")
    print("| Altere estas configuracoes deacordo ao seu ambiente, e cuidado com duplicidade de   |")
    print("|codigo.                                                                              |")
    print("+-------------------------------------------------------------------------------------+")
    print("|   1.   | Definir a porta por defeito (Opcional, pos ja vem configurado).            |")
    print("| Codigo | port http_port 3128                                                        |")
    print("+--------+----------------------------------------------------------------------------+")
    print("|   2.   | Define a rede local permitida (toda a subnet 192.168.1.0/24).              |")
    print("| Codigo | acl localnet src 192.168.1.0/24                                            |")
    print("+--------+----------------------------------------------------------------------------+")
    print("|   a)   | Bloquer o acesso de um ip ao exterior.                                     |")
    print("+--------+----------------------------------------------------------------------------+")
    print("| Acl: acl ip_bloqueado src 192.168.1.100 | Info: Define o IP que queremos bloquear.  |")
    print("| Regra: http_access deny ip_bloqueado    | Info: Nega acesso ao IP bloqueado.        |")
    print("+--------+----------------------------------------------------------------------------+")
    print("|   b)   | Definir lista de sites para serem bloqueados.                              |")
    print("+--------+----------------------------------------------------------------------------+")
    print("| Acl: acl bad_url dstdomain “/etc/squid/bad-sites.acl”                               |")
    print("| Regra: http_access deny bad_url                                                     |")
    print("+-------------------------------------------------------------------------------------+")
    print("|   3.   | permite o acesso ao proxy para todos os IPs que estão na ACL localnet.     |")
    print("| Codigo | http_access allow localnet                                                 |")
    print("+-------------------------------------------------------------------------------------+")
    print("|   4.   | Nega tudo o resto (segurança — regra final).                               |")
    print("| Codigo | http_access deny all                                                       |")
    print("+-------------------------------------------------------------------------------------+")
    print("| No final reinicie o servico squid e configure o browser do host com o ip do         |")
    print("|servidor e e prta correspondente.                                                    |")
    print("+-------------------------------------------------------------------------------------+")
    print("|                          Precione [ E N T E R ] para continuar                      |")
    print("+-------------------------------------------------------------------------------------+")
    print("|                                       - CMEasy -                                    |")
    print("+-------------------------------------------------------------------------------------+")
def squid_menu_cof3 ():
    print("+-------------------------------------------------------------------------------------+")
    print("|                                SQUID - Conf - Sintaxe                               |")
    print("+-------------------------------------------------------------------------------------+")
    print("|1. Definir ACLs (Critérios usados para decidir quem ou o quê pode aceder ao proxy.). |")
    print("|2. Regras específicas.                                                               |")
    print("|3. Regra final (catch-all 'seguranca').                                              |")
    print("+-------------------------------------------------------------------------------------+")
    print("|                          Precione [ E N T E R ] para continuar                      |")
    print("+-------------------------------------------------------------------------------------+")
    print("|                                       - CMEasy -                                    |")
    print("+-------------------------------------------------------------------------------------+")
def squid_logs ():    
    while True:
        subprocess.run(["clear"])
        print("+-------------------------------------------------------------------------------------+")
        print("|                                     SQUID Logs                                      |")
        print("+-------------------------------------------------------------------------------------+")
        print("|   1.   | Monitorizar o trafego proxy.                                               |")
        print("+--------+----------------------------------------------------------------------------+")
        print("|   2.   | Monitorizar a cache.                                                       |")
        print("+--------+----------------------------------------------------------------------------+")
        print("|   3.   | Sair.                                                                      |")
        print("+-------------------------------------------------------------------------------------+")
        print("|                                       - CMEasy -                                    |")
        print("+-------------------------------------------------------------------------------------+")
        escolha = input ("Escolha uma das opções acima: ")
        # Se o utilizador nao ditar nada 
        if escolha == "":
                entrada_invalida1 ()
                continue
        # Se o utilizador digitar alguma coisa diferente 
        else:  
            try:
                opcao = int(escolha)
                match opcao:
                    case 1:
                        subprocess.run(["clear"])
                        print ("|------------- Registro de acesso ao exterior ----------------|")
                        subprocess.run(["sudo", "tail", "-f", "/var/log/squid/access.log"])
                        continue
                    case 2:
                        subprocess.run(["clear"])
                        print ("|------------- Registro de acesso ----------------|")
                        subprocess.run(["sudo", "tail", "-f", "/var/log/squid/cache.log"])
                        continue
                    case 3:
                        break   
                    case _:
                        entrada_invalida3 ()
                        continue  
            except ValueError:
                # Se a conversão falhar (não for um número), exibe uma mensagem de erro
                entrada_invalida2 ()
                continue              
def suricata_config ():
    while True:
        # Limpar a tela antes de iniciar o porgrama
        os.system("cls" if os.name == "nt" else "clear")
        # Painel Principal (Menu Principal)
        suricata_menu_config ()
        escolha = input ("Escolha uma das opções acima: ")
        # Se o utilizador nao ditar nada 
        if escolha == "":
                entrada_invalida1 ()
                continue
        # Se o utilizador digitar alguma coisa diferente 
        else:  
            try:
                opcao = int(escolha)
                match opcao:
                    case 1:
                        os.system("cls" if os.name == "nt" else "clear")
                        suricata_menu_config_geral ()
                        subprocess.run(["sudo", "nano", "/etc/suricata/suricata.yaml"])
                        continue
                    case 2:
                        subprocess.run(["ls", "/etc/suricata/rules/"])
                        input ("Clique enter para continuar... ")
                        continue
                    case 3:
                        subprocess.run(["sudo", "suricata", "-T", "-c", "/etc/suricata/suricata.yaml"])
                        input ("Clique enter para continuar... ")
                        continue
                    case 4:
                        break   
                    case _:
                        entrada_invalida3 ()
                        continue  
            except ValueError:
                # Se a conversão falhar (não for um número), exibe uma mensagem de erro
                entrada_invalida2 ()
                continue                
# Programa suricata
def suricata ():
    while True:
        # Limpar a tela antes de iniciar o porgrama
        os.system("cls" if os.name == "nt" else "clear")
        # Painel Principal (Menu Principal)
        suricata_menu_principal ()
        escolha = input ("Escolha uma das opções acima: ")
        # Se o utilizador nao ditar nada 
        if escolha == "":
                entrada_invalida1 ()
                continue
        # Se o utilizador digitar alguma coisa diferente 
        else:  
            try:
                opcao = int(escolha)
                match opcao:
                    case 1:
                        suricata_instalacao ()
                        continue
                    case 2:
                        suricata_desinstalar ()
                        continue
                    case 3:
                        comandos_suricata ()
                        continue
                    case 4:
                        suricata_config ()
                        continue
                    case 5:
                        subprocess.run(["clear"])
                        print ("|------------- Registro de acesso ao exterior ----------------|")
                        subprocess.run(["sudo", "tail", "-f", "/var/log/suricata/eve.json"])
                        continue
                    case 6:
                        break   
                    case _:
                        entrada_invalida3 ()
                        continue  
            except ValueError:
                # Se a conversão falhar (não for um número), exibe uma mensagem de erro
                entrada_invalida2 ()
                continue 
#-----------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------
#---> Wiregroup VPN <---
# Menus
def wireguardvpn_menu_principal ():
    print("+-----------------------------------------------------------------------------+")
    print("|                                VPN WIREGUARD                                |")
    print("+-----------------------------------------------------------------------------+")
    print("| Oque é ? | É um protocolo de VPN de código aberto, moderno e extremamente   |")
    print("|          |rápido, focado em alta segurança e desempenho.                    |")
    print("+----------+------------------------------------------------------------------+")
    print("|          | - Criptografia Segura.                                           |")
    print("|          | - Conexão Simples e Leve.                                        |")
    print("| Funções  | - Roteamento de Rede.                                            |")
    print("|          | - Baixa Latência e Alto Desempenho.                              |")
    print("|          | - Roaming.                                                       |")
    print("+----------+------------------------------------------------------------------+")
    print("| Site ofi-| Link: https://www.wireguard.com/                                 |")
    print("|----------+------------------------------------------------------------------|")
    print("|  Testes  | Ubunto (22), Debian, Kali Linux                                  |")
    print("|-----------------------------------------------------------------------------+")
    print("|          1. Instalar no servidor      |      2. Instalar no Cliente         |")
    print("+---------------------------------------+-------------------------------------+")
    print("|             4. Comandos               |           5. Condigurações          |")
    print("+---------------------------------------+-------------------------------------+")
    print("|             6. Teste no servidor      |          7. Teste no cliente        |")
    print("+---------------------------------------+-------------------------------------+")
    print("|              8. Desinstalar           |      9. Ver trafego (Servidor)      |")
    print("+-----------------------------------------------------------------------------+")
    print("|                                  10. Voltar                                 |")
    print("+-----------------------------------------------------------------------------+")
    print("|                                  @cmeasy                                    |")
    print("+-----------------------------------------------------------------------------+")
def wireguardvpn_config_server ():
    print("+-----------------------------------------------------------------------------+")
    print("|                   Cópie, cole e altere como bem entender                    |")
    print("+-----------------------------------------------------------------------------+")
    print("[Interface]")
    print("# Endereço IP do servidor na rede VPN (sub-rede interna)")
    print("Address = 10.10.0.1/24")
    print("# Chave privada do servidor (NUNCA partilhar)")
    print("PrivateKey = <SUA_CHAVE_PRIVADA_AQUI>")
    print("# Porta UDP onde o WireGuard vai escutar")
    print("ListenPort = 51820")
    print("\n# ================================")
    print("# CONFIGURAÇÃO DE ENCAMINHAMENTO")
    print("# ================================")
    print("# ATIVAR encaminhamento de pacotes IPv4 (necessário para acesso à internet via VPN)")
    print("PostUp = sysctl -w net.ipv4.ip_forward=1")
    print("# NAT: permite que os clientes da VPN acedam à internet através da interface do servidor")
    print("# IMPORTANTE: substituir 'enp0s3' pela interface de rede correta do servidor")
    print("PostUp = iptables -t nat -A POSTROUTING -s 10.10.0.0/24 -o enp0s3 -j MASQUERADE")
    print("# Permitir tráfego da VPN (wg0) para a interface externa")
    print("PostUp = iptables -A FORWARD -i wg0 -o enp0s3 -j ACCEPT")
    print("# Permitir tráfego de retorno (estado ESTABLISHED, RELATED)")
    print("PostUp = iptables -A FORWARD -i enp0s3 -o wg0 -m state --state ESTABLISHED,RELATED -j ACCEPT")
    print("\n# ================================")
    print("# LIMPEZA DAS REGRAS (AO DESLIGAR)")
    print("# ================================")
    print("# Remove as regras criadas acima para evitar duplicação")
    print("PostDown = iptables -t nat -D POSTROUTING -s 10.10.0.0/24 -o enp0s3 -j MASQUERADE")
    print("PostDown = iptables -D FORWARD -i wg0 -o enp0s3 -j ACCEPT")
    print("PostDown = iptables -D FORWARD -i enp0s3 -o wg0 -m state --state ESTABLISHED,RELATED -j ACCEPT")
    print("\n# ================================")
    print("# CONFIGURAÇÃO DO CLIENTE")
    print("# ================================")
    print("[Peer]")
    print("# Chave pública do cliente")
    print("PublicKey = <CHAVE_PUBLICA_CLIENTE>")
    print("# IP atribuído ao cliente dentro da VPN (apenas este IP é permitido)")
    print("AllowedIPs = 10.10.0.2/32")
    print("+-----------------------------------------------------------------------------+")
    print("|                                  @cmeasy                                    |")
    print("+-----------------------------------------------------------------------------+")
def wireguardvpn_config_client ():
    print("+-----------------------------------------------------------------------------+")
    print("|                   Cópie, cole e altere como bem entender                    |")
    print("+-----------------------------------------------------------------------------+")
    print("[Interface]")
    print("# ================================")
    print("# CONFIGURAÇÃO DO CLIENTE")
    print("# ================================")
    print("# Endereço IP do cliente dentro da VPN")
    print("# Este IP deve ser único na sub-rede da VPN (não repetir)")
    print("# Ex.: servidor é 10.10.0.1/24, clientes podem ser 10.10.0.2/24, 10.10.0.3/24, etc.")
    print("Address = 10.10.0.2/24")
    print("# Chave privada do cliente")
    print("# MANTER SECRETA, nunca partilhar")
    print("PrivateKey = Chave privada do cliente")
    print("DNS = 1.1.1.1")
    print("\n[Peer]")
    print("# ================================")
    print("# CONFIGURAÇÃO DO SERVIDOR")
    print("# ================================")
    print("# Chave pública do servidor")
    print("# Vem do arquivo server_public.key")
    print("PublicKey = Chave pública do servidor")
    print("# Endereço público ou IP do servidor e porta WireGuard")
    print("# Substituir pelo IP ou domínio real do servidor")
    print("# Certificar que a porta UDP (51820) está aberta no firewall/router")
    print("Endpoint = 192.168.5.199:51820")
    print("# Define quais IPs o cliente pode acessar através da VPN")
    print("# 0.0.0.0/0 → todo o tráfego IPv4 passa pela VPN")
    print("# ::/0 → todo o tráfego IPv6 passa pela VPN")
    print("# Isso faz da VPN “full tunnel”, roteando toda a internet do cliente pelo servidor")
    print("AllowedIPs = 0.0.0.0/0, ::/0")
    print("# Mantém o túnel ativo mesmo sem tráfego")
    print("# Necessário para clientes atrás de NAT/firewall")
    print("PersistentKeepalive = 25")
    print("+-----------------------------------------------------------------------------+")
    print("|                                  @cmeasy                                    |")
    print("+-----------------------------------------------------------------------------+")
def wireguardvpn_comandos_menu ():
    print("+-----------------------------------------------------------------------------+")
    print("|                              C O M A N D O S                                |")
    print("+-----------------------------------------------------------------------------+")
    print("| 1. | Iniciar o serviço.                                                     |")
    print("+----+------------------------------------------------------------------------+")
    print("| 2. | Ativar o Serviço.                                                      |")
    print("+----+------------------------------------------------------------------------+")
    print("| 3. | Estado do serviço.                                                     |")
    print("+----+------------------------------------------------------------------------+")
    print("| 4. | Parar o serviço.                                                       |")
    print("+----+------------------------------------------------------------------------+")
    print("| 5. | Reiniciar o serviço.                                                   |")
    print("+----+------------------------------------------------------------------------+")
    print("| 6. | Versão do serviço.                                                     |")
    print("+----+------------------------------------------------------------------------+")
    print("| 7. | Voltar.                                                                |")
    print("+-----------------------------------------------------------------------------+")
    print("|                                - CMEasy -                                   |")
    print("+-----------------------------------------------------------------------------+")
def wireguardvpn_config_menu ():
    print("+-----------------------------------------------------------------------------+")
    print("|                          ARQUIVOS DE CONFIGURAÇÃO                           |")
    print("+-----------------------------------------------------------------------------+")
    print("| 1. | Arquivo principal.                                                     |")
    print("+----+------------------------------------------------------------------------+")
    print("| 2. | Configurar parâmetros do kernel.                                       |")
    print("+----+------------------------------------------------------------------------+")
    print("| 3. | Voltar.                                                                |")
    print("+-----------------------------------------------------------------------------+")
    print("|                                - CMEasy -                                   |")
    print("+-----------------------------------------------------------------------------+")
# Comandos
def start_wireguardvpn ():
    try:
        subprocess.run(["sudo", "wg-quick", "up", "wg0"], check=True)   
    except subprocess.CalledProcessError as e:
        print(f"[ERRO] Ocorreu um erro ao executar o comando: {e}")
    enter_clear()
def enable_wireguardvpn ():
    try:
        subprocess.run(["sudo", "systemctl", "enable", "wg-quick@wg0"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"[ERRO] Ocorreu um erro ao executar o comando: {e}")
    enter_clear()
def stop_wireguardvpn ():
    try:
        subprocess.run(["sudo", "sudo", "wg-quick", "down", "wg0"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"[ERRO] Ocorreu um erro ao executar o comando: {e}")
    enter_clear()
def restart_wireguardvpn ():
    try:
        subprocess.run(["sudo", "wg-quick", "down", "wg0"], check=True)
        subprocess.run(["sudo", "wg-quick", "up", "wg0"], check=True)   
    except subprocess.CalledProcessError as e:
        print(f"[ERRO] Ocorreu um erro ao executar o comando: {e}")
    enter_clear()
def version_wireguardvpn ():
    try:
        subprocess.run(["wg", "--version"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"[ERRO] Ocorreu um erro ao executar o comando: {e}")
    enter_clear()
# instalação
def instalacao_wireguardvpn_server():
    result = subprocess.run(["dpkg", "-l", "wireguard"], capture_output=True, text=True)
    if result.returncode == 0 and "wireguard" in result.stdout:
        print("|---------------------------- WireGuard já está instalado ----------------------------|")
    else:
        try:
            print("|---------------------------- Atualizando os pacotes  ------------------------------|")
            subprocess.run(["sudo", "apt", "update"], check=True)
            subprocess.run(["sudo", "apt", "install", "curl"], check=True)
            subprocess.run(["sudo", "apt", "install", "iptables-persistent"], check=True)
            subprocess.run(["sudo", "dpkg", "--configure", "-a"], check=True)
            subprocess.run(["sudo", "netfilter-persistent", "save"], check=True)
            subprocess.run(["sudo", "apt-get", "install", "-y", "ufw"], check=True)
            print("|------------------------ Pacotes atualizados com sucesso --------------------------|")
            
            print("|---------------------------- Instalando wireGuard ----------------------------|")
            subprocess.run(["sudo", "apt", "install", "-y", "wireguard"], check=True)      
            subprocess.run(["wg", "--version"], check=True)
            print("|---------------------------- Wireguard Instalado com sucesso ----------------------------|") 
            
            print("|---------------------------- Confifurando a firewall ----------------------------|")
            subprocess.run(["sudo", "ufw", "allow", "51820/udp"], check=True)      
            subprocess.run(["sudo", "ufw", "enable"], check=True)
            print("|---------------------------- Firewall configurado ----------------------------|") 

            print("|---------------------------- Gerando chaves para o servidor ---------------------------|")
            # Gerar chave privada
            print("|---------------------------- Gerando chave privada do servidor ---------------------------|")
            priv = subprocess.run(
                ["wg", "genkey"],
                capture_output=True,
                text=True,
                check=True
            )
            chave_privada = priv.stdout.strip()
            with open("server_private.key", "w") as f:
                f.write(chave_privada)
            print(f"Chave Privada: {chave_privada}")
            # Gerar chave pública
            print("|---------------------------- Gerando chave publica do servidor ---------------------------|")
            pub = subprocess.run(
                ["wg", "pubkey"],
                input=chave_privada,
                capture_output=True,
                text=True,
                check=True
            )
            chave_publica = pub.stdout.strip()
            with open("server_public.key", "w") as f:
                f.write(chave_publica)
            print(f"Chave Pública: {chave_publica}")
            print("|---------------------------- Chaves geradas com sucesso ---------------------------|")  
            
            print("|---------------------------- Preparando o arquivo de configuração ---------------------------|") 
            wireguardvpn_config_server ()
            input ("Clique enter para continuar...")          
            subprocess.run(["sudo", "nano", "/etc/wireguard/wg0.conf"], check=True) 
            subprocess.run(["sudo", "sysctl", "-w", "net.ipv4.ip_forward=1"], check=True)
            subprocess.run(["sudo", "sysctl", "-p"], check=True)
            
            
            print("|---------------------------- Iniciando o serviço ---------------------------|") 
            subprocess.run(["sudo", "wg-quick", "up", "wg0"], check=True)
            subprocess.run(["sudo", "systemctl", "enable", "wg-quick@wg0"], check=True)
            print("|---------------------------- Serviço iniciado com sucesso---------------------------|") 
            

        except subprocess.CalledProcessError as e:
            print(f"Ocorreu um erro ao executar o comando: {e}")
    enter_clear ()
def instalacao_wireguardvpn_cliente():
    result = subprocess.run(["dpkg", "-l", "wireguard"], capture_output=True, text=True)
    if result.returncode == 0 and "wireguard" in result.stdout:
        print("|---------------------------- WireGuard já está instalado ----------------------------|")
    else:
        try:
            print("|---------------------------- Atualizando os pacotes  ------------------------------|")
            subprocess.run(["sudo", "apt", "update"], check=True)
            subprocess.run(["sudo", "dpkg", "--configure", "-a"], check=True)
            subprocess.run(["sudo", "apt", "install", "resolvconf"], check=True)
            subprocess.run(["sudo", "apt", "install", "curl"], check=True)
            print("|------------------------ Pacotes atualizados com sucesso --------------------------|")
            
            print("|---------------------------- Instalando wireGuard ----------------------------|")
            subprocess.run(["sudo", "apt", "install", "-y", "wireguard"], check=True)      
            subprocess.run(["wg", "--version"], check=True)
            print("|---------------------------- Wireguard Instalado com sucesso ----------------------------|")
            
            print("|---------------------------- Gerando chaves para o Cliente ---------------------------|")
            # Gerar chave privada
            print("|---------------------------- Gerando chave privada do servidor ---------------------------|")
            priv = subprocess.run(
                ["wg", "genkey"],
                capture_output=True,
                text=True,
                check=True
            )
            chave_privada = priv.stdout.strip()
            with open("client_private.key", "w") as f:
                f.write(chave_privada)
            print(f"Chave Privada: {chave_privada}")
            # Gerar chave pública
            print("|---------------------------- Gerando chave publica do servidor ---------------------------|")
            pub = subprocess.run(
                ["wg", "pubkey"],
                input=chave_privada,
                capture_output=True,
                text=True,
                check=True
            )
            chave_publica = pub.stdout.strip()
            with open("client_public.key", "w") as f:
                f.write(chave_publica)
            print(f"Chave Pública: {chave_publica}")
            print("|---------------------------- Chaves geradas com sucesso ---------------------------|") 
            
            print("|---------------------------- Preparando o arquivo de configuração ---------------------------|") 
            wireguardvpn_config_client ()
            input ("Clique enter para continuar...")          
            subprocess.run(["sudo", "nano", "/etc/wireguard/wg0.conf"], check=True) 
            
            
            
            print("|---------------------------- Iniciando o serviço ---------------------------|") 
            subprocess.run(["sudo", "wg-quick", "up", "wg0"], check=True)
            subprocess.run(["sudo", "systemctl", "enable", "wg-quick@wg0"], check=True)             
                        

        except subprocess.CalledProcessError as e:
            print(f"Ocorreu um erro ao executar o comando: {e}")
    enter_clear ()
def desintslacao_wireguardvpn ():
    try:
        print("|---------------------------- Desinstalamndo o WiregroupVpn  ------------------------------|")
        subprocess.run(["sudo", "apt", "remove", "wireguard"], check=True)
        subprocess.run(["sudo", "apt", "purge", "wireguard"], check=True)
        subprocess.run(["sudo", "apt", "update"], check=True)
        subprocess.run(["sudo", "apt", "purge", "wireguard"], check=True)
        print("|------------------------ Desinstalação bem sucedida --------------------------|")
    except subprocess.CalledProcessError as e:
        print(f"Ocorreu um erro ao executar o comando: {e}")
    enter_clear ()
# programas
def wireguardvpn_test_server ():
    try:
        print("|-------------------- Testando a conexão WireGuard --------------------|")
        print("Verificando se há troca de pacotes entre o peer do cliente e o servidor...")
        # Mostra o status atual do WireGuard
        subprocess.run(["sudo", "wg"], check=True)
        print("\nVerifique se o servidor tem conexão com o cliente.")
        # Solicita o IP do cliente
        ip = input("Indique o IP do Cliente: ")
        print(f"Testando conectividade com {ip}...")
        # Executa o ping para testar a conectividade
        subprocess.run(["ping", "-c", "4", ip], check=True)  # '-c 4' envia 4 pacotes
        print("\n|------------------------ Teste finalizado ------------------------|")
        print("Conexão estabelecida com sucesso!")
        subprocess.run(["sudo", "ufw", "status", "verbose"], check=True)      
        print("Verifique se há o controlo da porta 51820/udp...")
    except subprocess.CalledProcessError as e:
        print(f"\nOcorreu um erro ao executar o comando: {e}")
        print("Verifique se o WireGuard está ativo, se o IP está correto ou se há firewall bloqueando a conexão.")
    enter_clear ()
def wireguardvpn_test_client (): 
    try:
        print("|-------------------- Testando a conexão WireGuard (Cliente) --------------------|")
        print("Verificando se há troca de pacotes entre o cliente e o servidor...")
        # Mostra o status atual do WireGuard
        subprocess.run(["sudo", "wg"], check=True)
        print("\nVerifique se o cliente consegue se comunicar com o servidor.")
        # Solicita o IP do servidor
        server_ip = input("Indique o IP do Servidor: ")
        print(f"Testando conectividade com o servidor {server_ip}...")
        # Ping para verificar conectividade
        subprocess.run(["ping", "-c", "4", server_ip], check=True)
        print("\nVerificando o IP público da conexão...")
        # Curl para verificar IP público
        subprocess.run(["curl", "ifconfig.me"], check=True)
        print("\n|------------------------ Teste finalizado ------------------------|")
        print("Conexão do cliente com sucesso!")
        print("Podes ainda realizar testes com o comando traceroute...")
    except subprocess.CalledProcessError as e:
        print(f"\nOcorreu um erro ao executar o comando: {e}")
        print("Verifique se o WireGuard está ativo, se o IP do servidor está correto ou se há firewall bloqueando a conexão.")
    enter_clear ()
def wireguardvpn_config ():
    while True:
            os.system("cls" if os.name == "nt" else "clear")
            wireguardvpn_config_menu ()
            escolha = input ("Escolha uma das opções acima: ")
            if escolha == "":
                entrada_invalida1 ()
                continue
            else:
                try:
                    opcao = int (escolha)
                    match opcao: 
                        case 1:
                            try:
                                os.system("cls" if os.name == "nt" else "clear")
                                wireguardvpn_config_server ()
                                input ("Clique enter ara continuar... ")
                                subprocess.run(["sudo", "nano", "/etc/wireguard/wg0.conf"], check=True) 
                            except subprocess.CalledProcessError as e:
                                print(f"[ERRO] Ocorreu um erro ao executar o comando: {e}")
                            continue
                        case 2:
                            try:
                                os.system("cls" if os.name == "nt" else "clear")
                                wireguardvpn_config_client ()
                                input ("Clique enter ara continuar... ")
                                subprocess.run(["sudo", "nano", "/etc/sysctl.conf"], check=True) 
                                subprocess.run(["sudo", "sysctl", "-p"], check=True)
                            except subprocess.CalledProcessError as e:
                                print(f"[ERRO] Ocorreu um erro ao executar o comando: {e}")
                            continue
                        case 3:
                            break
                        case _:
                            entrada_invalida3 ()
                            continue
                except ValueError:
                    entrada_invalida2 ()
                    continue
def wireguardvpn_comandos ():
    while True:
            os.system("cls" if os.name == "nt" else "clear")
            wireguardvpn_comandos_menu ()
            escolha = input ("Escolha uma das opções acima: ")
            if escolha == "":
                entrada_invalida1 ()
                continue
            else:
                try:
                    opcao = int (escolha)
                    match opcao: 
                        case 1:
                            start_wireguardvpn ()
                            continue
                        case 2:
                            enable_wireguardvpn ()
                            continue
                        case 3:
                            print ("Indisponivel no momento...")
                            enter_clear ()
                            continue
                        case 4:
                            stop_wireguardvpn ()
                            continue
                        case 5:
                            restart_wireguardvpn ()
                            continue
                        case 6:
                            version_wireguardvpn ()
                            continue
                        case 7:
                            break
                        case _:
                            entrada_invalida3 ()
                            continue
                except ValueError:
                    entrada_invalida2 ()
                    continue
def wireguardvpn ():
    while True:
            os.system("cls" if os.name == "nt" else "clear")
            wireguardvpn_menu_principal ()
            escolha = input ("Escolha uma das opções acima: ")
            if escolha == "":
                entrada_invalida1 ()
                continue
            else:
                try:
                    opcao = int (escolha)
                    match opcao: 
                        case 1:
                            instalacao_wireguardvpn_server ()
                            continue
                        case 2:
                            instalacao_wireguardvpn_cliente ()
                            continue
                        case 3:
                            wireguardvpn_config ()
                            continue
                        case 4:
                            wireguardvpn_comandos ()
                            continue
                        case 5:
                            wireguardvpn_config ()
                            continue
                        case 6:
                            wireguardvpn_test_server ()
                            continue
                        case 7:
                            wireguardvpn_test_client ()
                            continue
                        case 8:
                            desintslacao_wireguardvpn ()
                            continue
                        case 9:
                            try:
                                subprocess.run(["tcpdump", "-i", "wg0"], check=True)
                            except subprocess.CalledProcessError as e:
                                print(f"[ERRO] Ocorreu um erro ao executar o comando: {e}")
                            continue
                        case 10:
                            break
                        case _:
                            entrada_invalida3 ()
                            continue
                except ValueError:
                    entrada_invalida2 ()
                    continue
#-----------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------
#---> OpenVPN <---
# Menus
def Openvpn_menu_principal ():
    print("+-----------------------------------------------------------------------------+")
    print("|                                    OPEN VPN                                 |")
    print("+-----------------------------------------------------------------------------+")
    print("| Oque é ? | OpenVPN é um protocolo e software de VPN que cria uma ligação    |")
    print("|          |segura e encriptada pela internet, permitindo aceder a redes      |")
    print("|          |de forma protegida e anónima.                                     |")
    print("+----------+------------------------------------------------------------------+")
    print("|          | - Encriptar a ligação.                                           |")
    print("|          | - Criar túneis seguros (VPN).                                    |")
    print("| Funções  | - Ocultar o IP.                                                  |")
    print("|          | - Aceder a redes remotas.                                        |")
    print("|          | - Proteger em redes públicas.                                    |")
    print("+----------+------------------------------------------------------------------+")
    print("| Site ofi-| Link: https://openvpn.net/                                       |")
    print("|----------+------------------------------------------------------------------|")
    print("|  Testes  |                                                                  |")
    print("|-----------------------------------------------------------------------------+")
    print("|        1. Instalar no servidor        |       2. Instalar no cliente        |")
    print("+---------------------------------------+-------------------------------------+")
    print("|                4. Comandos            |           5. Condigurações          |")
    print("+---------------------------------------+-------------------------------------+")
    print("|                4. Comandos            |           5. Condigurações          |")
    print("+-----------------------------------------------------------------------------+")
    print("|                                  10. Voltar                                 |")
    print("+-----------------------------------------------------------------------------+")
    print("|                                  @cmeasy                                    |")
    print("+-----------------------------------------------------------------------------+")
def openvpn_config_server ():
    print("+-----------------------------------------------------------------------------+")
    print("|               Cópie, cole ou altere a de definição já existente             |")
    print("+-----------------------------------------------------------------------------+")
    print("port 1194")
    print("proto udp")
    print("dev tun")
    print("# Certificados e chaves, isto define os ficheiros de segurança.")
    print("ca ca.crt")
    print("cert server.crt")
    print("key server.key")
    print("dh dh.pem")
    print("#Rede VPN, define o ip rede interna da VPN e a mascara.")
    print("server 10.8.0.0 255.255.255.0")
    print("# Redirecionamento de tráfego: faz o cliente enviar TODO o tráfego pela VPN.")
    print('push "redirect-gateway def1 bypass-dhcp"')
    print("# Define o DNS que o cliente vai usar.")
    print('push "dhcp-option DNS 8.8.8.8"')
    print("# Manter a ligação ativa.")
    print("keepalive 10 120")
    print("# Algoritmo de encriptação da VPN.")
    print("cipher AES-256-CBC")
    print("# Permissões de segurança. OpenVPN deixa de correr como root epassa a utilizador sem privilégios")
    print("user nobody")
    print("group nogroup")
    print("# Evita reinicialização de componentes: mantém chaves carregadas, mantém interface VPN ativa.")
    print("persist-key")
    print("persist-tun")
    print("# Logs")
    print("status openvpn-status.log")
    print("verb 3")
    print("+-----------------------------------------------------------------------------+")
    print("|                                  @cmeasy                                    |")
    print("+-----------------------------------------------------------------------------+")
def openvpn_config_client ():
    print("+-----------------------------------------------------------------------------+")
    print("|               Cópie, cole ou altere a de definição já existente             |")
    print("+-----------------------------------------------------------------------------+")
    print("port 1194")
    print("proto udp")
    print("dev tun")
    print("# Certificados e chaves, isto define os ficheiros de segurança.")
    print("ca ca.crt")
    print("cert server.crt")
    print("key server.key")
    print("dh dh.pem")
    print("#Rede VPN, define o ip rede interna da VPN e a mascara.")
    print("server 10.8.0.0 255.255.255.0")
    print("# Redirecionamento de tráfego: faz o cliente enviar TODO o tráfego pela VPN.")
    print('push "redirect-gateway def1 bypass-dhcp"')
    print("# Define o DNS que o cliente vai usar.")
    print('push "dhcp-option DNS 8.8.8.8"')
    print("# Manter a ligação ativa.")
    print("keepalive 10 120")
    print("# Algoritmo de encriptação da VPN.")
    print("cipher AES-256-CBC")
    print("# Permissões de segurança. OpenVPN deixa de correr como root epassa a utilizador sem privilégios")
    print("user nobody")
    print("group nogroup")
    print("# Evita reinicialização de componentes: mantém chaves carregadas, mantém interface VPN ativa.")
    print("persist-key")
    print("persist-tun")
    print("# Logs")
    print("status openvpn-status.log")
    print("verb 3")
    print("+-----------------------------------------------------------------------------+")
    print("|                                  @cmeasy                                    |")
    print("+-----------------------------------------------------------------------------+")
def wireguardvpn_config_client ():
    print("+-----------------------------------------------------------------------------+")
    print("|                   Cópie, cole e altere como bem entender                    |")
    print("+-----------------------------------------------------------------------------+")
    print("[Interface]")
    print("# ================================")
    print("# CONFIGURAÇÃO DO CLIENTE")
    print("# ================================")
    print("# Endereço IP do cliente dentro da VPN")
    print("# Este IP deve ser único na sub-rede da VPN (não repetir)")
    print("# Ex.: servidor é 10.10.0.1/24, clientes podem ser 10.10.0.2/24, 10.10.0.3/24, etc.")
    print("Address = 10.10.0.2/24")
    print("# Chave privada do cliente")
    print("# MANTER SECRETA, nunca partilhar")
    print("PrivateKey = Chave privada do cliente")
    print("DNS = 1.1.1.1")
    print("\n[Peer]")
    print("# ================================")
    print("# CONFIGURAÇÃO DO SERVIDOR")
    print("# ================================")
    print("# Chave pública do servidor")
    print("# Vem do arquivo server_public.key")
    print("PublicKey = Chave pública do servidor")
    print("# Endereço público ou IP do servidor e porta WireGuard")
    print("# Substituir pelo IP ou domínio real do servidor")
    print("# Certificar que a porta UDP (51820) está aberta no firewall/router")
    print("Endpoint = 192.168.5.199:51820")
    print("# Define quais IPs o cliente pode acessar através da VPN")
    print("# 0.0.0.0/0 → todo o tráfego IPv4 passa pela VPN")
    print("# ::/0 → todo o tráfego IPv6 passa pela VPN")
    print("# Isso faz da VPN “full tunnel”, roteando toda a internet do cliente pelo servidor")
    print("AllowedIPs = 0.0.0.0/0, ::/0")
    print("# Mantém o túnel ativo mesmo sem tráfego")
    print("# Necessário para clientes atrás de NAT/firewall")
    print("PersistentKeepalive = 25")
    print("+-----------------------------------------------------------------------------+")
    print("|                                  @cmeasy                                    |")
    print("+-----------------------------------------------------------------------------+")

# Comandos
def start_openvpn ():
    try:
        subprocess.run(["sudo", "systemctl", "start", "openvpn"], check=True)   
    except subprocess.CalledProcessError as e:
        print(f"[ERRO] Ocorreu um erro ao executar o comando: {e}")
    enter_clear()
def enable_openvpn ():
    try:
        subprocess.run(["sudo", "systemctl", "enable", "openvpn"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"[ERRO] Ocorreu um erro ao executar o comando: {e}")
    enter_clear()
def stop_openvpn ():
    try:
        subprocess.run(["sudo", "systemctl", "stop", "openvpn"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"[ERRO] Ocorreu um erro ao executar o comando: {e}")
    enter_clear()
def restart_openvpn ():
    try:
        subprocess.run(["sudo", "systemctl", "status", "openvpn"], check=True)   
    except subprocess.CalledProcessError as e:
        print(f"[ERRO] Ocorreu um erro ao executar o comando: {e}")
    enter_clear()
def status_openvpn ():
    try:
        subprocess.run(["sudo", "systemctl", "restart", "openvpn"], check=True)   
    except subprocess.CalledProcessError as e:
        print(f"[ERRO] Ocorreu um erro ao executar o comando: {e}")
    enter_clear()
def version_openvpn ():
    try:
        subprocess.run(["openvpn", "--version"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"[ERRO] Ocorreu um erro ao executar o comando: {e}")
    enter_clear()
# instalação
def instalacao_openvpn_server():
    result = subprocess.run(["dpkg", "-l", "openvpn"], capture_output=True, text=True)
    if result.returncode == 0 and "ii" in result.stdout:
        print("|---------------------------- OpenVpn já está instalado ----------------------------|")
    else:
        try:
            print("|---------------------------- Atualizando os pacotes  ------------------------------|")
            subprocess.run(["sudo", "apt", "update"], check=True)
            print("|------------------------ Pacotes atualizados com sucesso --------------------------|")
            print("|---------------------------- Instalando OpenVpn ----------------------------|")
            subprocess.run(["sudo", "apt", "install", "openvpn", "easy-rsa", "-y"], check=True)      
            subprocess.run(["openvpn", "--version"], check=True)
            print("|---------------------------- OpenVpn Instalado com sucesso ----------------------------|") 
            print("|---------------------------- Criando infraestrutura de chaves PKI (Public Key Infrastructure) ----------------------------|")
            path = os.path.expanduser("~/openvpn-ca")
            subprocess.run(["make-cadir", path], check=True)    
            subprocess.run(["./easyrsa", "init-pki"], check=True, cwd=os.path.expanduser("~/openvpn-ca"))
            print("|---------------------------- Inicializando o PKI ----------------------------|")
            subprocess.run(["./easyrsa", "init-pki"], check=True)
            print("|---------------------------- Criaando a Autoridade Certificadora (CA) ----------------------------|")
            print("|--------------------------------------------------------")
            print("|--- A CA (Certificate Authority) é o “chefe” de tudo...")
            print("|--- Vais definir uma password para CA (Enter New CA Key Passphrase: ) e dar um nome...")
            print("|--------------------------------------------------------")
            subprocess.run(["./easyrsa", "build-ca"], check=True)
            print("|---------------------------- Criando o certificado do servidor ----------------------------|")
            print("|---------------------------- Gerando pedido de certificado (chave privada do servidor, pedido de certificado) ----------------------------|")
            subprocess.run(["./easyrsa", "gen-req", "server"], check=True)
            print("|---------------------------- Assinando o certificado ----------------------------|")            
            subprocess.run(["./easyrsa", "sign-req", "server", "server"], check=True)
            print("|---------------------------- Gerando parâmetros para troca segura de chaves ----------------------------|")            
            subprocess.run(["./easyrsa", "gen-dh"], check=True)
            print("|---------------------------- Configurar o servidor OpenVPN ----------------------------|")   
            subprocess.run(["sudo", "cp", "pki/ca.crt", "pki/private/server.key", "pki/issued/server.crt", "pki/dh.pem", "/etc/openvpn/"], check=True)
            openvpn_config_server ()
            input ("Clique enter para continuar...")
            subprocess.run(["sudo", "nano", "/etc/openvpn/server.conf"], check=True)
            print("|---------------------------- Configurando a firewall ----------------------------|")  
            subprocess.run(["sudo", "ufw", "allow", "1194/udp"], check=True)
            subprocess.run(["sudo", "ufw", "enable"], check=True)
            print("|---------------------------- Ativando o encaminhamento de IP ----------------------------|")  
            print ("Descomenta: net.ipv4.ip_forward=1")
            input ("Clique enter para continuar...")  
            subprocess.run(["sudo", "nano", "/etc/sysctl.conf"], check=True)
            subprocess.run(["sudo", "sysctl", "-p"], check=True)
            print("|---------------------------- Configurando NAT (iptables) ---------------------------|")   
            subprocess.run(["ip", "a"], check=True)
            ip = input ("Indique o ip da sua rede com am sub mascara (ex: 192.168.1.2/24): ")
            int_rede = input ("Indique a sua interface de rede (ex: eth0): ")
            subprocess.run(["sudo", "iptables", "-t", "nat", "-A", "POSTROUTING", "-s", ip, "-o", int_rede, "-j", "MASQUERADE"], check=True)
            subprocess.run(["sudo", "apt", "install", "iptables-persistent"], check=True)
            print("|---------------------------- Iniciando o serviço ---------------------------|")
            subprocess.run(["sudo", "systemctl", "start", "openvpn@server"], check=True) 
            subprocess.run(["sudo", "systemctl", "enable", "openvpn@server"], check=True)
            subprocess.run(["sudo", "systemctl", "status", "openvpn@server"], check=True)
            print("|---------------------------- OPENVPN PRONTO A SER UTILIZADO ---------------------------|")
        except subprocess.CalledProcessError as e:
            print(f"Ocorreu um erro ao executar o comando: {e}")
    enter_clear ()
def instalacao_openvpn_cliente_debian():
    result = subprocess.run(["dpkg", "-l", "openvpn"], capture_output=True, text=True)
    if result.returncode == 0 and "ii" in result.stdout:
        print("|---------------------------- OpenVpn já está instalado ----------------------------|")
    else:
        try:
            print("|---------------------------- Atualizando os pacotes  ------------------------------|")
            subprocess.run(["sudo", "apt", "update"], check=True)
            subprocess.run(["sudo", "apt", "-f", "install"], check=True)
            subprocess.run(["sudo", "dpkg", "--configure", "-a"], check=True)
            print("|------------------------ Pacotes atualizados com sucesso --------------------------|")
            print("|---------------------------- Instalando OpenVpn ----------------------------|")
            subprocess.run(["sudo", "apt", "install", "openvpn", "-y"], check=True)      
            subprocess.run(["openvpn", "--version"], check=True)
            print("|---------------------------- OpenVpn Instalado com sucesso ----------------------------|")  
        except subprocess.CalledProcessError as e:
            print(f"Ocorreu um erro ao executar o comando: {e}")
    enter_clear ()
def instalacao_openvpn_cliente_redHat():
    result = subprocess.run(["dpkg", "-l", "openvpn"], capture_output=True, text=True)
    if result.returncode == 0 and "ii" in result.stdout:
        print("|---------------------------- OpenVpn já está instalado ----------------------------|")
    else:
        try:
            print("|---------------------------- Atualizando os pacotes  ------------------------------|")
            subprocess.run(["sudo", "dnf", "update"], check=True)
            print("|------------------------ Pacotes atualizados com sucesso --------------------------|")
            print("|---------------------------- Instalando OpenVpn ----------------------------|")
            subprocess.run(["sudo", "dnf", "install", "openvpn", "-y"], check=True)      
            subprocess.run(["openvpn", "--version"], check=True)
            print("|---------------------------- OpenVpn Instalado com sucesso ----------------------------|")  
        except subprocess.CalledProcessError as e:
            print(f"Ocorreu um erro ao executar o comando: {e}")
    enter_clear ()
def add_cliente_openvpn():
    try:
        print("|---------------------------- Adicinando um cliente ao servidor  ------------------------------|")    
        subprocess.run(["cd", "~/openvpn-ca"], check=True) 
        cliente= input ("Indique o nome do cliente: ")
        subprocess.run(["./easyrsa", "gen-req", cliente, "nopass"], check=True) 
        subprocess.run(["./easyrsa", "sign-req", "client", cliente], check=True) 
        print("|---------------------------- Mostrando os certificados criados para oo cliente  ------------------------------|")
        subprocess.run(["cd", "/root/openvpn-ca"], check=True)
        subprocess.run(["cat", "pki/ca.crt"], check=True)
        subprocess.run(["cat", f"pki/issued/{cliente}.crt"], check=True) 
        subprocess.run(["cat", f"pki/private/{cliente}.key"], check=True) 
        
        print ("##########################################")
        print ("O QUE DEVE SER COLOCADO")
        print ("##########################################")
        print ("-----BEGIN CERTIFICATE----- \n...\n -----END CERTIFICATE-----")
        print ("Parte muito importatente tenha atenção")
        
        subprocess.run(["nano", f"{cliente}.ovpn"], check=True) 

        print("|---------------------------- Ciente criado ---------------------------|")            
        print("|---------------------------- Copie este arquivo para máquina do cliente ---------------------------|")            
                    
    except subprocess.CalledProcessError as e:
        print(f"Ocorreu um erro ao executar o comando: {e}")
    enter_clear ()
def desintslacao_wireguardvpn ():
    try:
        print("|---------------------------- Desinstalamndo o WiregroupVpn  ------------------------------|")
        subprocess.run(["sudo", "apt", "remove", "wireguard"], check=True)
        subprocess.run(["sudo", "apt", "purge", "wireguard"], check=True)
        subprocess.run(["sudo", "apt", "update"], check=True)
        subprocess.run(["sudo", "apt", "purge", "wireguard"], check=True)
        print("|------------------------ Desinstalação bem sucedida --------------------------|")
    except subprocess.CalledProcessError as e:
        print(f"Ocorreu um erro ao executar o comando: {e}")
    enter_clear ()
# programas

def openvpn_comandos ():
    while True:
            os.system("cls" if os.name == "nt" else "clear")
            comandos_menu ()
            escolha = input ("Escolha uma das opções acima: ")
            if escolha == "":
                entrada_invalida1 ()
                continue
            else:
                try:
                    opcao = int (escolha)
                    match opcao: 
                        case 1:
                            start_openvpn ()
                            continue
                        case 2:
                            enable_openvpn ()
                            continue
                        case 3:
                            status_openvpn ()
                            continue
                        case 4:
                            stop_openvpn ()
                            continue
                        case 5:
                            restart_openvpn ()
                            continue
                        case 6:
                            version_openvpn ()
                            continue
                        case 7:
                            break
                        case _:
                            entrada_invalida3 ()
                            continue
                except ValueError:
                    entrada_invalida2 ()
                    continue
def openvpn ():
    while True:
            os.system("cls" if os.name == "nt" else "clear")
            wireguardvpn_menu_principal ()
            escolha = input ("Escolha uma das opções acima: ")
            if escolha == "":
                entrada_invalida1 ()
                continue
            else:
                try:
                    opcao = int (escolha)
                    match opcao: 
                        case 1:
                            instalacao_openvpn_server ()
                            continue
                        case 2:
                            instalacao_wireguardvpn_cliente ()
                            continue
                        case 3:
                            wireguardvpn_config ()
                            continue
                        case 4:
                            wireguardvpn_comandos ()
                            continue
                        case 5:
                            wireguardvpn_config ()
                            continue
                        case 6:
                            wireguardvpn_test_server ()
                            continue
                        case 7:
                            wireguardvpn_test_client ()
                            continue
                        case 8:
                            desintslacao_wireguardvpn ()
                            continue
                        case 10:
                            break
                        case _:
                            entrada_invalida3 ()
                            continue
                except ValueError:
                    entrada_invalida2 ()
                    continue
#-----------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------
def ciberseguranca ():
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        menu_so_ciberseguranca ()
        escolha = input ("Escolha uma das opções acima: ")
        if escolha == "":
            entrada_invalida1 ()
            continue
        else:
            try:
                opcao = int (escolha)
                match opcao: 
                    case 1:
                        fail2ban ()
                        continue
                    case 2:
                        snort ()
                        continue
                    case 3:
                        proxy_squid ()
                        continue
                    case 4:
                        bwapp ()
                        continue
                    case 5 :
                        suricata ()
                        continue
                    case 6:
                        wireguardvpn ()
                        continue
                    case 7:
                        openvpn ()
                        continue
                    # Voltar ao menu anterior
                    case 8:
                        break
                    case _:
                        entrada_invalida3 ()
                        continue
            except ValueError:
                entrada_invalida2 ()
                continue
#-----------------------------------------------------------------------------------
def family_deban ():
    while True: 
        subprocess.run(["clear"])
        menu_tipo_de_programa ()
        escolha = input ("Escolha uma das opções acima: ")
        if escolha == "":
            entrada_invalida1 ()
            continue
        else:
            try:
                opcao = int (escolha)
                match opcao:
                    #-------- Ciberseguranca  
                    case 1:
                        ciberseguranca ()
                        continue
                    #-------- Programacao
                    case 2:
                        print ("Indisponivel no momento...")
                        enter_clear ()
                        continue
                    #-------- Outros Programas
                    case 3:
                        ourtros_programas_debian ()
                        continue                                                               
                    # Voltar ao menu anterior
                    case 4:
                        break
                    case _:
                        entrada_invalida3 ()
                        continue
            except ValueError:
                entrada_invalida2 ()
                continue       
def family_redHat ():
    while True: 
        subprocess.run(["clear"])
        menu_tipo_de_programa ()
        escolha = input ("Escolha uma das opções acima: ")
        if escolha == "":
            entrada_invalida1 ()
            continue
        else:
            try:
                opcao = int (escolha)
                match opcao:
                    #-------- Ciberseguranca  
                    case 1:
                        print ("Indisponivel no momento...")
                        enter_clear ()
                        continue
                    #-------- Programacao
                    case 2:
                        print ("Indisponivel no momento...")
                        enter_clear ()
                        continue
                    #-------- Outros Programas
                    case 3:
                        print ("Indisponivel no momento...")
                        enter_clear ()
                        continue                                                               
                    # Voltar ao menu anterior
                    case 4:
                        break
                    case _:
                        entrada_invalida3 ()
                        continue
            except ValueError:
                entrada_invalida2 ()
                continue   
def tipo_de_programas_linux ():
    while True: 
        os.system("cls" if os.name == "nt" else "clear")
        menu_instalar_programas ()
        escolha = input ("Escolha uma das opções acima: ")
        if escolha == "":
            entrada_invalida1 ()
            continue
        else:
            try:
                opcao = int (escolha)
                match opcao:
                    #-------- Tipos de programas 
                    case 1:
                        family_deban ()
                        continue             
                    case 2:
                        family_redHat ()
                        continue                       
                    # Voltar ao menu anterior
                    case 3:
                        break
                    case _:
                        entrada_invalida3 ()
                        continue  
            except ValueError:
                entrada_invalida2 ()
                continue
#-----------------------------------------------------------------------------------
def menu_programas_windows ():
    print("+--------------------------------------------------------+")
    print("|                  --> PROGRAMAS <--                     |")
    print("+--------------------------------------------------------+")
    print("|  1.  | Obter utilizadore e senha.                      |")
    print("+------+-------------------------------------------------+")
    print("|  2.  | Voltar                                          |")
    print("+--------------------------------------------------------+")
    print("|                       @cmeasy                          |")
    print("+--------------------------------------------------------+")
def programas_windows ():
    while True:
            os.system("cls" if os.name == "nt" else "clear")
            menu_programas_windows ()
            escolha = input ("Escolha uma das opções acima: ")
            if escolha == "":
                entrada_invalida1 ()
                continue
            else:
                try:
                    opcao = int (escolha)
                    match opcao: 
                        case 1:
                            print ("Indisponivel no momento...")
                            enter_clear ()
                            continue
                        case 2:
                            break
                        case _:
                            entrada_invalida3 ()
                            continue
                except ValueError:
                    entrada_invalida2 ()
                    continue
#-----------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------
def programas_windows ():
    while True:
            os.system("cls" if os.name == "nt" else "clear")
            menu_programas_sO ()
            escolha = input ("Escolha uma das opções acima: ")
            if escolha == "":
                entrada_invalida1 ()
                continue
            else:
                try:
                    opcao = int (escolha)
                    match opcao: 
                        case 1:
                            print ("Indisponivel no momento...")
                            enter_clear ()
                            continue
                        case 2:
                            break
                        case _:
                            entrada_invalida3 ()
                            continue
                except ValueError:
                    entrada_invalida2 ()
                    continue




def programas ():
    while True:
            os.system("cls" if os.name == "nt" else "clear")
            menu_programas_sO ()
            escolha = input ("Escolha uma das opções acima: ")
            if escolha == "":
                entrada_invalida1 ()
                continue
            else:
                try:
                    opcao = int (escolha)
                    match opcao: 
                        case 1:
                            tipo_de_programas_linux ()
                            continue
                        case 2:
                            print ("Indisponivel no momento...")
                            enter_clear ()
                            continue
                        case 3:
                            break
                        case _:
                            entrada_invalida3 ()
                            continue
                except ValueError:
                    entrada_invalida2 ()
                    continue
############################################################################################################################################
############################################################################################################################################
############################################################################################################################################

#----------------> 2. Executar Comandos Linux <-----------------
# Menus
def menu_permisions_type ():
    print("+----------------------------------------+")
    print("|            O P Ç Õ E S                 |")
    print("+----------------------------------------+")
    print("|1. Permissão de leitura (read).         |")
    print("|2. Permissão de escrita (write).        |")
    print("|3. Permissão de execução (execute).     |")
    print("|4. Remover permissão de leitura.        |")
    print("|5. Remover permissão de escrita.        |")
    print("|6. Remover permissão de execução.       |")
    print("|7. Sair.                                |")
    print("+----------------------------------------+")
    print("|             - CMEasy -                 |")
    print("+----------------------------------------+")
def menu_zip_type ():
    print("+-------------------------------------------------+")
    print("|                  O P Ç Õ E S                    |")
    print("+-------------------------------------------------+")
    print("|1. Instalar o compactador de arquivos ou pasta.  |")
    print("+-------------------------------------------------+")
    print("|2. Zipar um arquivo.                             |")
    print("|3. Zipar um arquivo com senha.                   |")
    print("|4. Zipar uma pasta.                              |")
    print("|5. Zipar um arquivo com senha.                   |")
    print("|6. Sair.                                         |")
    print("+-------------------------------------------------+")
    print("|                   - CMEasy -                    |")
    print("+-------------------------------------------------+")
def comandos_linux_menu1 ():
    print("+-----------------------------------------------------------------------------+")
    print("|                            C O M A N D O S                                  |")
    print("+-----------------------------------------------------------------------------+")
    print("|  1.  | Ajustar relógio do sistema.                                          |")
    print("+------+----------------------------------------------------------------------+")
    print("|  2.  | Alterar a senha de um usuário.                                       |")
    print("+------+----------------------------------------------------------------------+")
    print("|  3.  | Atualizar todos os programas instalados.                             |")
    print("+------+----------------------------------------------------------------------+")
    print("|  4.  | Informações de rede e interfaces.                                    |")
    print("+------+----------------------------------------------------------------------+")
    print("|  5.  | Informação do sistema.                                               |")
    print("+------+----------------------------------------------------------------------+")
    print("|  6.  | Localizar arquivos no sistema.                                       |")
    print("+------+----------------------------------------------------------------------+")
    print("|  7.  | Extrair arquivos.                                                    |")
    print("+------+----------------------------------------------------------------------+")
    print("|  8.  | Listar arquivos e pastas de um diretório.                            |")
    print("+------+----------------------------------------------------------------------+")
    print("|  9.  | Listar arquivos e pastas de um diretório especifico.                 |")
    print("+------+----------------------------------------------------------------------+")
    print("|  10. | Alterar permissões de arquivos e pastas.                             |")
    print("+------+----------------------------------------------------------------------+")
    print("|  11. | Matar um processo.                                                   |")
    print("+------+----------------------------------------------------------------------+")
    print("|  12. | Pesquisar um Ficheiros no sistema.                                   |")
    print("+------+----------------------------------------------------------------------+")
    print("|  13. | Criar um utilizador.                                                 |")
    print("+------+----------------------------------------------------------------------+")
    print("|  14. | Zipar um arquivo ou pasta.                                           |")
    print("+------+----------------------------------------------------------------------+")
    print("|  15. | Informação de harware do sistema.                                    |")
    print("+------+----------------------------------------------------------------------+")
    print("|  16. | Listar todos os processos em execução no sistema.                    |")
    print("+------+----------------------------------------------------------------------+")
    print("|  17. | Monitorização de Portas e Serviços de Rede.                          |")
    print("+------+----------------------------------------------------------------------+")
    print("|  18. | Visualizar a rota da rede.                                           |")
    print("+------+----------------------------------------------------------------------+")
    print("|  19. | Capturar Pacotes na rede.                                            |")
    print("+-----------------------------------------------------------------------------+")
    print("|                                20. Ver mais.                                |")
    print("+-----------------------------------------------------------------------------+")
    print("|  21. | Voltar.                                                              |")
    print("+-----------------------------------------------------------------------------+")
    print("|                                   - CMEasy -                                |")
    print("+-----------------------------------------------------------------------------+")
def comandos_linux_menu2 ():
    print("+-----------------------------------------------------------------------------+")
    print("|                            C O M A N D O S                                  |")
    print("+-----------------------------------------------------------------------------+")
    print("|  1.  | Visualizar Logs do sistema.                                          |")
    print("+------+----------------------------------------------------------------------+")
    print("|  2.  | Visualizar a listar Pacotes Instalados.                              |")
    print("+-----------------------------------------------------------------------------+")
    print("|                                20. Ver mais.                                |")
    print("+-----------------------------------------------------------------------------+")
    print("|  21. | Voltar.                                                              |")
    print("+-----------------------------------------------------------------------------+")
    print("|                                   - CMEasy -                                |")
    print("+-----------------------------------------------------------------------------+")
################# COMANDOS LINUX ################################
# Informação do sistema
def comando_infoSystem_hardware ():
    subprocess.run(["sudo", "lshw", "-short"])
    enter_clear ()
# Informação do sistema
def comando_infoSystem ():
    subprocess.run(["hostnamectl"])
    enter_clear ()
# Nome de usuario
def comando_username ():
    user = subprocess.run(["whoami"], capture_output=True, text=True)
    print(f"Nome do utilizador: {user.stdout}")
    enter_clear ()
# Alterar o nome de usuario
def comando_alterar_username ():
    antigo_nome = input("Escreva o nome do atual: ")
    novo_nome = input("Escreva o novo nome: ")
    user = subprocess.run( ["sudo", "usermod", "-l", novo_nome, "-d", f"/home/{novo_nome}", "-m", antigo_nome], capture_output=True, text=True )
    if user.returncode == 0:
        print(f"Utilizador {antigo_nome} renomeado para {novo_nome} com sucesso!")
    else:
        print("Ocorreu um erro:")
        print(user.stderr)
    enter_clear ()
# Matar um processo
def comando_killProcess ():
    n_processo = input ("Indique o número do processo: ")
    subprocess.run(["kill", "-9", n_processo])
    print(f"O processo nº {n_processo} foi encerrado com sucesso")
    enter_clear ()
# Ajuste de relogio
def comando_time_so ():
    try:
        print("|------------Alterando do relogio do sistema--------------|")
        subprocess.run(["sudo", "apt", "update"], check=True)
        subprocess.run(["sudo", "dpkg-reconfigure", "tzdata"], check=True)
        subprocess.run(["sudo", "apt", "install", "chrony", "-y"], check=True)
        print("|------------Comando executado com sucesso--------------|")
    except subprocess.CalledProcessError as e:
        print(f"Ocorreu um erro ao executar o comando: {e}")
    enter_clear()
def comando_time_so2 ():
    try:
        print("|------------Alterando do relogio do sistema--------------|")
        subprocess.run(["sudo", "apt", "update"], check=True)
        subprocess.run(["sudo", "dpkg-reconfigure", "tzdata"], check=True)
        subprocess.run(["sudo", "dnf", "install", "chrony", "-y"], check=True)
        print("|------------Comando executado com sucesso--------------|")
    except subprocess.CalledProcessError as e:
        print(f"Ocorreu um erro ao executar o comando: {e}")
    enter_clear()
# Alterar senha de usuarios
def comando_passwd_users ():
    userName= input("Qual e o nome do usuario: ")
    subprocess.run(["passwd", userName])
    print("|------------Comando executado com sucesso--------------|")
    enter_clear()
# Atualizar todos programas 
def comando_upgrade_prog ():
    subprocess.run(["sudo", "apt", "upgrade", "-y"], check=True)
    print("|------------Comando executado com sucesso--------------|")
    enter_clear()
# Interface de rede
def comando_inf_rede ():
    subprocess.run(["ip", "a"], check=True)
    print("|------------Comando executado com sucesso--------------|")
    enter_clear ()
# Localizar Arquivo
def comando_local_arq ():
    arquivo_pasta= input ("Escreva o nome do arquivo: ")
    subprocess.run(["locate", arquivo_pasta], check=True)
    print("|------------Comando executado com sucesso--------------|")
    enter_clear()
# Extrair arquivos
def menu_comandos_zip ():
    print("+-----------------------------------------------------------------------------+")
    print("|                           TIPOS DE ARQUIVOS ZIP                             |")
    print("+-----------------------------------------------------------------------------+")
    print("|  1.  | Extrair arquivos (.tar).                                             |")
    print("+------+----------------------------------------------------------------------+")
    print("|  2.  | Extrair arquivos (.tar.gz).                                          |")
    print("+------+----------------------------------------------------------------------+")
    print("|  3.  | Extrair arquivos (.gz).                                              |")
    print("+------+----------------------------------------------------------------------+")
    print("|  4.  | Voltar.                                                              |")
    print("+-----------------------------------------------------------------------------+")
    print("|                                - CMEasy -                                   |")
    print("+-----------------------------------------------------------------------------+")
def comando_extrat_targz():
    arquivo_pasta= input ("Indique o camindo do arquivo: ")
    subprocess.run(["tar", "-xzvf", arquivo_pasta], check=True)
    print("|------------Comando executado com sucesso--------------|")
    enter_clear()
def comando_extrat_tar():
    arquivo_pasta= input ("Indique o camindo ou o nome do arquivo (ex: nome.tar.gz): ")
    subprocess.run(["tar", "-xvf", arquivo_pasta], check=True)
    print("|------------Comando executado com sucesso--------------|")
    enter_clear()
def comando_extrat_gz():
    arquivo_pasta= input ("Indique o camindo ou nome do arquivo (ex: nome.gz): ")
    subprocess.run(["gzip", "-d", arquivo_pasta], check=True)
    print("|------------Comando executado com sucesso--------------|")
    enter_clear()
def extr_zip ():
    try:
        while True:
                os.system("cls" if os.name == "nt" else "clear")
                menu_comandos_zip ()
                escolha = input ("Escolha uma das opções acima: ")
                if escolha == "":
                    entrada_invalida1 ()
                    continue
                else:
                    try:
                        opcao = int (escolha)
                        match opcao: 
                            case 1:
                                comando_extrat_tar ()
                                continue
                            case 2:
                                comando_extrat_targz ()
                                continue
                            case 3:
                                comando_extrat_gz ()
                                continue
                            case 4:
                                break
                            case _:
                                entrada_invalida3 ()
                                continue
                    except ValueError:
                        entrada_invalida2 ()
                        continue
    except KeyboardInterrupt:
        print("\nCMEasy encerrado! ")
# Listar arquivos e pastas
def comando_list_dir1():
    try:
        print("|------------ Executando o comando --------------|")
        subprocess.run(["ls", "-lha"], check=True)
        print("|------------ Comando executado com sucesso --------------|")
    except Exception as e:
        print("Ocorreu um erro durante a execução do comando:", e)
    enter_clear()
# Listar arquivos e pastas especifico
def comando_list_dir2():
    arquivo_pasta= input ("Indique o camindo da Diretoria: ")
    subprocess.run(["ls", "-lh", arquivo_pasta], check=True)
    print("|------------Comando executado com sucesso--------------|")
    enter_clear()
# Manipuar permioes de arquivos e pastas
def comando_permissao ():
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        menu_permisions_type ()
        escolha = input ("Escolha uma das opções acima: ")
        if escolha == "":
            entrada_invalida1 ()
            continue
        else:
            try:
                opcao = int (escolha)
                match opcao: 
                    case 1:
                        arquivo_pasta= input ("Indique o camindo da Direoria ou do arquivo: ")
                        subprocess.run(["chmod", "+r", arquivo_pasta])
                        print("|------------Comando executado com sucesso--------------|")
                        enter_clear ()
                    case 2:
                        arquivo_pasta= input ("Indique o camindo da Direoria ou do arquivo: ")
                        subprocess.run(["chmod", "+w", arquivo_pasta])
                        print("|------------Comando executado com sucesso--------------|")
                        enter_clear ()
                    case 3:
                        arquivo_pasta= input ("Indique o camindo da Direoria ou do arquivo: ")
                        subprocess.run(["chmod", "+x", arquivo_pasta])
                        print("|------------Comando executado com sucesso--------------|")
                        enter_clear ()
                    case 4:
                        arquivo_pasta= input ("Indique o camindo da Direoria ou do arquivo: ")
                        subprocess.run(["chmod", "-x", arquivo_pasta])
                        print("|------------Comando executado com sucesso--------------|")
                        enter_clear ()
                    case 5:
                        arquivo_pasta= input ("Indique o camindo da Direoria ou do arquivo: ")
                        subprocess.run(["chmod", "-r", arquivo_pasta])
                        print("|------------Comando executado com sucesso--------------|")
                        enter_clear ()
                    case 6:
                        arquivo_pasta= input ("Indique o camindo da Direoria ou do arquivo: ")
                        subprocess.run(["chmod", "-w", arquivo_pasta])
                        print("|------------Comando executado com sucesso--------------|")
                        enter_clear ()
                    case 7:
                        break
                    case _:
                        entrada_invalida3 ()
                        continue
            except ValueError:
                entrada_invalida2 ()
                continue
# Visualizar portas abertas
def comando_searhfile ():
    try:
        print("|------------ Executando o comando --------------|")
        ficheiro = input ("Indique o nome do ficheiro: ")
        subprocess.run(["find", "/", "-name", ficheiro], check=True)
        print("|------------ Comando executado com sucesso --------------|")
    except Exception as e:
        print("Ocorreu um erro durante a execução do comando:", e)
    enter_clear()
# Criar usuario 
def comando_creatUser ():
    # Pedir nome do usuário e senha
    userName = input("Indique o nome do utilizador: ")
    passUser = input("Indique a palavra passe: ")

    # Criar usuário com diretório home e shell bash
    subprocess.run(["sudo", "useradd", "-m", "-s", "/bin/bash", userName], check=True)

    # Definir a senha do usuário usando chpasswd
    subprocess.run(['sudo', 'chpasswd'], input=f"{userName}:{passUser}".encode(), check=True)

    print("|------------Comando executado com sucesso--------------|")
    enter_clear ()
# Zipar um arquivo 
def instalar_zip ():
    subprocess.run(["sudo", "apt", "install", "zip"], check=True)
    print("|------------ Comando executado com sucesso --------------|")
    enter_clear ()
def comando_zip1 ():
    arqZip1 = input("Indique o nome ou o arquivo zip (nome.zip): ")
    arqZip2 = input("Indique o nome ou o caminho do arquivo: ")
    subprocess.run(["sudo", "zip", arqZip1, arqZip2], check=True)
    print("|------------Comando executado com sucesso--------------|")
    enter_clear ()
def comando_zipPass1 ():
    arqZip1 = input("Indique o nome ou o arquivo zip (nome.zip): ")
    arqZip2 = input("Indique o nome ou o caminho do arquivo: ")
    subprocess.run(["sudo", "zip","-e", arqZip1, arqZip2], check=True)
    print("|------------Comando executado com sucesso--------------|")
    enter_clear ()
def comando_zip2 ():
    arqZip1 = input("Indique o nome ou o arquivo zip (nome.zip): ")
    arqZip2 = input("Indique o nome ou o caminho da pasta: ")
    subprocess.run(["sudo", "zip", "-r", arqZip1, arqZip2], check=True)
    print("|------------Comando executado com sucesso--------------|")
    enter_clear ()
def comando_zipPass2 ():
    arqZip1 = input("Indique o nome ou o arquivo zip (nome.zip): ")
    arqZip2 = input("Indique o nome ou o caminho do arquivo: ")
    subprocess.run(["sudo", "zip","-r", "-e", arqZip1, arqZip2], check=True)
    print("|------------Comando executado com sucesso--------------|")
    enter_clear ()
def comandos_zip ():
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        menu_zip_type ()
        escolha = input ("Escolha uma das opções acima: ")
        if escolha == "":
            entrada_invalida1 ()
            continue
        else:
            try:
                opcao = int (escolha)
                match opcao: 
                    case 1:
                        instalar_zip ()
                        continue
                    case 2:
                        comando_zip1 ()
                        continue
                    case 3:
                        comando_zipPass1 ()
                        continue
                    case 4:
                        comando_zip2 ()
                        continue
                    case 5:
                        comando_zipPass2 ()
                        continue
                    case 6:
                        break
                    case _:
                        entrada_invalida3 ()
                        continue
            except ValueError:
                entrada_invalida2 ()
                continue
#listar todos os processos em execução no sistema
def comandolistProcess():
    subprocess.run(["ps", "aux"])
    enter_clear ()
# Monitorização de Portas e Serviços de Rede
def comando_serviPortList ():
    try:
        print("|------------ Executando o comando --------------|")
        subprocess.run(["ss", "-tuln"], check=True)
        print("|------------ Comando executado com sucesso --------------|")
    except Exception as e:
        print("Ocorreu um erro durante a execução do comando:", e)
    enter_clear()
# Monitorização de Portas e Serviços de Rede
def comoando_rotaRede ():
    try:
        print("|------------ Executando o comando --------------|")
        destino = input ("Indique o ip ou dominio do alvo: ")
        subprocess.run(["traceroute", destino], check=True)
        print("|------------ Comando executado com sucesso --------------|")
    except Exception as e:
        print("Ocorreu um erro durante a execução do comando:", e)
    enter_clear()
# Capturar Pacotes na rede. 
def comando_capRede ():
    try:
        print("|------------ Executando o comando --------------|")
        subprocess.run(["ip", "link"], check=True)
        int_rede = input ("Indique a sua interface de rede: ")
        subprocess.run(["sudo", "tcpdump", "-i", int_rede], check=True)
        print("|------------ Comando executado com sucesso --------------|")
    except Exception as e:
        print("Ocorreu um erro durante a execução do comando:", e)
    enter_clear()
# Visualizar Logs do sistema
def comando_logsSystem ():
    try:
        print("|------------ Executando o comando --------------|")
        subprocess.run(["journalctl", "-xe"], check=True)
        print("|------------ Comando executado com sucesso --------------|")
    except Exception as e:
        print("Ocorreu um erro durante a execução do comando:", e)
    enter_clear()
# Visualizar a listar Pacotes Instalados.
def comando_Listpackadge ():
    try:
        print("|------------ Executando o comando --------------|")
        subprocess.run(["dpkg", "-l"], check=True)
        print("|------------ Comando executado com sucesso --------------|")
    except Exception as e:
        print("Ocorreu um erro durante a execução do comando:", e)
    enter_clear()
#####################################################################################################################

# programa comandos linux familia debian
def distro_debian1 ():    
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        comandos_linux_menu1 ()
        escolha = input ("Escolha uma das opções acima: ")
        if escolha == "":
            entrada_invalida1 ()
            continue
        else:
            try:
                opcao = int (escolha)
                match opcao: 
                    case 1:
                        comando_time_so ()
                        continue
                    case 2:
                        comando_passwd_users ()
                        continue
                    case 3:
                        comando_upgrade_prog ()
                        continue
                    case 4:
                        comando_inf_rede ()
                        continue
                    case 5:
                        comando_infoSystem ()
                        continue
                    case 6:
                        comando_local_arq ()
                        continue
                    case 7:
                        extr_zip ()
                        continue
                    case 8:
                        comando_list_dir1 ()
                        continue
                    case 9:
                        comando_list_dir2 ()
                        continue
                    case 10:
                        comando_permissao ()
                        continue
                    case 11:
                        comando_killProcess ()
                        continue
                    case 12:
                        comando_searhfile ()
                        continue
                    case 13:
                        comando_creatUser()
                        continue
                    case 14:
                        comandos_zip ()
                        continue
                    case 15:
                        comando_infoSystem_hardware ()
                        continue
                    case 16:
                        comandolistProcess ()
                        continue
                    case 17:
                        comando_serviPortList ()
                        continue
                    case 18:
                        comoando_rotaRede ()
                        continue
                    case 19:
                        comando_capRede ()
                        continue
                    case 20:
                        distro_debian2 ()
                        continue
                    case 21:
                        break
                    case _:
                        entrada_invalida3 ()
                        continue
            except ValueError:
                entrada_invalida2 ()
                continue
def distro_debian2 ():    
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        comandos_linux_menu2 ()
        escolha = input ("Escolha uma das opções acima: ")
        if escolha == "":
            entrada_invalida1 ()
            continue
        else:
            try:
                opcao = int (escolha)
                match opcao: 
                    case 1:
                        comando_logsSystem ()
                        continue
                    case 2:
                        comando_Listpackadge ()
                        continue
                    case 20:
                        print ("Indisponivel no momento...")
                        enter_clear ()
                        continue
                    case 21:
                        break
                    case _:
                        entrada_invalida3 ()
                        continue
            except ValueError:
                entrada_invalida2 ()
                continue
# programa comandos linux familia debian
def distro_redHat ():    
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        comandos_linux_menu1 ()
        escolha = input ("Escolha uma das opções acima: ")
        if escolha == "":
            entrada_invalida1 ()
            continue
        else:
            try:
                opcao = int (escolha)
                match opcao: 
                    case 1:
                        comando_time_so2 ()
                        continue
                    case 16:
                        comandolistProcess ()
                        continue
                    case 20:
                        break
                    case _:
                        entrada_invalida3 ()
                        continue
            except ValueError:
                entrada_invalida2 ()
                continue
# programa escolha de familias linux
def comandos_linux_distro ():    
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        menu_instalar_programas ()
        escolha = input ("Escolha uma das opções acima: ")
        if escolha == "":
            entrada_invalida1 ()
            continue
        else:
            try:
                opcao = int (escolha)
                match opcao: 
                    case 1:
                        distro_debian1 ()
                        continue
                    case 2:
                        print ("Indisponivel no momento...")
                        enter_clear ()
                        #distro_redHat ()
                        continue
                    case 3:
                        break
                    case _:
                        entrada_invalida3 ()
                        continue
            except ValueError:
                entrada_invalida2 ()
                continue

######################################################################################################################
######################################################################################################################
######################################################################################################################

#----------------> 3. Executar Comandos Windos <-----------------
def comandos_windows_menu ():
    print("+-----------------------------------------------------------------------------+")
    print("|                            C O M A N D O S                                  |")
    print("+-----------------------------------------------------------------------------+")
    print("|  1.  | Informação do sistema.                                               |")
    print("+------+----------------------------------------------------------------------+")
    print("|  2.  | Verificar e reparar arquivos do sistema.                             |")
    print("+------+----------------------------------------------------------------------+")
    print("|  3.  | Informação de Rede (Networking).                                     |")
    print("+------+----------------------------------------------------------------------+")
    print("|  4.  | Atualizar todos os programas.                                        |")
    print("+------+----------------------------------------------------------------------+")
    print("|  5.  | Verificar e corrigir erros no disco.                                 |")
    print("+------+----------------------------------------------------------------------+")
    print("|  6.  | Limpar cache de DNS (resolver problemas de internet).                |")
    print("+------+----------------------------------------------------------------------+")
    print("|  7.  | Apagar arquivos temporários do sistema.                              |")
    #print("+------+----------------------------------------------------------------------+")
    #print("|  9.  | Listar arquivos e pastas de um diretório.                            |")
    #print("+------+----------------------------------------------------------------------+")
    #print("|  10. | Listar arquivos e pastas de um diretório especifico.                 |")
    #print("+------+----------------------------------------------------------------------+")
    #print("|  11. | Alterar permissões de arquivos e pastas.                             |")
    #print("+------+----------------------------------------------------------------------+")
    #print("|  12. | Matar um processo.                                                   |")
    #print("+------+----------------------------------------------------------------------+")
    #print("|  13. | Visualizar as portas abertas no sistema.                             |")
    print("+------+----------------------------------------------------------------------+")
    print("|  20. | Voltar.                                                              |")
    print("+-----------------------------------------------------------------------------+")
    print("|                                - CMEasy -                                   |")
    print("+-----------------------------------------------------------------------------+")
################# COMANDOS WINDOWS ################################
def infsystem ():
    print ("Executando o comando...")
    try:
        os.system("systeminfo")
        enter_clear ()
    except ValueError:
        print("ocorreu um erro na execução do comando.")
        enter_clear ()
def error_system ():
    print ("Executando o comando...")
    try:
        os.system("sfc /scannow")
    except PermissionError:
        print("Erro: Permissão negada. Execute como administrador.")
    except ValueError:
        print("ocorreu um erro na execução do comando.")
    enter_clear ()
def infRede ():
    print ("Executando o comando...")
    try:
        os.system("ipconfig")
    except PermissionError:
        print("Erro: Permissão negada. Execute como administrador.")
    except Exception as e:
        print("Ocorreu um erro na execução do comando:", e)
    enter_clear ()
def actProgramas ():
    print ("Executando o comando...")
    try:
        os.system("winget upgrade --all -y")
    except PermissionError:
        print("Erro: Permissão negada. Execute como administrador.")
    except ValueError:
        print("ocorreu um erro na execução do comando.")
    enter_clear ()
def verif_disk ():
    print("Executando o comando...")
    try:
        disco = input("Indique a letra correspondente ao disco (ex: C): ").upper().replace(":", "")

        if len(disco) == 1 and disco.isalpha():
            os.system(f"chkdsk {disco}: /f")
        else:
            print("Entrada inválida.")
    except PermissionError:
        print("Erro: Permissão negada. Execute como administrador.")
    except Exception as e:
        print("Ocorreu um erro na execução do comando:", e)
    enter_clear ()
def clear_cahs_dns ():
    print ("Executando o comando...")
    try:
        os.system("ipconfig /flushdns")
    except PermissionError:
        print("Erro: Permissão negada. Execute como administrador.")
    except Exception as e:
        print("Ocorreu um erro na execução do comando:", e)
    enter_clear ()
def del_arq_temp ():
    print ("Executando o comando...")
    try:
        os.system("del /q/f/s %temp%*")
    except PermissionError:
        print("Erro: Permissão negada. Execute como administrador.")
    except Exception as e:
        print("Ocorreu um erro na execução do comando:", e)
    enter_clear ()
######################################################################################################################
# Comandos no windows   
def comandos_windows(): 
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        comandos_windows_menu ()
        escolha = input ("Escolha uma das opções acima: ")
        if escolha == "":
            entrada_invalida1 ()
            continue
        else:
            try:
                opcao = int (escolha)
                match opcao: 
                    case 1:
                        infsystem ()
                        continue
                    case 2:
                        error_system ()
                        continue
                    case 3:
                        infRede ()
                        continue
                    case 4:
                        actProgramas ()
                        continue
                    case 5:
                        verif_disk ()
                        continue
                    case 6:
                        clear_cahs_dns()
                        continue
                    case 7:
                        del_arq_temp()
                        continue
                    case 20:
                        break
                    case _:
                        entrada_invalida3 ()
                        continue
            except ValueError:
                entrada_invalida2 ()
                continue

######################################################################################################################
# Programas comandos windows
def comandos ():
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        menu_programas_sO ()
        escolha = input ("Escolha uma das opções acima: ")
        if escolha == "":
            entrada_invalida1 ()
            continue
        else:
            try:
                opcao = int (escolha)
                match opcao: 
                    case 1:
                        comandos_linux_distro ()
                        continue
                    case 2:
                        comandos_windows ()
                        continue
                    # Voltar ao menu anterior
                    case 3:
                        break
                    case _:
                        entrada_invalida3 ()
                        continue
            except ValueError:
                entrada_invalida2 ()
                continue

######################################################################################################################
######################################################################################################################
######################################################################################################################

#----------------> 3. Informacao do programa <-----------------
# Menu Informacao
def menu_inform ():
    print("+--------------------------------------------------------+")
    print("|           --> INFORMACAO DO PROGRAMA <--               |")
    print("+--------------------------------------------------------+")
    print("| Nome: CMEasy                                           |")
    print("+--------------------------------------------------------+")
    print("| Criador: Cleison Máquina                               |")
    print("+--------------------------------------------------------+")
    print("| Sistema Operacional: Linux, Windows                    |")
    print("+--------------------------------------------------------+")
    print("| Ano de Criação: 2026                                   |")
    print("+--------------------------------------------------------+")
    print("| Linguagem de Programação: Python                       |")
    print("+--------------------------------------------------------+")
    print("| Versao: 0.1v                                           |")
    print("+--------------------------------------------------------+")
    print("| Descrição: Ferramenta desenvolvida para otimizar       |")
    print("|processos operacionais através da automação de setups e |")
    print("|da padronização na execução de scripts e comandos.      |")
    print("+--------------------------------------------------------+")
    print("|            Clique [ ENTER ] para voltar                |")
    print("+--------------------------------------------------------+")
    print("|                     @cmeasy                            |")
    print("+--------------------------------------------------------+") 

######################################################################################################################
######################################################################################################################
######################################################################################################################

# Programa CMEasy.
def main ():
    while True:
        # Limpar a tela antes de iniciar o porgrama
        os.system("cls" if os.name == "nt" else "clear")
        # Painel Principal (Menu Principal)
        menu_principal ()
        escolha = input ("Escolha uma das opções acima: ")
        # Se o utilizador nao ditar nada 
        if escolha == "":
                entrada_invalida1 ()
                continue
        # Se o utilizador digitar alguma coisa diferente 
        else:  
            # Tentar converter a entrada para um número inteiro
            try:
                opcao = int(escolha)
                match opcao:
                    #-------- 1. Instalar Promagramas
                    case 1:
                        programas ()
                        continue
                    # Executar comandos
                    case 2:
                        comandos ()
                        continue
                    # Scripts para vulnerabildades
                    case 3:
                        print ("Indisponível no momento...")
                        enter_clear ()
                        continue
                    # Informacao do sistema operacional
                    case 4:
                        os.system("cls" if os.name == "nt" else "clear")
                        menu_inform ()
                        enter_clear ()
                        continue
                    #-------- 4. Encerrar o programa
                    case 5:
                        print("Programa 'CMEasy' encerrado, Obrigado!")
                        break 
                    case _:
                            # Este case captura qualquer entrada que não seja uma opção válida
                            entrada_invalida3 ()
                            continue  
            except ValueError:
                # Se a conversão falhar (não for um número), exibe uma mensagem de erro
                entrada_invalida2 ()
                continue
            

try:
    main()
except KeyboardInterrupt:
    print("\nCMEasy encerrado!!")