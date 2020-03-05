mkdir tonga
cd tonga
mkdir data app scripts notebooks
cd data
mkdir raw train test validation
cd ..
cd app
mkdir blueprints static templates .gitignore
touch app.py 
cd blueprints
mkdir home_page
cd home_page
touch __init__.py blueprint.py
cd ..
touch __init__.py
cd ../static
touch styles.css index.js
cd ../templates
touch base.html home.html
cd ../../scripts
touch preprocess.py model.py train.py




