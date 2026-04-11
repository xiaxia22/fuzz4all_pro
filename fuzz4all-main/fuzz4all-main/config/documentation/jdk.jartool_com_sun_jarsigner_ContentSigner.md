# Class ContentSigner

**Source:** `jdk.jartool\com\sun\jarsigner\ContentSigner.html`

### Class Description

```java
@Deprecated
(
since
="9")
public abstract class
ContentSigner

extends
Object
```

This class defines a content signing service.
Implementations must be instantiable using a zero-argument constructor.

**Since:** 1.5

---

### Field Details

*No entries found.*

### Constructor Details

#### public ContentSigner()

*No description found.*

---

### Method Details

#### public abstract byte[] generateSignedData​(
ContentSignerParameters
parameters,
boolean omitContent,
boolean applyTimestamp)
throws
NoSuchAlgorithmException
,

CertificateException
,

IOException

Generates a PKCS #7 signed data message.
This method is used when the signature has already been generated.
The signature, the signer's details, and optionally a signature
timestamp and the content that was signed, are all packaged into a
signed data message.

**Parameters:**
- parameters

- The non-null input parameters.
- omitContent

- true if the content should be omitted from the
signed data message. Otherwise the content is included.
- applyTimestamp

- true if the signature should be timestamped.
Otherwise timestamping is not performed.

**Returns:**
- A PKCS #7 signed data message.

**Throws:**
- NoSuchAlgorithmException

- The exception is thrown if the signature
algorithm is unrecognised.
- CertificateException

- The exception is thrown if an error occurs
while processing the signer's certificate or the TSA's
certificate.
- IOException

- The exception is thrown if an error occurs while
generating the signature timestamp or while generating the signed
data message.
- NullPointerException

- The exception is thrown if parameters is
null.

---

### Additional Sections

#### Class ContentSigner

java.lang.Object

- com.sun.jarsigner.ContentSigner

com.sun.jarsigner.ContentSigner

```java
@Deprecated
(
since
="9")
public abstract class
ContentSigner

extends
Object
```

Deprecated.

This class has been deprecated.

This class defines a content signing service.
Implementations must be instantiable using a zero-argument constructor.

**Since:** 1.5

@Deprecated

(

since

="9")
public abstract class

ContentSigner

extends

Object

This class defines a content signing service.
Implementations must be instantiable using a zero-argument constructor.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

ContentSigner

()

Deprecated.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Deprecated Methods

Modifier and Type

Method

Description

abstract byte[]

generateSignedData

​(

ContentSignerParameters

parameters,
boolean omitContent,
boolean applyTimestamp)

Deprecated.

Generates a PKCS #7 signed data message.

- Methods declared in class java.lang.

Object

clone

,

equals

,

finalize

,

getClass

,

hashCode

,

notify

,

notifyAll

,

toString

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

ContentSigner

()

Deprecated.

---

#### Constructor Summary

Deprecated.

Method Summary

All Methods

Instance Methods

Abstract Methods

Deprecated Methods

Modifier and Type

Method

Description

abstract byte[]

generateSignedData

​(

ContentSignerParameters

parameters,
boolean omitContent,
boolean applyTimestamp)

Deprecated.

Generates a PKCS #7 signed data message.

- Methods declared in class java.lang.

Object

clone

,

equals

,

finalize

,

getClass

,

hashCode

,

notify

,

notifyAll

,

toString

,

wait

,

wait

,

wait

---

#### Method Summary

Deprecated.

Generates a PKCS #7 signed data message.

Methods declared in class java.lang.

Object

clone

,

equals

,

finalize

,

getClass

,

hashCode

,

notify

,

notifyAll

,

toString

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

- ContentSigner

```java
public ContentSigner()
```

Deprecated.

============ METHOD DETAIL ==========

- Method Detail

- generateSignedData

```java
public abstract byte[] generateSignedData​(
ContentSignerParameters
parameters,
boolean omitContent,
boolean applyTimestamp)
throws
NoSuchAlgorithmException
,

CertificateException
,

IOException
```

Deprecated.

