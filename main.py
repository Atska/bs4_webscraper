"""
Program to web scrape the borderland twitter page for Shift codes
"""
import requests
import re
from bs4 import BeautifulSoup
from webscraper import get_dates, get_codes, save_as_csv


def main():
    # example shift code: CHCBT-TF6HB-ZC3WC-BT333-KBR3B
    # use regular expression to extract
    pattern = re.compile(r'\w{5}-\w{5}-\w{5}-\w{5}-\w{5}')
    source_url = 'https://twitter.com/DuvalMagic'
    get_url = requests.get(source_url)
    soup = BeautifulSoup(get_url.text, 'html.parser')
    #codes = re.findall(shift_code_regex, soup.text)

    # extract date from twitter
    containers = soup.find_all(class_='tweet js-stream-tweet js-actionable-tweet js-profile-popup-actionable '
                                      'dismissible-content original-tweet js-original-tweet has-cards has-content')

    codes = get_codes(containers, pattern)
    dates = get_dates(containers)
    csv_filename = 'Shift_codes.csv'
    save_location = 'C:/Users/Binh/PycharmProjects/bs4_webscraper/' + csv_filename
    save_as_csv(codes, dates, save_location)

if __name__ == '__main__':
    main()
