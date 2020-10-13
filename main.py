# practice scraping websites for info. 
#
# scrape top movies section of imdb and data as tsv file. 

import requests
from bs4 import BeautifulSoup

URL = "https://www.imdb.com/chart/top/?ref_=nv_mv_250"

def main():

    page = requests.get(URL)
    # get page from URL.

    parsedPage = BeautifulSoup(page.content, 'html.parser')
    # parse html page.

    results = parsedPage.find(class_ = 'lister-list')
    # search html for lister-list class tag and store object.

    movies = results.find_all('tr')
    # search lister-list for table rows and store object. 

    csv_file = open('IMDb_top_rated_movies.tsv', mode = 'a')
    # open csv file in preparation of writing.

    lineNumber = 0
    for movie in movies:
    # iterate over list of table rows. 

        if lineNumber == 0:
            csv_file.write('rank\ttitle\tyear\trating\n')

        movie_title = movie.find(class_ = 'titleColumn')
        # search table row for titleColumn class tag and store object.
        titleList = movie_title.text.splitlines()
        # get text from movie_title object and split at \n.
        newList = listCleaner(titleList)
        rank = int(newList[1].strip('.'))
        title = str(newList[2])
        year = int(newList[3].strip('()'))

        ratingColumn = movie.find(class_ = 'ratingColumn imdbRating')
        rating = float(ratingColumn.text.strip())

        csv_file.write(f'{rank}\t{title}\t{year}\t{rating}\n')

        lineNumber += 1

    csv_file.close()

    exit()

def listCleaner(messyList):

    cleanList = []

    for entry in messyList:
        cleanList.append(entry.strip())

    return cleanList

main()