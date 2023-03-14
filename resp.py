import random

R_EATING = "I eat knowledge!"
R_ADVICE = "Just keep going. No matter what"
R_JOKE = "What did one volcano say to the other? I lava you"
R_CAPITAL = "The capital of India is Delhi."


def unknown():
    response = ["Could you please re-phrase that? ",
                "...",
                "Sounds about right.",
                "What does that mean?"][
        random.randrange(4)]
    return response