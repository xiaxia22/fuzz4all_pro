# Class PKCS8EncodedKeySpec

**Source:** `java.base\java\security\spec\PKCS8EncodedKeySpec.html`

### Class Description

```java
public class
PKCS8EncodedKeySpec

extends
EncodedKeySpec
```

This class represents the ASN.1 encoding of a private key,
encoded according to the ASN.1 type

PrivateKeyInfo

.
The

PrivateKeyInfo

syntax is defined in the PKCS#8 standard
as follows:

```java
PrivateKeyInfo ::= SEQUENCE {
version Version,
privateKeyAlgorithm PrivateKeyAlgorithmIdentifier,
privateKey PrivateKey,
attributes [0] IMPLICIT Attributes OPTIONAL }

Version ::= INTEGER

PrivateKeyAlgorithmIdentifier ::= AlgorithmIdentifier

PrivateKey ::= OCTET STRING

Attributes ::= SET OF Attribute
```

**All Implemented Interfaces:** KeySpec

---

### Field Details

*No entries found.*

### Constructor Details

#### public PKCS8EncodedKeySpec​(byte[] encodedKey)

Creates a new

PKCS8EncodedKeySpec

with the given encoded key.

**Parameters:**
- encodedKey

- the key, which is assumed to be
encoded according to the PKCS #8 standard. The contents of
the array are copied to protect against subsequent modification.

**Throws:**
- NullPointerException

- if

encodedKey

is null.

---

#### public PKCS8EncodedKeySpec​(byte[] encodedKey,

String
algorithm)

Creates a new

PKCS8EncodedKeySpec

with the given encoded key and
algorithm. This constructor is useful when subsequent callers of
the

PKCS8EncodedKeySpec

object might not know the
algorithm of the private key.

**Parameters:**
- encodedKey

- the key, which is assumed to be
encoded according to the PKCS #8 standard. The contents of
the array are copied to protect against subsequent modification.
- algorithm

- the algorithm name of the encoded private key
See the KeyFactory section in the

Java Security Standard Algorithm Names Specification

for information about standard algorithm names.

**Throws:**
- NullPointerException

- if

encodedKey

or

algorithm

is null.
- IllegalArgumentException

- if

algorithm

is
the empty string

""

**Since:**
- 9

---

### Method Details

#### public byte[] getEncoded()

Returns the key bytes, encoded according to the PKCS #8 standard.

**Overrides:**
- getEncoded

in class

EncodedKeySpec

**Returns:**
- the PKCS #8 encoding of the key. Returns a new array
each time this method is called.

---

#### public final
String
getFormat()

Returns the name of the encoding format associated with this
key specification.

**Specified by:**
- getFormat

in class

EncodedKeySpec

**Returns:**
- the string

"PKCS#8"

.

---

### Additional Sections

#### Class PKCS8EncodedKeySpec

java.lang.Object

- java.security.spec.EncodedKeySpec
- - java.security.spec.PKCS8EncodedKeySpec

java.security.spec.EncodedKeySpec

- java.security.spec.PKCS8EncodedKeySpec

java.security.spec.PKCS8EncodedKeySpec

**All Implemented Interfaces:** KeySpec

```java
public class
PKCS8EncodedKeySpec

extends
EncodedKeySpec
```

This class represents the ASN.1 encoding of a private key,
encoded according to the ASN.1 type

PrivateKeyInfo

.
The

PrivateKeyInfo

syntax is defined in the PKCS#8 standard
as follows:

```java
PrivateKeyInfo ::= SEQUENCE {
version Version,
privateKeyAlgorithm PrivateKeyAlgorithmIdentifier,
privateKey PrivateKey,
attributes [0] IMPLICIT Attributes OPTIONAL }

Version ::= INTEGER

PrivateKeyAlgorithmIdentifier ::= AlgorithmIdentifier

PrivateKey ::= OCTET STRING

Attributes ::= SET OF Attribute
```

**Since:** 1.2
**See Also:** Key

,

KeyFactory

,

KeySpec

,

EncodedKeySpec

,

X509EncodedKeySpec

public class

PKCS8EncodedKeySpec

extends

EncodedKeySpec

This class represents the ASN.1 encoding of a private key,
encoded according to the ASN.1 type

PrivateKeyInfo

.
The

PrivateKeyInfo

syntax is defined in the PKCS#8 standard
as follows:

