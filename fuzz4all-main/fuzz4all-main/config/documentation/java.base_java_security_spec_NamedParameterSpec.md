# Class NamedParameterSpec

**Source:** `java.base\java\security\spec\NamedParameterSpec.html`

### Class Description

```java
public class
NamedParameterSpec

extends
Object

implements
AlgorithmParameterSpec
```

This class is used to specify any algorithm parameters that are determined
by a standard name. This class also holds constants for standard parameter
set names. The names of these constants exactly match the corresponding
parameter set name. For example, NamedParameterSpec.X25519 represents the
parameter set identified by the string "X25519". These strings are defined
in the

Java Security Standard Algorithm Names Specification

.

**All Implemented Interfaces:** AlgorithmParameterSpec

---

### Field Details

#### public static final
NamedParameterSpec
X25519

The X25519 parameters

---

#### public static final
NamedParameterSpec
X448

The X448 parameters

---

### Constructor Details

#### public NamedParameterSpec​(
String
stdName)

Creates a parameter specification using a standard (or predefined)
name

stdName

. For the
list of supported names, please consult the documentation
of the provider whose implementation will be used.

**Parameters:**
- stdName

- the standard name of the algorithm parameters

**Throws:**
- NullPointerException

- if

stdName

is null.

---

### Method Details

#### public
String
getName()

Returns the standard name that determines the algorithm parameters.

**Returns:**
- the standard name.

---

### Additional Sections

#### Class NamedParameterSpec

java.lang.Object

- java.security.spec.NamedParameterSpec

java.security.spec.NamedParameterSpec

**All Implemented Interfaces:** AlgorithmParameterSpec

**Direct Known Subclasses:** ECGenParameterSpec

```java
public class
NamedParameterSpec

extends
Object

implements
AlgorithmParameterSpec
```

This class is used to specify any algorithm parameters that are determined
by a standard name. This class also holds constants for standard parameter
set names. The names of these constants exactly match the corresponding
parameter set name. For example, NamedParameterSpec.X25519 represents the
parameter set identified by the string "X25519". These strings are defined
in the

Java Security Standard Algorithm Names Specification

.

**Since:** 11

public class

NamedParameterSpec

extends

Object

implements

AlgorithmParameterSpec

This class is used to specify any algorithm parameters that are determined
by a standard name. This class also holds constants for standard parameter
set names. The names of these constants exactly match the corresponding
parameter set name. For example, NamedParameterSpec.X25519 represents the
parameter set identified by the string "X25519". These strings are defined
in the

Java Security Standard Algorithm Names Specification

.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static

NamedParameterSpec

X25519

The X25519 parameters

static

NamedParameterSpec

X448

The X448 parameters

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

NamedParameterSpec

​(

String

stdName)

Creates a parameter specification using a standard (or predefined)
name

stdName

.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

String

getName

()

Returns the standard name that determines the algorithm parameters.

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

static

NamedParameterSpec

X25519

The X25519 parameters

static

NamedParameterSpec

X448

The X448 parameters

---

#### Field Summary

The X25519 parameters

The X448 parameters

Constructor Summary

Constructors

Constructor

Description

NamedParameterSpec

​(

String

stdName)

Creates a parameter specification using a standard (or predefined)
name

stdName

.

---

#### Constructor Summary

Creates a parameter specification using a standard (or predefined)
name

stdName

.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

String

getName

()

Returns the standard name that determines the algorithm parameters.

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

Returns the standard name that determines the algorithm parameters.

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

- X25519

```java
public static final
NamedParameterSpec
X25519
```

The X25519 parameters

- X448

```java
public static final
NamedParameterSpec
X448
```

The X448 parameters

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- NamedParameterSpec

```java
public NamedParameterSpec​(
String
stdName)
```

Creates a parameter specification using a standard (or predefined)
name

stdName

. For the
list of supported names, please consult the documentation
of the provider whose implementation will be used.

**Parameters:** stdName

- the standard name of the algorithm parameters
**Throws:** NullPointerException

- if

stdName

is null.

============ METHOD DETAIL ==========

- Method Detail

- getName

```java
public
String
getName()
```

Returns the standard name that determines the algorithm parameters.

**Returns:** the standard name.

Field Detail

- X25519

```java
public static final
NamedParameterSpec
X25519
```

The X25519 parameters

- X448

```java
public static final
NamedParameterSpec
X448
```

The X448 parameters

---

#### Field Detail

X25519

```java
public static final
NamedParameterSpec
X25519
```

The X25519 parameters

---

#### X25519

public static final

NamedParameterSpec

X25519

The X25519 parameters

X448

```java
public static final
NamedParameterSpec
X448
```

The X448 parameters

---

#### X448

public static final

NamedParameterSpec

X448

The X448 parameters

Constructor Detail

- NamedParameterSpec

```java
public NamedParameterSpec​(
String
stdName)
```

Creates a parameter specification using a standard (or predefined)
name

stdName

. For the
list of supported names, please consult the documentation
of the provider whose implementation will be used.

**Parameters:** stdName

- the standard name of the algorithm parameters
**Throws:** NullPointerException

- if

stdName

is null.

---

#### Constructor Detail

NamedParameterSpec

```java
public NamedParameterSpec​(
String
stdName)
```

Creates a parameter specification using a standard (or predefined)
name

stdName

. For the
list of supported names, please consult the documentation
of the provider whose implementation will be used.

**Parameters:** stdName

- the standard name of the algorithm parameters
**Throws:** NullPointerException

- if

stdName

is null.

---

#### NamedParameterSpec

public NamedParameterSpec​(

String

stdName)

Creates a parameter specification using a standard (or predefined)
name

stdName

. For the
list of supported names, please consult the documentation
of the provider whose implementation will be used.

Method Detail

- getName

```java
public
String
getName()
```

Returns the standard name that determines the algorithm parameters.

**Returns:** the standard name.

---

#### Method Detail

getName

```java
public
String
getName()
```

Returns the standard name that determines the algorithm parameters.

**Returns:** the standard name.

---

#### getName

public

String

getName()

Returns the standard name that determines the algorithm parameters.

---

