# Class EncodedKeySpec

**Source:** `java.base\java\security\spec\EncodedKeySpec.html`

### Class Description

```java
public abstract class
EncodedKeySpec

extends
Object

implements
KeySpec
```

This class represents a public or private key in encoded format.

**All Implemented Interfaces:** KeySpec

---

### Field Details

*No entries found.*

### Constructor Details

#### public EncodedKeySpec​(byte[] encodedKey)

Creates a new

EncodedKeySpec

with the given encoded key.

**Parameters:**
- encodedKey

- the encoded key. The contents of the
array are copied to protect against subsequent modification.

**Throws:**
- NullPointerException

- if

encodedKey

is null.

---

#### protected EncodedKeySpec​(byte[] encodedKey,

String
algorithm)

Creates a new

EncodedKeySpec

with the given encoded key.
This constructor is useful when subsequent callers of the

EncodedKeySpec

object might not know the algorithm
of the key.

**Parameters:**
- encodedKey

- the encoded key. The contents of the
array are copied to protect against subsequent modification.
- algorithm

- the algorithm name of the encoded key
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

#### public
String
getAlgorithm()

Returns the name of the algorithm of the encoded key.

**Returns:**
- the name of the algorithm, or null if not specified

**Since:**
- 9

---

#### public byte[] getEncoded()

Returns the encoded key.

**Returns:**
- the encoded key. Returns a new array each time
this method is called.

---

#### public abstract
String
getFormat()

Returns the name of the encoding format associated with this
key specification.

If the opaque representation of a key
(see

Key

) can be transformed
(see

KeyFactory

)
into this key specification (or a subclass of it),

getFormat

called
on the opaque key returns the same value as the

getFormat

method
of this key specification.

**Returns:**
- a string representation of the encoding format.

---

### Additional Sections

#### Class EncodedKeySpec

java.lang.Object

- java.security.spec.EncodedKeySpec

java.security.spec.EncodedKeySpec

**All Implemented Interfaces:** KeySpec

**Direct Known Subclasses:** PKCS8EncodedKeySpec

,

X509EncodedKeySpec

```java
public abstract class
EncodedKeySpec

extends
Object

implements
KeySpec
```

This class represents a public or private key in encoded format.

**Since:** 1.2
**See Also:** Key

,

KeyFactory

,

KeySpec

,

X509EncodedKeySpec

,

PKCS8EncodedKeySpec

public abstract class

EncodedKeySpec

extends

Object

implements

KeySpec

This class represents a public or private key in encoded format.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

EncodedKeySpec

​(byte[] encodedKey)

Creates a new

EncodedKeySpec

with the given encoded key.

protected

EncodedKeySpec

​(byte[] encodedKey,

String

algorithm)

Creates a new

EncodedKeySpec

with the given encoded key.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

String

getAlgorithm

()

Returns the name of the algorithm of the encoded key.

byte[]

getEncoded

()

Returns the encoded key.

abstract

String

getFormat

()

Returns the name of the encoding format associated with this
key specification.

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

Modifier

Constructor

Description

EncodedKeySpec

​(byte[] encodedKey)

Creates a new

EncodedKeySpec

with the given encoded key.

protected

EncodedKeySpec

​(byte[] encodedKey,

String

algorithm)

Creates a new

EncodedKeySpec

with the given encoded key.

---

#### Constructor Summary

Creates a new

EncodedKeySpec

with the given encoded key.

Method Summary

All Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

String

getAlgorithm

()

Returns the name of the algorithm of the encoded key.

byte[]

getEncoded

()

Returns the encoded key.

abstract

String

getFormat

()

Returns the name of the encoding format associated with this
key specification.

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

Returns the name of the algorithm of the encoded key.

Returns the encoded key.

Returns the name of the encoding format associated with this
key specification.

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

- EncodedKeySpec

```java
public EncodedKeySpec​(byte[] encodedKey)
```

Creates a new

EncodedKeySpec

with the given encoded key.

**Parameters:** encodedKey

- the encoded key. The contents of the
array are copied to protect against subsequent modification.
**Throws:** NullPointerException

- if

encodedKey

is null.

- EncodedKeySpec

```java
protected EncodedKeySpec​(byte[] encodedKey,

String
algorithm)
```

Creates a new

EncodedKeySpec

with the given encoded key.
This constructor is useful when subsequent callers of the

EncodedKeySpec

object might not know the algorithm
of the key.

**Parameters:** encodedKey

- the encoded key. The contents of the
array are copied to protect against subsequent modification.
**Parameters:** algorithm

- the algorithm name of the encoded key
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

- getAlgorithm

```java
public
String
getAlgorithm()
```

Returns the name of the algorithm of the encoded key.

**Returns:** the name of the algorithm, or null if not specified
**Since:** 9

