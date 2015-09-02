// Core NodeJS modules
var fs = require('fs');

// Command line arguments
model_file     = process.argv[2];
solution_file = process.argv[3];
output_file    = process.argv[4];

// [{id:'foo'}, ...] -> {foo: {id:'foo'}, ...}
function dictifyReactions(reactions) {
	var reactionsDict = new Object();

	reactions.forEach(function(reaction) {
		reactionsDict[reaction.id] = reaction;
	});

	return reactionsDict;
}

function integrateSolutions(reactionsDict, solution) {
	Object.keys(solution.x_dict).forEach(function(key) {
		reactionsDict[key].flux_value = solution.x_dict[key]
	})

	return reactionsDict;
}

function arrayifyReactions(reactionsDict) {
	var reactionsArray = new Array();

	Object.keys(reactionsDict).forEach(function(key) {
		reactionsArray.push(reactionsDict[key])
	})

	return reactionsArray;
}

// SMBL model stored as json
model = JSON.parse(fs.readFileSync(model_file));
reactions = dictifyReactions(model.reactions)
solution = JSON.parse(fs.readFileSync(solution_file))

reactionsWithFlux = integrateSolutions(reactions, solution)

reactionsWithFluxArray = arrayifyReactions(reactionsWithFlux)


// Push it back into the model
model.reactions = reactionsWithFluxArray

fs.writeFileSync(output_file, JSON.stringify(model))

console.log('Wrote ' + output_file)