```java
PrivateKeyInfo ::= SEQUENCE {
version Version,
privateKeyAlgorithm PrivateKeyAlgorithmIdentifier,
privateKey PrivateKey,
attributes [0] IMPLICIT Attributes OPTIONAL }

Version ::= INTEGER

PrivateKeyAlgorithmIdentifier ::= AlgorithmIdentifier

PrivateKey ::= OCTET STRING

Attributes ::= SET OF Attribute
```

PrivateKeyInfo ::= SEQUENCE {
version Version,
privateKeyAlgorithm PrivateKeyAlgorithmIdentifier,
privateKey PrivateKey,
attributes [0] IMPLICIT Attributes OPTIONAL }

Version ::= INTEGER

PrivateKeyAlgorithmIdentifier ::= AlgorithmIdentifier

PrivateKey ::= OCTET STRING

Attributes ::= SET OF Attribute

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

PKCS8EncodedKeySpec

​(byte[] encodedKey)

Creates a new

PKCS8EncodedKeySpec

with the given encoded key.

PKCS8EncodedKeySpec

​(byte[] encodedKey,

String

algorithm)

Creates a new

PKCS8EncodedKeySpec

with the given encoded key and
algorithm.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

byte[]

getEncoded

()

Returns the key bytes, encoded according to the PKCS #8 standard.

String

getFormat

()

Returns the name of the encoding format associated with this
key specification.

- Methods declared in class java.security.spec.

EncodedKeySpec

getAlgorithm

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

PKCS8EncodedKeySpec

​(byte[] encodedKey)

Creates a new

PKCS8EncodedKeySpec

with the given encoded key.

PKCS8EncodedKeySpec

​(byte[] encodedKey,

String

algorithm)

Creates a new

PKCS8EncodedKeySpec

with the given encoded key and
algorithm.

---

#### Constructor Summary

Creates a new

PKCS8EncodedKeySpec

with the given encoded key.

Creates a new

PKCS8EncodedKeySpec

with the given encoded key and
algorithm.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

byte[]

getEncoded

()

Returns the key bytes, encoded according to the PKCS #8 standard.

String

getFormat

()

Returns the name of the encoding format associated with this
key specification.

- Methods declared in class java.security.spec.

EncodedKeySpec

getAlgorithm

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

Returns the key bytes, encoded according to the PKCS #8 standard.

Returns the name of the encoding format associated with this
key specification.

Methods declared in class java.security.spec.

EncodedKeySpec

getAlgorithm

---

#### Methods declared in class java.security.spec. EncodedKeySpec

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

- PKCS8EncodedKeySpec

```java
public PKCS8EncodedKeySpec​(byte[] encodedKey)
```

Creates a new

PKCS8EncodedKeySpec

with the given encoded key.

**Parameters:** encodedKey

- the key, which is assumed to be
encoded according to the PKCS #8 standard. The contents of
the array are copied to protect against subsequent modification.
**Throws:** NullPointerException

- if

encodedKey

is null.

- PKCS8EncodedKeySpec

```java
public PKCS8EncodedKeySpec​(byte[] encodedKey,

String
algorithm)
```

Creates a new

PKCS8EncodedKeySpec

with the given encoded key and
algorithm. This constructor is useful when subsequent callers of
the

PKCS8EncodedKeySpec

object might not know the
algorithm of the private key.

**Parameters:** encodedKey

- the key, which is assumed to be
encoded according to the PKCS #8 standard. The contents of
the array are copied to protect against subsequent modification.
**Parameters:** algorithm

- the algorithm name of the encoded private key
See the KeyFactory section in the

Java Security Standard Algorithm Names Specification

for information about standard algorithm names.
**Throws:** NullPointerException

- if

encodedKey

or

algorithm

is null.
**Throws:** IllegalArgumentException

- if

algorithm

is
the empty string

""
**Since:** 9

============ METHOD DETAIL ==========

- Method Detail

- getEncoded

```java
public byte[] getEncoded()
```

Returns the key bytes, encoded according to the PKCS #8 standard.

**Overrides:** getEncoded

in class

EncodedKeySpec
**Returns:** the PKCS #8 encoding of the key. Returns a new array
each time this method is called.

- getFormat

```java
public final
String
getFormat()
```

Returns the name of the encoding format associated with this
key specification.

**Specified by:** getFormat

in class

EncodedKeySpec
**Returns:** the string

"PKCS#8"

.

Constructor Detail

- PKCS8EncodedKeySpec

