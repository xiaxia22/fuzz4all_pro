# Class DESedeKeySpec

**Source:** `java.base\javax\crypto\spec\DESedeKeySpec.html`

### Class Description

```java
public class
DESedeKeySpec

extends
Object

implements
KeySpec
```

This class specifies a DES-EDE ("triple-DES") key.

**All Implemented Interfaces:** KeySpec

---

### Field Details

#### public static final int DES_EDE_KEY_LEN

The constant which defines the length of a DESede key in bytes.

**See Also:**
- Constant Field Values

---

### Constructor Details

#### public DESedeKeySpec​(byte[] key)
throws
InvalidKeyException

Creates a DESedeKeySpec object using the first 24 bytes in

key

as the key material for the DES-EDE key.

The bytes that constitute the DES-EDE key are those between

key[0]

and

key[23]

inclusive

**Parameters:**
- key

- the buffer with the DES-EDE key material. The first
24 bytes of the buffer are copied to protect against subsequent
modification.

**Throws:**
- NullPointerException

- if

key

is null.
- InvalidKeyException

- if the given key material is shorter
than 24 bytes.

---

#### public DESedeKeySpec​(byte[] key,
int offset)
throws
InvalidKeyException

Creates a DESedeKeySpec object using the first 24 bytes in

key

, beginning at

offset

inclusive,
as the key material for the DES-EDE key.

The bytes that constitute the DES-EDE key are those between

key[offset]

and

key[offset+23]

inclusive.

**Parameters:**
- key

- the buffer with the DES-EDE key material. The first
24 bytes of the buffer beginning at

offset

inclusive
are copied to protect against subsequent modification.
- offset

- the offset in

key

, where the DES-EDE key
material starts.

**Throws:**
- NullPointerException

- if

key

is null.
- InvalidKeyException

- if the given key material, starting at

offset

inclusive, is shorter than 24 bytes

---

### Method Details

#### public byte[] getKey()

Returns the DES-EDE key.

**Returns:**
- the DES-EDE key. Returns a new array
each time this method is called.

---

#### public static boolean isParityAdjusted​(byte[] key,
int offset)
throws
InvalidKeyException

Checks if the given DES-EDE key, starting at

offset

inclusive, is parity-adjusted.

**Parameters:**
- key

- a byte array which holds the key value
- offset

- the offset into the byte array

**Returns:**
- true if the given DES-EDE key is parity-adjusted, false
otherwise

**Throws:**
- NullPointerException

- if

key

is null.
- InvalidKeyException

- if the given key material, starting at

offset

inclusive, is shorter than 24 bytes

---

### Additional Sections

#### Class DESedeKeySpec

java.lang.Object

- javax.crypto.spec.DESedeKeySpec

javax.crypto.spec.DESedeKeySpec

**All Implemented Interfaces:** KeySpec

```java
public class
DESedeKeySpec

extends
Object

implements
KeySpec
```

This class specifies a DES-EDE ("triple-DES") key.

**Since:** 1.4

public class

DESedeKeySpec

extends

Object

implements

KeySpec

This class specifies a DES-EDE ("triple-DES") key.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static int

DES_EDE_KEY_LEN

The constant which defines the length of a DESede key in bytes.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

DESedeKeySpec

​(byte[] key)

Creates a DESedeKeySpec object using the first 24 bytes in

key

as the key material for the DES-EDE key.

DESedeKeySpec

​(byte[] key,
int offset)

Creates a DESedeKeySpec object using the first 24 bytes in

key

, beginning at

offset

inclusive,
as the key material for the DES-EDE key.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

byte[]

getKey

()

Returns the DES-EDE key.

static boolean

isParityAdjusted

​(byte[] key,
int offset)

Checks if the given DES-EDE key, starting at

offset

inclusive, is parity-adjusted.

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

Field Summary

Fields

Modifier and Type

Field

Description

static int

DES_EDE_KEY_LEN

The constant which defines the length of a DESede key in bytes.

---

#### Field Summary

The constant which defines the length of a DESede key in bytes.

Constructor Summary

Constructors

Constructor

Description

DESedeKeySpec

​(byte[] key)

Creates a DESedeKeySpec object using the first 24 bytes in

key

as the key material for the DES-EDE key.

DESedeKeySpec

​(byte[] key,
int offset)

Creates a DESedeKeySpec object using the first 24 bytes in

key

, beginning at

offset

inclusive,
as the key material for the DES-EDE key.

---

#### Constructor Summary

Creates a DESedeKeySpec object using the first 24 bytes in

key

