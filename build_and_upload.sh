./clean_directories.sh
python3 setup.py sdist bdist_wheel
python3 -m twine upload dist/*
