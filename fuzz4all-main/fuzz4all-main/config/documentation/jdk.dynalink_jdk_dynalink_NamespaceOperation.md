# Class NamespaceOperation

**Source:** `jdk.dynalink\jdk\dynalink\NamespaceOperation.html`

### Class Description

```java
public final class
NamespaceOperation

extends
Object

implements
Operation
```

Describes an operation that operates on at least one

Namespace

of
an object. E.g. a property getter would be described as

```java
Operation propertyGetter = new NamespaceOperation(
StandardOperation.GET,
StandardNamespace.PROPERTY);
```

They are often combined with

NamedOperation

, e.g. to express a
property getter for a property named "color", you would construct:

```java
Operation colorPropertyGetter = new NamedOperation(
new NamespaceOperation(
StandardOperation.GET,
StandardNamespace.PROPERTY),
"color");
```

While

NamespaceOperation

can be constructed directly, it is often convenient
to use the

Operation.withNamespace(Namespace)

and

Operation.withNamespaces(Namespace...)

factory
methods instead, e.g.:

```java
Operation getElementOrPropertyEmpty =
StandardOperation.GET
.withNamespace(StandardNamespace.PROPERTY)
.named("color");
```

Operations on multiple namespaces

If multiple namespaces are specified, the namespaces are treated as
alternatives to each other in order of preference. The semantics of
such operation is "first applicable".
That is, a composite of

GET:PROPERTY|ELEMENT:color

should be
interpreted as

get the property named "color" on the object, but if the
property does not exist, then get the collection element named "color"
instead

.

Operations with multiple namespaces are helpful in implementation of languages that
don't distinguish between one or more of the namespaces, or when expressing operations
against objects that can be considered both ordinary objects and collections, e.g. Java

Map

objects. A

GET:PROPERTY|ELEMENT:empty

operation
against a Java map will always match
the

Map.isEmpty()

property, but

GET:ELEMENT|PROPERTY:empty

will actually match a map element with
key

"empty"

if the map contains that key, and only fall back to the

isEmpty()

property getter if the map does not contain the key. If
the source language mandates this semantics, it can be easily achieved using
operations on multiple namespaces.

Even if the language itself doesn't distinguish between some of the
namespaces, it can be helpful to map different syntaxes to different namespace orderings.
E.g. the source expression

obj.color

could map to

GET:PROPERTY|ELEMENT|METHOD:color

, but a different source
expression that looks like collection element access

obj[key]

could
be expressed instead as

GET:ELEMENT|PROPERTY|METHOD

in order to favor the
element semantics. Finally, if the retrieved value is subsequently called, then it makes sense
to bring

METHOD

to the front of the namespace list: the getter part of the
source expression

obj.color()

could be

GET:METHOD|PROPERTY|ELEMENT:color

and the one for

obj[key]()

could be

GET:METHOD|ELEMENT|PROPERTY

.

The base operation of a namespace operation can not itself be a namespace or named
operation, but rather one of simple operations such are elements of

StandardOperation

. A namespace operation itself can serve as the base
operation of a named operation, though; a typical way to construct e.g. the

GET:ELEMENT|PROPERTY:empty

from above would be:

```java
Operation getElementOrPropertyEmpty = StandardOperation.GET
.withNamespaces(
StandardNamespace.ELEMENT,
StandardNamespace.PROPERTY)
.named("empty");
```

**All Implemented Interfaces:** Operation

---

### Field Details

*No entries found.*

### Constructor Details

#### public NamespaceOperation​(
Operation
baseOperation,

Namespace
... namespaces)

Constructs a new namespace operation.

**Parameters:**
- baseOperation

- the base operation that operates on one or more namespaces.
- namespaces

- one or more namespaces this operation operates on.

**Throws:**
- IllegalArgumentException

- if less than one namespace is
specified, or the base operation is itself a

NamespaceOperation

or a

NamedOperation

.
- NullPointerException

- if either the

namespaces

array or any of its
elements are

null

, or if

baseOperation

is

null

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
Namespace
[] getNamespaces()

Returns the namespaces in this namespace operation. The returned
array is a copy and changes to it don't have effect on this
object.

**Returns:**
- the namespaces in this namespace operation.

---

#### public int getNamespaceCount()

Returns the number of namespaces in this namespace operation.

**Returns:**
- the number of namespaces in this namespace operation.

---

#### public
Namespace
getNamespace​(int i)

Returns the i-th namespace in this namespace operation.

**Parameters:**
- i

- the namespace index

