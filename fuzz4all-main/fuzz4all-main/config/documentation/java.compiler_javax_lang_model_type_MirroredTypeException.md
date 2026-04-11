# Class MirroredTypeException

**Source:** `java.compiler\javax\lang\model\type\MirroredTypeException.html`

### Class Description

```java
public class
MirroredTypeException

extends
MirroredTypesException
```

Thrown when an application attempts to access the

Class

object
corresponding to a

TypeMirror

.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public MirroredTypeException​(
TypeMirror
type)

Constructs a new MirroredTypeException for the specified type.

**Parameters:**
- type

- the type being accessed

---

### Method Details

#### public
TypeMirror
getTypeMirror()

Returns the type mirror corresponding to the type being accessed.
The type mirror may be unavailable if this exception has been
serialized and then read back in.

**Returns:**
- the type mirror, or

null

if unavailable

---

### Additional Sections

#### Class MirroredTypeException

java.lang.Object

- java.lang.Throwable
- - java.lang.Exception
- - java.lang.RuntimeException
- - javax.lang.model.type.MirroredTypesException
- - javax.lang.model.type.MirroredTypeException

java.lang.Throwable

- java.lang.Exception
- - java.lang.RuntimeException
- - javax.lang.model.type.MirroredTypesException
- - javax.lang.model.type.MirroredTypeException

java.lang.Exception

- java.lang.RuntimeException
- - javax.lang.model.type.MirroredTypesException
- - javax.lang.model.type.MirroredTypeException

java.lang.RuntimeException

- javax.lang.model.type.MirroredTypesException
- - javax.lang.model.type.MirroredTypeException

javax.lang.model.type.MirroredTypesException

- javax.lang.model.type.MirroredTypeException

javax.lang.model.type.MirroredTypeException

**All Implemented Interfaces:** Serializable

```java
public class
MirroredTypeException

extends
MirroredTypesException
```

Thrown when an application attempts to access the

Class

object
corresponding to a

TypeMirror

.

**Since:** 1.6
**See Also:** MirroredTypesException

,

Element.getAnnotation(Class)

,

Serialized Form

public class

MirroredTypeException

extends

MirroredTypesException

Thrown when an application attempts to access the

Class

object
corresponding to a

TypeMirror

.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

MirroredTypeException

​(

TypeMirror

type)

Constructs a new MirroredTypeException for the specified type.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

TypeMirror

getTypeMirror

()

Returns the type mirror corresponding to the type being accessed.

- Methods declared in class javax.lang.model.type.

MirroredTypesException

getTypeMirrors

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

MirroredTypeException

​(

TypeMirror

type)

Constructs a new MirroredTypeException for the specified type.

---

#### Constructor Summary

Constructs a new MirroredTypeException for the specified type.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

TypeMirror

getTypeMirror

()

Returns the type mirror corresponding to the type being accessed.

- Methods declared in class javax.lang.model.type.

MirroredTypesException

getTypeMirrors

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

Returns the type mirror corresponding to the type being accessed.

Methods declared in class javax.lang.model.type.

MirroredTypesException

getTypeMirrors

---

#### Methods declared in class javax.lang.model.type. MirroredTypesException

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

- MirroredTypeException

```java
public MirroredTypeException​(
TypeMirror
type)
```

Constructs a new MirroredTypeException for the specified type.

**Parameters:** type

- the type being accessed

============ METHOD DETAIL ==========

- Method Detail

- getTypeMirror

```java
public
TypeMirror
getTypeMirror()
```

Returns the type mirror corresponding to the type being accessed.
The type mirror may be unavailable if this exception has been
serialized and then read back in.

**Returns:** the type mirror, or

null

if unavailable

Constructor Detail

- MirroredTypeException

```java
public MirroredTypeException​(
TypeMirror
type)
```

Constructs a new MirroredTypeException for the specified type.

**Parameters:** type

- the type being accessed

---

#### Constructor Detail

MirroredTypeException

```java
public MirroredTypeException​(
TypeMirror
type)
```

Constructs a new MirroredTypeException for the specified type.

**Parameters:** type

- the type being accessed

---

#### MirroredTypeException

public MirroredTypeException​(

TypeMirror

type)

Constructs a new MirroredTypeException for the specified type.

Method Detail

- getTypeMirror

```java
public
TypeMirror
getTypeMirror()
```

Returns the type mirror corresponding to the type being accessed.
The type mirror may be unavailable if this exception has been
serialized and then read back in.

**Returns:** the type mirror, or

null

if unavailable

---

#### Method Detail

getTypeMirror

```java
public
TypeMirror
getTypeMirror()
```

Returns the type mirror corresponding to the type being accessed.
The type mirror may be unavailable if this exception has been
serialized and then read back in.

**Returns:** the type mirror, or

null

if unavailable

---

#### getTypeMirror

public

TypeMirror

getTypeMirror()

Returns the type mirror corresponding to the type being accessed.
The type mirror may be unavailable if this exception has been
serialized and then read back in.

---