```java
public PKCS8EncodedKeySpec​(byte[] encodedKey)
```

Creates a new

PKCS8EncodedKeySpec

with the given encoded key.

**Parameters:** encodedKey

- the key, which is assumed to be
encoded according to the PKCS #8 standard. The contents of
the array are copied to protect against subsequent modification.
**Throws:** NullPointerException

- if

encodedKey

is null.

- PKCS8EncodedKeySpec

```java
public PKCS8EncodedKeySpec​(byte[] encodedKey,

String
algorithm)
```

Creates a new

PKCS8EncodedKeySpec

with the given encoded key and
algorithm. This constructor is useful when subsequent callers of
the

PKCS8EncodedKeySpec

object might not know the
algorithm of the private key.

**Parameters:** encodedKey

- the key, which is assumed to be
encoded according to the PKCS #8 standard. The contents of
the array are copied to protect against subsequent modification.
**Parameters:** algorithm

- the algorithm name of the encoded private key
See the KeyFactory section in the

Java Security Standard Algorithm Names Specification

for information about standard algorithm names.
**Throws:** NullPointerException

- if

encodedKey

or

algorithm

is null.
**Throws:** IllegalArgumentException

- if

algorithm

is
the empty string

""
**Since:** 9

---

#### Constructor Detail

PKCS8EncodedKeySpec

```java
public PKCS8EncodedKeySpec​(byte[] encodedKey)
```

Creates a new

PKCS8EncodedKeySpec

with the given encoded key.

**Parameters:** encodedKey

- the key, which is assumed to be
encoded according to the PKCS #8 standard. The contents of
the array are copied to protect against subsequent modification.
**Throws:** NullPointerException

- if

encodedKey

is null.

---

#### PKCS8EncodedKeySpec

public PKCS8EncodedKeySpec​(byte[] encodedKey)

Creates a new

PKCS8EncodedKeySpec

with the given encoded key.

PKCS8EncodedKeySpec

```java
public PKCS8EncodedKeySpec​(byte[] encodedKey,

String
algorithm)
```

Creates a new

PKCS8EncodedKeySpec

with the given encoded key and
algorithm. This constructor is useful when subsequent callers of
the

PKCS8EncodedKeySpec

object might not know the
algorithm of the private key.

**Parameters:** encodedKey

- the key, which is assumed to be
encoded according to the PKCS #8 standard. The contents of
the array are copied to protect against subsequent modification.
**Parameters:** algorithm

- the algorithm name of the encoded private key
See the KeyFactory section in the

Java Security Standard Algorithm Names Specification

for information about standard algorithm names.
**Throws:** NullPointerException

- if

encodedKey

or

algorithm

is null.
**Throws:** IllegalArgumentException

- if

algorithm

is
the empty string

""
**Since:** 9

---

#### PKCS8EncodedKeySpec

public PKCS8EncodedKeySpec​(byte[] encodedKey,

String

algorithm)

Creates a new

PKCS8EncodedKeySpec

with the given encoded key and
algorithm. This constructor is useful when subsequent callers of
the

PKCS8EncodedKeySpec

object might not know the
algorithm of the private key.

Method Detail

- getEncoded

```java
public byte[] getEncoded()
```

Returns the key bytes, encoded according to the PKCS #8 standard.

**Overrides:** getEncoded

in class

EncodedKeySpec
**Returns:** the PKCS #8 encoding of the key. Returns a new array
each time this method is called.

- getFormat

```java
public final
String
getFormat()
```

Returns the name of the encoding format associated with this
key specification.

**Specified by:** getFormat

in class

EncodedKeySpec
**Returns:** the string

"PKCS#8"

.

---

#### Method Detail

getEncoded

```java
public byte[] getEncoded()
```

Returns the key bytes, encoded according to the PKCS #8 standard.

**Overrides:** getEncoded

in class

EncodedKeySpec
**Returns:** the PKCS #8 encoding of the key. Returns a new array
each time this method is called.

---

#### getEncoded

public byte[] getEncoded()

Returns the key bytes, encoded according to the PKCS #8 standard.

getFormat

```java
public final
String
getFormat()
```

Returns the name of the encoding format associated with this
key specification.

**Specified by:** getFormat

in class

EncodedKeySpec
**Returns:** the string

"PKCS#8"

.

---

#### getFormat

public final

String

getFormat()

Returns the name of the encoding format associated with this
key specification.

---

