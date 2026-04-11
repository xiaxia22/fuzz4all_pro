# Class RC2ParameterSpec

**Source:** `java.base\javax\crypto\spec\RC2ParameterSpec.html`

### Class Description

```java
public class
RC2ParameterSpec

extends
Object

implements
AlgorithmParameterSpec
```

This class specifies the parameters used with the

RC2

algorithm.

The parameters consist of an effective key size and optionally
an 8-byte initialization vector (IV) (only in feedback mode).

This class can be used to initialize a

Cipher

object that
implements the

RC2

algorithm.

**All Implemented Interfaces:** AlgorithmParameterSpec

---

### Field Details

*No entries found.*

### Constructor Details

#### public RC2ParameterSpec​(int effectiveKeyBits)

Constructs a parameter set for RC2 from the given effective key size
(in bits).

**Parameters:**
- effectiveKeyBits

- the effective key size in bits.

---

#### public RC2ParameterSpec​(int effectiveKeyBits,
byte[] iv)

Constructs a parameter set for RC2 from the given effective key size
(in bits) and an 8-byte IV.

The bytes that constitute the IV are those between

iv[0]

and

iv[7]

inclusive.

**Parameters:**
- effectiveKeyBits

- the effective key size in bits.
- iv

- the buffer with the 8-byte IV. The first 8 bytes of
the buffer are copied to protect against subsequent modification.

**Throws:**
- IllegalArgumentException

- if

iv

is null.

---

#### public RC2ParameterSpec​(int effectiveKeyBits,
byte[] iv,
int offset)

Constructs a parameter set for RC2 from the given effective key size
(in bits) and IV.

The IV is taken from

iv

, starting at

offset

inclusive.
The bytes that constitute the IV are those between

iv[offset]

and

iv[offset+7]

inclusive.

**Parameters:**
- effectiveKeyBits

- the effective key size in bits.
- iv

- the buffer with the IV. The first 8 bytes
of the buffer beginning at

offset

inclusive
are copied to protect against subsequent modification.
- offset

- the offset in

iv

where the 8-byte IV
starts.

**Throws:**
- IllegalArgumentException

- if

iv

is null.

---

### Method Details

#### public int getEffectiveKeyBits()

Returns the effective key size in bits.

**Returns:**
- the effective key size in bits.

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
object. Two RC2ParameterSpec objects are considered equal if their
effective key sizes and IVs are equal.
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

#### Class RC2ParameterSpec

java.lang.Object

- javax.crypto.spec.RC2ParameterSpec

javax.crypto.spec.RC2ParameterSpec

**All Implemented Interfaces:** AlgorithmParameterSpec

```java
public class
RC2ParameterSpec

extends
Object

implements
AlgorithmParameterSpec
```

This class specifies the parameters used with the

RC2

algorithm.

The parameters consist of an effective key size and optionally
an 8-byte initialization vector (IV) (only in feedback mode).

This class can be used to initialize a

Cipher

object that
implements the

RC2

algorithm.

**Since:** 1.4

public class

RC2ParameterSpec

extends

Object

implements

AlgorithmParameterSpec

This class specifies the parameters used with the

RC2

algorithm.

The parameters consist of an effective key size and optionally
an 8-byte initialization vector (IV) (only in feedback mode).

This class can be used to initialize a

Cipher

object that
implements the

RC2

algorithm.

The parameters consist of an effective key size and optionally
an 8-byte initialization vector (IV) (only in feedback mode).

This class can be used to initialize a

Cipher

object that
implements the

RC2

algorithm.

This class can be used to initialize a

Cipher

object that
implements the

RC2

algorithm.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

RC2ParameterSpec

​(int effectiveKeyBits)

Constructs a parameter set for RC2 from the given effective key size
(in bits).

RC2ParameterSpec

​(int effectiveKeyBits,
byte[] iv)

Constructs a parameter set for RC2 from the given effective key size
(in bits) and an 8-byte IV.

RC2ParameterSpec

​(int effectiveKeyBits,
byte[] iv,
int offset)

Constructs a parameter set for RC2 from the given effective key size
(in bits) and IV.

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

