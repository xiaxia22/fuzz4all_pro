# Class NamedOperation

**Source:** `jdk.dynalink\jdk\dynalink\NamedOperation.html`

### Class Description

```java
public final class
NamedOperation

extends
Object

implements
Operation
```

Operation that associates a name with another operation. Typically used with
operations that normally take a name or an index to bind them to a fixed
name. E.g.

```java
new NamedOperation(
new NamespaceOperation(
StandardOperation.GET,
StandardNamespace.PROPERTY),
"color")
```

will be a named operation for getting the property named "color" on the
object it is applied to, and

```java
new NamedOperation(
new NamespaceOperation(
StandardOperation.GET,
StandardNamespace.ELEMENT),
3)
```

will be a named operation for getting the element at index 3 from the collection
it is applied to ("name" in this context is akin to "address" and encompasses both
textual names, numeric indices, or any other kinds of addressing that linkers can
understand). In these cases, the expected signature of the call site for the
operation will change to no longer include the name parameter. Specifically,
the documentation for all

StandardOperation

members describes how
they are affected by being incorporated into a named operation.

While

NamedOperation

can be constructed directly, it is often convenient
to use the

Operation.named(Object)

factory method instead, e.g.:

```java
StandardOperation.GET
.withNamespace(StandardNamespace.ELEMENT),
.named(3)
)
```

Even though

NamedOperation

is most often used with

NamespaceOperation

as
its base, it can have other operations as its base too (except another named operation).
Specifically,

StandardOperation.CALL

as well as

StandardOperation.NEW

can
both be used with

NamedOperation

directly. The contract for these operations is such
that when they are used as named operations, their name is only used for diagnostic messages,
usually containing the textual representation of the source expression that retrieved the
callee, e.g.

StandardOperation.CALL.named("window.open")

.

**All Implemented Interfaces:** Operation

---

### Field Details

*No entries found.*

### Constructor Details

#### public NamedOperation​(
Operation
baseOperation,

Object
name)

Creates a new named operation.

**Parameters:**
- baseOperation

- the base operation that is associated with a name.
- name

- the name associated with the base operation. Note that the
name is not necessarily a string, but can be an arbitrary object. As the
name is used for addressing, it can be an

Integer

when meant
to be used as an index into an array or list etc.

**Throws:**
- NullPointerException

- if either

baseOperation

or

name

is null.
- IllegalArgumentException

- if

baseOperation

is itself a

NamedOperation

.

---

### Method Details

#### public
Operation
getBaseOperation()

Returns the base operation of this named operation.

**Returns:**
- the base operation of this named operation.

---

#### public
Object
getName()

Returns the name of this named operation.

**Returns:**
- the name of this named operation.

---

#### public final
NamedOperation
changeName​(
String
newName)

Finds or creates a named operation that differs from this one only in the name.

**Parameters:**
- newName

- the new name to replace the old name with.

**Returns:**
- a named operation with the changed name.

**Throws:**
- NullPointerException

- if the name is null.

---

#### public boolean equals​(
Object
obj)

Compares this named operation to another object. Returns true if the
other object is also a named operation, and both their base operations
and name are equal.

**Overrides:**
- equals

in class

Object

**Parameters:**
- obj

- the reference object with which to compare.

**Returns:**
- true

if this object is the same as the obj
argument;

false

otherwise.

**See Also:**
- Object.hashCode()

,

HashMap

---

#### public int hashCode()

Returns the hash code of this named operation. It is defined to be equal
to

baseOperation.hashCode() + 31 * name.hashCode()

.

**Overrides:**
- hashCode

in class

Object

**Returns:**
- a hash code value for this object.

**See Also:**
- Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### public
String
toString()

Returns the string representation of this named operation. It is defined
to be equal to

baseOperation.toString() + ":" + name.toString()

.

**Overrides:**
- toString

in class

Object

**Returns:**
- a string representation of the object.

---

#### public static
Operation
getBaseOperation​(
Operation
op)

If the passed operation is a named operation, returns its

getBaseOperation()

, otherwise returns the operation as is.

**Parameters:**
- op

- the operation

**Returns:**
- the base operation of the passed operation.

---

#### public static
Object
getName​(
Operation
op)

If the passed operation is a named operation, returns its

getName()

