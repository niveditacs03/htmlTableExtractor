import pandas as pd
scraper=pd.read_html("https://en.wikipedia.org/wiki/Comparison_of_Linux_distributions")
print("################################################################")
for index,data in enumerate(scraper):
    print(index)
    print(data)
print("################################################################")

print(scraper[3])