import crypt

def testPass(cryptPass): # открывает словарь с некодированными значенями словами подготовленными для брута, читает его значения и солит слово по его первым двум буквам
	salt = cryptPass[0:2] #берет два первых значения из списка слова для соли. get two first value for salt
	dictFile = open('dictionary.txt', 'r') #открывает словарь читает из него и пишет в dictFile
	for word in dictFile.readlines(): #перебор  данных в переменную word c функцией readlines
		word = word.strip('\n') #убирает все лишнее , пробелы и тд, слэш ну типа с новой строки и заносит в переменную word
		cryptWord = crypt.crypt(word,salt) # сам процесс соления(слово - две первые буквы)
		if (cryptWord == cryptPass): # сравнивает с хэшем , если равно то 200 ОК
			print("[+] Found Password:"+word+"\n") #принтит 200 ОК
			return # ни чего не возвращает
	print("[-] Password Not Found.\n") # 400 Not Found
	return # опять ни чего не возвращает
def main(): # типа главная функция которая открывает файл с солеными паролями которые нужно расшифровать
	passFile = open('passwords.txt') # берет значения из файла и заносит их в переменную passFile
	for line in passFile.readlines(): #перебирает данные в line
		if ":" in line: # если двоеточие присутствует в лайн то
			user = line.split(':')[0] # разделяет двоеточием первым эементом списка и помещает данные в переменную юзер
			cryptPass = line.split(':')[1].strip(' ') # это кароч делит первый элемент от второго типа root:dsfsadfdas и убирает треш
 			print("[*] Cracking Password For: "+user) # тупо принтит юзера который перед двоеточием :
			testPass(cryptPass) #запускает функцию testPass
if __name__ == "__main__": #this is true
	main() # main function
