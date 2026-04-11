# Class TypeNotPresentException

**Source:** `java.base\java\lang\TypeNotPresentException.html`

### Class Description

```java
public class
TypeNotPresentException

extends
RuntimeException
```

Thrown when an application tries to access a type using a string
representing the type's name, but no definition for the type with
the specified name can be found. This exception differs from

ClassNotFoundException

in that

ClassNotFoundException

is a
checked exception, whereas this exception is unchecked.

Note that this exception may be used when undefined type variables
are accessed as well as when types (e.g., classes, interfaces or
annotation types) are loaded.
In particular, this exception can be thrown by the

API used to read annotations
reflectively

.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public TypeNotPresentException​(
String
typeName,

Throwable
cause)

Constructs a

TypeNotPresentException

for the named type
with the specified cause.

**Parameters:**
- typeName

- the fully qualified name of the unavailable type
- cause

- the exception that was thrown when the system attempted to
load the named type, or

null

if unavailable or inapplicable

---

### Method Details

#### public
String
typeName()

Returns the fully qualified name of the unavailable type.

**Returns:**
- the fully qualified name of the unavailable type

---

### Additional Sections

#### Class TypeNotPresentException

java.lang.Object

- java.lang.Throwable
- - java.lang.Exception
- - java.lang.RuntimeException
- - java.lang.TypeNotPresentException

java.lang.Throwable

- java.lang.Exception
- - java.lang.RuntimeException
- - java.lang.TypeNotPresentException

java.lang.Exception

- java.lang.RuntimeException
- - java.lang.TypeNotPresentException

java.lang.RuntimeException

- java.lang.TypeNotPresentException

java.lang.TypeNotPresentException

**All Implemented Interfaces:** Serializable

```java
public class
TypeNotPresentException

extends
RuntimeException
```

Thrown when an application tries to access a type using a string
representing the type's name, but no definition for the type with
the specified name can be found. This exception differs from

ClassNotFoundException

in that

ClassNotFoundException

is a
checked exception, whereas this exception is unchecked.

Note that this exception may be used when undefined type variables
are accessed as well as when types (e.g., classes, interfaces or
annotation types) are loaded.
In particular, this exception can be thrown by the

API used to read annotations
reflectively

.

**Since:** 1.5
**See Also:** AnnotatedElement

,

Serialized Form

public class

TypeNotPresentException

extends

RuntimeException

Thrown when an application tries to access a type using a string
representing the type's name, but no definition for the type with
the specified name can be found. This exception differs from

ClassNotFoundException

in that

ClassNotFoundException

is a
checked exception, whereas this exception is unchecked.

Note that this exception may be used when undefined type variables
are accessed as well as when types (e.g., classes, interfaces or
annotation types) are loaded.
In particular, this exception can be thrown by the

API used to read annotations
reflectively

.

Note that this exception may be used when undefined type variables
are accessed as well as when types (e.g., classes, interfaces or
annotation types) are loaded.
In particular, this exception can be thrown by the

API used to read annotations
reflectively

.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

TypeNotPresentException

​(

String

typeName,

Throwable

cause)

Constructs a

TypeNotPresentException

for the named type
with the specified cause.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

String

typeName

()

Returns the fully qualified name of the unavailable type.

- Methods declared in class java.lang.

Throwable

addSuppressed

,

fillInStackTrace

,

getCause

,

getLocalizedMessage

,

getMessage

,

getStackTrace

,

getSuppressed

,

initCause

,

printStackTrace

,

printStackTrace

,

printStackTrace

,

setStackTrace

,

toString

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

Constructor Summary

Constructors

Constructor

Description

TypeNotPresentException

​(

String

typeName,

Throwable

cause)

Constructs a

TypeNotPresentException

for the named type
with the specified cause.

---

#### Constructor Summary

Constructs a

TypeNotPresentException

for the named type
with the specified cause.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

String

typeName

()

Returns the fully qualified name of the unavailable type.

- Methods declared in class java.lang.

Throwable

addSuppressed

,

fillInStackTrace

,

getCause

,

getLocalizedMessage

,

getMessage

,

getStackTrace

,

getSuppressed

,

initCause

,

printStackTrace

,

printStackTrace

,

printStackTrace

,

setStackTrace

,

toString

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

Returns the fully qualified name of the unavailable type.

Methods declared in class java.lang.

Throwable

addSuppressed

,

fillInStackTrace

,

getCause

,

getLocalizedMessage

,

getMessage

,

getStackTrace

,

getSuppressed

,

initCause

,

printStackTrace

,

printStackTrace

,

printStackTrace

,

setStackTrace

,

toString

---

#### Methods declared in class java.lang. Throwable

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

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- TypeNotPresentException

```java
public TypeNotPresentException​(
String
typeName,

Throwable
cause)
```

Constructs a

TypeNotPresentException

for the named type
with the specified cause.

**Parameters:** typeName

- the fully qualified name of the unavailable type
**Parameters:** cause

- the exception that was thrown when the system attempted to
load the named type, or

null

if unavailable or inapplicable

============ METHOD DETAIL ==========

- Method Detail

- typeName

```java
public
String
typeName()
```

Returns the fully qualified name of the unavailable type.

**Returns:** the fully qualified name of the unavailable type

Constructor Detail

- TypeNotPresentException

```java
public TypeNotPresentException​(
String
typeName,

Throwable
cause)
```

Constructs a

TypeNotPresentException

for the named type
with the specified cause.

**Parameters:** typeName

- the fully qualified name of the unavailable type
**Parameters:** cause

- the exception that was thrown when the system attempted to
load the named type, or

null

if unavailable or inapplicable

---

#### Constructor Detail

TypeNotPresentException

```java
public TypeNotPresentException​(
String
typeName,

Throwable
cause)
```

Constructs a

TypeNotPresentException

for the named type
with the specified cause.

**Parameters:** typeName

- the fully qualified name of the unavailable type
**Parameters:** cause

- the exception that was thrown when the system attempted to
load the named type, or

null

if unavailable or inapplicable

---

#### TypeNotPresentException

public TypeNotPresentException​(

String

typeName,

Throwable

cause)

Constructs a

TypeNotPresentException

for the named type
with the specified cause.

Method Detail

- typeName

```java
public
String
typeName()
```

Returns the fully qualified name of the unavailable type.

**Returns:** the fully qualified name of the unavailable type

---

#### Method Detail

typeName

```java
public
String
typeName()
```

Returns the fully qualified name of the unavailable type.

**Returns:** the fully qualified name of the unavailable type

---

#### typeName

public

String

typeName()

Returns the fully qualified name of the unavailable type.

---

