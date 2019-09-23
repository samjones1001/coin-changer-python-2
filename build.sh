  coverage run -m pytest
  zip lambda.zip coin_changer.py change/*.py
  mkdir build
  cp lambda.zip build