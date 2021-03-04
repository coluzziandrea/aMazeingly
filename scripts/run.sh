#!/bin/sh
echo "RUN Script: Init..."


echo "RUN Script: Executing Example 1..."
python /amaze_app/amaze/app.py ./scripts/input_map_example_1.json 2 Knife 'Potted Plant'  


echo "RUN Script: Executing Example 2..."
python /amaze_app/amaze/app.py ./scripts/input_map_example_2.json 4 Knife 'Potted Plant' Pillow  


echo "RUN Script: Finish."