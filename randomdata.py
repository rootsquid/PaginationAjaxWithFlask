import random

def GetRandomLine(fileName : str):

    with open(fileName, 'r') as file:
        lines = file.readlines()
        return random.choice(lines).strip()
        