import pickle 
import os 

class Predictor(): 
    def __init__(self):
        # Load model 
        self.nn = pickle.load(open(os.getcwd()+"/web_app/models/knn_model.pkl", "rb"))
        self.tfidf = pickle.load(open(os.getcwd()+"/web_app/models/knn_tfidf.pkl", "rb"))

    def predict(self,user_text,size=5): 
        # Create Vector 
        request = self.tfidf.transform([user_text])
        # Use knn model to calculate the top n strains 
        strain_ids = self.nn.kneighbors(request.todense(), n_neighbors=size)[1][0]
        return strain_ids