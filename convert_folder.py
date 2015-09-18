import sys
import cobra
import os


folder = 'Species'

for a,b,files in os.walk(folder):
    for file in files:
        if file[len(file)-4:] == '.xml':
            json_file = file[:len(file)-4] + '.json'

            success = False

            try:
                model = cobra.io.read_sbml_model(folder + '/' + file)
                success = True
            except ValueError:
                print 'failed for ' + file

            if success:
                cobra.io.save_json_model(model, folder + '/' + json_file)
                print "SBML at " + file + " --> " + "JSON at " + json_file 


# if (len(sys.argv) is not 3):
#     print "Usage: python convert_sbml_model_to_json.py <sbml_model> <json_model>"
#     quit()
#
# sbml_model = sys.argv[1]
# json_model = sys.argv[2]


# model = cobra.io.read_sbml_model(sbml_model)
# cobra.io.save_json_model(model, json_model)

# print "SBML at " + sbml_model + " --> " + "JSON at " + json_model
