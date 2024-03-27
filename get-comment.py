from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import tkinter.messagebox
def init_driver():
    driver = webdriver.Chrome()
    driver.get('https://www.instagram.com/secultfor/p/C2xvd-2JCEq/')
    driver.implicitly_wait(10)
    return driver
def get_comment(driver):
    web_elements = driver.find_elements(By.XPATH, '//div[@class="_a9zr"]')
    # more_comments = driver.find_element(By.XPATH, "//*[local-name()='svg' and @arial-label='Carregar mais comentários']/*[local-name()='path']")
    more_comments = driver.find_element(By.XPATH,"/html/body/div[7]/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/div[1]/ul/div[3]/div/div/li/div/button/div/svg")
    print(more_comments.text)
    #more_comments = driver.find_element(By.XPATH,
    #                                    "//*[local-name()='svg'][3]")
    i = 1
    for element in web_elements:
        print("#" * 40)
        print(f"Comentário{i}")
        i += 1
        print(element.text)

    # if (more_comments):
    #     more_comments.click()
    #     driver.implicitly_wait(10)

try:
    get_comment(init_driver())
except:
    mensagem = "Certifique-se de estar logado no Instagram ao executar o programa!"
    tkinter.messagebox.showerror("ERRO!",mensagem)