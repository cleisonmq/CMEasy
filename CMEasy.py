# CMEasy
# Versão 0.1v
# Create By Cleison Máquina

import subprocess
import shutil
import signal
import sys

#--------------------> Codigos mais usados <-----------------
# Botao para quando o utilisador clicar em enter o programa limpre a tela 
def enter_clear ():
    input("Pressione [ ENTER ] para continuar")
    subprocess.run(["clear"])
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
#------------------------------------------------------------

#-------------------------> CMEasy <-------------------------
# Menu Principal
def menu_principal ():
    print("+--------------------------------------------------------+")
    print("|                      - CMEasy -                        |")
    print("+--------------------------------------------------------+")
    print("|                       M E N U                          |")
    print("+------+-------------------------------------------------+")
    print("|  1.  | Instalar Promagramas                            |")
    print("+------+-------------------------------------------------+")
    print("|  2.  | Executar Comandos                               |")
    print("+------+-------------------------------------------------+")
    print("|  3.  | Informação                                      |")
    print("+------+-------------------------------------------------+")
    print("|  4.  | Encerrar o programa                             |")
    print("+--------------------------------------------------------+")
#------------------------------------------------------------
############################################################################

###########################################################################
#----------------> 1. Instalar Promagramas <-----------------

# Menu Principal (Tipos de distribuicao)
def menu_instalar_programas ():
    print("+--------------------------------------------------------+")
    print("|              --> INSTALAR PROGRAMAS <--                |")
    print("+--------------------------------------------------------+")
    print("|                  DISTRIBUÇÃO LINUX                     |")
    print("+--------------------------------------------------------+")
    print("|  1.  | Familia Debian (Ubunto, Kali Linux...)          |")
    print("+------+-------------------------------------------------+")
    #print("|      | Familia Red Hat (Rocky Linux, Cent OS...)      |")
    #print("+------+-------------------------------------------------+")
    #print("|      | Familia Arch (Arch Linux, Manjaro...)           |")
    #print("+------+-------------------------------------------------+")
    print("|  2.  | Voltar                                          |")
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
    print("|  3.  | Outros Tipos                                    |")
    print("+------+-------------------------------------------------+")
    print("|  4.  | Voltar                                          |")
    print("+--------------------------------------------------------+")
    print("|                       @cmeasy                          |")
    print("+--------------------------------------------------------+")
#-------------------------------------------------
#------------------------> Ciberseguranca
#--- Menu programas Ciberseguranca
def menu_so_ciberseguranca ():
    print("+--------------------------------------------------------+")
    print("|               --> SO CIBERSEGURANCA <--                |")
    print("+--------------------------------------------------------+")
    print("|  1.  | Fail2Ban                                        |")
    print("+------+-------------------------------------------------+")
    #print("|      | Programação                                     |")
    #print("+------+-------------------------------------------------+")
    #print("|      | Outros Tipos                                    |")
    #print("+------+-------------------------------------------------+")
    print("|  2.  | Voltar                                          |")
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
    print("|-----------------------------------------------------------------------------|")
    print("|       1. Instalar      |      2. Desinstalar       |      3. Comandos       |")
    print("+------------------------+---------------------------+------------------------+")
    print("|    4. Configuracoes    |          5. Logs          |        6. Sair         |")
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
            stop_fail2ban()
            subprocess.run(["sudo", "apt", "remove", "--purge", "fail2ban", "-y"], check=True)
            subprocess.run(["sudo", "apt", "autoremove", "-y"], check=True)
            subprocess.run(["sudo", "rm", "-rf", "/etc/fail2ban"], check=True)
            subprocess.run(["sudo", "rm", "-rf", "/var/log/fail2ban*"], check=True)
            subprocess.run(["sudo", "rm", "-rf", "/var/lib/fail2ban"], check=True)
            subprocess.run(["sudo", "rm", "-rf", "/run/fail2ban"], check=True)
            subprocess.run(["sudo", "systemctl", "daemon-reload"], check=True)
            try:
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
    print("| [sshd]                                                                           |")
    print("| enabled = true                                                                   |")
    print("| port = ssh                                                                       |")
    print("| filter = sshd                                                                    |")
    print("| logpath = /var/log/auth.log                                                      |")
    print("| bantime = 900                                                                    |")
    print("| banaction = iptables-allports                                                    |")
    print("| findtime = 900                                                                   |")
    print("| maxretry = 3                                                                     |")
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

