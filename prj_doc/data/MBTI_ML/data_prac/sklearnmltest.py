# from sklearn.datasets import load_diabetes
# from sklearn.tree import DecisionTreeRegressor
# from sklearn2pmml import PMMLPipeline, sklearn2pmml
# import pandas as pd
# # fetching data example
# df = load_diabetes()
# X = pd.DataFrame(columns = df.feature_names, data = df.get('data'))
# y = pd.DataFrame(columns = ['target'], data = df.get('target'))
# # here you can use the key classifier, if suitable
# pipeline = PMMLPipeline([ ('regressor', DecisionTreeRegressor()) ])
# #training the model
# pipeline.fit(X, y)
# # exporting the model
# sklearn2pmml(pipeline, 'model.pmml', with_repr = True)

from sklearn import tree
from sklearn2pmml.pipeline import PMMLPipeline
from sklearn2pmml import sklearn2pmml
from sklearn2pmml import make_pmml_pipeline # Convert pkl file to pmml_pipeline format

import os
os.environ["PATH"] += os.pathsep +'C:/Program Files/Java/jdk1.8.0_171/bin'

X=[[1,2,3,1],[2,4,1,5],[7,8,3,6],[4,8,4,7],[2,5,6, 9]]
y=[0,1,0,2,1]
# PMMLPipeline only handles estimator and cannot handle transformer
# Note: Sometimes you need to add custom functions to PMMLPipeline, you can refer to the blog https://blog.csdn.net/weixin_38569817/article/details/87810658
pipeline = PMMLPipeline([("classifier", tree.DecisionTreeClassifier(random_state=9))])
pipeline.fit(X,y)

sklearn2pmml(pipeline, ".\demo.pmml", with_repr = True)
