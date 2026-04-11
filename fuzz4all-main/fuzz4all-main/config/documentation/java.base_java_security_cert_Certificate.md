# Class Certificate

**Source:** `java.base\java\security\cert\Certificate.html`

### Class Description

```java
public abstract class
Certificate

extends
Object

implements
Serializable
```

Abstract class for managing a variety of identity certificates.
An identity certificate is a binding of a principal to a public key which
is vouched for by another principal. (A principal represents
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

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### protected Certificate​(
String
type)

Creates a certificate of the specified type.

**Parameters:**
- type

- the standard name of the certificate type.
See the CertificateFactory section in the

Java Security Standard Algorithm Names Specification

for information about standard certificate types.

---

### Method Details

#### public final
String
getType()

Returns the type of this certificate.

**Returns:**
- the type of this certificate.

---

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
- true iff the encoded forms of the two certificates
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
- the encoded form of this certificate

**Throws:**
- CertificateEncodingException

- if an encoding error occurs.

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

- on unsupported signature
algorithms.
- InvalidKeyException

- on incorrect key.
- NoSuchProviderException

- on incorrect provider.
- SignatureException

- on signature errors.
- CertificateException

- on encoding errors.

---

#### public void verify​(
PublicKey
key,

Provider
sigProvider)
throws
CertificateException
,

NoSuchAlgorithmException
,

InvalidKeyException
,

SignatureException

Verifies that this certificate was signed using the
private key that corresponds to the specified public key.
This method uses the signature verification engine
supplied by the specified provider. Note that the specified
Provider object does not have to be registered in the provider list.

This method was added to version 1.8 of the Java Platform
Standard Edition. In order to maintain backwards compatibility with
existing service providers, this method cannot be

abstract

and by default throws an

UnsupportedOperationException

.

**Parameters:**
- key

- the PublicKey used to carry out the verification.
- sigProvider

- the signature provider.

**Throws:**
- NoSuchAlgorithmException

- on unsupported signature
algorithms.
- InvalidKeyException

- on incorrect key.
- SignatureException

- on signature errors.
- CertificateException

- on encoding errors.
- UnsupportedOperationException

- if the method is not supported

**Since:**
- 1.8

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

#### protected
Object
writeReplace()
throws
ObjectStreamException

Replace the Certificate to be serialized.

**Returns:**
- the alternate Certificate object to be serialized

**Throws:**
- ObjectStreamException

- if a new object representing
this Certificate could not be created

**Since:**
- 1.3

---

### Additional Sections

#### Class Certificate

java.lang.Object

- java.security.cert.Certificate

java.security.cert.Certificate

**All Implemented Interfaces:** Serializable

**Direct Known Subclasses:** X509Certificate

```java
public abstract class
Certificate

extends
Object

implements
Serializable
```

