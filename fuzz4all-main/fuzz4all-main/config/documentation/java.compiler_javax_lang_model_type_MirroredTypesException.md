# Class MirroredTypesException

**Source:** `java.compiler\javax\lang\model\type\MirroredTypesException.html`

### Class Description

```java
public class
MirroredTypesException

extends
RuntimeException
```

Thrown when an application attempts to access a sequence of

Class

objects each corresponding to a

TypeMirror

.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public MirroredTypesException​(
List
<? extends
TypeMirror
> types)

Constructs a new MirroredTypesException for the specified types.

**Parameters:**
- types

- the types being accessed

---

### Method Details

#### public
List
<? extends
TypeMirror
> getTypeMirrors()

Returns the type mirrors corresponding to the types being accessed.
The type mirrors may be unavailable if this exception has been
serialized and then read back in.

**Returns:**
- the type mirrors in construction order, or

null

if unavailable

---

### Additional Sections

#### Class MirroredTypesException

java.lang.Object

- java.lang.Throwable
- - java.lang.Exception
- - java.lang.RuntimeException
- - javax.lang.model.type.MirroredTypesException

java.lang.Throwable

- java.lang.Exception
- - java.lang.RuntimeException
- - javax.lang.model.type.MirroredTypesException

java.lang.Exception

- java.lang.RuntimeException
- - javax.lang.model.type.MirroredTypesException

java.lang.RuntimeException

- javax.lang.model.type.MirroredTypesException

javax.lang.model.type.MirroredTypesException

**All Implemented Interfaces:** Serializable

**Direct Known Subclasses:** MirroredTypeException

```java
public class
MirroredTypesException

extends
RuntimeException
```

Thrown when an application attempts to access a sequence of

Class

objects each corresponding to a

TypeMirror

.

**Since:** 1.6
**See Also:** MirroredTypeException

,

Element.getAnnotation(Class)

,

Serialized Form

public class

MirroredTypesException

extends

RuntimeException

Thrown when an application attempts to access a sequence of

Class

objects each corresponding to a

TypeMirror

.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

MirroredTypesException

​(

List

<? extends

TypeMirror

> types)

Constructs a new MirroredTypesException for the specified types.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

List

<? extends

TypeMirror

>

getTypeMirrors

()

Returns the type mirrors corresponding to the types being accessed.

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

MirroredTypesException

​(

List

<? extends

TypeMirror

> types)

Constructs a new MirroredTypesException for the specified types.

---

#### Constructor Summary

Constructs a new MirroredTypesException for the specified types.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

List

<? extends

TypeMirror

>

getTypeMirrors

()

Returns the type mirrors corresponding to the types being accessed.

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

Returns the type mirrors corresponding to the types being accessed.

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

- MirroredTypesException

```java
public MirroredTypesException​(
List
<? extends
TypeMirror
> types)
```

Constructs a new MirroredTypesException for the specified types.

**Parameters:** types

- the types being accessed

============ METHOD DETAIL ==========

- Method Detail

- getTypeMirrors

```java
public
List
<? extends
TypeMirror
> getTypeMirrors()
```

Returns the type mirrors corresponding to the types being accessed.
The type mirrors may be unavailable if this exception has been
serialized and then read back in.

**Returns:** the type mirrors in construction order, or

null

if unavailable

Constructor Detail

- MirroredTypesException

```java
public MirroredTypesException​(
List
<? extends
TypeMirror
> types)
```

Constructs a new MirroredTypesException for the specified types.

**Parameters:** types

- the types being accessed

---

#### Constructor Detail

MirroredTypesException

```java
public MirroredTypesException​(
List
<? extends
TypeMirror
> types)
```

Constructs a new MirroredTypesException for the specified types.

**Parameters:** types

- the types being accessed

---

#### MirroredTypesException

public MirroredTypesException​(

List

<? extends

TypeMirror

> types)

Constructs a new MirroredTypesException for the specified types.

Method Detail

- getTypeMirrors

```java
public
List
<? extends
TypeMirror
> getTypeMirrors()
```

Returns the type mirrors corresponding to the types being accessed.
The type mirrors may be unavailable if this exception has been
serialized and then read back in.

**Returns:** the type mirrors in construction order, or

null

if unavailable

---

#### Method Detail

getTypeMirrors

```java
public
List
<? extends
TypeMirror
> getTypeMirrors()
```

Returns the type mirrors corresponding to the types being accessed.
The type mirrors may be unavailable if this exception has been
serialized and then read back in.

**Returns:** the type mirrors in construction order, or

null

if unavailable

---

#### getTypeMirrors

public

List

<? extends

TypeMirror

> getTypeMirrors()

Returns the type mirrors corresponding to the types being accessed.
The type mirrors may be unavailable if this exception has been
serialized and then read back in.

---

