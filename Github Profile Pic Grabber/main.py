from bs4 import BeautifulSoup as bs
import requests

github_user = input("Enter Github User's Profile URL: ")
url = f'https://github.com/{github_user}'
r = requests.get(url)

# soup=bs(r) gives a 200/404 etc response.
soup = bs(r.content, 'html.parser')

# locate the image tag with the alt as Avatar and once that is done, return the value of the 'src' tag into profile_image
profile_image = soup.find('img', {'alt': 'Avatar'})['src']

# prints the Link to the Profile Picture
print(profile_image)
