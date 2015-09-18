import sys
import json
# COnstraint Based Reconstruction and Analysis
import cobra

# Get command line arguments
model_file = sys.argv[1]
out_file   = sys.argv[2]

# Load JSON model
model = cobra.io.load_json_model(model_file)

# Optimize for biomass
model.optimize()

# Create a dictionary out of Solution object
solution = {}
solution['f'] = model.solution.f
solution['status'] = model.solution.status
solution['x_dict'] = model.solution.x_dict
solution['x'] = model.solution.x
solution['y_dict'] = model.solution.y_dict
solution['y'] = model.solution.x

# Write solution dictionary to json file
solution_filename = out_file.split('.json')[0] + '_solution.json'
with open(solution_filename, 'w') as outfile:
    json.dump(solution, outfile)
print 'Dumped ' + solution_filename