as the key material for the DES-EDE key.

Creates a DESedeKeySpec object using the first 24 bytes in

key

, beginning at

offset

inclusive,
as the key material for the DES-EDE key.

Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

byte[]

getKey

()

Returns the DES-EDE key.

static boolean

isParityAdjusted

​(byte[] key,
int offset)

Checks if the given DES-EDE key, starting at

offset

inclusive, is parity-adjusted.

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

Returns the DES-EDE key.

Checks if the given DES-EDE key, starting at

offset

inclusive, is parity-adjusted.

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

============ FIELD DETAIL ===========

- Field Detail

- DES_EDE_KEY_LEN

```java
public static final int DES_EDE_KEY_LEN
```

The constant which defines the length of a DESede key in bytes.

**See Also:** Constant Field Values

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- DESedeKeySpec

```java
public DESedeKeySpec​(byte[] key)
throws
InvalidKeyException
```

Creates a DESedeKeySpec object using the first 24 bytes in

key

as the key material for the DES-EDE key.

The bytes that constitute the DES-EDE key are those between

key[0]

and

key[23]

inclusive

**Parameters:** key

- the buffer with the DES-EDE key material. The first
24 bytes of the buffer are copied to protect against subsequent
modification.
**Throws:** NullPointerException

- if

key

is null.
**Throws:** InvalidKeyException

- if the given key material is shorter
than 24 bytes.

- DESedeKeySpec

```java
public DESedeKeySpec​(byte[] key,
int offset)
throws
InvalidKeyException
```

Creates a DESedeKeySpec object using the first 24 bytes in

key

, beginning at

offset

inclusive,
as the key material for the DES-EDE key.

The bytes that constitute the DES-EDE key are those between

key[offset]

and

key[offset+23]

inclusive.

**Parameters:** key

- the buffer with the DES-EDE key material. The first
24 bytes of the buffer beginning at

offset

inclusive
are copied to protect against subsequent modification.
**Parameters:** offset

- the offset in

key

, where the DES-EDE key
material starts.
**Throws:** NullPointerException

- if

key

is null.
**Throws:** InvalidKeyException

- if the given key material, starting at

offset

inclusive, is shorter than 24 bytes

============ METHOD DETAIL ==========

- Method Detail

- getKey

```java
public byte[] getKey()
```

Returns the DES-EDE key.

**Returns:** the DES-EDE key. Returns a new array
each time this method is called.

- isParityAdjusted

```java
public static boolean isParityAdjusted​(byte[] key,
int offset)
throws
InvalidKeyException
```

Checks if the given DES-EDE key, starting at

offset

inclusive, is parity-adjusted.

**Parameters:** key

- a byte array which holds the key value
**Parameters:** offset

- the offset into the byte array
**Returns:** true if the given DES-EDE key is parity-adjusted, false
otherwise
**Throws:** NullPointerException

- if

key

is null.
**Throws:** InvalidKeyException

- if the given key material, starting at

offset

inclusive, is shorter than 24 bytes

Field Detail

- DES_EDE_KEY_LEN

```java
public static final int DES_EDE_KEY_LEN
```

The constant which defines the length of a DESede key in bytes.

**See Also:** Constant Field Values

---

#### Field Detail

DES_EDE_KEY_LEN

```java
public static final int DES_EDE_KEY_LEN
```

The constant which defines the length of a DESede key in bytes.

**See Also:** Constant Field Values

---

#### DES_EDE_KEY_LEN

public static final int DES_EDE_KEY_LEN

The constant which defines the length of a DESede key in bytes.

Constructor Detail

- DESedeKeySpec

```java
public DESedeKeySpec​(byte[] key)
throws
InvalidKeyException
```

Creates a DESedeKeySpec object using the first 24 bytes in

key

as the key material for the DES-EDE key.

The bytes that constitute the DES-EDE key are those between

key[0]

and

key[23]

inclusive

**Parameters:** key

- the buffer with the DES-EDE key material. The first
24 bytes of the buffer are copied to protect against subsequent
modification.
**Throws:** NullPointerException

- if

key

is null.
**Throws:** InvalidKeyException

- if the given key material is shorter
than 24 bytes.

- DESedeKeySpec

```java
public DESedeKeySpec​(byte[] key,
int offset)
throws
InvalidKeyException
```

Creates a DESedeKeySpec object using the first 24 bytes in

key

, beginning at

offset

inclusive,
as the key material for the DES-EDE key.

The bytes that constitute the DES-EDE key are those between

key[offset]

and

key[offset+23]

inclusive.

**Parameters:** key

