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


def getImageURL(name):

	images = 	{
'Richard(Dick) B. Cheney': '<a title="Image from the U.S. Air Force website, but likely made by office of the President. [Public domain], via Wikimedia Commons" href="https://commons.wikimedia.org/wiki/File:Richard_Cheney_2005_official_portrait.jpg"><img  alt="Richard Cheney 2005 official portrait" src="https://upload.wikimedia.org/wikipedia/commons/thumb/2/2b/Richard_Cheney_2005_official_portrait.jpg/128px-Richard_Cheney_2005_official_portrait.jpg"></a>'
,
'Hillary D. R. Clinton':'<a title="United States Department of State [Public domain], via Wikimedia Commons" href="https://commons.wikimedia.org/wiki/File:Hillary_Clinton_official_Secretary_of_State_portrait_crop.jpg"><img width="128"height="190" alt="Hillary Clinton official Secretary of State portrait crop" src="https://upload.wikimedia.org/wikipedia/commons/thumb/2/27/Hillary_Clinton_official_Secretary_of_State_portrait_crop.jpg/128px-Hillary_Clinton_official_Secretary_of_State_portrait_crop.jpg"></a>'
,
'Donald J. Trump':'<a title="Shealah Craighead [Public domain], via Wikimedia Commons" href="https://commons.wikimedia.org/wiki/File:Donald_Trump_official_portrait.jpg"><img width="128"height="190" alt="Donald Trump official portrait" src="https://upload.wikimedia.org/wikipedia/commons/thumb/5/56/Donald_Trump_official_portrait.jpg/128px-Donald_Trump_official_portrait.jpg"></a>'
,
'Johnny(John) R. Edwards':'<a title="United States Senate [Public domain], via Wikimedia Commons" href="https://commons.wikimedia.org/wiki/File:John_Edwards,_official_Senate_photo_portrait.jpg"><img width="128"height="190" alt="John Edwards, official Senate photo portrait" src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c2/John_Edwards%2C_official_Senate_photo_portrait.jpg/128px-John_Edwards%2C_official_Senate_photo_portrait.jpg"></a>'
,
'Jimmy E. Carter':'<a title="Department of Defense. Department of the Navy. Naval Photographic Center [Public domain], via Wikimedia Commons" href="https://commons.wikimedia.org/wiki/File:JimmyCarterPortrait2.jpg"><img width="128"height="190" alt="JimmyCarterPortrait2" src="https://upload.wikimedia.org/wikipedia/commons/thumb/5/5a/JimmyCarterPortrait2.jpg/128px-JimmyCarterPortrait2.jpg"></a>'
,
'Gerald R. Ford':'<a title="David Hume Kennerly [Public domain], via Wikimedia Commons" href="https://commons.wikimedia.org/wiki/File:Gerald_Ford_presidential_portrait_(cropped).jpg"><img width="128"height="190" alt="Gerald Ford presidential portrait (cropped)" src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/36/Gerald_Ford_presidential_portrait_%28cropped%29.jpg/128px-Gerald_Ford_presidential_portrait_%28cropped%29.jpg"></a>',
		  'Robert J. Dole':'<a title="PCCWW [Public domain], via Wikimedia Commons" href="https://commons.wikimedia.org/wiki/File:Bob_Dole,_PCCWW_photo_portrait.JPG"><img width="128"height="190" alt="Bob Dole, PCCWW photo portrait" src="https://upload.wikimedia.org/wikipedia/commons/4/4f/Bob_Dole%2C_PCCWW_photo_portrait.JPG"></a>',
		  'William(Bill) J. Clinton':'<a title="Bob McNeely, The White House[1] [Public domain], via Wikimedia Commons" href="https://commons.wikimedia.org/wiki/File:Bill_Clinton.jpg"><img width="128"height="190" alt="Bill Clinton" src="https://upload.wikimedia.org/wikipedia/commons/thumb/d/d3/Bill_Clinton.jpg/128px-Bill_Clinton.jpg"></a>',
		  'Jack F. Kemp':'<a title="Department of Housing and Urban Development [Public domain], via Wikimedia Commons" href="https://commons.wikimedia.org/wiki/File:Jack_Kemp_official_portrait.jpg"><img width="128"height="190"  alt="Jack Kemp official portrait" src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/9e/Jack_Kemp_official_portrait.jpg/128px-Jack_Kemp_official_portrait.jpg"></a>',
		  'Albert A. Gore':'<a title="See page for author [Public domain], via Wikimedia Commons" href="https://commons.wikimedia.org/wiki/File:Al_Gore,_Vice_President_of_the_United_States,_official_portrait_1994.jpg"><img width="128"height="190" alt="Al Gore, Vice President of the United States, official portrait 1994" src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c5/Al_Gore%2C_Vice_President_of_the_United_States%2C_official_portrait_1994.jpg/128px-Al_Gore%2C_Vice_President_of_the_United_States%2C_official_portrait_1994.jpg"></a>',
		  'Barack H. Obama':'<a title="Official White House Photo by Pete Souza [Public domain], via Wikimedia Commons" href="https://commons.wikimedia.org/wiki/File:President_Barack_Obama.jpg"><img width="128"height="190" alt="President Barack Obama" src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/8d/President_Barack_Obama.jpg/128px-President_Barack_Obama.jpg"></a>',
		  'John S. McCain':'<a title="United States Congress [Public domain], via Wikimedia Commons" href="https://commons.wikimedia.org/wiki/File:John_McCain_official_portrait_2009.jpg"><img width="128"height="190" alt="John McCain official portrait 2009" src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/e1/John_McCain_official_portrait_2009.jpg/128px-John_McCain_official_portrait_2009.jpg"></a>',
		  'James D. Quayle':'<a title="U.S. Department of Defense [Public domain], via Wikimedia Commons" href="https://commons.wikimedia.org/wiki/File:Dan_Quayle.jpg"><img width="128"height="190" alt="Dan Quayle" src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/3c/Dan_Quayle.jpg/128px-Dan_Quayle.jpg"></a>',
		  'Lloyd M. Bentsen':'<a title="Department of the Treasury[1] [Public domain], via Wikimedia Commons" href="https://commons.wikimedia.org/wiki/File:LloydBentsen.jpg"><img width="128"height="190" alt="LloydBentsen" src="https://upload.wikimedia.org/wikipedia/commons/1/12/LloydBentsen.jpg"></a>',
		  'Sarah L. Palin':'<a  href="https://en.wikipedia.org/wiki/Sarah_Palin#/media/File:Sarah_Palin_by_Gage_Skidmore_2.jpg"><img width="128"height="190" alt="SaraPalin" src="https://en.wikipedia.org/wiki/Sarah_Palin#/media/File:Sarah_Palin_by_Gage_Skidmore_2.jpg"></a>',
		  'Joseph(Joe) R. Biden':'<a title="David Lienemann [Public domain], via Wikimedia Commons" href="https://commons.wikimedia.org/wiki/File:Biden_2013.jpg"><img width="128"height="190" alt="Biden 2013" src="https://upload.wikimedia.org/wikipedia/commons/thumb/6/64/Biden_2013.jpg/128px-Biden_2013.jpg"></a>',
		  'Willard(Mitt) M. Romney':'<a title="United States Congress [Public domain], via Wikimedia Commons" href="https://commons.wikimedia.org/wiki/File:Mitt_Romney_official_US_Senate_portrait.jpg"><img width="128"height="190" alt="Mitt Romney official US Senate portrait" src="https://upload.wikimedia.org/wikipedia/commons/thumb/7/7f/Mitt_Romney_official_US_Senate_portrait.jpg/128px-Mitt_Romney_official_US_Senate_portrait.jpg"></a>',
		  'Richard M. Nixon':'<a title="Department of Defense. Department of the Army. Office of the Deputy Chief of Staff for Operations. U.S. Army Audiovisual Center.	 (ca. 1974 - 05/15/1984) [Public domain], via Wikimedia Commons" href="https://commons.wikimedia.org/wiki/File:Richard_Nixon_presidential_portrait.jpg"><img width="128"height="190" alt="Richard Nixon presidential portrait" src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/ec/Richard_Nixon_presidential_portrait.jpg/128px-Richard_Nixon_presidential_portrait.jpg"></a>',
		  'John F. Kennedy':'<a title="Cecil Stoughton, White House [Public domain], via Wikimedia Commons" href="https://commons.wikimedia.org/wiki/File:John_F._Kennedy,_White_House_color_photo_portrait.jpg"><img width="128"height="190" alt="John F. Kennedy, White House color photo portrait" src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/John_F._Kennedy%2C_White_House_color_photo_portrait.jpg/128px-John_F._Kennedy%2C_White_House_color_photo_portrait.jpg"></a>',
		  'John B. Anderson':'<a title="Leffler, Warren K., photographer. [Public domain], via Wikimedia Commons" href="https://commons.wikimedia.org/wiki/File:John_Bayard_Anderson.jpg"><img width="128"height="190" alt="John Bayard Anderson" src="https://upload.wikimedia.org/wikipedia/commons/thumb/a/a2/John_Bayard_Anderson.jpg/128px-John_Bayard_Anderson.jpg"></a>',
		  'Ronald W. Reagan':'<a title="See page for author [Public domain], via Wikimedia Commons" href="https://commons.wikimedia.org/wiki/File:Official_Portrait_of_President_Reagan_1981.jpg"><img width="128"height="190" alt="Official Portrait of President Reagan 1981" src="https://upload.wikimedia.org/wikipedia/commons/thumb/1/16/Official_Portrait_of_President_Reagan_1981.jpg/128px-Official_Portrait_of_President_Reagan_1981.jpg"></a>',
		  'Walter F. Mondale':'<a title="See page for author [Public domain], via Wikimedia Commons" href="https://commons.wikimedia.org/wiki/File:Vice_President_Mondale_1977.jpg"><img width="128"height="190" alt="Vice President Mondale 1977" src="https://upload.wikimedia.org/wikipedia/commons/thumb/b/b3/Vice_President_Mondale_1977.jpg/128px-Vice_President_Mondale_1977.jpg"></a>',
		  'James B. Stockdale':'<a title="U.S. Navy File Photo [Public domain], via Wikimedia Commons" href="https://commons.wikimedia.org/wiki/File:James_Stockdale_Formal_Portrait.jpg"><img width="128"height="190" alt="James Stockdale Formal Portrait" src="https://upload.wikimedia.org/wikipedia/commons/thumb/f/f8/James_Stockdale_Formal_Portrait.jpg/128px-James_Stockdale_Formal_Portrait.jpg"></a>',
		  'John F. Kerry':'<a title="United States Department of State [Public domain], via Wikimedia Commons" href="https://commons.wikimedia.org/wiki/File:John_Kerry_official_Secretary_of_State_portrait.jpg"><img width="128"height="190" alt="John Kerry official Secretary of State portrait" src="https://upload.wikimedia.org/wikipedia/commons/2/2c/John_Kerry_official_Secretary_of_State_portrait.jpg"></a>',
		  'George W. Bush':'<a title="White house photo by Eric Draper. [Public domain], via Wikimedia Commons" href="https://commons.wikimedia.org/wiki/File:George-W-Bush.jpeg"><img width="128"height="190" alt="George-W-Bush" src="https://upload.wikimedia.org/wikipedia/commons/thumb/d/d4/George-W-Bush.jpeg/128px-George-W-Bush.jpeg"></a>',
		  'George H. W. Bush':'<a title="See page for author [Public domain], via Wikimedia Commons" href="https://commons.wikimedia.org/wiki/File:George_H._W._Bush,_President_of_the_United_States,_1989_official_portrait_(cropped).jpg"><img width="128"height="190" alt="George H. W. Bush, President of the United States, 1989 official portrait (cropped)" src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/90/George_H._W._Bush%2C_President_of_the_United_States%2C_1989_official_portrait_%28cropped%29.jpg/128px-George_H._W._Bush%2C_President_of_the_United_States%2C_1989_official_portrait_%28cropped%29.jpg"></a>',
		  'Michael S. Dukakis':'<a title="Original image: O&#039;Halloran, Thomas J., photographer [Public domain], via Wikimedia Commons" href="https://commons.wikimedia.org/wiki/File:Governor_Dukakis_speaks_at_the_1976_Democratic_National_Convention_(cropped).jpg"><img width="128"height="190" alt="Governor Dukakis speaks at the 1976 Democratic National Convention (cropped)" src="https://upload.wikimedia.org/wikipedia/commons/thumb/b/bb/Governor_Dukakis_speaks_at_the_1976_Democratic_National_Convention_%28cropped%29.jpg/128px-Governor_Dukakis_speaks_at_the_1976_Democratic_National_Convention_%28cropped%29.jpg"></a>',
		  'Henry Ross Perot':'<a  href="https://upload.wikimedia.org/wikipedia/commons/b/b7/Ross_Perot_in_his_office_Allan_Warren_%28cropped%29.jpg"><img width="128"height="190" alt="RossPerot" src=""https://en.wikipedia.org/wiki/Ross_Perot#/media/File:Ross_Perot_in_his_office_Allan_Warren_(cropped).jpg"></a>',

		  'Joseph I. Lieberman':'<a title="See page for author [Public domain], via Wikimedia Commons" href="https://commons.wikimedia.org/wiki/File:Joe_Lieberman_official_portrait_2_(cropped_2).jpg"><img width="128"height="190" alt="Joe Lieberman official portrait 2 (cropped 2)" src="https://upload.wikimedia.org/wikipedia/commons/thumb/5/54/Joe_Lieberman_official_portrait_2_%28cropped_2%29.jpg/128px-Joe_Lieberman_official_portrait_2_%28cropped_2%29.jpg"></a>',
		  'Paul D. Ryan':'<a title="United States House of Representatives [Public domain], via Wikimedia Commons" href="https://commons.wikimedia.org/wiki/File:Paul_Ryan,_113th_Congress.png"><img width="128"height="190" alt="Paul Ryan, 113th Congress" src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/0f/Paul_Ryan%2C_113th_Congress.png/128px-Paul_Ryan%2C_113th_Congress.png"></a>',
		  'Geraldine A. Ferraro':'<a  href="https://en.wikipedia.org/wiki/Geraldine_Ferraro#/media/File:GERALDINE_FERRARO.jpg"><img width="128"height="190" alt="Ferraro" src="https://en.wikipedia.org/wiki/Geraldine_Ferraro#/media/File:GERALDINE_FERRARO.jpg"></a>'



}

	try:
		return images[name]
	except:
		return None





def CreateImgHtml(name):
	img_url = getImageURL(name)
	if(img_url!=None):
		html = '<div class = "debater-pic"><figure>'+getImageURL(name)+'<figcaption>'+str(name)+ '</figcaption></figure></div>'
	else:
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
