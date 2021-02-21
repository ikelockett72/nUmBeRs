import inflect
from classes import WordNumber
engine = inflect.engine()
makeNumberWord = engine.number_to_words

for i in range(1000):
    num = makeNumberWord(i).replace(" ", "").replace("-","")
    try:
        exec(f"globals()[num] = WordNumber(num)", globals())
    except KeyError:
        print(f"NotImplementedError: The number {num} is not yet implemented. Please keep updating for new numbers")
