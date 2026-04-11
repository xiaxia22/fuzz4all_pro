# Class RC5ParameterSpec

**Source:** `java.base\javax\crypto\spec\RC5ParameterSpec.html`

### Class Description

```java
public class
RC5ParameterSpec

extends
Object

implements
AlgorithmParameterSpec
```

This class specifies the parameters used with the

RC5

algorithm.

The parameters consist of a version number, a rounds count, a word
size, and optionally an initialization vector (IV) (only in feedback mode).

This class can be used to initialize a

Cipher

object that
implements the

RC5

algorithm as supplied by

RSA Security LLC

,
or any parties authorized by RSA Security.

**All Implemented Interfaces:** AlgorithmParameterSpec

---

### Field Details

*No entries found.*

### Constructor Details

#### public RC5ParameterSpec​(int version,
int rounds,
int wordSize)

Constructs a parameter set for RC5 from the given version, number of
rounds and word size (in bits).

**Parameters:**
- version

- the version.
- rounds

- the number of rounds.
- wordSize

- the word size in bits.

---

#### public RC5ParameterSpec​(int version,
int rounds,
int wordSize,
byte[] iv)

Constructs a parameter set for RC5 from the given version, number of
rounds, word size (in bits), and IV.

Note that the size of the IV (block size) must be twice the word
size. The bytes that constitute the IV are those between

iv[0]

and

iv[2*(wordSize/8)-1]

inclusive.

**Parameters:**
- version

- the version.
- rounds

- the number of rounds.
- wordSize

- the word size in bits.
- iv

- the buffer with the IV. The first

2*(wordSize/8)

bytes of the buffer are copied to protect against subsequent
modification.

**Throws:**
- IllegalArgumentException

- if

iv

is

null

or

(iv.length < 2 * (wordSize / 8))

---

#### public RC5ParameterSpec​(int version,
int rounds,
int wordSize,
byte[] iv,
int offset)

Constructs a parameter set for RC5 from the given version, number of
rounds, word size (in bits), and IV.

The IV is taken from

iv

, starting at

offset

inclusive.
Note that the size of the IV (block size), starting at

offset

inclusive, must be twice the word size.
The bytes that constitute the IV are those between

iv[offset]

and

iv[offset+2*(wordSize/8)-1]

inclusive.

**Parameters:**
- version

- the version.
- rounds

- the number of rounds.
- wordSize

- the word size in bits.
- iv

- the buffer with the IV. The first

2*(wordSize/8)

bytes of the buffer beginning at

offset

inclusive are copied to protect against subsequent modification.
- offset

- the offset in

iv

where the IV starts.

**Throws:**
- IllegalArgumentException

- if

iv

is

null

or

(iv.length - offset < 2 * (wordSize / 8))

---

### Method Details

#### public int getVersion()

Returns the version.

**Returns:**
- the version.

---

#### public int getRounds()

Returns the number of rounds.

**Returns:**
- the number of rounds.

---

#### public int getWordSize()

Returns the word size in bits.

**Returns:**
- the word size in bits.

---

#### public byte[] getIV()

Returns the IV or null if this parameter set does not contain an IV.

**Returns:**
- the IV or null if this parameter set does not contain an IV.
Returns a new array each time this method is called.

---

#### public boolean equals​(
Object
obj)

Tests for equality between the specified object and this
object. Two RC5ParameterSpec objects are considered equal if their
version numbers, number of rounds, word sizes, and IVs are equal.
(Two IV references are considered equal if both are

null

.)

**Overrides:**
- equals

in class

Object

**Parameters:**
- obj

- the object to test for equality with this object.

**Returns:**
- true if the objects are considered equal, false if

obj

is null or otherwise.

**See Also:**
- Object.hashCode()

,

HashMap

---

#### public int hashCode()

Calculates a hash code value for the object.
Objects that are equal will also have the same hashcode.

**Overrides:**
- hashCode

in class

Object

**Returns:**
- a hash code value for this object.

**See Also:**
- Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

### Additional Sections

#### Class RC5ParameterSpec

java.lang.Object

- javax.crypto.spec.RC5ParameterSpec

