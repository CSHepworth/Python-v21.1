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
        return self

    def enroll(self):
        if self.is_rewards_member == True:
            print("User already a member")
            return False
        else:
            self.is_rewards_member = True
            self.gold_card_points = 200
            return self
    def spend_points(self, amount):
        if amount > self.gold_card_points:
            print("You do not have enough points")
        else:
            self.gold_card_points -= amount
        return self

#user1
user1 = User("Cooper", "Hepworth", "cooperhepworth@hotmail.com", 25)
user1.display_info().enroll().spend_points(50).display_info()

#user2
#user2 = User("Isaac", "Clark", "isaacclark@cec.com", 32)
#user2.enroll().spend_points(80).display_info()
