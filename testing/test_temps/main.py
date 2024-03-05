from data import load_data, clean_data
from processing import calculate_statistics

from pathlib import Path

#from colorama import Fore, Back, Style
import colorama

def main():

    filename = "temperatures.txt"
    if not Path(filename).is_file():
        strg = f'file {filename} not at current folder, changing to other directory'
        print(colorama.Fore.YELLOW + strg)
        print(colorama.Style.RESET_ALL, end="")
        filename = "./testing/test_temps/"+filename
    raw_data = load_data(filename)
    temperatures = clean_data(raw_data)
    stats = calculate_statistics(temperatures)

    if stats:
        print(f"Minimum Temperature: {stats['min']}°C")
        print(f"Maximum Temperature: {stats['max']}°C")
        print(f"Average Temperature: {stats['average']:.2f}°C")
        print(f"Median Temperature: {stats['median']:.2f}°C")
    else:
        print("No temperature data available.")

if __name__ == "__main__":
    main()