javax.crypto.spec.RC5ParameterSpec

**All Implemented Interfaces:** AlgorithmParameterSpec

```java
public class
RC5ParameterSpec

extends
Object

implements
AlgorithmParameterSpec
```

This class specifies the parameters used with the

RC5

algorithm.

The parameters consist of a version number, a rounds count, a word
size, and optionally an initialization vector (IV) (only in feedback mode).

This class can be used to initialize a

Cipher

object that
implements the

RC5

algorithm as supplied by

RSA Security LLC

,
or any parties authorized by RSA Security.

**Since:** 1.4

public class

RC5ParameterSpec

extends

Object

implements

AlgorithmParameterSpec

This class specifies the parameters used with the

RC5

algorithm.

The parameters consist of a version number, a rounds count, a word
size, and optionally an initialization vector (IV) (only in feedback mode).

This class can be used to initialize a

Cipher

object that
implements the

RC5

algorithm as supplied by

RSA Security LLC

,
or any parties authorized by RSA Security.

The parameters consist of a version number, a rounds count, a word
size, and optionally an initialization vector (IV) (only in feedback mode).

This class can be used to initialize a

Cipher

object that
implements the

RC5

algorithm as supplied by

RSA Security LLC

,
or any parties authorized by RSA Security.

This class can be used to initialize a

Cipher

object that
implements the

RC5

algorithm as supplied by

RSA Security LLC

,
or any parties authorized by RSA Security.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

RC5ParameterSpec

​(int version,
int rounds,
int wordSize)

Constructs a parameter set for RC5 from the given version, number of
rounds and word size (in bits).

RC5ParameterSpec

​(int version,
int rounds,
int wordSize,
byte[] iv)

Constructs a parameter set for RC5 from the given version, number of
rounds, word size (in bits), and IV.

RC5ParameterSpec

​(int version,
int rounds,
int wordSize,
byte[] iv,
int offset)

Constructs a parameter set for RC5 from the given version, number of
rounds, word size (in bits), and IV.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

boolean

equals

​(

Object

obj)

Tests for equality between the specified object and this
object.

byte[]

getIV

()

Returns the IV or null if this parameter set does not contain an IV.

int

getRounds

()

Returns the number of rounds.

int

getVersion

()

Returns the version.

int

getWordSize

()

Returns the word size in bits.

int

hashCode

()

Calculates a hash code value for the object.

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

RC5ParameterSpec

​(int version,
int rounds,
int wordSize)

Constructs a parameter set for RC5 from the given version, number of
rounds and word size (in bits).

RC5ParameterSpec

​(int version,
int rounds,
int wordSize,
byte[] iv)

Constructs a parameter set for RC5 from the given version, number of
rounds, word size (in bits), and IV.

RC5ParameterSpec

​(int version,
int rounds,
int wordSize,
byte[] iv,
int offset)

Constructs a parameter set for RC5 from the given version, number of
rounds, word size (in bits), and IV.

---

#### Constructor Summary

Constructs a parameter set for RC5 from the given version, number of
rounds and word size (in bits).

Constructs a parameter set for RC5 from the given version, number of
rounds, word size (in bits), and IV.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

boolean

equals

​(

Object

obj)

Tests for equality between the specified object and this
object.

byte[]

getIV

()

Returns the IV or null if this parameter set does not contain an IV.

int

getRounds

()

Returns the number of rounds.

int

getVersion

()

Returns the version.

int

getWordSize

()

Returns the word size in bits.

int

hashCode

()

Calculates a hash code value for the object.

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

toString

,

wait

,

wait

,

wait

---

#### Method Summary

Tests for equality between the specified object and this
object.

Returns the IV or null if this parameter set does not contain an IV.

Returns the number of rounds.

Returns the version.

Returns the word size in bits.

Calculates a hash code value for the object.

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

- RC5ParameterSpec

```java
public RC5ParameterSpec​(int version,
int rounds,
int wordSize)
```

Constructs a parameter set for RC5 from the given version, number of
rounds and word size (in bits).

**Parameters:** version

- the version.
**Parameters:** rounds

