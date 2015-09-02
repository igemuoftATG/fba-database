#!/bin/bash

node integrateSolution.js models/Ecoli-K12-MG1655.json solutions/Ecoli-K12-MG1655_solution.json models_optimized/Ecoli-K12-MG1655_optimized.json
node integrateSolution.js models/Methanosarcina-barkeri-Fusaro-iMG746.json solutions/Methanosarcina-barkeri-Fusaro-iMG746_solution.json models_optimized/Methanosarcina-barkeri-Fusaro-iMG746_optimized.json
node integrateSolution.js models/Rhodobacter-sphaeroides.json solutions/Rhodobacter-sphaeroides_solution.json models_optimized/Rhodobacter-sphaeroides_optimized.json
