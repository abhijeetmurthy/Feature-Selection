from helper import *
import pandas as pd
import matplotlib.pyplot as plt
def bacxward_elimination(data, filename):
    n = data.shape[1]
    current_features = list(range(1,n))
    global_accuracy = 0
    global_features = list(range(1,n))
    dict = {'Features':[],
        'Accuracy':[],
       }
    df = pd.DataFrame(dict)
    for i in range(1,n):
        selected_feaatures = []
        local_accuracy = 0
        for x in range(1, n):
            if x not in current_features:
                continue
            test = [n for n in current_features if n != x]
            accuracy = evaluation(data[:,[0]+test])
            print("Features Considered : {features} with accuracy {accuracy}%".format(features=test, accuracy=accuracy))
            df_2=pd.DataFrame({'Features': [test] , 'Accuracy': [accuracy]})
            df=df.append(df_2)
            if accuracy > local_accuracy:
                local_accuracy = accuracy
                selected_feaatures = x
        if selected_feaatures:
            current_features = [n for n in current_features if n != selected_feaatures]
            if local_accuracy > global_accuracy:
                global_accuracy = local_accuracy
                global_features[:] = current_features
                print("\nFeature set"+current_features+"was best, with accuracy"+local_accuracy)
            else:
                print("Discarded!")
                print("\nFeature set"+current_features+"was best, with accuracy"+local_accuracy)
    df.to_csv(filename+"_bacxward.csv", encoding='utf-8', index=False, sep =';')
    print("The best features are "+global_features+" which has an accuracy of" + global_accuracy)