, otherwise returns null. Note that a named operation
object can never have a null name, therefore returning null is indicative
that the passed operation is not, in fact, a named operation.

**Parameters:**
- op

- the operation

**Returns:**
- the name in the passed operation, or null if it is not a named
operation.

---

### Additional Sections

#### Class NamedOperation

java.lang.Object

- jdk.dynalink.NamedOperation

jdk.dynalink.NamedOperation

**All Implemented Interfaces:** Operation

```java
public final class
NamedOperation

extends
Object

implements
Operation
```

Operation that associates a name with another operation. Typically used with
operations that normally take a name or an index to bind them to a fixed
name. E.g.

```java
new NamedOperation(
new NamespaceOperation(
StandardOperation.GET,
StandardNamespace.PROPERTY),
"color")
```

will be a named operation for getting the property named "color" on the
object it is applied to, and

```java
new NamedOperation(
new NamespaceOperation(
StandardOperation.GET,
StandardNamespace.ELEMENT),
3)
```

will be a named operation for getting the element at index 3 from the collection
it is applied to ("name" in this context is akin to "address" and encompasses both
textual names, numeric indices, or any other kinds of addressing that linkers can
understand). In these cases, the expected signature of the call site for the
operation will change to no longer include the name parameter. Specifically,
the documentation for all

StandardOperation

members describes how
they are affected by being incorporated into a named operation.

While

NamedOperation

can be constructed directly, it is often convenient
to use the

Operation.named(Object)

factory method instead, e.g.:

```java
StandardOperation.GET
.withNamespace(StandardNamespace.ELEMENT),
.named(3)
)
```

Even though

NamedOperation

is most often used with

NamespaceOperation

as
its base, it can have other operations as its base too (except another named operation).
Specifically,

StandardOperation.CALL

as well as

StandardOperation.NEW

can
both be used with

NamedOperation

directly. The contract for these operations is such
that when they are used as named operations, their name is only used for diagnostic messages,
usually containing the textual representation of the source expression that retrieved the
callee, e.g.

StandardOperation.CALL.named("window.open")

.

public final class

NamedOperation

extends

Object

implements

Operation

Operation that associates a name with another operation. Typically used with
operations that normally take a name or an index to bind them to a fixed
name. E.g.

```java
new NamedOperation(
new NamespaceOperation(
StandardOperation.GET,
StandardNamespace.PROPERTY),
"color")
```

will be a named operation for getting the property named "color" on the
object it is applied to, and

```java
new NamedOperation(
new NamespaceOperation(
StandardOperation.GET,
StandardNamespace.ELEMENT),
3)
```

will be a named operation for getting the element at index 3 from the collection
it is applied to ("name" in this context is akin to "address" and encompasses both
textual names, numeric indices, or any other kinds of addressing that linkers can
understand). In these cases, the expected signature of the call site for the
operation will change to no longer include the name parameter. Specifically,
the documentation for all

StandardOperation

members describes how
they are affected by being incorporated into a named operation.

While

NamedOperation

can be constructed directly, it is often convenient
to use the

Operation.named(Object)

factory method instead, e.g.:

```java
StandardOperation.GET
.withNamespace(StandardNamespace.ELEMENT),
.named(3)
)
```

Even though

NamedOperation

is most often used with

NamespaceOperation

as
its base, it can have other operations as its base too (except another named operation).
Specifically,

StandardOperation.CALL

as well as

StandardOperation.NEW

can
both be used with

NamedOperation

directly. The contract for these operations is such
that when they are used as named operations, their name is only used for diagnostic messages,
usually containing the textual representation of the source expression that retrieved the
callee, e.g.

StandardOperation.CALL.named("window.open")

.

new NamedOperation(
new NamespaceOperation(
StandardOperation.GET,
StandardNamespace.PROPERTY),
"color")

new NamedOperation(
new NamespaceOperation(
StandardOperation.GET,
StandardNamespace.ELEMENT),
3)

While

NamedOperation

can be constructed directly, it is often convenient
to use the

Operation.named(Object)

factory method instead, e.g.:

```java
StandardOperation.GET
.withNamespace(StandardNamespace.ELEMENT),
.named(3)
)
```

Even though

NamedOperation

is most often used with

NamespaceOperation

as
its base, it can have other operations as its base too (except another named operation).
Specifically,

StandardOperation.CALL

as well as

