import keras
import scipy
from sklearn import metrics
from keras.models import load_model
import string
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
import pickle
import numpy as np
import json
import re
from string import punctuation
def pred2label(pred,inv_classes):
    out = []
    for pred_i in pred:

        out_i = []
        for p in pred_i:


            p_i = np.argmax(p)

            tag = inv_classes[p_i]
            out_i.append(tag)

        out.append(out_i)
    return out
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
	def __init__(self,cp = False,seq = False):
		save_directory = "data/arg/"
		if(cp== True):
			save_directory = "data/cp/"
		if(seq == True):
			    save_directory ="data/seq/"
		self.embedding_model = None
		self.max_len_sequence= 0
		self.coded_classes={}
		self.tokenizer = None
		self.seq = seq
		if(self.LoadModel(save_directory)):
			self.embedding_model._make_predict_function()
		else:
			pass
			#raise Exception("Could not load model in ", save_directory)



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
		import re
		test_sample = re.sub('(([^a-zA-Z]))', r' \1', test_sample)
		test_sample = re.sub('\s{2,}', ' ', test_sample)
		test_input_array=[test_sample]

		tokenized_test= self.tokenizer.texts_to_sequences(test_input_array)
		padded_test_x = pad_sequences(tokenized_test, maxlen=self.max_len_sequence, value = 0 ,padding = 'post')
		y_pred_class = self.embedding_model.predict(padded_test_x)

		inv_classes = {v: k for k, v in self.coded_classes.items()}

		if (self.seq != True):
		          return inv_classes[np.argmax(y_pred_class)]
		pred_labels = pred2label(y_pred_class, inv_classes)

		res=[]


		words = keras.preprocessing.text.text_to_word_sequence(test_sample,lower = False,filters='')
		pred_labels = pred_labels[0]
		pred_labels = pred_labels[0:len(words)]
		prev_label = "O"
		for i in range(max(len(words),len(prev_label))):
		          try:
                            index = self.tokenizer.word_index[words[i].lower()]
                            res.append((words[i],pred_labels[i]))

		          except:
                            res.append((words[i],prev_label))
		          prev_label = pred_labels[i]




		return res
