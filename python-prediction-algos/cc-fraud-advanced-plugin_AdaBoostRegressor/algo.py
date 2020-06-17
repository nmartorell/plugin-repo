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
        
        # Get user-defined parameters for AdaBoost
        n_estimators = params["n_estimators"]
        learning_rate = params["learning_rate"]
        loss = params["loss"]
        random_state = params["random_state"]
            
        # Get base estimator
        base_estimator = params["base_estimator"]
            
        # Assign clf depending on choice of base_estimator
        if base_estimator == "decisiontree":
            
            # Get decision tree parameters
            max_depth_tree = params["max_depth_tree"]
            min_samples_split_tree = params["min_samples_split_tree"]
            min_samples_leaf_tree = params["min_samples_leaf_tree"]
            
            # Apply clf
            self.clf = AdaBoostRegressor(random_state=random_state,
                                         n_estimators=n_estimators,
                                         learning_rate=learning_rate,
                                         loss=loss,
                                         base_estimator=DecisionTreeRegressor(max_depth=max_depth_tree,
                                                                              min_samples_split=min_samples_split_tree,
                                                                              min_samples_leaf=min_samples_leaf_tree))
            
            super(CustomPredictionAlgorithm, self).__init__(prediction_type, params)
            
        elif base_estimator == "lightgbm":
            
            # Get lightgbm parameters
            max_depth_gbm = params["max_depth_gbm"]
            n_estimators_gbm = params["n_estimators_gbm"]
            min_child_samples_gbm = params["min_child_samples_gbm"]
            learning_rate_gbm = params["learning_rate_gbm"]
            
            # Apply clf
            self.clf = AdaBoostRegressor(random_state=random_state,
                                         n_estimators=n_estimators,
                                         learning_rate=learning_rate,
                                         loss=loss,
                                         base_estimator=LGBMRegressor(max_depth=max_depth_gbm,
                                                                      n_estimators=n_estimators_gbm,
                                                                      main_child_samples=main_child_samples_gbm,
                                                                      learning_rate=learning_rate_gbm))
            
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