StandardOperation.NEW

can
both be used with

NamedOperation

directly. The contract for these operations is such
that when they are used as named operations, their name is only used for diagnostic messages,
usually containing the textual representation of the source expression that retrieved the
callee, e.g.

StandardOperation.CALL.named("window.open")

.

StandardOperation.GET
.withNamespace(StandardNamespace.ELEMENT),
.named(3)
)

Even though

NamedOperation

is most often used with

NamespaceOperation

as
its base, it can have other operations as its base too (except another named operation).
Specifically,

StandardOperation.CALL

as well as

StandardOperation.NEW

can
both be used with

NamedOperation

directly. The contract for these operations is such
that when they are used as named operations, their name is only used for diagnostic messages,
usually containing the textual representation of the source expression that retrieved the
callee, e.g.

StandardOperation.CALL.named("window.open")

.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

NamedOperation

​(

Operation

baseOperation,

Object

name)

Creates a new named operation.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

NamedOperation

changeName

​(

String

newName)

Finds or creates a named operation that differs from this one only in the name.

boolean

equals

​(

Object

obj)

Compares this named operation to another object.

Operation

getBaseOperation

()

Returns the base operation of this named operation.

static

Operation

getBaseOperation

​(

Operation

op)

If the passed operation is a named operation, returns its

getBaseOperation()

, otherwise returns the operation as is.

Object

getName

()

Returns the name of this named operation.

static

Object

getName

​(

Operation

op)

If the passed operation is a named operation, returns its

getName()

, otherwise returns null.

int

hashCode

()

Returns the hash code of this named operation.

String

toString

()

Returns the string representation of this named operation.

- Methods declared in class java.lang.

Object

clone

,

finalize

,

getClass

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

- Methods declared in interface jdk.dynalink.

Operation

named

,

withNamespace

,

withNamespaces

Constructor Summary

Constructors

Constructor

Description

NamedOperation

​(

Operation

baseOperation,

Object

name)

Creates a new named operation.

---

#### Constructor Summary

Creates a new named operation.

Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

NamedOperation

changeName

​(

String

newName)

Finds or creates a named operation that differs from this one only in the name.

boolean

equals

​(

Object

obj)

Compares this named operation to another object.

Operation

getBaseOperation

()

Returns the base operation of this named operation.

static

Operation

getBaseOperation

​(

Operation

op)

If the passed operation is a named operation, returns its

getBaseOperation()

, otherwise returns the operation as is.

Object

getName

()

Returns the name of this named operation.

static

Object

getName

​(

Operation

op)

If the passed operation is a named operation, returns its

getName()

, otherwise returns null.

int

hashCode

()

Returns the hash code of this named operation.

String

toString

()

Returns the string representation of this named operation.

- Methods declared in class java.lang.

Object

clone

,

finalize

,

getClass

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

- Methods declared in interface jdk.dynalink.

Operation

named

,

withNamespace

,

withNamespaces

---

#### Method Summary

Finds or creates a named operation that differs from this one only in the name.

Compares this named operation to another object.

Returns the base operation of this named operation.

If the passed operation is a named operation, returns its

getBaseOperation()

, otherwise returns the operation as is.

Returns the name of this named operation.

If the passed operation is a named operation, returns its

getName()

, otherwise returns null.

Returns the hash code of this named operation.

Returns the string representation of this named operation.

Methods declared in class java.lang.

Object

clone

,

finalize

,

getClass

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

Methods declared in interface jdk.dynalink.

Operation

named

,

withNamespace

,

withNamespaces

---

#### Methods declared in interface jdk.dynalink. Operation

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- NamedOperation

```java
public NamedOperation​(
Operation
baseOperation,

Object
name)
```

Creates a new named operation.

**Parameters:** baseOperation

- the base operation that is associated with a name.
**Parameters:** name

- the name associated with the base operation. Note that the
name is not necessarily a string, but can be an arbitrary object. As the
name is used for addressing, it can be an

Integer

when meant
to be used as an index into an array or list etc.
**Throws:** NullPointerException

- if either

baseOperation

or

name

is null.
**Throws:** IllegalArgumentException

- if

baseOperation

is itself a

NamedOperation

.

============ METHOD DETAIL ==========

- Method Detail

- getBaseOperation

```java
public
Operation
getBaseOperation()
```