**Returns:**
- the i-th namespace in this namespace operation.

**Throws:**
- IndexOutOfBoundsException

- if the index is out of range.

---

#### public boolean contains​(
Namespace
namespace)

Returns true if this namespace operation contains a namespace equal to
the specified namespace.

**Parameters:**
- namespace

- the namespace being searched for. Must not be null.

**Returns:**
- true if the if this namespace operation contains a namespace
equal to the specified namespace.

---

#### public boolean equals​(
Object
obj)

Returns true if the other object is also a namespace operation and their
base operation and namespaces are equal.

**Overrides:**
- equals

in class

Object

**Parameters:**
- obj

- the object to compare to

**Returns:**
- true if this object is equal to the other one, false otherwise.

**See Also:**
- Object.hashCode()

,

HashMap

---

#### public int hashCode()

Returns the hash code of this namespace operation. Defined to be equal
to

baseOperation.hashCode() + 31 * Arrays.hashCode(namespaces)

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

Returns the string representation of this namespace operation. Defined to
be the

toString

of its base operation, followed by a colon character,
followed with the list of its namespaces separated with the vertical line
character (e.g.

"GET:PROPERTY|ELEMENT"

).

**Overrides:**
- toString

in class

Object

**Returns:**
- the string representation of this namespace operation.

---

#### public static
Operation
getBaseOperation​(
Operation
op)

If the passed operation is a namespace operation, returns its

getBaseOperation()

, otherwise returns the operation as is.

**Parameters:**
- op

- the operation

**Returns:**
- the base operation of the passed operation.

---

#### public static
Namespace
[] getNamespaces​(
Operation
op)

If the passed operation is a namespace operation, returns its

getNamespaces()

, otherwise returns an empty array.

**Parameters:**
- op

- the operation

**Returns:**
- the namespaces of the passed operation.

---

#### public static boolean contains​(
Operation
op,

Operation
baseOperation,

Namespace
namespace)

Returns true if the specified operation is a

NamespaceOperation

and its base operation is equal to the specified operation, and it
contains the specified namespace. If it is not a

NamespaceOperation

,
then it returns false.

**Parameters:**
- op

- the operation. Must not be null.
- baseOperation

- the base operation being searched for. Must not be null.
- namespace

- the namespace being searched for. Must not be null.

**Returns:**
- true if the if the passed operation is a

NamespaceOperation

,
its base operation equals the searched base operation, and contains a namespace
equal to the searched namespace.

---

### Additional Sections

#### Class NamespaceOperation

java.lang.Object

- jdk.dynalink.NamespaceOperation

jdk.dynalink.NamespaceOperation

**All Implemented Interfaces:** Operation

```java
public final class
NamespaceOperation

extends
Object

implements
Operation
```

Describes an operation that operates on at least one

Namespace

of
an object. E.g. a property getter would be described as

```java
Operation propertyGetter = new NamespaceOperation(
StandardOperation.GET,
StandardNamespace.PROPERTY);
```

They are often combined with

NamedOperation

, e.g. to express a
property getter for a property named "color", you would construct:

```java
Operation colorPropertyGetter = new NamedOperation(
new NamespaceOperation(
StandardOperation.GET,
StandardNamespace.PROPERTY),
"color");
```

While

NamespaceOperation

can be constructed directly, it is often convenient
to use the

Operation.withNamespace(Namespace)

and

Operation.withNamespaces(Namespace...)

factory
methods instead, e.g.:

```java
Operation getElementOrPropertyEmpty =
StandardOperation.GET
.withNamespace(StandardNamespace.PROPERTY)
.named("color");
```

Operations on multiple namespaces

If multiple namespaces are specified, the namespaces are treated as
alternatives to each other in order of preference. The semantics of
such operation is "first applicable".
That is, a composite of

GET:PROPERTY|ELEMENT:color

should be
interpreted as

get the property named "color" on the object, but if the
property does not exist, then get the collection element named "color"
instead

.

Operations with multiple namespaces are helpful in implementation of languages that
don't distinguish between one or more of the namespaces, or when expressing operations
against objects that can be considered both ordinary objects and collections, e.g. Java

Map

objects. A

GET:PROPERTY|ELEMENT:empty

operation
against a Java map will always match
the

Map.isEmpty()

property, but

GET:ELEMENT|PROPERTY:empty

will actually match a map element with
key

"empty"

if the map contains that key, and only fall back to the

isEmpty()

property getter if the map does not contain the key. If
the source language mandates this semantics, it can be easily achieved using
operations on multiple namespaces.

