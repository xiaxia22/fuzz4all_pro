# Interface Certificate

**Source:** `java.base\java\security\Certificate.html`

### Class Description

```java
@Deprecated
(
since
="1.2",

forRemoval
=true)
public interface
Certificate
```

This is an interface of abstract methods for managing a
variety of identity certificates.
An identity certificate is a guarantee by a principal that
a public key is that of another principal. (A principal represents
an entity such as an individual user, a group, or a corporation.)

In particular, this interface is intended to be a common
abstraction for constructs that have different formats but
important common uses. For example, different types of
certificates, such as X.509 certificates and PGP certificates,
share general certificate functionality (the need to encode and
decode certificates) and some types of information, such as a
public key, the principal whose key it is, and the guarantor
guaranteeing that the public key is that of the specified
principal. So an implementation of X.509 certificates and an
implementation of PGP certificates can both utilize the Certificate
interface, even though their formats and additional types and
amounts of information stored are different.

Important

: This interface is useful for cataloging and
grouping objects sharing certain common uses. It does not have any
semantics of its own. In particular, a Certificate object does not
make any statement as to the

validity

of the binding. It is
the duty of the application implementing this interface to verify
the certificate and satisfy itself of its validity.

**Since:** 1.1
**See Also:** Certificate

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### Principal
getGuarantor()

Returns the guarantor of the certificate, that is, the principal
guaranteeing that the public key associated with this certificate
is that of the principal associated with this certificate. For X.509
certificates, the guarantor will typically be a Certificate Authority
(such as the United States Postal Service or Verisign, Inc.).

**Returns:**
- the guarantor which guaranteed the principal-key
binding.

---

#### Principal
getPrincipal()

Returns the principal of the principal-key pair being guaranteed by
the guarantor.

**Returns:**
- the principal to which this certificate is bound.

---

#### PublicKey
getPublicKey()

Returns the key of the principal-key pair being guaranteed by
the guarantor.

**Returns:**
- the public key that this certificate certifies belongs
to a particular principal.

---

#### void encode​(
OutputStream
stream)
throws
KeyException
,

IOException

Encodes the certificate to an output stream in a format that can
be decoded by the

decode

method.

**Parameters:**
- stream

- the output stream to which to encode the
certificate.

**Throws:**
- KeyException

- if the certificate is not
properly initialized, or data is missing, etc.
- IOException

- if a stream exception occurs while
trying to output the encoded certificate to the output stream.

**See Also:**
- decode(java.io.InputStream)

,

getFormat()

---

#### void decode​(
InputStream
stream)
throws
KeyException
,

IOException

Decodes a certificate from an input stream. The format should be
that returned by

getFormat

and produced by

encode

.

**Parameters:**
- stream

- the input stream from which to fetch the data
being decoded.

**Throws:**
- KeyException

- if the certificate is not properly initialized,
or data is missing, etc.
- IOException

- if an exception occurs while trying to input
the encoded certificate from the input stream.

**See Also:**
- encode(java.io.OutputStream)

,

getFormat()

---

#### String
getFormat()

Returns the name of the coding format. This is used as a hint to find
an appropriate parser. It could be "X.509", "PGP", etc. This is
the format produced and understood by the

encode

and

decode

methods.

**Returns:**
- the name of the coding format.

---

#### String
toString​(boolean detailed)

Returns a string that represents the contents of the certificate.

**Parameters:**
- detailed

- whether or not to give detailed information
about the certificate

**Returns:**
- a string representing the contents of the certificate

---

### Additional Sections

#### Interface Certificate

```java
@Deprecated
(
since
="1.2",

forRemoval
=true)
public interface
Certificate
```

Deprecated, for removal: This API element is subject to removal in a future version.

This class is deprecated and subject to removal in a future
version of Java SE. It has been replaced by

java.security.cert.Certificate

and related classes.

This is an interface of abstract methods for managing a
variety of identity certificates.
An identity certificate is a guarantee by a principal that
a public key is that of another principal. (A principal represents
an entity such as an individual user, a group, or a corporation.)

In particular, this interface is intended to be a common
abstraction for constructs that have different formats but
important common uses. For example, different types of
certificates, such as X.509 certificates and PGP certificates,
share general certificate functionality (the need to encode and
decode certificates) and some types of information, such as a
public key, the principal whose key it is, and the guarantor
guaranteeing that the public key is that of the specified
principal. So an implementation of X.509 certificates and an
implementation of PGP certificates can both utilize the Certificate
interface, even though their formats and additional types and
amounts of information stored are different.

