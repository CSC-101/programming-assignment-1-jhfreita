import data
import math
# Write your functions for each part in the space below.

# Part 1
# The purpose of the function vowel_count is to a string of letters, such as a sentence, as the input, sort through the
# letters in the string, and return the number of letters in the string that are vowels, whether uppercase or lowercase, as the output.
def vowel_count(word:str):
    letter_list = list(word)
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    vowel_list = [i for i in letter_list if i in vowels]
    return len(vowel_list)

# Part 2
# The purpose of the function short_lists is to take a list of element lists of numbers as the input and return a new list as the output
# that consists only of the element lists that are two numbers long.
def short_lists(scroll: list):
    short_lists = [list for list in scroll if len(list) == 2]
    return short_lists

# Part 3
# The purpose of the function ascending_pairs is to take a list of element lists of numbers as the input and return the same list
# except under the condition that all the elements that were originally pairs of numbers where the second is greater than the
# first now have the greater number as the second entry, not the first. This new list of element lists is the output.
def ascending_pairs(scroll: list):
    for i in range(len(scroll)):
        if len(scroll[i]) == 2 and scroll[i][1] < scroll[i][0]:
            scroll[i] = [scroll[i][1], scroll[i][0]]
    return scroll

# Part 4
# The purpose of the function add_prices is to take two prices of class Price as the input with dollar and cent amounts
# and add them together to return an output price of the same class with a cent amount in the range of 0-99, like in real
# life, as the output.
def add_prices(price1, price2):
    dollars = price1.dollars + price2.dollars
    cents = price1.cents + price2.cents
    if cents > 99:
        cents = cents - 100
        dollars = dollars + 1
    return data.Price(dollars, cents)

# Part 5
# The purpose of the function rectangle_area is to take a rectangle specified by two corners as the input and return the
# area of the rectangle (an integer) as the output.
def rectangle_area(Rectangle):
    length = Rectangle.bottom_right.x - Rectangle.top_left.x
    width = Rectangle.top_left.y - Rectangle.bottom_right.y
    return length * width

# Part 6
# The purpose of the function books_by_author is to take a list of books of class Book and a specific author (string) as
# the input and return a list of book titles that were written by the author specified as the output.
def books_by_author(author:str, book_list:list):
    author_list = [Book.title for Book in book_list if Book.authors == author]
    return author_list
author = "Steven King"

# Part 7
# The purpose of the function circle_bound is to take a rectangle of class Rectangle (defined by two points as corners)
# as the input and return a circle of class Circle, defined by a center point and radius, as the output.
def circle_bound(Rectangle):
    length = Rectangle.bottom_right.x - Rectangle.top_left.x
    width = Rectangle.top_left.y - Rectangle.bottom_right.y
    r = 0.5 * math.sqrt(length**2 + width**2)
    c = data.Point(Rectangle.top_left.x + 0.5 * length, Rectangle.bottom_right.y + 0.5 * width)
    return data.Circle(c, r)

# Part 8
# The purpose of the function pay_below_average is to take a list of employees of class Employee as the input and return
# a list of employees who's pay rate is below that of the average employee in the list.
def pay_below_average(employee_list:list):
    sum = 0
    pay_list = [Employee.pay_rate for Employee in employee_list]
    for i in range(len(pay_list)):
        sum += pay_list[i]
    average = sum / len(pay_list)
    return [Employee.name for Employee in employee_list if Employee.pay_rate < average]
