from html.parser import HTMLParser
import requests as httprequests

def isdigitalpluspoint(str):
    for i in range(len(str)-1):
        if str[i].isdigit() and str[i+1]=='.':
            return True
    return False

class YOUDAOHTMLParser(HTMLParser):
    isTrans=False
    isFirstTrans=True
    chtrans=[]

    isCollins=False
    collinsdef=[]
    collinsCounter=-1;
    
    def handle_starttag(self, tag, attrs):
        if(tag=='div'):
            for a in attrs:
                if len(a)<2:
                    return
                if self.isFirstTrans and a[0]=='class' and a[1]=='trans-container':
                    self.isFirstTrans=False
                    self.isTrans=True
                if a[0]=='class' and (a[1]=='collinsMajorTrans' or a[1]=='exampleLists'):
                    self.isCollins=True

    def handle_endtag(self, tag):
        if(tag=='div'):
            self.isTrans=False
            self.isCollins=False

    def handle_data(self, data):
        if(self.isTrans):
            data=data.lstrip()
            if len(data)<=0:
                return
            self.chtrans.append(data)
        if(self.isCollins):
            data=' '.join(data.replace('\t',' ').replace('\n',' ').split() )
            if len(data)<=0:
                return
            if isdigitalpluspoint(data):
                self.collinsCounter=self.collinsCounter+1
                self.collinsdef.append('')
            self.collinsdef[self.collinsCounter]=self.collinsdef[self.collinsCounter]+' '+data

def getDefyd(word):
    page=httprequests.get("http://dict.youdao.com/w/eng/"+word)

    parser = YOUDAOHTMLParser()
    parser.feed(page.text)
    return {'cn':parser.chtrans,'collis':parser.collinsdef}


