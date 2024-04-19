# Imports
import scrapy

# Main Scrapper
class MangaSpider(scrapy.Spider) :
    name = "manga-spider"
    start_urls = ["https://myanimelist.net/topmanga.php"]
    num_titles = 0

    def parse(self, response):
        # Mengekstrak semua elemen tr dengan kelas 'ranking-list'
        for manga in response.css('tr.ranking-list'):
            # Menghasilkan item dalam format JSON langsung di yield
            yield {
                'rank': manga.css('span[class^="lightLink top-anime-rank-text rank"]::text').get(),
                'title': manga.css('a.hoverinfo_trigger.fs14.fw-b::text').get()
            }

            next_page = response.css("a.link-blue-box.next::attr(href)").get()
            if (next_page is not None) and (self.num_titles <= 200):
                self.num_titles += 1
                next_page_url = "https://myanimelist.net/topmanga.php"+next_page
                yield response.follow(next_page_url, callback = self.parse)

'''scrapy crawl manga-spider -o ..\view\hasil.json'''
