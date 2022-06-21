from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time  
import random
from instagramutils.settings import * 


class BotInstagram():
    """Essa classe vai ter as Principais funções de
    um robo do instagram."""


    def __init__(self,name,password) -> None:
        self.password = password
        self.username = name
        self.driver = webdriver.Chrome('./chromedriver')
    
    @staticmethod
    def close(self):
        cursor = self.driver
        cursor.close()
    
    @staticmethod
    def dormir(cursor):
        time.sleep(random.randint(3,6)/1.714775)

        # Abre uma nova aba
        cursor.execute_script("window.open('');") 

        time.sleep(random.randint(2,7)/1.714775)
        cursor.switch_to.window(cursor.window_handles[0])
        
        time.sleep(random.randint(1,5))
        # Fecha a aba
        cursor.close()

        time.sleep(random.randint(2,7)/1.714775)
        cursor.switch_to.window(cursor.window_handles[0])

    def login(self):
        """Metódo para logar a conta"""

        cursor=self.driver 

        cursor.get('https://www.instagram.com/')
        time.sleep(2)
        ## Username
        user = cursor.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
        user.send_keys(self.username)

        ## Senha
        password = cursor.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
        password.send_keys(self.password)
        password.send_keys(Keys.ENTER)
        time.sleep(7)


    def follow(self):
        """Aqui vamos seguir as pessoas"""

        cursor = self.driver
        camp = cursor.find_element_by_xpath(PATH_CAMPODBUSCA)    
        
        #TODO: Colocar DataBase
        #Colocar uma data base de tags
        
        tag = '#memesfutebol'

        for letra in tag:
            camp.send_keys(letra)
            time.sleep(random.randint(1,5)/10)
        try:
            time.sleep(4)
            cursor.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[1]/a').click()
        except:
            pass

        time.sleep(random.randint(10,15)/1.1735)
       


        """Pegando os links para acessar o perfil"""
        links = cursor.find_elements_by_tag_name('a')
 
        hrefs = [href.get_attribute('href') for href in links]

        # Indo em cada link e seguindo
        for link in hrefs:
           
            """Aqui vai entrar em cada página e seguir algumas pessoas"""

            if not '/p/' in link:
                return
            # Verificando

            cursor.get(link)
            time.sleep(random.randint(10,13)/1.3785)

            # Indo na pag
            cursor.find_element_by_xpath(PATH_PAGINA).click()
            time.sleep(random.randint(7,11)/1.7389)

            # Clicando para ver seguidores
            cursor.find_element_by_xpath(PATH_SEGUIDORES).click()
            time.sleep(random.randint(7,11)/1.578)

            """Seguindo as pessoas"""
            PessoasSeguidas = 0
            while True:

                follow =  cursor.find_elements_by_tag_name('span')
                button = cursor.find_elements_by_tag_name('button')
                buttons = []
                follows = []

                for btn in button:
                    if '_acan _acap _acas' in btn.get_attribute('class') or '_acan _acap _acat' in btn.get_attribute('class'):
                        
                        buttons.append(btn)
                
                for user in follow:
                    if '_aacl _aaco _aacw _aacx _aad7 _aade' in user.get_attribute('class'):
                        follows.append(user)


                del buttons[0]
                #Pegando o botão para seguir e o nome do user
                print(f'Pessoas {len(follows)} Botoẽs:{len(buttons)}')


                """Indo seguir todos"""
                for pessoa in follows:

                    pessoa = pessoa.text

                    # Abrindo a database
                    with open('logs/database.txt','r') as db:
                        
                        # Checando se a pessoa já foi seguida
                        if pessoa in db:
                            del buttons[0]
                            continue

                        buttons[0].click()
                        del buttons[0]
                        PessoasSeguidas += 1

                    with open('logs/database.txt','a') as db:
                        db.write(f'{pessoa}\n')
                
                    time.sleep(random.randint(5,9)/1.87531)

                    if PessoasSeguidas >= 11:
                        break
                if PessoasSeguidas >= 11:
                        break
                
                """ Scroll"""
                pop_up_window = cursor.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[2]")    
                # Scroll till Followers list is there
                for i in range(0,4):
                    cursor.execute_script('arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;', 
                    pop_up_window)
                    time.sleep(random.randint(5,9)/1.25)


           

            self.dormir(cursor)
            time.sleep(random.randint(1240,1537)/0.9873)




test = BotInstagram('aoxybr','Shigapo1!!')

test.login()
while True:
    test.follow()
    time.sleep(random.randint(4000,7070))



