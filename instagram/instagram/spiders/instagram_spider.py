# -*- coding: utf-8 -*-
# python3.6
import scrapy
import json
import hashlib
from instagram.items import InstagramItem


class InstagramSpiderSpider(scrapy.Spider):
    name = 'instagram_spider'

    headers = {
        "accept": "*/*",
        "accept-language": "zh-CN,zh;q=0.9",
        "referer": "https://www.instagram.com/instagram/",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36",
        # "x-instagram-gis": "c0820ba911cd8dd114963aee240cdeeb",
        "x-requested-with": "XMLHttpRequest",
    }

    def start_requests(self):
        end_cursor = 'QVFBbU5fOHBHZW5BV0tENmFCWUFTV19RajVLQ1hibUpvNHlqNzRQdF96bm1wNmJoZ2cwQUVQYnV2Z0VCVnRZbWotODgwSzFfWkdGSHoybTVqXzVKbkJIeg=='
        code = '{"id":"25025320","first":12,"after":"%s"}' % end_cursor
        url = f'https://www.instagram.com/graphql/query/?query_hash=5b0222df65d7f6659c9b82246780caa7&variables={code}'

        headers = self.headers
        headers['x-instagram-gis'] = self.make_gis(code)

        yield scrapy.Request(url=url, headers=headers)

    # 构造x-instagram-gis
    def make_gis(self, code):

        MD5 = hashlib.md5()
        string = f'3f4bb7e50149b12acb6c51b2ae6c5089:{code}'
        MD5.update(string.encode(encoding='utf-8'))
        return MD5.hexdigest()

    def parse(self, response):
        item = InstagramItem()
        # print(response.text)
        edge_owner_to_timeline_media = json.loads(response.text)['data']['user']['edge_owner_to_timeline_media']
        count = edge_owner_to_timeline_media['count']
        edges = edge_owner_to_timeline_media['edges']
        print(count)
        for edge in edges:
            # print(edge)
            img_url = edge['node']['display_url']
            comment_count = edge['node']['edge_media_preview_like']['count']
            like_count = edge['node']['edge_media_to_comment']['count']
            text = edge['node']['edge_media_to_caption']['edges'][0]['node']['text']
            item['img_url'] = img_url
            item['comment_count'] = comment_count
            item['like_count'] = like_count
            item['text'] = text
            yield item

        page_info = edge_owner_to_timeline_media['page_info']
        has_next_page = page_info['has_next_page']
        end_cursor = page_info['end_cursor']
        print(has_next_page)
        if has_next_page:
            code = '{"id":"25025320","first":12,"after":"%s"}' % end_cursor

            headers = self.headers
            headers['x-instagram-gis'] = self.make_gis(code)

            url = f'https://www.instagram.com/graphql/query/?query_hash=5b0222df65d7f6659c9b82246780caa7&variables={code}'

            yield scrapy.Request(url=url, callback=self.parse, headers=headers)
