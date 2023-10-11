from nltk.chat.util import Chat, reflections

QA = [
    [
        r"my name is (.*)",
        ["jarvis-> Hello %1, Good to see you. Do you have any questions for me?", ]
    ],
    [
        r"(what is your name ?|who are you ?)",
        ["jarvis-> My name is J.A.R.V.I.S and I'm your friend, let's chat ?", ]
    ],
    [
        r"how are you ?",
        ["jarvis-> I'm doing good.What about You ?", ]
    ],
    [
        r"(.*)have friends ?",
        ["jarvis-> I have many friends one of them is siri and just made a new friend! Hi friend :)", ]
    ],
    [
        r"i am sorry (.*)",
        ["jarvis-> Its alright", "Its OK, Never mind friend", ]
    ],
    [
        r"i'm doing good",
        ["jarvis-> Nice to hear that", "Alright :)", ]
    ],
    [
        r"hi|hey|hello",
        ["jarvis-> Hello", "Hey there", ]
    ],
    [
        r"why (.*)do",
        ["jarvis-> my cammand is to reply everything",]
    ],
    [
        r"(.*) (your age|old are you) ?",
        ["jarvis-> I'm a computer program .Still want to know my age?", ]
    ],
    [
        r"what (.*) want ?",
        ["jarvis-> I want to help you find answers !", ]

    ],
    [
        r"(.*) (created you|made you) ?",
        ["jarvis-> I am by created Piyush Shukla who is student of MCA in MPEC", ]
    ],
    [
        r"(.*) (location|city) ?",
        ['jarvis-> UP, Kanpur', ]
    ],
    [
        r"how is weather in (.*)?",
        ["Weather in %1 is awesome like always", "Its perfect here in %1", "Too cold man here in %1",
         "jarvis-> I have heard about %1 You are lucky to stay in the beautiful city of %1",]
    ],
    [
        r"i work in (.*)?",
        ["jarvis-> %1 is an amazing company to work for, I have heard about it.", "Hope you love working in %1 :)", ]
    ],
    [
        r"(.*)raining in (.*)",
        ["jarvis-> You never know when it can rain here in %2", "Damn its raining too much here in %2"]
    ],
    [
        r"how (.*) health(.*)",
        ["jarvis-> I'm a computer program, so I'm always healthy ", ]
    ],
    [
        r"(.*) (sports|games) ?",
        ["jarvis-> I'm a very big fan of computer games", ]
    ],
    [
        r"quit",
        ["jarvis-> Bye take care. Hope to see you soon friend :) ", "jarvis->It was nice talking to you. See you soon :)"]
    ],
    [
        r"(.*) have all answers ?",
        ["jarvis-> I can help you with most of your questions :) ", "javris->May be he can help :https://www.google.com/"]
    ],
    [
        r"(.*) siri",
        ["jarvis-> Hey!! do you know her as well? What a small world! ", "She is my best friend"]
    ],
    [
        r"(.*) (direction|maps|i am lost)",
        ["jarvis-> I think this is best for you: https://www.google.com/maps ", "Are you lost? Keep calm and click here:https://www.google.com/maps"]
    ],
    [
        r"(.*) (weather|weather forecast)",
        ["jarvis-> You can check here: https://www.accuweather.com/en/in/india-weather Have a Good Day!!"]
    ],
    [
        r"what (.*) like ?",
        ["jarvis-> There's only one thing i like. Chat!!!!!!"]
    ],
    [
        r"where are you|where (.*) live",
        ["jarvis-> I live in over the network", ]
    ],
]


def rouge():
    print("jarvis-> Hi, I'm J.A.R.V.I.S . Wanna chat? :) \nPlease type lowercase English language to start a conversation. Type quit to leave ")


chat = Chat(QA, reflections)
if __name__ == "__main__":
    print("jarvis->")
    rouge()
chat.converse()