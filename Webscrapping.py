import requests
from bs4 import BeautifulSoup
import re
import sys



if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')


def extraction(url, headers):
    try:
        response = requests.get(url, headers=headers)
        print(f"Status Code: {response.status_code}")


        soup = BeautifulSoup(response.content, "html.parser")  
        products = []


        with open("debug.html", "w", encoding="utf-8") as f:
            f.write(response.text)


        
        for product in soup.find_all("div", class_=re.compile("s-result-item.*")):
            title = product.find("span", class_=re.compile("a-size-medium.*"))
            price = product.find("span", class_=re.compile("a-price.*"))
            rating = product.find("span", class_=re.compile("a-icon-alt.*"))


            if title:
                product_data = {
                    "title": title.get_text(strip=True),
                    "price": price.get_text(strip=True) if price else "N/A",
                    "rating": rating.get_text(strip=True) if rating else "N/A"
                }


                
                product_data['price'] = product_data['price'].replace('₹', 'INR ')


                products.append(product_data)


        return products
    except Exception as e:
        print(f"Error: {e}")
        return []


if __name__ == "__main__":
    url = "https://www.amazon.in/s?k=laptops&rh=n%3A1375424031&ref=nb_sb_noss"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.9"
    }


    products = extraction(url, headers)
    if products:
        for product in products:
            print(f"Title: {product['title']}")
            print(f"Price:  {product['price']}")
            print(f"Rating: {product['rating']}")
            print("-" * 50)
    else:
        print("No products found. Check debug.html for more details.")

