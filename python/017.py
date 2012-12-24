from utils.main import main

"""
If the numbers 1 to 5 are written out in words: one, two, three, four, five,
then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in
words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and
forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20
letters. The use of "and" when writing out numbers is in compliance with
British usage.
"""

def generate_written_out_numbers(start, prepend, append, num_range, numbers):
    for i in num_range:
        numbers[start + i] = prepend + numbers[i] + append


def get_written_out_numbers():
    numbers = ['']*1001
    numbers[0] = 'zero'
    numbers[1] = 'one'
    numbers[2] = 'two'
    numbers[3] = 'three'
    numbers[4] = 'four'
    numbers[5] = 'five'
    numbers[6] = 'six'
    numbers[7] = 'seven'
    numbers[8] = 'eight'
    numbers[9] = 'nine'
    numbers[10] = 'ten'
    numbers[11] = 'eleven'
    numbers[12] = 'twelve'
    numbers[13] = 'thirteen'

    generate_written_out_numbers(10, '', 'teen', range(4, 10), numbers)

    numbers[15] = 'fifteen'
    numbers[18] = 'eighteen'

    numbers[20] = 'twenty'
    numbers[30] = 'thirty'
    numbers[40] = 'forty'
    numbers[50] = 'fifty'

    for i in range(60, 100, 10):
        numbers[i] = numbers[i/10] + 'ty'

    numbers[80] = 'eighty'

    for i in range(20, 100, 10):
        generate_written_out_numbers(i, numbers[i], '', range(1, 10), numbers)

    for i in range(100, 1000, 100):
        numbers[i] = numbers[i/100] + 'hundred'
        generate_written_out_numbers(i, numbers[i] + 'and', '', range(1, 100),
                                     numbers)

    numbers[1000] = 'onethousand'

    return numbers


def length_of_written_out_numbers(start, end):
    numbers = get_written_out_numbers()
    return sum(map(len, numbers[start:end]))



if __name__ == '__main__':
    main(length_of_written_out_numbers, 1, 1001)
