# Dataset Analysis

This is a dataset analysis project, it uses `pandas` and `YData Profiling` to do a statistical analysis of the dataset.
And then, it uses `sklearn` to do a machine learning analysis of the dataset (classification, regression, clustering, etc).


## Installation

```bash
chmod +x install.sh
./install.sh
```

## Usage

```bash
chmod +x run.sh
```

```bash
./run.sh --config config.json
```

## Configuration

### Default Configuration

Runs analysis with default configuration. Run for all datasets in the [LoadDataset](https://github.com/Olavo-B/LoadDataset) lib, and for this set of parameters:

| Model | Dataset Size (%) | Parameters | Variations |
| --- | --- | --- | --- |
| Naive Bayes | 10...100 | - | - |
| Logistic Regression | 10...100 | {'C': 1.0, 'penalty': 'l2'} | - |
| KNN | 10...100 | {'n_neighbors': 5, 'weights': 'uniform', 'algorithm': 'auto'} | - |
| Decision Tree | 10...100 | {'criterion': 'gini', 'max_depth': None, 'max_features': None} | - |
| Random Forest | 10...100 | {'n_estimators': 100, 'max_depth': None, 'max_features': 'auto'} | (3,3) ... (100,None) |
| Gradient Boosting | 10...100 | {'n_estimators': 100, 'max_depth': 3, 'learning_rate': 0.1} | (3,3) ... (100,None) |
| AdaBoost | 10...100 | {'n_estimators': 50, 'learning_rate': 1} | (3,1) ... (50,1) |
| XGBoost | 10...100 | {'n_estimators': 100, 'max_depth': 3, 'learning_rate': 0.1} | (3,3) ... (100,3) |


To run the default configuration, you can use the following command:

```bash
./run.sh
```

### Custom Configuration

You can also create a custom configuration file, and run the analysis with it.

```json
{
    "datasets": [
        {
            "name": "iris",
            "path": "misc/data/iris.csv",
            "size": [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
        }
    ],
    "profiling":
    {
        "title": "Custom Profiling Title",
        "parameters": {
            "minimal": "True",
            "explorative": "True"

        }
    },
    "models": [
        {
            "name": "Random Forest",
            "parameters": {
                "max_features": "auto"
            },
            "variations": [
                {
                    "n_estimators": 3,
                    "max_depth": 3
                },
                {
                    "n_estimators": 100,
                    "max_depth": null
                }
            ]
        }
    ]
}
```

To run the custom configuration, you can use the following command:

```bash
./run.sh --config custom_config.json
```

## Input Folder Structure

```bash
misc
├── data
│   ├── dataset_name.csv
```

Dataset is a CSV file with target column in the first column.


## Output Folder Structure

```bash
results
├── dataset_name
│   ├── dataset_name_profiling.html
│   ├── dataset_name_results.pdf
│   │   ├── model_name_dataset_name_results.json
│   │   ├── model_name_dataset_name_scatter_plot.png

```

## Requirements



## Contributing


