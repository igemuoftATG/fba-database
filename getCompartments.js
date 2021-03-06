// Generated by CoffeeScript 1.9.3
(function() {
  var arrayEquals, cmpts, compartments, file, files, fs, i, j, json_dir, json_models, k, key, l, len, len1, len2, len3, len4, len5, len6, m, metabolite, model, modelCompartments, n, o, p, ref, ref1, ref2, ref3, ref4, type,
    indexOf = [].indexOf || function(item) { for (var i = 0, l = this.length; i < l; i++) { if (i in this && this[i] === item) return i; } return -1; };

  fs = require("fs");

  arrayEquals = function(arr1, arr2) {
    var j, key, len;
    if (arr1.length !== arr2.length) {
      return false;
    }
    for (j = 0, len = arr1.length; j < len; j++) {
      key = arr1[j];
      if (indexOf.call(arr2, key) < 0) {
        return false;
      }
    }
    return true;
  };

  json_dir = process.argv[2];

  files = (function() {
    var j, len, ref, results;
    ref = fs.readdirSync(json_dir);
    results = [];
    for (j = 0, len = ref.length; j < len; j++) {
      file = ref[j];
      results.push(file);
    }
    return results;
  })();

  json_models = (function() {
    var j, len, results;
    results = [];
    for (j = 0, len = files.length; j < len; j++) {
      file = files[j];
      results.push(JSON.parse(fs.readFileSync(json_dir + "/" + file)));
    }
    return results;
  })();

  compartments = new Object();

  compartments.species = new Object();

  for (i = j = 0, len = json_models.length; j < len; i = ++j) {
    model = json_models[i];
    if (model.id === "") {
      model.id = "noId-" + i;
    }
    compartments.species[model.id] = new Object();
    modelCompartments = compartments.species[model.id].compartments = new Array;
    compartments.species[model.id].file = files[i];
    ref = model.metabolites;
    for (k = 0, len1 = ref.length; k < len1; k++) {
      metabolite = ref[k];
      if (ref1 = metabolite.compartment, indexOf.call(modelCompartments, ref1) < 0) {
        modelCompartments.push(metabolite.compartment);
      }
    }
  }

  compartments.types = new Array();

  for (i = l = 0, len2 = json_models.length; l < len2; i = ++l) {
    model = json_models[i];
    modelCompartments = compartments.species[model.id].compartments;
    if (indexOf.call((function() {
      var results;
      results = [];
      for (key in compartments.types) {
        results.push(arrayEquals(modelCompartments, compartments.types[key]));
      }
      return results;
    })(), true) < 0) {
      compartments.types.push(modelCompartments);
    }
  }

  compartments.compatibles = new Object();

  ref2 = compartments.types;
  for (i = m = 0, len3 = ref2.length; m < len3; i = ++m) {
    type = ref2[i];
    compartments.compatibles[i] = new Array();
  }

  for (n = 0, len4 = json_models.length; n < len4; n++) {
    model = json_models[n];
    ref3 = compartments.types;
    for (i = o = 0, len5 = ref3.length; o < len5; i = ++o) {
      type = ref3[i];
      if (arrayEquals(compartments.species[model.id].compartments, type)) {
        compartments.compatibles[i].push(model.id);
      }
    }
  }

  compartments.compartments = new Array();

  ref4 = compartments.types;
  for (i = p = 0, len6 = ref4.length; p < len6; i = ++p) {
    type = ref4[i];
    cmpts = {
      compartments: type,
      compatible: compartments.compatibles[i]
    };
    compartments.compartments.push(cmpts);
  }

  delete compartments.types;

  delete compartments.compatibles;

  fs.writeFileSync("compartments.json", JSON.stringify(compartments));

}).call(this);
