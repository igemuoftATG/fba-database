# For reading and writing JSONs
fs = require "fs"

# Return true if two arrays are identical. False otherwise.
# Order is not important.
arrayEquals = (arr1, arr2) ->
    if arr1.length isnt arr2.length
        return false

    for key in arr1
        if key not in arr2
            return false

    return true

# First CLI argument is directory containing only .json's
json_dir = process.argv[2]
# Parse each file in json_dir as JSON, store objects as array in json_models
files = (file for file in fs.readdirSync(json_dir))
json_models = (JSON.parse(fs.readFileSync("#{json_dir}/#{file}")) for file in files)

# The main object we will store compartment info in, and will be written to compartments.json
compartments = new Object()
# The species object
compartments.species = new Object()

# Loop through each metabolic model
for model,i in json_models
    # P. putida KT2440 has no ID
    if model.id is "" then model.id = "noId-#{i}"

    # Species object uses model IDs ad keys
    compartments.species[model.id] = new Object()
    # and have compartments (array) and file (string) attributes
    modelCompartments = compartments.species[model.id].compartments = new Array
    compartments.species[model.id].file = files[i]

    # Loop through each metabolite for a model
    for metabolite in model.metabolites
        # Add compartment to array if its not already there
        if metabolite.compartment not in modelCompartments
            modelCompartments.push(metabolite.compartment)

# Array of different types of groups of compartments
compartments.types = new Array()
for model,i in json_models
    modelCompartments = compartments.species[model.id].compartments
    if true not in (arrayEquals(modelCompartments, compartments.types[key]) for key of compartments.types)
        compartments.types.push(modelCompartments)

# Object for storing compatible models
compartments.compatibles = new Object()
# Instantiate empty array for each type of compartment group
for type, i in compartments.types
    compartments.compatibles[i] = new Array()

# Models are compatible if they employ the same group of compartments
for model in json_models
    for type, i in compartments.types
        if arrayEquals(compartments.species[model.id].compartments, type)
            compartments.compatibles[i].push(model.id)

# Because I didn't think ahead
compartments.compartments = new Array()
for type, i in compartments.types
    cmpts =
        compartments: type,
        compatible: compartments.compatibles[i]
    compartments.compartments.push(cmpts)
    
delete compartments.types
delete compartments.compatibles

# Write to filesystem
fs.writeFileSync("compartments.json", JSON.stringify(compartments))
