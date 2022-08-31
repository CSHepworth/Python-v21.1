class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0

    def display_info(self):
        details = self.__dict__
        for key in details:
            print(details[key])

    def enroll(self):
        if self.is_rewards_member == True:
            print("User already a member")
            return False
        else:
            self.is_rewards_member = True
            self.gold_card_points = 200
    def spend_points(self, amount):
        if amount > self.gold_card_points:
            print("You do not have enough points")
        else:
            self.gold_card_points -= amount

#user1
user1 = User("Cooper", "Hepworth", "cooperhepworth@hotmail.com", 25)
user1.display_info()
user1.enroll()
user1.spend_points(50)
print(user1.gold_card_points)
user1.enroll()

#user2
user2 = User("Isaac", "Clark", "isaacclark@cec.com", 32)
user2.enroll()
user2.spend_points(80)
user2.display_info()