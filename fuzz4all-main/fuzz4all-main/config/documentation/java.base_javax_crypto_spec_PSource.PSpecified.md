# Class PSource.PSpecified

**Source:** `java.base\javax\crypto\spec\PSource.PSpecified.html`

### Class Description

```java
public static final class
PSource.PSpecified

extends
PSource
```

This class is used to explicitly specify the value for
encoding input P in OAEP Padding.

**Enclosing class:** PSource

---

### Field Details

#### public static final
PSource.PSpecified
DEFAULT

The encoding input P whose value equals byte[0].

---

### Constructor Details

#### public PSpecified​(byte[] p)

Constructs the source explicitly with the specified
value

p

as the encoding input P.
Note:

**Parameters:**
- p

- the value of the encoding input. The contents
of the array are copied to protect against subsequent
modification.

**Throws:**
- NullPointerException

- if

p

is null.

---

### Method Details

#### public byte[] getValue()

Returns the value of encoding input P.

**Returns:**
- the value of encoding input P. A new array is
returned each time this method is called.

---

### Additional Sections

#### Class PSource.PSpecified

java.lang.Object

- javax.crypto.spec.PSource
- - javax.crypto.spec.PSource.PSpecified

javax.crypto.spec.PSource

- javax.crypto.spec.PSource.PSpecified

javax.crypto.spec.PSource.PSpecified

**Enclosing class:** PSource

```java
public static final class
PSource.PSpecified

extends
PSource
```

This class is used to explicitly specify the value for
encoding input P in OAEP Padding.

**Since:** 1.5

public static final class

PSource.PSpecified

extends

PSource

This class is used to explicitly specify the value for
encoding input P in OAEP Padding.

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

- Nested classes/interfaces declared in class javax.crypto.spec.

PSource

PSource.PSpecified

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static

PSource.PSpecified

DEFAULT

The encoding input P whose value equals byte[0].

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

PSpecified

​(byte[] p)

Constructs the source explicitly with the specified
value

p

as the encoding input P.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

byte[]

getValue

()

Returns the value of encoding input P.

- Methods declared in class javax.crypto.spec.

PSource

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

Nested Class Summary

- Nested classes/interfaces declared in class javax.crypto.spec.

PSource

PSource.PSpecified

---

#### Nested Class Summary

Nested classes/interfaces declared in class javax.crypto.spec.

PSource

PSource.PSpecified

---

#### Nested classes/interfaces declared in class javax.crypto.spec. PSource

Field Summary

Fields

Modifier and Type

Field

Description

static

PSource.PSpecified

DEFAULT

The encoding input P whose value equals byte[0].

---

#### Field Summary

The encoding input P whose value equals byte[0].

Constructor Summary

Constructors

Constructor

Description

PSpecified

​(byte[] p)

Constructs the source explicitly with the specified
value

p

as the encoding input P.

---

#### Constructor Summary

Constructs the source explicitly with the specified
value

p

as the encoding input P.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

byte[]

getValue

()

Returns the value of encoding input P.

- Methods declared in class javax.crypto.spec.

PSource

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

Returns the value of encoding input P.

Methods declared in class javax.crypto.spec.

PSource

getAlgorithm

---

#### Methods declared in class javax.crypto.spec. PSource

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

- DEFAULT

```java
public static final
PSource.PSpecified
DEFAULT
```

The encoding input P whose value equals byte[0].

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- PSpecified

```java
public PSpecified​(byte[] p)
```

Constructs the source explicitly with the specified
value

p

as the encoding input P.
Note:

**Parameters:** p

- the value of the encoding input. The contents
of the array are copied to protect against subsequent
modification.
**Throws:** NullPointerException

- if

p

is null.

============ METHOD DETAIL ==========

- Method Detail

- getValue

```java
public byte[] getValue()
```

Returns the value of encoding input P.

**Returns:** the value of encoding input P. A new array is
returned each time this method is called.

Field Detail

- DEFAULT

```java
public static final
PSource.PSpecified
DEFAULT
```

The encoding input P whose value equals byte[0].

---

#### Field Detail

DEFAULT

```java
public static final
PSource.PSpecified
DEFAULT
```

The encoding input P whose value equals byte[0].

---

#### DEFAULT

public static final

PSource.PSpecified

DEFAULT

The encoding input P whose value equals byte[0].

Constructor Detail

- PSpecified

```java
public PSpecified​(byte[] p)
```

Constructs the source explicitly with the specified
value

p

as the encoding input P.
Note:

**Parameters:** p

- the value of the encoding input. The contents
of the array are copied to protect against subsequent
modification.
**Throws:** NullPointerException

- if

p

is null.

---

#### Constructor Detail

PSpecified

```java
public PSpecified​(byte[] p)
```

Constructs the source explicitly with the specified
value

p

as the encoding input P.
Note:

**Parameters:** p

- the value of the encoding input. The contents
of the array are copied to protect against subsequent
modification.
**Throws:** NullPointerException

- if

p

is null.

---

#### PSpecified

public PSpecified​(byte[] p)

Constructs the source explicitly with the specified
value

p

as the encoding input P.
Note:

Method Detail

- getValue

```java
public byte[] getValue()
```

Returns the value of encoding input P.

**Returns:** the value of encoding input P. A new array is
returned each time this method is called.

---

#### Method Detail

getValue

```java
public byte[] getValue()
```

Returns the value of encoding input P.

**Returns:** the value of encoding input P. A new array is
returned each time this method is called.

---

#### getValue

public byte[] getValue()

Returns the value of encoding input P.

---

