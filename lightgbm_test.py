import pickle
import lightgbm as lgb
import pandas as pd
from sklearn.metrics import accuracy_score
df = pd.read_csv("./input/df_final.csv")
df_test = pd.read_csv("./input/df_test_final.csv")
# 説明変数,目的変数
df_train = df.drop('angle',axis=1).values # 説明変数(target以外の特徴量)
train_labels = df['angle'].values  # 目的変数(target)
df_test = df.drop('angle',axis=1).values # 説明変数(target以外の特徴量)
test_labels = df['angle'].values  # 目的変数(target)

# 学習条件を設定
model = lgb.LGBMClassifier(objective='multiclass',
                        num_leaves = 23,
                        learning_rate=0.1,
                        n_estimators=100)

# 学習する
result = model.fit(df_train, train_labels,
                   eval_set=[(df_test, test_labels)],
                   eval_metric='multi_logloss',
                   early_stopping_rounds=20)
# テストデータで予測する
y_pred = model.predict(df_test, num_iteration=result.best_iteration_)
print(accuracy_score(test_labels, y_pred))

# importanceを表示する
df = df.drop('angle',axis=1)
importance = pd.DataFrame(model.feature_importances_, index=df.columns, columns=['importance'])
importance = importance.sort_values("importance", ascending=False)
importance.to_csv("./output_importance.csv")
# モデルを保存する
filename = './model/lightgbm_model.sav'
pickle.dump(model, open(filename, 'wb'))



