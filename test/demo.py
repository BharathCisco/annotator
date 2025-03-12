def add_numbers(a, b):
    return a + b


def greet(name):
    return "Hello, {}!".format(name)


def process_data(data):
    if isinstance(data, list):
        return [x * 2 for x in data]
    return None


def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)


def find_max(numbers):
    if not numbers:
        return None
    return max(numbers)


def reverse_string(s):
    return s[::-1]


def fibonacci(n):
    a, b = 0, 1
    sequence = []
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence


def word_count(text):
    words = text.split()
    return len(words)


def is_palindrome(s):
    return s == s[::-1]


def sum_of_squares(n):
    return sum(x ** 2 for x in range(n + 1))


def sort_list(lst):
    return sorted(lst)


def count_vowels(text):
    vowels = "aeiouAEIOU"
    return sum(1 for char in text if char in vowels)


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


if __name__ == "__main__":
    result = add_numbers(3, 5)
    message = greet("Alice")
    processed = process_data([1, 2, 3])
    fact = factorial(5)
    max_value = find_max([10, 20, 5, 8])
    reversed_str = reverse_string("hello")
    fib_seq = fibonacci(10)
    word_count_result = word_count("This is a test sentence.")
    palindrome_check = is_palindrome("racecar")
    squares_sum = sum_of_squares(5)
    sorted_numbers = sort_list([5, 2, 9, 1])
    vowel_count = count_vowels("Hello World!")
    gcd_result = gcd(48, 18)