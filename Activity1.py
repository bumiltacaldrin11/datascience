import scrapy



class DataSpiderSpider(scrapy.Spider):
    name = 'horror'
    page_number = 2
    start_urls = [
    'https://www.imdb.com/list/ls026579006/?st_dt=&mode=detail&page=1&sort=list_order,asc' #most downloaded movies.

    ]

    def parse(self, response):#datas from the site that will be extracted.          
        movie_title = response.css('.lister-item-header a::text').extract()
        movie_votes = response.css('.text-muted+ span:nth-child(2)').css('::text').extract()
        movie_cost = response.css('.ghost~ .text-muted+ span').css('::text').extract()
       
         
        
        for item in zip (movie_title, movie_votes, movie_cost):#this functions is only for the arrangement into columns and rows
        
            new_item = DatascienceItem()
            new_item['movie_title'] = item[0]
            new_item['movie_votes'] = item[1]
            new_item['movie_cost'] = item[2]            
       
          
            
            yield new_item
            
            next_page = 'https://www.imdb.com/list/ls026579006/?st_dt=&mode=detail&page=&sort=list_order,asc' + str(DataSpiderSpider.page_number)#for scraping multiple pages
            if DataSpiderSpider.page_number <= 10:
               DataSpiderSpider.page_number += 1  
               yield response.follow(next_page, callback = self.parse)
    
class DatascienceItem(scrapy.Item): #items that will be called
   movie_title = scrapy.Field()
   movie_votes = scrapy.Field()    
   movie_cost = scrapy.Field()
     
      