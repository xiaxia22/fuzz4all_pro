# Class X509CRL

**Source:** `java.base\java\security\cert\X509CRL.html`

### Class Description

```java
public abstract class
X509CRL

extends
CRL

implements
X509Extension
```

Abstract class for an X.509 Certificate Revocation List (CRL).
A CRL is a time-stamped list identifying revoked certificates.
It is signed by a Certificate Authority (CA) and made freely
available in a public repository.

Each revoked certificate is
identified in a CRL by its certificate serial number. When a
certificate-using system uses a certificate (e.g., for verifying a
remote user's digital signature), that system not only checks the
certificate signature and validity but also acquires a suitably-
recent CRL and checks that the certificate serial number is not on
that CRL. The meaning of "suitably-recent" may vary with local
policy, but it usually means the most recently-issued CRL. A CA
issues a new CRL on a regular periodic basis (e.g., hourly, daily, or
weekly). Entries are added to CRLs as revocations occur, and an
entry may be removed when the certificate expiration date is reached.

The X.509 v2 CRL format is described below in ASN.1:

```java
CertificateList ::= SEQUENCE {
tbsCertList TBSCertList,
signatureAlgorithm AlgorithmIdentifier,
signature BIT STRING }
```

More information can be found in

RFC 5280: Internet X.509
Public Key Infrastructure Certificate and CRL Profile

.

The ASN.1 definition of

tbsCertList

is:

```java
TBSCertList ::= SEQUENCE {
version Version OPTIONAL,
-- if present, must be v2
signature AlgorithmIdentifier,
issuer Name,
thisUpdate ChoiceOfTime,
nextUpdate ChoiceOfTime OPTIONAL,
revokedCertificates SEQUENCE OF SEQUENCE {
userCertificate CertificateSerialNumber,
revocationDate ChoiceOfTime,
crlEntryExtensions Extensions OPTIONAL
-- if present, must be v2
} OPTIONAL,
crlExtensions [0] EXPLICIT Extensions OPTIONAL
-- if present, must be v2
}
```

CRLs are instantiated using a certificate factory. The following is an
example of how to instantiate an X.509 CRL:

```java
try (InputStream inStream = new FileInputStream("fileName-of-crl")) {
CertificateFactory cf = CertificateFactory.getInstance("X.509");
X509CRL crl = (X509CRL)cf.generateCRL(inStream);
}
```

**All Implemented Interfaces:** X509Extension

---

### Field Details

*No entries found.*

### Constructor Details

#### protected X509CRL()

Constructor for X.509 CRLs.

---

### Method Details

#### public boolean equals​(
Object
other)

Compares this CRL for equality with the given
object. If the

other

object is an

instanceof

X509CRL

, then
its encoded form is retrieved and compared with the
encoded form of this CRL.

**Overrides:**
- equals

in class

Object

**Parameters:**
- other

- the object to test for equality with this CRL.

**Returns:**
- true iff the encoded forms of the two CRLs
match, false otherwise.

**See Also:**
- Object.hashCode()

,

HashMap

---

#### public int hashCode()

Returns a hashcode value for this CRL from its
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
CRLException

Returns the ASN.1 DER-encoded form of this CRL.

**Returns:**
- the encoded form of this certificate

**Throws:**
- CRLException

- if an encoding error occurs.

---

#### public abstract void verify​(
PublicKey
key)
throws
CRLException
,

NoSuchAlgorithmException
,

InvalidKeyException
,

NoSuchProviderException
,

SignatureException

Verifies that this CRL was signed using the
private key that corresponds to the given public key.

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
- CRLException

- on encoding errors.

---

#### public abstract void verify​(
PublicKey
key,

String
sigProvider)
throws
CRLException
,

NoSuchAlgorithmException
,

InvalidKeyException
,

NoSuchProviderException
,

SignatureException

Verifies that this CRL was signed using the
private key that corresponds to the given public key.
This method uses the signature verification engine
supplied by the given provider.

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
- CRLException

- on encoding errors.

---

#### public void verify​(
PublicKey
key,

Provider
sigProvider)
throws
CRLException
,

NoSuchAlgorithmException
,

InvalidKeyException
,

SignatureException

Verifies that this CRL was signed using the
private key that corresponds to the given public key.
This method uses the signature verification engine
supplied by the given provider. Note that the specified Provider object
does not have to be registered in the provider list.

This method was added to version 1.8 of the Java Platform Standard
Edition. In order to maintain backwards compatibility with existing
service providers, this method is not

abstract

and it provides a default implementation.

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
- CRLException

- on encoding errors.

**Since:**
- 1.8

---

#### public abstract int getVersion()

Gets the

version

(version number) value from the CRL.
The ASN.1 definition for this is:

```java
version Version OPTIONAL,
-- if present, must be v2

Version ::= INTEGER { v1(0), v2(1), v3(2) }
-- v3 does not apply to CRLs but appears for consistency
-- with definition of Version for certs
```

**Returns:**
- the version number, i.e. 1 or 2.

---

#### public abstract
Principal
getIssuerDN()

Denigrated

, replaced by

getIssuerX500Principal()

. This method returns the

issuer

as an implementation specific Principal object, which should not be
relied upon by portable code.

Gets the

issuer

(issuer distinguished name) value from
the CRL. The issuer name identifies the entity that signed (and
issued) the CRL.

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
attributes,
such as country name, and corresponding values, such as US.
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

#### public
X500Principal
getIssuerX500Principal()

Returns the issuer (issuer distinguished name) value from the
CRL as an

X500Principal

.

It is recommended that subclasses override this method.

**Returns:**
- an

X500Principal

representing the issuer
distinguished name

**Since:**
- 1.4

---

#### public abstract
Date
getThisUpdate()

Gets the

thisUpdate

date from the CRL.
The ASN.1 definition for this is:

```java
thisUpdate ChoiceOfTime
ChoiceOfTime ::= CHOICE {
utcTime UTCTime,
generalTime GeneralizedTime }
```

**Returns:**
- the

thisUpdate

date from the CRL.

---

#### public abstract
Date
getNextUpdate()

Gets the

nextUpdate

date from the CRL.

**Returns:**
- the

nextUpdate

date from the CRL, or null if
not present.

---

#### public abstract
X509CRLEntry
getRevokedCertificate​(
BigInteger
serialNumber)

Gets the CRL entry, if any, with the given certificate serialNumber.

**Parameters:**
- serialNumber

- the serial number of the certificate for which a CRL entry
is to be looked up

**Returns:**
- the entry with the given serial number, or null if no such entry
exists in this CRL.

**See Also:**
- X509CRLEntry

---

#### public
X509CRLEntry
getRevokedCertificate​(
X509Certificate
certificate)

Get the CRL entry, if any, for the given certificate.

