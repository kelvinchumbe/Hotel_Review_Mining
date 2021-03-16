import scrapy

class ReviewsSpider(scrapy.Spider):
    name = "reviews"
    start_urls = [
        'https://www.tripadvisor.com/Hotel_Review-g1062161-d500854-Reviews-or0-Sarova_Whitesands_Beach_Resort_Spa-Bamburi_Mombasa_Coast_Province.html#REVIEWS',
        'https://www.tripadvisor.com/Hotel_Review-g294207-d302829-Reviews-or0-Sarova_Stanley-Nairobi.html#REVIEWS',
        'https://www.tripadvisor.com/Hotel_Review-g294207-d305107-Reviews-or0-Sarova_Panafric-Nairobi.html#REVIEWS',
        'https://www.tripadvisor.com/Hotel_Review-g294209-d504789-Reviews-or0-Sarova_Mara_Game_Camp-Maasai_Mara_National_Reserve_Rift_Valley_Province.html#REVIEWS',
        'https://www.tripadvisor.com/Hotel_Review-g303975-d505971-Reviews-or0-Sarova_Lion_Hill_Game_Lodge-Lake_Nakuru_National_Park_Rift_Valley_Province.html#REVIEWS'
    ]

    def parse(self, response):
        # self.scrap_page(response)

        # total_pages = int(response.css('div._16gKMTFp > div > div > .pageNum::text').getall()[-1])

        # for page in range(1, total_pages):
        #     index = page*5
        #     page_url = 'https://www.tripadvisor.com/Hotel_Review-g303975-d505971-Reviews-or%s-Sarova_Lion_Hill_Game_Lodge-Lake_Nakuru_National_Park_Rift_Valley_Province.html#REVIEWS' % index
            # yield scrapy.Request(page_url, self.scrap_page)

        hotel = response.css('#HEADING::text').get()
        reviews = response.css('div._2f_ruteS._1bona3Pu > div.cPQsENeY > q > span:nth-child(1)::text').getall()
        titles = response.css('div.glasR4aX > a > span > span::text').getall()
        ratings = response.css('div._2UEC-y30 > div > span::attr(class)').getall()
        dates = response.css('span._34Xs-BQm::text').getall()
        

        for review, title, rating, date in zip(reviews, titles, ratings, dates):
            yield dict(hotel=hotel, review=review, title=title, rating=rating.split("_")[-1], date=date)

        next_page_url = 'https://www.tripadvisor.co.uk' + response.css('div._16gKMTFp > div > a.ui_button.nav.next.primary::attr(href)').get()
        
        yield scrapy.Request(next_page_url, self.parse)


    # def scrap_page(self, response):
    #     hotel = response.css('#HEADING::text').get()
    #     reviews = response.css('div._2f_ruteS._1bona3Pu > div.cPQsENeY > q > span:nth-child(1)::text').getall()
    #     titles = response.css('div.glasR4aX > a > span > span::text').getall()
    #     ratings = response.css('div._2UEC-y30 > div > span::attr(class)').getall()
    #     dates = response.css('span._34Xs-BQm::text').getall()

    #     for review, title, rating, date in zip(reviews, titles, ratings, dates):
    #         yield dict(hotel=hotel, review=review, title=title, rating=rating.split("_")[-1], date=date)






    