# Class IncompleteAnnotationException

**Source:** `java.base\java\lang\annotation\IncompleteAnnotationException.html`

### Class Description

```java
public class
IncompleteAnnotationException

extends
RuntimeException
```

Thrown to indicate that a program has attempted to access an element of
an annotation type that was added to the annotation type definition after
the annotation was compiled (or serialized). This exception will not be
thrown if the new element has a default value.
This exception can be thrown by the

API used to read annotations
reflectively

.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public IncompleteAnnotationException​(
Class
<? extends
Annotation
> annotationType,

String
elementName)

Constructs an IncompleteAnnotationException to indicate that
the named element was missing from the specified annotation type.

**Parameters:**
- annotationType

- the Class object for the annotation type
- elementName

- the name of the missing element

**Throws:**
- NullPointerException

- if either parameter is

null

---

### Method Details

#### public
Class
<? extends
Annotation
> annotationType()

Returns the Class object for the annotation type with the
missing element.

**Returns:**
- the Class object for the annotation type with the
missing element

---

#### public
String
elementName()

Returns the name of the missing element.

**Returns:**
- the name of the missing element

---

### Additional Sections

#### Class IncompleteAnnotationException

java.lang.Object

- java.lang.Throwable
- - java.lang.Exception
- - java.lang.RuntimeException
- - java.lang.annotation.IncompleteAnnotationException

java.lang.Throwable

- java.lang.Exception
- - java.lang.RuntimeException
- - java.lang.annotation.IncompleteAnnotationException

java.lang.Exception

- java.lang.RuntimeException
- - java.lang.annotation.IncompleteAnnotationException

java.lang.RuntimeException

- java.lang.annotation.IncompleteAnnotationException

java.lang.annotation.IncompleteAnnotationException

**All Implemented Interfaces:** Serializable

```java
public class
IncompleteAnnotationException

extends
RuntimeException
```

Thrown to indicate that a program has attempted to access an element of
an annotation type that was added to the annotation type definition after
the annotation was compiled (or serialized). This exception will not be
thrown if the new element has a default value.
This exception can be thrown by the

API used to read annotations
reflectively

.

**Since:** 1.5
**See Also:** AnnotatedElement

,

Serialized Form

public class

IncompleteAnnotationException

extends

RuntimeException

Thrown to indicate that a program has attempted to access an element of
an annotation type that was added to the annotation type definition after
the annotation was compiled (or serialized). This exception will not be
thrown if the new element has a default value.
This exception can be thrown by the

API used to read annotations
reflectively

.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

IncompleteAnnotationException

​(

Class

<? extends

Annotation

> annotationType,

String

elementName)

Constructs an IncompleteAnnotationException to indicate that
the named element was missing from the specified annotation type.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Class

<? extends

Annotation

>

annotationType

()

Returns the Class object for the annotation type with the
missing element.

String

elementName

()

Returns the name of the missing element.

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

IncompleteAnnotationException

​(

Class

<? extends

Annotation

> annotationType,

String

elementName)

Constructs an IncompleteAnnotationException to indicate that
the named element was missing from the specified annotation type.

---

#### Constructor Summary

Constructs an IncompleteAnnotationException to indicate that
the named element was missing from the specified annotation type.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Class

<? extends

Annotation

>

annotationType

()

Returns the Class object for the annotation type with the
missing element.

String

elementName

()

Returns the name of the missing element.

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

Returns the Class object for the annotation type with the
missing element.

Returns the name of the missing element.

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

- IncompleteAnnotationException

```java
public IncompleteAnnotationException​(
Class
<? extends
Annotation
> annotationType,

String
elementName)
```

Constructs an IncompleteAnnotationException to indicate that
the named element was missing from the specified annotation type.

**Parameters:** annotationType

- the Class object for the annotation type
**Parameters:** elementName

- the name of the missing element
**Throws:** NullPointerException

- if either parameter is

null

============ METHOD DETAIL ==========

- Method Detail

- annotationType

```java
public
Class
<? extends
Annotation
> annotationType()
```

Returns the Class object for the annotation type with the
missing element.

**Returns:** the Class object for the annotation type with the
missing element

- elementName

```java
public
String
elementName()
```

Returns the name of the missing element.

**Returns:** the name of the missing element

Constructor Detail

- IncompleteAnnotationException

```java
public IncompleteAnnotationException​(
Class
<? extends
Annotation
> annotationType,

String
elementName)
```

Constructs an IncompleteAnnotationException to indicate that
the named element was missing from the specified annotation type.

**Parameters:** annotationType

- the Class object for the annotation type
**Parameters:** elementName

- the name of the missing element
**Throws:** NullPointerException

- if either parameter is

null

---

#### Constructor Detail

IncompleteAnnotationException

```java
public IncompleteAnnotationException​(
Class
<? extends
Annotation
> annotationType,

String
elementName)
```

Constructs an IncompleteAnnotationException to indicate that
the named element was missing from the specified annotation type.

**Parameters:** annotationType

- the Class object for the annotation type
**Parameters:** elementName

- the name of the missing element
**Throws:** NullPointerException

- if either parameter is

null

---

#### IncompleteAnnotationException

public IncompleteAnnotationException​(

Class

<? extends

Annotation

> annotationType,

String

elementName)

Constructs an IncompleteAnnotationException to indicate that
the named element was missing from the specified annotation type.

Method Detail

- annotationType

```java
public
Class
<? extends
Annotation
> annotationType()
```

Returns the Class object for the annotation type with the
missing element.

**Returns:** the Class object for the annotation type with the
missing element

- elementName

```java
public
String
elementName()
```

Returns the name of the missing element.

**Returns:** the name of the missing element

---

#### Method Detail

annotationType

```java
public
Class
<? extends
Annotation
> annotationType()
```

Returns the Class object for the annotation type with the
missing element.

**Returns:** the Class object for the annotation type with the
missing element

---

#### annotationType

public

Class

<? extends

Annotation

> annotationType()

Returns the Class object for the annotation type with the
missing element.

elementName

```java
public
String
elementName()
```

Returns the name of the missing element.

**Returns:** the name of the missing element

---

#### elementName

public

String

elementName()

Returns the name of the missing element.

---

