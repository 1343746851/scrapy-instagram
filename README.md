## scrapy-instagram
使用scrapy框架爬取instagram博主的相关字段
目标url：https://www.instagram.com/instagram/
目标数据： img_url, text, comment_count, like_count

## 样本数据：

{ 
 "img_url":"https://scontent-sea1-1.cdninstagram.com/vp/55b4acca286c9a38de60aab4982a7105/5BFEEF09/t51.2885-15/e35/36837260_1936075219847146_5119664694017130496_n.jpg", 
   "comment_count" : 201, 
   "like_count" : 18427, 
   "text" : "يوم طويل لكن جميل! صورنا كولكشن دلاليد وانوتا لعيد الأضحى ❤️\nوااااايد راح يعجبكم! اغلبه قطع عملية ومريحة للسفر ❤️\n#dalalidXAnotah\n@anotahfashion \nToday was awesome! Can’t wait to share with you #DalalidXAnotah new collection!! 

}

##　目标数据说明：

Comment_count: 评论数
Like_count: 点赞数
Text: 帖子内容
(帖子内容可从www.instagram.com/instagram点击帖子图片后 跳转页面看到)

Img_url: 帖子图片


## 要求：
1.爬取120条不同帖子
2.每条帖子需要的数据有：img_url, text, comment_cout, like_count
3.每条数据格式为样本数据格式
4.提交爬虫代码与120条数据（json格式）
5.禁止使用js渲染，模拟浏览器
6.无需使用cookies


