mkdir -p usr/bin/
cp ../bin/phantomjs usr/bin/
sed -i -e 's#/home#.//./#g' usr/bin/phantomjs
rm phantomjs-aarch64.AppImage
../bin/appimagetool .
