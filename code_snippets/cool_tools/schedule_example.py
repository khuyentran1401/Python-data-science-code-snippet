import schedule 
import time 

def get_incoming_data():
    print("Get incoming data")

def train_model():
    print("Retraining model")

schedule.every().day.at("10:30").do(get_incoming_data)
schedule.every().wednesday.at("08:00").do(train_model)

while True:
    schedule.run_pending()
    time.sleep(1)