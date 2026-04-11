# Class DESKeySpec

**Source:** `java.base\javax\crypto\spec\DESKeySpec.html`

### Class Description

```java
public class
DESKeySpec

extends
Object

implements
KeySpec
```

This class specifies a DES key.

**All Implemented Interfaces:** KeySpec

---

### Field Details

#### public static final int DES_KEY_LEN

The constant which defines the length of a DES key in bytes.

**See Also:**
- Constant Field Values

---

### Constructor Details

#### public DESKeySpec​(byte[] key)
throws
InvalidKeyException

Creates a DESKeySpec object using the first 8 bytes in

key

as the key material for the DES key.

The bytes that constitute the DES key are those between

key[0]

and

key[7]

inclusive.

**Parameters:**
- key

- the buffer with the DES key material. The first 8 bytes
of the buffer are copied to protect against subsequent modification.

**Throws:**
- NullPointerException

- if the given key material is

null
- InvalidKeyException

- if the given key material is shorter
than 8 bytes.

---

#### public DESKeySpec​(byte[] key,
int offset)
throws
InvalidKeyException

Creates a DESKeySpec object using the first 8 bytes in

key

, beginning at

offset

inclusive,
as the key material for the DES key.

The bytes that constitute the DES key are those between

key[offset]

and

key[offset+7]

inclusive.

**Parameters:**
- key

- the buffer with the DES key material. The first 8 bytes
of the buffer beginning at

offset

inclusive are copied
to protect against subsequent modification.
- offset

- the offset in

key

, where the DES key
material starts.

**Throws:**
- NullPointerException

- if the given key material is

null
- InvalidKeyException

- if the given key material, starting at

offset

inclusive, is shorter than 8 bytes.

---

### Method Details

#### public byte[] getKey()

Returns the DES key material.

**Returns:**
- the DES key material. Returns a new array
each time this method is called.

---

#### public static boolean isParityAdjusted​(byte[] key,
int offset)
throws
InvalidKeyException

Checks if the given DES key material, starting at

offset

inclusive, is parity-adjusted.

**Parameters:**
- key

- the buffer with the DES key material.
- offset

- the offset in

key

, where the DES key
material starts.

**Returns:**
- true if the given DES key material is parity-adjusted, false
otherwise.

**Throws:**
- InvalidKeyException

- if the given key material is

null

, or starting at

offset

inclusive, is
shorter than 8 bytes.

---

#### public static boolean isWeak​(byte[] key,
int offset)
throws
InvalidKeyException

Checks if the given DES key material is weak or semi-weak.

**Parameters:**
- key

- the buffer with the DES key material.
- offset

- the offset in

key

, where the DES key
material starts.

**Returns:**
- true if the given DES key material is weak or semi-weak, false
otherwise.

**Throws:**
- InvalidKeyException

- if the given key material is

null

, or starting at

offset

inclusive, is
shorter than 8 bytes.

---

### Additional Sections

#### Class DESKeySpec

java.lang.Object

- javax.crypto.spec.DESKeySpec

javax.crypto.spec.DESKeySpec

**All Implemented Interfaces:** KeySpec

```java
public class
DESKeySpec

extends
Object

implements
KeySpec
```

This class specifies a DES key.

**Since:** 1.4

public class

DESKeySpec

extends

Object

implements

KeySpec

This class specifies a DES key.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static int

DES_KEY_LEN

The constant which defines the length of a DES key in bytes.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

DESKeySpec

​(byte[] key)

Creates a DESKeySpec object using the first 8 bytes in

key

as the key material for the DES key.

DESKeySpec

​(byte[] key,
int offset)

Creates a DESKeySpec object using the first 8 bytes in

key

, beginning at

offset

inclusive,
as the key material for the DES key.

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

Returns the DES key material.

static boolean

isParityAdjusted

​(byte[] key,
int offset)

Checks if the given DES key material, starting at

offset

inclusive, is parity-adjusted.

static boolean

isWeak

​(byte[] key,
int offset)

Checks if the given DES key material is weak or semi-weak.

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

DES_KEY_LEN

The constant which defines the length of a DES key in bytes.

---

#### Field Summary

The constant which defines the length of a DES key in bytes.

Constructor Summary

Constructors

Constructor

Description

DESKeySpec

​(byte[] key)

Creates a DESKeySpec object using the first 8 bytes in

key

as the key material for the DES key.

DESKeySpec

​(byte[] key,
int offset)

Creates a DESKeySpec object using the first 8 bytes in

key

, beginning at

offset

inclusive,
as the key material for the DES key.

---

#### Constructor Summary

Creates a DESKeySpec object using the first 8 bytes in

key

as the key material for the DES key.

Creates a DESKeySpec object using the first 8 bytes in

key

, beginning at

offset

inclusive,
as the key material for the DES key.

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

Returns the DES key material.

static boolean

isParityAdjusted

​(byte[] key,
int offset)

Checks if the given DES key material, starting at

offset

