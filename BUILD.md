## Build
To build this package:
1) run `python setup.py sdist bdist_wheel`
2) get a pypi token from our [PyPi](http://pypi.org) account
3) Add the token to `$HOME/.pypirc` under `[pypi]` (follow instructions from the pypi webpage)
4) run `python -m twine upload --repository pypi dist/*`
   (run `python -m twine upload --repository testpypi dist/*` to publish a tests to [Test.PyPi](http://test.pypi.org))