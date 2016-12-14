
#!venv/bin/python
import requests
import json
import re
import bs4
from flask import Flask, jsonify, make_response, request, render_template

#Use the following to not return an error when BS reads in non-ascii characters
import sys
reload(sys)
sys.setdefaultencoding('utf-8')



app = Flask(__name__)


global returnOutput

returnOutput = []


@app.route('/<string:topic>/<int:run>', methods=['GET', 'POST'])
def get_wiki(topic,run):
    returnOutput[:] = []
    return bsFunc('/wiki/'+topic,run)


def hasNoIntersection(a, b):
    return set(a).isdisjoint(b)



def helperRecursion(addAppend, iterate):

    if iterate > 1:
        iterate = iterate - 1
        bsFunc(addAppend,iterate)
    else:
        return


'''



for link in soup.find_all('a'):
    print(link.get('href'))
# http://example.com/elsie
# http://example.com/lacie
# http://example.com/tillie

'''




def bsFunc(category, iterate):
    
    convertList = []
    cleanList = []
    firstsList = []
    cleanString = ''
    hrefLinks = []
    nameNum = 0

    index_url="https://en.wikipedia.org"
    concURL = index_url+category
    response = requests.get(concURL)
    soup = bs4.BeautifulSoup(response.text, 'html.parser') 
    firstSoup = soup.p
    #Use find_all_next rather than find_all in case first paragraph has no 
    #Use href = True to pull the URL and not hyperlink text
    followLink = firstSoup.find_all_next('a')

    for link in followLink:
        hrefLinks.append(link.get('href'))

   # for convert in followLink:
   #     convertList.append(convert.text)

   # convertDummy = convertList[0] 
   # nameNum = convertDummy.find('/wiki/')

    

    for cleanup in hrefLinks:
        cleanup = str(cleanup)
        # : To check against onomonopeia letters (Polyphemus), ] to check against footnotes ([3])
        if hasNoIntersection(cleanup, ":]#"):
            cleanList.append(cleanup)
    
    

    cleanString = cleanList[0]

    returnOutput.append(cleanString)

    

    if cleanString != '/wiki/Philosophy':
        helperRecursion(cleanString,iterate)

    return templateTeal()

 
def templateTeal():
    return render_template('loopingTemplate.html', loopingOutput = returnOutput)

if __name__ == '__main__':
    app.run(debug=True)


