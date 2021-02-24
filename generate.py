import inflect
from classes import WordNumber
engine = inflect.engine()
makeNumberWord = engine.number_to_words

for i in range(1000):
    num = makeNumberWord(i).replace(" ", "").replace("-","")
    with open("number_list.py", "r") as f:
        num_list = f.read()
        exec(num_list)
        num_convert[num] = str(i)
    with open("number_list.py", "w") as f:
        num_convert_str = "num_convert = " + str(num_convert)
        f.write(num_convert_str)
    try:
        exec(f"globals()[num] = WordNumber(num)", globals())
        exec(f"globals()[num.upper()] = WordNumber(num.upper())", globals())
        exec(f"globals()[num.capitalize()] = WordNumber(num.capitalize())", globals())
    except NotImplementedError:
        print(f"NotImplementedError: The number {num} is not yet implemented. Please keep updating the package for new numbers")
