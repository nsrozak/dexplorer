from mlearn.datasets import SyntheticClassification

train_make_classification_kwargs = {'n_samples': 1000, 
                                    'n_features': 12,
                                    'n_informative': 12,
                                    'n_redundant': 0,
                                    'n_repeated': 0,
                                    'random_state': 123
                                   }
continuous_range = [(-100, 100), (10, 20), (0, 50), (-5, 5), 
                    (-5, 60), (100, 2000), (4, 90), (10, 12), (0, 70)
                    ]
categories_number = [3, 4, 7]

train_synthetic_classification = SyntheticClassification(
    make_classification_kwargs=train_make_classification_kwargs,
    continuous_range=continuous_range, 
    categories_number=categories_number
)
train_data = train_synthetic_classification.get_data()

train_data.to_csv('data.csv', index=False)