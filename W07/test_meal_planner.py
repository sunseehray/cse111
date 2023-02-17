import pytest
from meal_planner import write_file, append_list
import os

def test_write_file():
    """Verify that the write_file function works correctly."""
    lines = [
    "Beware of false prophets, who come to you in sheep's",
    "clothing, but inwardly they are ravening wolves. Ye",
    "shall know them by their fruits. Do men gather grapes",
    "of thorns, or figs of thistles? Even so every good tree",
    "bringeth forth good fruit; but a corrupt tree bringeth",
    "forth evil fruit. A good tree cannot bring forth evil",
    "fruit, neither a corrupt tree bring forth good fruit.",
    "Every tree that bringeth not forth good fruit is hewn",
    "down, and cast into the fire. Wherefore, by their fruits",
    "ye shall know them."
    ]
    filename = "fruits.txt"

    # Call the write_file function to
    # write a file named fruits.txt.
    write_file(filename, lines)

    # Read the contents of the fruits.txt file.
    with open(filename, "rt") as infile:

        # Read all the characters in the file into a string.
        string = infile.read()

    # Split the string into a list of strings named
    # written. Each line of text from the text file
    # will be stored in its own element in the list.
    written = string.splitlines()

    # Delete the fruits.txt file.
    os.remove(filename)

    # Verify that write_file correctly wrote the fruits.txt file.
    assert lines == written

    # test blank lines
    lines = []
    filename = "lines.txt"

    # Call the write_file function to
    # write a file named fruits.txt.
    write_file(filename, lines)

    # Read the contents of the fruits.txt file.
    with open(filename, "rt") as infile:

        # Read all the characters in the file into a string.
        string = infile.read()

    # Split the string into a list of strings named
    # written. Each line of text from the text file
    # will be stored in its own element in the list.
    written = string.splitlines()

    # Delete the fruits.txt file.
    os.remove(filename)

    # Verify that write_file correctly wrote the fruits.txt file.
    assert lines == written

def test_append_list():
    """verify that the append_list function works properly"""
    test_list = [
        "One",
        "Two",
        "Three"
    ]
    add_list = [
        "Four",
        "Five",
        "Six"
    ]

    # call the append_list function
    append_list(test_list,add_list)

    assert test_list == ["One","Two","Three","Four","Five","Six"]

    # test empty list
    empty_list = []
    add_list = [
        "add",
        "me",
        "to",
        "the",
        "empty",
        "list"
    ]

    append_list(empty_list,add_list)
    
    assert empty_list == ["add","me","to","the","empty","list"]

# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])