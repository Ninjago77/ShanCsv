rmdir /s /q "./dist/"
pip install setuptools twine
python setup.py sdist
python -m twine upload --repository-url https://upload.pypi.org/legacy/ dist/*