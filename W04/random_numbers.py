import random

def main():
    numbers = [16.2, 75.1, 52.3]
    words = []
    print(numbers)
    append_random_numbers(numbers)
    print(numbers)
    append_random_numbers(numbers, 2)
    print(numbers)
    append_random_words(words)
    print(words)

def append_random_numbers(numbers_list, quantity=1):
    
    for i in range(quantity):
        number = random.uniform(1,100)
        number = round(number, 1)
        numbers_list.append(number)
    
def append_random_words(words_list, quantity=1):
    words = ["dog","cat","mouse","pig","snake","cow","fly"]
    for i in range(quantity):
        word = random.choice(words)
        words_list.append(word)

if __name__ == "__main__":
    main()