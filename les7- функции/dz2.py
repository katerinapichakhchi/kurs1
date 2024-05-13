def correct_sentence(text: str) -> str:
    if not text.endswith("."):
        text = text + "."
    return text.replace(text[0], text[0].title(), 1)


assert correct_sentence("greetings, friends") == "Greetings, friends."
assert correct_sentence("hello") == "Hello."
assert correct_sentence("Greetings. Friends") == "Greetings. Friends."
assert correct_sentence("Greetings, friends.") == "Greetings, friends."
assert correct_sentence("greetings, friends.") == "Greetings, friends."
print('ОК')
