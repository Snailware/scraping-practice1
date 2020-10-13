# practice scraping websites for info. 
#
#

import requests

URL = "https://www.monster.com/jobs/search/?q=Software-Developer&where=Australia"

def main():

    page = requests.get(URL)

    print(page.content)









    exit()

main()