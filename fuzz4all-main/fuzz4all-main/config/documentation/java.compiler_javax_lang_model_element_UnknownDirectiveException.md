# Class UnknownDirectiveException

**Source:** `java.compiler\javax\lang\model\element\UnknownDirectiveException.html`

### Class Description

```java
public class
UnknownDirectiveException

extends
UnknownEntityException
```

Indicates that an unknown kind of module directive was encountered.
This can occur if the language evolves and new kinds of directives are
added to the

Directive

hierarchy. May be thrown by a

directive visitor

to
indicate that the visitor was created for a prior version of the language.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public UnknownDirectiveException​(
ModuleElement.Directive
d,

Object
p)

Creates a new

UnknownElementException

. The

p

parameter may be used to pass in an additional argument with
information about the context in which the unknown directive was
encountered; for example, the visit methods of

DirectiveVisitor

may pass in
their additional parameter.

**Parameters:**
- d

- the unknown directive, may be

null
- p

- an additional parameter, may be

null

---

### Method Details

#### public
ModuleElement.Directive
getUnknownDirective()

Returns the unknown directive.
The value may be unavailable if this exception has been
serialized and then read back in.

**Returns:**
- the unknown directive, or

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

#### Class UnknownDirectiveException

java.lang.Object

- java.lang.Throwable
- - java.lang.Exception
- - java.lang.RuntimeException
- - javax.lang.model.UnknownEntityException
- - javax.lang.model.element.UnknownDirectiveException

java.lang.Throwable

- java.lang.Exception
- - java.lang.RuntimeException
- - javax.lang.model.UnknownEntityException
- - javax.lang.model.element.UnknownDirectiveException

java.lang.Exception

- java.lang.RuntimeException
- - javax.lang.model.UnknownEntityException
- - javax.lang.model.element.UnknownDirectiveException

java.lang.RuntimeException

- javax.lang.model.UnknownEntityException
- - javax.lang.model.element.UnknownDirectiveException

javax.lang.model.UnknownEntityException

- javax.lang.model.element.UnknownDirectiveException

javax.lang.model.element.UnknownDirectiveException

**All Implemented Interfaces:** Serializable

```java
public class
UnknownDirectiveException

extends
UnknownEntityException
```

Indicates that an unknown kind of module directive was encountered.
This can occur if the language evolves and new kinds of directives are
added to the

Directive

hierarchy. May be thrown by a

directive visitor

to
indicate that the visitor was created for a prior version of the language.

**Since:** 9
**See Also:** ModuleElement.DirectiveVisitor.visitUnknown(javax.lang.model.element.ModuleElement.Directive, P)

,

Serialized Form

public class

UnknownDirectiveException

extends

UnknownEntityException

Indicates that an unknown kind of module directive was encountered.
This can occur if the language evolves and new kinds of directives are
added to the

Directive

hierarchy. May be thrown by a

directive visitor

to
indicate that the visitor was created for a prior version of the language.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

UnknownDirectiveException

​(

ModuleElement.Directive

d,

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

ModuleElement.Directive

getUnknownDirective

()

Returns the unknown directive.

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

UnknownDirectiveException

​(

ModuleElement.Directive

d,

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

ModuleElement.Directive

getUnknownDirective

()

Returns the unknown directive.

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

Returns the unknown directive.

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

- UnknownDirectiveException

```java
public UnknownDirectiveException​(
ModuleElement.Directive
d,

Object
p)
```

Creates a new

UnknownElementException

. The

p

parameter may be used to pass in an additional argument with
information about the context in which the unknown directive was
encountered; for example, the visit methods of

DirectiveVisitor

may pass in
their additional parameter.

**Parameters:** d

- the unknown directive, may be

null
**Parameters:** p

- an additional parameter, may be

null

============ METHOD DETAIL ==========

- Method Detail

- getUnknownDirective

```java
public
ModuleElement.Directive
getUnknownDirective()
```

Returns the unknown directive.
The value may be unavailable if this exception has been
serialized and then read back in.

**Returns:** the unknown directive, or

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

- UnknownDirectiveException

```java
public UnknownDirectiveException​(
ModuleElement.Directive
d,

Object
p)
```

Creates a new

UnknownElementException

. The

p

parameter may be used to pass in an additional argument with
information about the context in which the unknown directive was
encountered; for example, the visit methods of

DirectiveVisitor

may pass in
their additional parameter.

**Parameters:** d

- the unknown directive, may be

null
**Parameters:** p

- an additional parameter, may be

null

---

#### Constructor Detail

UnknownDirectiveException

```java
public UnknownDirectiveException​(
ModuleElement.Directive
d,

Object
p)
```

Creates a new

UnknownElementException

. The

p

parameter may be used to pass in an additional argument with
information about the context in which the unknown directive was
encountered; for example, the visit methods of

DirectiveVisitor

may pass in
their additional parameter.

**Parameters:** d

- the unknown directive, may be

null
**Parameters:** p

- an additional parameter, may be

null

---

#### UnknownDirectiveException

public UnknownDirectiveException​(

ModuleElement.Directive

d,

Object

p)

Creates a new

UnknownElementException

. The

p

parameter may be used to pass in an additional argument with
information about the context in which the unknown directive was
encountered; for example, the visit methods of

DirectiveVisitor

may pass in
their additional parameter.

Method Detail

- getUnknownDirective

```java
public
ModuleElement.Directive
getUnknownDirective()
```

Returns the unknown directive.
The value may be unavailable if this exception has been
serialized and then read back in.

**Returns:** the unknown directive, or

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

getUnknownDirective

```java
public
ModuleElement.Directive
getUnknownDirective()
```

Returns the unknown directive.
The value may be unavailable if this exception has been
serialized and then read back in.

**Returns:** the unknown directive, or

null

if unavailable

---

#### getUnknownDirective

public

ModuleElement.Directive

getUnknownDirective()

Returns the unknown directive.
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

