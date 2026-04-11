# Class IvParameterSpec

**Source:** `java.base\javax\crypto\spec\IvParameterSpec.html`

### Class Description

```java
public class
IvParameterSpec

extends
Object

implements
AlgorithmParameterSpec
```

This class specifies an

initialization vector

(IV).
Examples which use IVs are ciphers in feedback mode,
e.g., DES in CBC mode and RSA ciphers with OAEP encoding
operation.

**All Implemented Interfaces:** AlgorithmParameterSpec

---

### Field Details

*No entries found.*

### Constructor Details

#### public IvParameterSpec​(byte[] iv)

Creates an IvParameterSpec object using the bytes in

iv

as the IV.

**Parameters:**
- iv

- the buffer with the IV. The contents of the
buffer are copied to protect against subsequent modification.

**Throws:**
- NullPointerException

- if

iv

is

null

---

#### public IvParameterSpec​(byte[] iv,
int offset,
int len)

Creates an IvParameterSpec object using the first

len

bytes in

iv

, beginning at

offset

inclusive, as the IV.

The bytes that constitute the IV are those between

iv[offset]

and

iv[offset+len-1]

inclusive.

**Parameters:**
- iv

- the buffer with the IV. The first

len

bytes of the buffer beginning at

offset

inclusive
are copied to protect against subsequent modification.
- offset

- the offset in

iv

where the IV
starts.
- len

- the number of IV bytes.

**Throws:**
- IllegalArgumentException

- if

iv

is

null

or

(iv.length - offset < len)
- ArrayIndexOutOfBoundsException

- is thrown if

offset

or

len

index bytes outside the

iv

.

---

### Method Details

#### public byte[] getIV()

Returns the initialization vector (IV).

**Returns:**
- the initialization vector (IV). Returns a new array
each time this method is called.

---

### Additional Sections

#### Class IvParameterSpec

java.lang.Object

- javax.crypto.spec.IvParameterSpec

javax.crypto.spec.IvParameterSpec

**All Implemented Interfaces:** AlgorithmParameterSpec

```java
public class
IvParameterSpec

extends
Object

implements
AlgorithmParameterSpec
```

This class specifies an

initialization vector

(IV).
Examples which use IVs are ciphers in feedback mode,
e.g., DES in CBC mode and RSA ciphers with OAEP encoding
operation.

**Since:** 1.4

public class

IvParameterSpec

extends

Object

implements

AlgorithmParameterSpec

This class specifies an

initialization vector

(IV).
Examples which use IVs are ciphers in feedback mode,
e.g., DES in CBC mode and RSA ciphers with OAEP encoding
operation.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

IvParameterSpec

​(byte[] iv)

Creates an IvParameterSpec object using the bytes in

iv

as the IV.

IvParameterSpec

​(byte[] iv,
int offset,
int len)

Creates an IvParameterSpec object using the first

len

bytes in

iv

, beginning at

offset

inclusive, as the IV.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

byte[]

getIV

()

Returns the initialization vector (IV).

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

IvParameterSpec

​(byte[] iv)

Creates an IvParameterSpec object using the bytes in

iv

as the IV.

IvParameterSpec

​(byte[] iv,
int offset,
int len)

Creates an IvParameterSpec object using the first

len

bytes in

iv

, beginning at

offset

inclusive, as the IV.

---

#### Constructor Summary

Creates an IvParameterSpec object using the bytes in

iv

as the IV.

Creates an IvParameterSpec object using the first

len

bytes in

iv

, beginning at

offset

inclusive, as the IV.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

byte[]

getIV

()

Returns the initialization vector (IV).

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

Returns the initialization vector (IV).

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

- IvParameterSpec

```java
public IvParameterSpec​(byte[] iv)
```

Creates an IvParameterSpec object using the bytes in

iv

as the IV.

**Parameters:** iv

- the buffer with the IV. The contents of the
buffer are copied to protect against subsequent modification.
**Throws:** NullPointerException

- if

iv

is

null

- IvParameterSpec

```java
public IvParameterSpec​(byte[] iv,
int offset,
int len)
```

Creates an IvParameterSpec object using the first

len

bytes in

iv

, beginning at

offset

inclusive, as the IV.

