class Mathematician:

    @staticmethod
    def square_nums(initial_list):
        return [num**2 for num in initial_list]

    @staticmethod
    def remove_positives(initial_list):
        return [num for num in initial_list if num <= 0]

    @staticmethod
    def filter_leaps(initial_list):
        return [year for year in initial_list if year % 4 == 0 and year % 100 != 0 or year % 400 == 0]


m = Mathematician()
print(m.square_nums([7, 11, 5, 4]))
print(m.remove_positives([26, -11, -8, 13, -90]))
print(m.filter_leaps([2001, 1884, 1995, 2003, 2020]))
