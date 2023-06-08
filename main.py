from nltk.chat.util import Chat, reflections
import re
from random import choice

pairs = [
    (r"hi|hello|hey", ["Welcome to SYNC. How can I assist you?"]),
    (r"(.*) internship", ["We offer Android development, UI/UX Design, Machine Learning, Software development, Web development, Java, Python, React JS, and Artificial intelligence courses."]),
    (r"(.*) time", ["The duration of the course is 30 days."]),
    (r"(.*) react Js", ["React Js internship provides you the opportunity to learn how to create, build and maintain any website and apps.\n This internship will also improve your practical knowledge by doing hands-on projects."]),
    (r"(.*) artificial intelligence", ["Our Artificial intelligence internship will offer you to enhance your skills by doing real life example projects. \nThis internship will also teach you how a machine act like a human by training using Dataset."]),
    (r"(.*) machine learning", ["Our machine learning internship will offer you to enhance your skills by doing real life example projects. \nThis internship will increase your knowledge in the field of data and algorithms to understand how a machine learns"]),
    (r"(.*) java", ["Java internship will teach you how to develop android applications and software by making projects on real world problems. \nIt will also improve your basic knowledge about how to maintain java-based components and interfaces."]),
    (r"(.*) python", ["This python internship will improve your problem-solving skills by making projects on real world problems. \nIt will also improve your basic knowledge about data analytics, analysis and some python frameworks."]),
    (r"(.*) UI/UX design", ["This UX/UI internship will teach you how to create a web and mobile designs for e-Commerce web & apps. \nIt will also teach you how to take a client's business objectives and turning them into intuitive, effective designs."]),
    (r"(.*) Software development", ["Software development Internship will teach you about how to develop, test and deploy any software. It also provides .\n This internship will also improve your practical knowledge by doing hands-on projects"]),
    (r"(.*) app development", ["Android development internship helps you to learn and develop software which will be used for Android devices.\n This internship also teaches you how to build mobile apps like gaming apps, music apps, learning apps etc."]),
    (r"(.*) web development", ["Web development internship provides you the opportunity to learn how to create, build and maintain any website and apps\n. This internship will also improve your practical knowledge by doing hands-on projects."]),
    (r"(.*) (end|finished) ", ["If you perform well in your internship, we will provide you with a letter of recommendation."]),
    (r"bye|goodbye", {"Goodbye!", "Take care!"}),
]

chatbot = Chat(pairs, reflections)

# Define a function to generate a response
def generate_response(message):
    response = chatbot.respond(message)
    if response:
        return response
    else:
        return "I'm sorry, I didn't understand your question."

# Test the chatbot
while True:
    user_input = input("User: ")
    if user_input.lower() == 'bye':
        print("BotSYNC: Goodbye!")
        break
    response = generate_response(user_input)
    print("BotSYNC:", response)