- the buffer with the DES-EDE key material. The first
24 bytes of the buffer beginning at

offset

inclusive
are copied to protect against subsequent modification.
**Parameters:** offset

- the offset in

key

, where the DES-EDE key
material starts.
**Throws:** NullPointerException

- if

key

is null.
**Throws:** InvalidKeyException

- if the given key material, starting at

offset

inclusive, is shorter than 24 bytes

---

#### Constructor Detail

DESedeKeySpec

```java
public DESedeKeySpec​(byte[] key)
throws
InvalidKeyException
```

Creates a DESedeKeySpec object using the first 24 bytes in

key

as the key material for the DES-EDE key.

The bytes that constitute the DES-EDE key are those between

key[0]

and

key[23]

inclusive

**Parameters:** key

- the buffer with the DES-EDE key material. The first
24 bytes of the buffer are copied to protect against subsequent
modification.
**Throws:** NullPointerException

- if

key

is null.
**Throws:** InvalidKeyException

- if the given key material is shorter
than 24 bytes.

---

#### DESedeKeySpec

public DESedeKeySpec​(byte[] key)
throws

InvalidKeyException

Creates a DESedeKeySpec object using the first 24 bytes in

key

as the key material for the DES-EDE key.

The bytes that constitute the DES-EDE key are those between

key[0]

and

key[23]

inclusive

The bytes that constitute the DES-EDE key are those between

key[0]

and

key[23]

inclusive

DESedeKeySpec

```java
public DESedeKeySpec​(byte[] key,
int offset)
throws
InvalidKeyException
```

Creates a DESedeKeySpec object using the first 24 bytes in

key

, beginning at

offset

inclusive,
as the key material for the DES-EDE key.

The bytes that constitute the DES-EDE key are those between

key[offset]

and

key[offset+23]

inclusive.

**Parameters:** key

- the buffer with the DES-EDE key material. The first
24 bytes of the buffer beginning at

offset

inclusive
are copied to protect against subsequent modification.
**Parameters:** offset

- the offset in

key

, where the DES-EDE key
material starts.
**Throws:** NullPointerException

- if

key

is null.
**Throws:** InvalidKeyException

- if the given key material, starting at

offset

inclusive, is shorter than 24 bytes

---

#### DESedeKeySpec

public DESedeKeySpec​(byte[] key,
int offset)
throws

InvalidKeyException

Creates a DESedeKeySpec object using the first 24 bytes in

key

, beginning at

offset

inclusive,
as the key material for the DES-EDE key.

The bytes that constitute the DES-EDE key are those between

key[offset]

and

key[offset+23]

inclusive.

The bytes that constitute the DES-EDE key are those between

key[offset]

and

key[offset+23]

inclusive.

Method Detail

- getKey

```java
public byte[] getKey()
```

Returns the DES-EDE key.

**Returns:** the DES-EDE key. Returns a new array
each time this method is called.

- isParityAdjusted

```java
public static boolean isParityAdjusted​(byte[] key,
int offset)
throws
InvalidKeyException
```

Checks if the given DES-EDE key, starting at

offset

inclusive, is parity-adjusted.

**Parameters:** key

- a byte array which holds the key value
**Parameters:** offset

- the offset into the byte array
**Returns:** true if the given DES-EDE key is parity-adjusted, false
otherwise
**Throws:** NullPointerException

- if

key

is null.
**Throws:** InvalidKeyException

- if the given key material, starting at

offset

inclusive, is shorter than 24 bytes

---

#### Method Detail

getKey

```java
public byte[] getKey()
```

Returns the DES-EDE key.

**Returns:** the DES-EDE key. Returns a new array
each time this method is called.

---

#### getKey

public byte[] getKey()

Returns the DES-EDE key.

isParityAdjusted

```java
public static boolean isParityAdjusted​(byte[] key,
int offset)
throws
InvalidKeyException
```

Checks if the given DES-EDE key, starting at

offset

inclusive, is parity-adjusted.

**Parameters:** key

- a byte array which holds the key value
**Parameters:** offset

- the offset into the byte array
**Returns:** true if the given DES-EDE key is parity-adjusted, false
otherwise
**Throws:** NullPointerException

- if

key

is null.
**Throws:** InvalidKeyException

- if the given key material, starting at

offset

inclusive, is shorter than 24 bytes

---

#### isParityAdjusted

public static boolean isParityAdjusted​(byte[] key,
int offset)
throws

InvalidKeyException

Checks if the given DES-EDE key, starting at

offset

inclusive, is parity-adjusted.

---

