import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC
from sklearn.pipeline import Pipeline
from sklearn import metrics
from sklearn.metrics import classification_report, f1_score
import pickle
import os.path
import plotly.offline as pyo
import plotly.graph_objs as go
import spacy
from nltk.stem.snowball import SnowballStemmer
from sklearn.feature_extraction.text import CountVectorizer

##데이터 로드 및 확인
data_dir = './MBTI_dataset/'

train = pd.read_csv(os.path.join(data_dir, 'MBTI_train_v3.csv'), encoding='ISO 8859-1', header=None, names=['type', 'posts'])
test = pd.read_csv(os.path.join(data_dir, 'MBTI_test_4.csv'), encoding='utf-8-sig', header=None, names=['posts'])

print(train.shape, test.shape) # 74357, 9337 -> (90833, 2) (16313, 1)
# train.head()
# test.head()

## 모델 로드 후 학습
# recreate_model=False
filename = 'mbti_svm_v2.sav'

if not os.path.isfile(filename):
    recreate_model=True

X = train['posts'] # features
y = train['type']  # labels
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# loading the model from disk
text_clf = pickle.load(open(filename, 'rb'))

# # 모델 재생성 여부 확인
# if recreate_model:    
    
#     # vectorizer 정의 및 fit_transform
#     vectorizer = TfidfVectorizer()
#     X_train_tfidf = vectorizer.fit_transform(X_train)
    
#     # 훈련
#     clf = LinearSVC()
#     clf.fit(X_train_tfidf, y_train)
    
#     # vectorizer 및 모델 파이프라인
#     text_clf = Pipeline([('tfidf',TfidfVectorizer()),('clf',LinearSVC())])
#     text_clf.fit(X_train, y_train)
    
#     # 모델 저장
#     pickle.dump(text_clf, open(filename, 'wb'))

# # 모델 재생성하지 않으면 기존 저장된 모델 불러오기
# else:
#     # loading the model from disk
#     text_clf = pickle.load(open(filename, 'rb'))

## 학습
predictions = text_clf.predict(X_test)

## 결과
predictions = text_clf.predict(test['posts'])
print(predictions)