openssl genrsa -des3 -passout pass:x -out server.pass.key 2048
openssl rsa -passin pass:x -in server.pass.key -out server.key
openssl req -new -key server.key -out server.csr
openssl x509 -req -sha256 -days 365 -in server.csr -signkey server.key -out server.crt

python generateRSAKeys.py

rm server.pass.key
mv server.key server/certs/
mv server.csr server/certs/
cp server.crt server/certs/
mv server.crt client/
mv public.key server/
mv private.key client/
