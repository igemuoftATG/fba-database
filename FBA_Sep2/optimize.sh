#!/bin/bash

models_folder='models'
output_folder='solutions'

models=`ls $models_folder`

for model in $models
do
    python Optimize.py $models_folder/$model $output_folder/$model
done
