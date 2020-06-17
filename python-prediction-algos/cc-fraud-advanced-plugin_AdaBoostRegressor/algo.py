# This file is the actual code for the custom Python algorithm cc-fraud-advanced-plugin_AdaBoostRegressor
from dataiku.doctor.plugins.custom_prediction_algorithm import BaseCustomPredictionAlgorithm
from sklearn.ensemble import AdaBoostRegressor

from sklearn.tree import DecisionTreeRegressor
from lightgbm import LGBMRegressor

class CustomPredictionAlgorithm(BaseCustomPredictionAlgorithm):    
    """
        Class defining the behaviour of `cc-fraud-advanced-plugin_AdaBoostRegressor` algorithm:
        - how it handles parameters passed to it
        - how the estimator works

        Example here defines an Adaboost Regressor from Scikit Learn that would work for regression
        (see https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.AdaBoostRegressor.html)

        You need to at least define a `get_clf` method that must return a scikit-learn compatible model

        Args:
            prediction_type (str): type of prediction for which the algorithm is used. Is relevant when 
                                   algorithm works for more than one type of prediction.
                                   Possible values are: "BINARY_CLASSIFICATION", "MULTICLASS", "REGRESSION"
            params (dict): dictionary of params set by the user in the UI.
    """
    
    def __init__(self, prediction_type=None, params=None):
        
        # First, determine the chosen base estimator
        
        # Get user-defined parameters
        
        
        # Assign the clf with the user-defined parameters
        self.clf = AdaBoostRegressor(random_state=params.get("random_state", None))
        super(CustomPredictionAlgorithm, self).__init__(prediction_type, params)
    
    def get_clf(self):
        """
        This method must return a scikit-learn compatible model, ie:
        - have a fit(X,y) and predict(X) methods. If sample weights
          are enabled for this algorithm (in algo.json), the fit method
          must have instead the signature fit(X, y, sample_weight=None)
        - have a get_params() and set_params(**params) methods
        """
        return self.clf