
```shell
cd /home/brijeshdhaker/IdeaProjects/apps-on-kubernetes/open-ssl
mkdir -p root/ca
cd /root/ca
mkdir certs crl newcerts private
chmod 700 private
touch index.txt
echo 1000 > serial

```
#
## Create the root key
#
```shell
cd root/ca
openssl genrsa -aes256 -out private/ca.key.pem 4096

Enter pass phrase for ca.key.pem: secretpassword
Verifying - Enter pass phrase for ca.key.pem: secretpassword

chmod 400 private/ca.key.pem
```

#
## Create the root certificate
#
```shell
cd /root/ca
openssl req -config openssl.cnf \
      -key private/ca.key.pem \
      -new -x509 -days 7300 -sha256 -extensions v3_ca \
      -out certs/ca.cert.pem

Enter pass phrase for ca.key.pem: secretpassword
You are about to be asked to enter information that will be incorporated
into your certificate request.
-----
Country Name (2 letter code) [XX]:GB
State or Province Name []:England
Locality Name []:
Organization Name []:Alice Ltd
Organizational Unit Name []:Alice Ltd Certificate Authority
Common Name []:Alice Ltd Root CA
Email Address []:

chmod 444 certs/ca.cert.pem
```

#
## Verify the root certificate
#
```shell

openssl x509 -noout -text -in certs/ca.cert.pem

```
