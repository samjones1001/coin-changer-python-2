  coverage run -m pytest
  zip lambda.zip coin_changer.py changer/*.py
  mkdir build
  cp lambda.zip build