# Class X509Certificate

**Source:** `java.base\javax\security\cert\X509Certificate.html`

### Class Description

```java
@Deprecated
(
since
="9")
public abstract class
X509Certificate

extends
Certificate
```

Abstract class for X.509 v1 certificates. This provides a standard
way to access all the version 1 attributes of an X.509 certificate.
Attributes that are specific to X.509 v2 or v3 are not available
through this interface. Future API evolution will provide full access to
complete X.509 v3 attributes.

The basic X.509 format was defined by
ISO/IEC and ANSI X9 and is described below in ASN.1:

```java
Certificate ::= SEQUENCE {
tbsCertificate TBSCertificate,
signatureAlgorithm AlgorithmIdentifier,
signature BIT STRING }
```

These certificates are widely used to support authentication and
other functionality in Internet security systems. Common applications
include Privacy Enhanced Mail (PEM), Transport Layer Security (SSL),
code signing for trusted software distribution, and Secure Electronic
Transactions (SET).

These certificates are managed and vouched for by

Certificate
Authorities

(CAs). CAs are services which create certificates by
placing data in the X.509 standard format and then digitally signing
that data. CAs act as trusted third parties, making introductions
between principals who have no direct knowledge of each other.
CA certificates are either signed by themselves, or by some other
CA such as a "root" CA.

The ASN.1 definition of

tbsCertificate

is:

```java
TBSCertificate ::= SEQUENCE {
version [0] EXPLICIT Version DEFAULT v1,
serialNumber CertificateSerialNumber,
signature AlgorithmIdentifier,
issuer Name,
validity Validity,
subject Name,
subjectPublicKeyInfo SubjectPublicKeyInfo,
}
```

Here is sample code to instantiate an X.509 certificate:

```java
InputStream inStream = new FileInputStream("fileName-of-cert");
X509Certificate cert = X509Certificate.getInstance(inStream);
inStream.close();
```

OR

```java
byte[] certData = <certificate read from a file, say>
X509Certificate cert = X509Certificate.getInstance(certData);
```

In either case, the code that instantiates an X.509 certificate
consults the value of the

cert.provider.x509v1

security property
to locate the actual implementation or instantiates a default implementation.

The

cert.provider.x509v1

property is set to a default
implementation for X.509 such as:

```java
cert.provider.x509v1=com.sun.security.cert.internal.x509.X509V1CertImpl
```

The value of this

cert.provider.x509v1

property has to be
changed to instantiate another implementation. If this security
property is not set, a default implementation will be used.
Currently, due to possible security restrictions on access to
Security properties, this value is looked up and cached at class
initialization time and will fallback on a default implementation if
the Security property is not accessible.

Note: The classes in the package

javax.security.cert

exist for compatibility with earlier versions of the
Java Secure Sockets Extension (JSSE). New applications should instead
use the standard Java SE certificate classes located in

java.security.cert

.

**Since:** 1.4
**See Also:** Certificate

,

X509Extension

,

security properties

---

### Field Details

*No entries found.*

### Constructor Details

#### public X509Certificate()

*No description found.*

---

### Method Details

#### public static final
X509Certificate
getInstance​(
InputStream
inStream)
throws
CertificateException

Instantiates an X509Certificate object, and initializes it with
the data read from the input stream

inStream

.
The implementation (X509Certificate is an abstract class) is
provided by the class specified as the value of the

cert.provider.x509v1

security property.

Note: Only one DER-encoded
certificate is expected to be in the input stream.
Also, all X509Certificate
subclasses must provide a constructor of the form:

```java
public <subClass>(InputStream inStream) ...
```

**Parameters:**
- inStream

- an input stream with the data to be read to
initialize the certificate.

**Returns:**
- an X509Certificate object initialized with the data
from the input stream.

**Throws:**
- CertificateException

- if a class initialization
or certificate parsing error occurs.

---

#### public static final
X509Certificate
getInstance​(byte[] certData)
throws
CertificateException

Instantiates an X509Certificate object, and initializes it with
the specified byte array.
The implementation (X509Certificate is an abstract class) is
provided by the class specified as the value of the

cert.provider.x509v1

security property.

Note: All X509Certificate
subclasses must provide a constructor of the form:

```java
public <subClass>(InputStream inStream) ...
```

**Parameters:**
- certData

- a byte array containing the DER-encoded
certificate.

**Returns:**
- an X509Certificate object initialized with the data
from

certData

.

**Throws:**
- CertificateException

- if a class initialization
or certificate parsing error occurs.

---

#### public abstract void checkValidity()
throws
CertificateExpiredException
,

CertificateNotYetValidException

Checks that the certificate is currently valid. It is if
the current date and time are within the validity period given in the
certificate.

The validity period consists of two date/time values:
the first and last dates (and times) on which the certificate
is valid. It is defined in
ASN.1 as:

```java
validity Validity

Validity ::= SEQUENCE {
notBefore CertificateValidityDate,
notAfter CertificateValidityDate }

CertificateValidityDate ::= CHOICE {
utcTime UTCTime,
generalTime GeneralizedTime }
```

**Throws:**
- CertificateExpiredException

- if the certificate has expired.
- CertificateNotYetValidException

- if the certificate is not
yet valid.

---

#### public abstract void checkValidity​(
Date
date)
throws
CertificateExpiredException
,

CertificateNotYetValidException

Checks that the specified date is within the certificate's
validity period. In other words, this determines whether the
certificate would be valid at the specified date/time.

**Parameters:**
- date

- the Date to check against to see if this certificate
is valid at that date/time.

**Throws:**
- CertificateExpiredException

- if the certificate has expired
with respect to the

date

supplied.
- CertificateNotYetValidException

- if the certificate is not
yet valid with respect to the

date

supplied.

**See Also:**
- checkValidity()

---

#### public abstract int getVersion()

Gets the

version

(version number) value from the
certificate. The ASN.1 definition for this is:

```java
version [0] EXPLICIT Version DEFAULT v1

Version ::= INTEGER { v1(0), v2(1), v3(2) }
```

**Returns:**
- the version number from the ASN.1 encoding, i.e. 0, 1 or 2.

---

#### public abstract
BigInteger
getSerialNumber()

Gets the

serialNumber

value from the certificate.
The serial number is an integer assigned by the certification
authority to each certificate. It must be unique for each
certificate issued by a given CA (i.e., the issuer name and
serial number identify a unique certificate).
The ASN.1 definition for this is:

```java
serialNumber CertificateSerialNumber

CertificateSerialNumber ::= INTEGER
```

**Returns:**
- the serial number.

---

#### public abstract
Principal
getIssuerDN()

Gets the

issuer

(issuer distinguished name) value from
the certificate. The issuer name identifies the entity that signed (and
issued) the certificate.

The issuer name field contains an
X.500 distinguished name (DN).
The ASN.1 definition for this is:

```java
issuer Name

Name ::= CHOICE { RDNSequence }
RDNSequence ::= SEQUENCE OF RelativeDistinguishedName
RelativeDistinguishedName ::=
SET OF AttributeValueAssertion

AttributeValueAssertion ::= SEQUENCE {
AttributeType,
AttributeValue }
AttributeType ::= OBJECT IDENTIFIER
AttributeValue ::= ANY
```

The

Name

describes a hierarchical name composed of
attributes, such as country name, and corresponding values, such as US.
The type of the

AttributeValue

component is determined by
the

AttributeType

; in general it will be a

directoryString

. A

directoryString

is usually
one of

PrintableString

,

TeletexString

or

UniversalString

.

**Returns:**
- a Principal whose name is the issuer distinguished name.

---

#### public abstract
Principal
getSubjectDN()

Gets the

subject

(subject distinguished name) value
from the certificate.
The ASN.1 definition for this is:

```java
subject Name
```

See

getIssuerDN

for

Name

and other relevant definitions.

**Returns:**
- a Principal whose name is the subject name.

**See Also:**
- getIssuerDN()

---

#### public abstract
Date
getNotBefore()

Gets the

notBefore

