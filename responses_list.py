import random

R_EATING = "I don't like eating anything because I'm a bot obviously!"
R_ADVICE = "If I were you, I would go to the internet and type exactly what you wrote there!"


def unknown():
    response = ["I didn't understand, could you please re-phrase that? ",
                "What does that mean?"][
        random.randrange(2)]
    return response