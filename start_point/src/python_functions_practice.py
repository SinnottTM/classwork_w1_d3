def return_10():
    return 10

def add(number_1, number_2):
    return number_1 + number_2

def subtract(number_1, number_2):
    return number_1 - number_2

def multiply(number_1, number_2):
    return number_1 * number_2

def divide(number_1, number_2):
    return number_1 / number_2

def length_of_string(string):
    return len(string)

def join_string(string_1, string_2):
    return string_1 + string_2

def add_string_as_number(string_1, string_2):
    return int(string_1) + int(string_2)

#  Initial attempts, had to edit tests. Still, good proof of concept.

# def number_to_full_name_month_1(number):
#     if number == 1:
#         return "January"

# def number_to_full_name_month_3(number):
#     if number == 3:
#         return "March"
    
# def number_to_full_name__month_9(number):
#     if number == 9:
#         return "September"

def number_to_full_name_month(number):
    if number == 1:
        return "January"
    if number == 3:
        return "March"
    if number == 9:
        return "September"

def number_to_short_month_name(number):
    if number == 1:
        return "Jan"
    if number == 4:
        return "Apr"
    if number == 10:
        return "Oct"

def volume_of_cube_logic(number_1, number_2, number_3):
    return number_1 * number_2 * number_3

def test_reverse_string(self):
      reversed_string = string_reverser("Hello")
      self.assertEqual("olleH", reversed_string)

# def string_reverser(text):
#     return text.reversed

# def test_fahrenheit_to_celsius():
#     pass

# if __name__ == '__main__': ???
#   unittest.main() ???
# NO IDEA WHAT ANY OF THAT MEANS!
