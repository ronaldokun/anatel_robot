#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 24 23:14:09 2017

@author: ronaldo
"""

# HTML PARSER
from bs4 import BeautifulSoup as soup

# INITIALIZE DRIVER
from selenium import webdriver


# WAIT AND CONDITIONS METHODS
# available since 2.26.0
from selenium.webdriver.support.ui import Select

# METHODS
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
# EXCEPTIONS
from selenium.common.exceptions import \
    NoSuchElementException

from locators import Login, Base, LatMenu, \
    Main, ListaBlocos, Bloco, Processo, Envio


from base import Page

import re


class LoginPage(Page):

    def login(self, usr, pwd):
        """
        make login and return and instance of browser"""

        self.driver.get(Login.URL)
        self.driver.maximize_window()

        usuario = self.wait_for_element_to_click(Login.LOGIN)
        senha = self.wait_for_element_to_click(Login.SENHA)

        # Clear any clutter on the form
        usuario.clear()
        usuario.send_keys(usr)

        senha.clear()
        senha.send_keys(pwd)

        # Hit Enter
        senha.send_keys(Keys.RETURN)

        return PagInicial(self.driver)


class PagInicial(Page):

    """
    This class is a subclass of page, this class is a logged page
    """

    def expand_visual(self):
        # example use

        try:
            ver_todos_processos = self.wait_for_element_to_click(
                Main.FILTROATRIBUICAO)

            if ver_todos_processos.text == 'Ver todos os processos':
                ver_todos_processos.click()
        except:

            print("Ocorreu algum erro na Visualização dos Processos")

        # Verifica se está na visualização detalhada senão muda para ela
        try:
            visualizacao_detalhada = self.wait_for_element_to_click(
                Main.TIPOVISUALIZACAO)

            if visualizacao_detalhada.text == 'Visualização detalhada':
                visualizacao_detalhada.click()

        except:
            print("Falha na visualização detalhada dos processos")

    def isPaginaInicial(self):
        return self.get_title() == 'SEI - Controle de Processos'

    def go_to_initial_page(self):
        self.wait_for_element_to_click(
            Base.INITIALPAGE).click()

    def exibir_menu_lateral(self):

        menu = self.wait_for_element(Base.EXIBIRMENU)

        if menu.get_attribute("title") == "Exibir Menu do Sistema":
            menu.click()

    def lista_processos(self):

        processos = []

        if not self.isPaginaInicial():
            self.go_to_initial_page()

        contador = Select(self.wait_for_element(Main.CONTADOR))

        pages = [pag.text for pag in contador.options]

        for pag in pages:

            contador = Select(self.wait_for_element(Main.CONTADOR))
            contador.select_by_visible_text(pag)
            html_sei = soup(driver.page_source, "lxml")
            processos += html_sei("tr", {"class": 'infraTrClara'})

        return processos

    def go_to_blocos(self):
        self.exibir_menu_lateral()
        self.wait_for_element(LatMenu.BLOCOASS).click()

    def exibir_bloco(self, numero):

        if self.get_title() != ListaBlocos.TITLE:
            self.go_to_blocos()

        try:
            self.wait_for_element((By.LINK_TEXT, str(numero))).click()

        except NoSuchElementException:
            print("O Bloco de Assinatura informado não existe ou está \
                  concluído!")

    def armazena_bloco(self, numero):

        if self.get_title() != Bloco.TITLE + " " + str(numero):

            self.exibir_bloco(numero)

        html_bloco = soup(driver.page_source, "lxml")
        linhas = html_bloco.find_all("tr", class_=['infraTrClara', 'infraTrEscura'])

        chaves = ['checkbox', 'seq', "processo", 'documento', 'data', 'tipo',
                  'assinatura', 'anotacoes', 'acoes']

        lista_processos = []

        for linha in linhas:
            
            proc = {k: None for k in chaves}

            cols = [v for v in linha.contents if v != "\n"]
            
            #proc['checkbox'] = linha("a", class_="infraCheckbox")
            
            #proc['seq'] = linha.
            
            assert len(chaves) == len(cols), "Verifique as linhas do bloco!"
                        
            for k, v in zip(chaves, cols):

                proc[k] = v

            lista_processos.append(proc)

        return lista_processos

    
      
    
    def expedir_bloco(self, numero):


        processos = self.armazena_bloco(numero)

        for p in processos:

            if podeExpedir(p):

                proc = p['processo'].a.string
                
                num_doc = p['documento'].a.string

                link = Base.NAV_URL + p['processo'].a.attrs['href'] 

                self.expedir_oficio(proc, num_doc, link)               
                

    def expedir_oficio(self, proc, num_doc, link):
        
        # Guarda o link para abrir o processo
        #elem = self.wait_for_element_to_click((By.LINK_TEXT, proc))

        (main_window, proc_window) = navigate_link_to_new_window(self.driver, link)
        
        info = self.info_oficio(num_doc) 
        
        self.driver.switch_to_window(proc_window)
                            
        buttons = self.acoes_oficio()
            
        self.atualiza_andamento(buttons, info)
        
        self.enviar_processo_sede(buttons)
        
        self.driver.close()
        
        self.driver.switch_to_window(main_window)
            
        
        
    def enviar_processo_sede(self, buttons): 
        
        with self.wait_for_page_load():
        
            assert self.get_title() == Processo.TITLE, \
            "Erro ao navegar para o processo"
        
            enviar = buttons[3]
            
            link = Base.NAV_URL + enviar.attrs["href"]
            
            (proc_window, new_window) = navigate_link_to_new_window(self.driver, link)        
            
            self.driver.execute_script(Envio.LUPA)
            
        with self.wait_for_page_load():
            
            # Guarda as janelas do navegador presentes
            windows = driver.window_handles
    
            # Troca o foco do navegador
            self.driver.switch_to_window(windows[-1])
            
        assert self.get_title() == Envio.TITLE, \
        "Erro ao navegar para as unidades de tramitação"
                                
        unidade = self.wait_for_element(Envio.IDSIGLA)
        
        unidade.clear()
            
        unidade.send_keys(Envio.SIGLASEDE + Keys.RETURN)
        
        sede = self.wait_for_element(Envio.IDSEDE)
        
        assert sede.get_attribute("title") == Envio.TXTSEDE, \
        "Erro ao selecionar a Unidade Protocolo.Sede para envio"
        
        sede.click()
        
        self.wait_for_element_to_click(Envio.TRSP).click()
        
        self.driver.close()
        
        # Troca o foco do navegador
        self.driver.switch_to_window(new_window)
        
        self.wait_for_element_to_click(Envio.MANTERABERTO).click()
                
        self.wait_for_element_to_click(Envio.RETDIAS).click()
                
        prazo = self.wait_for_element(Envio.NUMDIAS)
        
        prazo.clear()
        
        prazo.send_keys(Envio.PRAZO)
        
        self.wait_for_element_to_click(Envio.UTEIS).click()
        
        self.wait_for_element_to_click(Envio.ENVIAR).click()           
        
        
        
        
        
    def acoes_oficio(self):
        
        assert self.get_title() == Processo.TITLE, \
        "Erro ao navegar para o processo"
        
        # Switch to central frame
        self.driver.switch_to_frame("ifrVisualizacao")
        
        html_frame = soup(self.driver.page_source, "lxml")
        
        buttons = html_frame.find(id="divArvoreAcoes").contents
                
        assert len(buttons) == 17, "Erro ao guardar os botões de ação do processo"
        
        self.driver.switch_to_default_content()

        
        return buttons
                
        
        
        
        
        
    def info_oficio(self, num_doc):
        
        assert self.get_title() == Processo.TITLE, \
        "Erro ao navegar para o processo"
        
        # Switch to tree frame
        self.driver.switch_to_frame("ifrArvore")
        
        with self.wait_for_page_load():
        
            html_tree = soup(self.driver.page_source, "lxml")
            
            info = html_tree.find(title=re.compile(num_doc)).string
            
            assert info != '' , "Falha ao retornar Info do Ofício da Árvore"
            
            #return to parent frame
            self.driver.switch_to_default_content()
            
            return info
        
    def atualiza_andamento(self, buttons, info):
        
        assert self.get_title() == Processo.TITLE, \
        "Erro ao navegar para o processo"
        
        
        andamento = buttons[4]
        
        link = Base.NAV_URL + andamento.attrs['href']        
        
        (proc_window, new_window) = navigate_link_to_new_window(self.driver, link)
        
        input_and = self.wait_for_element((By.ID, "txaDescricao"))

        text = Processo.TXT_AND_PRE + info + Processo.TXT_AND_POS        
        
        input_and.send_keys(text)
        
        self.wait_for_element_to_click((By.ID, "sbmSalvar")).click()
        
        self.driver.close()
        
        self.driver.switch_to_window(proc_window)
        
        
        
        
    
    

        
        
    


def podeExpedir(p):

    t1 = p['processo'].find_all('a', class_="protocoloAberto")
        
    t2 = p['tipo'].find_all(string="Ofício")

    t3 = p['assinatura'].find_all(string=re.compile("Coordenador"))
    
    t4 = p['assinatura'].find_all(string=re.compile("Gerente"))
    
    return bool(t1) and bool(t2) and (bool(t3) or bool(t4))


def navigate_elem_to_new_window(driver, elem):
        """ Receive an instance of Page, navigate the link to a new window

            focus the driver in the new window

            return the main window and the driver focused on new window

            Assumes link is in page
        """
        # Guarda janela principal
        main_window = driver.current_window_handle

        # Abre link no elem em uma nova janela
        elem.send_keys(Keys.SHIFT + Keys.RETURN)
        
        
        # Guarda as janelas do navegador presentes
        windows = driver.window_handles

        # Troca o foco do navegador
        driver.switch_to_window(windows[-1])

        return (main_window, windows[-1])
    
def navigate_link_to_new_window(driver, link):
    
    # Guarda janela principal
    main_window = driver.current_window_handle

    # Abre link no elem em uma nova janela
    #body = self.driver.find_element_by_tag_name('body')
    
    #body.send_keys(Keys.CONTROL + 'n')
    
    driver.execute_script("window.open()")
    # Guarda as janelas do navegador presentes
    windows = driver.window_handles

    # Troca o foco do navegador
    driver.switch_to_window(windows[-1])
    
    driver.get(link)
    
    return (main_window, windows[-1])


driver = webdriver.Chrome()

sei = LoginPage(driver).login('rsilva', 'Savorthemom3nts')

#sei.go_to_blocos()

# sei.exibir_bloco(68049)

# bloco = sei.armazena_bloco(69745)

sei.expedir_bloco(70668)

#sei.expedir_bloco(68757)

# sei.expand_visual()

# processos = sei.lista_processos()

# sei.exibir_menu_lateral()
