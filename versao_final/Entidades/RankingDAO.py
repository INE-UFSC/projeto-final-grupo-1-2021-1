from Entidades.DAO import DAO

class RankingDAO(DAO):
    # Borg Pattern, para mais informações: https://code.activestate.com/recipes/66531/
    __estado_compatilhado = {}
    def __init__(self):
      self.__dict__ = self.__estado_compatilhado
      super().__init__("ranking.pkl")

    def add_tempo(self, tempo):
      recordes = self.ranking()

      if len(recordes) < 5:
        super().add(tempo)
      else:
        recordes.append(tempo)
        recordes.sort()
        super().resetarCache(recordes[:5])

    def ranking(self):
        rank = super().get_all()
        rank.sort()
        return rank