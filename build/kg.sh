#!/bin/sh
# index.html에 지식 색인(#kg)·꾸러미(#export)를 붙인다. ahnboat_lab_explainer 저장소 경로를 첫 인자로.
T=${1:-../ahnboat_lab_explainer}
python3 build/make_kg.py
python3 $T/packs/task/onto-retrofit/tools/retrofit.py index.html --kg kg/kg.json --refs kg/refs.json --meta kg/meta.json --backbone $T/data/backbone_stats.json
rm -f index.html.bak