int

getEffectiveKeyBits

()

Returns the effective key size in bits.

byte[]

getIV

()

Returns the IV or null if this parameter set does not contain an IV.

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

RC2ParameterSpec

​(int effectiveKeyBits)

Constructs a parameter set for RC2 from the given effective key size
(in bits).

RC2ParameterSpec

​(int effectiveKeyBits,
byte[] iv)

Constructs a parameter set for RC2 from the given effective key size
(in bits) and an 8-byte IV.

RC2ParameterSpec

​(int effectiveKeyBits,
byte[] iv,
int offset)

Constructs a parameter set for RC2 from the given effective key size
(in bits) and IV.

---

#### Constructor Summary

Constructs a parameter set for RC2 from the given effective key size
(in bits).

Constructs a parameter set for RC2 from the given effective key size
(in bits) and an 8-byte IV.

Constructs a parameter set for RC2 from the given effective key size
(in bits) and IV.

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

int

getEffectiveKeyBits

()

Returns the effective key size in bits.

byte[]

getIV

()

Returns the IV or null if this parameter set does not contain an IV.

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

Returns the effective key size in bits.

Returns the IV or null if this parameter set does not contain an IV.

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

- RC2ParameterSpec

```java
public RC2ParameterSpec​(int effectiveKeyBits)
```

Constructs a parameter set for RC2 from the given effective key size
(in bits).

**Parameters:** effectiveKeyBits

- the effective key size in bits.

- RC2ParameterSpec

```java
public RC2ParameterSpec​(int effectiveKeyBits,
byte[] iv)
```

Constructs a parameter set for RC2 from the given effective key size
(in bits) and an 8-byte IV.

The bytes that constitute the IV are those between

iv[0]

and

iv[7]

inclusive.

**Parameters:** effectiveKeyBits

- the effective key size in bits.
**Parameters:** iv

- the buffer with the 8-byte IV. The first 8 bytes of
the buffer are copied to protect against subsequent modification.
**Throws:** IllegalArgumentException

- if

iv

is null.

- RC2ParameterSpec

```java
public RC2ParameterSpec​(int effectiveKeyBits,
byte[] iv,
int offset)
```

Constructs a parameter set for RC2 from the given effective key size
(in bits) and IV.

The IV is taken from

iv

, starting at

offset

inclusive.
The bytes that constitute the IV are those between

iv[offset]

and

iv[offset+7]

inclusive.

**Parameters:** effectiveKeyBits

- the effective key size in bits.
**Parameters:** iv

- the buffer with the IV. The first 8 bytes
of the buffer beginning at

offset

inclusive
are copied to protect against subsequent modification.
**Parameters:** offset

- the offset in

iv

where the 8-byte IV
starts.
**Throws:** IllegalArgumentException

- if

iv

is null.

============ METHOD DETAIL ==========

- Method Detail

- getEffectiveKeyBits

```java
public int getEffectiveKeyBits()
```

Returns the effective key size in bits.

**Returns:** the effective key size in bits.

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
object. Two RC2ParameterSpec objects are considered equal if their
effective key sizes and IVs are equal.
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

- RC2ParameterSpec

```java
public RC2ParameterSpec​(int effectiveKeyBits)
```

Constructs a parameter set for RC2 from the given effective key size
(in bits).

**Parameters:** effectiveKeyBits

- the effective key size in bits.

- RC2ParameterSpec

```java
public RC2ParameterSpec​(int effectiveKeyBits,
byte[] iv)
```

Constructs a parameter set for RC2 from the given effective key size
(in bits) and an 8-byte IV.

The bytes that constitute the IV are those between

iv[0]

and

iv[7]

inclusive.

**Parameters:** effectiveKeyBits

- the effective key size in bits.
**Parameters:** iv

- the buffer with the 8-byte IV. The first 8 bytes of
the buffer are copied to protect against subsequent modification.
**Throws:** IllegalArgumentException

- if

iv

is null.

- RC2ParameterSpec

```java
public RC2ParameterSpec​(int effectiveKeyBits,
byte[] iv,
int offset)
```