Even if the language itself doesn't distinguish between some of the
namespaces, it can be helpful to map different syntaxes to different namespace orderings.
E.g. the source expression

obj.color

could map to

GET:PROPERTY|ELEMENT|METHOD:color

, but a different source
expression that looks like collection element access

obj[key]

could
be expressed instead as

GET:ELEMENT|PROPERTY|METHOD

in order to favor the
element semantics. Finally, if the retrieved value is subsequently called, then it makes sense
to bring

METHOD

to the front of the namespace list: the getter part of the
source expression

obj.color()

could be

GET:METHOD|PROPERTY|ELEMENT:color

and the one for

obj[key]()

could be

GET:METHOD|ELEMENT|PROPERTY

.

The base operation of a namespace operation can not itself be a namespace or named
operation, but rather one of simple operations such are elements of

StandardOperation

. A namespace operation itself can serve as the base
operation of a named operation, though; a typical way to construct e.g. the

GET:ELEMENT|PROPERTY:empty

from above would be:

```java
Operation getElementOrPropertyEmpty = StandardOperation.GET
.withNamespaces(
StandardNamespace.ELEMENT,
StandardNamespace.PROPERTY)
.named("empty");
```

public final class

NamespaceOperation

extends

Object

implements

Operation

Describes an operation that operates on at least one

Namespace

of
an object. E.g. a property getter would be described as

```java
Operation propertyGetter = new NamespaceOperation(
StandardOperation.GET,
StandardNamespace.PROPERTY);
```

They are often combined with

NamedOperation

, e.g. to express a
property getter for a property named "color", you would construct:

```java
Operation colorPropertyGetter = new NamedOperation(
new NamespaceOperation(
StandardOperation.GET,
StandardNamespace.PROPERTY),
"color");
```

While

NamespaceOperation

can be constructed directly, it is often convenient
to use the

Operation.withNamespace(Namespace)

and

Operation.withNamespaces(Namespace...)

factory
methods instead, e.g.:

```java
Operation getElementOrPropertyEmpty =
StandardOperation.GET
.withNamespace(StandardNamespace.PROPERTY)
.named("color");
```

Operations on multiple namespaces

If multiple namespaces are specified, the namespaces are treated as
alternatives to each other in order of preference. The semantics of
such operation is "first applicable".
That is, a composite of

GET:PROPERTY|ELEMENT:color

should be
interpreted as

get the property named "color" on the object, but if the
property does not exist, then get the collection element named "color"
instead

.

Operations with multiple namespaces are helpful in implementation of languages that
don't distinguish between one or more of the namespaces, or when expressing operations
against objects that can be considered both ordinary objects and collections, e.g. Java

Map

objects. A

GET:PROPERTY|ELEMENT:empty

operation
against a Java map will always match
the

Map.isEmpty()

property, but

GET:ELEMENT|PROPERTY:empty

will actually match a map element with
key

"empty"

if the map contains that key, and only fall back to the

isEmpty()

property getter if the map does not contain the key. If
the source language mandates this semantics, it can be easily achieved using
operations on multiple namespaces.

Even if the language itself doesn't distinguish between some of the
namespaces, it can be helpful to map different syntaxes to different namespace orderings.
E.g. the source expression

obj.color

could map to

GET:PROPERTY|ELEMENT|METHOD:color

, but a different source
expression that looks like collection element access

obj[key]

could
be expressed instead as

GET:ELEMENT|PROPERTY|METHOD

in order to favor the
element semantics. Finally, if the retrieved value is subsequently called, then it makes sense
to bring

METHOD

to the front of the namespace list: the getter part of the
source expression

obj.color()

could be

GET:METHOD|PROPERTY|ELEMENT:color

and the one for

obj[key]()

could be

GET:METHOD|ELEMENT|PROPERTY

.

The base operation of a namespace operation can not itself be a namespace or named
operation, but rather one of simple operations such are elements of

StandardOperation

. A namespace operation itself can serve as the base
operation of a named operation, though; a typical way to construct e.g. the

GET:ELEMENT|PROPERTY:empty

from above would be:

```java
Operation getElementOrPropertyEmpty = StandardOperation.GET
.withNamespaces(
StandardNamespace.ELEMENT,
StandardNamespace.PROPERTY)
.named("empty");
```

Operation propertyGetter = new NamespaceOperation(
StandardOperation.GET,
StandardNamespace.PROPERTY);

Operation colorPropertyGetter = new NamedOperation(
new NamespaceOperation(
StandardOperation.GET,
StandardNamespace.PROPERTY),
"color");

