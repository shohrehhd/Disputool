
import pandas as pd
def getImageAddress(name):
	images = {'Richard(Dick) B. Cheney': "cheney.jpg",
 		  'Johnny(John) R. Edwards':"johnny-edwards.jpg",
		  'Jimmy E. Carter':"jimmy-carter.jpg",
		  'Gerald R. Ford':"gerald-r-ford.jpg",
		  'Robert J. Dole':"robert-dole.jpg",
		  'William(Bill) J. Clinton':"william-j-clinton.jpg",
		  'Jack F. Kemp':"jack-kemp.jpg",
		  'Albert A. Gore':"albert-gore.jpg",
		  'Hillary D. R. Clinton':"hillary-clinton.jpg",
		  'Donald J. Trump':"donald-j-trump.jpg",
		  'Barack H. Obama':"barack-obama.jpg",
		  'John S. McCain':"john-mccain.jpg",
		  'James D. Quayle':"dan-quayle.jpg",
		  'Lloyd M. Bentsen':"Lloyd-Bentsen.jpg",
		  'Sarah L. Palin':"sarah-palin.jpg",
		  'Joseph(Joe) R. Biden':"joe-biden.jpg",
		  'Willard(Mitt) M. Romney':"mitt-romney.jpg",
		  'Richard M. Nixon':"richard-nixon.jpg",
		  'John F. Kennedy':"john-f-kennedy.jpg",
		  'John B. Anderson':"john-anderson.jpg",
		  'Ronald W. Reagan':"ronald-reagan.jpg",
		  'Walter F. Mondale':"walter-f-mondale.jpg",
		  'James B. Stockdale':"james-stockdale.jpg",
		  'John F. Kerry':"john-f-kerry.jpg",
		  'George W. Bush':"george-w-bush.jpg",
		  'George H. W. Bush':"george-bush.jpg",
		  'Michael S. Dukakis':"michael-s-dukakis.jpg",
		  'Henry Ross Perot':"ross-perot.jpg",
		  'Joseph I. Lieberman':"joseph-lieberman.jpg",
		  'Paul D. Ryan':"paul-ryan.jpg",
		  'Geraldine A. Ferraro':"geraldine-ferraro.jpg"}
	address = "/static/images/"
	try:
		address+=images[name]
	except:
		address+="no-one.jpg"
	
	return address

def getImageURL(name):
	images = 
	{'Donald J. Trump':'<a title="Shealah Craighead [Public domain], via Wikimedia Commons" href="https://commons.wikimedia.org/wiki/File:Donald_Trump_official_portrait.jpg"><img width="256" alt="Donald Trump official portrait" src="https://upload.wikimedia.org/wikipedia/commons/thumb/5/56/Donald_Trump_official_portrait.jpg/256px-Donald_Trump_official_portrait.jpg"></a>'}

	try:
		return images[name]
	except:
		return None
	



def CreateImgHtml(name):
	html = '<div class = "debater-pic">+'getImageURL(name)+'</div>'
	if(html==None):
		html = "<img class = 'debater-pic' id = name src = '"+ getImageAddress(name)+"'/>"
	return html
	
def RightBubble(name,speech):
	
	img_html=CreateImgHtml(name)
	bubble = '<div class="talk-bubble tri-right round border right-top"> <div class="talktext"><p>'+speech+'</p> </div> </div>
	final  = "<div class = 'row'>"+bubble+img_html+"</div>"
	return final

def LeftBubble(name, speech):
	img_html=CreateImgHtml(name)
	bubble = '<div class="talk-bubble tri-right round border left-top"> <div class="talktext"><p>'+speech+'</p> </div> </div>'
	final  = "<div class = 'row'>"+img_html+bubble"</div>"
	return final

def createTable(db):
	html = "<div class = 'container-fluid'"
	right = False
	previous_speaker=""
	for index,row in db.iterrows():
		speaker = row['Name']
		if(speaker!=previous_speaker):
			right = not right
		if(right):
			html+=RigthBubble(row['Name'],row['Speech'])
		else:
			html+=LeftBubble(row['Name'],row['Speech'])
		previous_speaker = speaker

	html+="</div>"
	return html
 



