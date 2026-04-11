# Class ByteOrder

**Source:** `java.base\java\nio\ByteOrder.html`

### Class Description

```java
public final class
ByteOrder

extends
Object
```

A typesafe enumeration for byte orders.

**Since:** 1.4

---

### Field Details

#### public static final
ByteOrder
BIG_ENDIAN

Constant denoting big-endian byte order. In this order, the bytes of a
multibyte value are ordered from most significant to least significant.

---

#### public static final
ByteOrder
LITTLE_ENDIAN

Constant denoting little-endian byte order. In this order, the bytes of
a multibyte value are ordered from least significant to most
significant.

---

### Constructor Details

*No entries found.*

### Method Details

#### public static
ByteOrder
nativeOrder()

Retrieves the native byte order of the underlying platform.

This method is defined so that performance-sensitive Java code can
allocate direct buffers with the same byte order as the hardware.
Native code libraries are often more efficient when such buffers are
used.

**Returns:**
- The native byte order of the hardware upon which this Java
virtual machine is running

---

#### public
String
toString()

Constructs a string describing this object.

This method returns the string

"BIG_ENDIAN"

for

BIG_ENDIAN

and

"LITTLE_ENDIAN"

for

LITTLE_ENDIAN

.

**Overrides:**
- toString

in class

Object

**Returns:**
- The specified string

---

### Additional Sections

#### Class ByteOrder

java.lang.Object

- java.nio.ByteOrder

java.nio.ByteOrder

```java
public final class
ByteOrder

extends
Object
```

A typesafe enumeration for byte orders.

**Since:** 1.4

public final class

ByteOrder

extends

Object

A typesafe enumeration for byte orders.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static

ByteOrder

BIG_ENDIAN

Constant denoting big-endian byte order.

static

ByteOrder

LITTLE_ENDIAN

Constant denoting little-endian byte order.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

static

ByteOrder

nativeOrder

()

Retrieves the native byte order of the underlying platform.

String

toString

()

Constructs a string describing this object.

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

static

ByteOrder

BIG_ENDIAN

Constant denoting big-endian byte order.

static

ByteOrder

LITTLE_ENDIAN

Constant denoting little-endian byte order.

---

#### Field Summary

Constant denoting big-endian byte order.

Constant denoting little-endian byte order.

Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

static

ByteOrder

nativeOrder

()

Retrieves the native byte order of the underlying platform.

String

toString

()

Constructs a string describing this object.

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

wait

,

wait

,

wait

---

#### Method Summary

Retrieves the native byte order of the underlying platform.

Constructs a string describing this object.

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

wait

,

wait

,

wait

---

#### Methods declared in class java.lang. Object

============ FIELD DETAIL ===========

- Field Detail

- BIG_ENDIAN

```java
public static final
ByteOrder
BIG_ENDIAN
```

Constant denoting big-endian byte order. In this order, the bytes of a
multibyte value are ordered from most significant to least significant.

- LITTLE_ENDIAN

```java
public static final
ByteOrder
LITTLE_ENDIAN
```

Constant denoting little-endian byte order. In this order, the bytes of
a multibyte value are ordered from least significant to most
significant.

============ METHOD DETAIL ==========

- Method Detail

- nativeOrder

```java
public static
ByteOrder
nativeOrder()
```

Retrieves the native byte order of the underlying platform.

This method is defined so that performance-sensitive Java code can
allocate direct buffers with the same byte order as the hardware.
Native code libraries are often more efficient when such buffers are
used.

**Returns:** The native byte order of the hardware upon which this Java
virtual machine is running

- toString

```java
public
String
toString()
```

Constructs a string describing this object.

This method returns the string

"BIG_ENDIAN"

for

BIG_ENDIAN

and

"LITTLE_ENDIAN"

for

LITTLE_ENDIAN

.

**Overrides:** toString

in class

Object
**Returns:** The specified string

Field Detail

- BIG_ENDIAN

```java
public static final
ByteOrder
BIG_ENDIAN
```

Constant denoting big-endian byte order. In this order, the bytes of a
multibyte value are ordered from most significant to least significant.

- LITTLE_ENDIAN

```java
public static final
ByteOrder
LITTLE_ENDIAN
```

Constant denoting little-endian byte order. In this order, the bytes of
a multibyte value are ordered from least significant to most
significant.

---

#### Field Detail

BIG_ENDIAN

```java
public static final
ByteOrder
BIG_ENDIAN
```

Constant denoting big-endian byte order. In this order, the bytes of a
multibyte value are ordered from most significant to least significant.

---

#### BIG_ENDIAN

public static final

ByteOrder

BIG_ENDIAN

Constant denoting big-endian byte order. In this order, the bytes of a
multibyte value are ordered from most significant to least significant.

LITTLE_ENDIAN

```java
public static final
ByteOrder
LITTLE_ENDIAN
```

Constant denoting little-endian byte order. In this order, the bytes of
a multibyte value are ordered from least significant to most
significant.

---

#### LITTLE_ENDIAN

public static final

ByteOrder

LITTLE_ENDIAN

Constant denoting little-endian byte order. In this order, the bytes of
a multibyte value are ordered from least significant to most
significant.

Method Detail

- nativeOrder

```java
public static
ByteOrder
nativeOrder()
```

Retrieves the native byte order of the underlying platform.

This method is defined so that performance-sensitive Java code can
allocate direct buffers with the same byte order as the hardware.
Native code libraries are often more efficient when such buffers are
used.

**Returns:** The native byte order of the hardware upon which this Java
virtual machine is running

- toString

```java
public
String
toString()
```

Constructs a string describing this object.

This method returns the string

"BIG_ENDIAN"

for

BIG_ENDIAN

and

"LITTLE_ENDIAN"

for

LITTLE_ENDIAN

.

**Overrides:** toString

in class

Object
**Returns:** The specified string

---

#### Method Detail

nativeOrder

```java
public static
ByteOrder
nativeOrder()
```

Retrieves the native byte order of the underlying platform.

This method is defined so that performance-sensitive Java code can
allocate direct buffers with the same byte order as the hardware.
Native code libraries are often more efficient when such buffers are
used.

**Returns:** The native byte order of the hardware upon which this Java
virtual machine is running

---

#### nativeOrder

public static

ByteOrder

nativeOrder()

Retrieves the native byte order of the underlying platform.

This method is defined so that performance-sensitive Java code can
allocate direct buffers with the same byte order as the hardware.
Native code libraries are often more efficient when such buffers are
used.

This method is defined so that performance-sensitive Java code can
allocate direct buffers with the same byte order as the hardware.
Native code libraries are often more efficient when such buffers are
used.

toString

```java
public
String
toString()
```

Constructs a string describing this object.

This method returns the string

"BIG_ENDIAN"

for

BIG_ENDIAN

and

"LITTLE_ENDIAN"

for

LITTLE_ENDIAN

.

**Overrides:** toString

in class

Object
**Returns:** The specified string

---

#### toString

public

String

toString()

Constructs a string describing this object.

This method returns the string

"BIG_ENDIAN"

for

BIG_ENDIAN

and

"LITTLE_ENDIAN"

for

LITTLE_ENDIAN

.

This method returns the string

"BIG_ENDIAN"

for

BIG_ENDIAN

and

"LITTLE_ENDIAN"

for

LITTLE_ENDIAN

.

---

