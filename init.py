#!/usr/bin/python

import sys
from os import path, getenv
from dotenv import load_dotenv
from datetime import datetime
import requests

def make_path(filename):
    return path.join(path.dirname(__file__), filename)

load_dotenv()

day = "1"
if len(sys.argv) < 2:
    day = datetime.today().strftime("%-d")
else:
    day = sys.argv[1].strip()
    
def create():
    solutions_path = make_path(f'solutions/day{day}.py')
    input_path = make_path(f'input/day{day}.txt')
    template_path = make_path(f'template.py')

    if not path.exists(make_path(solutions_path)):
        lines = []
        with open(template_path) as f:
            lines = [line.replace("day0", f"day{day}") for line in f]
        
        with open(solutions_path, "w") as f:
            f.writelines(lines)
    else:
        print("Warning: solutions file already exists. No action taken.")
        return
            
    if not path.exists(input_path):
        cookies = {
            'session': getenv('SESSION'),
        }
        headers = {}
        response = requests.get(f'https://adventofcode.com/2023/day/{day}/input', cookies=cookies, headers=headers)
        with open(input_path, "w") as f:
            f.write(response.text)     

def main():
    create()
            
if __name__ == "__main__":
    main()