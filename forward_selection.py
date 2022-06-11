from tempfile import tempdir
from helper import evaluation
import pandas as pd 

def forward_selection(data, filename):
    n = data.shape[1]
    considered_features = []
    global_accuracy = 0
    global_features = []
    dict = {'Features':[],
        'Accuracy':[],
       }
  
    df = pd.DataFrame(dict)
    for _ in range(1,n):
        selected_features = []
        local_accuracy = 0

        for x in range(1, n):
            if x in considered_features:
                continue
            test_features = [0] + considered_features + [x]
            accuracy = evaluation(data[:,test_features])
            print("Features Considered : {features} with accuracy {accuracy}%".format(features=considered_features+[x], accuracy=accuracy))
            df_2=pd.DataFrame({'Features': [considered_features+[x]] , 'Accuracy': [accuracy]})
            df=df.append(df_2)

            if accuracy > local_accuracy:
                local_accuracy = accuracy
                selected_features = x 

        if selected_features:
            considered_features.append(selected_features)
            if local_accuracy > global_accuracy:
                global_accuracy = local_accuracy
                global_features[:] = considered_features
                print("\nFeature set"+considered_features+"was best, with accuracy"+local_accuracy)
            else:
                print("\nFeature set"+considered_features+"was best, with accuracy"+local_accuracy)
                print("\nFeature set {} was best, with accuracy {}\n".format(considered_features, local_accuracy))

    df.to_csv(filename+"_forward.csv", encoding='utf-8', index=False, sep =';')
    print("The best features are "+global_features+" which has an accuracy of" + global_accuracy)