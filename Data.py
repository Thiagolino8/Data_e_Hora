from datetime import datetime, timedelta


class Data:
    def __init__(self):
        self._momento_do_cadastro = datetime.today()

    def __str__(self):
        return self.data_formatada()

    def mês_do_cadastro(self):
        meses_do_ano = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
        mês_do_cadastro = self._momento_do_cadastro.month
        return meses_do_ano[mês_do_cadastro - 1]

    def dia_do_cadastro(self):
        dias_da_semana = ["Domingo", "Segunda", "Terça", "Quarta", "Quinta", "Sexta"]
        dia_do_cadastro = self._momento_do_cadastro.weekday()
        return dias_da_semana[dia_do_cadastro - 1]

    def data_formatada(self):
        return self._momento_do_cadastro.strftime("%d/%m/%y %H:%M")

    def tempo_de_cadastro(self):
        return datetime.today() - self._momento_do_cadastro