inclusive, is parity-adjusted.

static boolean

isWeak

​(byte[] key,
int offset)

Checks if the given DES key material is weak or semi-weak.

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

Returns the DES key material.

Checks if the given DES key material, starting at

offset

inclusive, is parity-adjusted.

Checks if the given DES key material is weak or semi-weak.

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

- DES_KEY_LEN

```java
public static final int DES_KEY_LEN
```

The constant which defines the length of a DES key in bytes.

**See Also:** Constant Field Values

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- DESKeySpec

```java
public DESKeySpec​(byte[] key)
throws
InvalidKeyException
```

Creates a DESKeySpec object using the first 8 bytes in

key

as the key material for the DES key.

The bytes that constitute the DES key are those between

key[0]

and

key[7]

inclusive.

**Parameters:** key

- the buffer with the DES key material. The first 8 bytes
of the buffer are copied to protect against subsequent modification.
**Throws:** NullPointerException

- if the given key material is

null
**Throws:** InvalidKeyException

- if the given key material is shorter
than 8 bytes.

- DESKeySpec

```java
public DESKeySpec​(byte[] key,
int offset)
throws
InvalidKeyException
```

Creates a DESKeySpec object using the first 8 bytes in

key

, beginning at

offset

inclusive,
as the key material for the DES key.

The bytes that constitute the DES key are those between

key[offset]

and

key[offset+7]

inclusive.

**Parameters:** key

- the buffer with the DES key material. The first 8 bytes
of the buffer beginning at

offset

inclusive are copied
to protect against subsequent modification.
**Parameters:** offset

- the offset in

key

, where the DES key
material starts.
**Throws:** NullPointerException

- if the given key material is

null
**Throws:** InvalidKeyException

- if the given key material, starting at

offset

inclusive, is shorter than 8 bytes.

============ METHOD DETAIL ==========

- Method Detail

- getKey

```java
public byte[] getKey()
```

Returns the DES key material.

**Returns:** the DES key material. Returns a new array
each time this method is called.

- isParityAdjusted

```java
public static boolean isParityAdjusted​(byte[] key,
int offset)
throws
InvalidKeyException
```

Checks if the given DES key material, starting at

offset

inclusive, is parity-adjusted.

**Parameters:** key

- the buffer with the DES key material.
**Parameters:** offset

- the offset in

key

, where the DES key
material starts.
**Returns:** true if the given DES key material is parity-adjusted, false
otherwise.
**Throws:** InvalidKeyException

- if the given key material is

null

, or starting at

offset

inclusive, is
shorter than 8 bytes.

- isWeak

```java
public static boolean isWeak​(byte[] key,
int offset)
throws
InvalidKeyException
```

Checks if the given DES key material is weak or semi-weak.

**Parameters:** key

- the buffer with the DES key material.
**Parameters:** offset

- the offset in

key

, where the DES key
material starts.
**Returns:** true if the given DES key material is weak or semi-weak, false
otherwise.
**Throws:** InvalidKeyException

- if the given key material is

null

, or starting at

offset

inclusive, is
shorter than 8 bytes.

Field Detail

- DES_KEY_LEN

```java
public static final int DES_KEY_LEN
```

The constant which defines the length of a DES key in bytes.

**See Also:** Constant Field Values

---

#### Field Detail

DES_KEY_LEN

```java
public static final int DES_KEY_LEN
```

The constant which defines the length of a DES key in bytes.

**See Also:** Constant Field Values

---

#### DES_KEY_LEN

public static final int DES_KEY_LEN

The constant which defines the length of a DES key in bytes.

Constructor Detail

- DESKeySpec

```java
public DESKeySpec​(byte[] key)
throws
InvalidKeyException
```

Creates a DESKeySpec object using the first 8 bytes in

key

as the key material for the DES key.

The bytes that constitute the DES key are those between

key[0]

and

key[7]

inclusive.

**Parameters:** key

- the buffer with the DES key material. The first 8 bytes
of the buffer are copied to protect against subsequent modification.
**Throws:** NullPointerException

- if the given key material is

null
**Throws:** InvalidKeyException

- if the given key material is shorter
than 8 bytes.

- DESKeySpec

```java
public DESKeySpec​(byte[] key,
int offset)
throws
InvalidKeyException
```

Creates a DESKeySpec object using the first 8 bytes in

key

, beginning at

offset

inclusive,
as the key material for the DES key.

The bytes that constitute the DES key are those between

key[offset]

and

key[offset+7]

inclusive.

**Parameters:** key

- the buffer with the DES key material. The first 8 bytes
of the buffer beginning at

offset

inclusive are copied
to protect against subsequent modification.
**Parameters:** offset

- the offset in

key

, where the DES key
material starts.
**Throws:** NullPointerException

- if the given key material is

null
**Throws:** InvalidKeyException

- if the given key material, starting at

offset

inclusive, is shorter than 8 bytes.

---

#### Constructor Detail

DESKeySpec

