import json
import numpy as np
import pickle
import config
import sys
sys.path.append(r"D:\VELOCITY_DATA\Project\Bank_telemarketing_Project")

class BankDeposit():

    def __init__(self, age, job,  housing, day, month, duration, poutcome):

       self.age = age
       self.job = job
       self.housing = housing
       self.day = day
       self.month = month
       self.duration = duration
       self.poutcome = poutcome

    def load_model(self):
        with open(config.JSON_FILE_PATH,'r')as f:
            self.json_data = json.load(f)

        with open(config.LABEL_ENCODED_DATA,'rb')as f:
            self.label_encode = pickle.load(f)

        with open(config.MODEL_FILE_PATH,'rb')as f:
            self.rf_model = pickle.load(f)

    def get_bank_analysis(self):

        self.load_model()
        test_array = np.zeros(len(self.json_data['columns']))

        test_array[0] = self.age
        test_array[1] = self.label_encode[0].transform([self.job])[0]
        test_array[2] = self.label_encode[4].transform([self.housing])
        test_array[3] = self.day
        test_array[4] = self.json_data['month'][self.month]
        test_array[5] = self.duration
        test_array[6] = self.label_encode[7].transform([self.poutcome])[0]


        predict_responce = self.rf_model.predict([test_array])[0]
        return predict_responce

       