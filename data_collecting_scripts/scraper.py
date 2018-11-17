import scrapy
import os
import urllib.request as url

class Scraper(scrapy.Spider):
    name = "malek_spider1"
    page_number = 1
    start_urls = ["https://www.yifysubtitles.com/language/english/?page={0}"]
    download_delay = 1
    rated_number = 1
    unrated_number = 1

    def parse(self, respose):
        movie_base_url = "https://www.yifysubtitles.com"

        for media_item in respose.css(".media-body"):
            link =  media_item.css("a::attr(href)").extract_first()
            request = scrapy.Request(url=movie_base_url + link,callback=self.parse2)
            request.meta["download_timeout"] = 60
            request.meta["link"] = link
            yield request

        if self.page_number < 416:
            self.page_number +=1
            request = scrapy.Request(url=self.start_urls[0].format(self.page_number),callback=self.parse)
            request.meta["download_timeout"] = 60
            yield request


    def parse2(self, respose):
            subtitle_base_url = "https://www.yifysubtitles.com/subtitle"
            movie_title = respose.css(".row .movie-main-title ::text").extract_first()
            movie_genre = respose.css(".row .movie-genre ::text").extract_first()
            movie_rating = ""
            target = ""

            #Take the text in the cell of the film infos
            for list_group_item in respose.css(".row .list-group-item"):
                text = list_group_item.css(".text-muted ::text").extract_first()
                if text == "Rated:" :
                    movie_rating = list_group_item.css(".pull-right ::text").extract_first()
                    
            for subtitles in respose.css(".row .other-subs tr"):
                text = subtitles.css(".sub-lang ::text").extract_first()

                if text == "English":
                    link = subtitles.css(".download-cell a::attr(href)").extract_first()
                    target = link.split(os.sep)[2]

                    if movie_rating == "N/A" or movie_rating == "NOT RATED" or movie_rating == "UNRATED" or movie_rating == "Not Rated" or movie_rating == "Approved":
                        url.urlretrieve(subtitle_base_url + "/" + target + ".zip", "./unrated/" + str(self.unrated_number) + "_" + respose.meta["link"].split("/")[2])
                        self.unrated_number += 1
                    else:
                        url.urlretrieve(subtitle_base_url + "/" + target + ".zip", "./rated/"   +   str(self.rated_number) + "_" + movie_rating)
                        self.rated_number += 1

                    return {
                        "movie_title" : movie_title,
                        "movie_rating" : movie_rating,
                        "target" : target
                    }
                 