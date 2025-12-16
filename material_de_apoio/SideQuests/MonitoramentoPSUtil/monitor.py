import psutil
import time

class MonitorSistema:
    """
    Classe responsável por monitorar recursos do sistema operacional
    utilizando a biblioteca psutil.
    """

    def __init__(self, intervalo=2):
        """
        Construtor da classe.
        :param intervalo: tempo (em segundos) entre cada leitura
        """
        self.intervalo = intervalo

    def uso_cpu(self):
        """
        Retorna o uso da CPU em porcentagem.
        """
        return psutil.cpu_percent(interval=1)

    def uso_memoria(self):
        """
        Retorna o uso da memória RAM em porcentagem.
        """
        memoria = psutil.virtual_memory()
        return memoria.percent

    def uso_disco(self):
        """
        Retorna o uso do disco em porcentagem.
        """
        disco = psutil.disk_usage('/')
        return disco.percent

    def exibir_informacoes(self):
        """
        Exibe as informações coletadas no terminal.
        """
        print("=== Monitoramento do Sistema ===")
        print(f"CPU: {self.uso_cpu()}%") 
        print(f"Memória: {self.uso_memoria()}%") 
        print(f"Disco: {self.uso_disco()}%") 
        print("-" * 35)

    def iniciar(self):
        """
        Inicia o monitoramento contínuo.
        """
        while True:
            self.exibir_informacoes()
            time.sleep(self.intervalo)


if __name__ == "__main__":
    monitor = MonitorSistema(intervalo=2)
    monitor.iniciar()