Generates a PKCS #7 signed data message.
This method is used when the signature has already been generated.
The signature, the signer's details, and optionally a signature
timestamp and the content that was signed, are all packaged into a
signed data message.

**Parameters:** parameters

- The non-null input parameters.
**Parameters:** omitContent

- true if the content should be omitted from the
signed data message. Otherwise the content is included.
**Parameters:** applyTimestamp

- true if the signature should be timestamped.
Otherwise timestamping is not performed.
**Returns:** A PKCS #7 signed data message.
**Throws:** NoSuchAlgorithmException

- The exception is thrown if the signature
algorithm is unrecognised.
**Throws:** CertificateException

- The exception is thrown if an error occurs
while processing the signer's certificate or the TSA's
certificate.
**Throws:** IOException

- The exception is thrown if an error occurs while
generating the signature timestamp or while generating the signed
data message.
**Throws:** NullPointerException

- The exception is thrown if parameters is
null.

Constructor Detail

- ContentSigner

```java
public ContentSigner()
```

Deprecated.

---

#### Constructor Detail

ContentSigner

```java
public ContentSigner()
```

Deprecated.

---

#### ContentSigner

public ContentSigner()

Method Detail

- generateSignedData

```java
public abstract byte[] generateSignedData​(
ContentSignerParameters
parameters,
boolean omitContent,
boolean applyTimestamp)
throws
NoSuchAlgorithmException
,

CertificateException
,

IOException
```

Deprecated.

Generates a PKCS #7 signed data message.
This method is used when the signature has already been generated.
The signature, the signer's details, and optionally a signature
timestamp and the content that was signed, are all packaged into a
signed data message.

**Parameters:** parameters

- The non-null input parameters.
**Parameters:** omitContent

- true if the content should be omitted from the
signed data message. Otherwise the content is included.
**Parameters:** applyTimestamp

- true if the signature should be timestamped.
Otherwise timestamping is not performed.
**Returns:** A PKCS #7 signed data message.
**Throws:** NoSuchAlgorithmException

- The exception is thrown if the signature
algorithm is unrecognised.
**Throws:** CertificateException

- The exception is thrown if an error occurs
while processing the signer's certificate or the TSA's
certificate.
**Throws:** IOException

- The exception is thrown if an error occurs while
generating the signature timestamp or while generating the signed
data message.
**Throws:** NullPointerException

- The exception is thrown if parameters is
null.

---

#### Method Detail

generateSignedData

```java
public abstract byte[] generateSignedData​(
ContentSignerParameters
parameters,
boolean omitContent,
boolean applyTimestamp)
throws
NoSuchAlgorithmException
,

CertificateException
,

IOException
```

Deprecated.

Generates a PKCS #7 signed data message.
This method is used when the signature has already been generated.
The signature, the signer's details, and optionally a signature
timestamp and the content that was signed, are all packaged into a
signed data message.

**Parameters:** parameters

- The non-null input parameters.
**Parameters:** omitContent

- true if the content should be omitted from the
signed data message. Otherwise the content is included.
**Parameters:** applyTimestamp

- true if the signature should be timestamped.
Otherwise timestamping is not performed.
**Returns:** A PKCS #7 signed data message.
**Throws:** NoSuchAlgorithmException

- The exception is thrown if the signature
algorithm is unrecognised.
**Throws:** CertificateException

- The exception is thrown if an error occurs
while processing the signer's certificate or the TSA's
certificate.
**Throws:** IOException

- The exception is thrown if an error occurs while
generating the signature timestamp or while generating the signed
data message.
**Throws:** NullPointerException

- The exception is thrown if parameters is
null.

---

#### generateSignedData

public abstract byte[] generateSignedData​(

ContentSignerParameters

parameters,
boolean omitContent,
boolean applyTimestamp)
throws

NoSuchAlgorithmException

,

CertificateException

,

IOException

Generates a PKCS #7 signed data message.
This method is used when the signature has already been generated.
The signature, the signer's details, and optionally a signature
timestamp and the content that was signed, are all packaged into a
signed data message.

---

