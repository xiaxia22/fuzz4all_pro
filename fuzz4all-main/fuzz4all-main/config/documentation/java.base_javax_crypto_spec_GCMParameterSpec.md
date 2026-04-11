# Class GCMParameterSpec

**Source:** `java.base\javax\crypto\spec\GCMParameterSpec.html`

### Class Description

```java
public class
GCMParameterSpec

extends
Object

implements
AlgorithmParameterSpec
```

Specifies the set of parameters required by a

Cipher

using the Galois/Counter Mode (GCM) mode.

Simple block cipher modes (such as CBC) generally require only an
initialization vector (such as

IvParameterSpec

),
but GCM needs these parameters:

- IV

: Initialization Vector (IV)
- tLen

: length (in bits) of authentication tag T

In addition to the parameters described here, other GCM inputs/output
(Additional Authenticated Data (AAD), Keys, block ciphers,
plain/ciphertext and authentication tags) are handled in the

Cipher

class.

Please see

RFC 5116

for more information on the Authenticated Encryption with
Associated Data (AEAD) algorithm, and

NIST Special Publication 800-38D

, "NIST Recommendation for Block
Cipher Modes of Operation: Galois/Counter Mode (GCM) and GMAC."

The GCM specification states that

tLen

may only have the
values {128, 120, 112, 104, 96}, or {64, 32} for certain
applications. Other values can be specified for this class, but not
all CSP implementations will support them.

**All Implemented Interfaces:** AlgorithmParameterSpec

---

### Field Details

*No entries found.*

### Constructor Details

#### public GCMParameterSpec​(int tLen,
byte[] src)

Constructs a GCMParameterSpec using the specified authentication
tag bit-length and IV buffer.

**Parameters:**
- tLen

- the authentication tag length (in bits)
- src

- the IV source buffer. The contents of the buffer are
copied to protect against subsequent modification.

**Throws:**
- IllegalArgumentException

- if

tLen

is negative,
or

src

is null.

---

#### public GCMParameterSpec​(int tLen,
byte[] src,
int offset,
int len)

Constructs a GCMParameterSpec object using the specified
authentication tag bit-length and a subset of the specified
buffer as the IV.

**Parameters:**
- tLen

- the authentication tag length (in bits)
- src

- the IV source buffer. The contents of the
buffer are copied to protect against subsequent modification.
- offset

- the offset in

src

where the IV starts
- len

- the number of IV bytes

**Throws:**
- IllegalArgumentException

- if

tLen

is negative,

src

is null,

len

or

offset

is negative,
or the sum of

offset

and

len

is greater than the
length of the

src

byte array.

---

### Method Details

#### public int getTLen()

Returns the authentication tag length.

**Returns:**
- the authentication tag length (in bits)

---

#### public byte[] getIV()

Returns the Initialization Vector (IV).

**Returns:**
- the IV. Creates a new array each time this method
is called.

---

### Additional Sections

#### Class GCMParameterSpec

java.lang.Object

- javax.crypto.spec.GCMParameterSpec

javax.crypto.spec.GCMParameterSpec

**All Implemented Interfaces:** AlgorithmParameterSpec

```java
public class
GCMParameterSpec

extends
Object

implements
AlgorithmParameterSpec
```

Specifies the set of parameters required by a

Cipher

using the Galois/Counter Mode (GCM) mode.

Simple block cipher modes (such as CBC) generally require only an
initialization vector (such as

IvParameterSpec

),
but GCM needs these parameters:

- IV

: Initialization Vector (IV)
- tLen

: length (in bits) of authentication tag T

In addition to the parameters described here, other GCM inputs/output
(Additional Authenticated Data (AAD), Keys, block ciphers,
plain/ciphertext and authentication tags) are handled in the

Cipher

class.

Please see

RFC 5116

for more information on the Authenticated Encryption with
Associated Data (AEAD) algorithm, and

NIST Special Publication 800-38D

, "NIST Recommendation for Block
Cipher Modes of Operation: Galois/Counter Mode (GCM) and GMAC."

The GCM specification states that

tLen

may only have the
values {128, 120, 112, 104, 96}, or {64, 32} for certain
applications. Other values can be specified for this class, but not
all CSP implementations will support them.

**Since:** 1.7
**See Also:** Cipher

public class

GCMParameterSpec

extends

Object

implements

AlgorithmParameterSpec

Specifies the set of parameters required by a

Cipher

using the Galois/Counter Mode (GCM) mode.

Simple block cipher modes (such as CBC) generally require only an
initialization vector (such as

IvParameterSpec

),
but GCM needs these parameters:

- IV

: Initialization Vector (IV)
- tLen

