import scrapy
import json
import os

class MangaSpider(scrapy.Spider):
    name = "manga-spider"
    start_urls = ["https://myanimelist.net/topmanga.php"]
    for i in range(1, 5):
        start_urls.append("https://myanimelist.net/topmanga.php?limit=" + str(i * 50))
    i = 0

    def parse(self, response):
        # Mengekstrak semua elemen tr dengan kelas 'ranking-list'
        for mangas in response.css('tr.ranking-list'):
            # Mengambil data-data yang diperlukan
            rank = mangas.css("td.rank.ac span.lightLink::text").get()
            volume = mangas.css("div.information.di-ib.mt4::text").getall()[0].replace('\n', ' ').strip()
            waktupublish = mangas.css("div.information.di-ib.mt4::text").getall()[1].replace('\n', ' ').strip()
            title = mangas.css('a.hoverinfo_trigger.fs14.fw-b::text').get()
            links = mangas.css("a.hoverinfo_trigger::attr(href)").get()

            # Membuat request baru untuk setiap manga
            request = scrapy.Request(response.urljoin(links), callback=self.parse_creator)
            request.meta['rank'] = rank
            request.meta['volume'] = volume
            request.meta['waktupublish'] = waktupublish
            request.meta['title'] = title
            yield request

    def parse_creator(self, response):
        # Memasukkan data kedalam variable
        rank = response.meta['rank']
        title = response.meta['title']
        volume = response.meta['volume']
        waktupublish = response.meta['waktupublish']
        possible_genres = response.css("div.leftside div.spaceit_pad").css('span[itemprop="genre"]')
        genres_text = []
        if possible_genres:
            for genre in possible_genres[:3]:  
                genre_name = " ".join(genre.css('::text').get().strip().split()[:3])
                genres_text.append(genre_name)

        # Menghasilkan item dalam format JSON langsung di yield
        yield {
            'rank': rank,
            'score': response.css("div.score-label::text").get(),
            'popularity': response.css("span.numbers.popularity strong::text").get().strip('#'),
            'title': title,
            'genres': ", ".join(genres_text),
            'volume': volume,
            'waktupublish': waktupublish,
            'synopsis': (response.css('span[itemprop="description"]::text').getall()[0] +
                         response.css('span[itemprop="description"]::text').getall()[2]).replace("\r\n", "<br><br>"),
            'imglink': response.css("div#myanimelist div.wrapper div#contentWrapper div#content table tr "
                                    "td.borderClass div.leftside div a img::attr(data-src)").get(),
            'author': response.css("span.information.studio.author a::text").get()
        }

'''scrapy crawl manga-spider -o ..\view\hasil.json'''