This method can be used to lookup CRL entries in indirect CRLs,
that means CRLs that contain entries from issuers other than the CRL
issuer. The default implementation will only return entries for
certificates issued by the CRL issuer. Subclasses that wish to
support indirect CRLs should override this method.

**Parameters:**
- certificate

- the certificate for which a CRL entry is to be looked
up

**Returns:**
- the entry for the given certificate, or null if no such entry
exists in this CRL.

**Throws:**
- NullPointerException

- if certificate is null

**Since:**
- 1.5

---

#### public abstract
Set
<? extends
X509CRLEntry
> getRevokedCertificates()

Gets all the entries from this CRL.
This returns a Set of X509CRLEntry objects.

**Returns:**
- all the entries or null if there are none present.

**See Also:**
- X509CRLEntry

---

#### public abstract byte[] getTBSCertList()
throws
CRLException

Gets the DER-encoded CRL information, the

tbsCertList

from this CRL.
This can be used to verify the signature independently.

**Returns:**
- the DER-encoded CRL information.

**Throws:**
- CRLException

- if an encoding error occurs.

---

#### public abstract byte[] getSignature()

Gets the

signature

value (the raw signature bits) from
the CRL.
The ASN.1 definition for this is:

```java
signature BIT STRING
```

**Returns:**
- the signature.

---

#### public abstract
String
getSigAlgName()

Gets the signature algorithm name for the CRL
signature algorithm. An example is the string "SHA256withRSA".
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

Gets the signature algorithm OID string from the CRL.
An OID is represented by a set of nonnegative whole numbers separated
by periods.
For example, the string "1.2.840.10040.4.3" identifies the SHA-1
with DSA signature algorithm defined in

RFC 3279: Algorithms and
Identifiers for the Internet X.509 Public Key Infrastructure Certificate
and CRL Profile

.

See

getSigAlgName

for
relevant ASN.1 definitions.

**Returns:**
- the signature algorithm OID string.

---

#### public abstract byte[] getSigAlgParams()

Gets the DER-encoded signature algorithm parameters from this
CRL's signature algorithm. In most cases, the signature
algorithm parameters are null; the parameters are usually
supplied with the public key.
If access to individual parameter values is needed then use

AlgorithmParameters

and instantiate with the name returned by

getSigAlgName

.

See

getSigAlgName

for
relevant ASN.1 definitions.

**Returns:**
- the DER-encoded signature algorithm parameters, or
null if no parameters are present.

---

### Additional Sections

#### Class X509CRL

java.lang.Object

- java.security.cert.CRL
- - java.security.cert.X509CRL

java.security.cert.CRL

- java.security.cert.X509CRL

java.security.cert.X509CRL

**All Implemented Interfaces:** X509Extension

```java
public abstract class
X509CRL

extends
CRL

implements
X509Extension
```

Abstract class for an X.509 Certificate Revocation List (CRL).
A CRL is a time-stamped list identifying revoked certificates.
It is signed by a Certificate Authority (CA) and made freely
available in a public repository.

