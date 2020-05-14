import os
import csv
import newspaper
from Identifier.CategoryIdentifier import Identifier

all_websites = []
news_websites = [    "news.yahoo.com",
    "hindustantimes.com",
    "thehindu.com",
    "theverge.com",
    "cnn.com",
    "nytimes.com",
    "foxnews.com",
    "dailymail.co.uk",
    "washingtonpost.com",
    "theguardian.com",
    "abcnews.go.com",
    "usatoday.com",
    "thedailybeast.com",
    "nationalgeographic.com",
    "euronews.com",
    "reuters.com",
    "bbc.com",
    "independent.co.uk",
    "news.sky.com",
    "express.co.uk",
    "nbcnews.com",
    "nypost.com",
    "forbes.com",
    "wsj.com",
    "medium.com",
    "https://medium.com/topic/technology",
    "https://pitchfork.com/",
    "https://www.hypebot.com/",
    "https://www.complex.com/pigeons-and-planes/",
    "http://www.myoldkentuckyblog.com/",
    "https://runthetrap.com/",
    "https://consequenceofsound.net/",
    "https://edm.com/",
    "https://dancingastronaut.com/",
    "http://www.birp.fm/",
    "https://www.stereogum.com/",
    "https://cookpad.com/",
    "http://allrecipes.com",
    "http://journaldesfemmes.fr",
    "http://giallozafferano.it",
    "http://chefkoch.de",
    "http://marmiton.org",
    "http://delish.com",
    "http://foodnetwork.com",
    "http://tasteofhome.com",
    "http://tudogostoso.com.br"
    "https://www.polygon.com/",
     "https://www.dicebreaker.com/",
     "https://techcrunch.com/",
     "https://thenextweb.com/",
     "https://www.wired.com/",
     "https://www.firstpost.com/tech/",
     "https://www.gizmodo.co.uk/",
     "https://mashable.com/?europe=true",
     "https://www.digitaltrends.com/",
     "https://www.techradar.com/uk",
     "https://www.businessinsider.com/",
     "https://www.macrumors.com/",
     "https://venturebeat.com/",
     "https://blog.us.playstation.com/",
     "https://gigaom.com/",
     "https://www.engadget.com/",
     "https://www.slashgear.com/",
     "https://www.eurogamer.net/"]