Returns the base operation of this named operation.

**Returns:** the base operation of this named operation.

- getName

```java
public
Object
getName()
```

Returns the name of this named operation.

**Returns:** the name of this named operation.

- changeName

```java
public final
NamedOperation
changeName​(
String
newName)
```

Finds or creates a named operation that differs from this one only in the name.

**Parameters:** newName

- the new name to replace the old name with.
**Returns:** a named operation with the changed name.
**Throws:** NullPointerException

- if the name is null.

- equals

```java
public boolean equals​(
Object
obj)
```

Compares this named operation to another object. Returns true if the
other object is also a named operation, and both their base operations
and name are equal.

**Overrides:** equals

in class

Object
**Parameters:** obj

- the reference object with which to compare.
**Returns:** true

if this object is the same as the obj
argument;

false

otherwise.
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
public int hashCode()
```

Returns the hash code of this named operation. It is defined to be equal
to

baseOperation.hashCode() + 31 * name.hashCode()

.

**Overrides:** hashCode

in class

Object
**Returns:** a hash code value for this object.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

- toString

```java
public
String
toString()
```

Returns the string representation of this named operation. It is defined
to be equal to

baseOperation.toString() + ":" + name.toString()

.

**Overrides:** toString

in class

Object
**Returns:** a string representation of the object.

- getBaseOperation

```java
public static
Operation
getBaseOperation​(
Operation
op)
```

If the passed operation is a named operation, returns its

getBaseOperation()

, otherwise returns the operation as is.

**Parameters:** op

- the operation
**Returns:** the base operation of the passed operation.

- getName

```java
public static
Object
getName​(
Operation
op)
```

If the passed operation is a named operation, returns its

getName()

, otherwise returns null. Note that a named operation
object can never have a null name, therefore returning null is indicative
that the passed operation is not, in fact, a named operation.

**Parameters:** op

- the operation
**Returns:** the name in the passed operation, or null if it is not a named
operation.

Constructor Detail

- NamedOperation

```java
public NamedOperation​(
Operation
baseOperation,

Object
name)
```

Creates a new named operation.

**Parameters:** baseOperation

- the base operation that is associated with a name.
**Parameters:** name

- the name associated with the base operation. Note that the
name is not necessarily a string, but can be an arbitrary object. As the
name is used for addressing, it can be an

Integer

when meant
to be used as an index into an array or list etc.
**Throws:** NullPointerException

- if either

baseOperation

or

name

is null.
**Throws:** IllegalArgumentException

- if

baseOperation

is itself a

NamedOperation

.

---

#### Constructor Detail

NamedOperation

```java
public NamedOperation​(
Operation
baseOperation,

Object
name)
```

Creates a new named operation.

**Parameters:** baseOperation

- the base operation that is associated with a name.
**Parameters:** name

- the name associated with the base operation. Note that the
name is not necessarily a string, but can be an arbitrary object. As the
name is used for addressing, it can be an

Integer

when meant
to be used as an index into an array or list etc.
**Throws:** NullPointerException

- if either

baseOperation

or

name

is null.
**Throws:** IllegalArgumentException

- if

baseOperation

is itself a

NamedOperation

.

---

#### NamedOperation

public NamedOperation​(

Operation

baseOperation,

Object

name)

Creates a new named operation.

Method Detail

- getBaseOperation

```java
public
Operation
getBaseOperation()
```

Returns the base operation of this named operation.

**Returns:** the base operation of this named operation.

- getName

```java
public
Object
getName()
```

Returns the name of this named operation.

**Returns:** the name of this named operation.

- changeName

```java
public final
NamedOperation
changeName​(
String
newName)
```

Finds or creates a named operation that differs from this one only in the name.

**Parameters:** newName

- the new name to replace the old name with.
**Returns:** a named operation with the changed name.
**Throws:** NullPointerException

- if the name is null.

- equals

```java
public boolean equals​(
Object
obj)
```

Compares this named operation to another object. Returns true if the
other object is also a named operation, and both their base operations
and name are equal.

**Overrides:** equals

in class

Object
**Parameters:** obj

- the reference object with which to compare.
**Returns:** true

if this object is the same as the obj
argument;

false

otherwise.
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
public int hashCode()
```

Returns the hash code of this named operation. It is defined to be equal
to

baseOperation.hashCode() + 31 * name.hashCode()