Abstract class for managing a variety of identity certificates.
An identity certificate is a binding of a principal to a public key which
is vouched for by another principal. (A principal represents
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

**Since:** 1.2
**See Also:** X509Certificate

,

CertificateFactory

,

Serialized Form

public abstract class

Certificate

extends

Object

implements

Serializable

Abstract class for managing a variety of identity certificates.
An identity certificate is a binding of a principal to a public key which
is vouched for by another principal. (A principal represents
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

This class is an abstraction for certificates that have different
formats but important common uses. For example, different types of
certificates, such as X.509 and PGP, share general certificate
functionality (like encoding and verifying) and
some types of information (like a public key).

X.509, PGP, and SDSI certificates can all be implemented by
subclassing the Certificate class, even though they contain different
sets of information, and they store and retrieve the information in
different ways.

X.509, PGP, and SDSI certificates can all be implemented by
subclassing the Certificate class, even though they contain different
sets of information, and they store and retrieve the information in
different ways.

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

protected static class

Certificate.CertificateRep

Alternate Certificate class for serialization.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

Certificate

​(

String

type)

Creates a certificate of the specified type.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

boolean

equals

​(

Object

other)

Compares this certificate for equality with the specified
object.

abstract byte[]

getEncoded

()

Returns the encoded form of this certificate.

abstract

PublicKey

getPublicKey

()

Gets the public key from this certificate.

String

getType

()

Returns the type of this certificate.

int

hashCode

()

Returns a hashcode value for this certificate from its
encoded form.

abstract

String

toString

()

Returns a string representation of this certificate.

abstract void

verify

​(

PublicKey

key)

Verifies that this certificate was signed using the
private key that corresponds to the specified public key.

abstract void

verify

​(

PublicKey

key,

String

sigProvider)

Verifies that this certificate was signed using the
private key that corresponds to the specified public key.

void

verify

​(

PublicKey

key,

Provider

sigProvider)

Verifies that this certificate was signed using the
private key that corresponds to the specified public key.

protected

Object

writeReplace

()

Replace the Certificate to be serialized.

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

Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

protected static class

Certificate.CertificateRep

Alternate Certificate class for serialization.

---

#### Nested Class Summary

Alternate Certificate class for serialization.

Constructor Summary

Constructors

Modifier

Constructor

Description

protected

Certificate

​(

String

type)

Creates a certificate of the specified type.

---

#### Constructor Summary

Creates a certificate of the specified type.

Method Summary

All Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

boolean

equals

​(

Object

other)

Compares this certificate for equality with the specified
object.

abstract byte[]

getEncoded

()

Returns the encoded form of this certificate.

abstract

PublicKey

getPublicKey

()

Gets the public key from this certificate.

String

getType

()

Returns the type of this certificate.

int

hashCode

()

Returns a hashcode value for this certificate from its
encoded form.

abstract

String

toString

()

Returns a string representation of this certificate.

abstract void

verify

​(

PublicKey

key)

Verifies that this certificate was signed using the
private key that corresponds to the specified public key.

abstract void

verify

​(

PublicKey

key,

String

sigProvider)

Verifies that this certificate was signed using the
private key that corresponds to the specified public key.

void

verify

​(

PublicKey

key,

Provider

sigProvider)

Verifies that this certificate was signed using the
private key that corresponds to the specified public key.

protected

Object

writeReplace

()

Replace the Certificate to be serialized.

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

Compares this certificate for equality with the specified
object.

Returns the encoded form of this certificate.

Gets the public key from this certificate.

Returns the type of this certificate.

Returns a hashcode value for this certificate from its
encoded form.

Returns a string representation of this certificate.

Verifies that this certificate was signed using the
private key that corresponds to the specified public key.

Replace the Certificate to be serialized.

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
protected Certificate​(
String
type)
```

Creates a certificate of the specified type.

**Parameters:** type

- the standard name of the certificate type.
See the CertificateFactory section in the

Java Security Standard Algorithm Names Specification

for information about standard certificate types.

============ METHOD DETAIL ==========

- Method Detail

- getType

```java
public final
String
getType()
```

Returns the type of this certificate.

**Returns:** the type of this certificate.

- equals

```java
public boolean equals​(
Object
other)
```

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
**Returns:** true iff the encoded forms of the two certificates
match, false otherwise.
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
public int hashCode()
```

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

Returns the encoded form of this certificate. It is
assumed that each certificate type would have only a single
form of encoding; for example, X.509 certificates would
be encoded as ASN.1 DER.

**Returns:** the encoded form of this certificate
**Throws:** CertificateEncodingException

- if an encoding error occurs.

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

Verifies that this certificate was signed using the
private key that corresponds to the specified public key.
This method uses the signature verification engine
supplied by the specified provider.

**Parameters:** key

- the PublicKey used to carry out the verification.
**Parameters:** sigProvider

- the name of the signature provider.
**Throws:** NoSuchAlgorithmException

- on unsupported signature
algorithms.
**Throws:** InvalidKeyException

- on incorrect key.
**Throws:** NoSuchProviderException

- on incorrect provider.
**Throws:** SignatureException

- on signature errors.
**Throws:** CertificateException

- on encoding errors.

- verify

```java
public void verify​(
PublicKey
key,

Provider
sigProvider)
throws
CertificateException
,

NoSuchAlgorithmException
,

InvalidKeyException
,

SignatureException
```

Verifies that this certificate was signed using the
private key that corresponds to the specified public key.
This method uses the signature verification engine
supplied by the specified provider. Note that the specified
Provider object does not have to be registered in the provider list.

This method was added to version 1.8 of the Java Platform
Standard Edition. In order to maintain backwards compatibility with
existing service providers, this method cannot be

abstract

and by default throws an

UnsupportedOperationException

.

**Parameters:** key

- the PublicKey used to carry out the verification.
**Parameters:** sigProvider

- the signature provider.
**Throws:** NoSuchAlgorithmException

- on unsupported signature
algorithms.
**Throws:** InvalidKeyException

- on incorrect key.
**Throws:** SignatureException

- on signature errors.
**Throws:** CertificateException

- on encoding errors.
**Throws:** UnsupportedOperationException

- if the method is not supported
**Since:** 1.8

- toString

```java
public abstract
String
toString()
```

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

Gets the public key from this certificate.

**Returns:** the public key.

- writeReplace

```java
protected
Object
writeReplace()
throws
ObjectStreamException
```

Replace the Certificate to be serialized.

**Returns:** the alternate Certificate object to be serialized
**Throws:** ObjectStreamException

- if a new object representing
this Certificate could not be created
**Since:** 1.3

Constructor Detail

- Certificate

```java
protected Certificate​(
String
type)
```

Creates a certificate of the specified type.

**Parameters:** type

- the standard name of the certificate type.
See the CertificateFactory section in the

Java Security Standard Algorithm Names Specification

for information about standard certificate types.

---

#### Constructor Detail

Certificate

```java
protected Certificate​(
String
type)
```

Creates a certificate of the specified type.

**Parameters:** type

- the standard name of the certificate type.
See the CertificateFactory section in the

Java Security Standard Algorithm Names Specification

for information about standard certificate types.

---

#### Certificate

protected Certificate​(

String

type)

Creates a certificate of the specified type.

Method Detail

- getType

```java
public final
String
getType()
```

Returns the type of this certificate.

**Returns:** the type of this certificate.

- equals

```java
public boolean equals​(
Object
other)
```

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
**Returns:** true iff the encoded forms of the two certificates
match, false otherwise.
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
public int hashCode()
```

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

Returns the encoded form of this certificate. It is
assumed that each certificate type would have only a single
form of encoding; for example, X.509 certificates would
be encoded as ASN.1 DER.

**Returns:** the encoded form of this certificate
**Throws:** CertificateEncodingException

- if an encoding error occurs.

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

Verifies that this certificate was signed using the
private key that corresponds to the specified public key.
This method uses the signature verification engine
supplied by the specified provider.

**Parameters:** key

- the PublicKey used to carry out the verification.
**Parameters:** sigProvider

- the name of the signature provider.
**Throws:** NoSuchAlgorithmException

- on unsupported signature
algorithms.
**Throws:** InvalidKeyException

- on incorrect key.
**Throws:** NoSuchProviderException

- on incorrect provider.
**Throws:** SignatureException

- on signature errors.
**Throws:** CertificateException

- on encoding errors.

- verify

```java
public void verify​(
PublicKey
key,

Provider
sigProvider)
throws
CertificateException
,

NoSuchAlgorithmException
,

InvalidKeyException
,

SignatureException
```

Verifies that this certificate was signed using the
private key that corresponds to the specified public key.
This method uses the signature verification engine
supplied by the specified provider. Note that the specified
Provider object does not have to be registered in the provider list.

This method was added to version 1.8 of the Java Platform
Standard Edition. In order to maintain backwards compatibility with
existing service providers, this method cannot be

abstract

and by default throws an

UnsupportedOperationException

.

**Parameters:** key

- the PublicKey used to carry out the verification.
**Parameters:** sigProvider

- the signature provider.
**Throws:** NoSuchAlgorithmException

- on unsupported signature
algorithms.
**Throws:** InvalidKeyException

- on incorrect key.
**Throws:** SignatureException

- on signature errors.
**Throws:** CertificateException

- on encoding errors.
**Throws:** UnsupportedOperationException

- if the method is not supported
**Since:** 1.8

- toString

```java
public abstract
String
toString()
```

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

Gets the public key from this certificate.

**Returns:** the public key.

- writeReplace

```java
protected
Object
writeReplace()
throws
ObjectStreamException
```

Replace the Certificate to be serialized.

**Returns:** the alternate Certificate object to be serialized
**Throws:** ObjectStreamException

- if a new object representing
this Certificate could not be created
**Since:** 1.3

---

#### Method Detail

getType

```java
public final
String
getType()
```

Returns the type of this certificate.

**Returns:** the type of this certificate.

---

#### getType

public final

String

getType()

Returns the type of this certificate.

equals

```java
public boolean equals​(
Object
other)
```

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
**Returns:** true iff the encoded forms of the two certificates
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

Returns the encoded form of this certificate. It is
assumed that each certificate type would have only a single
form of encoding; for example, X.509 certificates would
be encoded as ASN.1 DER.

**Returns:** the encoded form of this certificate
**Throws:** CertificateEncodingException

- if an encoding error occurs.

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

Verifies that this certificate was signed using the
private key that corresponds to the specified public key.
This method uses the signature verification engine
supplied by the specified provider.

**Parameters:** key

- the PublicKey used to carry out the verification.
**Parameters:** sigProvider

- the name of the signature provider.
**Throws:** NoSuchAlgorithmException

- on unsupported signature
algorithms.
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

verify

```java
public void verify​(
PublicKey
key,

Provider
sigProvider)
throws
CertificateException
,

NoSuchAlgorithmException
,

InvalidKeyException
,

SignatureException
```

Verifies that this certificate was signed using the
private key that corresponds to the specified public key.
This method uses the signature verification engine
supplied by the specified provider. Note that the specified
Provider object does not have to be registered in the provider list.

This method was added to version 1.8 of the Java Platform
Standard Edition. In order to maintain backwards compatibility with
existing service providers, this method cannot be

abstract

and by default throws an

UnsupportedOperationException

.

**Parameters:** key

- the PublicKey used to carry out the verification.
**Parameters:** sigProvider

- the signature provider.
**Throws:** NoSuchAlgorithmException

- on unsupported signature
algorithms.
**Throws:** InvalidKeyException

- on incorrect key.
**Throws:** SignatureException

- on signature errors.
**Throws:** CertificateException

- on encoding errors.
**Throws:** UnsupportedOperationException

- if the method is not supported
**Since:** 1.8

---

#### verify

public void verify​(

PublicKey

key,

Provider

sigProvider)
throws

CertificateException

,

NoSuchAlgorithmException

,

InvalidKeyException

,

SignatureException

Verifies that this certificate was signed using the
private key that corresponds to the specified public key.
This method uses the signature verification engine
supplied by the specified provider. Note that the specified
Provider object does not have to be registered in the provider list.

This method was added to version 1.8 of the Java Platform
Standard Edition. In order to maintain backwards compatibility with
existing service providers, this method cannot be

abstract

and by default throws an

UnsupportedOperationException

.

This method was added to version 1.8 of the Java Platform
Standard Edition. In order to maintain backwards compatibility with
existing service providers, this method cannot be

abstract

and by default throws an

UnsupportedOperationException

.

toString

```java
public abstract
String
toString()
```

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

Gets the public key from this certificate.

**Returns:** the public key.

---

#### getPublicKey

public abstract

PublicKey

getPublicKey()

Gets the public key from this certificate.

writeReplace

```java
protected
Object
writeReplace()
throws
ObjectStreamException
```

Replace the Certificate to be serialized.

**Returns:** the alternate Certificate object to be serialized
**Throws:** ObjectStreamException

- if a new object representing
this Certificate could not be created
**Since:** 1.3

---

#### writeReplace

protected

Object

writeReplace()
throws

ObjectStreamException

Replace the Certificate to be serialized.

---