While

NamespaceOperation

can be constructed directly, it is often convenient
to use the

Operation.withNamespace(Namespace)

and

Operation.withNamespaces(Namespace...)

factory
methods instead, e.g.:

```java
Operation getElementOrPropertyEmpty =
StandardOperation.GET
.withNamespace(StandardNamespace.PROPERTY)
.named("color");
```

Operations on multiple namespaces

If multiple namespaces are specified, the namespaces are treated as
alternatives to each other in order of preference. The semantics of
such operation is "first applicable".
That is, a composite of

GET:PROPERTY|ELEMENT:color

should be
interpreted as

get the property named "color" on the object, but if the
property does not exist, then get the collection element named "color"
instead

.

Operations with multiple namespaces are helpful in implementation of languages that
don't distinguish between one or more of the namespaces, or when expressing operations
against objects that can be considered both ordinary objects and collections, e.g. Java

Map

objects. A

GET:PROPERTY|ELEMENT:empty

operation
against a Java map will always match
the

Map.isEmpty()

property, but

GET:ELEMENT|PROPERTY:empty

will actually match a map element with
key

"empty"

if the map contains that key, and only fall back to the

isEmpty()

property getter if the map does not contain the key. If
the source language mandates this semantics, it can be easily achieved using
operations on multiple namespaces.

Even if the language itself doesn't distinguish between some of the
namespaces, it can be helpful to map different syntaxes to different namespace orderings.
E.g. the source expression

obj.color

could map to

GET:PROPERTY|ELEMENT|METHOD:color

, but a different source
expression that looks like collection element access

obj[key]

could
be expressed instead as

GET:ELEMENT|PROPERTY|METHOD

in order to favor the
element semantics. Finally, if the retrieved value is subsequently called, then it makes sense
to bring

METHOD

to the front of the namespace list: the getter part of the
source expression

obj.color()

could be

GET:METHOD|PROPERTY|ELEMENT:color

and the one for

obj[key]()

could be

GET:METHOD|ELEMENT|PROPERTY

.

The base operation of a namespace operation can not itself be a namespace or named
operation, but rather one of simple operations such are elements of

StandardOperation

. A namespace operation itself can serve as the base
operation of a named operation, though; a typical way to construct e.g. the

GET:ELEMENT|PROPERTY:empty

from above would be:

```java
Operation getElementOrPropertyEmpty = StandardOperation.GET
.withNamespaces(
StandardNamespace.ELEMENT,
StandardNamespace.PROPERTY)
.named("empty");
```

Operation getElementOrPropertyEmpty =
StandardOperation.GET
.withNamespace(StandardNamespace.PROPERTY)
.named("color");

---

#### Operations on multiple namespaces

Operations with multiple namespaces are helpful in implementation of languages that
don't distinguish between one or more of the namespaces, or when expressing operations
against objects that can be considered both ordinary objects and collections, e.g. Java

Map

objects. A

GET:PROPERTY|ELEMENT:empty

operation
against a Java map will always match
the

Map.isEmpty()

property, but

GET:ELEMENT|PROPERTY:empty

will actually match a map element with
key

"empty"

if the map contains that key, and only fall back to the

isEmpty()

property getter if the map does not contain the key. If
the source language mandates this semantics, it can be easily achieved using
operations on multiple namespaces.

Even if the language itself doesn't distinguish between some of the
namespaces, it can be helpful to map different syntaxes to different namespace orderings.
E.g. the source expression

obj.color

could map to

GET:PROPERTY|ELEMENT|METHOD:color

, but a different source
expression that looks like collection element access

obj[key]

could
be expressed instead as

GET:ELEMENT|PROPERTY|METHOD

in order to favor the
element semantics. Finally, if the retrieved value is subsequently called, then it makes sense
to bring

METHOD

to the front of the namespace list: the getter part of the
source expression

obj.color()

could be

GET:METHOD|PROPERTY|ELEMENT:color

and the one for

obj[key]()

could be

GET:METHOD|ELEMENT|PROPERTY

.

The base operation of a namespace operation can not itself be a namespace or named
operation, but rather one of simple operations such are elements of

StandardOperation

. A namespace operation itself can serve as the base
operation of a named operation, though; a typical way to construct e.g. the

GET:ELEMENT|PROPERTY:empty

from above would be:

```java
Operation getElementOrPropertyEmpty = StandardOperation.GET
.withNamespaces(
StandardNamespace.ELEMENT,
StandardNamespace.PROPERTY)
.named("empty");
```

