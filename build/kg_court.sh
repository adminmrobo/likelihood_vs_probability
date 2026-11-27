#!/bin/sh
T=${1:-../ahnboat_lab_explainer}
python3 build/make_kg.py court
python3 $T/packs/task/onto-retrofit/tools/retrofit.py court.html --kg kg/court/kg.json --refs kg/court/refs.json --meta kg/court/meta.json --backbone $T/data/backbone_stats.json
rm -f court.html.bak
