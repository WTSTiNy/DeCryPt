import requests, os, threading, logging, time, random
from colorama import Fore

def http(DeCryPt_HTTP):
  while True:
    http_proxies = requests.get("https://gimmeproxy.com/api/getProxy?curl=false&protocal=http=true&ipPort=true").text
    http_proxy = str(http_proxies)
    if http_proxy == "Rate limited.":
      logging.info(f"{Fore.CYAN}|| {Fore.RESET}{Fore.BLUE}[{Fore.RESET}{Fore.MAGENTA}-{Fore.RESET}{Fore.BLUE}] Scrape Failed {Fore.RESET}{Fore.CYAN}|| [{Fore.RESET}{Fore.MAGENTA}!{Fore.RESET}{Fore.CYAN}] Trying again...")
    elif http_proxy == "Internal Server Error":
      logging.info(f"{Fore.CYAN}|| {Fore.RESET}{Fore.BLUE}[{Fore.RESET}{Fore.MAGENTA}-{Fore.RESET}{Fore.BLUE}] Scrape Failed {Fore.RESET}{Fore.CYAN}|| [{Fore.RESET}{Fore.MAGENTA}!{Fore.RESET}{Fore.CYAN}] Trying again...")
    else:
      scraped_http_proxies = open(f"Proxy Scraper by DeCryPt/http.txt", "a")
      scraped_http_proxies.write(f"{http_proxy}\n")
      logging.info(f"{Fore.MAGENTA}|| {Fore.RESET}{Fore.CYAN}{Fore.RESET}{Fore.BLUE}[{Fore.RESET}{Fore.MAGENTA}+{Fore.MAGENTA}{Fore.RESET}{Fore.BLUE}]{Fore.BLUE} Scraped HTTP Proxy{Fore.RESET} {Fore.MAGENTA}||{Fore.RESET} {Fore.BLUE}Proxy Scraper by DeCryPt{Fore.RESET}")
    
def https(DeCryPt_HTTPS):
  while True:
    https_proxies = requests.get("https://gimmeproxy.com/api/getProxy?curl=false&supportsHttps=true&ipPort=true").text
    https_proxy = str(https_proxies)
    if https_proxy == "Rate limited.":
      logging.info(f"{Fore.CYAN}|| {Fore.RESET}{Fore.BLUE}[{Fore.RESET}{Fore.MAGENTA}-{Fore.RESET}{Fore.BLUE}] Scrape Failed {Fore.RESET}{Fore.CYAN}|| [{Fore.RESET}{Fore.MAGENTA}!{Fore.RESET}{Fore.CYAN}] Trying again...")
    elif https_proxy == "Internal Server Error":
      logging.info(f"{Fore.CYAN}|| {Fore.RESET}{Fore.BLUE}[{Fore.RESET}{Fore.MAGENTA}-{Fore.RESET}{Fore.BLUE}] Scrape Failed {Fore.RESET}{Fore.CYAN}|| [{Fore.RESET}{Fore.MAGENTA}!{Fore.RESET}{Fore.CYAN}] Trying again...")
    else:
      scraped_https_proxies = open(f"Proxy Scraper by DeCryPt/https.txt", "a")
      scraped_https_proxies.write(f"{https_proxy}\n")
      logging.info(f"{Fore.MAGENTA}|| {Fore.RESET}{Fore.CYAN}{Fore.RESET}{Fore.BLUE}[{Fore.RESET}{Fore.MAGENTA}+{Fore.MAGENTA}{Fore.RESET}{Fore.BLUE}]{Fore.BLUE} Scraped HTTPS Proxy{Fore.RESET} {Fore.MAGENTA}||{Fore.RESET} {Fore.BLUE}Proxy Scraper by DeCryPt{Fore.RESET}")