Even if the language itself doesn't distinguish between some of the
namespaces, it can be helpful to map different syntaxes to different namespace orderings.
E.g. the source expression

obj.color

could map to

GET:PROPERTY|ELEMENT|METHOD:color

, but a different source
expression that looks like collection element access

obj[key]

could
be expressed instead as

GET:ELEMENT|PROPERTY|METHOD

in order to favor the
element semantics. Finally, if the retrieved value is subsequently called, then it makes sense
to bring

METHOD

to the front of the namespace list: the getter part of the
source expression

obj.color()

could be

GET:METHOD|PROPERTY|ELEMENT:color

and the one for

obj[key]()

could be

GET:METHOD|ELEMENT|PROPERTY

.

The base operation of a namespace operation can not itself be a namespace or named
operation, but rather one of simple operations such are elements of

StandardOperation

. A namespace operation itself can serve as the base
operation of a named operation, though; a typical way to construct e.g. the

GET:ELEMENT|PROPERTY:empty

from above would be:

```java
Operation getElementOrPropertyEmpty = StandardOperation.GET
.withNamespaces(
StandardNamespace.ELEMENT,
StandardNamespace.PROPERTY)
.named("empty");
```

The base operation of a namespace operation can not itself be a namespace or named
operation, but rather one of simple operations such are elements of

StandardOperation

. A namespace operation itself can serve as the base
operation of a named operation, though; a typical way to construct e.g. the

GET:ELEMENT|PROPERTY:empty

from above would be:

```java
Operation getElementOrPropertyEmpty = StandardOperation.GET
.withNamespaces(
StandardNamespace.ELEMENT,
StandardNamespace.PROPERTY)
.named("empty");
```

Operation getElementOrPropertyEmpty = StandardOperation.GET
.withNamespaces(
StandardNamespace.ELEMENT,
StandardNamespace.PROPERTY)
.named("empty");

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

NamespaceOperation

​(

Operation

baseOperation,

Namespace

... namespaces)

Constructs a new namespace operation.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

boolean

contains

​(

Namespace

namespace)

Returns true if this namespace operation contains a namespace equal to
the specified namespace.

static boolean

contains

​(

Operation

op,

Operation

baseOperation,

Namespace

namespace)

Returns true if the specified operation is a

NamespaceOperation

and its base operation is equal to the specified operation, and it
contains the specified namespace.

boolean

equals

​(

Object

obj)

Returns true if the other object is also a namespace operation and their
base operation and namespaces are equal.

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

If the passed operation is a namespace operation, returns its

getBaseOperation()

, otherwise returns the operation as is.

Namespace

getNamespace

​(int i)

Returns the i-th namespace in this namespace operation.

int

getNamespaceCount

()

Returns the number of namespaces in this namespace operation.

Namespace

[]

getNamespaces

()

Returns the namespaces in this namespace operation.

static

Namespace

[]

getNamespaces

​(

Operation

op)

If the passed operation is a namespace operation, returns its

getNamespaces()

, otherwise returns an empty array.

int

hashCode

()

Returns the hash code of this namespace operation.

String

toString

()

Returns the string representation of this namespace operation.

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

NamespaceOperation

​(

Operation

baseOperation,

Namespace

... namespaces)

Constructs a new namespace operation.

---

#### Constructor Summary

Constructs a new namespace operation.

Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

boolean

contains

​(

Namespace

namespace)

Returns true if this namespace operation contains a namespace equal to
the specified namespace.

static boolean

contains

​(

Operation

op,

Operation

baseOperation,

Namespace

namespace)

Returns true if the specified operation is a

NamespaceOperation

and its base operation is equal to the specified operation, and it
contains the specified namespace.

boolean

equals

​(

Object

obj)

Returns true if the other object is also a namespace operation and their
base operation and namespaces are equal.

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

If the passed operation is a namespace operation, returns its

getBaseOperation()

, otherwise returns the operation as is.

Namespace

getNamespace

​(int i)

Returns the i-th namespace in this namespace operation.

int

getNamespaceCount

()

Returns the number of namespaces in this namespace operation.

Namespace

[]

getNamespaces

()

Returns the namespaces in this namespace operation.

static

Namespace

[]

getNamespaces

​(

Operation

op)

If the passed operation is a namespace operation, returns its

getNamespaces()

, otherwise returns an empty array.

int

hashCode

()

Returns the hash code of this namespace operation.

String

toString

()

Returns the string representation of this namespace operation.

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