date from the validity period of
the certificate.
The relevant ASN.1 definitions are:

```java
validity Validity

Validity ::= SEQUENCE {
notBefore CertificateValidityDate,
notAfter CertificateValidityDate }

CertificateValidityDate ::= CHOICE {
utcTime UTCTime,
generalTime GeneralizedTime }
```

**Returns:**
- the start date of the validity period.

**See Also:**
- checkValidity()

---

#### public abstract
Date
getNotAfter()

Gets the

notAfter

date from the validity period of
the certificate. See

getNotBefore

for relevant ASN.1 definitions.

**Returns:**
- the end date of the validity period.

**See Also:**
- checkValidity()

---

#### public abstract
String
getSigAlgName()

Gets the signature algorithm name for the certificate
signature algorithm. An example is the string "SHA-1/DSA".
The ASN.1 definition for this is:

```java
signatureAlgorithm AlgorithmIdentifier

AlgorithmIdentifier ::= SEQUENCE {
algorithm OBJECT IDENTIFIER,
parameters ANY DEFINED BY algorithm OPTIONAL }
-- contains a value of the type
-- registered for use with the
-- algorithm object identifier value
```

The algorithm name is determined from the

algorithm

OID string.

**Returns:**
- the signature algorithm name.

---

#### public abstract
String
getSigAlgOID()

Gets the signature algorithm OID string from the certificate.
An OID is represented by a set of positive whole numbers separated
by periods.
For example, the string "1.2.840.10040.4.3" identifies the SHA-1
with DSA signature algorithm, as per the PKIX part I.

See

getSigAlgName

for
relevant ASN.1 definitions.

**Returns:**
- the signature algorithm OID string.

---

#### public abstract byte[] getSigAlgParams()

Gets the DER-encoded signature algorithm parameters from this
certificate's signature algorithm. In most cases, the signature
algorithm parameters are null; the parameters are usually
supplied with the certificate's public key.

See

getSigAlgName

for
relevant ASN.1 definitions.

**Returns:**
- the DER-encoded signature algorithm parameters, or
null if no parameters are present.

---

### Additional Sections

#### Class X509Certificate

java.lang.Object

- javax.security.cert.Certificate
- - javax.security.cert.X509Certificate

javax.security.cert.Certificate

- javax.security.cert.X509Certificate

javax.security.cert.X509Certificate

```java
@Deprecated
(
since
="9")
public abstract class
X509Certificate

extends
Certificate
```

Deprecated.

Use the classes in

java.security.cert

instead.

Abstract class for X.509 v1 certificates. This provides a standard
way to access all the version 1 attributes of an X.509 certificate.
Attributes that are specific to X.509 v2 or v3 are not available
through this interface. Future API evolution will provide full access to
complete X.509 v3 attributes.

The basic X.509 format was defined by
ISO/IEC and ANSI X9 and is described below in ASN.1:

```java
Certificate ::= SEQUENCE {
tbsCertificate TBSCertificate,
signatureAlgorithm AlgorithmIdentifier,
signature BIT STRING }
```

These certificates are widely used to support authentication and
other functionality in Internet security systems. Common applications
include Privacy Enhanced Mail (PEM), Transport Layer Security (SSL),
code signing for trusted software distribution, and Secure Electronic
Transactions (SET).

These certificates are managed and vouched for by

Certificate
Authorities

(CAs). CAs are services which create certificates by
placing data in the X.509 standard format and then digitally signing
that data. CAs act as trusted third parties, making introductions
between principals who have no direct knowledge of each other.
CA certificates are either signed by themselves, or by some other
CA such as a "root" CA.

The ASN.1 definition of

tbsCertificate

is:

```java
TBSCertificate ::= SEQUENCE {
version [0] EXPLICIT Version DEFAULT v1,
serialNumber CertificateSerialNumber,
signature AlgorithmIdentifier,
issuer Name,
validity Validity,
subject Name,
subjectPublicKeyInfo SubjectPublicKeyInfo,
}
```

Here is sample code to instantiate an X.509 certificate:

```java
InputStream inStream = new FileInputStream("fileName-of-cert");
X509Certificate cert = X509Certificate.getInstance(inStream);
inStream.close();
```

OR

```java
byte[] certData = <certificate read from a file, say>
X509Certificate cert = X509Certificate.getInstance(certData);
```

In either case, the code that instantiates an X.509 certificate
consults the value of the

cert.provider.x509v1

security property
to locate the actual implementation or instantiates a default implementation.

The

cert.provider.x509v1

property is set to a default
implementation for X.509 such as:

```java
cert.provider.x509v1=com.sun.security.cert.internal.x509.X509V1CertImpl
```

The value of this

cert.provider.x509v1

property has to be
changed to instantiate another implementation. If this security
property is not set, a default implementation will be used.
Currently, due to possible security restrictions on access to
Security properties, this value is looked up and cached at class
initialization time and will fallback on a default implementation if
the Security property is not accessible.

Note: The classes in the package

javax.security.cert

exist for compatibility with earlier versions of the
Java Secure Sockets Extension (JSSE). New applications should instead
use the standard Java SE certificate classes located in

java.security.cert

.

**Since:** 1.4
**See Also:** Certificate

,

X509Extension

,

security properties

@Deprecated

(

since

="9")
public abstract class

X509Certificate

extends

Certificate

Abstract class for X.509 v1 certificates. This provides a standard
way to access all the version 1 attributes of an X.509 certificate.
Attributes that are specific to X.509 v2 or v3 are not available
through this interface. Future API evolution will provide full access to
complete X.509 v3 attributes.

The basic X.509 format was defined by
ISO/IEC and ANSI X9 and is described below in ASN.1:

```java
Certificate ::= SEQUENCE {
tbsCertificate TBSCertificate,
signatureAlgorithm AlgorithmIdentifier,
signature BIT STRING }
```

These certificates are widely used to support authentication and
other functionality in Internet security systems. Common applications
include Privacy Enhanced Mail (PEM), Transport Layer Security (SSL),
code signing for trusted software distribution, and Secure Electronic
Transactions (SET).

These certificates are managed and vouched for by

Certificate
Authorities

(CAs). CAs are services which create certificates by
placing data in the X.509 standard format and then digitally signing
that data. CAs act as trusted third parties, making introductions
between principals who have no direct knowledge of each other.
CA certificates are either signed by themselves, or by some other
CA such as a "root" CA.

The ASN.1 definition of

tbsCertificate

is:

```java
TBSCertificate ::= SEQUENCE {
version [0] EXPLICIT Version DEFAULT v1,
serialNumber CertificateSerialNumber,
signature AlgorithmIdentifier,
issuer Name,
validity Validity,
subject Name,
subjectPublicKeyInfo SubjectPublicKeyInfo,
}
```

Here is sample code to instantiate an X.509 certificate:

```java
InputStream inStream = new FileInputStream("fileName-of-cert");
X509Certificate cert = X509Certificate.getInstance(inStream);
inStream.close();
```

OR

```java
byte[] certData = <certificate read from a file, say>
X509Certificate cert = X509Certificate.getInstance(certData);
```

In either case, the code that instantiates an X.509 certificate
consults the value of the

cert.provider.x509v1

security property
to locate the actual implementation or instantiates a default implementation.

The

cert.provider.x509v1

property is set to a default
implementation for X.509 such as:

```java
cert.provider.x509v1=com.sun.security.cert.internal.x509.X509V1CertImpl
```

The value of this

cert.provider.x509v1

property has to be
changed to instantiate another implementation. If this security
property is not set, a default implementation will be used.
Currently, due to possible security restrictions on access to
Security properties, this value is looked up and cached at class
initialization time and will fallback on a default implementation if
the Security property is not accessible.

Note: The classes in the package

javax.security.cert

exist for compatibility with earlier versions of the
Java Secure Sockets Extension (JSSE). New applications should instead
use the standard Java SE certificate classes located in

java.security.cert

.

The basic X.509 format was defined by
ISO/IEC and ANSI X9 and is described below in ASN.1:

