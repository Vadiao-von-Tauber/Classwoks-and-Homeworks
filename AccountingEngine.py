from CalcEngine import CalcEngine



class AccountingEngine:
    def __init__(self):
        self.calc_engine = CalcEngine()

    def calc_se_taxes(self, income):
        se_taxes_percent = self.calc_engine.percent(income, AccountingEngine.get_se_taxes_percent_from_gov())
        return se_taxes_percent


    @staticmethod
    def get_se_taxes_percent_from_gov():
        return 16


