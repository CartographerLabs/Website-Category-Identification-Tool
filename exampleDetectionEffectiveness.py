from Identifier.CategoryIdentifier import Identifier

news_website_articles = [
    "https://www.theverge.com/2020/1/28/21080720/amazon-product-liability-lawsuits-marketplace-damage-third-party",
    "https://news.yahoo.com/joe-scarborough-trashes-trump-defense-162401753.html",
    "https://news.yahoo.com/trumps-impeachment-defense-ken-starrs-lecture-on-partisanship-followed-by-attacks-on-joe-biden-012839837.html",
    "https://www.hindustantimes.com/india-news/no-need-to-move-foreigners-out-who-as-india-preps-to-evacuate-citizens-in-china/story-KkfXhhoT7ywbv2v0lr0KPN.html",
    "https://www.thehindu.com/news/national/sharjeel-imam-arrested-in-bihar/article30674659.ece",
    "https://www.theverge.com/2020/1/28/21100071/microsoft-surface-pro-x-edge-chromebook-chrome-browser-arm-chip-apps",
    "https://edition.cnn.com/asia/live-news/coronavirus-outbreak-01-28-20-intl-hnk/index.html",
    "https://edition.cnn.com/2020/01/28/politics/donald-trump-impeachment-president-defense/index.html",
    "https://www.nytimes.com/2020/01/28/us/politics/impeachment-legal-teams.html?action=click&module=Top%20Stories&pgtype=Homepage",
    "https://www.nytimes.com/2020/01/28/opinion/john-bolton-book-trump.html?action=click&module=Opinion&pgtype=Homepage",
    "https://www.foxnews.com/shows/bill-hemmer-reports",
    "https://www.foxnews.com/politics/massive-crowds-form-for-trumps-new-jersey-rally-amid-impeachment-fight",
    "https://www.nbcnews.com/politics/trump-impeachment-inquiry/bolton-pits-trump-against-senate-gop-s-majority-n1124291",
    "https://www.nbcnews.com/politics/trump-impeachment-inquiry/trump-s-senate-impeachment-trial-what-happened-day-6-n1124256",
    "https://www.dailymail.co.uk/health/article-7937887/Coronavirus-fears-hit-Birmingham-facemask-wearing-patient-escorted-ambulance.html",
    "https://www.dailymail.co.uk/news/article-7938587/Former-TalkTalk-executive-sues-firm-equal-pay-law.html",
    "https://www.washingtonpost.com/politics/leaked-bolton-book-threatens-to-upend-senate-impeachment-trial/2020/01/27/870f75e0-411d-11ea-b503-2b077c436617_story.html",
    "https://www.washingtonpost.com/sports/2020/01/28/kobe-bryant-dad-daughters-gigi/",
    "https://www.theguardian.com/science/2020/jan/28/germany-confirms-first-human-coronavirus-transmission-in-europe",
    "https://www.theguardian.com/world/2020/jan/28/netanyahu-withdraws-immunity-from-prosecution-request",
    "https://www.wsj.com/articles/trump-set-to-release-middle-east-peace-plan-11580221616?mod=hp_lead_pos1",
    "https://www.wsj.com/articles/who-chief-praises-beijings-coronavirus-response-as-travel-barriers-rise-11580227640?mod=hp_lead_pos5",
    "https://abcnews.go.com/Politics/senate-impeachment-trial-live-updates-trump-legal-team/story?id=68584065",
    "https://abcnews.go.com/US/boy-allegedly-stabs-sister-multiple-times-charged-attempted/story?id=68581609",
    "https://www.bbc.co.uk/news/technology-51283059",
    "https://www.bbc.co.uk/news/world-asia-china-51279726",
    "https://eu.usatoday.com/story/sports/nba/2020/01/28/nike-suspends-sale-kobe-bryant-products-online/4595811002/",
    "https://eu.usatoday.com/story/news/politics/2020/01/28/impeachment-live-updates-trump-defense-team-presents-last-day/4594434002/",
    "https://www.thedailybeast.com/trumps-impeachment-acquittal-will-have-real-national-security-consequences-us-officials-warn?ref=home",
    "https://www.thedailybeast.com/the-crown-is-wrong-to-end-in-2003-its-just-when-the-royal-family-of-now-gets-interesting?ref=home",
    "https://www.nationalgeographic.com/animals/2018/09/colombia-cocaine-hippos-rewilding-experiment-news/",
    "https://www.nationalgeographic.com/science/2020/01/how-coronavirus-spreads-on-a-plane/",
    "https://www.euronews.com/2020/01/31/macron-says-brexit-day-is-historic-alarm-signal-for-reform-in-europe",
    "https://www.euronews.com/2020/01/31/live-updates-eu-and-uk-to-remain-allies-partners-friends-leaders-say-on-brexit-day",
    "https://www.nbcnews.com/politics/trump-impeachment-inquiry/senate-trial-trump-may-have-gained-power-lost-political-case-n1128066",
    "https://www.nbcnews.com/politics/trump-impeachment-inquiry/senate-vote-calling-witnesses-fails-ushering-trial-endgame-n1127966",
    "https://pagesix.com/2020/02/01/meghan-markles-first-gig-will-be-reality-tv-show-about-second-weddings/?_ga=2.133696843.41828152.1580577765-1960980106.1580577765",
    "https://nypost.com/2020/02/01/rashida-tlaib-boos-hillary-clinton-at-bernie-sanders-event-in-iowa/",
    "https://uk.reuters.com/article/uk-britain-eu/brexit-at-last-britain-leaves-the-eu-as-champagne-corks-fly-idUKKBN1ZU1TM",
    "https://uk.reuters.com/article/us-china-health/russia-to-evacuate-citizens-from-china-as-virus-toll-rises-idUKKBN1ZV38I",
    "https://www.cnbc.com/2020/02/01/coronavirus-companies-suspend-china-operations-restrict-travel.html",
    "https://www.cnbc.com/2020/01/31/coronavirus-just-starting-to-have-an-impact-on-global-economy-geopolitics.html",
    "https://www.forbes.com/sites/alanohnsman/2020/01/29/ups-jumps-into-the-future-with-plan-to-buy-10000-electric-vans-and-a-waymo-self-driving-delivery-pilot/#6eeb409a5aa5",
    "https://www.forbes.com/sites/mattperez/2020/01/29/top-earning-video-gamers-the-ten-highest-paid-players-pocketed-more-than-120-million-in-2019/#201b4fbc4880",
    "https://www.foxnews.com/media/ted-cruz-nancy-pelosi-clap",
    "https://www.foxnews.com/health/coronavirus-cdc-seventh-case-us",
    "https://www.theguardian.com/politics/2020/feb/01/brexit-trade-talks-eu-to-back-spain-over-gibraltar-claims",
    "https://www.nytimes.com/2020/01/31/us/politics/trump-impeachment-trial.html?action=click&module=Spotlight&pgtype=Homepage",
    "https://edition.cnn.com/asia/live-news/coronavirus-outbreak-02-01-20-intl-hnk/index.html",
    "https://www.youtube.com/watch?v=CkonLJ2bUQk",
    "https://www.youtube.com/watch?v=N2EHwjOPEvc"
]

