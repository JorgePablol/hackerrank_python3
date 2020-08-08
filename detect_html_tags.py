#Detect HTML Tags, Attributes and Attribute Values
    
    #You are given an HTML code snippet of  lines.
    #Your task is to detect and print all the HTML tags, attributes and attribute values.

    #Link = https://www.hackerrank.com/challenges/detect-html-tags-attributes-and-attribute-values/problem



from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        for attr in attrs:
            print ("->"," > ".join(attr))

parser = MyHTMLParser()

html = ""
for i in range(int(input())):
    html += input()
    html += '\n'


parser.feed(html)
