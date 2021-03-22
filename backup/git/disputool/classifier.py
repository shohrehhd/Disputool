import keras
import scipy 
from sklearn import metrics
from keras.models import load_model

from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
import pickle
import numpy as np
import json
import re
from string import punctuation

def preprocess(text):
   
    # lowercase
    text=text.lower()
    
    #remove tags
    text=re.sub("&lt;/?.*?&gt;"," &lt;&gt; ",text)
    #text=re.sub("\\s+","\\s",text)
    # remove special characters and digits
    text=re.sub("(\\W)+"," ",text)
    
    return text

#test_input = "I think I am the best"
#test_input = "I have been in this office for more than 10 years"
class Model:
	def __init__(self,cp = False):
		save_directory = "data/arg/"
		if(cp== True):
			save_directory = "data/cp/"
		self.embedding_model = None
		self.max_len_sequence= 0
		self.coded_classes={}
		self.tokenizer = None
		if(self.LoadModel(save_directory)):
			self.embedding_model._make_predict_function()



	def LoadModel(self,save_directory):
		try:
			self.embedding_model= load_model(save_directory+"/embedding_model")
		
			self.max_len_sequence = 0
			with open(save_directory+'/config.txt') as json_file:  
			   
			    config = json.loads(json_file.read())
			    self.max_len_sequence = config["max_length"]

			with open(save_directory+'/classes.txt') as json_file:  
			    self.coded_classes = json.loads(json_file.read())


			with open(save_directory+'/tokenizer.pickle', 'rb') as handle:
			    self.tokenizer = pickle.load(handle)
		except:
			return False
		    
		return True
	def TestModel(self,test_sample):
		test_input_array=[test_sample]
					
		tokenized_test= self.tokenizer.texts_to_sequences(test_input_array)
		padded_test_x = pad_sequences(tokenized_test, maxlen=self.max_len_sequence, value = 0 ,padding = 'post')
		y_pred_class = self.embedding_model.predict(padded_test_x)

		inv_classes = {v: k for k, v in self.coded_classes.items()}
		

		return inv_classes[np.argmax(y_pred_class)]
		
		 





