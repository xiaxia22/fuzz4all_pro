# Class UnknownAnnotationValueException

**Source:** `java.compiler\javax\lang\model\element\UnknownAnnotationValueException.html`

### Class Description

```java
public class
UnknownAnnotationValueException

extends
UnknownEntityException
```

Indicates that an unknown kind of annotation value was encountered.
This can occur if the language evolves and new kinds of annotation
values can be stored in an annotation. May be thrown by an

annotation value visitor

to
indicate that the visitor was created for a prior version of the
language.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public UnknownAnnotationValueException​(
AnnotationValue
av,

Object
p)

Creates a new

UnknownAnnotationValueException

. The

p

parameter may be used to pass in an additional
argument with information about the context in which the
unknown annotation value was encountered; for example, the
visit methods of

AnnotationValueVisitor

may pass in
their additional parameter.

**Parameters:**
- av

- the unknown annotation value, may be

null
- p

- an additional parameter, may be

null

---

### Method Details

#### public
AnnotationValue
getUnknownAnnotationValue()

Returns the unknown annotation value.
The value may be unavailable if this exception has been
serialized and then read back in.

**Returns:**
- the unknown element, or

null

if unavailable

---

#### public
Object
getArgument()

Returns the additional argument.

**Returns:**
- the additional argument, or

null

if unavailable

---

### Additional Sections

#### Class UnknownAnnotationValueException

java.lang.Object

- java.lang.Throwable
- - java.lang.Exception
- - java.lang.RuntimeException
- - javax.lang.model.UnknownEntityException
- - javax.lang.model.element.UnknownAnnotationValueException

java.lang.Throwable

- java.lang.Exception
- - java.lang.RuntimeException
- - javax.lang.model.UnknownEntityException
- - javax.lang.model.element.UnknownAnnotationValueException

java.lang.Exception

- java.lang.RuntimeException
- - javax.lang.model.UnknownEntityException
- - javax.lang.model.element.UnknownAnnotationValueException

java.lang.RuntimeException

- javax.lang.model.UnknownEntityException
- - javax.lang.model.element.UnknownAnnotationValueException

javax.lang.model.UnknownEntityException

- javax.lang.model.element.UnknownAnnotationValueException

javax.lang.model.element.UnknownAnnotationValueException

**All Implemented Interfaces:** Serializable

```java
public class
UnknownAnnotationValueException

extends
UnknownEntityException
```

Indicates that an unknown kind of annotation value was encountered.
This can occur if the language evolves and new kinds of annotation
values can be stored in an annotation. May be thrown by an

annotation value visitor

to
indicate that the visitor was created for a prior version of the
language.

**Since:** 1.6
**See Also:** AnnotationValueVisitor.visitUnknown(javax.lang.model.element.AnnotationValue, P)

,

Serialized Form

public class

UnknownAnnotationValueException

extends

UnknownEntityException

Indicates that an unknown kind of annotation value was encountered.
This can occur if the language evolves and new kinds of annotation
values can be stored in an annotation. May be thrown by an

annotation value visitor

to
indicate that the visitor was created for a prior version of the
language.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

UnknownAnnotationValueException

​(

AnnotationValue

av,

Object

p)

Creates a new

UnknownAnnotationValueException

.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Object

getArgument

()

Returns the additional argument.

AnnotationValue

getUnknownAnnotationValue

()

Returns the unknown annotation value.

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

UnknownAnnotationValueException

​(

AnnotationValue

av,

Object

p)

Creates a new

UnknownAnnotationValueException

.

---

#### Constructor Summary

Creates a new

UnknownAnnotationValueException

.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Object

getArgument

()

Returns the additional argument.

AnnotationValue

getUnknownAnnotationValue

()

Returns the unknown annotation value.

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

Returns the additional argument.

Returns the unknown annotation value.

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

- UnknownAnnotationValueException

```java
public UnknownAnnotationValueException​(
AnnotationValue
av,

Object
p)
```

Creates a new

UnknownAnnotationValueException

. The

p

parameter may be used to pass in an additional
argument with information about the context in which the
unknown annotation value was encountered; for example, the
visit methods of

AnnotationValueVisitor

may pass in
their additional parameter.

**Parameters:** av

- the unknown annotation value, may be

null
**Parameters:** p

- an additional parameter, may be

null

============ METHOD DETAIL ==========

- Method Detail

- getUnknownAnnotationValue

```java
public
AnnotationValue
getUnknownAnnotationValue()
```

Returns the unknown annotation value.
The value may be unavailable if this exception has been
serialized and then read back in.

**Returns:** the unknown element, or

null

if unavailable

- getArgument

```java
public
Object
getArgument()
```

Returns the additional argument.

**Returns:** the additional argument, or

null

if unavailable

Constructor Detail

- UnknownAnnotationValueException

```java
public UnknownAnnotationValueException​(
AnnotationValue
av,

Object
p)
```

Creates a new

UnknownAnnotationValueException

. The

p

parameter may be used to pass in an additional
argument with information about the context in which the
unknown annotation value was encountered; for example, the
visit methods of

AnnotationValueVisitor

may pass in
their additional parameter.

**Parameters:** av

- the unknown annotation value, may be

null
**Parameters:** p

- an additional parameter, may be

null

---

#### Constructor Detail

UnknownAnnotationValueException

```java
public UnknownAnnotationValueException​(
AnnotationValue
av,

Object
p)
```

Creates a new

UnknownAnnotationValueException

. The

p

parameter may be used to pass in an additional
argument with information about the context in which the
unknown annotation value was encountered; for example, the
visit methods of

AnnotationValueVisitor

may pass in
their additional parameter.

**Parameters:** av

- the unknown annotation value, may be

null
**Parameters:** p

- an additional parameter, may be

null

---

#### UnknownAnnotationValueException

public UnknownAnnotationValueException​(

AnnotationValue

av,

Object

p)

Creates a new

UnknownAnnotationValueException

. The

p

parameter may be used to pass in an additional
argument with information about the context in which the
unknown annotation value was encountered; for example, the
visit methods of

AnnotationValueVisitor

may pass in
their additional parameter.

Method Detail

- getUnknownAnnotationValue

```java
public
AnnotationValue
getUnknownAnnotationValue()
```

Returns the unknown annotation value.
The value may be unavailable if this exception has been
serialized and then read back in.

**Returns:** the unknown element, or

null

if unavailable

- getArgument

```java
public
Object
getArgument()
```

Returns the additional argument.

**Returns:** the additional argument, or

null

if unavailable

---

#### Method Detail

getUnknownAnnotationValue

```java
public
AnnotationValue
getUnknownAnnotationValue()
```

Returns the unknown annotation value.
The value may be unavailable if this exception has been
serialized and then read back in.

**Returns:** the unknown element, or

null

if unavailable

---

#### getUnknownAnnotationValue

public

AnnotationValue

getUnknownAnnotationValue()

Returns the unknown annotation value.
The value may be unavailable if this exception has been
serialized and then read back in.

getArgument

```java
public
Object
getArgument()
```

Returns the additional argument.

**Returns:** the additional argument, or

null

if unavailable

---

#### getArgument

public

Object

getArgument()

Returns the additional argument.

---

