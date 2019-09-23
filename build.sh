  coverage run -m pytest
  cd changer
  zip lambda.zip coin_changer.py change/*.py
  cd ..
  mkdir build
  cp lambda.zip build