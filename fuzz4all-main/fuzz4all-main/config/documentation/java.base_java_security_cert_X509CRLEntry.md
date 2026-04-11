# Class X509CRLEntry

**Source:** `java.base\java\security\cert\X509CRLEntry.html`

### Class Description

```java
public abstract class
X509CRLEntry

extends
Object

implements
X509Extension
```

Abstract class for a revoked certificate in a CRL (Certificate
Revocation List).

The ASN.1 definition for

revokedCertificates

is:

```java
revokedCertificates SEQUENCE OF SEQUENCE {
userCertificate CertificateSerialNumber,
revocationDate ChoiceOfTime,
crlEntryExtensions Extensions OPTIONAL
-- if present, must be v2
} OPTIONAL

CertificateSerialNumber ::= INTEGER

Extensions ::= SEQUENCE SIZE (1..MAX) OF Extension

Extension ::= SEQUENCE {
extnId OBJECT IDENTIFIER,
critical BOOLEAN DEFAULT FALSE,
extnValue OCTET STRING
-- contains a DER encoding of a value
-- of the type registered for use with
-- the extnId object identifier value
}
```

**All Implemented Interfaces:** X509Extension

---

### Field Details

*No entries found.*

### Constructor Details

#### public X509CRLEntry()

*No description found.*

---

### Method Details

#### public boolean equals​(
Object
other)

Compares this CRL entry for equality with the given
object. If the

other

object is an

instanceof

X509CRLEntry

, then
its encoded form (the inner SEQUENCE) is retrieved and compared
with the encoded form of this CRL entry.

**Overrides:**
- equals

in class

Object

**Parameters:**
- other

- the object to test for equality with this CRL entry.

**Returns:**
- true iff the encoded forms of the two CRL entries
match, false otherwise.

**See Also:**
- Object.hashCode()

,

HashMap

---

#### public int hashCode()

Returns a hashcode value for this CRL entry from its
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

Returns the ASN.1 DER-encoded form of this CRL Entry,
that is the inner SEQUENCE.

**Returns:**
- the encoded form of this certificate

**Throws:**
- CRLException

- if an encoding error occurs.

---

#### public abstract
BigInteger
getSerialNumber()

Gets the serial number from this X509CRLEntry,
the

userCertificate

.

**Returns:**
- the serial number.

---

#### public
X500Principal
getCertificateIssuer()

Get the issuer of the X509Certificate described by this entry. If
the certificate issuer is also the CRL issuer, this method returns
null.

This method is used with indirect CRLs. The default implementation
always returns null. Subclasses that wish to support indirect CRLs
should override it.

**Returns:**
- the issuer of the X509Certificate described by this entry
or null if it is issued by the CRL issuer.

**Since:**
- 1.5

---

#### public abstract
Date
getRevocationDate()

Gets the revocation date from this X509CRLEntry,
the

revocationDate

.

**Returns:**
- the revocation date.

---

#### public abstract boolean hasExtensions()

Returns true if this CRL entry has extensions.

**Returns:**
- true if this entry has extensions, false otherwise.

---

#### public abstract
String
toString()

Returns a string representation of this CRL entry.

**Overrides:**
- toString

in class

Object

**Returns:**
- a string representation of this CRL entry.

---

#### public
CRLReason
getRevocationReason()

Returns the reason the certificate has been revoked, as specified
in the Reason Code extension of this CRL entry.

**Returns:**
- the reason the certificate has been revoked, or

null

if this CRL entry does not have
a Reason Code extension

**Since:**
- 1.7

---

### Additional Sections

#### Class X509CRLEntry

java.lang.Object

- java.security.cert.X509CRLEntry

java.security.cert.X509CRLEntry

**All Implemented Interfaces:** X509Extension

```java
public abstract class
X509CRLEntry

extends
Object

implements
X509Extension
```

Abstract class for a revoked certificate in a CRL (Certificate
Revocation List).

The ASN.1 definition for

revokedCertificates

is:

```java
revokedCertificates SEQUENCE OF SEQUENCE {
userCertificate CertificateSerialNumber,
revocationDate ChoiceOfTime,
crlEntryExtensions Extensions OPTIONAL
-- if present, must be v2
} OPTIONAL

CertificateSerialNumber ::= INTEGER

Extensions ::= SEQUENCE SIZE (1..MAX) OF Extension

Extension ::= SEQUENCE {
extnId OBJECT IDENTIFIER,
critical BOOLEAN DEFAULT FALSE,
extnValue OCTET STRING
-- contains a DER encoding of a value
-- of the type registered for use with
-- the extnId object identifier value
}
```

