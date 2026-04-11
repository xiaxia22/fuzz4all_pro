# Class AnnotationTypeMismatchException

**Source:** `java.base\java\lang\annotation\AnnotationTypeMismatchException.html`

### Class Description

```java
public class
AnnotationTypeMismatchException

extends
RuntimeException
```

Thrown to indicate that a program has attempted to access an element of
an annotation whose type has changed after the annotation was compiled
(or serialized).
This exception can be thrown by the

API used to read annotations
reflectively

.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public AnnotationTypeMismatchException​(
Method
element,

String
foundType)

Constructs an AnnotationTypeMismatchException for the specified
annotation type element and found data type.

**Parameters:**
- element

- the

Method

object for the annotation
element, may be

null
- foundType

- the (erroneous) type of data found in the annotation.
This string may, but is not required to, contain the value
as well. The exact format of the string is unspecified,
may be

null

.

---

### Method Details

#### public
Method
element()

Returns the

Method

object for the incorrectly typed element.
The value may be unavailable if this exception has been
serialized and then read back in.

**Returns:**
- the

Method

object for the incorrectly typed
element, or

null

if unavailable

---

#### public
String
foundType()

Returns the type of data found in the incorrectly typed element.
The returned string may, but is not required to, contain the value
as well. The exact format of the string is unspecified and the string
may be

null

.

**Returns:**
- the type of data found in the incorrectly typed element

---

### Additional Sections

#### Class AnnotationTypeMismatchException

java.lang.Object

- java.lang.Throwable
- - java.lang.Exception
- - java.lang.RuntimeException
- - java.lang.annotation.AnnotationTypeMismatchException

java.lang.Throwable

- java.lang.Exception
- - java.lang.RuntimeException
- - java.lang.annotation.AnnotationTypeMismatchException

java.lang.Exception

- java.lang.RuntimeException
- - java.lang.annotation.AnnotationTypeMismatchException

java.lang.RuntimeException

- java.lang.annotation.AnnotationTypeMismatchException

java.lang.annotation.AnnotationTypeMismatchException

**All Implemented Interfaces:** Serializable

```java
public class
AnnotationTypeMismatchException

extends
RuntimeException
```

Thrown to indicate that a program has attempted to access an element of
an annotation whose type has changed after the annotation was compiled
(or serialized).
This exception can be thrown by the

API used to read annotations
reflectively

.

**Since:** 1.5
**See Also:** AnnotatedElement

,

Serialized Form

public class

AnnotationTypeMismatchException

extends

RuntimeException

Thrown to indicate that a program has attempted to access an element of
an annotation whose type has changed after the annotation was compiled
(or serialized).
This exception can be thrown by the

API used to read annotations
reflectively

.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

AnnotationTypeMismatchException

​(

Method

element,

String

foundType)

Constructs an AnnotationTypeMismatchException for the specified
annotation type element and found data type.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Method

element

()

Returns the

Method

object for the incorrectly typed element.

String

foundType

()

Returns the type of data found in the incorrectly typed element.

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

AnnotationTypeMismatchException

​(

Method

element,

String

foundType)

Constructs an AnnotationTypeMismatchException for the specified
annotation type element and found data type.

---

#### Constructor Summary

Constructs an AnnotationTypeMismatchException for the specified
annotation type element and found data type.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Method

element

()

Returns the

Method

object for the incorrectly typed element.

String

foundType

()

Returns the type of data found in the incorrectly typed element.

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

Returns the

Method

object for the incorrectly typed element.

Returns the type of data found in the incorrectly typed element.

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

- AnnotationTypeMismatchException

```java
public AnnotationTypeMismatchException​(
Method
element,

String
foundType)
```

Constructs an AnnotationTypeMismatchException for the specified
annotation type element and found data type.

**Parameters:** element

- the

Method

object for the annotation
element, may be

null
**Parameters:** foundType

- the (erroneous) type of data found in the annotation.
This string may, but is not required to, contain the value
as well. The exact format of the string is unspecified,
may be

null

.

============ METHOD DETAIL ==========

- Method Detail

- element

```java
public
Method
element()
```

Returns the

Method

object for the incorrectly typed element.
The value may be unavailable if this exception has been
serialized and then read back in.

**Returns:** the

Method

object for the incorrectly typed
element, or

null

if unavailable

- foundType

```java
public
String
foundType()
```

Returns the type of data found in the incorrectly typed element.
The returned string may, but is not required to, contain the value
as well. The exact format of the string is unspecified and the string
may be

null

.

**Returns:** the type of data found in the incorrectly typed element

Constructor Detail

- AnnotationTypeMismatchException

```java
public AnnotationTypeMismatchException​(
Method
element,

String
foundType)
```

Constructs an AnnotationTypeMismatchException for the specified
annotation type element and found data type.

**Parameters:** element

- the

Method

object for the annotation
element, may be

null
**Parameters:** foundType

- the (erroneous) type of data found in the annotation.
This string may, but is not required to, contain the value
as well. The exact format of the string is unspecified,
may be

null

.

---

#### Constructor Detail

AnnotationTypeMismatchException

```java
public AnnotationTypeMismatchException​(
Method
element,

String
foundType)
```

Constructs an AnnotationTypeMismatchException for the specified
annotation type element and found data type.

**Parameters:** element

- the

Method

object for the annotation
element, may be

null
**Parameters:** foundType

- the (erroneous) type of data found in the annotation.
This string may, but is not required to, contain the value
as well. The exact format of the string is unspecified,
may be

null

.

---

#### AnnotationTypeMismatchException

public AnnotationTypeMismatchException​(

Method

element,

String

foundType)

Constructs an AnnotationTypeMismatchException for the specified
annotation type element and found data type.

Method Detail

- element

```java
public
Method
element()
```

Returns the

Method

object for the incorrectly typed element.
The value may be unavailable if this exception has been
serialized and then read back in.

**Returns:** the

Method

object for the incorrectly typed
element, or

null

if unavailable

- foundType

```java
public
String
foundType()
```

Returns the type of data found in the incorrectly typed element.
The returned string may, but is not required to, contain the value
as well. The exact format of the string is unspecified and the string
may be

null

.

**Returns:** the type of data found in the incorrectly typed element

---

#### Method Detail

element

```java
public
Method
element()
```

Returns the

Method

object for the incorrectly typed element.
The value may be unavailable if this exception has been
serialized and then read back in.

**Returns:** the

Method

object for the incorrectly typed
element, or

null

if unavailable

---

#### element

public

Method

element()

Returns the

Method

object for the incorrectly typed element.
The value may be unavailable if this exception has been
serialized and then read back in.

foundType

```java
public
String
foundType()
```

Returns the type of data found in the incorrectly typed element.
The returned string may, but is not required to, contain the value
as well. The exact format of the string is unspecified and the string
may be

null

.

**Returns:** the type of data found in the incorrectly typed element

---

#### foundType

public

String

foundType()

Returns the type of data found in the incorrectly typed element.
The returned string may, but is not required to, contain the value
as well. The exact format of the string is unspecified and the string
may be

null

.

---