```java
Certificate ::= SEQUENCE {
tbsCertificate TBSCertificate,
signatureAlgorithm AlgorithmIdentifier,
signature BIT STRING }
```

These certificates are widely used to support authentication and
other functionality in Internet security systems. Common applications
include Privacy Enhanced Mail (PEM), Transport Layer Security (SSL),
code signing for trusted software distribution, and Secure Electronic
Transactions (SET).

These certificates are managed and vouched for by

Certificate
Authorities

(CAs). CAs are services which create certificates by
placing data in the X.509 standard format and then digitally signing
that data. CAs act as trusted third parties, making introductions
between principals who have no direct knowledge of each other.
CA certificates are either signed by themselves, or by some other
CA such as a "root" CA.

The ASN.1 definition of

tbsCertificate

is:

```java
TBSCertificate ::= SEQUENCE {
version [0] EXPLICIT Version DEFAULT v1,
serialNumber CertificateSerialNumber,
signature AlgorithmIdentifier,
issuer Name,
validity Validity,
subject Name,
subjectPublicKeyInfo SubjectPublicKeyInfo,
}
```

Here is sample code to instantiate an X.509 certificate:

```java
InputStream inStream = new FileInputStream("fileName-of-cert");
X509Certificate cert = X509Certificate.getInstance(inStream);
inStream.close();
```

OR

```java
byte[] certData = <certificate read from a file, say>
X509Certificate cert = X509Certificate.getInstance(certData);
```

In either case, the code that instantiates an X.509 certificate
consults the value of the

cert.provider.x509v1

security property
to locate the actual implementation or instantiates a default implementation.

The

cert.provider.x509v1

property is set to a default
implementation for X.509 such as:

```java
cert.provider.x509v1=com.sun.security.cert.internal.x509.X509V1CertImpl
```

The value of this

cert.provider.x509v1

property has to be
changed to instantiate another implementation. If this security
property is not set, a default implementation will be used.
Currently, due to possible security restrictions on access to
Security properties, this value is looked up and cached at class
initialization time and will fallback on a default implementation if
the Security property is not accessible.

Note: The classes in the package

javax.security.cert

exist for compatibility with earlier versions of the
Java Secure Sockets Extension (JSSE). New applications should instead
use the standard Java SE certificate classes located in

java.security.cert

.

Certificate ::= SEQUENCE {
tbsCertificate TBSCertificate,
signatureAlgorithm AlgorithmIdentifier,
signature BIT STRING }

These certificates are widely used to support authentication and
other functionality in Internet security systems. Common applications
include Privacy Enhanced Mail (PEM), Transport Layer Security (SSL),
code signing for trusted software distribution, and Secure Electronic
Transactions (SET).

These certificates are managed and vouched for by

Certificate
Authorities

(CAs). CAs are services which create certificates by
placing data in the X.509 standard format and then digitally signing
that data. CAs act as trusted third parties, making introductions
between principals who have no direct knowledge of each other.
CA certificates are either signed by themselves, or by some other
CA such as a "root" CA.

The ASN.1 definition of

tbsCertificate

is:

```java
TBSCertificate ::= SEQUENCE {
version [0] EXPLICIT Version DEFAULT v1,
serialNumber CertificateSerialNumber,
signature AlgorithmIdentifier,
issuer Name,
validity Validity,
subject Name,
subjectPublicKeyInfo SubjectPublicKeyInfo,
}
```

Here is sample code to instantiate an X.509 certificate:

```java
InputStream inStream = new FileInputStream("fileName-of-cert");
X509Certificate cert = X509Certificate.getInstance(inStream);
inStream.close();
```

OR

```java
byte[] certData = <certificate read from a file, say>
X509Certificate cert = X509Certificate.getInstance(certData);
```

In either case, the code that instantiates an X.509 certificate
consults the value of the

cert.provider.x509v1

security property
to locate the actual implementation or instantiates a default implementation.

The

cert.provider.x509v1

property is set to a default
implementation for X.509 such as:

```java
cert.provider.x509v1=com.sun.security.cert.internal.x509.X509V1CertImpl
```

The value of this

cert.provider.x509v1

property has to be
changed to instantiate another implementation. If this security
property is not set, a default implementation will be used.
Currently, due to possible security restrictions on access to
Security properties, this value is looked up and cached at class
initialization time and will fallback on a default implementation if
the Security property is not accessible.

Note: The classes in the package

javax.security.cert

exist for compatibility with earlier versions of the
Java Secure Sockets Extension (JSSE). New applications should instead
use the standard Java SE certificate classes located in

java.security.cert

.

These certificates are managed and vouched for by

Certificate
Authorities

(CAs). CAs are services which create certificates by
placing data in the X.509 standard format and then digitally signing
that data. CAs act as trusted third parties, making introductions
between principals who have no direct knowledge of each other.
CA certificates are either signed by themselves, or by some other
CA such as a "root" CA.

The ASN.1 definition of

tbsCertificate

is:

```java
TBSCertificate ::= SEQUENCE {
version [0] EXPLICIT Version DEFAULT v1,
serialNumber CertificateSerialNumber,
signature AlgorithmIdentifier,
issuer Name,
validity Validity,
subject Name,
subjectPublicKeyInfo SubjectPublicKeyInfo,
}
```

Here is sample code to instantiate an X.509 certificate:

```java
InputStream inStream = new FileInputStream("fileName-of-cert");
X509Certificate cert = X509Certificate.getInstance(inStream);
inStream.close();
```

OR

```java
byte[] certData = <certificate read from a file, say>
X509Certificate cert = X509Certificate.getInstance(certData);
```

In either case, the code that instantiates an X.509 certificate
consults the value of the

cert.provider.x509v1

security property
to locate the actual implementation or instantiates a default implementation.

The

cert.provider.x509v1

property is set to a default
implementation for X.509 such as:

```java
cert.provider.x509v1=com.sun.security.cert.internal.x509.X509V1CertImpl
```

The value of this

cert.provider.x509v1

property has to be
changed to instantiate another implementation. If this security
property is not set, a default implementation will be used.
Currently, due to possible security restrictions on access to
Security properties, this value is looked up and cached at class
initialization time and will fallback on a default implementation if
the Security property is not accessible.

Note: The classes in the package

javax.security.cert

exist for compatibility with earlier versions of the
Java Secure Sockets Extension (JSSE). New applications should instead
use the standard Java SE certificate classes located in

java.security.cert

.

The ASN.1 definition of

tbsCertificate

is:

```java
TBSCertificate ::= SEQUENCE {
version [0] EXPLICIT Version DEFAULT v1,
serialNumber CertificateSerialNumber,
signature AlgorithmIdentifier,
issuer Name,
validity Validity,
subject Name,
subjectPublicKeyInfo SubjectPublicKeyInfo,
}
```

Here is sample code to instantiate an X.509 certificate:

```java
InputStream inStream = new FileInputStream("fileName-of-cert");
X509Certificate cert = X509Certificate.getInstance(inStream);
inStream.close();
```

OR

```java
byte[] certData = <certificate read from a file, say>
X509Certificate cert = X509Certificate.getInstance(certData);
```

In either case, the code that instantiates an X.509 certificate
consults the value of the

cert.provider.x509v1

security property
to locate the actual implementation or instantiates a default implementation.

The

cert.provider.x509v1

property is set to a default
implementation for X.509 such as:

```java
cert.provider.x509v1=com.sun.security.cert.internal.x509.X509V1CertImpl
```

The value of this

cert.provider.x509v1

property has to be
changed to instantiate another implementation. If this security
property is not set, a default implementation will be used.
Currently, due to possible security restrictions on access to
Security properties, this value is looked up and cached at class
initialization time and will fallback on a default implementation if
the Security property is not accessible.

Note: The classes in the package

javax.security.cert

exist for compatibility with earlier versions of the
Java Secure Sockets Extension (JSSE). New applications should instead
use the standard Java SE certificate classes located in

java.security.cert

.

