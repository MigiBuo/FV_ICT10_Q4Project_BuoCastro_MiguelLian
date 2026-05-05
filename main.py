from js import document #type: ignore

class Classmate:
    def __init__(self, name, section, favorite_subject):
        self.name = name
        self.section = section
        self.favorite_subject = favorite_subject

    def introduce(self):
        return f"Hello! I'm {self.name}, a student from {self.section}. My favorite subject is {self.favorite_subject}."

classmates = [
    Classmate("Arabella", "Emerald", "SS"),
    Classmate("Rycob", "Sapphire", "ICT"),
    Classmate("Emille", "Ruby", "Math"),
    Classmate("Lian", "Topaz", "Music and Arts"),
    Classmate("Miguel", "Emerald", "Science"),
]

def get_input(id):
    return document.getElementById(id).value.strip()

def show_introductions(event=None):

    if event is not None:
        event.preventDefault()
    output = document.getElementById("output")
    message = document.getElementById("message")

    cards = [
        f"<p class='intro-card'>{classmate.introduce()}</p>"
        for classmate in classmates 
    ]
    output.innerHTML = "".join(cards)
    message.innerText = "Classmate list refreshed."

def add_classmate(event=None):
    name = get_input("name")
    section = get_input("section")
    favorite_subject = get_input("favorite_subject")
    message = document.getElementById("message")

    if not (name and section and favorite_subject):
        message.innerText = "Please fill in every field."
        return

    classmates.append(Classmate(name, section, favorite_subject))
    message.innerText = "Classmate added. Click Show List to view the updated list."

    for field in ("name", "section", "favorite_subject"):
        document.getElementById(field).value = ""

def show_intro(event=None):
    show_introductions(event)
