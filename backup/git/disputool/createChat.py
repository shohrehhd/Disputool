from nltk.tokenize import word_tokenize,sent_tokenize
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
		address+="noone.png"
	
	return address


def CreateSpeechTag(speech,anns):
	html="<p>"
	for index, row in anns.iterrows():
			if row['TYPE'] == "Claim":
				speech=speech.replace(row['TEXT'], '<span class="claim">'+row['TEXT']+'</span>')
			elif  row['TYPE'] == "Premise":
				speech=speech.replace(row['TEXT'], '<span class="premise">'+row['TEXT']+'</span>')
	html+=speech


	
	

	html+="</p>"
	return html

def CreateImgHtml(name):
	
	html = "<div class='debater-pic'> <figure><img class = 'debater-pic' src = '"+ getImageAddress(name)+"'/> <figcaption>"+str(name)+ "</figcaption></figure></div>"
	
	return html
	
def RightBubble(name,speech,anns):
	
	img_html=CreateImgHtml(name)
	bubble = '<div class="talk-bubble tri-right talk-round talk-border right-top"> <div class="talktext">'+CreateSpeechTag(speech,anns)+' </div> </div>'
	final  = "<div class ='right-speaker'><div class = 'row'>"+bubble+img_html+"</div></div>"
	return final

def LeftBubble(name, speech,anns):
	img_html=CreateImgHtml(name)
	bubble = '<div class="talk-bubble tri-right talk-round talk-border left-top"> <div class="talktext">'+CreateSpeechTag(speech,anns)+'</div> </div>'
	final  = "<div class ='left-speaker'><div class='row'>"+img_html+bubble+"</div></div>"
	return final

def createTable(db,ann_db):
	html = "<div class = 'container-fluid'>"
	right = False
	previous_speaker=""
	for index,row in db.iterrows():
		anns =ann_db.loc[((ann_db['Document']==row['Document'])&(ann_db["PartIndex"]==row['Part']))]
		speaker = str(row['Name'])
		if(speaker!=previous_speaker):
			right = not right
		if(right):
			html+=RightBubble(str(row['Name']),str(row['Speech']),anns)
		else:
			html+=LeftBubble(str(row['Name']),str(row['Speech']),anns)
		previous_speaker = speaker

	html+="</div>"
	return html
 



