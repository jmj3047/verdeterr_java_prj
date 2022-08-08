import sys
import csv
import time

def main():
    print("hello world before")
    import pandas as pd
    data_dir = './MBTI_dataset/'
    time.sleep(2)
    train = pd.read_csv('./MBTI_dataset/MBTI_train.csv', encoding='ISO 8859-1', header=None, names=['type', 'posts'])
    time.sleep(2)
    # with open('./MBTI_dataset/csvtest.csv', 'r', encoding='ISO 8859-1') as csvfile:
    #     train = csv.reader(csvfile, delimiter=' ', quotechar='|')
    #     for row in train:
    #         print(', '.join(row))
    #     # train = csv.reader('./MBTI_dataset/MBTI_train.csv', encoding='ISO 8859-1')
    #     # print(train)
    #     y = train['type']
    #     print(y)
    print("after the dataframe")

time.sleep(2)
print(sys.argv[1])
time.sleep(2)
main()
time.sleep(2)