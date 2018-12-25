import zipfile

zFile = zipfile.ZipFile("code.zip")
try:
	zFile.extractall(pwd="aaaaa")
except Exception, e:
    print e
