import sys
import cobra

if (len(sys.argv) is not 3):
    print "Usage: python convert_sbml_model_to_json.py <sbml_model> <json_model>"
    quit()

sbml_model = sys.argv[1]
json_model = sys.argv[2]


model = cobra.io.read_sbml_model(sbml_model)
cobra.io.save_json_model(model, json_model)

print "SBML at " + sbml_model + " --> " + "JSON at " + json_model