non_news = [
    "http://www.bristol.ac.uk/students/study/it/",
    "https://github.com/",
    "https://www.youtube.com/watch?v=S74hOTexWN8",
    "https://www.w3schools.com/python/python_classes.asp",
    "http://www.activeresponse.org/the-4-qualities-of-good-threat-intelligence/",
    "https://specterops.zoom.us/webinar/register/WN_Ak7pi_zxSM28HBIl5RIVWw",
    "https://info.signalsciences.com/detecting-account-takeovers-defending-your-users?utm_source=twitter&utm_medium=cpc",
    "https://react-bootstrap-demo.web.app/auth/signin"
]

news_list_of_total_length = []
news_list_of_self_identifiication = []
list_of_news_that_looks_like_not_news = []

# This seems to be appending to the already existing website over and over again. Its member variables are static
for website in news_website_articles:

    print(website)

    my_news_detector = Identifier(website, "Identifier/newsDetector.json")
    amount_of_news = my_news_detector._get_count_of_word_in_website("news")
    length_of_body = my_news_detector._get_length_of_body()

    news_list_of_total_length.append(length_of_body)
    news_list_of_self_identifiication.append(amount_of_news)

    if not my_news_detector.is_match():
        print("News that doesn't look like news")
        print(website)
        print(length_of_body)
        print(amount_of_news)
        list_of_news_that_looks_like_not_news.append(website)


non_news_list_of_total_length = []
non_news_list_of_self_identifiication = []

list_of_not_news_that_look_like_news = []

for website in non_news:

    print(website)

    my_news_detector = Identifier(website, "Identifier/newsDetector.json")
    amount_of_news = my_news_detector._get_count_of_word_in_website("news")
    length_of_body = my_news_detector._get_length_of_body()

    non_news_list_of_total_length.append(length_of_body)
    non_news_list_of_self_identifiication.append(amount_of_news)

    if my_news_detector.is_match():
        print("Not news that looks like news")
        print(website)
        print(length_of_body)
        print(amount_of_news)
        list_of_not_news_that_look_like_news.append(website)


print("News")
print("Total length:")
print("Max - "+str(max(news_list_of_total_length)))
print("Min - "+str(min(news_list_of_total_length)))
print("Avrg - "+str(sum(news_list_of_total_length)/len(news_list_of_total_length)))
print("Self identification:")
print("Max - "+str(max(news_list_of_self_identifiication)))
print("Min - "+str(min(news_list_of_self_identifiication)))
print("Avrg - "+str(sum(news_list_of_self_identifiication)/len(news_list_of_self_identifiication)))

print("Non-News")
print("Total length:")
print("Max - "+str(max(non_news_list_of_total_length)))
print("Min - "+str(min(non_news_list_of_total_length)))
print("Avrg - "+str(sum(non_news_list_of_total_length)/len(non_news_list_of_total_length)))
print("Self identification:")
print("Max - "+str(max(non_news_list_of_self_identifiication)))
print("Min - "+str(min(non_news_list_of_self_identifiication)))
print("Avrg - "+str(sum(non_news_list_of_self_identifiication)/len(non_news_list_of_self_identifiication)))


print("-"*20)

print("Amount of news that doesn't look like news "+ str(len(list_of_news_that_looks_like_not_news)))
print("Amount of not news that looks like news " + str(len(list_of_not_news_that_look_like_news)))

print("Percentage of news false negatives " + str(((len(list_of_news_that_looks_like_not_news)/len(news_website_articles))*100))+"%")
print("Percentage of non news false positives " + str(((len(list_of_not_news_that_look_like_news)/len(non_news))*100))+"%")
