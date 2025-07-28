class Results:
    def __init__(self, victories, draws, losses):
        self.victories = victories
        self.draws = draws
        self.losses = losses
class Football(Results):
    def __init__(self, victories, draws, losses):
        super().__init__(victories, draws, losses)
    
    def number_of_wins(self):
        return f'Футбольных побед: {self.victories}'
    
    def number_of_draws(self):
        return f'Футбольных ничьих: {self.draws}'
    
    def number_of_losses(self):
        return f'Футбольных поражений: {self.losses}'
    
    def total_points(self):
        self.total_points = 3*self.victories + self.draws
        return f'Общее количество очков: {self.total_points}'
    
class Hockey(Results):
    def __init__(self, victories, draws, losses):
        super().__init__(victories, draws, losses)
    
    def number_of_wins(self):
        return f'Хоккейных побед: {self.victories}'
    
    def number_of_draws(self):
        return f'Хоккейных ничьих: {self.draws}'
    
    def number_of_losses(self):
        return f'Хоккейных поражений: {self.losses}'
    
    def total_points(self):
        self.total_points = 3*self.victories + self.draws
        return f'Общее количество очков: {self.total_points}'
    
football_team = Football(victories = 2, draws = 2, losses=2)

hockey_team = Hockey(victories = 2, draws = 2, losses=2)

methods = ["number_of_wins", 
           "number_of_draws", 
           "number_of_losses", 
           "total_points"]

for method in (methods):
    method_name = getattr(football_team, method)
    print(method_name())

for method in (methods):
    method_name = getattr(hockey_team, method)
    print(method_name())