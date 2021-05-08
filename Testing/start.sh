coverage run --include=venv/lib/python3.9/site-packages/Serializer/*,test.py,tests.py \
             --omit=*__init__.py \
             -m pytest test.py
coverage report