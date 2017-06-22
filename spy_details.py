from datetime import datetime

class Spy:

    def __init__(self, name, salutation, age, rating):
        self.name = name
        self.salutation = salutation
        self.age = age
        self.rating = rating
        self.is_online = True
        self.chats = []
        self.current_status_message = None


class ChatMessage:

    def __init__(self,message,sent_by_me):
        self.message = message
        self.time = datetime.now()
        self.sent_by_me = sent_by_me

spy = Spy('Churchill', 'Mr.', 24, 4.7)

ally_one = Spy('ATTLEE', 'Mr.', 33, 4.6)
ally_two = Spy('REAGAN', 'Mr.', 21, 3.8)
ally_three = Spy('Rooselvelt', 'Mr.', 29, 4.1)
ally_four = Spy('Madison', 'Mr', 35, 4.4)

allies = [ally_one, ally_two, ally_three,ally_four]

