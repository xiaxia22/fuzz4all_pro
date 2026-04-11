# Class PSource

**Source:** `java.base\javax\crypto\spec\PSource.html`

### Class Description

```java
public class
PSource

extends
Object
```

This class specifies the source for encoding input P in OAEP Padding,
as defined in the

PKCS#1 v2.2

standard.

```java
PSourceAlgorithm ::= AlgorithmIdentifier {
{PKCS1PSourceAlgorithms}
}
```

where

```java
PKCS1PSourceAlgorithms ALGORITHM-IDENTIFIER ::= {
{ OID id-pSpecified PARAMETERS EncodingParameters },
... -- Allows for future expansion --
}
EncodingParameters ::= OCTET STRING(SIZE(0..MAX))
```

**Direct Known Subclasses:** PSource.PSpecified

---

### Field Details

*No entries found.*

### Constructor Details

#### protected PSource​(
String
pSrcName)

Constructs a source of the encoding input P for OAEP
padding as defined in the PKCS #1 standard using the
specified PSource algorithm.

**Parameters:**
- pSrcName

- the algorithm for the source of the
encoding input P.

**Throws:**
- NullPointerException

- if

pSrcName

is null.

---

### Method Details

#### public
String
getAlgorithm()

Returns the PSource algorithm name.

**Returns:**
- the PSource algorithm name.

---

### Additional Sections

#### Class PSource

java.lang.Object

- javax.crypto.spec.PSource

javax.crypto.spec.PSource

**Direct Known Subclasses:** PSource.PSpecified

```java
public class
PSource

extends
Object
```

This class specifies the source for encoding input P in OAEP Padding,
as defined in the

PKCS#1 v2.2

standard.

```java
PSourceAlgorithm ::= AlgorithmIdentifier {
{PKCS1PSourceAlgorithms}
}
```

where

```java
PKCS1PSourceAlgorithms ALGORITHM-IDENTIFIER ::= {
{ OID id-pSpecified PARAMETERS EncodingParameters },
... -- Allows for future expansion --
}
EncodingParameters ::= OCTET STRING(SIZE(0..MAX))
```

**Since:** 1.5

public class

PSource

extends

Object

This class specifies the source for encoding input P in OAEP Padding,
as defined in the

PKCS#1 v2.2

standard.

```java
PSourceAlgorithm ::= AlgorithmIdentifier {
{PKCS1PSourceAlgorithms}
}
```

where

```java
PKCS1PSourceAlgorithms ALGORITHM-IDENTIFIER ::= {
{ OID id-pSpecified PARAMETERS EncodingParameters },
... -- Allows for future expansion --
}
EncodingParameters ::= OCTET STRING(SIZE(0..MAX))
```

PSourceAlgorithm ::= AlgorithmIdentifier {
{PKCS1PSourceAlgorithms}
}

PKCS1PSourceAlgorithms ALGORITHM-IDENTIFIER ::= {
{ OID id-pSpecified PARAMETERS EncodingParameters },
... -- Allows for future expansion --
}
EncodingParameters ::= OCTET STRING(SIZE(0..MAX))

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

static class

PSource.PSpecified

This class is used to explicitly specify the value for
encoding input P in OAEP Padding.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

PSource

​(

String

pSrcName)

Constructs a source of the encoding input P for OAEP
padding as defined in the PKCS #1 standard using the
specified PSource algorithm.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

String

getAlgorithm

()

Returns the PSource algorithm name.

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

PSource.PSpecified

This class is used to explicitly specify the value for
encoding input P in OAEP Padding.

---

#### Nested Class Summary

This class is used to explicitly specify the value for
encoding input P in OAEP Padding.

Constructor Summary

Constructors

Modifier

Constructor

Description

protected

PSource

​(

String

pSrcName)

Constructs a source of the encoding input P for OAEP
padding as defined in the PKCS #1 standard using the
specified PSource algorithm.

---

#### Constructor Summary

Constructs a source of the encoding input P for OAEP
padding as defined in the PKCS #1 standard using the
specified PSource algorithm.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

String

getAlgorithm

()

Returns the PSource algorithm name.

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

Returns the PSource algorithm name.

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

- PSource

```java
protected PSource​(
String
pSrcName)
```

Constructs a source of the encoding input P for OAEP
padding as defined in the PKCS #1 standard using the
specified PSource algorithm.

**Parameters:** pSrcName

- the algorithm for the source of the
encoding input P.
**Throws:** NullPointerException

- if

pSrcName

is null.

============ METHOD DETAIL ==========

- Method Detail

- getAlgorithm

```java
public
String
getAlgorithm()
```

Returns the PSource algorithm name.

**Returns:** the PSource algorithm name.

Constructor Detail

- PSource

```java
protected PSource​(
String
pSrcName)
```

Constructs a source of the encoding input P for OAEP
padding as defined in the PKCS #1 standard using the
specified PSource algorithm.

**Parameters:** pSrcName

- the algorithm for the source of the
encoding input P.
**Throws:** NullPointerException

- if

pSrcName

is null.

---

#### Constructor Detail

PSource

```java
protected PSource​(
String
pSrcName)
```

Constructs a source of the encoding input P for OAEP
padding as defined in the PKCS #1 standard using the
specified PSource algorithm.

**Parameters:** pSrcName

- the algorithm for the source of the
encoding input P.
**Throws:** NullPointerException

- if

pSrcName

is null.

---

#### PSource

protected PSource​(

String

pSrcName)

Constructs a source of the encoding input P for OAEP
padding as defined in the PKCS #1 standard using the
specified PSource algorithm.

Method Detail

- getAlgorithm

```java
public
String
getAlgorithm()
```

Returns the PSource algorithm name.

**Returns:** the PSource algorithm name.

---

#### Method Detail

getAlgorithm

```java
public
String
getAlgorithm()
```

Returns the PSource algorithm name.

**Returns:** the PSource algorithm name.

---

#### getAlgorithm

public

String

getAlgorithm()

Returns the PSource algorithm name.

---

