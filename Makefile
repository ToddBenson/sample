init:
		pip install -r requirements.txt

test:
		py.test --cov=kata tests/basic_tests.py
		py.test ./tests/basic_tests.py 