#https://en.wikipedia.org/wiki/List_of_most_popular_websites
non_news_websites = [
    "https://en.wikipedia.org/wiki/Google",
    "https://en.wikipedia.org/wiki/News",
    "https://www.programiz.com/python-programming/writing-csv-files",
    "https://universityofbristol.eu.qualtrics.com/login?path=%2FControlPanel%2F&product=ControlPanel",
    "https://www.google.com/search?rlz=1C1CHBD_enGB879GB879&ei=PVSkXqWeLNTpxgPh05OICg&q=shopping&oq=shopping",
    "https://newspaper.readthedocs.io/en/latest/",
    "https://zoom.us/",
    "https://www.ebay.co.uk/itm/Toy-Truck-Carrier-6-Mini-Cars-Play-Set-Transport-Car-Toys-Lorry-Truck-Kids-Toy/283509008809?hash=item42027429a9:g:gb0AAOSwEJZdEecR",
    "https://stackoverflow.com/questions/11227809/why-is-processing-a-sorted-array-faster-than-processing-an-unsorted-array",
    "https://twitter.com/i/events/1253969860905693186",
    "https://www.msn.com/en-gb/",
    "https://www.blogger.com/about/?r=1-null_user",
    "https://www.microsoft.com/en-GB/microsoft-365/",
    "https://www.instagram.com/mechanical.keyboards/",
    "https://www.twitch.tv/",
    "https://www.twitch.tv/directory/game/Fortnite",
    "https://www.bing.com/search?q=rockhopper+penguin"
    "https://www.facebook.com/bristoluniversity/",
    "https://www.bristol.ac.uk/city/",
    "https://github.com/user1342/Hunch",
    "https://medium.com/themlblog/getting-started-with-tensorflow-constants-variables-placeholders-and-sessions-80900727b489",
    "https://medium.com/themlblog/multivariate-regression-using-deep-neural-networks-in-tensorflow-f94f42a148b3",
    "https://marketplace.visualstudio.com/items?itemName=James-Yu.latex-workshop",
    "https://www.instagram.com/developer/authentication/",
    "https://ai.facebook.com/tools#libraries-models-and-datasets",
    "https://www.youtube.com/watch?v=RPocW_aMZKE,"
    "https://www.youtube.com/watch?v=tPYj3fFJGjk",
    "https://mathiasbynens.be/demo/url-regex",
    "https://towardsdatascience.com/topic-modelling-in-python-with-nltk-and-gensim-4ef03213cd21",
    "https://gosling.psy.utexas.edu/scales-weve-developed/ten-item-personality-measure-tipi/",
    "https://en.wikipedia.org/wiki/Kalyanam_(Non-governmental_organization)",
    "https://en.wikipedia.org/wiki/Hitomi_Station",
    "https://en.wikipedia.org/wiki/1947_Swiss_Grand_Prix",
    "https://en.wikipedia.org/wiki/Flower_Fables",
    "https://en.wikipedia.org/wiki/House_Owner",
    "https://en.wikipedia.org/wiki/Bournemouth_Corporation_Tramways",
    "https://en.wikipedia.org/wiki/Darlington,_Ohio",
    "https://www.youtube.com/watch?v=dX3k_QDnzHE",
    "https://www.youtube.com/watch?v=tfSS1e3kYeo",
    "https://www.youtube.com/watch?v=4NRXx6U8ABQ",
    "https://www.youtube.com/watch?v=mZvQ9ipTK_8",
    "https://www.youtube.com/watch?v=m7Bc3pLyij0",
    "https://www.youtube.com/watch?v=gl1aHhXnN1k",
    "https://dev.to/nas5w/creating-a-javascript-function-to-calculate-whether-it-s-a-leap-year-2cip",
    "https://dev.to/asaoluelijah/how-to-access-dev-tool-on-mobile-browsers-14nd",
    "https://dev.to/jkga/portfolio-generator-built-with-nextjs-json-resume-1cpa",
    "https://dev.to/arschles/crystal-fridays-is-in-30-minutes-jam",
    "https://dev.to/akhilpokle/string-compression-facebook-interview-question-3d2o",
    "https://dev.to/fergarram/creating-a-game-for-feature-phones-using-javascript-3bnn",
    "https://stackoverflow.com/questions/5767325/how-can-i-remove-a-specific-item-from-an-array",
    "https://stackoverflow.com/questions/6591213/how-do-i-rename-a-local-git-branch",
    "https://stackoverflow.com/questions/1642028/what-is-the-operator-in-c",
    "https://stackoverflow.com/questions/348170/how-do-i-undo-git-add-before-commit",
    "https://stackoverflow.com/questions/231767/what-does-the-yield-keyword-do",
    "https://stackoverflow.com/questions/477816/what-is-the-correct-json-content-type",
    "https://stackoverflow.com/questions/292357/what-is-the-difference-between-git-pull-and-git-fetch",
    "https://stackoverflow.com/questions/2003505/how-do-i-delete-a-git-branch-locally-and-remotely",
    "https://stackoverflow.com/questions/927358/how-do-i-undo-the-most-recent-local-commits-in-git",
    "https://www.theverge.com/2020/5/4/21244667/election-candidates-zoom-campaign-social-media-politicians-rally",
    "https://www.theverge.com/2020/5/4/21246284/amazon-vp-resign-whistleblower-firings-warehouse-workers",
    "https://www.theverge.com/2020/5/4/21245940/macbook-pro-13-inch-apple-new-magic-keyboard-price-release-date",
    "https://www.theverge.com/2020/5/4/21246561/microsoft-windows-10x-single-screens-windows-usage-demand-coronavirus-pandemic",
    "https://www.theverge.com/2020/5/4/21246386/augmented-reality-ar-copy-cut-paste-real-world-photoshop-demo",
    "http://www.hackinginsider.com/2018/03/gdpr-to-put-a-high-price-on-security-breaches/",
    "http://www.hackinginsider.com/2018/02/4293/",
    "http://www.hackinginsider.com/2018/01/the-past-present-and-future-of-the-password/",
    "http://www.hackinginsider.com/2017/06/a-guide-to-offender-profiling-malicious-actors/",
    "https://techcrunch.com/2020/05/04/decrypted-cheggs-third-time-unlucky-oktas-new-cso-rapid7-beefs-up-cloud-security/",
    "https://techcrunch.com/2020/05/04/tech-stocks-open-lower-ahead-of-another-busy-earnings-week/",
    "https://techcrunch.com/2020/05/04/equity-monday-intel-covets-moovit-two-early-stage-rounds-and-ubers-earnings/",
    "https://techcrunch.com/2020/05/04/amazon-flipkart-ola-and-uber-begin-to-resume-their-services-in-india/",
    "https://www.wired.com/story/how-might-the-change-of-seasons-affect-covid-19/",
    "https://www.wired.com/story/which-macbook-should-you-buy/",
    "https://www.wired.com/story/for-jeffrey-epstein-mit-was-just-a-safety-school/",
    "https://www.wired.com/story/theaters-covid-19-coronavirus/",
    "https://www.wired.com/story/this-mental-health-app-is-tailor-made-for-your-pandemic-woes/",
    "https://mashable.com/uk/shopping/best-deals-lego-star-wars-may-3/?europe=true",
    "https://mashable.com/uk/roundup/best-dumbbells-uk/?europe=true",
    "https://www.eurogamer.net/articles/digitalfoundry-2019-the-new-cyberpunk-2077-video-looks-good-but-the-gamescom-demo-was-better",
    "https://www.eurogamer.net/articles/2020-02-05-cyberpunk-2077-got-delayed-so-i-made-it-in-fallout-4-with-mods",
    "https://www.eurogamer.net/articles/2019-08-19-google-reveals-more-games-coming-to-stadia-including-cyberpunk-2077",
    "https://www.dicebreaker.com/games/catan-1/news/catan-two-player-rules-free-expansion",
    "https://www.dicebreaker.com/games/capital-lux-2-generations/news/capital-lux-2-kickstarter",
    "https://www.dicebreaker.com/games/frosthaven/news/frosthaven-kickstarter-record",
    "https://www.dicebreaker.com/games/arkham-horror-the-card-game/news/innsmouth-conspiracy-announced-arkham-horror-tcg",
    "https://www.polygon.com/entertainment/2020/5/4/21244551/best-new-movies-tv-shows-comics-anime-2020-summer-release-dates",
    "https://www.polygon.com/2019/11/13/20959862/star-wars-watch-order-disney-plus-movies-shows-chronological-skywalker-saga",
    "https://www.polygon.com/ps4/2020/5/4/21244022/playstation-4-ps4-buy-guide-best-console-playstation-plus-playstation-now-4k",
    "https://www.polygon.com/2020/5/2/21225330/online-gaming-lockdown-quarantine-coronavirus-destiny-animal-crossing"
    "https://arstechnica.com/information-technology/2020/05/ubuntu-20-04-welcome-to-the-future-linux-lts-disciples/",
    "https://www.tomshardware.com/uk/news/hp-omen-25l-30l-gaming-desktop-2020-price-specs-release-date",
    "https://9to5mac.com/2020/04/10/ios-adoption-us-smartphone-activations/",
    "https://9to5mac.com/2020/05/04/apple-updates-13-inch-macbook-pro-with-magic-keyboard-doubles-ssd-storage/"
]