#------------------------> Programacao

#------------------------> Outros programas
# Menu Principal
def menu_outros_programas ():
    print("+--------------------------------------------------------------+")
    print("|                      OUTROS PROGRAMAS                        |")
    print("+--------------------------------------------------------------+")
    print("|  1.  | SSH (Secure Shell)                                    |")
    print("+------+-------------------------------------------------------+")
    #print("| 2. | Iniciar                                                 |")
    #print("+----+---------------------------------------------------------+")
    #print("| 3. | Estado                                                  |")
    #print("+----+---------------------------------------------------------+")
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
    print("|  2.  | Sair                                                  |")
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
        subprocess.run(["sudo", "apt","install", "-y", "openssh-server"], check=True)
        print("|---------------------- SSH instalado com sucesso --------------------------------|")
        
        print("|-------------------------- ativando o ssh ------------------------------|")
        subprocess.run(["systemctl", "enable", "ssh"], check=True)
        print("|---------------------- SSH ativado com sucesso --------------------------------|")
        
        print("|---------------------------- Iniviando o ssh --------------------------------|")
        subprocess.run(["sudo", "apt", "install", "-y", "fail2ban"], check=True)
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
        subprocess.run(["sudo", "apt", "remove", "--purge", "-y", "openssh-server"], check=True)
        subprocess.run(["sudo", "apt", "autoremove", "-y"], check=True)
        subprocess.run(["sudo", "rm", "-rf", "/etc/ssh"], check=True) 
        subprocess.run(["sudo", "rm", "-rf", "/home/*/.ssh"], check=True)
        print("|----------------------- ssh desinstalado com sucesso ----------------------------|")
    except subprocess.CalledProcessError as e:
        print(f"Ocorreu um erro ao executar o comando: {e}")
        #-------------------- limpar a tela                                     
    enter_clear()
# Comandos
def menu_ssh_comandos ():
    print("+----------------------------------------------------+")
    print("|                    COMANDOS SSH                    |")
    print("+----------------------------------------------------+")
    print("| 1. Ativar                                          |")
    print("| 2. Iniciar                                         |")
    print("| 3. Estado                                          |")
    print("| 4. Parar                                           |")
    print("| 5. Reiniciar                                       |")
    print("| 6. Versao                                          |")
    print("| 7. Sair                                            |")
    print("+----------------------------------------------------+") 
def comandos_ssh ():
    while True:
        subprocess.run(["clear"])
        menu_ssh_comandos ()
        escolha = input ("Escolha uma das opções acima: ")
        if escolha == "":
            entrada_invalida1 ()
            continue
        else:
            try:
                opcao = int(escolha)
                match opcao:
                    case 1:
                        subprocess.run(["sudo", "systemctl", "enable", "ssh"], check=True) 
                        print ("|---------------- ssh Ativado com sucesso -----------------------|")
                        enter_clear ()
                        continue
                    case 2:
                        subprocess.run(["sudo", "systemctl", "start", "ssh"], check=True) 
                        print ("|---------------- ssh iniciado com sucesso -----------------------|")
                        enter_clear ()
                        continue
                    case 3:
                        subprocess.run(["sudo", "systemctl", "status", "ssh"]) 
                        enter_clear ()
                        continue
                    case 4:
                        subprocess.run(["sudo", "systemctl", "stop", "ssh"], check=True) 
                        print ("|---------------- ssh parado com sucesso -----------------------|")
                        enter_clear ()
                        continue
                    case 5:
                        subprocess.run(["sudo", "systemctl", "restart", "ssh"], check=True) 
                        print ("|---------------- ssh reiniciado com sucesso -----------------------|")
                        enter_clear ()
                        continue
                    case 6:
                        subprocess.run(["ssh", "-V"], check=True) 
                        enter_clear ()
                        continue
                    case 7:
                        enter_clear ()
                        break
                    case _:
                        entrada_invalida3 ()
                        continue 
            except ValueError:
                entrada_invalida2 ()
                continue 
###########################################################################

###########################################################################
#----------------> 2. Executar Comandos <-----------------

###########################################################################

