import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

data = pd.read_excel('data.xlsx')
print(data)
new = data[['平均气温（°C）', '累计降水量(mm)', '平均风速（m/s）', '平均气压(hPa)', '平均相对湿度(1%)', '质量等级']]
print(new)
test_x = new[['平均气温（°C）', '累计降水量(mm)', '平均风速（m/s）', '平均气压(hPa)', '平均相对湿度(1%)']]
test_y = new['质量等级']
Xtrain, Xtest, Ytrain, Ytest = train_test_split(test_x, test_y, test_size=0.3)

test = pd.read_excel('问题三测试数据.xlsx')

rfc = RandomForestClassifier()
rfc.fit(Xtrain, Ytrain)
y_predict = rfc.predict(Xtest)
print('随机森林准确率', rfc.score(Xtest, Ytest))

yPredict = rfc.predict(test)
print("predict:")
print(yPredict)
