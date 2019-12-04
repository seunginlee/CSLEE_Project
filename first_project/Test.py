import pandas as pd

pd.options.mode.chained_assignment = None

class Wilson_Analysis_System:
    def __init__(self, filename, encoding_value):
        self.origin = pd.read_csv(str(filename) + '.csv',  encoding=str(encoding_value))

    def sort(self, set_default, set_column_year_value, set_year_range, set_column_etc):
        self.origin_sort = pd.DataFrame(self.origin, columns=[str(set_default)])
        start = int(set_column_year_value)
        end = int(set_column_year_value)+int(set_year_range)
        for i in range(start, end):
            self.origin_sort[str(i) + str(set_column_etc)] = \
                self.origin[str(i) + str(set_column_etc)]
        return self.origin_sort

    def per_sort(self, set_default, set_default_name , set_column_year_value, set_year_range, set_column_etc):
        self.origin_per_sort = pd.DataFrame(self.origin, columns=[str(set_default)])
        start = int(set_column_year_value)
        end = int(set_column_year_value) + int(set_year_range)
        for i in range(start, end):
           self.origin_per_sort[str(i) + str(set_default_name)] = (self.origin[str(i) + str(set_column_etc)] / self.origin[
                str(i-1) + str(set_column_etc)]) - 1

        return self.origin_per_sort

if __name__ == "__main__":
    WASX = Wilson_Analysis_System('D:/python/day4/sodc', 'CP949')
    WASY = Wilson_Analysis_System('D:/python/day4/choolsan', 'CP949')
    print(WASX.sort('시도별', 2007, 11, ' 1인당 개인소득 (천원)'))
    print(WASY.sort('시도별', 2007, 11, ' 합계출산율'))
    print(WASX.per_sort('시도별', ' 소득증감률', 2008, 10, ' 1인당 개인소득 (천원)'))
    print(WASY.per_sort('시도별', ' 출산증감률', 2008, 10, ' 합계출산율'))