import logging
import os
from datetime import datetime

class Logger:
    def __init__(self, nome_arquivo: str = "app.log", log_dir: str = "logs", nivel=logging.INFO):
        os.makedirs(log_dir, exist_ok=True)
        caminho_log = os.path.join(log_dir, nome_arquivo)

        self.logger = logging.getLogger("SistemaBilhetagem")
        self.logger.setLevel(nivel)

        if not self.logger.handlers:
            
            arquivo_handler = logging.FileHandler(caminho_log)
            arquivo_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
            self.logger.addHandler(arquivo_handler)

            
            console_handler = logging.StreamHandler()
            console_handler.setFormatter(logging.Formatter('%(levelname)s - %(message)s'))
            self.logger.addHandler(console_handler)

    def info(self, mensagem):
        self.logger.info(mensagem)

    def warning(self, mensagem):
        self.logger.warning(mensagem)

    def error(self, mensagem):
        self.logger.error(mensagem)

    def debug(self, mensagem):
        self.logger.debug(mensagem)
