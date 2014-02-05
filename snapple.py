import codecs
import urllib2
from bs4 import BeautifulSoup

BASE_URL = 'http://www.snapple.com/real-facts/list-view/'

# loop over each page of facts and parse the fact number and detail
for i in range(1, 10):
    page = urllib2.urlopen(BASE_URL + str(i))
    soup = BeautifulSoup(page)

    fact_numbers = soup.find_all('h3', class_='fact_number')
    fact_details = soup.find_all('p', class_='fact_detail')

    for number, fact in zip(fact_numbers, fact_details):
        with codecs.open('facts', 'a', 'utf-8') as output:
            # output a csv file for importing into database
            # backticks used due to single and double quotes
            # being used interchangeably within the fact details
            output.write('`' + number.string + '`' + ',' +
                         '`' + fact.string + '`' + '\n')