- getEncoded

```java
public byte[] getEncoded()
```

Returns the encoded key.

**Returns:** the encoded key. Returns a new array each time
this method is called.

- getFormat

```java
public abstract
String
getFormat()
```

Returns the name of the encoding format associated with this
key specification.

If the opaque representation of a key
(see

Key

) can be transformed
(see

KeyFactory

)
into this key specification (or a subclass of it),

getFormat

called
on the opaque key returns the same value as the

getFormat

method
of this key specification.

**Returns:** a string representation of the encoding format.

Constructor Detail

- EncodedKeySpec

```java
public EncodedKeySpec​(byte[] encodedKey)
```

Creates a new

EncodedKeySpec

with the given encoded key.

**Parameters:** encodedKey

- the encoded key. The contents of the
array are copied to protect against subsequent modification.
**Throws:** NullPointerException

- if

encodedKey

is null.

- EncodedKeySpec

```java
protected EncodedKeySpec​(byte[] encodedKey,

String
algorithm)
```

Creates a new

EncodedKeySpec

with the given encoded key.
This constructor is useful when subsequent callers of the

EncodedKeySpec

object might not know the algorithm
of the key.

**Parameters:** encodedKey

- the encoded key. The contents of the
array are copied to protect against subsequent modification.
**Parameters:** algorithm

- the algorithm name of the encoded key
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

EncodedKeySpec

```java
public EncodedKeySpec​(byte[] encodedKey)
```

Creates a new

EncodedKeySpec

with the given encoded key.

**Parameters:** encodedKey

- the encoded key. The contents of the
array are copied to protect against subsequent modification.
**Throws:** NullPointerException

- if

encodedKey

is null.

---

#### EncodedKeySpec

public EncodedKeySpec​(byte[] encodedKey)

Creates a new

EncodedKeySpec

with the given encoded key.

EncodedKeySpec

```java
protected EncodedKeySpec​(byte[] encodedKey,

String
algorithm)
```

Creates a new

EncodedKeySpec

with the given encoded key.
This constructor is useful when subsequent callers of the

EncodedKeySpec

object might not know the algorithm
of the key.

**Parameters:** encodedKey

- the encoded key. The contents of the
array are copied to protect against subsequent modification.
**Parameters:** algorithm

- the algorithm name of the encoded key
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

#### EncodedKeySpec

protected EncodedKeySpec​(byte[] encodedKey,

String

algorithm)

Creates a new

EncodedKeySpec

with the given encoded key.
This constructor is useful when subsequent callers of the

EncodedKeySpec

object might not know the algorithm
of the key.

Method Detail

- getAlgorithm

```java
public
String
getAlgorithm()
```

Returns the name of the algorithm of the encoded key.

**Returns:** the name of the algorithm, or null if not specified
**Since:** 9

- getEncoded

```java
public byte[] getEncoded()
```

Returns the encoded key.

**Returns:** the encoded key. Returns a new array each time
this method is called.

- getFormat

```java
public abstract
String
getFormat()
```

Returns the name of the encoding format associated with this
key specification.

If the opaque representation of a key
(see

Key

) can be transformed
(see

KeyFactory

)
into this key specification (or a subclass of it),

getFormat

called
on the opaque key returns the same value as the

getFormat

method
of this key specification.

**Returns:** a string representation of the encoding format.

---

#### Method Detail

getAlgorithm

```java
public
String
getAlgorithm()
```

Returns the name of the algorithm of the encoded key.

**Returns:** the name of the algorithm, or null if not specified
**Since:** 9

---

#### getAlgorithm

public

String

getAlgorithm()

Returns the name of the algorithm of the encoded key.

getEncoded

```java
public byte[] getEncoded()
```

Returns the encoded key.

**Returns:** the encoded key. Returns a new array each time
this method is called.

---

#### getEncoded

public byte[] getEncoded()

Returns the encoded key.

getFormat

```java
public abstract
String
getFormat()
```

Returns the name of the encoding format associated with this
key specification.

If the opaque representation of a key
(see

Key

) can be transformed
(see

KeyFactory

)
into this key specification (or a subclass of it),

getFormat

called
on the opaque key returns the same value as the

getFormat

method
of this key specification.

**Returns:** a string representation of the encoding format.

---

#### getFormat

public abstract

String

getFormat()

Returns the name of the encoding format associated with this
key specification.

If the opaque representation of a key
(see

Key

) can be transformed
(see

KeyFactory

)
into this key specification (or a subclass of it),

getFormat

called
on the opaque key returns the same value as the

getFormat

method
of this key specification.

If the opaque representation of a key
(see

Key

) can be transformed
(see

KeyFactory

)
into this key specification (or a subclass of it),

getFormat

called
on the opaque key returns the same value as the

getFormat

method
of this key specification.

---

