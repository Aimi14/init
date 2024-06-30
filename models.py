class InvestmentFund:
    def __init__(self, fund_id, name, manager_name, description, nav, date_of_creation, performance):
        self.fund_id = fund_id
        self.name = name
        self.manager_name = manager_name
        self.description = description
        self.nav = nav
        self.date_of_creation = date_of_creation
        self.performance = performance

    def __repr__(self):
        return f"<InvestmentFund {self.name} managed by {self.manager_name}>"