Important

: This interface is useful for cataloging and
grouping objects sharing certain common uses. It does not have any
semantics of its own. In particular, a Certificate object does not
make any statement as to the

validity

of the binding. It is
the duty of the application implementing this interface to verify
the certificate and satisfy itself of its validity.

**Since:** 1.1
**See Also:** Certificate

@Deprecated

(

since

="1.2",

forRemoval

=true)
public interface

Certificate

This is an interface of abstract methods for managing a
variety of identity certificates.
An identity certificate is a guarantee by a principal that
a public key is that of another principal. (A principal represents
an entity such as an individual user, a group, or a corporation.)

In particular, this interface is intended to be a common
abstraction for constructs that have different formats but
important common uses. For example, different types of
certificates, such as X.509 certificates and PGP certificates,
share general certificate functionality (the need to encode and
decode certificates) and some types of information, such as a
public key, the principal whose key it is, and the guarantor
guaranteeing that the public key is that of the specified
principal. So an implementation of X.509 certificates and an
implementation of PGP certificates can both utilize the Certificate
interface, even though their formats and additional types and
amounts of information stored are different.

Important

: This interface is useful for cataloging and
grouping objects sharing certain common uses. It does not have any
semantics of its own. In particular, a Certificate object does not
make any statement as to the

validity

of the binding. It is
the duty of the application implementing this interface to verify
the certificate and satisfy itself of its validity.

In particular, this interface is intended to be a common
abstraction for constructs that have different formats but
important common uses. For example, different types of
certificates, such as X.509 certificates and PGP certificates,
share general certificate functionality (the need to encode and
decode certificates) and some types of information, such as a
public key, the principal whose key it is, and the guarantor
guaranteeing that the public key is that of the specified
principal. So an implementation of X.509 certificates and an
implementation of PGP certificates can both utilize the Certificate
interface, even though their formats and additional types and
amounts of information stored are different.

Important

: This interface is useful for cataloging and
grouping objects sharing certain common uses. It does not have any
semantics of its own. In particular, a Certificate object does not
make any statement as to the

validity

of the binding. It is
the duty of the application implementing this interface to verify
the certificate and satisfy itself of its validity.

Important

: This interface is useful for cataloging and
grouping objects sharing certain common uses. It does not have any
semantics of its own. In particular, a Certificate object does not
make any statement as to the

validity

of the binding. It is
the duty of the application implementing this interface to verify
the certificate and satisfy itself of its validity.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Deprecated Methods

Modifier and Type

Method

Description

void

decode

​(

InputStream

stream)

Deprecated, for removal: This API element is subject to removal in a future version.

Decodes a certificate from an input stream.

void

encode

​(

OutputStream

stream)

Deprecated, for removal: This API element is subject to removal in a future version.

Encodes the certificate to an output stream in a format that can
be decoded by the

decode

method.

String

getFormat

()

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the name of the coding format.

Principal

getGuarantor

()

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the guarantor of the certificate, that is, the principal
guaranteeing that the public key associated with this certificate
is that of the principal associated with this certificate.

Principal

getPrincipal

()

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the principal of the principal-key pair being guaranteed by
the guarantor.

PublicKey

getPublicKey

()

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the key of the principal-key pair being guaranteed by
the guarantor.

String

toString

​(boolean detailed)

Deprecated, for removal: This API element is subject to removal in a future version.

Returns a string that represents the contents of the certificate.

Method Summary

All Methods

Instance Methods

Abstract Methods

Deprecated Methods

Modifier and Type

Method

Description

void

decode

​(

InputStream

stream)

Deprecated, for removal: This API element is subject to removal in a future version.

Decodes a certificate from an input stream.

void

encode

​(

OutputStream

stream)

Deprecated, for removal: This API element is subject to removal in a future version.

Encodes the certificate to an output stream in a format that can
be decoded by the

decode

method.

String

getFormat

()

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the name of the coding format.

Principal

getGuarantor

()

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the guarantor of the certificate, that is, the principal
guaranteeing that the public key associated with this certificate
is that of the principal associated with this certificate.

Principal

getPrincipal

()

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the principal of the principal-key pair being guaranteed by
the guarantor.

PublicKey

getPublicKey

()

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the key of the principal-key pair being guaranteed by
the guarantor.

String

toString

​(boolean detailed)

Deprecated, for removal: This API element is subject to removal in a future version.

Returns a string that represents the contents of the certificate.

---

#### Method Summary

