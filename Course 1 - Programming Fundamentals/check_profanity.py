import urllib

def read_text():
    quotes = open(r""D:\Udacity\FullStackDeveloper-UdacityNanodegree\Course 1 - Programming Fundamentals\Profanity Filter\movie_quotes.txt"")
    contents_of_file = quotes.read()
    print(contents_of_file)
    quotes.close()
    check_profanity(contents_of_file)

def check_profanity(text_to_check):
    connection = urllib.urlopen("http://www.wdylike.appspot.com/?q="+text_to_check)
    output = connection.read()
    if "true" in output:
        print("Profanity Alert!!")
    elif "false" in output:
        print("This document is clean!")
    else:
        print("Could not scan the document correctly.")
    connection.close()
    
read_text()