max_count = 0
# Loos through all news websites and collects articles from their front page
for website in news_websites:
    if not website.startswith("http"):
        website = "http://{}".format(website)
    print(website)
    page = newspaper.build(website)
    website_count = 0
    for article in page.articles:
        print("\t{}".format(article.url))
        all_websites.append(article.url)
        website_count = website_count + 1
        max_count = max_count + 1

        if website_count >= 5:
            break


# Loops through all non news websites, adds the original url then finds other urls on the root of the webpage.
max_count = 0
for website in non_news_websites:
    all_websites.append(website)
    if not website.startswith("http"):
        website = "http://{}".format(website)
    print(website)
    page = newspaper.build(website)
    website_count = 0
    for article in page.articles:
        print("\t{}".format(article.url))
        all_websites.append(article.url)
        website_count = website_count + 1
        max_count = max_count + 1
        # five articles max per source
        if website_count >= 5:
            break


# Remove duplicates
for website in all_websites:
    website = website.strip("https://")
    website = website.strip("http://")

    for website_to_compare in all_websites:
        if website in website_to_compare:
            all_websites.remove(website_to_compare)

cvs_file = 'websites.csv'
if os.path.isfile(cvs_file):
    os.remove(cvs_file)

# Loops over all of the news websites and identifies if they are a news website or not
# A second check is done with a secondary file which doesn't have the blacklist / whitelist data in.
for website_url in all_websites:
    match_using_blacklist = False
    blacklist_identifier = Identifier(website_url, "newsDetector.json")
    if blacklist_identifier.is_match():
        print("The website {} is a news website.".format(website_url))
        match_using_blacklist = True
    else:
        print("The website {} is not a news website.".format(website_url))

    # Secondary check without black/white list
    match_without_blacklist = False
    blacklist_identifier = Identifier(website_url, "newsDetector2.json")
    if blacklist_identifier.is_match():
        print("The website {} is a news website.".format(website_url))
        match_without_blacklist = True
    else:
        print("The website {} is not a news website.".format(website_url))

    # Writes output to CVS file
    try:
        file = open(cvs_file, 'a', newline='')
        writer = csv.writer(file)

    except:
        file = open(cvs_file, 'w', newline='')
        writer = csv.writer(file)
        writer.writerow(["URL", "Tool (No Blacklists)", "Tool (With Blacklist)"])

    writer.writerow([website_url,match_without_blacklist, match_using_blacklist])
    file.close()