**Since:** 1.2
**See Also:** X509CRL

,

X509Extension

public abstract class

X509CRLEntry

extends

Object

implements

X509Extension

Abstract class for a revoked certificate in a CRL (Certificate
Revocation List).

The ASN.1 definition for

revokedCertificates

is:

```java
revokedCertificates SEQUENCE OF SEQUENCE {
userCertificate CertificateSerialNumber,
revocationDate ChoiceOfTime,
crlEntryExtensions Extensions OPTIONAL
-- if present, must be v2
} OPTIONAL

CertificateSerialNumber ::= INTEGER

Extensions ::= SEQUENCE SIZE (1..MAX) OF Extension

Extension ::= SEQUENCE {
extnId OBJECT IDENTIFIER,
critical BOOLEAN DEFAULT FALSE,
extnValue OCTET STRING
-- contains a DER encoding of a value
-- of the type registered for use with
-- the extnId object identifier value
}
```

revokedCertificates SEQUENCE OF SEQUENCE {
userCertificate CertificateSerialNumber,
revocationDate ChoiceOfTime,
crlEntryExtensions Extensions OPTIONAL
-- if present, must be v2
} OPTIONAL

CertificateSerialNumber ::= INTEGER

Extensions ::= SEQUENCE SIZE (1..MAX) OF Extension

Extension ::= SEQUENCE {
extnId OBJECT IDENTIFIER,
critical BOOLEAN DEFAULT FALSE,
extnValue OCTET STRING
-- contains a DER encoding of a value
-- of the type registered for use with
-- the extnId object identifier value
}

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

X509CRLEntry

()

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

Compares this CRL entry for equality with the given
object.

X500Principal

getCertificateIssuer

()

Get the issuer of the X509Certificate described by this entry.

abstract byte[]

getEncoded

()

Returns the ASN.1 DER-encoded form of this CRL Entry,
that is the inner SEQUENCE.

abstract

Date

getRevocationDate

()

Gets the revocation date from this X509CRLEntry,
the

revocationDate

.

CRLReason

getRevocationReason

()

Returns the reason the certificate has been revoked, as specified
in the Reason Code extension of this CRL entry.

abstract

BigInteger

getSerialNumber

()

Gets the serial number from this X509CRLEntry,
the

userCertificate

.

abstract boolean

hasExtensions

()

Returns true if this CRL entry has extensions.

int

hashCode

()

Returns a hashcode value for this CRL entry from its
encoded form.

abstract

String

toString

()

Returns a string representation of this CRL entry.

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

Constructor

Description

X509CRLEntry

()

---

#### Constructor Summary

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

Compares this CRL entry for equality with the given
object.

X500Principal

getCertificateIssuer

()

Get the issuer of the X509Certificate described by this entry.

abstract byte[]

getEncoded

()

Returns the ASN.1 DER-encoded form of this CRL Entry,
that is the inner SEQUENCE.

abstract

Date

getRevocationDate

()

Gets the revocation date from this X509CRLEntry,
the

revocationDate

.

CRLReason

getRevocationReason

()

Returns the reason the certificate has been revoked, as specified
in the Reason Code extension of this CRL entry.

abstract

BigInteger

getSerialNumber

()

Gets the serial number from this X509CRLEntry,
the

userCertificate

.

abstract boolean

hasExtensions

()

Returns true if this CRL entry has extensions.

int

hashCode

()

Returns a hashcode value for this CRL entry from its
encoded form.

abstract

String

toString

()

Returns a string representation of this CRL entry.

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

Compares this CRL entry for equality with the given
object.

Get the issuer of the X509Certificate described by this entry.

Returns the ASN.1 DER-encoded form of this CRL Entry,
that is the inner SEQUENCE.

Gets the revocation date from this X509CRLEntry,
the

revocationDate

.

Returns the reason the certificate has been revoked, as specified
in the Reason Code extension of this CRL entry.

Gets the serial number from this X509CRLEntry,
the

userCertificate

.

Returns true if this CRL entry has extensions.

Returns a hashcode value for this CRL entry from its
encoded form.

Returns a string representation of this CRL entry.

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

- X509CRLEntry

```java
public X509CRLEntry()
```

