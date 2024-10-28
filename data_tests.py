import data

import unittest

import hw1
# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 1
    def test_vowel_count(self):
        word1 = "Call me Ishmal"
        word2 = "ABCDEFGHIJKLMNopqrstuvwxyz"
        self.assertAlmostEqual(hw1.vowel_count(word1), 4)
        self.assertAlmostEqual(hw1.vowel_count(word2), 5)

    # Part 2
    def test_short_lists(self):
        list1 = [[4, 2], [4, 2, 4, 2], [5, 7], [7, 0, 3]]
        list2 = [[3,8,5],[4,24], [5,75], [72,0,34]]
        self.assertEqual(hw1.short_lists(list1), [[4,2], [5,7]])
        self.assertEqual(hw1.short_lists(list2), [[4,24], [5,75]])

    # Part 3
    def test_ascending_pairs(self):
        list1 = [[41, 2], [45, 2, 42, 2], [51, 30], [70, 71], [1, 2, 3, 4]]
        list2 = [[27,25],[2,42],[51,30],[70,71],[11,24,31,44]]
        self.assertEqual(hw1.ascending_pairs(list1), [[2,41], [45, 2, 42, 2], [30,51], [70,71], [1, 2, 3, 4]])
        self.assertEqual(hw1.ascending_pairs(list2), [[25, 27], [2, 42], [30, 51], [70, 71], [11, 24, 31, 44]])

    # Part 4
    def test_add_prices(self):
        price1 = data.Price(120, 22)
        price2 = data.Price(200, 88)
        price3 = data.Price(181, 99)
        price4 = data.Price(242, 1)
        self.assertEqual(hw1.add_prices(price1, price2), data.Price(321, 10))
        self.assertEqual(hw1.add_prices(price3, price4), data.Price(424, 0))

    # Part 5
    def test_rectangle_area(self):
        Point1 = data.Point(4, 2)
        Point2 = data.Point(0, 4)
        Point3 = data.Point(3, -2)
        Point4 = data.Point(-5, 8)
        Rectangle1 = data.Rectangle(Point1, Point2)
        Rectangle2 = data.Rectangle(Point3, Point4)
        self.assertEqual(hw1.rectangle_area(Rectangle1), 8)
        self.assertEqual(hw1.rectangle_area(Rectangle2), 80)

    # Part 6
    def test_books_by_author(self):
        author = "Steven King"
        Book1 = data.Book("Steven King", "The Shining")
        Book2 = data.Book("Steven King", "Salem's Lot")
        Book3 = data.Book("Leo Tolstoy", "War and Peace")
        Book4 = data.Book("Charles Dickens", "David Copperfield")
        Book5 = data.Book("Steven King", "It")
        Book6 = data.Book("Mary Shelley", "Frankenstein")
        Book7 = data.Book("Charles Dickens", "A Christmas Carol")
        Book8 = data.Book("Steven King", "11/22/63")
        self.assertEqual(hw1.books_by_author("Steven King", [Book1, Book2, Book3, Book4, Book5, Book6, Book7, Book8]), ["The Shining", "Salem's Lot", "It", "11/22/63"])
        self.assertEqual(hw1.books_by_author("Charles Dickens", [Book1, Book2, Book3, Book4, Book5, Book6, Book7, Book8]), ["David Copperfield", "A Christmas Carol"])

    # Part 7
    def test_circle_bound(self):
        Point1 = data.Point(4, 2)
        Point2 = data.Point(0, 4)
        Point3 = data.Point(3, -2)
        Point4 = data.Point(-5, 8)
        Rectangle1 = data.Rectangle(Point1, Point2)
        Rectangle2 = data.Rectangle(Point3, Point4)
        self.assertAlmostEqual(hw1.circle_bound(Rectangle1).center.x, 2)
        self.assertAlmostEqual(hw1.circle_bound(Rectangle1).center.y, 3)
        self.assertAlmostEqual(hw1.circle_bound(Rectangle1).radius, 2.236067977)
        self.assertAlmostEqual(hw1.circle_bound(Rectangle2).center.x, -1)
        self.assertAlmostEqual(hw1.circle_bound(Rectangle2).center.y, 3)
        self.assertAlmostEqual(hw1.circle_bound(Rectangle2).radius, 6.403124237)

    # Part 8
def test_pay_below_average(self):
    employee1 = data.Employee("Bob", 100)
    employee2 = data.Employee("Ryan", 200)
    employee3 = data.Employee("Jack", 500)
    employee4 = data.Employee("Mike", 250)
    employee5 = data.Employee("Nathan", 150)
    employee6 = data.Employee("Oliver", 400)
    employee_list1 = [employee1, employee2, employee4, employee5]
    employee_list2 = [employee1, employee2, employee3, employee4, employee5, employee6]
    self.assertEqual(hw1.pay_below_average(employee_list1), ["Bob", "Nathan"])
    self.assertEqual(hw1.pay_below_average(employee_list2), ["Bob", "Ryan", "Mike", "Nathan"])




if __name__ == '__main__':
    unittest.main()
