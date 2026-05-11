import nmap;import time;import random;import ipapi;import datetime  # СКАЧАЙТЕ
END = '\033[0m'

RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
PURPLE = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'

# Стили
BOLD = '\033[1m'       # Жирный
UNDERLINE = '\033[4m'  # Подчеркнуты
def start_now():
    print(rf'''{RED}
--------------------------------------------------------------------------------------------------------
殪幢緻Iii爰曷樔黎㌢´　　｀ⅷ
艇艀裲f睚鳫巓襴骸　　　　贒憊
殪幢緻I翰儂樔黎夢'”　 　 ,ｨ傾
盥皋袍i耘蚌紕偸′　　　 雫寬I
悗f篝嚠篩i縒縡齢　　 　 Ⅷ辨f
輯駲f迯瓲i軌帶′　　　　　`守I厖孩
幢儂儼巓襴緲′　 　 　 　 　 `守枢i磬廛
嚠篩I縒縡夢'´　　　 　 　 　 　 　 `守峽f
蚌紕襴緲′　　　　　　　　　　　　　‘守畝
f瓲軌揄′　　　　　　　　　　　　　,gf毯綴
鳫襴鑿　　　　　　　　　　 　 　 奪寔f厦
絨緲′　　　　　　 　 　 　 　　　　 　 ”'罨悳
巓緲′　　　　　　 　 　 　 　 　 　 綴〟 ”'罨椁
巓登嶮 薤篝㎜㎜ g　 　 緲　 　 甯體i爺綴｡, ”'罨琥
I軌襴暹 甯幗緲fi'　　 緲',纜　　贒i綟碕碚爺綴｡ ”'罨皴
巓襴驫 霤I緲緲　　 纜穐　　甯絛跨飩i髢綴馳爺綴｡`'等誄                     
version->V1.2
K1RPIT
-------------------------------------------------------------------------------------------------------   {END}''')
                                                                  
start_now()

#sudo python3 x.py




ip_1q = [
    178,  46, 95,   # СНГ 
    212, 213, 80, 77,   # Европа/РФ  
    109,            
    82, 91, 101,         
    193, 194, 195,       
     103,    
    104, 107,  
    31, 37,     
    146, 149,   
    1, 37, 46, 77, 78, 91, 93, 94, 95, 159, 176, 178, 185, 188, 193, 194, 195, 212, 213, 217,
    45, 185, 188, 193
]

ip_1q = list(set(ip_1q))

def random_ip():
    global Q
    global R43
    R43 =datetime.datetime.now().strftime('%H:%M')
    q1=random.choice(ip_1q)
    q2 = random.randint(0, 255)
    q3 = random.randint(0, 255)
    q4= random.randint(0, 255)
    Q = f'{q1}.{q2}.{q3}.{q4}'
    print(f'[{R43}]-{Q}')



def scan_nm():
    global nm
    global ie
    nm = nmap.PortScanner()
    nm.scan(hosts=Q, arguments='-Pn -sV -p  21,22,23,80,135,137,139,445,554,1154,3389,5900,5901,5902 --open --reason --host-timeout 30s ')
    if Q in nm.all_hosts():
        status = nm[f'{Q}'].state() 
        print(F'{GREEN}[*]{END}')
        if status == 'up':
            print(f'🚀{GREEN}[+] ip {Q} OPEN{END}🚀')
            ie = ipapi.location(Q) #НОВОЯ ФУНКЦИЯ
            print(f'[*]{UNDERLINE} Локация: {ie.get("country_name")}, {ie.get("city")}{END}')
            port_c = nm[Q].all_tcp()
            print(port_c)
            if len(port_c) > 0:
                print(f'🎯{BLUE}[+|?]sheck baner and soft{END}🎯')
                for port in port_c:  
                    service = nm[Q]['tcp'][port]['name']
                    product = nm[Q]['tcp'][port]['product']
                    version = nm[Q]['tcp'][port]['version']
                    print(F'🔥{CYAN}[++++] Port: {port}\n  {service} | {product} {version}{END}🔥')
                    with open("results.txt", "a") as file:
                        file.write(f" Time:[{R43}]ip:{Q}||{ie}\n port:{port}\n {service}|||{product} {version}\n") 
                        file.write("-" * 50 + "\n")
                     
        else:       

            
            print(f'💀{RED}[-]ip {Q}CLOSE OR F{END}💀')

    else:
        print(f'{RED}[-]{END}')
     


while True:
    try:
        random_ip()
        scan_nm()
        print(f'{PURPLE}SCAN🤖🔍{END}')
        time.sleep(random.randint(9, 16))
    except nmap.PortScannerError:  
        print(f'{RED}[!]pip istall nmap and sudo apt install nmap,pls')
        break
    except KeyboardInterrupt:
        print(f'{BOLD}[пока!]{END}')
        break