============ METHOD DETAIL ==========

- Method Detail

- equals

```java
public boolean equals​(
Object
other)
```

Compares this CRL entry for equality with the given
object. If the

other

object is an

instanceof

X509CRLEntry

, then
its encoded form (the inner SEQUENCE) is retrieved and compared
with the encoded form of this CRL entry.

**Overrides:** equals

in class

Object
**Parameters:** other

- the object to test for equality with this CRL entry.
**Returns:** true iff the encoded forms of the two CRL entries
match, false otherwise.
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
public int hashCode()
```

Returns a hashcode value for this CRL entry from its
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

Returns the ASN.1 DER-encoded form of this CRL Entry,
that is the inner SEQUENCE.

**Returns:** the encoded form of this certificate
**Throws:** CRLException

- if an encoding error occurs.

- getSerialNumber

```java
public abstract
BigInteger
getSerialNumber()
```

Gets the serial number from this X509CRLEntry,
the

userCertificate

.

**Returns:** the serial number.

- getCertificateIssuer

```java
public
X500Principal
getCertificateIssuer()
```

Get the issuer of the X509Certificate described by this entry. If
the certificate issuer is also the CRL issuer, this method returns
null.

This method is used with indirect CRLs. The default implementation
always returns null. Subclasses that wish to support indirect CRLs
should override it.

**Returns:** the issuer of the X509Certificate described by this entry
or null if it is issued by the CRL issuer.
**Since:** 1.5

- getRevocationDate

```java
public abstract
Date
getRevocationDate()
```

Gets the revocation date from this X509CRLEntry,
the

revocationDate

.

**Returns:** the revocation date.

- hasExtensions

```java
public abstract boolean hasExtensions()
```

Returns true if this CRL entry has extensions.

**Returns:** true if this entry has extensions, false otherwise.

- toString

```java
public abstract
String
toString()
```

Returns a string representation of this CRL entry.

**Overrides:** toString

in class

Object
**Returns:** a string representation of this CRL entry.

- getRevocationReason

```java
public
CRLReason
getRevocationReason()
```

Returns the reason the certificate has been revoked, as specified
in the Reason Code extension of this CRL entry.

**Returns:** the reason the certificate has been revoked, or

null

if this CRL entry does not have
a Reason Code extension
**Since:** 1.7

Constructor Detail

- X509CRLEntry

```java
public X509CRLEntry()
```

---

#### Constructor Detail

X509CRLEntry

```java
public X509CRLEntry()
```

---

#### X509CRLEntry

public X509CRLEntry()

Method Detail

- equals

```java
public boolean equals​(
Object
other)
```

Compares this CRL entry for equality with the given
object. If the

other

object is an

instanceof

X509CRLEntry

, then
its encoded form (the inner SEQUENCE) is retrieved and compared
with the encoded form of this CRL entry.

**Overrides:** equals

in class

Object
**Parameters:** other

- the object to test for equality with this CRL entry.
**Returns:** true iff the encoded forms of the two CRL entries
match, false otherwise.
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
public int hashCode()
```

Returns a hashcode value for this CRL entry from its
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

Returns the ASN.1 DER-encoded form of this CRL Entry,
that is the inner SEQUENCE.

**Returns:** the encoded form of this certificate
**Throws:** CRLException

- if an encoding error occurs.

- getSerialNumber

```java
public abstract
BigInteger
getSerialNumber()
```

Gets the serial number from this X509CRLEntry,
the

userCertificate

.

**Returns:** the serial number.

- getCertificateIssuer

```java
public
X500Principal
getCertificateIssuer()
```

Get the issuer of the X509Certificate described by this entry. If
the certificate issuer is also the CRL issuer, this method returns
null.

This method is used with indirect CRLs. The default implementation
always returns null. Subclasses that wish to support indirect CRLs
should override it.

**Returns:** the issuer of the X509Certificate described by this entry
or null if it is issued by the CRL issuer.
**Since:** 1.5

- getRevocationDate

```java
public abstract
Date
getRevocationDate()
```

Gets the revocation date from this X509CRLEntry,
the

revocationDate

.

**Returns:** the revocation date.

- hasExtensions

```java
public abstract boolean hasExtensions()
```

Returns true if this CRL entry has extensions.

**Returns:** true if this entry has extensions, false otherwise.

- toString

```java
public abstract
String
toString()
```

Returns a string representation of this CRL entry.

**Overrides:** toString