TBSCertificate ::= SEQUENCE {
version [0] EXPLICIT Version DEFAULT v1,
serialNumber CertificateSerialNumber,
signature AlgorithmIdentifier,
issuer Name,
validity Validity,
subject Name,
subjectPublicKeyInfo SubjectPublicKeyInfo,
}

Here is sample code to instantiate an X.509 certificate:

```java
InputStream inStream = new FileInputStream("fileName-of-cert");
X509Certificate cert = X509Certificate.getInstance(inStream);
inStream.close();
```

OR

```java
byte[] certData = <certificate read from a file, say>
X509Certificate cert = X509Certificate.getInstance(certData);
```

In either case, the code that instantiates an X.509 certificate
consults the value of the

cert.provider.x509v1

security property
to locate the actual implementation or instantiates a default implementation.

The

cert.provider.x509v1

property is set to a default
implementation for X.509 such as:

```java
cert.provider.x509v1=com.sun.security.cert.internal.x509.X509V1CertImpl
```

The value of this

cert.provider.x509v1

property has to be
changed to instantiate another implementation. If this security
property is not set, a default implementation will be used.
Currently, due to possible security restrictions on access to
Security properties, this value is looked up and cached at class
initialization time and will fallback on a default implementation if
the Security property is not accessible.

Note: The classes in the package

javax.security.cert

exist for compatibility with earlier versions of the
Java Secure Sockets Extension (JSSE). New applications should instead
use the standard Java SE certificate classes located in

java.security.cert

.

InputStream inStream = new FileInputStream("fileName-of-cert");
X509Certificate cert = X509Certificate.getInstance(inStream);
inStream.close();

byte[] certData = <certificate read from a file, say>
X509Certificate cert = X509Certificate.getInstance(certData);

In either case, the code that instantiates an X.509 certificate
consults the value of the

cert.provider.x509v1

security property
to locate the actual implementation or instantiates a default implementation.

The

cert.provider.x509v1

property is set to a default
implementation for X.509 such as:

```java
cert.provider.x509v1=com.sun.security.cert.internal.x509.X509V1CertImpl
```

The value of this

cert.provider.x509v1

property has to be
changed to instantiate another implementation. If this security
property is not set, a default implementation will be used.
Currently, due to possible security restrictions on access to
Security properties, this value is looked up and cached at class
initialization time and will fallback on a default implementation if
the Security property is not accessible.

Note: The classes in the package

javax.security.cert

exist for compatibility with earlier versions of the
Java Secure Sockets Extension (JSSE). New applications should instead
use the standard Java SE certificate classes located in

java.security.cert

.

The

cert.provider.x509v1

property is set to a default
implementation for X.509 such as:

```java
cert.provider.x509v1=com.sun.security.cert.internal.x509.X509V1CertImpl
```

The value of this

cert.provider.x509v1

property has to be
changed to instantiate another implementation. If this security
property is not set, a default implementation will be used.
Currently, due to possible security restrictions on access to
Security properties, this value is looked up and cached at class
initialization time and will fallback on a default implementation if
the Security property is not accessible.

Note: The classes in the package

javax.security.cert

exist for compatibility with earlier versions of the
Java Secure Sockets Extension (JSSE). New applications should instead
use the standard Java SE certificate classes located in

java.security.cert

.

cert.provider.x509v1=com.sun.security.cert.internal.x509.X509V1CertImpl

The value of this

cert.provider.x509v1

property has to be
changed to instantiate another implementation. If this security
property is not set, a default implementation will be used.
Currently, due to possible security restrictions on access to
Security properties, this value is looked up and cached at class
initialization time and will fallback on a default implementation if
the Security property is not accessible.

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

X509Certificate

()

Deprecated.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Instance Methods

Abstract Methods

Concrete Methods

Deprecated Methods

Modifier and Type

Method

Description

abstract void

checkValidity

()

Deprecated.

Checks that the certificate is currently valid.

abstract void

checkValidity

​(

Date

date)

Deprecated.

Checks that the specified date is within the certificate's
validity period.

static

X509Certificate

getInstance

​(byte[] certData)

Deprecated.

Instantiates an X509Certificate object, and initializes it with
the specified byte array.

static

X509Certificate

getInstance

​(

InputStream

inStream)

Deprecated.

Instantiates an X509Certificate object, and initializes it with
the data read from the input stream

inStream

.

abstract

Principal

getIssuerDN

()

Deprecated.

Gets the

issuer

(issuer distinguished name) value from
the certificate.

abstract

Date

getNotAfter

()

Deprecated.

Gets the

notAfter

date from the validity period of
the certificate.

abstract

Date

getNotBefore

()

Deprecated.

Gets the

notBefore

date from the validity period of
the certificate.

abstract

BigInteger

getSerialNumber

()

Deprecated.

Gets the

serialNumber

value from the certificate.

abstract

String

getSigAlgName

()

Deprecated.

Gets the signature algorithm name for the certificate
signature algorithm.

abstract

String

getSigAlgOID

()

Deprecated.

Gets the signature algorithm OID string from the certificate.

abstract byte[]

getSigAlgParams

()

Deprecated.

Gets the DER-encoded signature algorithm parameters from this
certificate's signature algorithm.

abstract

Principal

getSubjectDN

()

Deprecated.

Gets the

subject

(subject distinguished name) value
from the certificate.

abstract int

getVersion

()

Deprecated.

Gets the

version

(version number) value from the
certificate.

- Methods declared in class javax.security.cert.

Certificate

equals

,

getEncoded

,

getPublicKey

,

hashCode

,

toString

,

verify

,

verify

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

X509Certificate

()

Deprecated.

---

#### Constructor Summary

Deprecated.

Method Summary

All Methods

Static Methods

Instance Methods

Abstract Methods

Concrete Methods

Deprecated Methods

Modifier and Type

Method

Description

abstract void

checkValidity

()

Deprecated.

Checks that the certificate is currently valid.

abstract void

checkValidity

​(

Date

date)

Deprecated.

Checks that the specified date is within the certificate's
validity period.

static

X509Certificate

getInstance

​(byte[] certData)

Deprecated.

Instantiates an X509Certificate object, and initializes it with
the specified byte array.

static

X509Certificate

getInstance

​(

InputStream

inStream)

Deprecated.

Instantiates an X509Certificate object, and initializes it with
the data read from the input stream

inStream

.

abstract

Principal

getIssuerDN

()

Deprecated.

Gets the

issuer

(issuer distinguished name) value from
the certificate.

abstract

Date

getNotAfter

()

Deprecated.

Gets the

notAfter

date from the validity period of
the certificate.

abstract

Date

getNotBefore

()

Deprecated.

Gets the

notBefore

date from the validity period of
the certificate.

abstract

BigInteger

getSerialNumber

()

Deprecated.

Gets the

serialNumber

value from the certificate.

abstract

String

getSigAlgName

()

Deprecated.

Gets the signature algorithm name for the certificate
signature algorithm.

abstract

String

getSigAlgOID

()

Deprecated.

Gets the signature algorithm OID string from the certificate.

abstract byte[]

getSigAlgParams

()

Deprecated.

Gets the DER-encoded signature algorithm parameters from this
certificate's signature algorithm.

abstract

Principal

getSubjectDN

()

Deprecated.

Gets the

subject

(subject distinguished name) value
from the certificate.

abstract int

getVersion

()

Deprecated.

Gets the

version

(version number) value from the
certificate.

- Methods declared in class javax.security.cert.

Certificate

equals

,

getEncoded

,

getPublicKey

,

hashCode

,

toString

,

verify

,

verify

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

Checks that the certificate is currently valid.

Checks that the specified date is within the certificate's
validity period.

Instantiates an X509Certificate object, and initializes it with
the specified byte array.

Instantiates an X509Certificate object, and initializes it with
the data read from the input stream

inStream

.

Gets the

issuer

(issuer distinguished name) value from
the certificate.

Gets the

notAfter

date from the validity period of
the certificate.

Gets the

notBefore

date from the validity period of
the certificate.

Gets the

serialNumber

value from the certificate.

