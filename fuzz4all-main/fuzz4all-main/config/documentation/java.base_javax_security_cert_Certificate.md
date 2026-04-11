# Class Certificate

**Source:** `java.base\javax\security\cert\Certificate.html`

### Class Description

```java
@Deprecated
(
since
="9")
public abstract class
Certificate

extends
Object
```

Abstract class for managing a variety of identity certificates.
An identity certificate is a guarantee by a principal that
a public key is that of another principal. (A principal represents
an entity such as an individual user, a group, or a corporation.)

This class is an abstraction for certificates that have different
formats but important common uses. For example, different types of
certificates, such as X.509 and PGP, share general certificate
functionality (like encoding and verifying) and
some types of information (like a public key).

X.509, PGP, and SDSI certificates can all be implemented by
subclassing the Certificate class, even though they contain different
sets of information, and they store and retrieve the information in
different ways.

Note: The classes in the package

javax.security.cert

exist for compatibility with earlier versions of the
Java Secure Sockets Extension (JSSE). New applications should instead
use the standard Java SE certificate classes located in

java.security.cert

.

**Direct Known Subclasses:** X509Certificate

---

### Field Details

*No entries found.*

### Constructor Details

#### public Certificate()

*No description found.*

---

### Method Details

#### public boolean equals​(
Object
other)

Compares this certificate for equality with the specified
object. If the

other

object is an

instanceof

Certificate

, then
its encoded form is retrieved and compared with the
encoded form of this certificate.

**Overrides:**
- equals

in class

Object

**Parameters:**
- other

- the object to test for equality with this certificate.

**Returns:**
- true if the encoded forms of the two certificates
match, false otherwise.

**See Also:**
- Object.hashCode()

,

HashMap

---

#### public int hashCode()

Returns a hashcode value for this certificate from its
encoded form.

**Overrides:**
- hashCode

in class

Object

**Returns:**
- the hashcode value.

**See Also:**
- Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### public abstract byte[] getEncoded()
throws
CertificateEncodingException

Returns the encoded form of this certificate. It is
assumed that each certificate type would have only a single
form of encoding; for example, X.509 certificates would
be encoded as ASN.1 DER.

**Returns:**
- encoded form of this certificate

**Throws:**
- CertificateEncodingException

- on internal certificate
encoding failure

---

#### public abstract void verify​(
PublicKey
key)
throws
CertificateException
,

NoSuchAlgorithmException
,

InvalidKeyException
,

NoSuchProviderException
,

SignatureException

Verifies that this certificate was signed using the
private key that corresponds to the specified public key.

**Parameters:**
- key

- the PublicKey used to carry out the verification.

**Throws:**
- NoSuchAlgorithmException

- on unsupported signature
algorithms.
- InvalidKeyException

- on incorrect key.
- NoSuchProviderException

- if there's no default provider.
- SignatureException

- on signature errors.
- CertificateException

- on encoding errors.

---

#### public abstract void verify​(
PublicKey
key,

String
sigProvider)
throws
CertificateException
,

NoSuchAlgorithmException
,

InvalidKeyException
,

NoSuchProviderException
,

SignatureException

Verifies that this certificate was signed using the
private key that corresponds to the specified public key.
This method uses the signature verification engine
supplied by the specified provider.

**Parameters:**
- key

- the PublicKey used to carry out the verification.
- sigProvider

- the name of the signature provider.

**Throws:**
- NoSuchAlgorithmException

- on unsupported signature algorithms.
- InvalidKeyException

- on incorrect key.
- NoSuchProviderException

- on incorrect provider.
- SignatureException

- on signature errors.
- CertificateException

- on encoding errors.

---

#### public abstract
String
toString()

Returns a string representation of this certificate.

**Overrides:**
- toString

in class

Object

**Returns:**
- a string representation of this certificate.

---

#### public abstract
PublicKey
getPublicKey()

Gets the public key from this certificate.

**Returns:**
- the public key.

---

### Additional Sections

#### Class Certificate

java.lang.Object

- javax.security.cert.Certificate

javax.security.cert.Certificate