- the number of rounds.
**Parameters:** wordSize

- the word size in bits.

- RC5ParameterSpec

```java
public RC5ParameterSpec​(int version,
int rounds,
int wordSize,
byte[] iv)
```

Constructs a parameter set for RC5 from the given version, number of
rounds, word size (in bits), and IV.

Note that the size of the IV (block size) must be twice the word
size. The bytes that constitute the IV are those between

iv[0]

and

iv[2*(wordSize/8)-1]

inclusive.

**Parameters:** version

- the version.
**Parameters:** rounds

- the number of rounds.
**Parameters:** wordSize

- the word size in bits.
**Parameters:** iv

- the buffer with the IV. The first

2*(wordSize/8)

bytes of the buffer are copied to protect against subsequent
modification.
**Throws:** IllegalArgumentException

- if

iv

is

null

or

(iv.length < 2 * (wordSize / 8))

- RC5ParameterSpec

```java
public RC5ParameterSpec​(int version,
int rounds,
int wordSize,
byte[] iv,
int offset)
```

Constructs a parameter set for RC5 from the given version, number of
rounds, word size (in bits), and IV.

The IV is taken from

iv

, starting at

offset

inclusive.
Note that the size of the IV (block size), starting at

offset

inclusive, must be twice the word size.
The bytes that constitute the IV are those between

iv[offset]

and

iv[offset+2*(wordSize/8)-1]

inclusive.

**Parameters:** version

- the version.
**Parameters:** rounds

- the number of rounds.
**Parameters:** wordSize

- the word size in bits.
**Parameters:** iv

- the buffer with the IV. The first

2*(wordSize/8)

bytes of the buffer beginning at

offset

inclusive are copied to protect against subsequent modification.
**Parameters:** offset

- the offset in

iv

where the IV starts.
**Throws:** IllegalArgumentException

- if

iv

is

null

or

(iv.length - offset < 2 * (wordSize / 8))

============ METHOD DETAIL ==========

- Method Detail

- getVersion

```java
public int getVersion()
```

Returns the version.

**Returns:** the version.

- getRounds

```java
public int getRounds()
```

Returns the number of rounds.

**Returns:** the number of rounds.

- getWordSize

```java
public int getWordSize()
```

Returns the word size in bits.

**Returns:** the word size in bits.

- getIV

```java
public byte[] getIV()
```

Returns the IV or null if this parameter set does not contain an IV.

**Returns:** the IV or null if this parameter set does not contain an IV.
Returns a new array each time this method is called.

- equals

```java
public boolean equals​(
Object
obj)
```

Tests for equality between the specified object and this
object. Two RC5ParameterSpec objects are considered equal if their
version numbers, number of rounds, word sizes, and IVs are equal.
(Two IV references are considered equal if both are

null

.)

**Overrides:** equals

in class

Object
**Parameters:** obj

- the object to test for equality with this object.
**Returns:** true if the objects are considered equal, false if

obj