Returns true if this namespace operation contains a namespace equal to
the specified namespace.

Returns true if the specified operation is a

NamespaceOperation

and its base operation is equal to the specified operation, and it
contains the specified namespace.

Returns true if the other object is also a namespace operation and their
base operation and namespaces are equal.

Returns the base operation of this named operation.

If the passed operation is a namespace operation, returns its

getBaseOperation()

, otherwise returns the operation as is.

Returns the i-th namespace in this namespace operation.

Returns the number of namespaces in this namespace operation.

Returns the namespaces in this namespace operation.

If the passed operation is a namespace operation, returns its

getNamespaces()

, otherwise returns an empty array.

Returns the hash code of this namespace operation.

Returns the string representation of this namespace operation.

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

- NamespaceOperation

```java
public NamespaceOperation​(
Operation
baseOperation,

Namespace
... namespaces)
```

Constructs a new namespace operation.

**Parameters:** baseOperation

- the base operation that operates on one or more namespaces.
**Parameters:** namespaces

- one or more namespaces this operation operates on.
**Throws:** IllegalArgumentException

- if less than one namespace is
specified, or the base operation is itself a

NamespaceOperation

or a

NamedOperation

.
**Throws:** NullPointerException

- if either the

namespaces

array or any of its
elements are

null

, or if

baseOperation

is

null

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

- getNamespaces

```java
public
Namespace
[] getNamespaces()
```

Returns the namespaces in this namespace operation. The returned
array is a copy and changes to it don't have effect on this
object.

**Returns:** the namespaces in this namespace operation.

- getNamespaceCount

```java
public int getNamespaceCount()
```

Returns the number of namespaces in this namespace operation.

**Returns:** the number of namespaces in this namespace operation.

- getNamespace

```java
public
Namespace
getNamespace​(int i)
```

Returns the i-th namespace in this namespace operation.

**Parameters:** i

- the namespace index
**Returns:** the i-th namespace in this namespace operation.
**Throws:** IndexOutOfBoundsException

- if the index is out of range.

- contains

```java
public boolean contains​(
Namespace
namespace)
```

Returns true if this namespace operation contains a namespace equal to
the specified namespace.

**Parameters:** namespace

- the namespace being searched for. Must not be null.
**Returns:** true if the if this namespace operation contains a namespace
equal to the specified namespace.

- equals

```java
public boolean equals​(
Object
obj)
```

Returns true if the other object is also a namespace operation and their
base operation and namespaces are equal.

**Overrides:** equals

in class

Object
**Parameters:** obj