**Direct Known Subclasses:** X509Certificate

```java
@Deprecated
(
since
="9")
public abstract class
Certificate

extends
Object
```

Deprecated.

Use the classes in

java.security.cert

instead.

Abstract class for managing a variety of identity certificates.
An identity certificate is a guarantee by a principal that
a public key is that of another principal. (A principal represents
an entity such as an individual user, a group, or a corporation.)

This class is an abstraction for certificates that have different
formats but important common uses. For example, different types of
certificates, such as X.509 and PGP, share general certificate
functionality (like encoding and verifying) and
some types of information (like a public key).

X.509, PGP, and SDSI certificates can all be implemented by
subclassing the Certificate class, even though they contain different
sets of information, and they store and retrieve the information in
different ways.

Note: The classes in the package

javax.security.cert

exist for compatibility with earlier versions of the
Java Secure Sockets Extension (JSSE). New applications should instead
use the standard Java SE certificate classes located in

java.security.cert

.

**Since:** 1.4
**See Also:** X509Certificate

@Deprecated

(

since

="9")
public abstract class

Certificate

extends

Object

Abstract class for managing a variety of identity certificates.
An identity certificate is a guarantee by a principal that
a public key is that of another principal. (A principal represents
an entity such as an individual user, a group, or a corporation.)

This class is an abstraction for certificates that have different
formats but important common uses. For example, different types of
certificates, such as X.509 and PGP, share general certificate
functionality (like encoding and verifying) and
some types of information (like a public key).

X.509, PGP, and SDSI certificates can all be implemented by
subclassing the Certificate class, even though they contain different
sets of information, and they store and retrieve the information in
different ways.

Note: The classes in the package

javax.security.cert

exist for compatibility with earlier versions of the
Java Secure Sockets Extension (JSSE). New applications should instead
use the standard Java SE certificate classes located in

java.security.cert

.

This class is an abstraction for certificates that have different
formats but important common uses. For example, different types of
certificates, such as X.509 and PGP, share general certificate
functionality (like encoding and verifying) and
some types of information (like a public key).

X.509, PGP, and SDSI certificates can all be implemented by
subclassing the Certificate class, even though they contain different
sets of information, and they store and retrieve the information in
different ways.

Note: The classes in the package

javax.security.cert

exist for compatibility with earlier versions of the
Java Secure Sockets Extension (JSSE). New applications should instead
use the standard Java SE certificate classes located in

java.security.cert

.

X.509, PGP, and SDSI certificates can all be implemented by
subclassing the Certificate class, even though they contain different
sets of information, and they store and retrieve the information in
different ways.

Note: The classes in the package

javax.security.cert

exist for compatibility with earlier versions of the
Java Secure Sockets Extension (JSSE). New applications should instead
use the standard Java SE certificate classes located in

java.security.cert

.

Note: The classes in the package

javax.security.cert

exist for compatibility with earlier versions of the
Java Secure Sockets Extension (JSSE). New applications should instead
use the standard Java SE certificate classes located in

java.security.cert

.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

Certificate

()

Deprecated.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Concrete Methods

Deprecated Methods

Modifier and Type

Method

Description

boolean

equals

​(

Object

other)

Deprecated.

Compares this certificate for equality with the specified
object.

abstract byte[]

getEncoded

()

Deprecated.

Returns the encoded form of this certificate.

abstract

PublicKey

getPublicKey

()

Deprecated.

Gets the public key from this certificate.

int

hashCode

()

Deprecated.

Returns a hashcode value for this certificate from its
encoded form.

abstract

String

toString

()

Deprecated.

Returns a string representation of this certificate.

abstract void

verify

​(

PublicKey

key)

Deprecated.

Verifies that this certificate was signed using the
private key that corresponds to the specified public key.

abstract void

verify

​(

PublicKey

key,

String

sigProvider)

Deprecated.

Verifies that this certificate was signed using the
private key that corresponds to the specified public key.

- Methods declared in class java.lang.

Object

clone

,

finalize

,

getClass

,

notify

,

notifyAll

,

wait

,