Gets the signature algorithm name for the certificate
signature algorithm.

Gets the signature algorithm OID string from the certificate.

Gets the DER-encoded signature algorithm parameters from this
certificate's signature algorithm.

Gets the

subject

(subject distinguished name) value
from the certificate.

Gets the

version

(version number) value from the
certificate.

Methods declared in class javax.security.cert.

Certificate

equals

,

getEncoded

,

getPublicKey

,

hashCode

,

toString

,

verify

,

verify

---

#### Methods declared in class javax.security.cert. Certificate

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

- X509Certificate

```java
public X509Certificate()
```

Deprecated.

============ METHOD DETAIL ==========

- Method Detail

- getInstance

```java
public static final
X509Certificate
getInstance​(
InputStream
inStream)
throws
CertificateException
```

Deprecated.

Instantiates an X509Certificate object, and initializes it with
the data read from the input stream

inStream

.
The implementation (X509Certificate is an abstract class) is
provided by the class specified as the value of the

cert.provider.x509v1

security property.

Note: Only one DER-encoded
certificate is expected to be in the input stream.
Also, all X509Certificate
subclasses must provide a constructor of the form:

```java
public <subClass>(InputStream inStream) ...
```

**Parameters:** inStream

- an input stream with the data to be read to
initialize the certificate.
**Returns:** an X509Certificate object initialized with the data
from the input stream.
**Throws:** CertificateException

- if a class initialization
or certificate parsing error occurs.

- getInstance

```java
public static final
X509Certificate
getInstance​(byte[] certData)
throws
CertificateException
```

Deprecated.

Instantiates an X509Certificate object, and initializes it with
the specified byte array.
The implementation (X509Certificate is an abstract class) is
provided by the class specified as the value of the

cert.provider.x509v1

security property.

Note: All X509Certificate
subclasses must provide a constructor of the form:

```java
public <subClass>(InputStream inStream) ...
```

**Parameters:** certData

- a byte array containing the DER-encoded
certificate.
**Returns:** an X509Certificate object initialized with the data
from

certData

.
**Throws:** CertificateException

- if a class initialization
or certificate parsing error occurs.

- checkValidity

```java
public abstract void checkValidity()
throws
CertificateExpiredException
,

CertificateNotYetValidException
```

Deprecated.

Checks that the certificate is currently valid. It is if
the current date and time are within the validity period given in the
certificate.

The validity period consists of two date/time values:
the first and last dates (and times) on which the certificate
is valid. It is defined in
ASN.1 as:

```java
validity Validity

Validity ::= SEQUENCE {
notBefore CertificateValidityDate,
notAfter CertificateValidityDate }

CertificateValidityDate ::= CHOICE {
utcTime UTCTime,
generalTime GeneralizedTime }
```

**Throws:** CertificateExpiredException

- if the certificate has expired.
**Throws:** CertificateNotYetValidException

- if the certificate is not
yet valid.

- checkValidity

```java
public abstract void checkValidity​(
Date
date)
throws
CertificateExpiredException
,

CertificateNotYetValidException
```

Deprecated.

Checks that the specified date is within the certificate's
validity period. In other words, this determines whether the
certificate would be valid at the specified date/time.

**Parameters:** date

- the Date to check against to see if this certificate
is valid at that date/time.
**Throws:** CertificateExpiredException

- if the certificate has expired
with respect to the

date

supplied.
**Throws:** CertificateNotYetValidException

- if the certificate is not
yet valid with respect to the

date

supplied.
**See Also:** checkValidity()

- getVersion

```java
public abstract int getVersion()
```

Deprecated.

Gets the

version

(version number) value from the
certificate. The ASN.1 definition for this is:

```java
version [0] EXPLICIT Version DEFAULT v1

Version ::= INTEGER { v1(0), v2(1), v3(2) }
```

**Returns:** the version number from the ASN.1 encoding, i.e. 0, 1 or 2.

- getSerialNumber

```java
public abstract
BigInteger
getSerialNumber()
```

Deprecated.

Gets the

serialNumber

value from the certificate.
The serial number is an integer assigned by the certification
authority to each certificate. It must be unique for each
certificate issued by a given CA (i.e., the issuer name and
serial number identify a unique certificate).
The ASN.1 definition for this is:

```java
serialNumber CertificateSerialNumber

CertificateSerialNumber ::= INTEGER
```

**Returns:** the serial number.

- getIssuerDN

```java
public abstract
Principal
getIssuerDN()
```

Deprecated.

Gets the

issuer

(issuer distinguished name) value from
the certificate. The issuer name identifies the entity that signed (and
issued) the certificate.

The issuer name field contains an
X.500 distinguished name (DN).
The ASN.1 definition for this is:

```java
issuer Name

Name ::= CHOICE { RDNSequence }
RDNSequence ::= SEQUENCE OF RelativeDistinguishedName
RelativeDistinguishedName ::=
SET OF AttributeValueAssertion

AttributeValueAssertion ::= SEQUENCE {
AttributeType,
AttributeValue }
AttributeType ::= OBJECT IDENTIFIER
AttributeValue ::= ANY
```

The

Name

describes a hierarchical name composed of
attributes, such as country name, and corresponding values, such as US.
The type of the

AttributeValue

component is determined by
the

AttributeType

; in general it will be a

directoryString

. A

directoryString

is usually
one of

PrintableString

,

TeletexString

or

UniversalString

.

**Returns:** a Principal whose name is the issuer distinguished name.

- getSubjectDN

```java
public abstract
Principal
getSubjectDN()
```

Deprecated.

Gets the

subject

(subject distinguished name) value
from the certificate.
The ASN.1 definition for this is:

```java
subject Name
```

See

getIssuerDN

for

Name

and other relevant definitions.

**Returns:** a Principal whose name is the subject name.
**See Also:** getIssuerDN()

- getNotBefore

```java
public abstract
Date
getNotBefore()
```

Deprecated.

Gets the

notBefore

date from the validity period of
the certificate.
The relevant ASN.1 definitions are:

```java
validity Validity

Validity ::= SEQUENCE {
notBefore CertificateValidityDate,
notAfter CertificateValidityDate }

CertificateValidityDate ::= CHOICE {
utcTime UTCTime,
generalTime GeneralizedTime }
```

**Returns:** the start date of the validity period.
**See Also:** checkValidity()

- getNotAfter

```java
public abstract
Date
getNotAfter()
```

Deprecated.

Gets the

notAfter

date from the validity period of
the certificate. See

getNotBefore

for relevant ASN.1 definitions.

**Returns:** the end date of the validity period.
**See Also:** checkValidity()

- getSigAlgName

```java
public abstract
String
getSigAlgName()
```

Deprecated.

Gets the signature algorithm name for the certificate
signature algorithm. An example is the string "SHA-1/DSA".
The ASN.1 definition for this is:

```java
signatureAlgorithm AlgorithmIdentifier

AlgorithmIdentifier ::= SEQUENCE {
algorithm OBJECT IDENTIFIER,
parameters ANY DEFINED BY algorithm OPTIONAL }
-- contains a value of the type
-- registered for use with the
-- algorithm object identifier value
```

The algorithm name is determined from the

algorithm

OID string.

**Returns:** the signature algorithm name.

- getSigAlgOID

```java
public abstract
String
getSigAlgOID()
```

Deprecated.

Gets the signature algorithm OID string from the certificate.
An OID is represented by a set of positive whole numbers separated
by periods.
For example, the string "1.2.840.10040.4.3" identifies the SHA-1
with DSA signature algorithm, as per the PKIX part I.

See

getSigAlgName

for
relevant ASN.1 definitions.

**Returns:** the signature algorithm OID string.

- getSigAlgParams

```java
public abstract byte[] getSigAlgParams()
```

Deprecated.

Gets the DER-encoded signature algorithm parameters from this
certificate's signature algorithm. In most cases, the signature
algorithm parameters are null; the parameters are usually
supplied with the certificate's public key.

See

getSigAlgName

for
relevant ASN.1 definitions.