def socks4(DeCryPt_SOCKS4):
  while True:
    socks4_proxies = requests.get("https://gimmeproxy.com/api/getProxy?curl=false&protocal=socks4=true&ipPort=true").text
    socks4_proxy = str(socks4_proxies)
    if socks4_proxy == "Rate limited.":
      logging.info(f"{Fore.CYAN}|| {Fore.RESET}{Fore.BLUE}[{Fore.RESET}{Fore.MAGENTA}-{Fore.RESET}{Fore.BLUE}] Scrape Failed {Fore.RESET}{Fore.CYAN}|| [{Fore.RESET}{Fore.MAGENTA}!{Fore.RESET}{Fore.CYAN}] Trying again...")
    elif socks4_proxy == "Internal Server Error":
      logging.info(f"{Fore.CYAN}|| {Fore.RESET}{Fore.BLUE}[{Fore.RESET}{Fore.MAGENTA}-{Fore.RESET}{Fore.BLUE}] Scrape Failed {Fore.RESET}{Fore.CYAN}|| [{Fore.RESET}{Fore.MAGENTA}!{Fore.RESET}{Fore.CYAN}] Trying again...")
    else:
      scraped_socks4_proxies = open(f"Proxy Scraper by DeCryPt/socks4.txt", "a")
      scraped_socks4_proxies.write(f"{socks4_proxy}\n")
      logging.info(f"{Fore.MAGENTA}|| {Fore.RESET}{Fore.CYAN}{Fore.RESET}{Fore.BLUE}[{Fore.RESET}{Fore.MAGENTA}+{Fore.MAGENTA}{Fore.RESET}{Fore.BLUE}]{Fore.BLUE} Scraped SOCKS4 Proxy{Fore.RESET} {Fore.MAGENTA}||{Fore.RESET} {Fore.BLUE}Proxy Scraper by DeCryPt{Fore.RESET}")

def socks5(DeCryPt_SOCKS5):
  while True:
    socks5_proxies = requests.get("https://gimmeproxy.com/api/getProxy?curl=false&protocal=socks5=true&ipPort=true").text
    socks5_proxy = str(socks5_proxies)
    if socks5_proxy == "Rate limited.":
      logging.info(f"{Fore.CYAN}|| {Fore.RESET}{Fore.BLUE}[{Fore.RESET}{Fore.MAGENTA}-{Fore.RESET}{Fore.BLUE}] Scrape Failed {Fore.RESET}{Fore.CYAN}|| [{Fore.RESET}{Fore.MAGENTA}!{Fore.RESET}{Fore.CYAN}] Trying again...")
    elif socks5_proxy == "Internal Server Error":
      logging.info(f"{Fore.CYAN}|| {Fore.RESET}{Fore.BLUE}[{Fore.RESET}{Fore.MAGENTA}-{Fore.RESET}{Fore.BLUE}] Scrape Failed {Fore.RESET}{Fore.CYAN}|| [{Fore.RESET}{Fore.MAGENTA}!{Fore.RESET}{Fore.CYAN}] Trying again...")
    else:
      scraped_socks5_proxies = open(f"Proxy Scraper by DeCryPt/socks5.txt", "a")
      scraped_socks5_proxies.write(f"{socks5_proxy}\n")
      logging.info(f"{Fore.MAGENTA}|| {Fore.RESET}{Fore.CYAN}{Fore.RESET}{Fore.BLUE}[{Fore.RESET}{Fore.MAGENTA}+{Fore.MAGENTA}{Fore.RESET}{Fore.BLUE}]{Fore.BLUE} Scraped SOCKS5 Proxy {Fore.RESET} {Fore.MAGENTA}||{Fore.RESET} {Fore.BLUE}Proxy Scraper by DeCryPt{Fore.RESET}")

