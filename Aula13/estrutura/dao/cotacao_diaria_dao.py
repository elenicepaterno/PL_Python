from dao.base_dao import BaseDao
from model.cotacao_diaria import CotacaoDiaria

class CotacaoDiariaDao(BaseDao):
    def __init__(self):
        self.model = CotacaoDiaria
        super().__init__(self.model)

    def list_pl(self):
        lista_pl = self.list_all()

        for n in lista_pl:
            n.pl = n.valor_fechamento / n.lpa        
        
        lista_ordenada = sorted(lista_pl, key = self.model.get_pl)

        return lista_ordenada