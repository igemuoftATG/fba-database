#!/bin/bash

sbml_dir=SBML-Lit
sbml_models=`ls $sbml_dir | grep .xml$`

for sbml_model in $sbml_models
do
    name=`echo $sbml_model | cut -d "." -f 1`
    python convert_sbml_model_to_json.py "$sbml_dir/$sbml_model" "JSON-Lit/$name.json" 
done
