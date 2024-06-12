import pandas as pd
from web_scraper import WebScraper
from df_utils import DataframeMethods
url_JPM = "https://finance.yahoo.com/quote/JPM/history?period1=322099200&period2=1718064000&interval=1d&filter=history&frequency=1d&includeAdjustedClose=true"
url_MS ="https://finance.yahoo.com/quote/MS/history?period1=730425600&period2=1718064000&interval=1d&filter=history&frequency=1d&includeAdjustedClose=true"

html_JPM = WebScraper.grab_html(url=url_JPM)
html_MS = WebScraper.grab_html(url=url_MS)

table_JPM = WebScraper.find_table(html_JPM)
table_MS = WebScraper.find_table(html_MS)

df_util_JPM = DataframeMethods("JPM", table_JPM)
df_util_JPM.rename_columns()
df_util_JPM.export_to_csv()

df_util_MS = DataframeMethods("MS", table_MS)
df_util_MS.rename_columns()
df_util_MS.export_to_csv()