**Returns:** the DER-encoded signature algorithm parameters, or
null if no parameters are present.

Constructor Detail

- X509Certificate

```java
public X509Certificate()
```

Deprecated.

---

#### Constructor Detail

X509Certificate

```java
public X509Certificate()
```

Deprecated.

---

#### X509Certificate

public X509Certificate()

Method Detail

- getInstance

```java
public static final
X509Certificate
getInstance​(
InputStream
inStream)
throws
CertificateException
```

Deprecated.

Instantiates an X509Certificate object, and initializes it with
the data read from the input stream

inStream

.
The implementation (X509Certificate is an abstract class) is
provided by the class specified as the value of the

cert.provider.x509v1

security property.

Note: Only one DER-encoded
certificate is expected to be in the input stream.
Also, all X509Certificate
subclasses must provide a constructor of the form:

```java
public <subClass>(InputStream inStream) ...
```

**Parameters:** inStream

- an input stream with the data to be read to
initialize the certificate.
**Returns:** an X509Certificate object initialized with the data
from the input stream.
**Throws:** CertificateException

- if a class initialization
or certificate parsing error occurs.

- getInstance

```java
public static final
X509Certificate
getInstance​(byte[] certData)
throws
CertificateException
```

Deprecated.

Instantiates an X509Certificate object, and initializes it with
the specified byte array.
The implementation (X509Certificate is an abstract class) is
provided by the class specified as the value of the

cert.provider.x509v1

security property.

Note: All X509Certificate
subclasses must provide a constructor of the form:

```java
public <subClass>(InputStream inStream) ...
```

**Parameters:** certData

- a byte array containing the DER-encoded
certificate.
**Returns:** an X509Certificate object initialized with the data
from

certData

.
**Throws:** CertificateException

- if a class initialization
or certificate parsing error occurs.

- checkValidity

```java
public abstract void checkValidity()
throws
CertificateExpiredException
,

CertificateNotYetValidException
```

Deprecated.

Checks that the certificate is currently valid. It is if
the current date and time are within the validity period given in the
certificate.

The validity period consists of two date/time values:
the first and last dates (and times) on which the certificate
is valid. It is defined in
ASN.1 as:

```java
validity Validity

Validity ::= SEQUENCE {
notBefore CertificateValidityDate,
notAfter CertificateValidityDate }

CertificateValidityDate ::= CHOICE {
utcTime UTCTime,
generalTime GeneralizedTime }
```

**Throws:** CertificateExpiredException

- if the certificate has expired.
**Throws:** CertificateNotYetValidException

- if the certificate is not
yet valid.

- checkValidity

```java
public abstract void checkValidity​(
Date
date)
throws
CertificateExpiredException
,

CertificateNotYetValidException
```

Deprecated.

Checks that the specified date is within the certificate's
validity period. In other words, this determines whether the
certificate would be valid at the specified date/time.

**Parameters:** date

- the Date to check against to see if this certificate
is valid at that date/time.
**Throws:** CertificateExpiredException

- if the certificate has expired
with respect to the

date

supplied.
**Throws:** CertificateNotYetValidException

- if the certificate is not
yet valid with respect to the

date

supplied.
**See Also:** checkValidity()

- getVersion

```java
public abstract int getVersion()
```

Deprecated.

Gets the

version

(version number) value from the
certificate. The ASN.1 definition for this is:

```java
version [0] EXPLICIT Version DEFAULT v1

Version ::= INTEGER { v1(0), v2(1), v3(2) }
```

**Returns:** the version number from the ASN.1 encoding, i.e. 0, 1 or 2.

- getSerialNumber

```java
public abstract
BigInteger
getSerialNumber()
```

Deprecated.

Gets the

serialNumber

value from the certificate.
The serial number is an integer assigned by the certification
authority to each certificate. It must be unique for each
certificate issued by a given CA (i.e., the issuer name and
serial number identify a unique certificate).
The ASN.1 definition for this is:

```java
serialNumber CertificateSerialNumber

CertificateSerialNumber ::= INTEGER
```

**Returns:** the serial number.

- getIssuerDN

```java
public abstract
Principal
getIssuerDN()
```

Deprecated.

Gets the

issuer

(issuer distinguished name) value from
the certificate. The issuer name identifies the entity that signed (and
issued) the certificate.

The issuer name field contains an
X.500 distinguished name (DN).
The ASN.1 definition for this is:

```java
issuer Name

Name ::= CHOICE { RDNSequence }
RDNSequence ::= SEQUENCE OF RelativeDistinguishedName
RelativeDistinguishedName ::=
SET OF AttributeValueAssertion

AttributeValueAssertion ::= SEQUENCE {
AttributeType,
AttributeValue }
AttributeType ::= OBJECT IDENTIFIER
AttributeValue ::= ANY
```

The

Name

describes a hierarchical name composed of
attributes, such as country name, and corresponding values, such as US.
The type of the

AttributeValue

component is determined by
the

AttributeType

; in general it will be a

directoryString

. A

directoryString

is usually
one of

PrintableString

,

TeletexString

or

UniversalString

.

**Returns:** a Principal whose name is the issuer distinguished name.

- getSubjectDN

```java
public abstract
Principal
getSubjectDN()
```

Deprecated.

Gets the

subject

(subject distinguished name) value
from the certificate.
The ASN.1 definition for this is:

```java
subject Name
```

See

getIssuerDN

for

Name

and other relevant definitions.

**Returns:** a Principal whose name is the subject name.
**See Also:** getIssuerDN()

- getNotBefore

```java
public abstract
Date
getNotBefore()
```

Deprecated.

Gets the

notBefore

date from the validity period of
the certificate.
The relevant ASN.1 definitions are:

```java
validity Validity

Validity ::= SEQUENCE {
notBefore CertificateValidityDate,
notAfter CertificateValidityDate }

CertificateValidityDate ::= CHOICE {
utcTime UTCTime,
generalTime GeneralizedTime }
```

**Returns:** the start date of the validity period.
**See Also:** checkValidity()

- getNotAfter

```java
public abstract
Date
getNotAfter()
```

Deprecated.

Gets the

notAfter

date from the validity period of
the certificate. See

getNotBefore

for relevant ASN.1 definitions.

**Returns:** the end date of the validity period.
**See Also:** checkValidity()

- getSigAlgName

```java
public abstract
String
getSigAlgName()
```

Deprecated.

Gets the signature algorithm name for the certificate
signature algorithm. An example is the string "SHA-1/DSA".
The ASN.1 definition for this is:

```java
signatureAlgorithm AlgorithmIdentifier

AlgorithmIdentifier ::= SEQUENCE {
algorithm OBJECT IDENTIFIER,
parameters ANY DEFINED BY algorithm OPTIONAL }
-- contains a value of the type
-- registered for use with the
-- algorithm object identifier value
```

The algorithm name is determined from the

algorithm

OID string.

**Returns:** the signature algorithm name.

- getSigAlgOID

```java
public abstract
String
getSigAlgOID()
```

Deprecated.

Gets the signature algorithm OID string from the certificate.
An OID is represented by a set of positive whole numbers separated
by periods.
For example, the string "1.2.840.10040.4.3" identifies the SHA-1
with DSA signature algorithm, as per the PKIX part I.

See

getSigAlgName

for
relevant ASN.1 definitions.

**Returns:** the signature algorithm OID string.

- getSigAlgParams

```java
public abstract byte[] getSigAlgParams()
```

Deprecated.

Gets the DER-encoded signature algorithm parameters from this
certificate's signature algorithm. In most cases, the signature
algorithm parameters are null; the parameters are usually
supplied with the certificate's public key.

See

getSigAlgName

for
relevant ASN.1 definitions.

**Returns:** the DER-encoded signature algorithm parameters, or
null if no parameters are present.

---

#### Method Detail

getInstance

```java
public static final
X509Certificate
getInstance​(
InputStream
inStream)
throws
CertificateException
```

Deprecated.

Instantiates an X509Certificate object, and initializes it with
the data read from the input stream

