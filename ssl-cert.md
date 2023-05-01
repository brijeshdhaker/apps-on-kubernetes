#
# Generate Private Key
#
openssl genrsa -out ca.key 2048

#
# Generate Certificate Signing Request
#
openssl req -new -key ca.key  -subj "/CN=Kubernetes-CA" -out ca.csr

#
# Sign Certificate
#
openssl x509 -req -in ca.csr -signkey ca.key -out ca.crt

#
#
# view certificate
#
openssl x509 -in ca.crt -text -noout