def DeCryPt_X(DeCryPt_ERA):
  while True:
    http_proxies = requests.get("https://gimmeproxy.com/api/getProxy?curl=false&protocal=http=true&ipPort=true").text
    http_proxy = str(http_proxies)
    if http_proxy == "Rate limited.":
      logging.info(f"{Fore.CYAN}|| {Fore.RESET}{Fore.BLUE}[{Fore.RESET}{Fore.MAGENTA}-{Fore.RESET}{Fore.BLUE}] Scrape Failed {Fore.RESET}{Fore.CYAN}|| [{Fore.RESET}{Fore.MAGENTA}!{Fore.RESET}{Fore.CYAN}] Trying again...")
    elif http_proxy == "Internal Server Error":
      logging.info(f"{Fore.CYAN}|| {Fore.RESET}{Fore.BLUE}[{Fore.RESET}{Fore.MAGENTA}-{Fore.RESET}{Fore.BLUE}] Scrape Failed {Fore.RESET}{Fore.CYAN}|| [{Fore.RESET}{Fore.MAGENTA}!{Fore.RESET}{Fore.CYAN}] Trying again...")
    else:
      scraped_http_proxies = open(f"Proxy Scraper by DeCryPt/http.txt", "a")
      scraped_http_proxies.write(f"{http_proxy}\n")
      logging.info(f"{Fore.MAGENTA}|| {Fore.RESET}{Fore.CYAN}{Fore.RESET}{Fore.BLUE}[{Fore.RESET}{Fore.MAGENTA}+{Fore.MAGENTA}{Fore.RESET}{Fore.BLUE}]{Fore.BLUE} Scraped HTTP Proxy{Fore.RESET} {Fore.MAGENTA}||{Fore.RESET} {Fore.BLUE}Proxy Scraper by DeCryPt{Fore.RESET}")
    https_proxies = requests.get("https://gimmeproxy.com/api/getProxy?curl=false&supportsHttps=true&ipPort=true").text
    https_proxy = str(https_proxies)
    if https_proxy == "Rate limited.":
        logging.info(f"{Fore.CYAN}|| {Fore.RESET}{Fore.BLUE}[{Fore.RESET}{Fore.MAGENTA}-{Fore.RESET}{Fore.BLUE}] Scrape Failed {Fore.RESET}{Fore.CYAN}|| [{Fore.RESET}{Fore.MAGENTA}!{Fore.RESET}{Fore.CYAN}] Trying again...")
    elif https_proxy == "Internal Server Error":
        logging.info(f"{Fore.CYAN}|| {Fore.RESET}{Fore.BLUE}[{Fore.RESET}{Fore.MAGENTA}-{Fore.RESET}{Fore.BLUE}] Scrape Failed {Fore.RESET}{Fore.CYAN}|| [{Fore.RESET}{Fore.MAGENTA}!{Fore.RESET}{Fore.CYAN}] Trying again...")
    else:
      scraped_https_proxies = open(f"Proxy Scraper by DeCryPt/https.txt", "a")
      scraped_https_proxies.write(f"{https_proxy}\n")
      logging.info(f"{Fore.MAGENTA}|| {Fore.RESET}{Fore.CYAN}{Fore.RESET}{Fore.BLUE}[{Fore.RESET}{Fore.MAGENTA}+{Fore.MAGENTA}{Fore.RESET}{Fore.BLUE}]{Fore.BLUE} Scraped HTTPS Proxy{Fore.RESET} {Fore.MAGENTA}||{Fore.RESET} {Fore.BLUE}Proxy Scraper by DeCryPt{Fore.RESET}")
    socks4_proxies = requests.get("https://gimmeproxy.com/api/getProxy?curl=false&protocal=socks4=true&ipPort=true").text
    socks4_proxy = str(socks4_proxies)
    if socks4_proxy == "Rate limited.":
        logging.info(f"{Fore.CYAN}|| {Fore.RESET}{Fore.BLUE}[{Fore.RESET}{Fore.MAGENTA}-{Fore.RESET}{Fore.BLUE}] Scrape Failed {Fore.RESET}{Fore.CYAN}|| [{Fore.RESET}{Fore.MAGENTA}!{Fore.RESET}{Fore.CYAN}] Trying again...")
    elif socks4_proxy == "Internal Server Error":
        logging.info(f"{Fore.CYAN}|| {Fore.RESET}{Fore.BLUE}[{Fore.RESET}{Fore.MAGENTA}-{Fore.RESET}{Fore.BLUE}] Scrape Failed {Fore.RESET}{Fore.CYAN}|| [{Fore.RESET}{Fore.MAGENTA}!{Fore.RESET}{Fore.CYAN}] Trying again...")
    else:
      scraped_socks4_proxies = open(f"Proxy Scraper by DeCryPt/socks4.txt", "a")
      scraped_socks4_proxies.write(f"{socks4_proxy}\n")
      logging.info(f"{Fore.MAGENTA}|| {Fore.RESET}{Fore.CYAN}{Fore.RESET}{Fore.BLUE}[{Fore.RESET}{Fore.MAGENTA}+{Fore.MAGENTA}{Fore.RESET}{Fore.BLUE}]{Fore.BLUE} Scraped SOCKS4 Proxy{Fore.RESET} {Fore.MAGENTA}||{Fore.RESET} {Fore.BLUE}Proxy Scraper by DeCryPt{Fore.RESET}")
    socks5_proxies = requests.get("https://gimmeproxy.com/api/getProxy?curl=false&protocal=socks5=true&ipPort=true").text
    socks5_proxy = str(socks5_proxies)
    if socks5_proxy == "Rate limited.":
      logging.info(f"{Fore.CYAN}|| {Fore.RESET}{Fore.BLUE}[{Fore.RESET}{Fore.MAGENTA}-{Fore.RESET}{Fore.BLUE}] Scrape Failed {Fore.RESET}{Fore.CYAN}|| [{Fore.RESET}{Fore.MAGENTA}!{Fore.RESET}{Fore.CYAN}] Trying again...")
    elif socks5_proxy == "Internal Server Error":
      logging.info(f"{Fore.CYAN}|| {Fore.RESET}{Fore.BLUE}[{Fore.RESET}{Fore.MAGENTA}-{Fore.RESET}{Fore.BLUE}] Scrape Failed {Fore.RESET}{Fore.CYAN}|| [{Fore.RESET}{Fore.MAGENTA}!{Fore.RESET}{Fore.CYAN}] Trying again...")
    else:
      scraped_socks5_proxies = open(f"Proxy Scraper by DeCryPt/socks5.txt", "a")
      scraped_socks5_proxies.write(f"{socks5_proxy}\n")
      logging.info(f"{Fore.MAGENTA}|| {Fore.RESET}{Fore.CYAN}{Fore.RESET}{Fore.BLUE}[{Fore.RESET}{Fore.MAGENTA}+{Fore.MAGENTA}{Fore.RESET}{Fore.BLUE}]{Fore.BLUE} Scraped SOCKS5 Proxy {Fore.RESET} {Fore.MAGENTA}||{Fore.RESET} {Fore.BLUE}Proxy Scraper by DeCryPt{Fore.RESET}")

  
