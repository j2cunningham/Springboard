# README

The requirements for this mini-project are to use both CSS and XPATH selectors to scrap a website and compare the output of the two. The two outputs should be identical. The link I decided to test scrapy on is 

`http://odp.org/Computers/Programming/Languages/Python/Books/`

This current directory contains several files. The important ones pertaining to this submission are 

- css-scraper-results.json
- xpath-scraper-results.json

To obtain the above files, one just has to execute on a terminal the two commands below

- `$ scrapy crawl odp_css -o css-scraper-results.json`
 
- `$ scrapy crawl odp_xpath -o xpath-scraper-results.json`

To check the validity of the two json output files, just run `python check_json.py`.

For ease, I have put all of these commands in `run.sh`.

