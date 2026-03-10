import config , telebot , random

facts = [
    "Octopuses have three hearts.",
    "Bananas are technically berries.",
    "Honey never spoils.",
    "Sharks existed before trees.",
    "A group of flamingos is called a flamboyance.",
    "The Eiffel Tower can grow taller in summer.",
    "Some turtles can breathe through their butts.",
    "Dolphins have names for each other."
]

bot = telebot.TeleBot(config.token)
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, "hello")



@bot.message_handler(commands=['info'])
def send_info(message):
    bot.reply_to(message, "Available commands:\n/start\n/info")


@bot.message_handler(content_types=["photo"])
def send_photo(message):
    bot.reply_to(message,"i see")


@bot.message_handler(commands=['fact'])
def send_fact(message):
    fact = random.choice(facts)
    bot.reply_to(message, fact)

class Car:

    def __init__(self, color, brand):
        self.color = color
        self.brand = brand

    def info(self):
        return f"Car brand: {self.brand}\nColor: {self.color}"

@bot.message_handler(commands=['car'])
def create_car(message):
    args = util.extract_arguments(message.text).split()

    if len(args) < 2:
        bot.reply_to(message, "Use: /car color brand")
        return

    color = args[0]
    brand = args[1]

    car = Car(color, brand)

    bot.reply_to(message, car.info())

bot.infinity_polling()