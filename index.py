import urllib3
import re
from bs4 import BeautifulSoup

http = urllib3.PoolManager()

# Replace URL with the one that you are checking a GTM container for
response = http.request('GET', "https://www.edurant.com/")
soup = BeautifulSoup(response.data,"html.parser")
GTM = soup.find_all("noscript")

# Replace with GTM container you wish to look for or use this regex script to find any GTM container present
# GTM-[A-Z0-9]{6,7}
print(re.search("GTM-PD7QX3T", str(GTM))[0])

# If it prints with the GTM container you wish to see, then the container is present on the site
# If it prints an error, then the GTM container is NOT present on the site