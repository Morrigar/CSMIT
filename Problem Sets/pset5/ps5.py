# 6.0001/6.00 Problem Set 5 - RSS Feed Filter
# Name: Kirk Sripinyo
# Collaborators:
# Time:

import feedparser
import string
import time
import threading
from project_util import translate_html
from mtTkinter import *
from datetime import datetime
import pytz


#-----------------------------------------------------------------------

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
        description = translate_html(entry.description)
        pubdate = translate_html(entry.published)

        try:
            pubdate = datetime.strptime(pubdate, "%a, %d %b %Y %H:%M:%S %Z")
            pubdate.replace(tzinfo=pytz.timezone("GMT"))
          #  pubdate = pubdate.astimezone(pytz.timezone('EST'))
          #  pubdate.replace(tzinfo=None)
        except ValueError:
            pubdate = datetime.strptime(pubdate, "%a, %d %b %Y %H:%M:%S %z")

        newsStory = NewsStory(guid, title, description, link, pubdate)
        ret.append(newsStory)
    return ret

#======================
# Data structure design
#======================

# Problem 1
class NewsStory (object):
    def __init__(self, guid, title, description, link, pubdate):
        self.guid         = guid
        self.title        = title
        self.description  = description
        self.link         = link
        self.pubdate      = pubdate    
    
    def get_guid(self):
        return self.guid
    
    def get_title(self):
        return self.title
    
    def get_description(self):
        return self.description
    
    def get_link(self):
        return self.link
    
    def get_pubdate(self):
        return self.pubdate
    
    
# TODO: NewsStory


#======================
# Triggers
#======================

