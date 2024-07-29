mkdir dist
cp src/driver.py dist/
cp Dockerfile dist/Dockerfile
zip -r dist/app.zip src -x driver.py