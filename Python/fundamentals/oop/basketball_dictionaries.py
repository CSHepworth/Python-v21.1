# Player class with updated constructor
class Player:
    def __init__(self, data):
        self.name = data['name']
        self.age = data['age']
        self.position = data['position']
        self.team = data['team']
    

kevin = {"name": "Kevin Durant", "age":34, "position": "small forward", "team": "Brooklyn Nets"}
jason = {"name": "Jason Tatum", "age":24, "position": "small forward", "team": "Boston Celtics"}
kyrie = {"name": "Kyrie Irving", "age":32, "position": "Point Guard", "team": "Brooklyn Nets"}
damian = {"name": "Damian Lillard", "age":33, "position": "Point Guard", "team": "Portland Trailblazers"}
joel = {"name": "Joel Embiid", "age":32, "position": "Power Forward", "team": "Philidelphia 76ers"}
demar = {"name": "DeMar DeRozan", "age":32, "position": "Shooting Guard", "team": "Chicago Bulls"}
    
player_kevin = Player(kevin)
player_jason = Player(jason)
player_kyrie = Player(kyrie)
player_damian = Player(damian)
player_joel = Player(joel)
player_demar = Player(demar)

print(player_jason)
print(player_kevin)
print(player_kyrie)
print(player_damian)
print(player_joel)
print(player_demar)