class Trigger(object):
    def evaluate(self, story):
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """
        # DO NOT CHANGE THIS!
        raise NotImplementedError

# PHRASE TRIGGERS

# Problem 2
# TODO: PhraseTrigger

class PhraseTrigger(Trigger):
    def __init__(self, phrase):
        self.phrase   = phrase      #the phrase to look for (i.e., the trigger phrase)

    def __str__(self)     :   
        return 'This trigger will return true if the phrase: '+str(self.phrase)+' is in the test text.'
        
    def get_phrase (self):
        return self.phrase
    
    def is_phrase_in(self, testtext):
        nonletters = string.punctuation
        cleanphraseword = []
        lowerphrase = self.phrase.lower()
        
        for word in lowerphrase.split():
            cleanphraseword.append(word.strip(nonletters))
        #print (cleanphraseword)

        textremove = testtext.lower()
        testtext = ''
        for char in textremove:
            if char in nonletters:
                testtext  += ' '
            else:
                testtext += char
        justwords = []
        for word in testtext.split():           #turn test text into a list of words
            wordclean = word.strip(nonletters)  #this allows it to remove strings of garbage punctuation
            if len (wordclean) != 0:
                justwords.append(wordclean)
        
        testdict ={}
        for i in range (0, len (justwords)):
            testdict[justwords[i]]=i
        #print (testdict)
        if len(cleanphraseword)==1 and testdict.get(cleanphraseword[0],0)!=0: 
            return True
        else: 
            for i in range (0, len(cleanphraseword)-1):
                if testdict.get(cleanphraseword[i], 'Notin')=='Notin':
                    return False
                elif testdict.get(cleanphraseword[i+1],0)-testdict.get(cleanphraseword[i],0) != 1:
                    return False
                else:
                    return True

        

# Problem 3
# TODO: TitleTrigger

class TitleTrigger(PhraseTrigger):
    def __init__(self, phrase):
        PhraseTrigger.__init__(self, phrase)
    
    def evaluate(self, story):
        if self.is_phrase_in(story.get_title()):
            return True
        elif not self.is_phrase_in(story.get_title()):
            return False

# Problem 4
# TODO: DescriptionTrigger

class DescriptionTrigger(PhraseTrigger):
    def __init__(self, phrase):
        PhraseTrigger.__init__(self, phrase)
    
    def evaluate(self, story):
        if self.is_phrase_in(story.get_description()):
            return True
        elif not self.is_phrase_in(story.get_description()):
            return False    

# TIME TRIGGERS

# Problem 5
# TODO: TimeTrigger
# Constructor:
#        Input: Time has to be in EST and in the format of "%d %b %Y %H:%M:%S".
#        Convert time from string to a datetime before saving it as an attribute.

class TimeTrigger (Trigger):
    """ Expects a mark for time to evaluate the publication date.
    """ 
    def __init__(self, mark):
        self.mark = mark
        try: 
            self.convmark = time.strptime(mark, "%d %b %Y %H:%M:%S-%z")
        except:
            self.convmark = time.strptime(mark, "%d %b %Y %H:%M:%S")
    def __str__(self):
        return 'Trigger DTG for is: ' + self.mark
        
    def get_mark (self):
        return self.mark
    
    def get_trigger_time(self):
        return time.mktime(self.convmark)


# Problem 6
# TODO: BeforeTrigger and AfterTrigger

class BeforeTrigger (TimeTrigger):
    def __init__(self, mark):
        TimeTrigger.__init__(self, mark)
    
    def evaluate(self, story):
        testDTG = story.get_pubdate()
        try: 
            testDTG = time.strptime(str(testDTG),'%Y-%m-%d %H:%M:%S%z')
        except:
            testDTG = time.strptime(str(testDTG),'%Y-%m-%d %H:%M:%S')
        #print (str(testDTG))
        if time.mktime(testDTG) < self.get_trigger_time():
            return True
        else:
            return False
        
class AfterTrigger (TimeTrigger): 
    def __init__(self, mark):
        TimeTrigger.__init__(self, mark)
    
    def evaluate(self, story):
        testDTG = story.get_pubdate()
        try: 
            testDTG = time.strptime(str(testDTG),'%Y-%m-%d %H:%M:%S%z')
        except:
            testDTG = time.strptime(str(testDTG),'%Y-%m-%d %H:%M:%S')
        #print (str(testDTG))
        if time.mktime(testDTG) > self.get_trigger_time():
            return True
        else:
            return False
    
# COMPOSITE TRIGGERS

# Problem 7
# TODO: NotTrigger

class NotTrigger(Trigger):
    def __init__(self,t):
        self.t = t
        
    def evaluate (self, story):
        return not self.t.evaluate(story)

# Problem 8
# TODO: AndTrigger

class AndTrigger (Trigger):
    def __init__(self, t1, t2):
        self.t1 = t1
        self.t2 = t2
        
    def evaluate (self, story):
        if self.t1.evaluate(story) and self.t2.evaluate(story):
            return True
        else:
            return False 

# Problem 9
# TODO: OrTrigger

class OrTrigger (Trigger):
    def __init__(self, t1, t2):
        self.t1 = t1
        self.t2 = t2
        
    def evaluate (self, story):
        if self.t1.evaluate(story) or self.t2.evaluate(story):
            return True
        else:
            return False 


#======================
# Filtering
#======================

# Problem 10
def filter_stories(stories, triggerlist):
    """
    Takes in a list of NewsStory instances.

    Returns: a list of only the stories for which a trigger in triggerlist fires.
    """
    returnstories = []
    for t in triggerlist:
        for i in range (0, len(stories)):
            #print ('Searching for: '+str(t.get_phrase()))
            if t.evaluate(stories[i]):
                returnstories.append(stories[i])
    stories = returnstories
    return stories

            
    # TODO: Problem 10
    # This is a placeholder
    # (we're just returning all the stories, with no filtering)
    return stories



#======================
# User-Specified Triggers
#======================
# Problem 11
def read_trigger_config(filename):
    """
    filename: the name of a trigger configuration file

    Returns: a list of trigger objects specified by the trigger configuration
        file.
    """
    # We give you the code to read in the file and eliminate blank lines and
    # comments. You don't need to know how it works for now!
    trigger_file = open(filename, 'r')
    lines = []
    for line in trigger_file:
        line = line.rstrip()
        if not (len(line) == 0 or line.startswith('//')):
            lines.append(line)

    # TODO: Problem 11
    # line is the list of lines that you need to parse and for which you need
    # to build triggers

    print(lines) # for now, print it so you see what it contains!



SLEEPTIME = 120 #seconds -- how often we poll

def main_thread(master):
    # A sample trigger list - you might need to change the phrases to correspond
    # to what is currently in the news
    try:
        t1 = TitleTrigger("Biden")
        t2 = DescriptionTrigger("Trump")
        t3 = DescriptionTrigger("Riot")
        #t4 = AndTrigger(t2, t3)
        triggerlist = [t1, t2, t3]

        # Problem 11
        # TODO: After implementing read_trigger_config, uncomment this line 
        # triggerlist = read_trigger_config('triggers.txt')
        
        # HELPER CODE - you don't need to understand this!
        # Draws the popup window that displays the filtered stories
        # Retrieves and filters the stories from the RSS feeds
        frame = Frame(master)
        frame.pack(side=BOTTOM)
        scrollbar = Scrollbar(master)
        scrollbar.pack(side=RIGHT,fill=Y)

        t = "Google & Yahoo Top News"
        title = StringVar()
        title.set(t)
        ttl = Label(master, textvariable=title, font=("Helvetica", 18))
        ttl.pack(side=TOP)
        cont = Text(master, font=("Helvetica",14), yscrollcommand=scrollbar.set)
        cont.pack(side=BOTTOM)
        cont.tag_config("title", justify='center')
        button = Button(frame, text="Exit", command=root.destroy)
        button.pack(side=BOTTOM)
        guidShown = []
        def get_cont(newstory):
            if newstory.get_guid() not in guidShown:
                cont.insert(END, newstory.get_title()+"\n", "title")
                cont.insert(END, "\n---------------------------------------------------------------\n", "title")
                cont.insert(END, newstory.get_description())
                cont.insert(END, "\n*********************************************************************\n", "title")
                guidShown.append(newstory.get_guid())

        while True:

            print("Polling . . .", end=' ')
            # Get stories from Google's Top Stories RSS news feed
            stories = process("http://news.google.com/news?output=rss")

            # Get stories from Yahoo's Top Stories RSS news feed
            #stories.extend(process("http://news.yahoo.com/rss/topstories"))

            stories = filter_stories(stories, triggerlist)

            list(map(get_cont, stories))
            scrollbar.config(command=cont.yview)


            print("Sleeping...")
            time.sleep(SLEEPTIME)

    except Exception as e:
        print(e)


if __name__ == '__main__':
    root = Tk()
    root.title("Some RSS parser")
    t = threading.Thread(target=main_thread, args=(root,))
    t.start()
    root.mainloop()
    pass

