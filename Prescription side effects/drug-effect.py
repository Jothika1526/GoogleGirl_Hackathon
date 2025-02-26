import numpy as np
import pandas as pd
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.utils import to_categorical
import joblib  # For saving non-Keras models, if needed

# Load the dataset
df = pd.read_csv("drug-adverse-effect.csv")
print(df.head())
print(df.describe())
print(df.shape)
print(df.isna().sum())

# Prepare the new DataFrame
new_df = df[["safetyreportid", "patientonsetage", "patientsex", "medicinalproduct", "activesubstancename", "reactionmeddrapt"]].copy()
print(new_df.head())
print(new_df.isna().sum())

# Handle missing values
mean = new_df["patientonsetage"].mean()
new_df["patientonsetage"].fillna(value=mean, inplace=True)
new_df.dropna(inplace=True)
print(new_df.isna().sum())
print(new_df.shape)

# Process reactions
reaction = dict()
for effect in new_df['reactionmeddrapt']:
    for r in effect.split(", "):
        if reaction.get(r.lower()):
            reaction[r.lower()] += 1
        else:
            reaction[r.lower()] = 1

reactionList = {}
i = 1
unw = ['device issue', 'incorrect dose administered', 'wrong technique in product usage process', 'prostate cancer', 'off label use',
       'product dose omission issue', 'death', 'covid-19', 'therapy interrupted', 'inappropriate schedule of product administration',
       'fall']
for (k, v) in reaction.items():
    if v >= 120 and k not in unw:
        reactionList[k] = i
        i += 1
reactionList["others"] = i
print(len(reactionList))

# Process drugs
drug = dict()
for med in new_df['activesubstancename']:
    for m in med.split(" "):
        if drug.get(m.lower()):
            drug[m.lower()] += 1
        else:
            drug[m.lower()] = 1

drugList = {}
i = 1
for (k, v) in drug.items():
    if v >= 120:
        drugList[k] = i
        i += 1
drugList["others"] = i
print(len(drugList))
print(drugList)
print(reactionList)

# Create reaction and drug dictionaries
reactiondict = {key: [0] * len(new_df) for key in reactionList.keys()}
for i, effect in enumerate(new_df["reactionmeddrapt"]):
    reactions = effect.split(", ")
    found = False
    for k in reactions:
        if k.lower() in reactionList.keys():
            reactiondict[k.lower()][i] = 1
            found = True
    if not found:
        reactiondict["others"][i] = 1

print(sum(reactiondict["others"]))

drugdict = {key: [0] * len(new_df) for key in drugList.keys()}
for i, drug in enumerate(new_df["medicinalproduct"]):
    drugs = drug.split(", ")
    found = False
    for k in drugs:
        if k.lower() in drugList.keys():
            drugdict[k.lower()][i] = 1
            found = True
    if not found:
        drugdict["others"][i] = 1

print(sum(drugdict["others"]))

# Add drug information to DataFrame
for k, v in drugdict.items():
    new_df[k] = v

# Prepare feature matrix X and target matrix y
X = new_df.drop(["patientonsetage", "patientsex", "safetyreportid", "medicinalproduct", "activesubstancename", "reactionmeddrapt"], axis=1)
print(X.shape)
print(X.head())
y = pd.DataFrame(reactiondict)
print(y.shape)
print(y.head())

# Convert y to categorical if needed
y_categorical = y.values

# Train-test split
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, y_categorical, test_size=0.1, random_state=42)

# Create a Keras model
model = Sequential()
model.add(Dense(128, input_dim=X_train.shape[1], activation='relu'))
model.add(Dense(64, activation='relu'))
model.add(Dense(y_categorical.shape[1], activation='sigmoid'))  # Sigmoid for multi-label classification

model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# Train the model
model.fit(X_train, Y_train, epochs=20, batch_size=32, validation_split=0.1)

# Save the model in .h5 format
model.save('model.h5')

# Making predictions
Y_pred = model.predict(X_test)

# Evaluate the model
from sklearn.metrics import accuracy_score, recall_score

acc_score = accuracy_score(Y_test, (Y_pred > 0.5).astype(int))  # Convert probabilities to binary
rec_score = recall_score(Y_test, (Y_pred > 0.5).astype(int), average='macro')

print('Accuracy : %.4f%%, \t, Recall : %.4f%%' % (acc_score * 100, rec_score * 100))
