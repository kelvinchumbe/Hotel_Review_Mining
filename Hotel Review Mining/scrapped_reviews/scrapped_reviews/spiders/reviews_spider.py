import scrapy

class ReviewsSpider(scrapy.Spider):
    name = "reviews"
    # start_urls = [
    #     'https://www.tripadvisor.com/Hotel_Review-g1062161-d500854-Reviews-or0-Sarova_Whitesands_Beach_Resort_Spa-Bamburi_Mombasa_Coast_Province.html#REVIEWS',
    #     'https://www.tripadvisor.com/Hotel_Review-g294207-d302829-Reviews-or0-Sarova_Stanley-Nairobi.html#REVIEWS',
    #     'https://www.tripadvisor.com/Hotel_Review-g294207-d305107-Reviews-or0-Sarova_Panafric-Nairobi.html#REVIEWS',
    #     'https://www.tripadvisor.com/Hotel_Review-g294209-d504789-Reviews-or0-Sarova_Mara_Game_Camp-Maasai_Mara_National_Reserve_Rift_Valley_Province.html#REVIEWS',
    #     'https://www.tripadvisor.com/Hotel_Review-g303975-d505971-Reviews-or0-Sarova_Lion_Hill_Game_Lodge-Lake_Nakuru_National_Park_Rift_Valley_Province.html#REVIEWS',
    #     'https://www.tripadvisor.com/Hotel_Review-g294207-d3223389-Reviews-Eka_Hotel_Nairobi-Nairobi.html',
    #     'https://www.tripadvisor.com/Hotel_Review-g294207-d1860203-Reviews-Sankara_Nairobi_Autograph_Collection_by_Marriott-Nairobi.html',
    #     'https://www.tripadvisor.com/Hotel_Review-g294207-d781694-Reviews-Kenya_Comfort_Hotel-Nairobi.html',
    #     'https://www.tripadvisor.com/Hotel_Review-g294207-d2070845-Reviews-Hennessis_Hotel-Nairobi.html',
    #     'https://www.tripadvisor.com/Hotel_Review-g294207-d301993-Reviews-Hilton_Nairobi-Nairobi.html',
    #     'https://www.tripadvisor.com/Hotel_Review-g294207-d621998-Reviews-The_Panari_Hotel-Nairobi.html',
    #     'https://www.tripadvisor.com/Hotel_Review-g294207-d455845-Reviews-Jacaranda_Nairobi_Hotel-Nairobi.html',
    #     'https://www.tripadvisor.com/Hotel_Review-g294207-d482091-Reviews-Nairobi_Safari_Club-Nairobi.html',
    # ]

    allowed_domains = ['www.tripadvisor.co.uk']
    start_urls = [
        # 'https://www.tripadvisor.co.uk/Hotel_Review-g187051-d239658-Reviews-or0-Hotel_Hilton_London_Gatwick_Airport-Crawley_West_Sussex_England.html'
        # 'https://www.tripadvisor.co.uk/Hotel_Review-g186338-d193089-Reviews-or0-Hilton_London_Metropole-London_England.html'
        # 'https://www.tripadvisor.co.uk/Hotel_Review-g186338-d192048-Reviews-or0-Hilton_London_Euston-London_England.html'
        # 'https://www.tripadvisor.co.uk/Hotel_Review-g186338-d193102-Reviews-or0-DoubleTree_by_Hilton_Hotel_London_West_End-London_England.html#REVIEWS'
        # 'https://www.tripadvisor.co.uk/Hotel_Review-g186338-d614236-Reviews-or0-Hilton_London_Tower_Bridge-London_England.html#REVIEWS'
        # 'https://www.tripadvisor.co.uk/Hotel_Review-g186338-d195185-Reviews-or0-Hilton_London_Kensington-London_England.html#REVIEWS'
        'https://www.tripadvisor.co.uk/Hotel_Review-g186338-d275581-Reviews-or0-DoubleTree_by_Hilton_London_Westminster-London_England.html#REVIEWS'
    ]

    def parse(self, response):
        hotel = response.css('#HEADING::text').get()
        reviews = response.css('div._2f_ruteS._1bona3Pu > div.cPQsENeY > q > span:nth-child(1)::text').getall()
        titles = response.css('div.glasR4aX > a > span > span::text').getall()
        ratings = response.css('div._2UEC-y30 > div > span::attr(class)').getall()
        dates = response.css('span._34Xs-BQm::text').getall()

        for review, title, rating, date in zip(reviews, titles, ratings, dates):
            yield dict(hotel=hotel, review=review, title=title, rating=rating.split("_")[-1], date=date)

        total_pages = int(response.css('div._16gKMTFp > div > div > .pageNum::text').getall()[-1])

        for page in range(1, total_pages):
            index = page*5
            page_url = 'https://www.tripadvisor.co.uk/Hotel_Review-g186338-d275581-Reviews-or%s-DoubleTree_by_Hilton_London_Westminster-London_England.html#REVIEWS' % index
            yield scrapy.Request(page_url, self.scrap_page)

        # hotel = response.css('#HEADING::text').get()
        # reviews = response.css('div._2f_ruteS._1bona3Pu > div.cPQsENeY > q > span:nth-child(1)::text').getall()
        # titles = response.css('div.glasR4aX > a > span > span::text').getall()
        # ratings = response.css('div._2UEC-y30 > div > span::attr(class)').getall()
        # dates = response.css('span._34Xs-BQm::text').getall()
        

        # for review, title, rating, date in zip(reviews, titles, ratings, dates):
        #     yield dict(hotel=hotel, review=review, title=title, rating=rating.split("_")[-1], date=date)

        # url = response.css('div._16gKMTFp > div > a.ui_button.nav.next.primary::attr(href)').get()
        # next_page_url = 'https://www.tripadvisor.co.uk' + url if url is not None else None
        
        # yield scrapy.Request(next_page_url, self.parse)


    def scrap_page(self, response):
        hotel = response.css('#HEADING::text').get()
        reviews = response.css('div._2f_ruteS._1bona3Pu > div.cPQsENeY > q > span:nth-child(1)::text').getall()
        titles = response.css('div.glasR4aX > a > span > span::text').getall()
        ratings = response.css('div._2UEC-y30 > div > span::attr(class)').getall()
        dates = response.css('span._34Xs-BQm::text').getall()

        for review, title, rating, date in zip(reviews, titles, ratings, dates):
            yield dict(hotel=hotel, review=review, title=title, rating=rating.split("_")[-1], date=date)






    