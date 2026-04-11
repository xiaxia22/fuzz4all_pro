# Class UnknownTreeException

**Source:** `jdk.scripting.nashorn\jdk\nashorn\api\tree\UnknownTreeException.html`

### Class Description

```java
@Deprecated
(
since
="11",

forRemoval
=true)
public class
UnknownTreeException

extends
RuntimeException
```

Indicates that an unknown kind of Tree was encountered. This
can occur if the language evolves and new kinds of Trees are
added to the

Tree

hierarchy. May be thrown by a

tree visitor

to indicate that the
visitor was created for a prior version of the language.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public UnknownTreeException​(
Tree
t,

Object
p)

Creates a new

UnknownTreeException

. The

p

parameter may be used to pass in an additional argument with
information about the context in which the unknown element was
encountered; for example, the visit methods of

TreeVisitor

may pass in their additional parameter.

**Parameters:**
- t

- the unknown tree, may be

null
- p

- an additional parameter, may be

null

---

### Method Details

#### public
Tree
getUnknownTree()

Returns the unknown tree.
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
The value may be unavailable if this exception has been
serialized and then read back in.

**Returns:**
- the additional argument

---

### Additional Sections

#### Class UnknownTreeException

java.lang.Object

- java.lang.Throwable
- - java.lang.Exception
- - java.lang.RuntimeException
- - jdk.nashorn.api.tree.UnknownTreeException

java.lang.Throwable

- java.lang.Exception
- - java.lang.RuntimeException
- - jdk.nashorn.api.tree.UnknownTreeException

java.lang.Exception

- java.lang.RuntimeException
- - jdk.nashorn.api.tree.UnknownTreeException

java.lang.RuntimeException

- jdk.nashorn.api.tree.UnknownTreeException

jdk.nashorn.api.tree.UnknownTreeException

**All Implemented Interfaces:** Serializable

```java
@Deprecated
(
since
="11",

forRemoval
=true)
public class
UnknownTreeException

extends
RuntimeException
```

Deprecated, for removal: This API element is subject to removal in a future version.

Nashorn JavaScript script engine and APIs, and the jjs tool
are deprecated with the intent to remove them in a future release.

Indicates that an unknown kind of Tree was encountered. This
can occur if the language evolves and new kinds of Trees are
added to the

Tree

hierarchy. May be thrown by a

tree visitor

to indicate that the
visitor was created for a prior version of the language.

**Since:** 9
**See Also:** Serialized Form

@Deprecated

(

since

="11",

forRemoval

=true)
public class

UnknownTreeException

extends

RuntimeException

Indicates that an unknown kind of Tree was encountered. This
can occur if the language evolves and new kinds of Trees are
added to the

Tree

hierarchy. May be thrown by a

tree visitor

to indicate that the
visitor was created for a prior version of the language.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

UnknownTreeException

​(

Tree

t,

Object

p)

Deprecated, for removal: This API element is subject to removal in a future version.

Creates a new

UnknownTreeException

.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Deprecated Methods

Modifier and Type

Method

Description

Object

getArgument

()

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the additional argument.

Tree

getUnknownTree

()

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the unknown tree.

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

UnknownTreeException

​(

Tree

t,

Object

p)

Deprecated, for removal: This API element is subject to removal in a future version.

Creates a new

UnknownTreeException

.

---

#### Constructor Summary

Deprecated, for removal: This API element is subject to removal in a future version.

Creates a new

UnknownTreeException

.

Method Summary

All Methods

Instance Methods

Concrete Methods

Deprecated Methods

Modifier and Type

Method

Description

Object

getArgument

()

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the additional argument.

Tree

getUnknownTree

()

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the unknown tree.

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

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the additional argument.

Returns the unknown tree.

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

- UnknownTreeException

```java
public UnknownTreeException​(
Tree
t,

Object
p)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Creates a new

UnknownTreeException

. The

p

parameter may be used to pass in an additional argument with
information about the context in which the unknown element was
encountered; for example, the visit methods of

TreeVisitor

may pass in their additional parameter.

**Parameters:** t

- the unknown tree, may be

null
**Parameters:** p

- an additional parameter, may be

null

============ METHOD DETAIL ==========

- Method Detail

- getUnknownTree

```java
public
Tree
getUnknownTree()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the unknown tree.
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

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the additional argument.
The value may be unavailable if this exception has been
serialized and then read back in.

**Returns:** the additional argument

Constructor Detail

- UnknownTreeException

```java
public UnknownTreeException​(
Tree
t,

Object
p)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Creates a new

UnknownTreeException

. The

p

parameter may be used to pass in an additional argument with
information about the context in which the unknown element was
encountered; for example, the visit methods of

TreeVisitor

may pass in their additional parameter.

**Parameters:** t

- the unknown tree, may be

null
**Parameters:** p

- an additional parameter, may be

null

---

#### Constructor Detail

UnknownTreeException

```java
public UnknownTreeException​(
Tree
t,

Object
p)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Creates a new

UnknownTreeException

. The

p

parameter may be used to pass in an additional argument with
information about the context in which the unknown element was
encountered; for example, the visit methods of

TreeVisitor

may pass in their additional parameter.

**Parameters:** t

- the unknown tree, may be

null
**Parameters:** p

- an additional parameter, may be

null

---

#### UnknownTreeException

public UnknownTreeException​(

Tree

t,

Object

p)

Creates a new

UnknownTreeException

. The

p

parameter may be used to pass in an additional argument with
information about the context in which the unknown element was
encountered; for example, the visit methods of

TreeVisitor

may pass in their additional parameter.

Method Detail

- getUnknownTree

```java
public
Tree
getUnknownTree()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the unknown tree.
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

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the additional argument.
The value may be unavailable if this exception has been
serialized and then read back in.

**Returns:** the additional argument

---

#### Method Detail

getUnknownTree

```java
public
Tree
getUnknownTree()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the unknown tree.
The value may be unavailable if this exception has been
serialized and then read back in.

**Returns:** the unknown element, or

null

if unavailable

---

#### getUnknownTree

public

Tree

getUnknownTree()

Returns the unknown tree.
The value may be unavailable if this exception has been
serialized and then read back in.

getArgument

```java
public
Object
getArgument()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the additional argument.
The value may be unavailable if this exception has been
serialized and then read back in.

**Returns:** the additional argument

---

#### getArgument

public

Object

getArgument()

Returns the additional argument.
The value may be unavailable if this exception has been
serialized and then read back in.

---