def exit():
  try:
    print("[+] Created by DeCryPt")
    os.system("exit")
  except:
    print("[-] Failed to Exit")

    
def directory_check():
  directory = os.getcwd()
  folder = "/Proxy Scraper by DeCryPt"
  if not os.path.isdir("".join([directory, folder])):
    print("[-] Proxy Scraping Directory Not Found")
    print("[!] Creating Proxy Scraping Directory")
    time.sleep(5)
    print("[!] Created Proxy Scraping Directory: ")
    os.mkdir("".join([directory, folder]))
    try:
      open("Proxy Scraper by DeCryPt/http.txt", "x")
      open("Proxy Scraper by DeCryPt/https.txt", "x")
      open("Proxy Scraper by DeCryPt/socks4.txt", "x")
      open("Proxy Scraper by DeCryPt/socks5.txt", "x")
    except FileExistsError:
      print("[-] Files for Proxy Scraper Were Found")
    except FileNotFoundError:
      open("Proxy Scraper by DeCryPt/http.txt", "x")
      open("Proxy Scraper by DeCryPt/https.txt", "x")
      open("Proxy Scraper by DeCryPt/socks4.txt", "x")
      open("Proxy Scraper by DeCryPt/socks5.txt", "x")
    except:
      print("[-] Finding Files Failed")

