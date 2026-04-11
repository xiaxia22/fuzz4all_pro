# Interface Key

**Source:** `java.base\java\security\Key.html`

### Class Description

```java
public interface
Key

extends
Serializable
```

The Key interface is the top-level interface for all keys. It
defines the functionality shared by all key objects. All keys
have three characteristics:

- An Algorithm

This is the key algorithm for that key. The key algorithm is usually
an encryption or asymmetric operation algorithm (such as DSA or
RSA), which will work with those algorithms and with related
algorithms (such as MD5 with RSA, SHA-1 with RSA, Raw DSA, etc.)
The name of the algorithm of a key is obtained using the

getAlgorithm

method.

An Encoded Form

This is an external encoded form for the key used when a standard
representation of the key is needed outside the Java Virtual Machine,
as when transmitting the key to some other party. The key
is encoded according to a standard format (such as
X.509

SubjectPublicKeyInfo

or PKCS#8), and
is returned using the

getEncoded

method.
Note: The syntax of the ASN.1 type

SubjectPublicKeyInfo

is defined as follows:

```java
SubjectPublicKeyInfo ::= SEQUENCE {
algorithm AlgorithmIdentifier,
subjectPublicKey BIT STRING }

AlgorithmIdentifier ::= SEQUENCE {
algorithm OBJECT IDENTIFIER,
parameters ANY DEFINED BY algorithm OPTIONAL }
```

For more information, see

RFC 5280:
Internet X.509 Public Key Infrastructure Certificate and CRL Profile

.

A Format

This is the name of the format of the encoded key. It is returned
by the

getFormat

method.

Keys are generally obtained through key generators, certificates,
or various Identity classes used to manage keys.
Keys may also be obtained from key specifications (transparent
representations of the underlying key material) through the use of a key
factory (see

KeyFactory

).

A Key should use KeyRep as its serialized representation.
Note that a serialized Key may contain sensitive information
which should not be exposed in untrusted environments. See the

Security Appendix

of the Serialization Specification for more information.

**All Superinterfaces:** Serializable

---

### Field Details

#### static final long serialVersionUID

The class fingerprint that is set to indicate
serialization compatibility with a previous
version of the class.

**See Also:**
- Constant Field Values

---

### Constructor Details

*No entries found.*

### Method Details

#### String
getAlgorithm()

Returns the standard algorithm name for this key. For
example, "DSA" would indicate that this key is a DSA key.
See the

Java Security Standard Algorithm Names

document
for more information.

**Returns:**
- the name of the algorithm associated with this key.

---

#### String
getFormat()

Returns the name of the primary encoding format of this key,
or null if this key does not support encoding.
The primary encoding format is
named in terms of the appropriate ASN.1 data format, if an
ASN.1 specification for this key exists.
For example, the name of the ASN.1 data format for public
keys is

SubjectPublicKeyInfo

, as
defined by the X.509 standard; in this case, the returned format is

"X.509"

. Similarly,
the name of the ASN.1 data format for private keys is

PrivateKeyInfo

,
as defined by the PKCS #8 standard; in this case, the returned format is

"PKCS#8"

.

**Returns:**
- the primary encoding format of the key.

---

#### byte[] getEncoded()

Returns the key in its primary encoding format, or null
if this key does not support encoding.

**Returns:**
- the encoded key, or null if the key does not support
encoding.

---

### Additional Sections

#### Interface Key

**All Superinterfaces:** Serializable

**All Known Subinterfaces:** DHPrivateKey

,

DHPublicKey

,

DSAPrivateKey

,

DSAPublicKey

,

ECPrivateKey

,

ECPublicKey

,

PBEKey

,

PrivateKey

,

PublicKey

,

RSAMultiPrimePrivateCrtKey

,

RSAPrivateCrtKey

,

RSAPrivateKey

,

RSAPublicKey

,

SecretKey

,

XECPrivateKey

,

XECPublicKey

**All Known Implementing Classes:** EncryptionKey

,

KerberosKey

,

SecretKeySpec

```java
public interface
Key

extends
Serializable
```

The Key interface is the top-level interface for all keys. It
defines the functionality shared by all key objects. All keys
have three characteristics:

- An Algorithm

This is the key algorithm for that key. The key algorithm is usually
an encryption or asymmetric operation algorithm (such as DSA or
RSA), which will work with those algorithms and with related
algorithms (such as MD5 with RSA, SHA-1 with RSA, Raw DSA, etc.)
The name of the algorithm of a key is obtained using the

getAlgorithm

method.

An Encoded Form

This is an external encoded form for the key used when a standard
representation of the key is needed outside the Java Virtual Machine,
as when transmitting the key to some other party. The key
is encoded according to a standard format (such as
X.509

SubjectPublicKeyInfo

or PKCS#8), and
is returned using the

getEncoded

method.
Note: The syntax of the ASN.1 type

SubjectPublicKeyInfo

is defined as follows:

```java
SubjectPublicKeyInfo ::= SEQUENCE {
algorithm AlgorithmIdentifier,
subjectPublicKey BIT STRING }

AlgorithmIdentifier ::= SEQUENCE {
algorithm OBJECT IDENTIFIER,
parameters ANY DEFINED BY algorithm OPTIONAL }
```

For more information, see

RFC 5280:
Internet X.509 Public Key Infrastructure Certificate and CRL Profile

.

A Format

This is the name of the format of the encoded key. It is returned
by the

getFormat

method.

Keys are generally obtained through key generators, certificates,
or various Identity classes used to manage keys.
Keys may also be obtained from key specifications (transparent
representations of the underlying key material) through the use of a key
factory (see

KeyFactory

).

A Key should use KeyRep as its serialized representation.
Note that a serialized Key may contain sensitive information
which should not be exposed in untrusted environments. See the

Security Appendix

of the Serialization Specification for more information.

**Since:** 1.1
**See Also:** PublicKey

,

PrivateKey

,

KeyPair

,

KeyPairGenerator

,

KeyFactory

,

KeyRep

,

KeySpec

,

Identity

,

Signer

public interface

Key

extends

Serializable

The Key interface is the top-level interface for all keys. It
defines the functionality shared by all key objects. All keys
have three characteristics:

- An Algorithm

This is the key algorithm for that key. The key algorithm is usually
an encryption or asymmetric operation algorithm (such as DSA or
RSA), which will work with those algorithms and with related
algorithms (such as MD5 with RSA, SHA-1 with RSA, Raw DSA, etc.)
The name of the algorithm of a key is obtained using the

getAlgorithm

method.

An Encoded Form

This is an external encoded form for the key used when a standard
representation of the key is needed outside the Java Virtual Machine,
as when transmitting the key to some other party. The key
is encoded according to a standard format (such as
X.509

SubjectPublicKeyInfo

or PKCS#8), and
is returned using the

getEncoded

method.
Note: The syntax of the ASN.1 type

SubjectPublicKeyInfo

is defined as follows:

```java
SubjectPublicKeyInfo ::= SEQUENCE {
algorithm AlgorithmIdentifier,
subjectPublicKey BIT STRING }

AlgorithmIdentifier ::= SEQUENCE {
algorithm OBJECT IDENTIFIER,
parameters ANY DEFINED BY algorithm OPTIONAL }
```

For more information, see

RFC 5280:
Internet X.509 Public Key Infrastructure Certificate and CRL Profile

.

A Format

This is the name of the format of the encoded key. It is returned
by the

getFormat

method.

Keys are generally obtained through key generators, certificates,
or various Identity classes used to manage keys.
Keys may also be obtained from key specifications (transparent
representations of the underlying key material) through the use of a key
factory (see

KeyFactory

).

A Key should use KeyRep as its serialized representation.
Note that a serialized Key may contain sensitive information
which should not be exposed in untrusted environments. See the

Security Appendix

of the Serialization Specification for more information.

An Algorithm

This is the key algorithm for that key. The key algorithm is usually
an encryption or asymmetric operation algorithm (such as DSA or
RSA), which will work with those algorithms and with related
algorithms (such as MD5 with RSA, SHA-1 with RSA, Raw DSA, etc.)
The name of the algorithm of a key is obtained using the

getAlgorithm

method.

An Encoded Form

This is an external encoded form for the key used when a standard
representation of the key is needed outside the Java Virtual Machine,
as when transmitting the key to some other party. The key
is encoded according to a standard format (such as
X.509

SubjectPublicKeyInfo

or PKCS#8), and
is returned using the

getEncoded

method.
Note: The syntax of the ASN.1 type

SubjectPublicKeyInfo

is defined as follows:

```java
SubjectPublicKeyInfo ::= SEQUENCE {
algorithm AlgorithmIdentifier,
subjectPublicKey BIT STRING }

AlgorithmIdentifier ::= SEQUENCE {
algorithm OBJECT IDENTIFIER,
parameters ANY DEFINED BY algorithm OPTIONAL }
```

For more information, see

RFC 5280:
Internet X.509 Public Key Infrastructure Certificate and CRL Profile

.

A Format

This is the name of the format of the encoded key. It is returned
by the

getFormat

method.

This is the key algorithm for that key. The key algorithm is usually
an encryption or asymmetric operation algorithm (such as DSA or
RSA), which will work with those algorithms and with related
algorithms (such as MD5 with RSA, SHA-1 with RSA, Raw DSA, etc.)
The name of the algorithm of a key is obtained using the

getAlgorithm

method.

An Encoded Form

This is an external encoded form for the key used when a standard
representation of the key is needed outside the Java Virtual Machine,
as when transmitting the key to some other party. The key
is encoded according to a standard format (such as
X.509

SubjectPublicKeyInfo

or PKCS#8), and
is returned using the

getEncoded

method.
Note: The syntax of the ASN.1 type

SubjectPublicKeyInfo

is defined as follows:

```java
SubjectPublicKeyInfo ::= SEQUENCE {
algorithm AlgorithmIdentifier,
subjectPublicKey BIT STRING }

AlgorithmIdentifier ::= SEQUENCE {
algorithm OBJECT IDENTIFIER,
parameters ANY DEFINED BY algorithm OPTIONAL }
```

For more information, see

RFC 5280:
Internet X.509 Public Key Infrastructure Certificate and CRL Profile

.

A Format

This is the name of the format of the encoded key. It is returned
by the

getFormat

method.

This is an external encoded form for the key used when a standard
representation of the key is needed outside the Java Virtual Machine,
as when transmitting the key to some other party. The key
is encoded according to a standard format (such as
X.509

SubjectPublicKeyInfo

or PKCS#8), and
is returned using the

getEncoded

method.
Note: The syntax of the ASN.1 type

SubjectPublicKeyInfo

is defined as follows:

```java
SubjectPublicKeyInfo ::= SEQUENCE {
algorithm AlgorithmIdentifier,
subjectPublicKey BIT STRING }

AlgorithmIdentifier ::= SEQUENCE {
algorithm OBJECT IDENTIFIER,
parameters ANY DEFINED BY algorithm OPTIONAL }
```

For more information, see

RFC 5280:
Internet X.509 Public Key Infrastructure Certificate and CRL Profile

.

A Format

This is the name of the format of the encoded key. It is returned
by the

getFormat

method.

SubjectPublicKeyInfo ::= SEQUENCE {
algorithm AlgorithmIdentifier,
subjectPublicKey BIT STRING }

AlgorithmIdentifier ::= SEQUENCE {
algorithm OBJECT IDENTIFIER,
parameters ANY DEFINED BY algorithm OPTIONAL }

This is the name of the format of the encoded key. It is returned
by the

getFormat

method.

A Key should use KeyRep as its serialized representation.
Note that a serialized Key may contain sensitive information
which should not be exposed in untrusted environments. See the

Security Appendix

of the Serialization Specification for more information.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static long

serialVersionUID

The class fingerprint that is set to indicate
serialization compatibility with a previous
version of the class.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

String

getAlgorithm

()

Returns the standard algorithm name for this key.

byte[]

getEncoded

()

Returns the key in its primary encoding format, or null
if this key does not support encoding.

String

getFormat

()

Returns the name of the primary encoding format of this key,
or null if this key does not support encoding.

Field Summary

Fields

Modifier and Type

Field

Description

static long

serialVersionUID

The class fingerprint that is set to indicate
serialization compatibility with a previous
version of the class.

---

#### Field Summary

The class fingerprint that is set to indicate
serialization compatibility with a previous
version of the class.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

String

getAlgorithm

()

Returns the standard algorithm name for this key.

byte[]

getEncoded

()

Returns the key in its primary encoding format, or null
if this key does not support encoding.

String

getFormat

()

Returns the name of the primary encoding format of this key,
or null if this key does not support encoding.

---

#### Method Summary

Returns the standard algorithm name for this key.

Returns the key in its primary encoding format, or null
if this key does not support encoding.

Returns the name of the primary encoding format of this key,
or null if this key does not support encoding.

============ FIELD DETAIL ===========

- Field Detail

- serialVersionUID

```java
static final long serialVersionUID
```

The class fingerprint that is set to indicate
serialization compatibility with a previous
version of the class.

**See Also:** Constant Field Values

============ METHOD DETAIL ==========

- Method Detail

- getAlgorithm

```java
String
getAlgorithm()
```

Returns the standard algorithm name for this key. For
example, "DSA" would indicate that this key is a DSA key.
See the

Java Security Standard Algorithm Names

document
for more information.

**Returns:** the name of the algorithm associated with this key.

- getFormat

```java
String
getFormat()
```

Returns the name of the primary encoding format of this key,
or null if this key does not support encoding.
The primary encoding format is
named in terms of the appropriate ASN.1 data format, if an
ASN.1 specification for this key exists.
For example, the name of the ASN.1 data format for public
keys is

SubjectPublicKeyInfo

, as
defined by the X.509 standard; in this case, the returned format is

"X.509"

. Similarly,
the name of the ASN.1 data format for private keys is

PrivateKeyInfo

,
as defined by the PKCS #8 standard; in this case, the returned format is

"PKCS#8"

.

**Returns:** the primary encoding format of the key.

- getEncoded

```java
byte[] getEncoded()
```

Returns the key in its primary encoding format, or null
if this key does not support encoding.

**Returns:** the encoded key, or null if the key does not support
encoding.

Field Detail

- serialVersionUID

```java
static final long serialVersionUID
```

The class fingerprint that is set to indicate
serialization compatibility with a previous
version of the class.

**See Also:** Constant Field Values

---

#### Field Detail

serialVersionUID

```java
static final long serialVersionUID
```

The class fingerprint that is set to indicate
serialization compatibility with a previous
version of the class.

**See Also:** Constant Field Values

---

#### serialVersionUID

static final long serialVersionUID

The class fingerprint that is set to indicate
serialization compatibility with a previous
version of the class.

Method Detail

- getAlgorithm

```java
String
getAlgorithm()
```

Returns the standard algorithm name for this key. For
example, "DSA" would indicate that this key is a DSA key.
See the

Java Security Standard Algorithm Names

document
for more information.

**Returns:** the name of the algorithm associated with this key.

- getFormat

```java
String
getFormat()
```

Returns the name of the primary encoding format of this key,
or null if this key does not support encoding.
The primary encoding format is
named in terms of the appropriate ASN.1 data format, if an
ASN.1 specification for this key exists.
For example, the name of the ASN.1 data format for public
keys is

SubjectPublicKeyInfo

, as
defined by the X.509 standard; in this case, the returned format is

"X.509"

. Similarly,
the name of the ASN.1 data format for private keys is

PrivateKeyInfo

,
as defined by the PKCS #8 standard; in this case, the returned format is

"PKCS#8"

.

**Returns:** the primary encoding format of the key.

- getEncoded

```java
byte[] getEncoded()
```

Returns the key in its primary encoding format, or null
if this key does not support encoding.

**Returns:** the encoded key, or null if the key does not support
encoding.

---

#### Method Detail

getAlgorithm

```java
String
getAlgorithm()
```

Returns the standard algorithm name for this key. For
example, "DSA" would indicate that this key is a DSA key.
See the

Java Security Standard Algorithm Names

document
for more information.

**Returns:** the name of the algorithm associated with this key.

---

#### getAlgorithm

String

getAlgorithm()

Returns the standard algorithm name for this key. For
example, "DSA" would indicate that this key is a DSA key.
See the

Java Security Standard Algorithm Names

document
for more information.

getFormat

```java
String
getFormat()
```

Returns the name of the primary encoding format of this key,
or null if this key does not support encoding.
The primary encoding format is
named in terms of the appropriate ASN.1 data format, if an
ASN.1 specification for this key exists.
For example, the name of the ASN.1 data format for public
keys is

SubjectPublicKeyInfo

, as
defined by the X.509 standard; in this case, the returned format is

"X.509"

. Similarly,
the name of the ASN.1 data format for private keys is

PrivateKeyInfo

,
as defined by the PKCS #8 standard; in this case, the returned format is

"PKCS#8"

.

**Returns:** the primary encoding format of the key.

---

#### getFormat

String

getFormat()

Returns the name of the primary encoding format of this key,
or null if this key does not support encoding.
The primary encoding format is
named in terms of the appropriate ASN.1 data format, if an
ASN.1 specification for this key exists.
For example, the name of the ASN.1 data format for public
keys is

SubjectPublicKeyInfo

, as
defined by the X.509 standard; in this case, the returned format is

"X.509"

. Similarly,
the name of the ASN.1 data format for private keys is

PrivateKeyInfo

,
as defined by the PKCS #8 standard; in this case, the returned format is

"PKCS#8"

.

getEncoded

```java
byte[] getEncoded()
```

Returns the key in its primary encoding format, or null
if this key does not support encoding.

**Returns:** the encoded key, or null if the key does not support
encoding.

---

#### getEncoded

byte[] getEncoded()

Returns the key in its primary encoding format, or null
if this key does not support encoding.

---