```java
public DESKeySpec​(byte[] key)
throws
InvalidKeyException
```

Creates a DESKeySpec object using the first 8 bytes in

key

as the key material for the DES key.

The bytes that constitute the DES key are those between

key[0]

and

key[7]

inclusive.

**Parameters:** key

- the buffer with the DES key material. The first 8 bytes
of the buffer are copied to protect against subsequent modification.
**Throws:** NullPointerException

- if the given key material is

null
**Throws:** InvalidKeyException

- if the given key material is shorter
than 8 bytes.

---

#### DESKeySpec

public DESKeySpec​(byte[] key)
throws

InvalidKeyException

Creates a DESKeySpec object using the first 8 bytes in

key

as the key material for the DES key.

The bytes that constitute the DES key are those between

key[0]

and

key[7]

inclusive.

The bytes that constitute the DES key are those between

key[0]

and

key[7]

inclusive.

DESKeySpec

```java
public DESKeySpec​(byte[] key,
int offset)
throws
InvalidKeyException
```

Creates a DESKeySpec object using the first 8 bytes in

key

, beginning at

offset

inclusive,
as the key material for the DES key.

The bytes that constitute the DES key are those between

key[offset]

and

key[offset+7]

inclusive.

**Parameters:** key

- the buffer with the DES key material. The first 8 bytes
of the buffer beginning at

offset

inclusive are copied
to protect against subsequent modification.
**Parameters:** offset

- the offset in

key

, where the DES key
material starts.
**Throws:** NullPointerException

- if the given key material is

null
**Throws:** InvalidKeyException

- if the given key material, starting at

offset

inclusive, is shorter than 8 bytes.

---

#### DESKeySpec

public DESKeySpec​(byte[] key,
int offset)
throws

InvalidKeyException

Creates a DESKeySpec object using the first 8 bytes in

key

, beginning at

offset

inclusive,
as the key material for the DES key.

The bytes that constitute the DES key are those between

key[offset]

and

key[offset+7]

inclusive.

The bytes that constitute the DES key are those between

key[offset]

and

key[offset+7]

inclusive.

Method Detail

- getKey

```java
public byte[] getKey()
```

Returns the DES key material.

**Returns:** the DES key material. Returns a new array
each time this method is called.

- isParityAdjusted

```java
public static boolean isParityAdjusted​(byte[] key,
int offset)
throws
InvalidKeyException
```

Checks if the given DES key material, starting at

offset

inclusive, is parity-adjusted.

**Parameters:** key

- the buffer with the DES key material.
**Parameters:** offset

- the offset in

key

, where the DES key
material starts.
**Returns:** true if the given DES key material is parity-adjusted, false
otherwise.
**Throws:** InvalidKeyException

- if the given key material is

null

, or starting at

offset

inclusive, is
shorter than 8 bytes.

- isWeak

```java
public static boolean isWeak​(byte[] key,
int offset)
throws
InvalidKeyException
```

Checks if the given DES key material is weak or semi-weak.

**Parameters:** key

- the buffer with the DES key material.
**Parameters:** offset

- the offset in

key

, where the DES key
material starts.
**Returns:** true if the given DES key material is weak or semi-weak, false
otherwise.
**Throws:** InvalidKeyException

- if the given key material is

null

, or starting at

offset

inclusive, is
shorter than 8 bytes.

---

#### Method Detail

getKey

```java
public byte[] getKey()
```

Returns the DES key material.

**Returns:** the DES key material. Returns a new array
each time this method is called.

---

#### getKey

public byte[] getKey()

Returns the DES key material.

isParityAdjusted

```java
public static boolean isParityAdjusted​(byte[] key,
int offset)
throws
InvalidKeyException
```

Checks if the given DES key material, starting at

offset

inclusive, is parity-adjusted.

**Parameters:** key

- the buffer with the DES key material.
**Parameters:** offset

- the offset in

key

, where the DES key
material starts.
**Returns:** true if the given DES key material is parity-adjusted, false
otherwise.
**Throws:** InvalidKeyException

- if the given key material is

null

, or starting at

offset

inclusive, is
shorter than 8 bytes.

---

#### isParityAdjusted

public static boolean isParityAdjusted​(byte[] key,
int offset)
throws

InvalidKeyException

Checks if the given DES key material, starting at

offset

inclusive, is parity-adjusted.

isWeak

```java
public static boolean isWeak​(byte[] key,
int offset)
throws
InvalidKeyException
```

Checks if the given DES key material is weak or semi-weak.

**Parameters:** key

- the buffer with the DES key material.
**Parameters:** offset

- the offset in

key

, where the DES key
material starts.
**Returns:** true if the given DES key material is weak or semi-weak, false
otherwise.
**Throws:** InvalidKeyException

- if the given key material is

null

, or starting at

offset

inclusive, is
shorter than 8 bytes.

---

#### isWeak

public static boolean isWeak​(byte[] key,
int offset)
throws

InvalidKeyException

Checks if the given DES key material is weak or semi-weak.

---

