# Class X509EncodedKeySpec

**Source:** `java.base\java\security\spec\X509EncodedKeySpec.html`

### Class Description

```java
public class
X509EncodedKeySpec

extends
EncodedKeySpec
```

This class represents the ASN.1 encoding of a public key,
encoded according to the ASN.1 type

SubjectPublicKeyInfo

.
The

SubjectPublicKeyInfo

syntax is defined in the X.509
standard as follows:

```java
SubjectPublicKeyInfo ::= SEQUENCE {
algorithm AlgorithmIdentifier,
subjectPublicKey BIT STRING }
```

**All Implemented Interfaces:** KeySpec

---

### Field Details

*No entries found.*

### Constructor Details

#### public X509EncodedKeySpec​(byte[] encodedKey)

Creates a new

X509EncodedKeySpec

with the given encoded key.

**Parameters:**
- encodedKey

- the key, which is assumed to be
encoded according to the X.509 standard. The contents of the
array are copied to protect against subsequent modification.

**Throws:**
- NullPointerException

- if

encodedKey

is null.

---

#### public X509EncodedKeySpec​(byte[] encodedKey,

String
algorithm)

Creates a new

X509EncodedKeySpec

with the given encoded key.
This constructor is useful when subsequent callers of the

X509EncodedKeySpec

object might not know the algorithm
of the key.

**Parameters:**
- encodedKey

- the key, which is assumed to be
encoded according to the X.509 standard. The contents of the
array are copied to protect against subsequent modification.
- algorithm

- the algorithm name of the encoded public key
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

Returns the key bytes, encoded according to the X.509 standard.

**Overrides:**
- getEncoded

in class

EncodedKeySpec

**Returns:**
- the X.509 encoding of the key. Returns a new array
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

"X.509"

.

---

### Additional Sections

#### Class X509EncodedKeySpec

java.lang.Object

- java.security.spec.EncodedKeySpec
- - java.security.spec.X509EncodedKeySpec

java.security.spec.EncodedKeySpec

- java.security.spec.X509EncodedKeySpec

java.security.spec.X509EncodedKeySpec

**All Implemented Interfaces:** KeySpec

```java
public class
X509EncodedKeySpec

extends
EncodedKeySpec
```

This class represents the ASN.1 encoding of a public key,
encoded according to the ASN.1 type

SubjectPublicKeyInfo

.
The

SubjectPublicKeyInfo

syntax is defined in the X.509
standard as follows:

```java
SubjectPublicKeyInfo ::= SEQUENCE {
algorithm AlgorithmIdentifier,
subjectPublicKey BIT STRING }
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

PKCS8EncodedKeySpec

public class

X509EncodedKeySpec

extends

EncodedKeySpec

This class represents the ASN.1 encoding of a public key,
encoded according to the ASN.1 type

SubjectPublicKeyInfo

.
The

SubjectPublicKeyInfo

syntax is defined in the X.509
standard as follows:

```java
SubjectPublicKeyInfo ::= SEQUENCE {
algorithm AlgorithmIdentifier,
subjectPublicKey BIT STRING }
```

SubjectPublicKeyInfo ::= SEQUENCE {
algorithm AlgorithmIdentifier,
subjectPublicKey BIT STRING }

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

X509EncodedKeySpec

​(byte[] encodedKey)

Creates a new

X509EncodedKeySpec

with the given encoded key.

X509EncodedKeySpec

​(byte[] encodedKey,

String

algorithm)

Creates a new

X509EncodedKeySpec

with the given encoded key.

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

Returns the key bytes, encoded according to the X.509 standard.

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

X509EncodedKeySpec

​(byte[] encodedKey)

Creates a new

X509EncodedKeySpec

with the given encoded key.

X509EncodedKeySpec

​(byte[] encodedKey,

String

algorithm)

Creates a new

X509EncodedKeySpec

with the given encoded key.

---

#### Constructor Summary

Creates a new

X509EncodedKeySpec

with the given encoded key.

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

Returns the key bytes, encoded according to the X.509 standard.

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

Returns the key bytes, encoded according to the X.509 standard.

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

- X509EncodedKeySpec

```java
public X509EncodedKeySpec​(byte[] encodedKey)
```

Creates a new

X509EncodedKeySpec

with the given encoded key.

**Parameters:** encodedKey

- the key, which is assumed to be
encoded according to the X.509 standard. The contents of the
array are copied to protect against subsequent modification.
**Throws:** NullPointerException

- if

encodedKey

is null.

- X509EncodedKeySpec

```java
public X509EncodedKeySpec​(byte[] encodedKey,

String
algorithm)
```

Creates a new

X509EncodedKeySpec

with the given encoded key.
This constructor is useful when subsequent callers of the

X509EncodedKeySpec

object might not know the algorithm
of the key.

**Parameters:** encodedKey

- the key, which is assumed to be
encoded according to the X.509 standard. The contents of the
array are copied to protect against subsequent modification.
**Parameters:** algorithm

- the algorithm name of the encoded public key
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

Returns the key bytes, encoded according to the X.509 standard.

**Overrides:** getEncoded

in class

EncodedKeySpec
**Returns:** the X.509 encoding of the key. Returns a new array
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

"X.509"

.

Constructor Detail

- X509EncodedKeySpec

```java
public X509EncodedKeySpec​(byte[] encodedKey)
```

Creates a new

X509EncodedKeySpec

with the given encoded key.

**Parameters:** encodedKey

- the key, which is assumed to be
encoded according to the X.509 standard. The contents of the
array are copied to protect against subsequent modification.
**Throws:** NullPointerException

- if

encodedKey

is null.

- X509EncodedKeySpec

```java
public X509EncodedKeySpec​(byte[] encodedKey,

String
algorithm)
```

Creates a new

X509EncodedKeySpec

with the given encoded key.
This constructor is useful when subsequent callers of the

X509EncodedKeySpec

object might not know the algorithm
of the key.

**Parameters:** encodedKey

- the key, which is assumed to be
encoded according to the X.509 standard. The contents of the
array are copied to protect against subsequent modification.
**Parameters:** algorithm

- the algorithm name of the encoded public key
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

X509EncodedKeySpec

```java
public X509EncodedKeySpec​(byte[] encodedKey)
```

Creates a new

X509EncodedKeySpec

with the given encoded key.

**Parameters:** encodedKey

- the key, which is assumed to be
encoded according to the X.509 standard. The contents of the
array are copied to protect against subsequent modification.
**Throws:** NullPointerException

- if

encodedKey

is null.

---

#### X509EncodedKeySpec

public X509EncodedKeySpec​(byte[] encodedKey)

Creates a new

X509EncodedKeySpec

with the given encoded key.

X509EncodedKeySpec

```java
public X509EncodedKeySpec​(byte[] encodedKey,

String
algorithm)
```

Creates a new

X509EncodedKeySpec

with the given encoded key.
This constructor is useful when subsequent callers of the

X509EncodedKeySpec

object might not know the algorithm
of the key.

**Parameters:** encodedKey

- the key, which is assumed to be
encoded according to the X.509 standard. The contents of the
array are copied to protect against subsequent modification.
**Parameters:** algorithm

- the algorithm name of the encoded public key
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

#### X509EncodedKeySpec

public X509EncodedKeySpec​(byte[] encodedKey,

String

algorithm)

Creates a new

X509EncodedKeySpec

with the given encoded key.
This constructor is useful when subsequent callers of the

X509EncodedKeySpec

object might not know the algorithm
of the key.

Method Detail

- getEncoded

```java
public byte[] getEncoded()
```

Returns the key bytes, encoded according to the X.509 standard.

**Overrides:** getEncoded

in class

EncodedKeySpec
**Returns:** the X.509 encoding of the key. Returns a new array
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

"X.509"

.

---

#### Method Detail

getEncoded

```java
public byte[] getEncoded()
```

Returns the key bytes, encoded according to the X.509 standard.

**Overrides:** getEncoded

in class

EncodedKeySpec
**Returns:** the X.509 encoding of the key. Returns a new array
each time this method is called.

---

#### getEncoded

public byte[] getEncoded()

Returns the key bytes, encoded according to the X.509 standard.

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

"X.509"

.

---

#### getFormat

public final

String

getFormat()

Returns the name of the encoding format associated with this
key specification.

---