wait

,

wait

Constructor Summary

Constructors

Constructor

Description

Certificate

()

Deprecated.

---

#### Constructor Summary

Deprecated.

Method Summary

All Methods

Instance Methods

Abstract Methods

Concrete Methods

Deprecated Methods

Modifier and Type

Method

Description

boolean

equals

​(

Object

other)

Deprecated.

Compares this certificate for equality with the specified
object.

abstract byte[]

getEncoded

()

Deprecated.

Returns the encoded form of this certificate.

abstract

PublicKey

getPublicKey

()

Deprecated.

Gets the public key from this certificate.

int

hashCode

()

Deprecated.

Returns a hashcode value for this certificate from its
encoded form.

abstract

String

toString

()

Deprecated.

Returns a string representation of this certificate.

abstract void

verify

​(

PublicKey

key)

Deprecated.

Verifies that this certificate was signed using the
private key that corresponds to the specified public key.

abstract void

verify

​(

PublicKey

key,

String

sigProvider)

Deprecated.

Verifies that this certificate was signed using the
private key that corresponds to the specified public key.

- Methods declared in class java.lang.

Object

clone

,

finalize

,

getClass

,

notify

,

notifyAll

,

wait

,

wait

,

wait

---

#### Method Summary

Deprecated.

Compares this certificate for equality with the specified
object.

Returns the encoded form of this certificate.

Gets the public key from this certificate.

Returns a hashcode value for this certificate from its
encoded form.

Returns a string representation of this certificate.

Verifies that this certificate was signed using the
private key that corresponds to the specified public key.

Methods declared in class java.lang.

Object

clone

,

finalize

,

getClass

,

notify

,

notifyAll

,

wait

,

wait

,

wait

---

#### Methods declared in class java.lang. Object

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- Certificate

```java
public Certificate()
```

Deprecated.

============ METHOD DETAIL ==========

- Method Detail

- equals

```java
public boolean equals​(
Object
other)
```

Deprecated.

Compares this certificate for equality with the specified
object. If the

other

object is an

instanceof

Certificate

, then
its encoded form is retrieved and compared with the
encoded form of this certificate.

**Overrides:** equals

in class

Object
**Parameters:** other

- the object to test for equality with this certificate.
**Returns:** true if the encoded forms of the two certificates
match, false otherwise.
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
public int hashCode()
```

Deprecated.

Returns a hashcode value for this certificate from its
encoded form.

**Overrides:** hashCode

in class

Object
**Returns:** the hashcode value.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

- getEncoded

```java
public abstract byte[] getEncoded()
throws
CertificateEncodingException
```

Deprecated.

Returns the encoded form of this certificate. It is
assumed that each certificate type would have only a single
form of encoding; for example, X.509 certificates would
be encoded as ASN.1 DER.

**Returns:** encoded form of this certificate
**Throws:** CertificateEncodingException

- on internal certificate
encoding failure

- verify

```java
public abstract void verify​(
PublicKey
key)
throws
CertificateException
,

NoSuchAlgorithmException
,

InvalidKeyException
,

NoSuchProviderException
,

SignatureException
```

Deprecated.

Verifies that this certificate was signed using the
private key that corresponds to the specified public key.

**Parameters:** key

- the PublicKey used to carry out the verification.
**Throws:** NoSuchAlgorithmException

- on unsupported signature
algorithms.
**Throws:** InvalidKeyException

- on incorrect key.
**Throws:** NoSuchProviderException

- if there's no default provider.
**Throws:** SignatureException

- on signature errors.
**Throws:** CertificateException

- on encoding errors.

- verify

```java
public abstract void verify​(
PublicKey
key,

String
sigProvider)
throws
CertificateException
,

NoSuchAlgorithmException
,

InvalidKeyException
,

NoSuchProviderException
,

