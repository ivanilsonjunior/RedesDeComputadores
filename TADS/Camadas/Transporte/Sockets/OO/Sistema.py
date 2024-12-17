import psutil
import webbrowser
import socket
import struct
import re


class IPNetwork:
    def __init__(self, ip1, ip2, mask_bits):
        """Inicializa a classe com dois IPs e o número de bits da máscara de rede."""
        # Verificar a validade dos IPs e da máscara
        if not self.is_valid_ip(ip1) or not self.is_valid_ip(ip2):
            raise ValueError("Um ou mais IPs estão em formato inválido.")
        if not self.is_valid_mask(mask_bits):
            raise ValueError("A máscara de rede deve ser um número entre 0 e 32.")
        
        self.ip1 = ip1
        self.ip2 = ip2
        self.mask_bits = mask_bits
        self.mask_int = self.netmask_to_int(mask_bits)
        self.ip1_int = self.ip_to_int(ip1)
        self.ip2_int = self.ip_to_int(ip2)

    def ip_to_int(self, ip):
        """Converte um IP em formato xxx.xxx.xxx.xxx para um número inteiro."""
        return struct.unpack("!I", socket.inet_aton(ip))[0]

    def netmask_to_int(self, mask_bits):
        """Converte a quantidade de bits da máscara para o formato inteiro de máscara."""
        return (2**32 - 1) << (32 - int(mask_bits)) & 0xFFFFFFFF

    def check_same_network(self):
        """Verifica se os dois IPs estão na mesma rede, dado o número de bits da máscara."""
        network_ip1 = self.ip1_int & self.mask_int
        network_ip2 = self.ip2_int & self.mask_int
        return network_ip1 == network_ip2

    def is_valid_ip(self, ip):
        """Verifica se o IP está no formato xxx.xxx.xxx.xxx e se cada octeto é válido."""
        regex = r"^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"
        return re.match(regex, ip) is not None

    def is_valid_mask(self, mask_bits):
        """Verifica se a máscara de rede é um número inteiro entre 0 e 32."""
        try:
            mask_bits = int(mask_bits)
            return 0 <= mask_bits <= 32
        except ValueError:
            return False


class Sistema:
    def __init__(self) -> None:
        pass
    def comando(self,cmd) -> str:
        match cmd.split( )[0]:
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
            case "/ip":
                _, ip1, ip2, mask = cmd.split()
                mask_bits = mask.strip("/")  # Retirar a barra da máscara
                try:
                    ip_network = IPNetwork(ip1, ip2, mask_bits)
                    return ip_network.check_same_network()
                except ValueError as e:
                    return str(e)
            case _:
                return "Opção Inválida"