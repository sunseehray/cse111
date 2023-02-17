def main():
    # Create and print a list named fruit.
    fruit_list = ["pear", "banana", "apple", "mango"]
    print(f"original: {fruit_list}")

    # reverse list
    fruit_list.reverse()
    print(f"reversed: {fruit_list}")

    # append orange
    fruit_list.append("orange")
    print(f'append orange: {fruit_list}')

    # find index of apple
    i = fruit_list.index("apple")

    # replace apple with cherry
    fruit_list.insert(i, "cherry")
    print(f'insert cherry: {fruit_list}')

    # remove banana
    fruit_list.remove("banana")
    print(f'remove banana: {fruit_list}')

    # pop last element
    i = len(fruit_list) - 1
    last_element = fruit_list[i]
    fruit_list.pop()
    print(f'pop {last_element}: {fruit_list}')

    # sort list
    fruit_list.sort()
    print(f'sorted: {fruit_list}')

    # clear list
    fruit_list.clear()
    print(f'cleared: {fruit_list}')



if __name__ == "__main__":
    main()