: length (in bits) of authentication tag T

In addition to the parameters described here, other GCM inputs/output
(Additional Authenticated Data (AAD), Keys, block ciphers,
plain/ciphertext and authentication tags) are handled in the

Cipher

class.

Please see

RFC 5116

for more information on the Authenticated Encryption with
Associated Data (AEAD) algorithm, and

NIST Special Publication 800-38D

, "NIST Recommendation for Block
Cipher Modes of Operation: Galois/Counter Mode (GCM) and GMAC."

The GCM specification states that

tLen

may only have the
values {128, 120, 112, 104, 96}, or {64, 32} for certain
applications. Other values can be specified for this class, but not
all CSP implementations will support them.

Simple block cipher modes (such as CBC) generally require only an
initialization vector (such as

IvParameterSpec

),
but GCM needs these parameters:

- IV

: Initialization Vector (IV)
- tLen

: length (in bits) of authentication tag T

In addition to the parameters described here, other GCM inputs/output
(Additional Authenticated Data (AAD), Keys, block ciphers,
plain/ciphertext and authentication tags) are handled in the

Cipher

class.

Please see

RFC 5116

for more information on the Authenticated Encryption with
Associated Data (AEAD) algorithm, and

NIST Special Publication 800-38D

, "NIST Recommendation for Block
Cipher Modes of Operation: Galois/Counter Mode (GCM) and GMAC."

The GCM specification states that

tLen

may only have the
values {128, 120, 112, 104, 96}, or {64, 32} for certain
applications. Other values can be specified for this class, but not
all CSP implementations will support them.

IV

: Initialization Vector (IV)

tLen

: length (in bits) of authentication tag T

In addition to the parameters described here, other GCM inputs/output
(Additional Authenticated Data (AAD), Keys, block ciphers,
plain/ciphertext and authentication tags) are handled in the

Cipher

class.

Please see

RFC 5116

for more information on the Authenticated Encryption with
Associated Data (AEAD) algorithm, and

NIST Special Publication 800-38D

, "NIST Recommendation for Block
Cipher Modes of Operation: Galois/Counter Mode (GCM) and GMAC."

The GCM specification states that

tLen

may only have the
values {128, 120, 112, 104, 96}, or {64, 32} for certain
applications. Other values can be specified for this class, but not
all CSP implementations will support them.

Please see

RFC 5116

for more information on the Authenticated Encryption with
Associated Data (AEAD) algorithm, and

NIST Special Publication 800-38D

, "NIST Recommendation for Block
Cipher Modes of Operation: Galois/Counter Mode (GCM) and GMAC."

The GCM specification states that

tLen

may only have the
values {128, 120, 112, 104, 96}, or {64, 32} for certain
applications. Other values can be specified for this class, but not
all CSP implementations will support them.

The GCM specification states that

tLen

may only have the
values {128, 120, 112, 104, 96}, or {64, 32} for certain
applications. Other values can be specified for this class, but not
all CSP implementations will support them.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

GCMParameterSpec

​(int tLen,
byte[] src)

Constructs a GCMParameterSpec using the specified authentication
tag bit-length and IV buffer.

GCMParameterSpec

​(int tLen,
byte[] src,
int offset,
int len)

Constructs a GCMParameterSpec object using the specified
authentication tag bit-length and a subset of the specified
buffer as the IV.

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

Returns the Initialization Vector (IV).

int

getTLen

()

Returns the authentication tag length.

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

GCMParameterSpec

​(int tLen,
byte[] src)

Constructs a GCMParameterSpec using the specified authentication
tag bit-length and IV buffer.

GCMParameterSpec

​(int tLen,
byte[] src,
int offset,
int len)

Constructs a GCMParameterSpec object using the specified
authentication tag bit-length and a subset of the specified
buffer as the IV.

---

#### Constructor Summary

Constructs a GCMParameterSpec using the specified authentication
tag bit-length and IV buffer.

Constructs a GCMParameterSpec object using the specified
authentication tag bit-length and a subset of the specified
buffer as the IV.

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

Returns the Initialization Vector (IV).

int

getTLen

()

Returns the authentication tag length.

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

Returns the Initialization Vector (IV).

Returns the authentication tag length.

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

- GCMParameterSpec

```java
public GCMParameterSpec​(int tLen,
byte[] src)
```

Constructs a GCMParameterSpec using the specified authentication
tag bit-length and IV buffer.

**Parameters:** tLen

- the authentication tag length (in bits)
**Parameters:** src

- the IV source buffer. The contents of the buffer are
copied to protect against subsequent modification.
**Throws:** IllegalArgumentException

- if

tLen

is negative,
or