Constructs a parameter set for RC2 from the given effective key size
(in bits) and IV.

The IV is taken from

iv

, starting at

offset

inclusive.
The bytes that constitute the IV are those between

iv[offset]

and

iv[offset+7]

inclusive.

**Parameters:** effectiveKeyBits

- the effective key size in bits.
**Parameters:** iv

- the buffer with the IV. The first 8 bytes
of the buffer beginning at

offset

inclusive
are copied to protect against subsequent modification.
**Parameters:** offset

- the offset in

iv

where the 8-byte IV
starts.
**Throws:** IllegalArgumentException

- if

iv

is null.

---

#### Constructor Detail

RC2ParameterSpec

```java
public RC2ParameterSpec​(int effectiveKeyBits)
```

Constructs a parameter set for RC2 from the given effective key size
(in bits).

**Parameters:** effectiveKeyBits

- the effective key size in bits.

---

#### RC2ParameterSpec

public RC2ParameterSpec​(int effectiveKeyBits)

Constructs a parameter set for RC2 from the given effective key size
(in bits).

RC2ParameterSpec

```java
public RC2ParameterSpec​(int effectiveKeyBits,
byte[] iv)
```

Constructs a parameter set for RC2 from the given effective key size
(in bits) and an 8-byte IV.

The bytes that constitute the IV are those between

iv[0]

and

iv[7]

inclusive.

**Parameters:** effectiveKeyBits

- the effective key size in bits.
**Parameters:** iv

- the buffer with the 8-byte IV. The first 8 bytes of
the buffer are copied to protect against subsequent modification.
**Throws:** IllegalArgumentException

- if

iv

is null.

---

#### RC2ParameterSpec

public RC2ParameterSpec​(int effectiveKeyBits,
byte[] iv)

Constructs a parameter set for RC2 from the given effective key size
(in bits) and an 8-byte IV.

The bytes that constitute the IV are those between

iv[0]

and

iv[7]

inclusive.

The bytes that constitute the IV are those between

iv[0]

and

iv[7]

inclusive.

RC2ParameterSpec

```java
public RC2ParameterSpec​(int effectiveKeyBits,
byte[] iv,
int offset)
```

Constructs a parameter set for RC2 from the given effective key size
(in bits) and IV.

The IV is taken from

iv

, starting at

offset

inclusive.
The bytes that constitute the IV are those between

iv[offset]

and

iv[offset+7]

inclusive.

**Parameters:** effectiveKeyBits

- the effective key size in bits.
**Parameters:** iv

- the buffer with the IV. The first 8 bytes
of the buffer beginning at

offset

inclusive
are copied to protect against subsequent modification.
**Parameters:** offset

- the offset in

iv

where the 8-byte IV
starts.
**Throws:** IllegalArgumentException

- if

iv

is null.

---

#### RC2ParameterSpec

public RC2ParameterSpec​(int effectiveKeyBits,
byte[] iv,
int offset)

Constructs a parameter set for RC2 from the given effective key size
(in bits) and IV.

The IV is taken from

iv

, starting at

offset

inclusive.
The bytes that constitute the IV are those between

iv[offset]

and

iv[offset+7]

inclusive.

The IV is taken from

iv

, starting at

offset

inclusive.
The bytes that constitute the IV are those between

iv[offset]

and

iv[offset+7]

inclusive.

Method Detail

- getEffectiveKeyBits

```java
public int getEffectiveKeyBits()
```

Returns the effective key size in bits.

**Returns:** the effective key size in bits.

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
object. Two RC2ParameterSpec objects are considered equal if their
effective key sizes and IVs are equal.
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

getEffectiveKeyBits

```java
public int getEffectiveKeyBits()
```

Returns the effective key size in bits.

**Returns:** the effective key size in bits.

---

#### getEffectiveKeyBits

public int getEffectiveKeyBits()

Returns the effective key size in bits.

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
object. Two RC2ParameterSpec objects are considered equal if their
effective key sizes and IVs are equal.
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
object. Two RC2ParameterSpec objects are considered equal if their
effective key sizes and IVs are equal.
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

