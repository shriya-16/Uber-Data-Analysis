import pandas as pd
import pickle

df=pd.read_excel("C:\\Users\\hp\\uber Data Analysis\\new_data.csv ")

x=df[['Location','DateOfMonth','Weekday','Hour']]
y=df[['No of Bookings']]

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=57)

from sklearn.linear_model import Ridge
from sklearn.model_selection import GridSearchCV

ridge=Ridge()
parameters={'alpha':[1e-15,1e-10,1e-8,1e-3,1e-2,1,5,10,20,30,35,40,45,50,55,100]}
ridge_regressor=GridSearchCV(ridge,parameters,scoring='neg_mean_squared_error',cv=5)
ridge_regressor.fit(x,y)

pickle.dump(ridge_regressor, open('model.pkl','wb'))

model = pickle.load(open('model.pkl','rb'))