src

is null.

- GCMParameterSpec

```java
public GCMParameterSpec​(int tLen,
byte[] src,
int offset,
int len)
```

Constructs a GCMParameterSpec object using the specified
authentication tag bit-length and a subset of the specified
buffer as the IV.

**Parameters:** tLen

- the authentication tag length (in bits)
**Parameters:** src

- the IV source buffer. The contents of the
buffer are copied to protect against subsequent modification.
**Parameters:** offset

- the offset in

src

where the IV starts
**Parameters:** len

- the number of IV bytes
**Throws:** IllegalArgumentException

- if

tLen

is negative,

src

is null,

len

or

offset

is negative,
or the sum of

offset

and

len

is greater than the
length of the

src

byte array.

============ METHOD DETAIL ==========

- Method Detail

- getTLen

```java
public int getTLen()
```

Returns the authentication tag length.

**Returns:** the authentication tag length (in bits)

- getIV

```java
public byte[] getIV()
```

Returns the Initialization Vector (IV).

**Returns:** the IV. Creates a new array each time this method
is called.

Constructor Detail

- GCMParameterSpec

```java
public GCMParameterSpec​(int tLen,
byte[] src)
```

Constructs a GCMParameterSpec using the specified authentication
tag bit-length and IV buffer.

**Parameters:** tLen

- the authentication tag length (in bits)
**Parameters:** src

- the IV source buffer. The contents of the buffer are
copied to protect against subsequent modification.
**Throws:** IllegalArgumentException

- if

tLen

is negative,
or

src

is null.

- GCMParameterSpec

```java
public GCMParameterSpec​(int tLen,
byte[] src,
int offset,
int len)
```

Constructs a GCMParameterSpec object using the specified
authentication tag bit-length and a subset of the specified
buffer as the IV.

**Parameters:** tLen

- the authentication tag length (in bits)
**Parameters:** src

- the IV source buffer. The contents of the
buffer are copied to protect against subsequent modification.
**Parameters:** offset

- the offset in

src

where the IV starts
**Parameters:** len

- the number of IV bytes
**Throws:** IllegalArgumentException

- if

tLen

is negative,

src

is null,

len

or

offset

is negative,
or the sum of

offset

and

len

is greater than the
length of the

src

byte array.

---

#### Constructor Detail

GCMParameterSpec

```java
public GCMParameterSpec​(int tLen,
byte[] src)
```

Constructs a GCMParameterSpec using the specified authentication
tag bit-length and IV buffer.

**Parameters:** tLen

- the authentication tag length (in bits)
**Parameters:** src

- the IV source buffer. The contents of the buffer are
copied to protect against subsequent modification.
**Throws:** IllegalArgumentException

- if

tLen

is negative,
or

src

is null.

---

#### GCMParameterSpec

public GCMParameterSpec​(int tLen,
byte[] src)

Constructs a GCMParameterSpec using the specified authentication
tag bit-length and IV buffer.

GCMParameterSpec

```java
public GCMParameterSpec​(int tLen,
byte[] src,
int offset,
int len)
```

Constructs a GCMParameterSpec object using the specified
authentication tag bit-length and a subset of the specified
buffer as the IV.

**Parameters:** tLen

- the authentication tag length (in bits)
**Parameters:** src

- the IV source buffer. The contents of the
buffer are copied to protect against subsequent modification.
**Parameters:** offset

- the offset in

src

where the IV starts
**Parameters:** len

- the number of IV bytes
**Throws:** IllegalArgumentException

- if

tLen

is negative,

src

is null,

len

or

offset

is negative,
or the sum of

offset

and

len

is greater than the
length of the

src

byte array.

---

#### GCMParameterSpec

public GCMParameterSpec​(int tLen,
byte[] src,
int offset,
int len)

Constructs a GCMParameterSpec object using the specified
authentication tag bit-length and a subset of the specified
buffer as the IV.

Method Detail

- getTLen

```java
public int getTLen()
```

Returns the authentication tag length.

**Returns:** the authentication tag length (in bits)

- getIV

```java
public byte[] getIV()
```

Returns the Initialization Vector (IV).

**Returns:** the IV. Creates a new array each time this method
is called.

---

#### Method Detail

getTLen

```java
public int getTLen()
```

Returns the authentication tag length.

**Returns:** the authentication tag length (in bits)

---

#### getTLen

public int getTLen()

Returns the authentication tag length.

getIV

```java
public byte[] getIV()
```

Returns the Initialization Vector (IV).

**Returns:** the IV. Creates a new array each time this method
is called.

---

#### getIV

public byte[] getIV()

Returns the Initialization Vector (IV).

---

