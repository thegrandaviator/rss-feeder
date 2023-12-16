import feedparser as fp

# parse_url = input("Enter your RSS feed url: ")

d = fp.parse('https://feedparser.readthedocs.io/en/latest/examples/rss20.xml')

rss_feed_title = d.feed.title
rss_feed_desc = d.feed.description
rss_feed_link = d.feed.link

print("The title of the feed is:\n", rss_feed_title + "\n")
print("The description of the feed is: \n", rss_feed_desc + "\n")
print("The original link of the feed is: \n", rss_feed_link + "\n")

