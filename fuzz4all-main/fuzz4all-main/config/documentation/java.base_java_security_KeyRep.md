# Class KeyRep

**Source:** `java.base\java\security\KeyRep.html`

### Class Description

```java
public class
KeyRep

extends
Object

implements
Serializable
```

Standardized representation for serialized Key objects.

Note that a serialized Key may contain sensitive information
which should not be exposed in untrusted environments. See the

Security Appendix

of the Serialization Specification for more information.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public KeyRep​(
KeyRep.Type
type,

String
algorithm,

String
format,
byte[] encoded)

Construct the alternate Key class.

**Parameters:**
- type

- either one of Type.SECRET, Type.PUBLIC, or Type.PRIVATE
- algorithm

- the algorithm returned from

Key.getAlgorithm()
- format

- the encoding format returned from

Key.getFormat()
- encoded

- the encoded bytes returned from

Key.getEncoded()

**Throws:**
- NullPointerException

- if type is

null

,
if algorithm is

null

,
if format is

null

,
or if encoded is

null

---

### Method Details

#### protected
Object
readResolve()
throws
ObjectStreamException

Resolve the Key object.

This method supports three Type/format combinations:

- Type.SECRET/"RAW" - returns a SecretKeySpec object
constructed using encoded key bytes and algorithm

Type.PUBLIC/"X.509" - gets a KeyFactory instance for
the key algorithm, constructs an X509EncodedKeySpec with the
encoded key bytes, and generates a public key from the spec

Type.PRIVATE/"PKCS#8" - gets a KeyFactory instance for
the key algorithm, constructs a PKCS8EncodedKeySpec with the
encoded key bytes, and generates a private key from the spec

**Returns:**
- the resolved Key object

**Throws:**
- ObjectStreamException

- if the Type/format
combination is unrecognized, if the algorithm, key format, or
encoded key bytes are unrecognized/invalid, of if the
resolution of the key fails for any reason

---

### Additional Sections

#### Class KeyRep

java.lang.Object

- java.security.KeyRep

java.security.KeyRep

**All Implemented Interfaces:** Serializable

```java
public class
KeyRep

extends
Object

implements
Serializable
```

Standardized representation for serialized Key objects.

Note that a serialized Key may contain sensitive information
which should not be exposed in untrusted environments. See the

Security Appendix

of the Serialization Specification for more information.

**Since:** 1.5
**See Also:** Key

,

KeyFactory

,

SecretKeySpec

,

X509EncodedKeySpec

,

PKCS8EncodedKeySpec

,

Serialized Form

public class

KeyRep

extends

Object

implements

Serializable

Standardized representation for serialized Key objects.

Note that a serialized Key may contain sensitive information
which should not be exposed in untrusted environments. See the

Security Appendix

of the Serialization Specification for more information.

Note that a serialized Key may contain sensitive information
which should not be exposed in untrusted environments. See the

Security Appendix

of the Serialization Specification for more information.

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

static class

KeyRep.Type

Key type.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

KeyRep

​(

KeyRep.Type

type,

String

algorithm,

String

format,
byte[] encoded)

Construct the alternate Key class.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

protected

Object

readResolve

()

Resolve the Key object.

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

Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

static class

KeyRep.Type

Key type.

---

#### Nested Class Summary

Key type.

Constructor Summary

Constructors

Constructor

Description

KeyRep

​(

KeyRep.Type

type,

String

algorithm,

String

format,
byte[] encoded)

Construct the alternate Key class.

---

#### Constructor Summary

Construct the alternate Key class.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

protected

Object

readResolve

()

Resolve the Key object.

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

Resolve the Key object.

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

- KeyRep

```java
public KeyRep​(
KeyRep.Type
type,

String
algorithm,

String
format,
byte[] encoded)
```

Construct the alternate Key class.

**Parameters:** type

- either one of Type.SECRET, Type.PUBLIC, or Type.PRIVATE
**Parameters:** algorithm

- the algorithm returned from

Key.getAlgorithm()
**Parameters:** format

- the encoding format returned from

Key.getFormat()
**Parameters:** encoded

- the encoded bytes returned from

Key.getEncoded()
**Throws:** NullPointerException

- if type is

null

,
if algorithm is

null

,
if format is

null

,
or if encoded is

null

============ METHOD DETAIL ==========

- Method Detail

- readResolve

```java
protected
Object
readResolve()
throws
ObjectStreamException
```

Resolve the Key object.

This method supports three Type/format combinations:

- Type.SECRET/"RAW" - returns a SecretKeySpec object
constructed using encoded key bytes and algorithm

Type.PUBLIC/"X.509" - gets a KeyFactory instance for
the key algorithm, constructs an X509EncodedKeySpec with the
encoded key bytes, and generates a public key from the spec

Type.PRIVATE/"PKCS#8" - gets a KeyFactory instance for
the key algorithm, constructs a PKCS8EncodedKeySpec with the
encoded key bytes, and generates a private key from the spec

**Returns:** the resolved Key object
**Throws:** ObjectStreamException

