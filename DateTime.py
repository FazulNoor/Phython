from datetime import datetime
import numpy as np

def input_date():
    return input("Enter the Date to find Days")

def convert_date():
    return datetime.strptime(input_date(), "%Y-%m-%d")

def print_diff_days():
    return convert_date() - datetime.today()


print(f"No of Days {print_diff_days()}")