is null or otherwise.
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
public int hashCode()
```

Calculates a hash code value for the object.
Objects that are equal will also have the same hashcode.

**Overrides:** hashCode

in class

Object
**Returns:** a hash code value for this object.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

Constructor Detail

- RC5ParameterSpec

```java
public RC5ParameterSpec​(int version,
int rounds,
int wordSize)
```

Constructs a parameter set for RC5 from the given version, number of
rounds and word size (in bits).

**Parameters:** version

- the version.
**Parameters:** rounds

- the number of rounds.
**Parameters:** wordSize

- the word size in bits.

- RC5ParameterSpec

```java
public RC5ParameterSpec​(int version,
int rounds,
int wordSize,
byte[] iv)
```

Constructs a parameter set for RC5 from the given version, number of
rounds, word size (in bits), and IV.

Note that the size of the IV (block size) must be twice the word
size. The bytes that constitute the IV are those between

iv[0]

and

iv[2*(wordSize/8)-1]

inclusive.

**Parameters:** version

- the version.
**Parameters:** rounds

- the number of rounds.
**Parameters:** wordSize

- the word size in bits.
**Parameters:** iv

- the buffer with the IV. The first

2*(wordSize/8)

bytes of the buffer are copied to protect against subsequent
modification.
**Throws:** IllegalArgumentException

- if

iv

is

null

or

(iv.length < 2 * (wordSize / 8))

- RC5ParameterSpec

```java
public RC5ParameterSpec​(int version,
int rounds,
int wordSize,
byte[] iv,
int offset)
```

Constructs a parameter set for RC5 from the given version, number of
rounds, word size (in bits), and IV.

The IV is taken from

iv

, starting at

offset

inclusive.
Note that the size of the IV (block size), starting at

offset

inclusive, must be twice the word size.
The bytes that constitute the IV are those between

iv[offset]

and

iv[offset+2*(wordSize/8)-1]

inclusive.

**Parameters:** version

- the version.
**Parameters:** rounds

- the number of rounds.
**Parameters:** wordSize

- the word size in bits.
**Parameters:** iv

- the buffer with the IV. The first

2*(wordSize/8)

bytes of the buffer beginning at

offset

inclusive are copied to protect against subsequent modification.
**Parameters:** offset

- the offset in

iv

where the IV starts.
**Throws:** IllegalArgumentException

- if

iv

is

null

or

(iv.length - offset < 2 * (wordSize / 8))

---

#### Constructor Detail

RC5ParameterSpec

```java
public RC5ParameterSpec​(int version,
int rounds,
int wordSize)
```

Constructs a parameter set for RC5 from the given version, number of
rounds and word size (in bits).

**Parameters:** version

- the version.
**Parameters:** rounds

- the number of rounds.
**Parameters:** wordSize

- the word size in bits.

---

#### RC5ParameterSpec

public RC5ParameterSpec​(int version,
int rounds,
int wordSize)

Constructs a parameter set for RC5 from the given version, number of
rounds and word size (in bits).

RC5ParameterSpec

```java
public RC5ParameterSpec​(int version,
int rounds,
int wordSize,
byte[] iv)
```

Constructs a parameter set for RC5 from the given version, number of
rounds, word size (in bits), and IV.

Note that the size of the IV (block size) must be twice the word
size. The bytes that constitute the IV are those between

iv[0]

and

iv[2*(wordSize/8)-1]

inclusive.

**Parameters:** version

- the version.
**Parameters:** rounds

- the number of rounds.
**Parameters:** wordSize

- the word size in bits.
**Parameters:** iv

- the buffer with the IV. The first

2*(wordSize/8)

bytes of the buffer are copied to protect against subsequent
modification.
**Throws:** IllegalArgumentException

- if

iv

is

null

or

(iv.length < 2 * (wordSize / 8))

---

#### RC5ParameterSpec

public RC5ParameterSpec​(int version,
int rounds,
int wordSize,
byte[] iv)

Constructs a parameter set for RC5 from the given version, number of
rounds, word size (in bits), and IV.

Note that the size of the IV (block size) must be twice the word
size. The bytes that constitute the IV are those between

iv[0]

and

iv[2*(wordSize/8)-1]

inclusive.

Note that the size of the IV (block size) must be twice the word
size. The bytes that constitute the IV are those between

iv[0]

and

iv[2*(wordSize/8)-1]

inclusive.

RC5ParameterSpec

```java
public RC5ParameterSpec​(int version,
int rounds,
int wordSize,
byte[] iv,
int offset)
```

Constructs a parameter set for RC5 from the given version, number of
rounds, word size (in bits), and IV.

The IV is taken from

iv

, starting at

offset

inclusive.
Note that the size of the IV (block size), starting at

offset

inclusive, must be twice the word size.
The bytes that constitute the IV are those between

iv[offset]

and

iv[offset+2*(wordSize/8)-1]

inclusive.

**Parameters:** version

- the version.
**Parameters:** rounds

- the number of rounds.
**Parameters:** wordSize

- the word size in bits.
**Parameters:** iv

- the buffer with the IV. The first

2*(wordSize/8)

bytes of the buffer beginning at

offset

inclusive are copied to protect against subsequent modification.
**Parameters:** offset

- the offset in

iv

where the IV starts.
**Throws:** IllegalArgumentException

- if

iv

is

null

or

(iv.length - offset < 2 * (wordSize / 8))

---

#### RC5ParameterSpec

public RC5ParameterSpec​(int version,
int rounds,
int wordSize,
byte[] iv,
int offset)

Constructs a parameter set for RC5 from the given version, number of
rounds, word size (in bits), and IV.

The IV is taken from

iv

, starting at

offset

inclusive.
Note that the size of the IV (block size), starting at

offset

inclusive, must be twice the word size.
The bytes that constitute the IV are those between

iv[offset]

and

iv[offset+2*(wordSize/8)-1]

inclusive.

The IV is taken from

iv

, starting at

offset

inclusive.
Note that the size of the IV (block size), starting at

offset

inclusive, must be twice the word size.
The bytes that constitute the IV are those between

iv[offset]

and

iv[offset+2*(wordSize/8)-1]

inclusive.

Method Detail

- getVersion

```java
public int getVersion()
```

Returns the version.

**Returns:** the version.

- getRounds

```java
public int getRounds()
```

Returns the number of rounds.

**Returns:** the number of rounds.

- getWordSize

```java
public int getWordSize()
```

Returns the word size in bits.

**Returns:** the word size in bits.

- getIV

```java
public byte[] getIV()
```

Returns the IV or null if this parameter set does not contain an IV.

**Returns:** the IV or null if this parameter set does not contain an IV.
Returns a new array each time this method is called.

- equals

```java
public boolean equals​(
Object
obj)
```

Tests for equality between the specified object and this
object. Two RC5ParameterSpec objects are considered equal if their
version numbers, number of rounds, word sizes, and IVs are equal.
(Two IV references are considered equal if both are

null

.)

**Overrides:** equals

in class

Object
**Parameters:** obj

- the object to test for equality with this object.
**Returns:** true if the objects are considered equal, false if

obj

is null or otherwise.
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
public int hashCode()
```

