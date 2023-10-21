# Mariano De Los Santos, Student ID 001523416

# import csv
import pandas as pd
from sklearn import metrics
from matplotlib import pyplot as plt

# Modelling
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

# set display-frame to read csv
df = pd.read_csv('incident_event_log_Clean.csv')
desc_one = pd.read_csv('incident_event_log_Raw.csv')

# ----------------
# split data
x = df.drop(columns='assignment_group')
y = df[['assignment_group']].copy()
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.20, random_state=41)

# reassign to arrays
y_train_array, y_test_array = y_train['assignment_group'].values, y_test['assignment_group'].values
x_train_array, x_test_array = x_train.values, x_test.values

# ---------------
# training

# random forest model
rf_model = RandomForestClassifier(n_estimators=100, max_depth=50, oob_score=True, random_state=41)
rf_model.fit(x_train_array, y_train_array)

# ----------
# Predictions

# predictions using train data
predictions_train = rf_model.predict(x_train_array)
score_train = metrics.accuracy_score(y_train_array, predictions_train)

# predictions using test data
predictions_test = rf_model.predict(x_test_array)
score_test = metrics.accuracy_score(y_test_array, predictions_test)


# -----------
# Visualization
# Descriptive Methods

# scatter plot of categories and groups
def cat_group_compare():
    desc_one.plot(kind='scatter', x='category', y='assignment_group')
    # display visual
    plt.show()


# Bar graph of different incident state
def inc_state_compare():
    desc_one["incident_state"].value_counts().plot(kind='bar')
    # display visual
    plt.show()


# bar chart of ticket reassignments
def reassign_compare():
    desc_one["reassignment_count"].value_counts().plot(kind='bar')
    # display visual
    plt.show()


# bar chart of reopened ticket
def reopened_compare():
    desc_one["reopen_count"].value_counts().plot(kind='bar')
    # display visual
    plt.show()


# model prediction accuracy
def predict_score():
    print()
    print("Training data accuracy: ", score_train)
    print("Test data accuracy: ", score_test)


# --------
# User Interface

def interface():
    print()
    print("Ticket Menu")
    input2 = "yes"
    # Begin loop
    while input2 == "yes":

        try:
            print("Please enter ticket details:")
            print("caller_id (Enter value 1 - 5642)")
            a = 0
            while a < 1 or a > 5642:
                value = int(input(": "))
                if 1 <= value <= 5642:
                    a = value
                else:
                    print("Invalid caller_id. Enter value (1 - 5642)")

            print("location (Enter value 1 - 249)")
            b = 0
            while b < 1 or b > 249:
                value = int(input(": "))
                if 1 <= value <= 249:
                    b = value
                else:
                    print("Invalid location. Enter value (1 - 249)")

            print("category (Enter value 1 - 63)")
            c = 0
            while c < 1 or c > 63:
                value = int(input(": "))
                if 1 <= value <= 63:
                    c = value
                else:
                    print("Invalid category. Enter value (1 - 63)")

            print("subcategory (Enter value 1 - 305)")
            d = 0
            while d < 1 or d > 305:
                value = int(input(": "))
                if 1 <= value <= 305:
                    d = value
                else:
                    print("Invalid subcategory. Enter value (1 - 305)")

            print("u_symptom (Enter value 1 - 609)")
            e = 0
            while e < 1 or e > 609:
                value = int(input(": "))
                if 1 <= value <= 609:
                    e = value
                else:
                    print("Invalid u_symptom. Enter value (1 - 609)")

            print("priority (Enter value 1 - 4)")
            f = 0
            while f < 1 or f > 4:
                value = int(input(": "))
                if 1 <= value <= 4:
                    f = value
                else:
                    print("Invalid priority. Enter value (1 - 4)")

            print("Please assign to: ", rf_model.predict([[a, b, c, d, e, f]]))
            # print(a, b, c, d, e, f)

        except ValueError:
            print("Entry invalid.")

        input2 = input("continue: yes or no? ")


def visuals():
    print()
    print("Data Menu")
    print("1 - categories vs groups, 2 - incident states, 3 - ticket reassignments, 4 - prediction accuracy, "
          "5 - reopened tickets")

    try:

        select = int(input("Choose 1-5: "))

        if select == 1:
            cat_group_compare()
        elif select == 2:
            inc_state_compare()
        elif select == 3:
            reassign_compare()
        elif select == 4:
            predict_score()
        elif select == 5:
            reopened_compare()

    except ValueError:
        print("INVALID ENTRY!.")


# -----------

class Main:
    loop = 'no'
    while loop == 'no':
        print()
        print("Main Menu")
        print("1 - Ticket prediction or 2 - Visual analysis")

        try:
            select = int(input("Choose 1 or 2: "))

            # User interface
            if select == 1:
                interface()

            # Visual analysis
            elif select == 2:
                visuals()

            print()
            loop = input("Exit program?: yes or no? ")

        except ValueError:
            print("INVALID ENTRY!")