###########################################################################
#----------------> 3. Informacao <-----------------
# Menu Informacao
def menu_inform ():
    print("+--------------------------------------------------------+")
    print("|           --> INFORMACAO DO PROGRAMA <--               |")
    print("+--------------------------------------------------------+")
    print("| Nome: CMEasy                                           |")
    print("+--------------------------------------------------------+")
    print("| Criador: Cleison Maquina                               |")
    print("+--------------------------------------------------------+")
    print("| Sistema Operacional: Linux                             |")
    print("+--------------------------------------------------------+")
    print("| Ano de Criacao: 2026                                   |")
    print("+--------------------------------------------------------+")
    print("| Linguagem de Programacao: Python                       |")
    print("+--------------------------------------------------------+")
    print("| Versao: 0.1v                                           |")
    print("+--------------------------------------------------------+")
    print("| Descricao: Automatizacao de processos refente a        |")
    print("|instalacao de programas e execusao de comandos.         |")
    print("+--------------------------------------------------------+")
    print("|            Clique [ ENTER ] para voltar                |")
    print("+--------------------------------------------------------+")
    print("|                     @cmeasy                            |")
    print("+--------------------------------------------------------+") 
###########################################################################

###########################################################################
# Programa CMEasy.
def main ():
    while True:
        # Limpar a tela antes de iniciar o porgrama
        subprocess.run(["clear"])
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
                        while True: 
                            subprocess.run(["clear"])
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
                                                                while True:
                                                                    subprocess.run(["clear"])
                                                                    menu_so_ciberseguranca ()
                                                                    escolha = input ("Escolha uma das opções acima: ")
                                                                    if escolha == "":
                                                                        entrada_invalida1 ()
                                                                        continue
                                                                    else:
                                                                        try:
                                                                            opcao = int (escolha)
                                                                            match opcao:
                                                                                # Programa Fail2Ban  
                                                                                case 1:
                                                                                    while True:
                                                                                        subprocess.run(["clear"])
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
                                                                                                            subprocess.run(["clear"])
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
                                                                                                                            enter_clear ()
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
                                                                                                                            enter_clear ()
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
                                                                                                        enter_clear ()
                                                                                                        break
                                                                                                    case _:
                                                                                                        entrada_invalida3 ()
                                                                                                        continue
                                                                                            except ValueError:
                                                                                                entrada_invalida2 ()
                                                                                                continue
                                                                                # Voltar ao menu anterior
                                                                                case 2:
                                                                                    enter_clear ()
                                                                                    break
                                                                                case _:
                                                                                    entrada_invalida3 ()
                                                                                    continue
                                                                        except ValueError:
                                                                            entrada_invalida2 ()
                                                                            continue
                                                            #-------- Programacao
                                                            case 2:
                                                                print ("Indisponivel no momento...")
                                                                enter_clear ()
                                                                continue
                                                            #-------- Outros Programas
                                                            case 3:
                                                                while True: 
                                                                    subprocess.run(["clear"])
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
                                                                                    while True: 
                                                                                        subprocess.run(["clear"])
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
                                                                                                        enter_clear ()
                                                                                                        break
                                                                                                    case _:
                                                                                                        entrada_invalida3 ()
                                                                                                        continue 
                                                                                            except ValueError:
                                                                                                entrada_invalida2 ()
                                                                                                continue 
                                                                                case 2:
                                                                                    enter_clear ()
                                                                                    break
                                                                                case _:
                                                                                    entrada_invalida3 ()
                                                                                    continue 
                                                                        except ValueError:
                                                                            entrada_invalida2 ()
                                                                            continue                                                               
                                                            # Voltar ao menu anterior
                                                            case 4:
                                                                enter_clear ()
                                                                break
                                                            case _:
                                                                entrada_invalida3 ()
                                                                continue
                                                    except ValueError:
                                                        entrada_invalida2 ()
                                                        continue                                        
                                        # Voltar ao menu anterior
                                        case 2:
                                            enter_clear ()
                                            break
                                        case _:
                                            entrada_invalida3 ()
                                            continue  
                                except ValueError:
                                    entrada_invalida2 ()
                                    continue
                    # Executar comandos
                    case 2:
                        print ("Indisponivel no momento...")
                        enter_clear ()
                        continue
                    # Informacao do sistema operacional
                    case 3:
                        subprocess.run(["clear"])
                        menu_inform ()
                        enter_clear ()
                        continue
                    #-------- 4. Encerrar o programa
                    case 4:
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

main ()