- the object to compare to
**Returns:** true if this object is equal to the other one, false otherwise.
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
public int hashCode()
```

Returns the hash code of this namespace operation. Defined to be equal
to

baseOperation.hashCode() + 31 * Arrays.hashCode(namespaces)

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

Returns the string representation of this namespace operation. Defined to
be the

toString

of its base operation, followed by a colon character,
followed with the list of its namespaces separated with the vertical line
character (e.g.

"GET:PROPERTY|ELEMENT"

).

**Overrides:** toString

in class

Object
**Returns:** the string representation of this namespace operation.

- getBaseOperation

```java
public static
Operation
getBaseOperation​(
Operation
op)
```

If the passed operation is a namespace operation, returns its

getBaseOperation()

, otherwise returns the operation as is.

**Parameters:** op

- the operation
**Returns:** the base operation of the passed operation.

- getNamespaces

```java
public static
Namespace
[] getNamespaces​(
Operation
op)
```

If the passed operation is a namespace operation, returns its

getNamespaces()

, otherwise returns an empty array.

**Parameters:** op

- the operation
**Returns:** the namespaces of the passed operation.

- contains

```java
public static boolean contains​(
Operation
op,

Operation
baseOperation,

Namespace
namespace)
```

Returns true if the specified operation is a

NamespaceOperation

and its base operation is equal to the specified operation, and it
contains the specified namespace. If it is not a

NamespaceOperation

,
then it returns false.

**Parameters:** op

- the operation. Must not be null.
**Parameters:** baseOperation

- the base operation being searched for. Must not be null.
**Parameters:** namespace

- the namespace being searched for. Must not be null.
**Returns:** true if the if the passed operation is a

NamespaceOperation

,
its base operation equals the searched base operation, and contains a namespace
equal to the searched namespace.

Constructor Detail

- NamespaceOperation

```java
public NamespaceOperation​(
Operation
baseOperation,

Namespace
... namespaces)
```

Constructs a new namespace operation.

**Parameters:** baseOperation

- the base operation that operates on one or more namespaces.
**Parameters:** namespaces

- one or more namespaces this operation operates on.
**Throws:** IllegalArgumentException

- if less than one namespace is
specified, or the base operation is itself a

NamespaceOperation

or a

NamedOperation

.
**Throws:** NullPointerException

- if either the

namespaces

array or any of its
elements are

null

, or if

baseOperation

is

null

.

---

#### Constructor Detail

NamespaceOperation

```java
public NamespaceOperation​(
Operation
baseOperation,

Namespace
... namespaces)
```

Constructs a new namespace operation.

**Parameters:** baseOperation

- the base operation that operates on one or more namespaces.
**Parameters:** namespaces

- one or more namespaces this operation operates on.
**Throws:** IllegalArgumentException

- if less than one namespace is
specified, or the base operation is itself a

NamespaceOperation

or a

NamedOperation

.
**Throws:** NullPointerException

- if either the

namespaces

array or any of its
elements are

null

, or if

baseOperation

is

null

.

---

#### NamespaceOperation

public NamespaceOperation​(

Operation

baseOperation,

Namespace

... namespaces)

Constructs a new namespace operation.

Method Detail

- getBaseOperation

```java
public
Operation
getBaseOperation()
```

Returns the base operation of this named operation.

**Returns:** the base operation of this named operation.

- getNamespaces

```java
public
Namespace
[] getNamespaces()
```

Returns the namespaces in this namespace operation. The returned
array is a copy and changes to it don't have effect on this
object.

**Returns:** the namespaces in this namespace operation.

- getNamespaceCount

```java
public int getNamespaceCount()
```

Returns the number of namespaces in this namespace operation.

**Returns:** the number of namespaces in this namespace operation.

- getNamespace

```java
public
Namespace
getNamespace​(int i)
```

Returns the i-th namespace in this namespace operation.

**Parameters:** i

- the namespace index
**Returns:** the i-th namespace in this namespace operation.
**Throws:** IndexOutOfBoundsException

- if the index is out of range.

- contains

```java
public boolean contains​(
Namespace
namespace)
```

Returns true if this namespace operation contains a namespace equal to
the specified namespace.

**Parameters:** namespace

- the namespace being searched for. Must not be null.
**Returns:** true if the if this namespace operation contains a namespace
equal to the specified namespace.

- equals

```java
public boolean equals​(
Object
obj)
```

Returns true if the other object is also a namespace operation and their
base operation and namespaces are equal.

**Overrides:** equals

in class

Object
**Parameters:** obj

- the object to compare to
**Returns:** true if this object is equal to the other one, false otherwise.
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
public int hashCode()
```

Returns the hash code of this namespace operation. Defined to be equal
to

baseOperation.hashCode() + 31 * Arrays.hashCode(namespaces)

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

Returns the string representation of this namespace operation. Defined to
be the

toString

of its base operation, followed by a colon character,
followed with the list of its namespaces separated with the vertical line
character (e.g.

"GET:PROPERTY|ELEMENT"

).

**Overrides:** toString

in class

Object
**Returns:** the string representation of this namespace operation.

- getBaseOperation

```java
public static
Operation
getBaseOperation​(
Operation
op)
```

If the passed operation is a namespace operation, returns its

getBaseOperation()

, otherwise returns the operation as is.

**Parameters:** op

- the operation
**Returns:** the base operation of the passed operation.

- getNamespaces

```java
public static
Namespace
[] getNamespaces​(
Operation
op)
```

If the passed operation is a namespace operation, returns its

getNamespaces()

, otherwise returns an empty array.

**Parameters:** op

- the operation
**Returns:** the namespaces of the passed operation.

- contains

```java
public static boolean contains​(
Operation
op,

Operation
baseOperation,

Namespace
namespace)
```

Returns true if the specified operation is a

NamespaceOperation

and its base operation is equal to the specified operation, and it
contains the specified namespace. If it is not a

NamespaceOperation

,
then it returns false.

**Parameters:** op

- the operation. Must not be null.
**Parameters:** baseOperation

- the base operation being searched for. Must not be null.
**Parameters:** namespace

- the namespace being searched for. Must not be null.
**Returns:** true if the if the passed operation is a

NamespaceOperation

,
its base operation equals the searched base operation, and contains a namespace
equal to the searched namespace.

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

getNamespaces

```java
public
Namespace
[] getNamespaces()
```

Returns the namespaces in this namespace operation. The returned
array is a copy and changes to it don't have effect on this
object.