Deprecated, for removal: This API element is subject to removal in a future version.

Decodes a certificate from an input stream.

Encodes the certificate to an output stream in a format that can
be decoded by the

decode

method.

Returns the name of the coding format.

Returns the guarantor of the certificate, that is, the principal
guaranteeing that the public key associated with this certificate
is that of the principal associated with this certificate.

Returns the principal of the principal-key pair being guaranteed by
the guarantor.

Returns the key of the principal-key pair being guaranteed by
the guarantor.

Returns a string that represents the contents of the certificate.

============ METHOD DETAIL ==========

- Method Detail

- getGuarantor

```java
Principal
getGuarantor()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the guarantor of the certificate, that is, the principal
guaranteeing that the public key associated with this certificate
is that of the principal associated with this certificate. For X.509
certificates, the guarantor will typically be a Certificate Authority
(such as the United States Postal Service or Verisign, Inc.).

**Returns:** the guarantor which guaranteed the principal-key
binding.

- getPrincipal

```java
Principal
getPrincipal()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the principal of the principal-key pair being guaranteed by
the guarantor.

**Returns:** the principal to which this certificate is bound.

- getPublicKey

```java
PublicKey
getPublicKey()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the key of the principal-key pair being guaranteed by
the guarantor.

**Returns:** the public key that this certificate certifies belongs
to a particular principal.

- encode

```java
void encode​(
OutputStream
stream)
throws
KeyException
,

IOException
```

Deprecated, for removal: This API element is subject to removal in a future version.

Encodes the certificate to an output stream in a format that can
be decoded by the

decode

method.

**Parameters:** stream

- the output stream to which to encode the
certificate.
**Throws:** KeyException

- if the certificate is not
properly initialized, or data is missing, etc.
**Throws:** IOException

- if a stream exception occurs while
trying to output the encoded certificate to the output stream.
**See Also:** decode(java.io.InputStream)

,

getFormat()

- decode

```java
void decode​(
InputStream
stream)
throws
KeyException
,

IOException
```

Deprecated, for removal: This API element is subject to removal in a future version.

Decodes a certificate from an input stream. The format should be
that returned by

getFormat

and produced by

encode

.

**Parameters:** stream

- the input stream from which to fetch the data
being decoded.
**Throws:** KeyException

- if the certificate is not properly initialized,
or data is missing, etc.
**Throws:** IOException

- if an exception occurs while trying to input
the encoded certificate from the input stream.
**See Also:** encode(java.io.OutputStream)

,

getFormat()

- getFormat

```java
String
getFormat()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the name of the coding format. This is used as a hint to find
an appropriate parser. It could be "X.509", "PGP", etc. This is
the format produced and understood by the

encode

and

decode

methods.

**Returns:** the name of the coding format.

- toString

```java
String
toString​(boolean detailed)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns a string that represents the contents of the certificate.

**Parameters:** detailed

- whether or not to give detailed information
about the certificate
**Returns:** a string representing the contents of the certificate

Method Detail

- getGuarantor

```java
Principal
getGuarantor()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the guarantor of the certificate, that is, the principal
guaranteeing that the public key associated with this certificate
is that of the principal associated with this certificate. For X.509
certificates, the guarantor will typically be a Certificate Authority
(such as the United States Postal Service or Verisign, Inc.).

**Returns:** the guarantor which guaranteed the principal-key
binding.

- getPrincipal

```java
Principal
getPrincipal()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the principal of the principal-key pair being guaranteed by
the guarantor.

**Returns:** the principal to which this certificate is bound.

- getPublicKey

```java
PublicKey
getPublicKey()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the key of the principal-key pair being guaranteed by
the guarantor.

**Returns:** the public key that this certificate certifies belongs
to a particular principal.

- encode

```java
void encode​(
OutputStream
stream)
throws
KeyException
,

IOException
```

Deprecated, for removal: This API element is subject to removal in a future version.

Encodes the certificate to an output stream in a format that can
be decoded by the

decode

method.

**Parameters:** stream

- the output stream to which to encode the
certificate.
**Throws:** KeyException

- if the certificate is not
properly initialized, or data is missing, etc.
**Throws:** IOException

- if a stream exception occurs while
trying to output the encoded certificate to the output stream.
**See Also:** decode(java.io.InputStream)

,

getFormat()

- decode

```java
void decode​(
InputStream
stream)
throws
KeyException
,

IOException
```

Deprecated, for removal: This API element is subject to removal in a future version.

Decodes a certificate from an input stream. The format should be
that returned by