Calculates a hash code value for the object.
Objects that are equal will also have the same hashcode.

**Overrides:** hashCode

in class

Object
**Returns:** a hash code value for this object.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### Method Detail

getVersion

```java
public int getVersion()
```

Returns the version.

**Returns:** the version.

---

#### getVersion

public int getVersion()

Returns the version.

getRounds

```java
public int getRounds()
```

Returns the number of rounds.

**Returns:** the number of rounds.

---

#### getRounds

public int getRounds()

Returns the number of rounds.

getWordSize

```java
public int getWordSize()
```

Returns the word size in bits.

**Returns:** the word size in bits.

---

#### getWordSize

public int getWordSize()

Returns the word size in bits.

getIV

```java
public byte[] getIV()
```

Returns the IV or null if this parameter set does not contain an IV.

**Returns:** the IV or null if this parameter set does not contain an IV.
Returns a new array each time this method is called.

---

#### getIV

public byte[] getIV()

Returns the IV or null if this parameter set does not contain an IV.

equals

```java
public boolean equals​(
Object
obj)
```

Tests for equality between the specified object and this
object. Two RC5ParameterSpec objects are considered equal if their
version numbers, number of rounds, word sizes, and IVs are equal.
(Two IV references are considered equal if both are

null

.)

**Overrides:** equals

in class

Object
**Parameters:** obj

- the object to test for equality with this object.
**Returns:** true if the objects are considered equal, false if

obj

is null or otherwise.
**See Also:** Object.hashCode()

,

HashMap

---

#### equals

public boolean equals​(

Object

obj)

Tests for equality between the specified object and this
object. Two RC5ParameterSpec objects are considered equal if their
version numbers, number of rounds, word sizes, and IVs are equal.
(Two IV references are considered equal if both are

null

.)

hashCode

```java
public int hashCode()
```

Calculates a hash code value for the object.
Objects that are equal will also have the same hashcode.

**Overrides:** hashCode

in class

Object
**Returns:** a hash code value for this object.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### hashCode

public int hashCode()

Calculates a hash code value for the object.
Objects that are equal will also have the same hashcode.

---

