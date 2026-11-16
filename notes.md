# MACHINE LEARNING PRACTICALS – RUN COMMANDS

## 1. Activate Environment

```bash
cd ~/Downloads/ML
source ml-env/bin/activate
```

## 2. Install Common Libraries

```bash
python -m pip install --upgrade pip
python -m pip install numpy pandas matplotlib scikit-learn xgboost
```

## EXPERIMENT 1 – LINEAR REGRESSION

```bash
python linear_regression.py
```

## EXPERIMENT 2 – NAIVE BAYES

```bash
python naive_bayes.py
```

## EXPERIMENT 3 – SUPPORT VECTOR MACHINE (SVM)

```bash
cd SVM_Practical
python -m pip install pandas scikit-learn
python svm.py
```

## EXPERIMENT 4 – K-MEANS CLUSTERING

```bash
cd ~/Downloads/ML
python kmeans_clustering.py
```

## EXPERIMENT 5 – RANDOM FOREST

```bash
cd Random_Forest
python -m pip install pandas scikit-learn
python random_forest.py
```

## EXPERIMENT 6 – BOOSTING

```bash
cd ~/Downloads/ML
python boosting.py
```

## EXPERIMENT 7 – Q-LEARNING (TAXI)

```bash
python -m pip install gymnasium[toy-text]
python taxi_qlearning.py
```

## EXPERIMENT 8 – Q-LEARNING (TIC TAC TOE)

```bash
python tic_tac_toe.py
```

## DEACTIVATE ENVIRONMENT

```bash
deactivate
```
