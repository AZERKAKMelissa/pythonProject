import requests
from bs4 import BeautifulSoup




url_base ="http://books.toscrape.com/index.html"

def recupere_categories():
    """retourne une liste contenant les urls categories"""
    page = requests.get(url_base)
    soup = BeautifulSoup(page.content, "html.parser")
    ul_element = soup.find('div', class_="side_categories").ul.ul
    urls_categories = ul_element.find_all('a')
    categories_urls = []

    for url in urls_categories:
        categories_urls.append(url["href"])

    return categories_urls


def recupere_données_livres(url):
    """retourne les données du livre sous forme de dictionnnaire"""

    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    title = soup.find('h1').get_text()
    price_including_tax = soup.find_all('td')[3].get_text()
    price_excluding_tax = soup.find_all('td')[2].get_text()
    number_available = soup.find_all('td')[5].get_text()
    product_description_titre = soup.find_all('h2')[0].get_text()
    product_description = soup.find_all('p')[3].get_text()
    category = soup.find_all('li')[2].a.get_text()
    review_rating = soup.find_all('td')[6].get_text()
    image_url = soup.find_all('img')[0]
    imurl = str(image_url)
#todo : compléter le dictionnaire
    data = {"titre": title, "price_including_tax": price_including_tax, "price_excluding_tax": price_excluding_tax, "number_available": number_available, "product_description_titre": product_description_titre, "product_description": product_description, "category": category, "review_rating": review_rating, "image_url": image_url }
    return data

    #product_page_url = url
    #universal_product_code =
    #product_code(upc)

    #price_excluding_tax
    #number_available
    #product_description
    #category
    #review_rating
    #image_url


    return données


if __name__ == '__main__':
    categories_url = recupere_categories()
    print("Récupérer le contenu de la page principal")
    print(categories_url)
    print("\n \n")
    url = "http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"
    #données_des_livres = []
    #données = recupere_données_livres(url)
    #données_des_livres.append(données)

    #url = "https://books.toscrape.com/catalogue/set-me-free_988/index.html"
    #données = recupere_données_livres(url)
    #données_des_livres.append(données)


    urls_livres = ["http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html",
                   "https://books.toscrape.com/catalogue/set-me-free_988/index.html",
                   "https://books.toscrape.com/catalogue/the-natural-history-of-us-the-fine-art-of-pretending-2_941/index.html"]
    données_des_livres = []
    for url in urls_livres:
        données = recupere_données_livres(url)
        données_des_livres.append(données)
        
    print(données_des_livres)

    #print("Recupere données livres : \n")
    #print(données)