def banner_startup_mf():
  try:
    quotes = [f"""{Fore.RESET}{Fore.MAGENTA}       DeCryPt is a group of people who know how to use       {Fore.RESET}{Fore.BLUE}    ║
              {Fore.RESET}{Fore.MAGENTA}computers better than \"normal\" people               {Fore.RESET}{Fore.BLUE}║""", f"   {Fore.RESET}{Fore.MAGENTA}\"It's not how you use it, it's how you do it\" - DeCryPt{Fore.RESET}{Fore.BLUE}        ║"]
    quote = random.choice(quotes)
    print(f"{Fore.BLUE}")
    print("══════════════════════════════════════════════════════════════════╗")
    print("                                                                  ║")
    print(" '||''|.             ..|'''.|                  '||''|.    .       ║")
    print("  ||   ||    ....  .|'     '  ... ..  .... ...  ||   || .||.      ║")
    print("  ||    || .|...|| ||          ||' ''  '|.  |   ||...|'  ||       ║")
    print("  ||    || ||      '|.      .  ||       '|.|    ||       ||       ║")
    print(" .||...|'   '|...'  ''|....'  .||.       '|    .||.      '|.'     ║")
    print("                                     .. |                         ║")
    print("                                      ''                          ║")
    print("                                                                  ║")
    print(f"{quote}")
    print("                                                                  ║")
    print(f"                      {Fore.RESET}{Fore.MAGENTA}[{Fore.RESET}{Fore.CYAN}#{Fore.RESET}{Fore.MAGENTA}] Version     :{Fore.RESET}{Fore.CYAN} v1.0{Fore.RESET}{Fore.BLUE}                      ║")  
    print(f"                      {Fore.RESET}{Fore.MAGENTA}[{Fore.RESET}{Fore.CYAN}#{Fore.RESET}{Fore.MAGENTA}] Created by  : {Fore.RESET}{Fore.CYAN}TiNy & Fro$tt{Fore.RESET}{Fore.BLUE}             ║")
    print(f"                      {Fore.RESET}{Fore.MAGENTA}[{Fore.RESET}{Fore.CYAN}#{Fore.RESET}{Fore.MAGENTA}] DeCryPt     : {Fore.CYAN}#FuckTheSkidsSunday{Fore.RESET}{Fore.BLUE}       ║")
    print("                                                                  ║")
    print("╔═════════════════════════════════════════════════════════════════╝")
    print(f"{Fore.BLUE}║{Fore.RESET} {Fore.MAGENTA}[{Fore.RESET}{Fore.CYAN}D{Fore.RESET} {Fore.MAGENTA}:{Fore.RESET} {Fore.CYAN}1{Fore.RESET}{Fore.MAGENTA}]{Fore.RESET} {Fore.MAGENTA} -> {Fore.RESET}{Fore.BLUE}|| Exit Proxy Scraper{Fore.RESET}")
    print(f"{Fore.BLUE}║{Fore.RESET} {Fore.MAGENTA}[{Fore.RESET}{Fore.CYAN}e{Fore.RESET} {Fore.MAGENTA}:{Fore.RESET} {Fore.CYAN}2{Fore.MAGENTA}]{Fore.RESET} {Fore.MAGENTA} -> {Fore.RESET}{Fore.BLUE}|| Scrape HTTP Proxies{Fore.RESET}")
    print(f"{Fore.BLUE}║{Fore.RESET} {Fore.MAGENTA}[{Fore.RESET}{Fore.CYAN}C{Fore.RESET} {Fore.MAGENTA}:{Fore.RESET} {Fore.CYAN}3{Fore.RESET}{Fore.MAGENTA}]{Fore.RESET} {Fore.MAGENTA} -> {Fore.RESET}{Fore.BLUE}|| Scrape HTTPS Proxies{Fore.RESET}")
    print(f"{Fore.BLUE}║{Fore.RESET} {Fore.MAGENTA}[{Fore.RESET}{Fore.CYAN}r{Fore.RESET} {Fore.MAGENTA}:{Fore.RESET} {Fore.CYAN}4{Fore.MAGENTA}]{Fore.RESET} {Fore.MAGENTA} -> {Fore.RESET}{Fore.BLUE}|| Scrape SOCKS4 Proxies{Fore.RESET}")
    print(f"{Fore.BLUE}║{Fore.RESET} {Fore.MAGENTA}[{Fore.RESET}{Fore.CYAN}y{Fore.RESET} {Fore.MAGENTA}:{Fore.RESET} {Fore.CYAN}5{Fore.RESET}{Fore.MAGENTA}]{Fore.RESET} {Fore.MAGENTA} -> {Fore.RESET}{Fore.BLUE}|| Scrape SOCKS5 Proxies{Fore.RESET}")
    print(f"{Fore.BLUE}║{Fore.RESET} {Fore.MAGENTA}[{Fore.RESET}{Fore.CYAN}P{Fore.RESET} {Fore.MAGENTA}:{Fore.RESET} {Fore.CYAN}6{Fore.RESET}{Fore.MAGENTA}]{Fore.RESET} {Fore.MAGENTA} -> {Fore.RESET}{Fore.BLUE}|| Scrape All Types of  Proxies{Fore.RESET}")
  except KeyboardInterrupt:
    exit()