- if the Type/format
combination is unrecognized, if the algorithm, key format, or
encoded key bytes are unrecognized/invalid, of if the
resolution of the key fails for any reason

Constructor Detail

- KeyRep

```java
public KeyRep​(
KeyRep.Type
type,

String
algorithm,

String
format,
byte[] encoded)
```

Construct the alternate Key class.

**Parameters:** type

- either one of Type.SECRET, Type.PUBLIC, or Type.PRIVATE
**Parameters:** algorithm

- the algorithm returned from

Key.getAlgorithm()
**Parameters:** format

- the encoding format returned from

Key.getFormat()
**Parameters:** encoded

- the encoded bytes returned from

Key.getEncoded()
**Throws:** NullPointerException

- if type is

null

,
if algorithm is

null

,
if format is

null

,
or if encoded is

null

---

#### Constructor Detail

KeyRep

```java
public KeyRep​(
KeyRep.Type
type,

String
algorithm,

String
format,
byte[] encoded)
```

Construct the alternate Key class.

**Parameters:** type

- either one of Type.SECRET, Type.PUBLIC, or Type.PRIVATE
**Parameters:** algorithm

- the algorithm returned from

Key.getAlgorithm()
**Parameters:** format

- the encoding format returned from

Key.getFormat()
**Parameters:** encoded

- the encoded bytes returned from

Key.getEncoded()
**Throws:** NullPointerException

- if type is

null

,
if algorithm is

null

,
if format is

null

,
or if encoded is

null

---

#### KeyRep

public KeyRep​(

KeyRep.Type

type,

String

algorithm,

String

format,
byte[] encoded)

Construct the alternate Key class.

Method Detail

- readResolve

```java
protected
Object
readResolve()
throws
ObjectStreamException
```

Resolve the Key object.

This method supports three Type/format combinations:

- Type.SECRET/"RAW" - returns a SecretKeySpec object
constructed using encoded key bytes and algorithm

Type.PUBLIC/"X.509" - gets a KeyFactory instance for
the key algorithm, constructs an X509EncodedKeySpec with the
encoded key bytes, and generates a public key from the spec

Type.PRIVATE/"PKCS#8" - gets a KeyFactory instance for
the key algorithm, constructs a PKCS8EncodedKeySpec with the
encoded key bytes, and generates a private key from the spec

**Returns:** the resolved Key object
**Throws:** ObjectStreamException

- if the Type/format
combination is unrecognized, if the algorithm, key format, or
encoded key bytes are unrecognized/invalid, of if the
resolution of the key fails for any reason

---

#### Method Detail

readResolve

```java
protected
Object
readResolve()
throws
ObjectStreamException
```

Resolve the Key object.

This method supports three Type/format combinations:

- Type.SECRET/"RAW" - returns a SecretKeySpec object
constructed using encoded key bytes and algorithm

Type.PUBLIC/"X.509" - gets a KeyFactory instance for
the key algorithm, constructs an X509EncodedKeySpec with the
encoded key bytes, and generates a public key from the spec

Type.PRIVATE/"PKCS#8" - gets a KeyFactory instance for
the key algorithm, constructs a PKCS8EncodedKeySpec with the
encoded key bytes, and generates a private key from the spec

**Returns:** the resolved Key object
**Throws:** ObjectStreamException

- if the Type/format
combination is unrecognized, if the algorithm, key format, or
encoded key bytes are unrecognized/invalid, of if the
resolution of the key fails for any reason

---

#### readResolve

protected

Object

readResolve()
throws

ObjectStreamException

Resolve the Key object.

This method supports three Type/format combinations:

- Type.SECRET/"RAW" - returns a SecretKeySpec object
constructed using encoded key bytes and algorithm

Type.PUBLIC/"X.509" - gets a KeyFactory instance for
the key algorithm, constructs an X509EncodedKeySpec with the
encoded key bytes, and generates a public key from the spec

Type.PRIVATE/"PKCS#8" - gets a KeyFactory instance for
the key algorithm, constructs a PKCS8EncodedKeySpec with the
encoded key bytes, and generates a private key from the spec

This method supports three Type/format combinations:

- Type.SECRET/"RAW" - returns a SecretKeySpec object
constructed using encoded key bytes and algorithm

Type.PUBLIC/"X.509" - gets a KeyFactory instance for
the key algorithm, constructs an X509EncodedKeySpec with the
encoded key bytes, and generates a public key from the spec

Type.PRIVATE/"PKCS#8" - gets a KeyFactory instance for
the key algorithm, constructs a PKCS8EncodedKeySpec with the
encoded key bytes, and generates a private key from the spec

Type.SECRET/"RAW" - returns a SecretKeySpec object
constructed using encoded key bytes and algorithm

Type.PUBLIC/"X.509" - gets a KeyFactory instance for
the key algorithm, constructs an X509EncodedKeySpec with the
encoded key bytes, and generates a public key from the spec

Type.PRIVATE/"PKCS#8" - gets a KeyFactory instance for
the key algorithm, constructs a PKCS8EncodedKeySpec with the
encoded key bytes, and generates a private key from the spec

---

