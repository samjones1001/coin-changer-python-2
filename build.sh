  coverage run -m pytest
  cd changer
  zip ../lambda.zip changer.py
  cd ..
  mkdir build
  cp lambda.zip build