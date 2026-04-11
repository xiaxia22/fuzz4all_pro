# Class UnknownElementException

**Source:** `java.compiler\javax\lang\model\element\UnknownElementException.html`

### Class Description

```java
public class
UnknownElementException

extends
UnknownEntityException
```

Indicates that an unknown kind of element was encountered. This
can occur if the language evolves and new kinds of elements are
added to the

Element

hierarchy. May be thrown by an

element visitor

to indicate that the
visitor was created for a prior version of the language.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public UnknownElementException​(
Element
e,

Object
p)

Creates a new

UnknownElementException

. The

p

parameter may be used to pass in an additional argument with
information about the context in which the unknown element was
encountered; for example, the visit methods of

ElementVisitor

may pass in their additional parameter.

**Parameters:**
- e

- the unknown element, may be

null
- p

- an additional parameter, may be

null

---

### Method Details

#### public
Element
getUnknownElement()

Returns the unknown element.
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

#### Class UnknownElementException

java.lang.Object

- java.lang.Throwable
- - java.lang.Exception
- - java.lang.RuntimeException
- - javax.lang.model.UnknownEntityException
- - javax.lang.model.element.UnknownElementException

java.lang.Throwable

- java.lang.Exception
- - java.lang.RuntimeException
- - javax.lang.model.UnknownEntityException
- - javax.lang.model.element.UnknownElementException

java.lang.Exception

- java.lang.RuntimeException
- - javax.lang.model.UnknownEntityException
- - javax.lang.model.element.UnknownElementException

java.lang.RuntimeException

- javax.lang.model.UnknownEntityException
- - javax.lang.model.element.UnknownElementException

javax.lang.model.UnknownEntityException

- javax.lang.model.element.UnknownElementException

javax.lang.model.element.UnknownElementException

**All Implemented Interfaces:** Serializable

```java
public class
UnknownElementException

extends
UnknownEntityException
```

Indicates that an unknown kind of element was encountered. This
can occur if the language evolves and new kinds of elements are
added to the

Element

hierarchy. May be thrown by an

element visitor

to indicate that the
visitor was created for a prior version of the language.

**Since:** 1.6
**See Also:** ElementVisitor.visitUnknown(javax.lang.model.element.Element, P)

,

Serialized Form

public class

UnknownElementException

extends

UnknownEntityException

Indicates that an unknown kind of element was encountered. This
can occur if the language evolves and new kinds of elements are
added to the

Element

hierarchy. May be thrown by an

element visitor

to indicate that the
visitor was created for a prior version of the language.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

UnknownElementException

​(

Element

e,

Object

p)

Creates a new

UnknownElementException

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

Element

getUnknownElement

()

Returns the unknown element.

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

UnknownElementException

​(

Element

e,

Object

p)

Creates a new

UnknownElementException

.

---

#### Constructor Summary

Creates a new

UnknownElementException

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

Element

getUnknownElement

()

Returns the unknown element.

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

Returns the unknown element.

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

- UnknownElementException

```java
public UnknownElementException​(
Element
e,

Object
p)
```

Creates a new

UnknownElementException

. The

p

parameter may be used to pass in an additional argument with
information about the context in which the unknown element was
encountered; for example, the visit methods of

ElementVisitor

may pass in their additional parameter.

**Parameters:** e

- the unknown element, may be

null
**Parameters:** p

- an additional parameter, may be

null

============ METHOD DETAIL ==========

- Method Detail

- getUnknownElement

```java
public
Element
getUnknownElement()
```

Returns the unknown element.
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

- UnknownElementException

```java
public UnknownElementException​(
Element
e,

Object
p)
```

Creates a new

UnknownElementException

. The

p

parameter may be used to pass in an additional argument with
information about the context in which the unknown element was
encountered; for example, the visit methods of

ElementVisitor

may pass in their additional parameter.

**Parameters:** e

- the unknown element, may be

null
**Parameters:** p

- an additional parameter, may be

null

---

#### Constructor Detail

UnknownElementException

```java
public UnknownElementException​(
Element
e,

Object
p)
```

Creates a new

UnknownElementException

. The

p

parameter may be used to pass in an additional argument with
information about the context in which the unknown element was
encountered; for example, the visit methods of

ElementVisitor

may pass in their additional parameter.

**Parameters:** e

- the unknown element, may be

null
**Parameters:** p

- an additional parameter, may be

null

---

#### UnknownElementException

public UnknownElementException​(

Element

e,

Object

p)

Creates a new

UnknownElementException

. The

p

parameter may be used to pass in an additional argument with
information about the context in which the unknown element was
encountered; for example, the visit methods of

ElementVisitor

may pass in their additional parameter.

Method Detail

- getUnknownElement

```java
public
Element
getUnknownElement()
```

Returns the unknown element.
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

getUnknownElement

```java
public
Element
getUnknownElement()
```

Returns the unknown element.
The value may be unavailable if this exception has been
serialized and then read back in.

**Returns:** the unknown element, or

null

if unavailable

---

#### getUnknownElement

public

Element

getUnknownElement()

Returns the unknown element.
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