**Returns:** the namespaces in this namespace operation.

---

#### getNamespaces

public

Namespace

[] getNamespaces()

Returns the namespaces in this namespace operation. The returned
array is a copy and changes to it don't have effect on this
object.

getNamespaceCount

```java
public int getNamespaceCount()
```

Returns the number of namespaces in this namespace operation.

**Returns:** the number of namespaces in this namespace operation.

---

#### getNamespaceCount

public int getNamespaceCount()

Returns the number of namespaces in this namespace operation.

getNamespace

```java
public
Namespace
getNamespace​(int i)
```

Returns the i-th namespace in this namespace operation.

**Parameters:** i

- the namespace index
**Returns:** the i-th namespace in this namespace operation.
**Throws:** IndexOutOfBoundsException

- if the index is out of range.

---

#### getNamespace

public

Namespace

getNamespace​(int i)

Returns the i-th namespace in this namespace operation.

contains

```java
public boolean contains​(
Namespace
namespace)
```

Returns true if this namespace operation contains a namespace equal to
the specified namespace.

**Parameters:** namespace

- the namespace being searched for. Must not be null.
**Returns:** true if the if this namespace operation contains a namespace
equal to the specified namespace.

---

#### contains

public boolean contains​(

Namespace

namespace)

Returns true if this namespace operation contains a namespace equal to
the specified namespace.

equals

```java
public boolean equals​(
Object
obj)
```

Returns true if the other object is also a namespace operation and their
base operation and namespaces are equal.

**Overrides:** equals

in class

Object
**Parameters:** obj

- the object to compare to
**Returns:** true if this object is equal to the other one, false otherwise.
**See Also:** Object.hashCode()

,

HashMap

---

#### equals

public boolean equals​(

Object

obj)

Returns true if the other object is also a namespace operation and their
base operation and namespaces are equal.

hashCode

```java
public int hashCode()
```

Returns the hash code of this namespace operation. Defined to be equal
to

baseOperation.hashCode() + 31 * Arrays.hashCode(namespaces)

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

Returns the hash code of this namespace operation. Defined to be equal
to

baseOperation.hashCode() + 31 * Arrays.hashCode(namespaces)

.

toString

```java
public
String
toString()
```

Returns the string representation of this namespace operation. Defined to
be the

toString

of its base operation, followed by a colon character,
followed with the list of its namespaces separated with the vertical line
character (e.g.

"GET:PROPERTY|ELEMENT"

).

**Overrides:** toString

in class

Object
**Returns:** the string representation of this namespace operation.

---

#### toString

public

String

toString()

Returns the string representation of this namespace operation. Defined to
be the

toString

of its base operation, followed by a colon character,
followed with the list of its namespaces separated with the vertical line
character (e.g.

"GET:PROPERTY|ELEMENT"

).

getBaseOperation

```java
public static
Operation
getBaseOperation​(
Operation
op)
```

If the passed operation is a namespace operation, returns its

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

If the passed operation is a namespace operation, returns its

getBaseOperation()

, otherwise returns the operation as is.

getNamespaces

```java
public static
Namespace
[] getNamespaces​(
Operation
op)
```

If the passed operation is a namespace operation, returns its

getNamespaces()

, otherwise returns an empty array.

**Parameters:** op

- the operation
**Returns:** the namespaces of the passed operation.

---

#### getNamespaces

public static

Namespace

[] getNamespaces​(

Operation

op)

If the passed operation is a namespace operation, returns its

getNamespaces()

, otherwise returns an empty array.

contains

```java
public static boolean contains​(
Operation
op,

Operation
baseOperation,

Namespace
namespace)
```

Returns true if the specified operation is a

NamespaceOperation

and its base operation is equal to the specified operation, and it
contains the specified namespace. If it is not a

NamespaceOperation

,
then it returns false.

**Parameters:** op

- the operation. Must not be null.
**Parameters:** baseOperation

- the base operation being searched for. Must not be null.
**Parameters:** namespace

- the namespace being searched for. Must not be null.
**Returns:** true if the if the passed operation is a

NamespaceOperation

,
its base operation equals the searched base operation, and contains a namespace
equal to the searched namespace.

---

#### contains

public static boolean contains​(

Operation

op,

Operation

baseOperation,

Namespace

namespace)

Returns true if the specified operation is a

NamespaceOperation

and its base operation is equal to the specified operation, and it
contains the specified namespace. If it is not a

NamespaceOperation

,
then it returns false.

---