.

**Overrides:** hashCode

in class

Object
**Returns:** a hash code value for this object.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

- toString

```java
public
String
toString()
```

Returns the string representation of this named operation. It is defined
to be equal to

baseOperation.toString() + ":" + name.toString()

.

**Overrides:** toString

in class

Object
**Returns:** a string representation of the object.

- getBaseOperation

```java
public static
Operation
getBaseOperation​(
Operation
op)
```

If the passed operation is a named operation, returns its

getBaseOperation()

, otherwise returns the operation as is.

**Parameters:** op

- the operation
**Returns:** the base operation of the passed operation.

- getName

```java
public static
Object
getName​(
Operation
op)
```

If the passed operation is a named operation, returns its

getName()

, otherwise returns null. Note that a named operation
object can never have a null name, therefore returning null is indicative
that the passed operation is not, in fact, a named operation.

**Parameters:** op

- the operation
**Returns:** the name in the passed operation, or null if it is not a named
operation.

---

#### Method Detail

getBaseOperation

```java
public
Operation
getBaseOperation()
```

Returns the base operation of this named operation.

**Returns:** the base operation of this named operation.

---

#### getBaseOperation

public

Operation

getBaseOperation()

Returns the base operation of this named operation.

getName

```java
public
Object
getName()
```

Returns the name of this named operation.

**Returns:** the name of this named operation.

---

#### getName

public

Object

getName()

Returns the name of this named operation.

changeName

```java
public final
NamedOperation
changeName​(
String
newName)
```

Finds or creates a named operation that differs from this one only in the name.

**Parameters:** newName

- the new name to replace the old name with.
**Returns:** a named operation with the changed name.
**Throws:** NullPointerException

- if the name is null.

---

#### changeName

public final

NamedOperation

changeName​(

String

newName)

Finds or creates a named operation that differs from this one only in the name.

equals

```java
public boolean equals​(
Object
obj)
```

Compares this named operation to another object. Returns true if the
other object is also a named operation, and both their base operations
and name are equal.

**Overrides:** equals

in class

Object
**Parameters:** obj

- the reference object with which to compare.
**Returns:** true

if this object is the same as the obj
argument;

false

otherwise.
**See Also:** Object.hashCode()

,

HashMap

---

#### equals

public boolean equals​(

Object

obj)

Compares this named operation to another object. Returns true if the
other object is also a named operation, and both their base operations
and name are equal.

hashCode

```java
public int hashCode()
```

Returns the hash code of this named operation. It is defined to be equal
to

baseOperation.hashCode() + 31 * name.hashCode()

.

**Overrides:** hashCode

in class

Object
**Returns:** a hash code value for this object.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### hashCode

public int hashCode()

Returns the hash code of this named operation. It is defined to be equal
to

baseOperation.hashCode() + 31 * name.hashCode()

.

toString

```java
public
String
toString()
```

Returns the string representation of this named operation. It is defined
to be equal to

baseOperation.toString() + ":" + name.toString()

.

**Overrides:** toString

in class

Object
**Returns:** a string representation of the object.

---

#### toString

public

String

toString()

Returns the string representation of this named operation. It is defined
to be equal to

baseOperation.toString() + ":" + name.toString()

.

getBaseOperation

```java
public static
Operation
getBaseOperation​(
Operation
op)
```

If the passed operation is a named operation, returns its

getBaseOperation()

, otherwise returns the operation as is.

**Parameters:** op

- the operation
**Returns:** the base operation of the passed operation.

---

#### getBaseOperation

public static

Operation

getBaseOperation​(

Operation

op)

If the passed operation is a named operation, returns its

getBaseOperation()

, otherwise returns the operation as is.

getName

```java
public static
Object
getName​(
Operation
op)
```

If the passed operation is a named operation, returns its

getName()

, otherwise returns null. Note that a named operation
object can never have a null name, therefore returning null is indicative
that the passed operation is not, in fact, a named operation.

**Parameters:** op

- the operation
**Returns:** the name in the passed operation, or null if it is not a named
operation.

---

#### getName

public static

Object

getName​(

Operation

op)

If the passed operation is a named operation, returns its

getName()

, otherwise returns null. Note that a named operation
object can never have a null name, therefore returning null is indicative
that the passed operation is not, in fact, a named operation.

---