in class

Object
**Returns:** a string representation of this CRL entry.

- getRevocationReason

```java
public
CRLReason
getRevocationReason()
```

Returns the reason the certificate has been revoked, as specified
in the Reason Code extension of this CRL entry.

**Returns:** the reason the certificate has been revoked, or

null

if this CRL entry does not have
a Reason Code extension
**Since:** 1.7

---

#### Method Detail

equals

```java
public boolean equals​(
Object
other)
```

Compares this CRL entry for equality with the given
object. If the

other

object is an

instanceof

X509CRLEntry

, then
its encoded form (the inner SEQUENCE) is retrieved and compared
with the encoded form of this CRL entry.

**Overrides:** equals

in class

Object
**Parameters:** other

- the object to test for equality with this CRL entry.
**Returns:** true iff the encoded forms of the two CRL entries
match, false otherwise.
**See Also:** Object.hashCode()

,

HashMap

---

#### equals

public boolean equals​(

Object

other)

Compares this CRL entry for equality with the given
object. If the

other

object is an

instanceof

X509CRLEntry

, then
its encoded form (the inner SEQUENCE) is retrieved and compared
with the encoded form of this CRL entry.

hashCode

```java
public int hashCode()
```

Returns a hashcode value for this CRL entry from its
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

Returns a hashcode value for this CRL entry from its
encoded form.

getEncoded

```java
public abstract byte[] getEncoded()
throws
CRLException
```

Returns the ASN.1 DER-encoded form of this CRL Entry,
that is the inner SEQUENCE.

**Returns:** the encoded form of this certificate
**Throws:** CRLException

- if an encoding error occurs.

---

#### getEncoded

public abstract byte[] getEncoded()
throws

CRLException

Returns the ASN.1 DER-encoded form of this CRL Entry,
that is the inner SEQUENCE.

getSerialNumber

```java
public abstract
BigInteger
getSerialNumber()
```

Gets the serial number from this X509CRLEntry,
the

userCertificate

.

**Returns:** the serial number.

---

#### getSerialNumber

public abstract

BigInteger

getSerialNumber()

Gets the serial number from this X509CRLEntry,
the

userCertificate

.

getCertificateIssuer

```java
public
X500Principal
getCertificateIssuer()
```

Get the issuer of the X509Certificate described by this entry. If
the certificate issuer is also the CRL issuer, this method returns
null.

This method is used with indirect CRLs. The default implementation
always returns null. Subclasses that wish to support indirect CRLs
should override it.

**Returns:** the issuer of the X509Certificate described by this entry
or null if it is issued by the CRL issuer.
**Since:** 1.5

---

#### getCertificateIssuer

public

X500Principal

getCertificateIssuer()

Get the issuer of the X509Certificate described by this entry. If
the certificate issuer is also the CRL issuer, this method returns
null.

This method is used with indirect CRLs. The default implementation
always returns null. Subclasses that wish to support indirect CRLs
should override it.

This method is used with indirect CRLs. The default implementation
always returns null. Subclasses that wish to support indirect CRLs
should override it.

getRevocationDate

```java
public abstract
Date
getRevocationDate()
```

Gets the revocation date from this X509CRLEntry,
the

revocationDate

.

**Returns:** the revocation date.

---

#### getRevocationDate

public abstract

Date

getRevocationDate()

Gets the revocation date from this X509CRLEntry,
the

revocationDate

.

hasExtensions

```java
public abstract boolean hasExtensions()
```

Returns true if this CRL entry has extensions.

**Returns:** true if this entry has extensions, false otherwise.

---

#### hasExtensions

public abstract boolean hasExtensions()

Returns true if this CRL entry has extensions.

toString

```java
public abstract
String
toString()
```

Returns a string representation of this CRL entry.

**Overrides:** toString

in class

Object
**Returns:** a string representation of this CRL entry.

---

#### toString

public abstract

String

toString()

Returns a string representation of this CRL entry.

getRevocationReason

```java
public
CRLReason
getRevocationReason()
```

Returns the reason the certificate has been revoked, as specified
in the Reason Code extension of this CRL entry.

**Returns:** the reason the certificate has been revoked, or

null

if this CRL entry does not have
a Reason Code extension
**Since:** 1.7

---

#### getRevocationReason

public

CRLReason

getRevocationReason()

Returns the reason the certificate has been revoked, as specified
in the Reason Code extension of this CRL entry.

---