inStream

.
The implementation (X509Certificate is an abstract class) is
provided by the class specified as the value of the

cert.provider.x509v1

security property.

Note: Only one DER-encoded
certificate is expected to be in the input stream.
Also, all X509Certificate
subclasses must provide a constructor of the form:

```java
public <subClass>(InputStream inStream) ...
```

**Parameters:** inStream

- an input stream with the data to be read to
initialize the certificate.
**Returns:** an X509Certificate object initialized with the data
from the input stream.
**Throws:** CertificateException

- if a class initialization
or certificate parsing error occurs.

---

#### getInstance

public static final

X509Certificate

getInstance​(

InputStream

inStream)
throws

CertificateException

Instantiates an X509Certificate object, and initializes it with
the data read from the input stream

inStream

.
The implementation (X509Certificate is an abstract class) is
provided by the class specified as the value of the

cert.provider.x509v1

security property.

Note: Only one DER-encoded
certificate is expected to be in the input stream.
Also, all X509Certificate
subclasses must provide a constructor of the form:

```java
public <subClass>(InputStream inStream) ...
```

Note: Only one DER-encoded
certificate is expected to be in the input stream.
Also, all X509Certificate
subclasses must provide a constructor of the form:

```java
public <subClass>(InputStream inStream) ...
```

public <subClass>(InputStream inStream) ...

getInstance

```java
public static final
X509Certificate
getInstance​(byte[] certData)
throws
CertificateException
```

Deprecated.

Instantiates an X509Certificate object, and initializes it with
the specified byte array.
The implementation (X509Certificate is an abstract class) is
provided by the class specified as the value of the

cert.provider.x509v1

security property.

Note: All X509Certificate
subclasses must provide a constructor of the form:

```java
public <subClass>(InputStream inStream) ...
```

**Parameters:** certData

- a byte array containing the DER-encoded
certificate.
**Returns:** an X509Certificate object initialized with the data
from

certData

.
**Throws:** CertificateException

- if a class initialization
or certificate parsing error occurs.

---

#### getInstance

public static final

X509Certificate

getInstance​(byte[] certData)
throws

CertificateException

Instantiates an X509Certificate object, and initializes it with
the specified byte array.
The implementation (X509Certificate is an abstract class) is
provided by the class specified as the value of the

cert.provider.x509v1

security property.

Note: All X509Certificate
subclasses must provide a constructor of the form:

```java
public <subClass>(InputStream inStream) ...
```

Note: All X509Certificate
subclasses must provide a constructor of the form:

```java
public <subClass>(InputStream inStream) ...
```

public <subClass>(InputStream inStream) ...

checkValidity

```java
public abstract void checkValidity()
throws
CertificateExpiredException
,

CertificateNotYetValidException
```

Deprecated.

Checks that the certificate is currently valid. It is if
the current date and time are within the validity period given in the
certificate.

The validity period consists of two date/time values:
the first and last dates (and times) on which the certificate
is valid. It is defined in
ASN.1 as:

```java
validity Validity

Validity ::= SEQUENCE {
notBefore CertificateValidityDate,
notAfter CertificateValidityDate }

CertificateValidityDate ::= CHOICE {
utcTime UTCTime,
generalTime GeneralizedTime }
```

**Throws:** CertificateExpiredException

- if the certificate has expired.
**Throws:** CertificateNotYetValidException

- if the certificate is not
yet valid.

---

#### checkValidity

public abstract void checkValidity()
throws

CertificateExpiredException

,

CertificateNotYetValidException

Checks that the certificate is currently valid. It is if
the current date and time are within the validity period given in the
certificate.

The validity period consists of two date/time values:
the first and last dates (and times) on which the certificate
is valid. It is defined in
ASN.1 as:

```java
validity Validity

Validity ::= SEQUENCE {
notBefore CertificateValidityDate,
notAfter CertificateValidityDate }

CertificateValidityDate ::= CHOICE {
utcTime UTCTime,
generalTime GeneralizedTime }
```

The validity period consists of two date/time values:
the first and last dates (and times) on which the certificate
is valid. It is defined in
ASN.1 as:

```java
validity Validity

Validity ::= SEQUENCE {
notBefore CertificateValidityDate,
notAfter CertificateValidityDate }

CertificateValidityDate ::= CHOICE {
utcTime UTCTime,
generalTime GeneralizedTime }
```

validity Validity

Validity ::= SEQUENCE {
notBefore CertificateValidityDate,
notAfter CertificateValidityDate }

CertificateValidityDate ::= CHOICE {
utcTime UTCTime,
generalTime GeneralizedTime }

checkValidity

```java
public abstract void checkValidity​(
Date
date)
throws
CertificateExpiredException
,

CertificateNotYetValidException
```

Deprecated.

Checks that the specified date is within the certificate's
validity period. In other words, this determines whether the
certificate would be valid at the specified date/time.

**Parameters:** date

- the Date to check against to see if this certificate
is valid at that date/time.
**Throws:** CertificateExpiredException

- if the certificate has expired
with respect to the

date

supplied.
**Throws:** CertificateNotYetValidException

- if the certificate is not
yet valid with respect to the

date

supplied.
**See Also:** checkValidity()

---

#### checkValidity

public abstract void checkValidity​(

Date

date)
throws

CertificateExpiredException

,

CertificateNotYetValidException

Checks that the specified date is within the certificate's
validity period. In other words, this determines whether the
certificate would be valid at the specified date/time.

getVersion

```java
public abstract int getVersion()
```

Deprecated.

Gets the

version

(version number) value from the
certificate. The ASN.1 definition for this is:

```java
version [0] EXPLICIT Version DEFAULT v1

Version ::= INTEGER { v1(0), v2(1), v3(2) }
```

**Returns:** the version number from the ASN.1 encoding, i.e. 0, 1 or 2.

---

#### getVersion

public abstract int getVersion()

Gets the

version

(version number) value from the
certificate. The ASN.1 definition for this is:

```java
version [0] EXPLICIT Version DEFAULT v1

Version ::= INTEGER { v1(0), v2(1), v3(2) }
```

version [0] EXPLICIT Version DEFAULT v1

Version ::= INTEGER { v1(0), v2(1), v3(2) }

getSerialNumber

```java
public abstract
BigInteger
getSerialNumber()
```

Deprecated.

Gets the

serialNumber

value from the certificate.
The serial number is an integer assigned by the certification
authority to each certificate. It must be unique for each
certificate issued by a given CA (i.e., the issuer name and
serial number identify a unique certificate).
The ASN.1 definition for this is:

```java
serialNumber CertificateSerialNumber

CertificateSerialNumber ::= INTEGER
```

**Returns:** the serial number.

---

#### getSerialNumber

public abstract

BigInteger

getSerialNumber()

Gets the

serialNumber

value from the certificate.
The serial number is an integer assigned by the certification
authority to each certificate. It must be unique for each
certificate issued by a given CA (i.e., the issuer name and
serial number identify a unique certificate).
The ASN.1 definition for this is:

```java
serialNumber CertificateSerialNumber

CertificateSerialNumber ::= INTEGER
```

serialNumber CertificateSerialNumber

CertificateSerialNumber ::= INTEGER

getIssuerDN

```java
public abstract
Principal
getIssuerDN()
```

Deprecated.

Gets the

issuer

(issuer distinguished name) value from
the certificate. The issuer name identifies the entity that signed (and
issued) the certificate.

The issuer name field contains an
X.500 distinguished name (DN).
The ASN.1 definition for this is:

```java
issuer Name

Name ::= CHOICE { RDNSequence }
RDNSequence ::= SEQUENCE OF RelativeDistinguishedName
RelativeDistinguishedName ::=
SET OF AttributeValueAssertion

AttributeValueAssertion ::= SEQUENCE {
AttributeType,
AttributeValue }
AttributeType ::= OBJECT IDENTIFIER
AttributeValue ::= ANY
```

The

Name

describes a hierarchical name composed of
attributes, such as country name, and corresponding values, such as US.
The type of the

AttributeValue

