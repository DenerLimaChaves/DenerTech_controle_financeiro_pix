import cv2
import pytesseract


#Ler imgagem
imagem = cv2.imread('comprovante_pix.jpeg')

#Estamos definindo o caminho do tesseract para o pytesseract, para que ele possa usar o OCR para extrair texto da imagem.
caminho = r"C:\Users\dener\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"

pytesseract.pytesseract.tesseract_cmd = caminho
#Pedir pytessact Estrair texto da imgagem 
texto = pytesseract.image_to_string(imagem)

#colocar cada linha dentro de uma posição de uma lista
linhas = texto.split('\n')

#verificar valor do pix
for linha in linhas:
    if 'R$' in linha:
        #print('Valor do Pix encontrado:', linha)
        #Separando a string ultilizando o separador R$ e atribuindo a posição 1, que contem o valor do pix. 
        VALOR_PIX = linha.split('R$')[1]
print('Valor do Pix encontrado:', VALOR_PIX)
