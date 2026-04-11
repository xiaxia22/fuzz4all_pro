# Class ECGenParameterSpec

**Source:** `java.base\java\security\spec\ECGenParameterSpec.html`

### Class Description

```java
public class
ECGenParameterSpec

extends
NamedParameterSpec
```

This immutable class specifies the set of parameters used for
generating elliptic curve (EC) domain parameters.

**All Implemented Interfaces:** AlgorithmParameterSpec

---

### Field Details

*No entries found.*

### Constructor Details

#### public ECGenParameterSpec​(
String
stdName)

Creates a parameter specification for EC parameter
generation using a standard (or predefined) name

stdName

in order to generate the corresponding
(precomputed) elliptic curve domain parameters. For the
list of supported names, please consult the documentation
of the provider whose implementation will be used.

**Parameters:**
- stdName

- the standard name of the to-be-generated EC
domain parameters.

**Throws:**
- NullPointerException

- if

stdName

is null.

---

### Method Details

*No entries found.*

### Additional Sections

#### Class ECGenParameterSpec

java.lang.Object

- java.security.spec.NamedParameterSpec
- - java.security.spec.ECGenParameterSpec

java.security.spec.NamedParameterSpec

- java.security.spec.ECGenParameterSpec

java.security.spec.ECGenParameterSpec

**All Implemented Interfaces:** AlgorithmParameterSpec

```java
public class
ECGenParameterSpec

extends
NamedParameterSpec
```

This immutable class specifies the set of parameters used for
generating elliptic curve (EC) domain parameters.

**Since:** 1.5
**See Also:** AlgorithmParameterSpec

public class

ECGenParameterSpec

extends

NamedParameterSpec

This immutable class specifies the set of parameters used for
generating elliptic curve (EC) domain parameters.

=========== FIELD SUMMARY ===========

- Field Summary

- Fields declared in class java.security.spec.

NamedParameterSpec

X25519

,

X448

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

ECGenParameterSpec

​(

String

stdName)

Creates a parameter specification for EC parameter
generation using a standard (or predefined) name

stdName

in order to generate the corresponding
(precomputed) elliptic curve domain parameters.

========== METHOD SUMMARY ===========

- Method Summary

- Methods declared in class java.security.spec.

NamedParameterSpec

getName

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

- Fields declared in class java.security.spec.

NamedParameterSpec

X25519

,

X448

---

#### Field Summary

Fields declared in class java.security.spec.

NamedParameterSpec

X25519

,

X448

---

#### Fields declared in class java.security.spec. NamedParameterSpec

Constructor Summary

Constructors

Constructor

Description

ECGenParameterSpec

​(

String

stdName)

Creates a parameter specification for EC parameter
generation using a standard (or predefined) name

stdName

in order to generate the corresponding
(precomputed) elliptic curve domain parameters.

---

#### Constructor Summary

Creates a parameter specification for EC parameter
generation using a standard (or predefined) name

stdName

in order to generate the corresponding
(precomputed) elliptic curve domain parameters.

Method Summary

- Methods declared in class java.security.spec.

NamedParameterSpec

getName

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

Methods declared in class java.security.spec.

NamedParameterSpec

getName

---

#### Methods declared in class java.security.spec. NamedParameterSpec

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

- ECGenParameterSpec

```java
public ECGenParameterSpec​(
String
stdName)
```

Creates a parameter specification for EC parameter
generation using a standard (or predefined) name

stdName

in order to generate the corresponding
(precomputed) elliptic curve domain parameters. For the
list of supported names, please consult the documentation
of the provider whose implementation will be used.

**Parameters:** stdName

- the standard name of the to-be-generated EC
domain parameters.
**Throws:** NullPointerException

- if

stdName

is null.

Constructor Detail

- ECGenParameterSpec

```java
public ECGenParameterSpec​(
String
stdName)
```

Creates a parameter specification for EC parameter
generation using a standard (or predefined) name

stdName

in order to generate the corresponding
(precomputed) elliptic curve domain parameters. For the
list of supported names, please consult the documentation
of the provider whose implementation will be used.

**Parameters:** stdName

- the standard name of the to-be-generated EC
domain parameters.
**Throws:** NullPointerException

- if

stdName

is null.

---

#### Constructor Detail

ECGenParameterSpec

```java
public ECGenParameterSpec​(
String
stdName)
```

Creates a parameter specification for EC parameter
generation using a standard (or predefined) name

stdName

in order to generate the corresponding
(precomputed) elliptic curve domain parameters. For the
list of supported names, please consult the documentation
of the provider whose implementation will be used.

**Parameters:** stdName

- the standard name of the to-be-generated EC
domain parameters.
**Throws:** NullPointerException

- if

stdName

is null.

---

#### ECGenParameterSpec

public ECGenParameterSpec​(

String

stdName)

Creates a parameter specification for EC parameter
generation using a standard (or predefined) name

stdName

in order to generate the corresponding
(precomputed) elliptic curve domain parameters. For the
list of supported names, please consult the documentation
of the provider whose implementation will be used.

---

