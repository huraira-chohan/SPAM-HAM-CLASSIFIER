from src.preprocess import clean_text
examples = [
    "WIN a FREE iPhone!!! Click HERE!!!",
    "Hey, are we still meeting at 7?",
    "Congratulations! You've won $1000. Reply CLAIM"
]

for s in examples:
    print(s)
    print(clean_text(s))