The bytes that constitute the IV are those between

iv[offset]

and

iv[offset+len-1]

inclusive.

**Parameters:** iv

- the buffer with the IV. The first

len

bytes of the buffer beginning at

offset

inclusive
are copied to protect against subsequent modification.
**Parameters:** offset

- the offset in

iv

where the IV
starts.
**Parameters:** len

- the number of IV bytes.
**Throws:** IllegalArgumentException

- if

iv

is

null

or

(iv.length - offset < len)
**Throws:** ArrayIndexOutOfBoundsException

- is thrown if

offset

or

len

index bytes outside the

iv

.

============ METHOD DETAIL ==========

- Method Detail

- getIV

```java
public byte[] getIV()
```

Returns the initialization vector (IV).

**Returns:** the initialization vector (IV). Returns a new array
each time this method is called.

Constructor Detail

- IvParameterSpec

```java
public IvParameterSpec​(byte[] iv)
```

Creates an IvParameterSpec object using the bytes in

iv

as the IV.

**Parameters:** iv

- the buffer with the IV. The contents of the
buffer are copied to protect against subsequent modification.
**Throws:** NullPointerException

- if

iv

is

null

- IvParameterSpec

```java
public IvParameterSpec​(byte[] iv,
int offset,
int len)
```

Creates an IvParameterSpec object using the first

len

bytes in

iv

, beginning at

offset

inclusive, as the IV.

The bytes that constitute the IV are those between

iv[offset]

and

iv[offset+len-1]

inclusive.

**Parameters:** iv

- the buffer with the IV. The first

len

bytes of the buffer beginning at

offset

inclusive
are copied to protect against subsequent modification.
**Parameters:** offset

- the offset in

iv

where the IV
starts.
**Parameters:** len

- the number of IV bytes.
**Throws:** IllegalArgumentException

- if

iv

is

null

or

(iv.length - offset < len)
**Throws:** ArrayIndexOutOfBoundsException

- is thrown if

offset

or

len

index bytes outside the

iv

.

---

#### Constructor Detail

IvParameterSpec

```java
public IvParameterSpec​(byte[] iv)
```

Creates an IvParameterSpec object using the bytes in

iv

as the IV.

**Parameters:** iv

- the buffer with the IV. The contents of the
buffer are copied to protect against subsequent modification.
**Throws:** NullPointerException

- if

iv

is

null

---

#### IvParameterSpec

public IvParameterSpec​(byte[] iv)

Creates an IvParameterSpec object using the bytes in

iv

as the IV.

IvParameterSpec

```java
public IvParameterSpec​(byte[] iv,
int offset,
int len)
```

Creates an IvParameterSpec object using the first

len

bytes in

iv

, beginning at

offset

inclusive, as the IV.

The bytes that constitute the IV are those between

iv[offset]

and

iv[offset+len-1]

inclusive.

**Parameters:** iv

- the buffer with the IV. The first

len

bytes of the buffer beginning at

offset

inclusive
are copied to protect against subsequent modification.
**Parameters:** offset

- the offset in

iv

where the IV
starts.
**Parameters:** len

- the number of IV bytes.
**Throws:** IllegalArgumentException

- if

iv

is

null

or

(iv.length - offset < len)
**Throws:** ArrayIndexOutOfBoundsException

- is thrown if

offset

or

len

index bytes outside the

iv

.

---

#### IvParameterSpec

public IvParameterSpec​(byte[] iv,
int offset,
int len)

Creates an IvParameterSpec object using the first

len

bytes in

iv

, beginning at

offset

inclusive, as the IV.

The bytes that constitute the IV are those between

iv[offset]

and

iv[offset+len-1]

inclusive.

The bytes that constitute the IV are those between

iv[offset]

and

iv[offset+len-1]

inclusive.

Method Detail

- getIV

```java
public byte[] getIV()
```

Returns the initialization vector (IV).

**Returns:** the initialization vector (IV). Returns a new array
each time this method is called.

---

#### Method Detail

getIV

```java
public byte[] getIV()
```

Returns the initialization vector (IV).

**Returns:** the initialization vector (IV). Returns a new array
each time this method is called.

---

#### getIV

public byte[] getIV()

Returns the initialization vector (IV).

---

