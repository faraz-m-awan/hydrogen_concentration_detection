import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score,make_scorer
import joblib


def trainModel(data_fp:str,target_variable:str)->RandomForestRegressor:
    df=pd.read_csv(data_fp)
    x=df.drop(columns=[target_variable])
    y=df[target_variable]

    x_train,x_test, y_train, y_test=train_test_split(x,y, test_size=0.33, random_state=42)

    scaler=StandardScaler()
    x_train_scaled=scaler.fit_transform(x_train)
    x_test_scaled=scaler.fit_transform(x_test)

    rf_model=RandomForestRegressor(n_estimators=100, random_state=42)
    
    mae_scorer=make_scorer(mean_absolute_error, greater_is_better=False)
    cross_val_mae=cross_val_score(rf_model, x_train_scaled,y_train, cv=5, scoring=mae_scorer)
    cross_val_r2=cross_val_score(rf_model, x_train_scaled,y_train, cv=5, scoring='r2')



    # Training on entire data
    rf_model.fit(x_train_scaled,y_train)
    y_pred_rf=rf_model.predict(x_test_scaled)
    mae_rf= mean_absolute_error(y_test,y_pred_rf)
    r2_rf= r2_score(y_test, y_pred_rf)

    print(f'************\nMAE: {mae_rf}\nr2:{r2_rf}')
    print(f'Cross Validation MAE: {-cross_val_mae.mean()}')
    print(f'Cross Validation r2: {cross_val_r2.mean()}')
    return rf_model


if __name__=='__main__':
    data_fp='hydrogen_concentration/data/processed_data.csv'
    target='hydrogen_ppm'

    model=trainModel(data_fp, target)

    save_model=input('Do you want to save model? (y/n):')
    save_model=save_model.lower()
    if save_model.lower()=='y':
        joblib.dump(model, 'hydrogen_concentration/model/rf_pred_hydrogen_concentration.joblib')
        print('Model saved!!!')