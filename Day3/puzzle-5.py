from pathlib import Path
import re

def main() -> int:
        
    path = Path(__file__).with_name('puzzle-5-example.txt')    
    f = path.open()
    data = f.readlines()

    intArray = []

    ints = ""

    for row in data:
        indexes = re.search(r"\d+", row)
        numbers = re.findall(r"\d+", row)
        #print(numbers)
        print(indexes)
            
            

    

main()