if __name__ == "__main__":
  os.system("clear")
  directory_check()   
  os.system("clear")
  format = f"{Fore.CYAN}[{Fore.RESET}{Fore.LIGHTBLUE_EX}%(asctime)s{Fore.RESET}{Fore.CYAN}]{Fore.RESET} %(message)s"
  logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")
  try:
    banner_startup_mf()
    proxy_type = input(f"{Fore.BLUE}║{Fore.RESET} {Fore.MAGENTA}[{Fore.RESET}{Fore.CYAN}t{Fore.RESET} {Fore.MAGENTA}:{Fore.RESET} {Fore.CYAN}0{Fore.RESET}{Fore.MAGENTA}]{Fore.RESET}  {Fore.MAGENTA}->{Fore.RESET} {Fore.BLUE}|| Enter A Option: {Fore.RESET}") 
    if "1" == proxy_type or "exit" == proxy_type or "EXIT" == proxy_type:
      exit()
    elif "2" == proxy_type or "http" == proxy_type or "HTTP" == proxy_type:
      print(f"{Fore.BLUE}╠══════════════════════════════════════════════════════════════════╗{Fore.RESET}") 
      print(f"{Fore.BLUE}║{Fore.RESET} {Fore.MAGENTA}[{Fore.RESET}{Fore.CYAN}${Fore.RESET} {Fore.MAGENTA}:{Fore.RESET} {Fore.CYAN}0{Fore.RESET}{Fore.MAGENTA}]{Fore.RESET} {Fore.MAGENTA} ~> {Fore.BLUE}|| [{Fore.RESET}{Fore.MAGENTA}+{Fore.RESET}{Fore.BLUE}] Selected HTTP Proxies                         ║{Fore.RESET}")
      thread_count = input(f"{Fore.BLUE}║ {Fore.RESET}{Fore.MAGENTA}[{Fore.RESET}{Fore.CYAN}${Fore.RESET}{Fore.MAGENTA} : {Fore.RESET}{Fore.CYAN}0{Fore.RESET}{Fore.MAGENTA}]  ~>{Fore.RESET} {Fore.BLUE}|| {Fore.BLUE}[{Fore.RESET}{Fore.MAGENTA}+{Fore.RESET}{Fore.BLUE}] Enter A Thread Amount: {Fore.RESET}").join("║")
      if len(thread_count) == 0:
        http_dft = threading.Thread(target=http, args=(15, ), daemon=True)
        print(f"{Fore.BLUE}╚══════════════════════════════════════════════════════════════════╝{Fore.RESET}")
        http_dft.start()
        http_dft.join()
      else:
        http_t = threading.Thread(target=http, args=(str(thread_count), ), daemon=True)
        print(f"{Fore.BLUE}╚══════════════════════════════════════════════════════════════════╝{Fore.RESET}")
        http_t.start()
        http_t.join()
    elif "3" == proxy_type or "https" == proxy_type or "HTTPS" == proxy_type:
      print(f"{Fore.BLUE}╠══════════════════════════════════════════════════════════════════╗{Fore.RESET}") 
      print(f"{Fore.BLUE}║{Fore.RESET} {Fore.MAGENTA}[{Fore.RESET}{Fore.CYAN}$ {Fore.RESET}{Fore.MAGENTA}:{Fore.RESET} {Fore.CYAN}0{Fore.RESET}{Fore.MAGENTA}]{Fore.RESET} {Fore.MAGENTA} ~> {Fore.BLUE}|| [+] Selected HTTPS Proxies                        ║{Fore.RESET}")
      thread_count = input(f"{Fore.BLUE}║ {Fore.RESET}{Fore.MAGENTA}[{Fore.RESET}{Fore.CYAN}${Fore.RESET}{Fore.MAGENTA} : {Fore.RESET}{Fore.CYAN}0{Fore.RESET}{Fore.MAGENTA}]  ~>{Fore.RESET} {Fore.BLUE}|| {Fore.BLUE}[{Fore.RESET}{Fore.MAGENTA}+{Fore.RESET}{Fore.BLUE}] Enter A Thread Amount: {Fore.RESET}").join("║")
      print(f"{Fore.BLUE}║{Fore.RESET} {Fore.MAGENTA}[{Fore.RESET}{Fore.CYAN}$ {Fore.RESET}{Fore.MAGENTA}:{Fore.RESET} {Fore.CYAN}0{Fore.RESET}{Fore.MAGENTA}]{Fore.RESET} {Fore.MAGENTA} ~> {Fore.BLUE}|| []")
      if len(thread_count) == 0:
        https_dft = threading.Thread(target=https, args=(15, ), daemon=True)
        print(f"{Fore.BLUE}╚══════════════════════════════════════════════════════════════════╝{Fore.RESET}")
        https_dft.start()
        https_dft.join()
      else:  
        https_t = threading.Thread(target=https, args=(str(thread_count), ), daemon=True)
        print(f"{Fore.BLUE}╚══════════════════════════════════════════════════════════════════╝{Fore.RESET}")
        https_t.start()
        https_t.join()
    elif "4" == proxy_type or "socks4" == proxy_type or "SOCKS4" == proxy_type:
      print(f"{Fore.BLUE}╠══════════════════════════════════════════════════════════════════╗{Fore.RESET}") 
      print(f"{Fore.BLUE}║{Fore.RESET} {Fore.MAGENTA}[{Fore.RESET}{Fore.CYAN}${Fore.RESET} {Fore.MAGENTA}:{Fore.RESET} {Fore.CYAN}0{Fore.RESET}{Fore.MAGENTA}]{Fore.RESET} {Fore.MAGENTA} ~> {Fore.BLUE}|| [+] Selected SOCKS4 Proxies                       ║{Fore.RESET}")
      thread_count = input(f"{Fore.BLUE}║ {Fore.RESET}{Fore.MAGENTA}[{Fore.RESET}{Fore.CYAN}${Fore.RESET}{Fore.MAGENTA} : {Fore.RESET}{Fore.CYAN}0{Fore.RESET}{Fore.MAGENTA}]  ~>{Fore.RESET} {Fore.BLUE}|| {Fore.BLUE}[{Fore.RESET}{Fore.MAGENTA}+{Fore.RESET}{Fore.BLUE}] Enter A Thread Amount: {Fore.RESET}").join("║")
      if len(thread_count) == 0:
        socks4_dft = threading.Thread(target=socks4, args=(15, ), daemon=True)
        print(f"{Fore.BLUE}╚══════════════════════════════════════════════════════════════════╝{Fore.RESET}")
        socks4_dft.start()
        socks4_dft.join()
      else:
        socks4_t = threading.Thread(target=socks4, args=(str(thread_count), ), daemon=True)
        print(f"{Fore.BLUE}╚══════════════════════════════════════════════════════════════════╝{Fore.RESET}")
        socks4_t.start()
        socks4_t.join()
    elif "5" == proxy_type or "socks5" == proxy_type or "SOCKS5" == proxy_type:
      print(f"{Fore.BLUE}╠══════════════════════════════════════════════════════════════════╗{Fore.RESET}") 
      print(f"{Fore.BLUE}║{Fore.RESET} {Fore.MAGENTA}[{Fore.RESET}{Fore.CYAN}${Fore.RESET} {Fore.MAGENTA}:{Fore.RESET} {Fore.CYAN}0{Fore.RESET}{Fore.MAGENTA}]{Fore.RESET} {Fore.MAGENTA} ~> {Fore.BLUE}|| [+] Selected SOCKS5 Proxies                       ║{Fore.RESET}")
      thread_count = input(f"{Fore.BLUE}║ {Fore.RESET}{Fore.MAGENTA}[{Fore.RESET}{Fore.CYAN}${Fore.RESET}{Fore.MAGENTA} : {Fore.RESET}{Fore.CYAN}0{Fore.RESET}{Fore.MAGENTA}]  ~>{Fore.RESET} {Fore.BLUE}|| {Fore.BLUE}[{Fore.RESET}{Fore.MAGENTA}+{Fore.RESET}{Fore.BLUE}] Enter A Thread Amount: {Fore.RESET}").join("║")
      if len(thread_count) == 0:
        socks5_dft = threading.Thread(target=socks5, args=(15, ), daemon=True)
        print(f"{Fore.BLUE}╚══════════════════════════════════════════════════════════════════╝{Fore.RESET}")
        socks5_dft.start()
        socks5_dft.join()
      else:
        socks5_t = threading.Thread(target=socks5, args=(str(thread_count), ), daemon=True)
        print(f"{Fore.BLUE}╚══════════════════════════════════════════════════════════════════╝{Fore.RESET}")
        socks5_t.start()
        socks5_t.join()
    elif "6" == proxy_type or "all" == proxy_type or "ALL" == proxy_type or "multiple" == proxy_type or "MULTIPLE" == proxy_type:
      print(f"{Fore.BLUE}╠══════════════════════════════════════════════════════════════════╗{Fore.RESET}") 
      print(f"{Fore.BLUE}║{Fore.RESET} {Fore.MAGENTA}[{Fore.RESET}{Fore.CYAN}${Fore.RESET} {Fore.MAGENTA}:{Fore.RESET} {Fore.CYAN}0{Fore.RESET}{Fore.MAGENTA}]{Fore.RESET} {Fore.MAGENTA} ~> {Fore.BLUE}|| [+] Selected Multiple Proxies                     ║{Fore.RESET}")
      thread_count = input(f"{Fore.BLUE}║ {Fore.RESET}{Fore.MAGENTA}[{Fore.RESET}{Fore.CYAN}${Fore.RESET}{Fore.MAGENTA} : {Fore.RESET}{Fore.CYAN}0{Fore.RESET}{Fore.MAGENTA}]  ~>{Fore.RESET} {Fore.BLUE}|| {Fore.BLUE}[{Fore.RESET}{Fore.MAGENTA}+{Fore.RESET}{Fore.BLUE}] Enter A Thread Amount: {Fore.RESET}")
      thread_count.join("║")
      if len(thread_count) == 0:
        DeCryPt_X_dft = threading.Thread(target=DeCryPt_X, args=(15, ), daemon=True)
        print(f"{Fore.BLUE}╚══════════════════════════════════════════════════════════════════╝{Fore.RESET}")
        DeCryPt_X_dft.start()
        DeCryPt_X_dft.join()
      else:
        DeCryPt_X_t = threading.Thread(target=DeCryPt_X, args=(str(thread_count), ), daemon=True)
        print(f"{Fore.BLUE}╚══════════════════════════════════════════════════════════════════╝{Fore.RESET}")
        DeCryPt_X_t.start()
        DeCryPt_X_t.join()
    else:
      exit()
  except KeyboardInterrupt:
    exit()