component is determined by
the

AttributeType

; in general it will be a

directoryString

. A

directoryString

is usually
one of

PrintableString

,

TeletexString

or

UniversalString

.

**Returns:** a Principal whose name is the issuer distinguished name.

---

#### getIssuerDN

public abstract

Principal

getIssuerDN()

Gets the

issuer

(issuer distinguished name) value from
the certificate. The issuer name identifies the entity that signed (and
issued) the certificate.

The issuer name field contains an
X.500 distinguished name (DN).
The ASN.1 definition for this is:

```java
issuer Name

Name ::= CHOICE { RDNSequence }
RDNSequence ::= SEQUENCE OF RelativeDistinguishedName
RelativeDistinguishedName ::=
SET OF AttributeValueAssertion

AttributeValueAssertion ::= SEQUENCE {
AttributeType,
AttributeValue }
AttributeType ::= OBJECT IDENTIFIER
AttributeValue ::= ANY
```

The

Name

describes a hierarchical name composed of
attributes, such as country name, and corresponding values, such as US.
The type of the

AttributeValue

component is determined by
the

AttributeType

; in general it will be a

directoryString

. A

directoryString

is usually
one of

PrintableString

,

TeletexString

or

UniversalString

.

The issuer name field contains an
X.500 distinguished name (DN).
The ASN.1 definition for this is:

```java
issuer Name

Name ::= CHOICE { RDNSequence }
RDNSequence ::= SEQUENCE OF RelativeDistinguishedName
RelativeDistinguishedName ::=
SET OF AttributeValueAssertion

AttributeValueAssertion ::= SEQUENCE {
AttributeType,
AttributeValue }
AttributeType ::= OBJECT IDENTIFIER
AttributeValue ::= ANY
```

The

Name

describes a hierarchical name composed of
attributes, such as country name, and corresponding values, such as US.
The type of the

AttributeValue

component is determined by
the

AttributeType

; in general it will be a

directoryString

. A

directoryString

is usually
one of

PrintableString

,

TeletexString

or

UniversalString

.

issuer Name

Name ::= CHOICE { RDNSequence }
RDNSequence ::= SEQUENCE OF RelativeDistinguishedName
RelativeDistinguishedName ::=
SET OF AttributeValueAssertion

AttributeValueAssertion ::= SEQUENCE {
AttributeType,
AttributeValue }
AttributeType ::= OBJECT IDENTIFIER
AttributeValue ::= ANY

getSubjectDN

```java
public abstract
Principal
getSubjectDN()
```

Deprecated.

Gets the

subject

(subject distinguished name) value
from the certificate.
The ASN.1 definition for this is:

```java
subject Name
```

See

getIssuerDN

for

Name

and other relevant definitions.

**Returns:** a Principal whose name is the subject name.
**See Also:** getIssuerDN()

---

#### getSubjectDN

public abstract

Principal

getSubjectDN()

Gets the

subject

(subject distinguished name) value
from the certificate.
The ASN.1 definition for this is:

```java
subject Name
```

See

getIssuerDN

for

Name

and other relevant definitions.

subject Name

See

getIssuerDN

for

Name

and other relevant definitions.

getNotBefore

```java
public abstract
Date
getNotBefore()
```

Deprecated.

Gets the

notBefore

date from the validity period of
the certificate.
The relevant ASN.1 definitions are:

```java
validity Validity

Validity ::= SEQUENCE {
notBefore CertificateValidityDate,
notAfter CertificateValidityDate }

CertificateValidityDate ::= CHOICE {
utcTime UTCTime,
generalTime GeneralizedTime }
```

**Returns:** the start date of the validity period.
**See Also:** checkValidity()

---

#### getNotBefore

public abstract

Date

getNotBefore()

Gets the

notBefore

date from the validity period of
the certificate.
The relevant ASN.1 definitions are:

```java
validity Validity

Validity ::= SEQUENCE {
notBefore CertificateValidityDate,
notAfter CertificateValidityDate }

CertificateValidityDate ::= CHOICE {
utcTime UTCTime,
generalTime GeneralizedTime }
```

validity Validity

Validity ::= SEQUENCE {
notBefore CertificateValidityDate,
notAfter CertificateValidityDate }

CertificateValidityDate ::= CHOICE {
utcTime UTCTime,
generalTime GeneralizedTime }

getNotAfter

```java
public abstract
Date
getNotAfter()
```

Deprecated.

Gets the

notAfter

date from the validity period of
the certificate. See

getNotBefore

for relevant ASN.1 definitions.

**Returns:** the end date of the validity period.
**See Also:** checkValidity()

---

#### getNotAfter

public abstract

Date

getNotAfter()

Gets the

notAfter

date from the validity period of
the certificate. See

getNotBefore

for relevant ASN.1 definitions.

getSigAlgName

```java
public abstract
String
getSigAlgName()
```

Deprecated.

Gets the signature algorithm name for the certificate
signature algorithm. An example is the string "SHA-1/DSA".
The ASN.1 definition for this is:

```java
signatureAlgorithm AlgorithmIdentifier

AlgorithmIdentifier ::= SEQUENCE {
algorithm OBJECT IDENTIFIER,
parameters ANY DEFINED BY algorithm OPTIONAL }
-- contains a value of the type
-- registered for use with the
-- algorithm object identifier value
```

The algorithm name is determined from the

algorithm

OID string.

**Returns:** the signature algorithm name.

---

#### getSigAlgName

public abstract

String

getSigAlgName()

Gets the signature algorithm name for the certificate
signature algorithm. An example is the string "SHA-1/DSA".
The ASN.1 definition for this is:

```java
signatureAlgorithm AlgorithmIdentifier

AlgorithmIdentifier ::= SEQUENCE {
algorithm OBJECT IDENTIFIER,
parameters ANY DEFINED BY algorithm OPTIONAL }
-- contains a value of the type
-- registered for use with the
-- algorithm object identifier value
```

The algorithm name is determined from the

algorithm

OID string.

signatureAlgorithm AlgorithmIdentifier

AlgorithmIdentifier ::= SEQUENCE {
algorithm OBJECT IDENTIFIER,
parameters ANY DEFINED BY algorithm OPTIONAL }
-- contains a value of the type
-- registered for use with the
-- algorithm object identifier value

The algorithm name is determined from the

algorithm

OID string.

getSigAlgOID

```java
public abstract
String
getSigAlgOID()
```

Deprecated.

Gets the signature algorithm OID string from the certificate.
An OID is represented by a set of positive whole numbers separated
by periods.
For example, the string "1.2.840.10040.4.3" identifies the SHA-1
with DSA signature algorithm, as per the PKIX part I.

See

getSigAlgName

for
relevant ASN.1 definitions.

**Returns:** the signature algorithm OID string.

---

#### getSigAlgOID

public abstract

String

getSigAlgOID()

Gets the signature algorithm OID string from the certificate.
An OID is represented by a set of positive whole numbers separated
by periods.
For example, the string "1.2.840.10040.4.3" identifies the SHA-1
with DSA signature algorithm, as per the PKIX part I.

See

getSigAlgName

for
relevant ASN.1 definitions.

See

getSigAlgName

for
relevant ASN.1 definitions.

getSigAlgParams

```java
public abstract byte[] getSigAlgParams()
```

Deprecated.

Gets the DER-encoded signature algorithm parameters from this
certificate's signature algorithm. In most cases, the signature
algorithm parameters are null; the parameters are usually
supplied with the certificate's public key.

See

getSigAlgName

for
relevant ASN.1 definitions.

**Returns:** the DER-encoded signature algorithm parameters, or
null if no parameters are present.

---

#### getSigAlgParams

public abstract byte[] getSigAlgParams()

Gets the DER-encoded signature algorithm parameters from this
certificate's signature algorithm. In most cases, the signature
algorithm parameters are null; the parameters are usually
supplied with the certificate's public key.

See

getSigAlgName

for
relevant ASN.1 definitions.

See

getSigAlgName

for
relevant ASN.1 definitions.

---

