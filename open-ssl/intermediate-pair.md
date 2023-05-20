
```shell
cd /home/brijeshdhaker/IdeaProjects/apps-on-kubernetes/open-ssl
mkdir -p root/ca/intermediate
cd root/ca/intermediate
mkdir certs crl csr newcerts private
chmod 700 private
touch index.txt
echo 1000 > serial
echo 1000 > /root/ca/intermediate/crlnumber

```

#
## Create the intermediate key
#
```shell

cd /home/brijeshdhaker/IdeaProjects/apps-on-kubernetes/open-ssl/root/ca
openssl genrsa -aes256 \
      -out intermediate/private/intermediate.key.pem 4096

Enter pass phrase for intermediate.key.pem: secretpassword
Verifying - Enter pass phrase for intermediate.key.pem: secretpassword

chmod 400 intermediate/private/intermediate.key.pem

```


#
## Create the intermediate certificate
#
```shell

# cd /root/ca
# openssl req -config intermediate/openssl.cnf -new -sha256 \
      -key intermediate/private/intermediate.key.pem \
      -out intermediate/csr/intermediate.csr.pem

Enter pass phrase for intermediate.key.pem: secretpassword
You are about to be asked to enter information that will be incorporated
into your certificate request.
-----
Country Name (2 letter code) [XX]:GB
State or Province Name []:England
Locality Name []:
Organization Name []:Alice Ltd
Organizational Unit Name []:Alice Ltd Certificate Authority
Common Name []:Alice Ltd Intermediate CA
Email Address []:


# cd /root/ca
# openssl ca -config openssl.cnf -extensions v3_intermediate_ca \
      -days 3650 -notext -md sha256 \
      -in intermediate/csr/intermediate.csr.pem \
      -out intermediate/certs/intermediate.cert.pem

Enter pass phrase for ca.key.pem: secretpassword
Sign the certificate? [y/n]: y

# chmod 444 intermediate/certs/intermediate.cert.pem
```

#
## Verify the intermediate certificate
#
```shell
openssl x509 -noout -text \
      -in intermediate/certs/intermediate.cert.pem

openssl verify -CAfile certs/ca.cert.pem \
intermediate/certs/intermediate.cert.pem

intermediate.cert.pem: OK

```

#
## Create the certificate chain file
#
```shell

cat intermediate/certs/intermediate.cert.pem \
      certs/ca.cert.pem > intermediate/certs/ca-chain.cert.pem

chmod 444 intermediate/certs/ca-chain.cert.pem

```