getFormat

and produced by

encode

.

**Parameters:** stream

- the input stream from which to fetch the data
being decoded.
**Throws:** KeyException

- if the certificate is not properly initialized,
or data is missing, etc.
**Throws:** IOException

- if an exception occurs while trying to input
the encoded certificate from the input stream.
**See Also:** encode(java.io.OutputStream)

,

getFormat()

- getFormat

```java
String
getFormat()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the name of the coding format. This is used as a hint to find
an appropriate parser. It could be "X.509", "PGP", etc. This is
the format produced and understood by the

encode

and

decode

methods.

**Returns:** the name of the coding format.

- toString

```java
String
toString​(boolean detailed)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns a string that represents the contents of the certificate.

**Parameters:** detailed

- whether or not to give detailed information
about the certificate
**Returns:** a string representing the contents of the certificate

---

#### Method Detail

getGuarantor

```java
Principal
getGuarantor()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the guarantor of the certificate, that is, the principal
guaranteeing that the public key associated with this certificate
is that of the principal associated with this certificate. For X.509
certificates, the guarantor will typically be a Certificate Authority
(such as the United States Postal Service or Verisign, Inc.).

**Returns:** the guarantor which guaranteed the principal-key
binding.

---

#### getGuarantor

Principal

getGuarantor()

Returns the guarantor of the certificate, that is, the principal
guaranteeing that the public key associated with this certificate
is that of the principal associated with this certificate. For X.509
certificates, the guarantor will typically be a Certificate Authority
(such as the United States Postal Service or Verisign, Inc.).

getPrincipal

```java
Principal
getPrincipal()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the principal of the principal-key pair being guaranteed by
the guarantor.

**Returns:** the principal to which this certificate is bound.

---

#### getPrincipal

Principal

getPrincipal()

Returns the principal of the principal-key pair being guaranteed by
the guarantor.

getPublicKey

```java
PublicKey
getPublicKey()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the key of the principal-key pair being guaranteed by
the guarantor.

**Returns:** the public key that this certificate certifies belongs
to a particular principal.

---

#### getPublicKey

PublicKey

getPublicKey()

Returns the key of the principal-key pair being guaranteed by
the guarantor.

encode

```java
void encode​(
OutputStream
stream)
throws
KeyException
,

IOException
```

Deprecated, for removal: This API element is subject to removal in a future version.

Encodes the certificate to an output stream in a format that can
be decoded by the

decode

method.

**Parameters:** stream

- the output stream to which to encode the
certificate.
**Throws:** KeyException

- if the certificate is not
properly initialized, or data is missing, etc.
**Throws:** IOException

- if a stream exception occurs while
trying to output the encoded certificate to the output stream.
**See Also:** decode(java.io.InputStream)

,

getFormat()

---

#### encode

void encode​(

OutputStream

stream)
throws

KeyException

,

IOException

Encodes the certificate to an output stream in a format that can
be decoded by the

decode

method.

decode

```java
void decode​(
InputStream
stream)
throws
KeyException
,

IOException
```

Deprecated, for removal: This API element is subject to removal in a future version.

Decodes a certificate from an input stream. The format should be
that returned by

getFormat

and produced by

encode

.

**Parameters:** stream

- the input stream from which to fetch the data
being decoded.
**Throws:** KeyException

- if the certificate is not properly initialized,
or data is missing, etc.
**Throws:** IOException

- if an exception occurs while trying to input
the encoded certificate from the input stream.
**See Also:** encode(java.io.OutputStream)

,

getFormat()

---

#### decode

void decode​(

InputStream

stream)
throws

KeyException

,

IOException

Decodes a certificate from an input stream. The format should be
that returned by

getFormat

and produced by

encode

.

getFormat

```java
String
getFormat()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the name of the coding format. This is used as a hint to find
an appropriate parser. It could be "X.509", "PGP", etc. This is
the format produced and understood by the

encode

and

decode

methods.

**Returns:** the name of the coding format.

---

#### getFormat

String

getFormat()

Returns the name of the coding format. This is used as a hint to find
an appropriate parser. It could be "X.509", "PGP", etc. This is
the format produced and understood by the

encode

and

decode

methods.

toString

```java
String
toString​(boolean detailed)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns a string that represents the contents of the certificate.

**Parameters:** detailed

- whether or not to give detailed information
about the certificate
**Returns:** a string representing the contents of the certificate

---

#### toString

String

toString​(boolean detailed)

Returns a string that represents the contents of the certificate.

---

