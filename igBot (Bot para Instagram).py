from selenium import webdriver
import time
import random
from datetime import datetime

global cont
# ANTES DE TUDO, LEMBRAR QUE PRECISA DO DRIVER EDGE, POIS ELE ESTÁ FEITO PELO EDGE

cont = 0
amigos = [ ]   #aqui você vai colocar o @ dos amigos que serão comentados


def remover_iguais(lista):
    l = []
    for i in lista:
        if i not in l:
            l.append(i)

    return l


print("Temos ", len(amigos), " Pessoas no nosso Banco")

data = "%d/%m/%Y %H:%M"
inicio = datetime.now().strftime(data)
print("Início em: ", inicio)


class EsseEMeu:

    @staticmethod
    def digitar(frase, ondeDigitar):
        for letra in frase:
            ondeDigitar.send_keys(letra)
            time.sleep(random.randint(3, 9) / 30)

    def esperar(self):
        time.sleep(5)

    def __init__(self, usuario, senha):
        self.usuario = usuario
        self.senha = senha
        self.driver = webdriver.Edge(executable_path=r'C:\Users\jacks\Desktop\Driver_Notes\msedgedriver.exe')

    def iniciar(self):
        global cont
        driver = self.driver
        driver.get("https://www.instagram.com")
        self.esperar()
        campoUsuario = driver.find_element_by_xpath("//input[@name = 'username']")
        campoUsuario.click()
        campoUsuario.clear()
        campoUsuario.send_keys(self.usuario)
        time.sleep(1)
        campoSenha = driver.find_element_by_xpath("//input[@name = 'password']")
        campoSenha.click()
        campoSenha.clear()
        campoSenha.send_keys(self.senha)
        self.esperar()
        botaoEntrar = driver.find_element_by_xpath("//button[@class = 'sqdOP  L3NKy   y3zKF     ']")
        botaoEntrar.click()
        time.sleep(4)
        driver.get("https://www.instagram.com/p/CIodli0BB6g/") #Colocar o Link do sorteio do instagram 
        self.esperar()
        driver.execute_script("window.scrollTo(0,200);")
        time.sleep(1)
        while (True):
            for i in amigos:
                try:
                    driver.find_element_by_class_name("Ypffh").click()
                    campoComentário = driver.find_element_by_class_name("Ypffh")
                    time.sleep(0.5)

                    self.digitar(i, campoComentário)
                    time.sleep(2)
                    botaoPublicar = driver.find_element_by_xpath("//button[contains(text(), 'Publicar')]")
                    botaoPublicar.click()
                    cont = cont + 1
                    r = random.randint(40, 120)
                    print("comentei ", cont, " vezes.", " Esperando ", r, " segundos")
                    time.sleep(r)
                except:
                    driver.execute_script("window.location.reload();")
                    time.sleep(3)


jackson = EsseEMeu("usuario", 'senha')  #Entre com seu Usuário e senha
jackson.iniciar()
