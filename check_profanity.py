import urllib.request

def read_text():
    quotes = open(r"C:\Users\lalor\Downloads\some_file.txt")
    contents_of_file = quotes.read()
    print(contents_of_file)
    quotes.close()
    check_profanity(contents_of_file)

def check_profanity(text_to_check):
    # Python 2: import urllib only
    # connection = urllib.urlopen("http://www.wdylike.appspot.com/?q=" + text_to_check)
    # Python 3: import urllib.request
    connection = urllib.request.urlopen("http://www.wdylike.appspot.com/?q=" + urllib.parse.quote(text_to_check))
    output = connection.read()
    output_string = output.decode("utf-8")
    if "true" in output_string:
        print("Profanity Alert!")
    elif "false" in output_string:
        print("Safe text, you can send it")
    else:
        print("Could not scan the document properly")
    connection.close()

read_text()    