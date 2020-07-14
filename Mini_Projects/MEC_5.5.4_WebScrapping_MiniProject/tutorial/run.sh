scrapy crawl odp_css   -o css-scraper-results.json
scrapy crawl odp_xpath -o xpath-scraper-results.json
python check_json.py