SignatureException
```

Deprecated.

Verifies that this certificate was signed using the
private key that corresponds to the specified public key.
This method uses the signature verification engine
supplied by the specified provider.

**Parameters:** key

- the PublicKey used to carry out the verification.
**Parameters:** sigProvider

- the name of the signature provider.
**Throws:** NoSuchAlgorithmException

- on unsupported signature algorithms.
**Throws:** InvalidKeyException

- on incorrect key.
**Throws:** NoSuchProviderException

- on incorrect provider.
**Throws:** SignatureException

- on signature errors.
**Throws:** CertificateException

- on encoding errors.

- toString

```java
public abstract
String
toString()
```

Deprecated.

Returns a string representation of this certificate.

**Overrides:** toString

in class

Object
**Returns:** a string representation of this certificate.

- getPublicKey

```java
public abstract
PublicKey
getPublicKey()
```

Deprecated.

Gets the public key from this certificate.

**Returns:** the public key.

Constructor Detail

- Certificate

```java
public Certificate()
```

Deprecated.

---

#### Constructor Detail

Certificate

```java
public Certificate()
```

Deprecated.

---

#### Certificate

public Certificate()

Method Detail

- equals

```java
public boolean equals​(
Object
other)
```

Deprecated.

Compares this certificate for equality with the specified
object. If the

other

object is an

instanceof

Certificate

, then
its encoded form is retrieved and compared with the
encoded form of this certificate.

**Overrides:** equals

in class

Object
**Parameters:** other

- the object to test for equality with this certificate.
**Returns:** true if the encoded forms of the two certificates
match, false otherwise.
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
public int hashCode()
```

Deprecated.

Returns a hashcode value for this certificate from its
encoded form.

**Overrides:** hashCode

in class

Object
**Returns:** the hashcode value.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

- getEncoded

```java
public abstract byte[] getEncoded()
throws
CertificateEncodingException
```

Deprecated.

Returns the encoded form of this certificate. It is
assumed that each certificate type would have only a single
form of encoding; for example, X.509 certificates would
be encoded as ASN.1 DER.

**Returns:** encoded form of this certificate
**Throws:** CertificateEncodingException

- on internal certificate
encoding failure

- verify

```java
public abstract void verify​(
PublicKey
key)
throws
CertificateException
,

NoSuchAlgorithmException
,

InvalidKeyException
,

NoSuchProviderException
,

SignatureException
```

Deprecated.

Verifies that this certificate was signed using the
private key that corresponds to the specified public key.

**Parameters:** key

- the PublicKey used to carry out the verification.
**Throws:** NoSuchAlgorithmException

- on unsupported signature
algorithms.
**Throws:** InvalidKeyException

- on incorrect key.
**Throws:** NoSuchProviderException

- if there's no default provider.
**Throws:** SignatureException

- on signature errors.
**Throws:** CertificateException

- on encoding errors.

- verify

```java
public abstract void verify​(
PublicKey
key,

String
sigProvider)
throws
CertificateException
,

NoSuchAlgorithmException
,

InvalidKeyException
,

NoSuchProviderException
,

SignatureException
```

Deprecated.

Verifies that this certificate was signed using the
private key that corresponds to the specified public key.
This method uses the signature verification engine
supplied by the specified provider.

**Parameters:** key

- the PublicKey used to carry out the verification.
**Parameters:** sigProvider

- the name of the signature provider.
**Throws:** NoSuchAlgorithmException

- on unsupported signature algorithms.
**Throws:** InvalidKeyException

- on incorrect key.
**Throws:** NoSuchProviderException

- on incorrect provider.
**Throws:** SignatureException

- on signature errors.
**Throws:** CertificateException

- on encoding errors.

- toString

```java
public abstract
String
toString()
```

Deprecated.

Returns a string representation of this certificate.

**Overrides:** toString

in class

Object
**Returns:** a string representation of this certificate.

- getPublicKey

```java
public abstract
PublicKey
getPublicKey()
```

Deprecated.

Gets the public key from this certificate.

**Returns:** the public key.

---

#### Method Detail

equals

```java
public boolean equals​(
Object
other)
```

Deprecated.

Compares this certificate for equality with the specified
object. If the

other

object is an

instanceof

Certificate

, then
its encoded form is retrieved and compared with the
encoded form of this certificate.

**Overrides:** equals

