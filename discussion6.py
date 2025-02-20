import unittest
import os
import csv

def load_csv(f):
    '''
    Params: 
        f, name or path of CSV file (string)

    Returns:
        Nested dict structure from CSV
        - Outer dict keys: (str) years, values: dicts
        - Inner dict keys: (str) months, values: (str) integers

    Note: Don't strip or otherwise modify strings. Don't change datatypes from strings. 
    '''
    base_path = os.path.abspath(os.path.dirname(__file__))
    full_path = os.path.join(base_path, f)

    data = {}

    with open(full_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        headers = next(reader)  

        for row in reader:
            month = row[0].strip()  
            for i in range(1, len(row)):  
                year = headers[i].strip()  
                if year not in data:
                    data[year] = {}  
                data[year][month] = row[i].strip() 

    return data

def get_annual_max(d):
    '''
    Params:
        d, dict created by load_csv above

    Returns:
        List of tuples, each with 3 items: (year, month, max_value)
        - max_value is the maximum value for a month in that year.
        - month is the corresponding month.

    Note: You'll have to change vals to int to compare them. 
    '''
    result = []

    for year, months in d.items():
        max_month = max(months, key=lambda m: int(months[m])) 
        max_value = int(months[max_month])  
        result.append((year, max_month, max_value))  

    return result

def get_month_avg(d):
    '''
    Params: 
        d, dict created by load_csv above

    Returns:
        Dict where:
        - Keys are years
        - Values are floats rounded to the nearest whole number (int)
          - These values represent the average visitors per month in that year.

    Note: Don't strip or otherwise modify strings. Do not change datatypes except where necessary.
          You'll have to make the vals int or float here and round the avg to pass tests.
    '''
    avg_dict = {}

    for year, months in d.items():
        values = [int(val) for val in months.values()]  
        avg_dict[year] = round(sum(values) / len(values))  

    return avg_dict

class dis7_test(unittest.TestCase):
    '''
    you should not change these test cases!
    '''
    def setUp(self):
        self.flight_dict = load_csv('daily_visitors.csv')
        self.max_tup_list = get_annual_max(self.flight_dict)
        self.month_avg_dict = get_month_avg(self.flight_dict)

    def test_load_csv(self):
        self.assertIsInstance(self.flight_dict['2021'], dict)
        self.assertEqual(self.flight_dict['2020']['JUN'], '435')

    def test_get_annual_max(self):
        self.assertEqual(self.max_tup_list[2], ('2022', 'AUG', 628))

    def test_month_avg_list(self):
        self.assertAlmostEqual(self.month_avg_dict['2020'], 398, 0)

def main():
    unittest.main(verbosity=2)

if __name__ == '__main__':
    main()


