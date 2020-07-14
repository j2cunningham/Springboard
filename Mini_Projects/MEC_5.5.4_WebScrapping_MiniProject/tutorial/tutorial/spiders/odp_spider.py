# Scrapy tutorial

# In order to run, do 'scrapy crawl odp_xpath'

# Last Modified: 7/13/2020

# The snippet below shows the source of the page that is being scrapped.
# The website: http://odp.org/Computers/Programming/Languages/Python/Books/
'''
<ul>
    <li class="listings">
    <h4><a href="http://www.network-theory.co.uk/python/intro/" target="_blank" style="text-decoration:none"><strong>An Introduction to Python</strong></a></h4>
	<p><font color="#013C7F"><strong>http://www.network-theory.co.uk/python/intro/</strong></font> <br /> By Guido van Rossum, Fred L. Drake, Jr.; Network Theory Ltd., 2003, ISBN 0954161769. Printed edition of official tutorial, for v2.x, from Python.org. [Network Theory, online]</p>
    </li>	
    <li class="listings">
    <h4><a href="http://www.brpreiss.com/books/opus7/html/book.html" target="_blank" style="text-decoration:none"><strong>Data Structures and Algorithms with Object-Oriented Design Patterns in Python</strong></a></h4>
	<p><font color="#013C7F"><strong>http://www.brpreiss.com/books/opus7/html/book.html</strong></font> <br /> The primary goal of this book is to promote object-oriented design using Python and to illustrate the use of the emerging object-oriented design patterns. A secondary goal of the book is to present mathematical tools just in time. Analysis techniques and proofs are presented as needed and in the proper context.</p>
    </li>
''';

import scrapy

class OdpSpiderXpath(scrapy.Spider):

	'''
	Scrapy with xpath option
	'''

	name = 'odp_xpath'
	start_urls = [
		"http://odp.org/Computers/Programming/Languages/Python/Books/"
	]

	def parse(self,response):
		for sel in response.xpath('//ul/li[@class="listings"]'):
			yield {
				'title': sel.xpath('h4/a//text()').get().strip(),
				'link' : sel.xpath('h4/a/@href').get().strip(),
				'desc' : sel.xpath('p//text()').getall()[2].strip()
			}


class OdpSpiderCSS(scrapy.Spider):

	'''
	Scrapy with css option
	'''

	name = 'odp_css'

	start_urls = [
		"http://odp.org/Computers/Programming/Languages/Python/Books/"
	]

	def parse(self,response):
		for sel in response.css('.listings'):
			yield {
				'title' : sel.css('h4 strong::text').get().strip(),
				'link'  : sel.css('h4 a::attr(href)').get().strip(),
				'desc'  : sel.css('p::text')[1].get().strip()
			}
			