in class

Object
**Parameters:** other

- the object to test for equality with this certificate.
**Returns:** true if the encoded forms of the two certificates
match, false otherwise.
**See Also:** Object.hashCode()

,

HashMap

---

#### equals

public boolean equals​(

Object

other)

Compares this certificate for equality with the specified
object. If the

other

object is an

instanceof

Certificate

, then
its encoded form is retrieved and compared with the
encoded form of this certificate.

hashCode

```java
public int hashCode()
```

Deprecated.

Returns a hashcode value for this certificate from its
encoded form.

**Overrides:** hashCode

in class

Object
**Returns:** the hashcode value.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### hashCode

public int hashCode()

Returns a hashcode value for this certificate from its
encoded form.

getEncoded

```java
public abstract byte[] getEncoded()
throws
CertificateEncodingException
```

Deprecated.

Returns the encoded form of this certificate. It is
assumed that each certificate type would have only a single
form of encoding; for example, X.509 certificates would
be encoded as ASN.1 DER.

**Returns:** encoded form of this certificate
**Throws:** CertificateEncodingException

- on internal certificate
encoding failure

---

#### getEncoded

public abstract byte[] getEncoded()
throws

CertificateEncodingException

Returns the encoded form of this certificate. It is
assumed that each certificate type would have only a single
form of encoding; for example, X.509 certificates would
be encoded as ASN.1 DER.

verify

```java
public abstract void verify​(
PublicKey
key)
throws
CertificateException
,

NoSuchAlgorithmException
,

InvalidKeyException
,

NoSuchProviderException
,

SignatureException
```

Deprecated.

Verifies that this certificate was signed using the
private key that corresponds to the specified public key.

**Parameters:** key

- the PublicKey used to carry out the verification.
**Throws:** NoSuchAlgorithmException

- on unsupported signature
algorithms.
**Throws:** InvalidKeyException

- on incorrect key.
**Throws:** NoSuchProviderException

- if there's no default provider.
**Throws:** SignatureException

- on signature errors.
**Throws:** CertificateException

- on encoding errors.

---

#### verify

public abstract void verify​(

PublicKey

key)
throws

CertificateException

,

NoSuchAlgorithmException

,

InvalidKeyException

,

NoSuchProviderException

,

SignatureException

Verifies that this certificate was signed using the
private key that corresponds to the specified public key.

verify

```java
public abstract void verify​(
PublicKey
key,

String
sigProvider)
throws
CertificateException
,

NoSuchAlgorithmException
,

InvalidKeyException
,

NoSuchProviderException
,

SignatureException
```

Deprecated.

Verifies that this certificate was signed using the
private key that corresponds to the specified public key.
This method uses the signature verification engine
supplied by the specified provider.

**Parameters:** key

- the PublicKey used to carry out the verification.
**Parameters:** sigProvider

- the name of the signature provider.
**Throws:** NoSuchAlgorithmException

- on unsupported signature algorithms.
**Throws:** InvalidKeyException

- on incorrect key.
**Throws:** NoSuchProviderException

- on incorrect provider.
**Throws:** SignatureException

- on signature errors.
**Throws:** CertificateException

- on encoding errors.

---

#### verify

public abstract void verify​(

PublicKey

key,

String

sigProvider)
throws

CertificateException

,

NoSuchAlgorithmException

,

InvalidKeyException

,

NoSuchProviderException

,

SignatureException

Verifies that this certificate was signed using the
private key that corresponds to the specified public key.
This method uses the signature verification engine
supplied by the specified provider.

toString

```java
public abstract
String
toString()
```

Deprecated.

Returns a string representation of this certificate.

**Overrides:** toString

in class

Object
**Returns:** a string representation of this certificate.

---

#### toString

public abstract

String

toString()

Returns a string representation of this certificate.

getPublicKey

```java
public abstract
PublicKey
getPublicKey()
```

Deprecated.

Gets the public key from this certificate.

**Returns:** the public key.

---

#### getPublicKey

public abstract

PublicKey

getPublicKey()

Gets the public key from this certificate.

---