Each revoked certificate is
identified in a CRL by its certificate serial number. When a
certificate-using system uses a certificate (e.g., for verifying a
remote user's digital signature), that system not only checks the
certificate signature and validity but also acquires a suitably-
recent CRL and checks that the certificate serial number is not on
that CRL. The meaning of "suitably-recent" may vary with local
policy, but it usually means the most recently-issued CRL. A CA
issues a new CRL on a regular periodic basis (e.g., hourly, daily, or
weekly). Entries are added to CRLs as revocations occur, and an
entry may be removed when the certificate expiration date is reached.

The X.509 v2 CRL format is described below in ASN.1:

```java
CertificateList ::= SEQUENCE {
tbsCertList TBSCertList,
signatureAlgorithm AlgorithmIdentifier,
signature BIT STRING }
```

More information can be found in

RFC 5280: Internet X.509
Public Key Infrastructure Certificate and CRL Profile

.

The ASN.1 definition of

tbsCertList

is:

```java
TBSCertList ::= SEQUENCE {
version Version OPTIONAL,
-- if present, must be v2
signature AlgorithmIdentifier,
issuer Name,
thisUpdate ChoiceOfTime,
nextUpdate ChoiceOfTime OPTIONAL,
revokedCertificates SEQUENCE OF SEQUENCE {
userCertificate CertificateSerialNumber,
revocationDate ChoiceOfTime,
crlEntryExtensions Extensions OPTIONAL
-- if present, must be v2
} OPTIONAL,
crlExtensions [0] EXPLICIT Extensions OPTIONAL
-- if present, must be v2
}
```

CRLs are instantiated using a certificate factory. The following is an
example of how to instantiate an X.509 CRL:

```java
try (InputStream inStream = new FileInputStream("fileName-of-crl")) {
CertificateFactory cf = CertificateFactory.getInstance("X.509");
X509CRL crl = (X509CRL)cf.generateCRL(inStream);
}
```

**Since:** 1.2
**See Also:** CRL

,

CertificateFactory

,

X509Extension

public abstract class

X509CRL

extends

CRL

implements

X509Extension

Abstract class for an X.509 Certificate Revocation List (CRL).
A CRL is a time-stamped list identifying revoked certificates.
It is signed by a Certificate Authority (CA) and made freely
available in a public repository.

Each revoked certificate is
identified in a CRL by its certificate serial number. When a
certificate-using system uses a certificate (e.g., for verifying a
remote user's digital signature), that system not only checks the
certificate signature and validity but also acquires a suitably-
recent CRL and checks that the certificate serial number is not on
that CRL. The meaning of "suitably-recent" may vary with local
policy, but it usually means the most recently-issued CRL. A CA
issues a new CRL on a regular periodic basis (e.g., hourly, daily, or
weekly). Entries are added to CRLs as revocations occur, and an
entry may be removed when the certificate expiration date is reached.

The X.509 v2 CRL format is described below in ASN.1:

```java
CertificateList ::= SEQUENCE {
tbsCertList TBSCertList,
signatureAlgorithm AlgorithmIdentifier,
signature BIT STRING }
```

More information can be found in

RFC 5280: Internet X.509
Public Key Infrastructure Certificate and CRL Profile

.

The ASN.1 definition of

tbsCertList

is:

```java
TBSCertList ::= SEQUENCE {
version Version OPTIONAL,
-- if present, must be v2
signature AlgorithmIdentifier,
issuer Name,
thisUpdate ChoiceOfTime,
nextUpdate ChoiceOfTime OPTIONAL,
revokedCertificates SEQUENCE OF SEQUENCE {
userCertificate CertificateSerialNumber,
revocationDate ChoiceOfTime,
crlEntryExtensions Extensions OPTIONAL
-- if present, must be v2
} OPTIONAL,
crlExtensions [0] EXPLICIT Extensions OPTIONAL
-- if present, must be v2
}
```

CRLs are instantiated using a certificate factory. The following is an
example of how to instantiate an X.509 CRL:

```java
try (InputStream inStream = new FileInputStream("fileName-of-crl")) {
CertificateFactory cf = CertificateFactory.getInstance("X.509");
X509CRL crl = (X509CRL)cf.generateCRL(inStream);
}
```

Each revoked certificate is
identified in a CRL by its certificate serial number. When a
certificate-using system uses a certificate (e.g., for verifying a
remote user's digital signature), that system not only checks the
certificate signature and validity but also acquires a suitably-
recent CRL and checks that the certificate serial number is not on
that CRL. The meaning of "suitably-recent" may vary with local
policy, but it usually means the most recently-issued CRL. A CA
issues a new CRL on a regular periodic basis (e.g., hourly, daily, or
weekly). Entries are added to CRLs as revocations occur, and an
entry may be removed when the certificate expiration date is reached.

The X.509 v2 CRL format is described below in ASN.1:

```java
CertificateList ::= SEQUENCE {
tbsCertList TBSCertList,
signatureAlgorithm AlgorithmIdentifier,
signature BIT STRING }
```

More information can be found in

RFC 5280: Internet X.509
Public Key Infrastructure Certificate and CRL Profile

.

The ASN.1 definition of

tbsCertList

is:

```java
TBSCertList ::= SEQUENCE {
version Version OPTIONAL,
-- if present, must be v2
signature AlgorithmIdentifier,
issuer Name,
thisUpdate ChoiceOfTime,
nextUpdate ChoiceOfTime OPTIONAL,
revokedCertificates SEQUENCE OF SEQUENCE {
userCertificate CertificateSerialNumber,
revocationDate ChoiceOfTime,
crlEntryExtensions Extensions OPTIONAL
-- if present, must be v2
} OPTIONAL,
crlExtensions [0] EXPLICIT Extensions OPTIONAL
-- if present, must be v2
}
```

CRLs are instantiated using a certificate factory. The following is an
example of how to instantiate an X.509 CRL:

```java
try (InputStream inStream = new FileInputStream("fileName-of-crl")) {
CertificateFactory cf = CertificateFactory.getInstance("X.509");
X509CRL crl = (X509CRL)cf.generateCRL(inStream);
}
```

The X.509 v2 CRL format is described below in ASN.1:

```java
CertificateList ::= SEQUENCE {
tbsCertList TBSCertList,
signatureAlgorithm AlgorithmIdentifier,
signature BIT STRING }
```

More information can be found in

RFC 5280: Internet X.509
Public Key Infrastructure Certificate and CRL Profile

.

The ASN.1 definition of

tbsCertList

is:

```java
TBSCertList ::= SEQUENCE {
version Version OPTIONAL,
-- if present, must be v2
signature AlgorithmIdentifier,
issuer Name,
thisUpdate ChoiceOfTime,
nextUpdate ChoiceOfTime OPTIONAL,
revokedCertificates SEQUENCE OF SEQUENCE {
userCertificate CertificateSerialNumber,
revocationDate ChoiceOfTime,
crlEntryExtensions Extensions OPTIONAL
-- if present, must be v2
} OPTIONAL,
crlExtensions [0] EXPLICIT Extensions OPTIONAL
-- if present, must be v2
}
```

CRLs are instantiated using a certificate factory. The following is an
example of how to instantiate an X.509 CRL:

```java
try (InputStream inStream = new FileInputStream("fileName-of-crl")) {
CertificateFactory cf = CertificateFactory.getInstance("X.509");
X509CRL crl = (X509CRL)cf.generateCRL(inStream);
}
```

CertificateList ::= SEQUENCE {
tbsCertList TBSCertList,
signatureAlgorithm AlgorithmIdentifier,
signature BIT STRING }

More information can be found in

RFC 5280: Internet X.509
Public Key Infrastructure Certificate and CRL Profile

.

The ASN.1 definition of

tbsCertList

is:

```java
TBSCertList ::= SEQUENCE {
version Version OPTIONAL,
-- if present, must be v2
signature AlgorithmIdentifier,
issuer Name,
thisUpdate ChoiceOfTime,
nextUpdate ChoiceOfTime OPTIONAL,
revokedCertificates SEQUENCE OF SEQUENCE {
userCertificate CertificateSerialNumber,
revocationDate ChoiceOfTime,
crlEntryExtensions Extensions OPTIONAL
-- if present, must be v2
} OPTIONAL,
crlExtensions [0] EXPLICIT Extensions OPTIONAL
-- if present, must be v2
}
```

CRLs are instantiated using a certificate factory. The following is an
example of how to instantiate an X.509 CRL:

```java
try (InputStream inStream = new FileInputStream("fileName-of-crl")) {
CertificateFactory cf = CertificateFactory.getInstance("X.509");
X509CRL crl = (X509CRL)cf.generateCRL(inStream);
}
```

The ASN.1 definition of

tbsCertList

is:

```java
TBSCertList ::= SEQUENCE {
version Version OPTIONAL,
-- if present, must be v2
signature AlgorithmIdentifier,
issuer Name,
thisUpdate ChoiceOfTime,
nextUpdate ChoiceOfTime OPTIONAL,
revokedCertificates SEQUENCE OF SEQUENCE {
userCertificate CertificateSerialNumber,
revocationDate ChoiceOfTime,
crlEntryExtensions Extensions OPTIONAL
-- if present, must be v2
} OPTIONAL,
crlExtensions [0] EXPLICIT Extensions OPTIONAL
-- if present, must be v2
}
```

CRLs are instantiated using a certificate factory. The following is an
example of how to instantiate an X.509 CRL:

```java
try (InputStream inStream = new FileInputStream("fileName-of-crl")) {
CertificateFactory cf = CertificateFactory.getInstance("X.509");
X509CRL crl = (X509CRL)cf.generateCRL(inStream);
}
```

TBSCertList ::= SEQUENCE {
version Version OPTIONAL,
-- if present, must be v2
signature AlgorithmIdentifier,
issuer Name,
thisUpdate ChoiceOfTime,
nextUpdate ChoiceOfTime OPTIONAL,
revokedCertificates SEQUENCE OF SEQUENCE {
userCertificate CertificateSerialNumber,
revocationDate ChoiceOfTime,
crlEntryExtensions Extensions OPTIONAL
-- if present, must be v2
} OPTIONAL,
crlExtensions [0] EXPLICIT Extensions OPTIONAL
-- if present, must be v2
}

CRLs are instantiated using a certificate factory. The following is an
example of how to instantiate an X.509 CRL:

```java
try (InputStream inStream = new FileInputStream("fileName-of-crl")) {
CertificateFactory cf = CertificateFactory.getInstance("X.509");
X509CRL crl = (X509CRL)cf.generateCRL(inStream);
}
```

try (InputStream inStream = new FileInputStream("fileName-of-crl")) {
CertificateFactory cf = CertificateFactory.getInstance("X.509");
X509CRL crl = (X509CRL)cf.generateCRL(inStream);
}

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

X509CRL

()

Constructor for X.509 CRLs.

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

Compares this CRL for equality with the given
object.

abstract byte[]

getEncoded

()

Returns the ASN.1 DER-encoded form of this CRL.

abstract

Principal

getIssuerDN

()

Denigrated

, replaced by

getIssuerX500Principal()

.

X500Principal

getIssuerX500Principal

()

Returns the issuer (issuer distinguished name) value from the
CRL as an

X500Principal

.

abstract

Date

getNextUpdate

()

Gets the

nextUpdate

date from the CRL.

abstract

X509CRLEntry

getRevokedCertificate

​(

BigInteger

serialNumber)

Gets the CRL entry, if any, with the given certificate serialNumber.

X509CRLEntry

getRevokedCertificate

​(

X509Certificate

certificate)

Get the CRL entry, if any, for the given certificate.

abstract

Set

<? extends

X509CRLEntry

>

getRevokedCertificates

()

Gets all the entries from this CRL.

abstract

String

getSigAlgName

()

Gets the signature algorithm name for the CRL
signature algorithm.

abstract

String

getSigAlgOID

()

Gets the signature algorithm OID string from the CRL.

abstract byte[]

getSigAlgParams

()

Gets the DER-encoded signature algorithm parameters from this
CRL's signature algorithm.

abstract byte[]

getSignature

()

Gets the

signature

value (the raw signature bits) from
the CRL.

abstract byte[]

getTBSCertList

()

Gets the DER-encoded CRL information, the

tbsCertList

from this CRL.

abstract

Date

getThisUpdate

()

Gets the

thisUpdate

date from the CRL.

abstract int

getVersion

()

Gets the

version

(version number) value from the CRL.

int

hashCode

()

Returns a hashcode value for this CRL from its
encoded form.

abstract void

verify

​(

PublicKey

key)

Verifies that this CRL was signed using the
private key that corresponds to the given public key.

abstract void

verify

​(

PublicKey

key,

String

sigProvider)

Verifies that this CRL was signed using the
private key that corresponds to the given public key.

void

verify

​(

PublicKey

key,

Provider

sigProvider)

Verifies that this CRL was signed using the
private key that corresponds to the given public key.

- Methods declared in class java.security.cert.

CRL

getType

,

isRevoked

,

toString

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

- Methods declared in interface java.security.cert.

X509Extension

getCriticalExtensionOIDs

,

getExtensionValue

,

getNonCriticalExtensionOIDs

,

hasUnsupportedCriticalExtension

Constructor Summary

Constructors

Modifier

Constructor

Description

protected

X509CRL

()

Constructor for X.509 CRLs.

---

#### Constructor Summary

Constructor for X.509 CRLs.

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

Compares this CRL for equality with the given
object.

abstract byte[]

getEncoded

()

Returns the ASN.1 DER-encoded form of this CRL.

abstract

Principal

getIssuerDN

()

Denigrated

, replaced by

getIssuerX500Principal()

.

X500Principal

getIssuerX500Principal

()

Returns the issuer (issuer distinguished name) value from the
CRL as an

X500Principal

.

abstract

Date

getNextUpdate

()

Gets the

nextUpdate

date from the CRL.

abstract

X509CRLEntry

getRevokedCertificate

​(

BigInteger

serialNumber)

Gets the CRL entry, if any, with the given certificate serialNumber.

X509CRLEntry

getRevokedCertificate

​(

X509Certificate

certificate)

Get the CRL entry, if any, for the given certificate.

abstract

Set

<? extends

X509CRLEntry

>

getRevokedCertificates

()

Gets all the entries from this CRL.

abstract

String

getSigAlgName

()

Gets the signature algorithm name for the CRL
signature algorithm.

abstract

String

getSigAlgOID

()

Gets the signature algorithm OID string from the CRL.

abstract byte[]

getSigAlgParams

()

Gets the DER-encoded signature algorithm parameters from this
CRL's signature algorithm.

abstract byte[]

getSignature

()

Gets the

signature

value (the raw signature bits) from
the CRL.

abstract byte[]

getTBSCertList

()

Gets the DER-encoded CRL information, the

tbsCertList

from this CRL.

abstract

Date

getThisUpdate

()

Gets the

thisUpdate

date from the CRL.

abstract int

getVersion

()

Gets the

version

(version number) value from the CRL.

int

hashCode

()

Returns a hashcode value for this CRL from its
encoded form.

abstract void

verify

​(

PublicKey

key)

Verifies that this CRL was signed using the
private key that corresponds to the given public key.

abstract void

verify

​(

PublicKey

key,

String

sigProvider)

Verifies that this CRL was signed using the
private key that corresponds to the given public key.

void

verify

​(

PublicKey

key,

Provider

sigProvider)

Verifies that this CRL was signed using the
private key that corresponds to the given public key.

- Methods declared in class java.security.cert.

CRL

getType

,

isRevoked

,

toString

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

- Methods declared in interface java.security.cert.

X509Extension

getCriticalExtensionOIDs

,

getExtensionValue

,

getNonCriticalExtensionOIDs

,

hasUnsupportedCriticalExtension

---

#### Method Summary

Compares this CRL for equality with the given
object.

Returns the ASN.1 DER-encoded form of this CRL.

Denigrated

, replaced by

getIssuerX500Principal()

.

Returns the issuer (issuer distinguished name) value from the
CRL as an

X500Principal

.

Gets the

nextUpdate

date from the CRL.

Gets the CRL entry, if any, with the given certificate serialNumber.

Get the CRL entry, if any, for the given certificate.

Gets all the entries from this CRL.

Gets the signature algorithm name for the CRL
signature algorithm.

Gets the signature algorithm OID string from the CRL.

Gets the DER-encoded signature algorithm parameters from this
CRL's signature algorithm.

Gets the

signature

value (the raw signature bits) from
the CRL.

Gets the DER-encoded CRL information, the

tbsCertList

from this CRL.

Gets the

thisUpdate

date from the CRL.

Gets the

version

(version number) value from the CRL.

Returns a hashcode value for this CRL from its
encoded form.

Verifies that this CRL was signed using the
private key that corresponds to the given public key.

Methods declared in class java.security.cert.

CRL

getType

,

isRevoked

,

toString

---

#### Methods declared in class java.security.cert. CRL

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

Methods declared in interface java.security.cert.

X509Extension

getCriticalExtensionOIDs

,

getExtensionValue

,

getNonCriticalExtensionOIDs

,

hasUnsupportedCriticalExtension

---

#### Methods declared in interface java.security.cert. X509Extension

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- X509CRL

```java
protected X509CRL()
```

Constructor for X.509 CRLs.

============ METHOD DETAIL ==========

- Method Detail

- equals

```java
public boolean equals​(
Object
other)
```

Compares this CRL for equality with the given
object. If the

other

object is an

instanceof

X509CRL

, then
its encoded form is retrieved and compared with the
encoded form of this CRL.

**Overrides:** equals

in class

Object
**Parameters:** other

- the object to test for equality with this CRL.
**Returns:** true iff the encoded forms of the two CRLs
match, false otherwise.
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
public int hashCode()
```

Returns a hashcode value for this CRL from its
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
CRLException
```

Returns the ASN.1 DER-encoded form of this CRL.

**Returns:** the encoded form of this certificate
**Throws:** CRLException

- if an encoding error occurs.

- verify

```java
public abstract void verify​(
PublicKey
key)
throws
CRLException
,

NoSuchAlgorithmException
,

InvalidKeyException
,

NoSuchProviderException
,

SignatureException
```

Verifies that this CRL was signed using the
private key that corresponds to the given public key.

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
**Throws:** CRLException

- on encoding errors.

- verify

```java
public abstract void verify​(
PublicKey
key,

String
sigProvider)
throws
CRLException
,

NoSuchAlgorithmException
,

InvalidKeyException
,

NoSuchProviderException
,

SignatureException
```

Verifies that this CRL was signed using the
private key that corresponds to the given public key.
This method uses the signature verification engine
supplied by the given provider.

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
**Throws:** CRLException

- on encoding errors.

- verify

```java
public void verify​(
PublicKey
key,

Provider
sigProvider)
throws
CRLException
,

NoSuchAlgorithmException
,

InvalidKeyException
,

SignatureException
```

Verifies that this CRL was signed using the
private key that corresponds to the given public key.
This method uses the signature verification engine
supplied by the given provider. Note that the specified Provider object
does not have to be registered in the provider list.

This method was added to version 1.8 of the Java Platform Standard
Edition. In order to maintain backwards compatibility with existing
service providers, this method is not

abstract

and it provides a default implementation.

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
**Throws:** CRLException

- on encoding errors.
**Since:** 1.8

- getVersion

```java
public abstract int getVersion()
```

Gets the

version

(version number) value from the CRL.
The ASN.1 definition for this is:

```java
version Version OPTIONAL,
-- if present, must be v2

Version ::= INTEGER { v1(0), v2(1), v3(2) }
-- v3 does not apply to CRLs but appears for consistency
-- with definition of Version for certs
```

**Returns:** the version number, i.e. 1 or 2.

- getIssuerDN

```java
public abstract
Principal
getIssuerDN()
```

Denigrated

, replaced by

getIssuerX500Principal()

. This method returns the

issuer

as an implementation specific Principal object, which should not be
relied upon by portable code.

Gets the

issuer

(issuer distinguished name) value from
the CRL. The issuer name identifies the entity that signed (and
issued) the CRL.

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
attributes,
such as country name, and corresponding values, such as US.
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

- getIssuerX500Principal

```java
public
X500Principal
getIssuerX500Principal()
```

Returns the issuer (issuer distinguished name) value from the
CRL as an

X500Principal

.

It is recommended that subclasses override this method.

**Returns:** an

X500Principal

representing the issuer
distinguished name
**Since:** 1.4

- getThisUpdate

```java
public abstract
Date
getThisUpdate()
```

Gets the

thisUpdate

date from the CRL.
The ASN.1 definition for this is:

```java
thisUpdate ChoiceOfTime
ChoiceOfTime ::= CHOICE {
utcTime UTCTime,
generalTime GeneralizedTime }
```

**Returns:** the

thisUpdate

date from the CRL.

- getNextUpdate

```java
public abstract
Date
getNextUpdate()
```

Gets the

nextUpdate

date from the CRL.

**Returns:** the

nextUpdate

date from the CRL, or null if
not present.

- getRevokedCertificate

```java
public abstract
X509CRLEntry
getRevokedCertificate​(
BigInteger
serialNumber)
```

Gets the CRL entry, if any, with the given certificate serialNumber.

**Parameters:** serialNumber

- the serial number of the certificate for which a CRL entry
is to be looked up
**Returns:** the entry with the given serial number, or null if no such entry
exists in this CRL.
**See Also:** X509CRLEntry

- getRevokedCertificate

```java
public
X509CRLEntry
getRevokedCertificate​(
X509Certificate
certificate)
```

Get the CRL entry, if any, for the given certificate.

This method can be used to lookup CRL entries in indirect CRLs,
that means CRLs that contain entries from issuers other than the CRL
issuer. The default implementation will only return entries for
certificates issued by the CRL issuer. Subclasses that wish to
support indirect CRLs should override this method.

**Parameters:** certificate

- the certificate for which a CRL entry is to be looked
up
**Returns:** the entry for the given certificate, or null if no such entry
exists in this CRL.
**Throws:** NullPointerException

- if certificate is null
**Since:** 1.5

- getRevokedCertificates

```java
public abstract
Set
<? extends
X509CRLEntry
> getRevokedCertificates()
```

Gets all the entries from this CRL.
This returns a Set of X509CRLEntry objects.

**Returns:** all the entries or null if there are none present.
**See Also:** X509CRLEntry

- getTBSCertList

```java
public abstract byte[] getTBSCertList()
throws
CRLException
```

Gets the DER-encoded CRL information, the

tbsCertList

from this CRL.
This can be used to verify the signature independently.

**Returns:** the DER-encoded CRL information.
**Throws:** CRLException

- if an encoding error occurs.

- getSignature

```java
public abstract byte[] getSignature()
```

Gets the

signature

value (the raw signature bits) from
the CRL.
The ASN.1 definition for this is:

```java
signature BIT STRING
```

**Returns:** the signature.

- getSigAlgName

```java
public abstract
String
getSigAlgName()
```

Gets the signature algorithm name for the CRL
signature algorithm. An example is the string "SHA256withRSA".
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

Gets the signature algorithm OID string from the CRL.
An OID is represented by a set of nonnegative whole numbers separated
by periods.
For example, the string "1.2.840.10040.4.3" identifies the SHA-1
with DSA signature algorithm defined in

RFC 3279: Algorithms and
Identifiers for the Internet X.509 Public Key Infrastructure Certificate
and CRL Profile

.

See

getSigAlgName

for
relevant ASN.1 definitions.

**Returns:** the signature algorithm OID string.

- getSigAlgParams

```java
public abstract byte[] getSigAlgParams()
```

Gets the DER-encoded signature algorithm parameters from this
CRL's signature algorithm. In most cases, the signature
algorithm parameters are null; the parameters are usually
supplied with the public key.
If access to individual parameter values is needed then use

AlgorithmParameters

and instantiate with the name returned by

getSigAlgName

.

See

getSigAlgName

for
relevant ASN.1 definitions.

**Returns:** the DER-encoded signature algorithm parameters, or
null if no parameters are present.

Constructor Detail

- X509CRL

```java
protected X509CRL()
```

Constructor for X.509 CRLs.

---

#### Constructor Detail

X509CRL

```java
protected X509CRL()
```

Constructor for X.509 CRLs.

---

#### X509CRL

protected X509CRL()

Constructor for X.509 CRLs.

Method Detail

- equals

```java
public boolean equals​(
Object
other)
```

Compares this CRL for equality with the given
object. If the

other

object is an

instanceof

X509CRL

, then
its encoded form is retrieved and compared with the
encoded form of this CRL.

**Overrides:** equals

in class

Object
**Parameters:** other

- the object to test for equality with this CRL.
**Returns:** true iff the encoded forms of the two CRLs
match, false otherwise.
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
public int hashCode()
```

Returns a hashcode value for this CRL from its
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
CRLException
```

Returns the ASN.1 DER-encoded form of this CRL.

**Returns:** the encoded form of this certificate
**Throws:** CRLException

- if an encoding error occurs.

- verify

```java
public abstract void verify​(
PublicKey
key)
throws
CRLException
,

NoSuchAlgorithmException
,

InvalidKeyException
,

NoSuchProviderException
,

SignatureException
```

Verifies that this CRL was signed using the
private key that corresponds to the given public key.

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
**Throws:** CRLException

- on encoding errors.

- verify

```java
public abstract void verify​(
PublicKey
key,

String
sigProvider)
throws
CRLException
,

NoSuchAlgorithmException
,

InvalidKeyException
,

NoSuchProviderException
,

SignatureException
```

Verifies that this CRL was signed using the
private key that corresponds to the given public key.
This method uses the signature verification engine
supplied by the given provider.

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
**Throws:** CRLException

- on encoding errors.

- verify

```java
public void verify​(
PublicKey
key,

Provider
sigProvider)
throws
CRLException
,

NoSuchAlgorithmException
,

InvalidKeyException
,

SignatureException
```

Verifies that this CRL was signed using the
private key that corresponds to the given public key.
This method uses the signature verification engine
supplied by the given provider. Note that the specified Provider object
does not have to be registered in the provider list.

This method was added to version 1.8 of the Java Platform Standard
Edition. In order to maintain backwards compatibility with existing
service providers, this method is not

abstract

and it provides a default implementation.

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
**Throws:** CRLException

- on encoding errors.
**Since:** 1.8

- getVersion

```java
public abstract int getVersion()
```

Gets the

version

(version number) value from the CRL.
The ASN.1 definition for this is:

```java
version Version OPTIONAL,
-- if present, must be v2

Version ::= INTEGER { v1(0), v2(1), v3(2) }
-- v3 does not apply to CRLs but appears for consistency
-- with definition of Version for certs
```

**Returns:** the version number, i.e. 1 or 2.

- getIssuerDN

```java
public abstract
Principal
getIssuerDN()
```

Denigrated

, replaced by

getIssuerX500Principal()

. This method returns the

issuer

as an implementation specific Principal object, which should not be
relied upon by portable code.

Gets the

issuer

(issuer distinguished name) value from
the CRL. The issuer name identifies the entity that signed (and
issued) the CRL.

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
attributes,
such as country name, and corresponding values, such as US.
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

- getIssuerX500Principal

```java
public
X500Principal
getIssuerX500Principal()
```

Returns the issuer (issuer distinguished name) value from the
CRL as an

X500Principal

.

It is recommended that subclasses override this method.

**Returns:** an

X500Principal

representing the issuer
distinguished name
**Since:** 1.4

- getThisUpdate

```java
public abstract
Date
getThisUpdate()
```

Gets the

thisUpdate

date from the CRL.
The ASN.1 definition for this is:

```java
thisUpdate ChoiceOfTime
ChoiceOfTime ::= CHOICE {
utcTime UTCTime,
generalTime GeneralizedTime }
```

**Returns:** the

thisUpdate

date from the CRL.

- getNextUpdate

```java
public abstract
Date
getNextUpdate()
```

Gets the

nextUpdate

date from the CRL.

**Returns:** the

nextUpdate

date from the CRL, or null if
not present.

- getRevokedCertificate

```java
public abstract
X509CRLEntry
getRevokedCertificate​(
BigInteger
serialNumber)
```

Gets the CRL entry, if any, with the given certificate serialNumber.

**Parameters:** serialNumber

- the serial number of the certificate for which a CRL entry
is to be looked up
**Returns:** the entry with the given serial number, or null if no such entry
exists in this CRL.
**See Also:** X509CRLEntry

- getRevokedCertificate

```java
public
X509CRLEntry
getRevokedCertificate​(
X509Certificate
certificate)
```

Get the CRL entry, if any, for the given certificate.

This method can be used to lookup CRL entries in indirect CRLs,
that means CRLs that contain entries from issuers other than the CRL
issuer. The default implementation will only return entries for
certificates issued by the CRL issuer. Subclasses that wish to
support indirect CRLs should override this method.

**Parameters:** certificate

- the certificate for which a CRL entry is to be looked
up
**Returns:** the entry for the given certificate, or null if no such entry
exists in this CRL.
**Throws:** NullPointerException

- if certificate is null
**Since:** 1.5

- getRevokedCertificates

```java
public abstract
Set
<? extends
X509CRLEntry
> getRevokedCertificates()
```

Gets all the entries from this CRL.
This returns a Set of X509CRLEntry objects.

**Returns:** all the entries or null if there are none present.
**See Also:** X509CRLEntry

- getTBSCertList

```java
public abstract byte[] getTBSCertList()
throws
CRLException
```

Gets the DER-encoded CRL information, the

tbsCertList

from this CRL.
This can be used to verify the signature independently.

**Returns:** the DER-encoded CRL information.
**Throws:** CRLException

- if an encoding error occurs.

- getSignature

```java
public abstract byte[] getSignature()
```

Gets the

signature

value (the raw signature bits) from
the CRL.
The ASN.1 definition for this is:

```java
signature BIT STRING
```

**Returns:** the signature.

- getSigAlgName

```java
public abstract
String
getSigAlgName()
```

Gets the signature algorithm name for the CRL
signature algorithm. An example is the string "SHA256withRSA".
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

Gets the signature algorithm OID string from the CRL.
An OID is represented by a set of nonnegative whole numbers separated
by periods.
For example, the string "1.2.840.10040.4.3" identifies the SHA-1
with DSA signature algorithm defined in

RFC 3279: Algorithms and
Identifiers for the Internet X.509 Public Key Infrastructure Certificate
and CRL Profile

.

See

getSigAlgName

for
relevant ASN.1 definitions.

**Returns:** the signature algorithm OID string.

- getSigAlgParams

```java
public abstract byte[] getSigAlgParams()
```

Gets the DER-encoded signature algorithm parameters from this
CRL's signature algorithm. In most cases, the signature
algorithm parameters are null; the parameters are usually
supplied with the public key.
If access to individual parameter values is needed then use

AlgorithmParameters

and instantiate with the name returned by

getSigAlgName

.

See

getSigAlgName

for
relevant ASN.1 definitions.

**Returns:** the DER-encoded signature algorithm parameters, or
null if no parameters are present.

---

#### Method Detail

equals

```java
public boolean equals​(
Object
other)
```

Compares this CRL for equality with the given
object. If the

other

object is an

instanceof

X509CRL

, then
its encoded form is retrieved and compared with the
encoded form of this CRL.

**Overrides:** equals

in class

Object
**Parameters:** other

- the object to test for equality with this CRL.
**Returns:** true iff the encoded forms of the two CRLs
match, false otherwise.
**See Also:** Object.hashCode()

,

HashMap

---

#### equals

public boolean equals​(

Object

other)

Compares this CRL for equality with the given
object. If the

other

object is an

instanceof

X509CRL

, then
its encoded form is retrieved and compared with the
encoded form of this CRL.

hashCode

```java
public int hashCode()
```

Returns a hashcode value for this CRL from its
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

Returns a hashcode value for this CRL from its
encoded form.

getEncoded

```java
public abstract byte[] getEncoded()
throws
CRLException
```

Returns the ASN.1 DER-encoded form of this CRL.

**Returns:** the encoded form of this certificate
**Throws:** CRLException

- if an encoding error occurs.

---

#### getEncoded

public abstract byte[] getEncoded()
throws

CRLException

Returns the ASN.1 DER-encoded form of this CRL.

verify

```java
public abstract void verify​(
PublicKey
key)
throws
CRLException
,

NoSuchAlgorithmException
,

InvalidKeyException
,

NoSuchProviderException
,

SignatureException
```

Verifies that this CRL was signed using the
private key that corresponds to the given public key.

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
**Throws:** CRLException

- on encoding errors.

---

#### verify

public abstract void verify​(

PublicKey

key)
throws

CRLException

,

NoSuchAlgorithmException

,

InvalidKeyException

,

NoSuchProviderException

,

SignatureException

Verifies that this CRL was signed using the
private key that corresponds to the given public key.

verify

```java
public abstract void verify​(
PublicKey
key,

String
sigProvider)
throws
CRLException
,

NoSuchAlgorithmException
,

InvalidKeyException
,

NoSuchProviderException
,

SignatureException
```

Verifies that this CRL was signed using the
private key that corresponds to the given public key.
This method uses the signature verification engine
supplied by the given provider.

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
**Throws:** CRLException

- on encoding errors.

---

#### verify

public abstract void verify​(

PublicKey

key,

String

sigProvider)
throws

CRLException

,

NoSuchAlgorithmException

,

InvalidKeyException

,

NoSuchProviderException

,

SignatureException

Verifies that this CRL was signed using the
private key that corresponds to the given public key.
This method uses the signature verification engine
supplied by the given provider.

verify

```java
public void verify​(
PublicKey
key,

Provider
sigProvider)
throws
CRLException
,

NoSuchAlgorithmException
,

InvalidKeyException
,

SignatureException
```

Verifies that this CRL was signed using the
private key that corresponds to the given public key.
This method uses the signature verification engine
supplied by the given provider. Note that the specified Provider object
does not have to be registered in the provider list.

This method was added to version 1.8 of the Java Platform Standard
Edition. In order to maintain backwards compatibility with existing
service providers, this method is not

abstract

and it provides a default implementation.

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
**Throws:** CRLException

- on encoding errors.
**Since:** 1.8

---

#### verify

public void verify​(

PublicKey

key,

Provider

sigProvider)
throws

CRLException

,

NoSuchAlgorithmException

,

InvalidKeyException

,

SignatureException

Verifies that this CRL was signed using the
private key that corresponds to the given public key.
This method uses the signature verification engine
supplied by the given provider. Note that the specified Provider object
does not have to be registered in the provider list.

This method was added to version 1.8 of the Java Platform Standard
Edition. In order to maintain backwards compatibility with existing
service providers, this method is not

abstract

and it provides a default implementation.

getVersion

```java
public abstract int getVersion()
```

Gets the

version

(version number) value from the CRL.
The ASN.1 definition for this is:

```java
version Version OPTIONAL,
-- if present, must be v2

Version ::= INTEGER { v1(0), v2(1), v3(2) }
-- v3 does not apply to CRLs but appears for consistency
-- with definition of Version for certs
```

**Returns:** the version number, i.e. 1 or 2.

---

#### getVersion

public abstract int getVersion()

Gets the

version

(version number) value from the CRL.
The ASN.1 definition for this is:

```java
version Version OPTIONAL,
-- if present, must be v2

Version ::= INTEGER { v1(0), v2(1), v3(2) }
-- v3 does not apply to CRLs but appears for consistency
-- with definition of Version for certs
```

version Version OPTIONAL,
-- if present, must be v2

Version ::= INTEGER { v1(0), v2(1), v3(2) }
-- v3 does not apply to CRLs but appears for consistency
-- with definition of Version for certs

getIssuerDN

```java
public abstract
Principal
getIssuerDN()
```

Denigrated

, replaced by

getIssuerX500Principal()

. This method returns the

issuer

as an implementation specific Principal object, which should not be
relied upon by portable code.

Gets the

issuer

(issuer distinguished name) value from
the CRL. The issuer name identifies the entity that signed (and
issued) the CRL.

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
attributes,
such as country name, and corresponding values, such as US.
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

Denigrated

, replaced by

getIssuerX500Principal()

. This method returns the

issuer

as an implementation specific Principal object, which should not be
relied upon by portable code.

Gets the

issuer

(issuer distinguished name) value from
the CRL. The issuer name identifies the entity that signed (and
issued) the CRL.

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
attributes,
such as country name, and corresponding values, such as US.
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

Gets the

issuer

(issuer distinguished name) value from
the CRL. The issuer name identifies the entity that signed (and
issued) the CRL.

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
attributes,
such as country name, and corresponding values, such as US.
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
attributes,
such as country name, and corresponding values, such as US.
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

getIssuerX500Principal

```java
public
X500Principal
getIssuerX500Principal()
```

Returns the issuer (issuer distinguished name) value from the
CRL as an

X500Principal

.

It is recommended that subclasses override this method.

**Returns:** an

X500Principal

representing the issuer
distinguished name
**Since:** 1.4

---

#### getIssuerX500Principal

public

X500Principal

getIssuerX500Principal()

Returns the issuer (issuer distinguished name) value from the
CRL as an

X500Principal

.

It is recommended that subclasses override this method.

It is recommended that subclasses override this method.

getThisUpdate

```java
public abstract
Date
getThisUpdate()
```

Gets the

thisUpdate

date from the CRL.
The ASN.1 definition for this is:

```java
thisUpdate ChoiceOfTime
ChoiceOfTime ::= CHOICE {
utcTime UTCTime,
generalTime GeneralizedTime }
```

**Returns:** the

thisUpdate

date from the CRL.

---

#### getThisUpdate

public abstract

Date

getThisUpdate()

Gets the

thisUpdate

date from the CRL.
The ASN.1 definition for this is:

```java
thisUpdate ChoiceOfTime
ChoiceOfTime ::= CHOICE {
utcTime UTCTime,
generalTime GeneralizedTime }
```

thisUpdate ChoiceOfTime
ChoiceOfTime ::= CHOICE {
utcTime UTCTime,
generalTime GeneralizedTime }

getNextUpdate

```java
public abstract
Date
getNextUpdate()
```

Gets the

nextUpdate

date from the CRL.

**Returns:** the

nextUpdate

date from the CRL, or null if
not present.

---

#### getNextUpdate

public abstract

Date

getNextUpdate()

Gets the

nextUpdate

date from the CRL.

getRevokedCertificate

```java
public abstract
X509CRLEntry
getRevokedCertificate​(
BigInteger
serialNumber)
```

Gets the CRL entry, if any, with the given certificate serialNumber.

**Parameters:** serialNumber

- the serial number of the certificate for which a CRL entry
is to be looked up
**Returns:** the entry with the given serial number, or null if no such entry
exists in this CRL.
**See Also:** X509CRLEntry

---

#### getRevokedCertificate

public abstract

X509CRLEntry

getRevokedCertificate​(

BigInteger

serialNumber)

Gets the CRL entry, if any, with the given certificate serialNumber.

getRevokedCertificate

```java
public
X509CRLEntry
getRevokedCertificate​(
X509Certificate
certificate)
```

Get the CRL entry, if any, for the given certificate.

This method can be used to lookup CRL entries in indirect CRLs,
that means CRLs that contain entries from issuers other than the CRL
issuer. The default implementation will only return entries for
certificates issued by the CRL issuer. Subclasses that wish to
support indirect CRLs should override this method.

**Parameters:** certificate

- the certificate for which a CRL entry is to be looked
up
**Returns:** the entry for the given certificate, or null if no such entry
exists in this CRL.
**Throws:** NullPointerException

- if certificate is null
**Since:** 1.5

---

#### getRevokedCertificate

public

X509CRLEntry

getRevokedCertificate​(

X509Certificate

certificate)

Get the CRL entry, if any, for the given certificate.

This method can be used to lookup CRL entries in indirect CRLs,
that means CRLs that contain entries from issuers other than the CRL
issuer. The default implementation will only return entries for
certificates issued by the CRL issuer. Subclasses that wish to
support indirect CRLs should override this method.

This method can be used to lookup CRL entries in indirect CRLs,
that means CRLs that contain entries from issuers other than the CRL
issuer. The default implementation will only return entries for
certificates issued by the CRL issuer. Subclasses that wish to
support indirect CRLs should override this method.

getRevokedCertificates

```java
public abstract
Set
<? extends
X509CRLEntry
> getRevokedCertificates()
```

Gets all the entries from this CRL.
This returns a Set of X509CRLEntry objects.

**Returns:** all the entries or null if there are none present.
**See Also:** X509CRLEntry

---

#### getRevokedCertificates

public abstract

Set

<? extends

X509CRLEntry

> getRevokedCertificates()

Gets all the entries from this CRL.
This returns a Set of X509CRLEntry objects.

getTBSCertList

```java
public abstract byte[] getTBSCertList()
throws
CRLException
```

Gets the DER-encoded CRL information, the

tbsCertList

from this CRL.
This can be used to verify the signature independently.

**Returns:** the DER-encoded CRL information.
**Throws:** CRLException

- if an encoding error occurs.

---

#### getTBSCertList

public abstract byte[] getTBSCertList()
throws

CRLException

Gets the DER-encoded CRL information, the

tbsCertList

from this CRL.
This can be used to verify the signature independently.

getSignature

```java
public abstract byte[] getSignature()
```

Gets the

signature

value (the raw signature bits) from
the CRL.
The ASN.1 definition for this is:

```java
signature BIT STRING
```

**Returns:** the signature.

---

#### getSignature

public abstract byte[] getSignature()

Gets the

signature

value (the raw signature bits) from
the CRL.
The ASN.1 definition for this is:

```java
signature BIT STRING
```

signature BIT STRING

getSigAlgName

```java
public abstract
String
getSigAlgName()
```

Gets the signature algorithm name for the CRL
signature algorithm. An example is the string "SHA256withRSA".
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

Gets the signature algorithm name for the CRL
signature algorithm. An example is the string "SHA256withRSA".
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

Gets the signature algorithm OID string from the CRL.
An OID is represented by a set of nonnegative whole numbers separated
by periods.
For example, the string "1.2.840.10040.4.3" identifies the SHA-1
with DSA signature algorithm defined in

RFC 3279: Algorithms and
Identifiers for the Internet X.509 Public Key Infrastructure Certificate
and CRL Profile

.

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

Gets the signature algorithm OID string from the CRL.
An OID is represented by a set of nonnegative whole numbers separated
by periods.
For example, the string "1.2.840.10040.4.3" identifies the SHA-1
with DSA signature algorithm defined in

RFC 3279: Algorithms and
Identifiers for the Internet X.509 Public Key Infrastructure Certificate
and CRL Profile

.

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

Gets the DER-encoded signature algorithm parameters from this
CRL's signature algorithm. In most cases, the signature
algorithm parameters are null; the parameters are usually
supplied with the public key.
If access to individual parameter values is needed then use

AlgorithmParameters

and instantiate with the name returned by

getSigAlgName

.

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
CRL's signature algorithm. In most cases, the signature
algorithm parameters are null; the parameters are usually
supplied with the public key.
If access to individual parameter values is needed then use

AlgorithmParameters

and instantiate with the name returned by

getSigAlgName

.

See

getSigAlgName

for
relevant ASN.1 definitions.

See

getSigAlgName

for
relevant ASN.1 definitions.

---

