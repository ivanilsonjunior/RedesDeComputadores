import psutil
import webbrowser

class Sistema:
    def __init__(self) -> None:
        pass
    def comando(self,cmd) -> str:
        match cmd:
            case "/help":
                return "Ajuda Requisitada: \n\t /mem para ver a memoria\n\t /off para desligar\n\t /hd espaço em disco\n\t /google abrir o navegador"
            case "/hd":
                resposta = psutil.virtual_memory()
                return str(resposta)
            case "/mem":
                resposta = psutil.disk_usage("c:\\")
                return str(resposta)
            case "/google":
                chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
                url = "https://laica.ifrn.edu.br/"
                webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
                webbrowser.get('chrome').open_new_tab(url)
                return "Abrindo Navegador"
            case _:
                return "Opção Inválida"