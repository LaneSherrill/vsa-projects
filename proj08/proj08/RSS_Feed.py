# Name:
# Date

import feedparser
import string
import time
from project_util import translate_html
from news_gui import Popup

#-----------------------------------------------------------------------
#
# proj08: RSS Feed Filter

#======================
# Code for retrieving and parsing
# Google and Yahoo News feeds
# Do not change this code
#======================

def process(url):
    """
    Fetches news items from the rss url and parses them.
    Returns a list of NewsStory-s.
    """
    feed = feedparser.parse(url)
    entries = feed.entries
    ret = []
    for entry in entries:
        guid = entry.guid
        title = translate_html(entry.title)
        link = entry.link
        summary = translate_html(entry.summary)
        try:
            subject = translate_html(entry.tags[0]['term'])
        except AttributeError:
            subject = ""
        newsStory = NewsStory(guid, title, subject, summary, link)
        ret.append(newsStory)
    return ret

#======================
# Part 1
# Data structure design
#======================

# Problem 1

# TODO: NewsStory

class NewsStory(object):
    def __init__(self,guid,title,subject,summary,link):
        self.guid = guid
        self.title=title
        self.subject=subject
        self.summary=summary
        self.link=link
    def get_guid(self):
        return self.guid
    def get_title(self):
        return self.title
    def get_subject(self):
        return self.subject
    def get_summary(self):
        return self.summary
    def get_link(self):
        return self.link






#======================
# Part 2
# Triggers
#======================

class Trigger(object):
    def evaluate(self, story):
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """
        raise NotImplementedError


# Whole Word Triggers
# Problems 2-5
class wordtrigger(Trigger):
    def __init__(self, word):
        self.word = word.lower()

    # TODO: WordTrigger
    def is_word_in(self, str):
        for character in string.punctuation:
            str = str.replace(character, ' ')
        str = str.lower()
        string1 = str.split(" ")
        if self.word in string1:
            return True
        else:
            return False
# TODO: TitleTrigger
class TitleTrigger(wordtrigger):
    def evaluate(self, story):
        return self.is_word_in(story.get_title())
# TODO: SubjectTrigger
class SubjectTrigger(wordtrigger):
    def evaluate(self, story):
        return self.is_word_in(story.get_subject())
# TODO: SummaryTrigger
class SummaryTrigger(wordtrigger):
    def evaluate(self, story):
        return self.is_word_in(story.get_summary())

# Composite Triggers
# Problems 6-8

# TODO: NotTrigger
class NotTrigger(Trigger):
    def __init__(self, Trigger):
        self.Trigger=Trigger
    def evaluate(self, story):
        return not self.Trigger.evaluate(story)

# TODO: AndTrigger
class AndTrigger(Trigger):
    def __init__(self, Trigger, Trigger2):
        self.Trigger = Trigger
        self.Trigger2 = Trigger2
    def evaluate(self, story):
        return self.Trigger.evaluate(story) and self.Trigger2.evaluate(story)

# TODO: OrTrigger
class OrTrigger(Trigger):
    def __init__(self, Trigger, Trigger2):
        self.Trigger = Trigger
        self.Trigger2 = Trigger2
    def evaluate(self, story):
        return self.Trigger.evaluate(story) or self.Trigger2.evaluate(story)

# Phrase Trigger
# Question 9

# TODO: PhraseTrigger
class PhraseTrigger(Trigger):
    def __init__(self, phrase):
        self.phrase = phrase


    def evaluate(self, story):
        if self.phrase in story.get_subject() or self.phrase in story.get_title() or self.phrase in story.get_summary():
            return True
        else:
            return False



#======================
# Part 3
# Filtering
#======================

def filter_stories(stories, triggerlist):
    """
    Takes in a list of NewsStory-s.
    Returns only those stories for whom
    a trigger in triggerlist fires.
    """
    # TODO: Problem 10
    # This is a placeholder (we're just returning all the stories, with no filtering) 
    # Feel free to change this line!
    list = []
    for story in stories:
        for trigger in triggerlist:
            if trigger.evaluate(story) == True:
                list.append(story)
    return list


#======================
# Extensions: Part 4
# User-Specified Triggers
#======================

def readTriggerConfig(filename):
    """
    Returns a list of trigger objects
    that correspond to the rules set
    in the file filename
    """
    # Here's some code that we give you
    # to read in the file and eliminate
    # blank lines and comments
    triggerfile = open(filename, "r")
    all = [ line.rstrip() for line in triggerfile.readlines() ]
    lines = []
    for line in all:
        if len(line) == 0 or line[0] == '#':
            continue
        lines.append(line)

    # TODO: Problem 11
    # 'lines' has a list of lines you need to parse
    # Build a set of triggers from it and
    # return the appropriate ones
    
import thread

def main_thread(p):
    # A sample trigger list - you'll replace
    # this with something more configurable in Problem 11
    t1 = SubjectTrigger("Trump")
    t2 = SummaryTrigger("Trump")
    t3 = PhraseTrigger("Trump")
    t4 = OrTrigger(t2, t3)
    triggerlist = [t1, t4]
    
    # TODO: Problem 11
    # After implementing readTriggerConfig, uncomment this line 
    #triggerlist = readTriggerConfig("triggers.txt")

    guidShown = []
    
    while True:
        print "Polling..."

        # Get stories from Google's Top Stories RSS news feed
        stories = process("http://news.google.com/?output=rss")
        # Get stories from Yahoo's Top Stories RSS news feed
        stories.extend(process("http://rss.news.yahoo.com/rss/topstories"))

        # Only select stories we're interested in
        stories = filter_stories(stories, triggerlist)
    
        # Don't print a story if we have already printed it before
        newstories = []
        for story in stories:
            if story.get_guid() not in guidShown:
                newstories.append(story)
        
        for story in newstories:
            guidShown.append(story.get_guid())
            p.newWindow(story)

        print "Sleeping..."
        time.sleep(SLEEPTIME)

SLEEPTIME = 10 #seconds -- how often we poll
if __name__ == '__main__':
    p = Popup()
    thread.start_new_thread(main_thread, (p,))
    p.start()

