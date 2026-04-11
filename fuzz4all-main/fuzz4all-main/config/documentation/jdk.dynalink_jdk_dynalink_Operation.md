# Interface Operation

**Source:** `jdk.dynalink\jdk\dynalink\Operation.html`

### Class Description

```java
public interface
Operation
```

An object that describes a dynamic operation. Dynalink defines a set of
standard operations with the

StandardOperation

class, as well as a
way to express the target

namespace(s)

of an operation
on an object using

NamespaceOperation

and finally a way to attach
a fixed target name to an operation using

NamedOperation

.
When presenting examples in this documentation, we will refer to standard
operations using their name (e.g.

GET

), to namespace operations
by separating their base operation with a colon from their namespace
(e.g.

GET:PROPERTY

), or in case of multiple namespaces we will
further separate those with the vertical line character (e.g.

GET:PROPERTY|ELEMENT

), and finally we will refer to named operations
by separating the base operation and the name with the colon character (e.g.

GET:PROPERTY|ELEMENT:color

).

**All Known Implementing Classes:** NamedOperation

,

NamespaceOperation

,

StandardOperation

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### default
NamespaceOperation
withNamespace​(
Namespace
namespace)

Returns a

NamespaceOperation

using this operation as its base.

**Parameters:**
- namespace

- the namespace that is the target of the namespace operation.

**Returns:**
- a

NamespaceOperation

with this operation as its base and the specified
namespace as its target.

**Throws:**
- IllegalArgumentException

- if this operation is already a namespace operation or a named operation.
- NullPointerException

- if

namespace

is null.

---

#### default
NamespaceOperation
withNamespaces​(
Namespace
... namespaces)

Returns a

NamespaceOperation

using this operation as its base.

**Parameters:**
- namespaces

- the namespaces that are the target of the namespace operation.

**Returns:**
- a

NamespaceOperation

with this operation as its base and the specified
namespaces as its targets.

**Throws:**
- IllegalArgumentException

- if this operation is already a namespace operation or a named operation.
- NullPointerException

- if

namespace

or any of its elements is null.

---

#### default
NamedOperation
named​(
Object
name)

Returns a

NamedOperation

using this operation as its base.

**Parameters:**
- name

- the name that is the target of the named operation.

**Returns:**
- a

NamedOperation

with this operation as its base and the specified name.

**Throws:**
- IllegalArgumentException

- if this operation is already a named operation.
- NullPointerException

- if

name

is null.

---

### Additional Sections

#### Interface Operation

**All Known Implementing Classes:** NamedOperation

,

NamespaceOperation

,

StandardOperation

```java
public interface
Operation
```

An object that describes a dynamic operation. Dynalink defines a set of
standard operations with the

StandardOperation

class, as well as a
way to express the target

namespace(s)

of an operation
on an object using

NamespaceOperation

and finally a way to attach
a fixed target name to an operation using

NamedOperation

.
When presenting examples in this documentation, we will refer to standard
operations using their name (e.g.

GET

), to namespace operations
by separating their base operation with a colon from their namespace
(e.g.

GET:PROPERTY

), or in case of multiple namespaces we will
further separate those with the vertical line character (e.g.

GET:PROPERTY|ELEMENT

), and finally we will refer to named operations
by separating the base operation and the name with the colon character (e.g.

GET:PROPERTY|ELEMENT:color

).

public interface

Operation

An object that describes a dynamic operation. Dynalink defines a set of
standard operations with the

StandardOperation

class, as well as a
way to express the target

namespace(s)

of an operation
on an object using

NamespaceOperation

and finally a way to attach
a fixed target name to an operation using

NamedOperation

.
When presenting examples in this documentation, we will refer to standard
operations using their name (e.g.

GET

), to namespace operations
by separating their base operation with a colon from their namespace
(e.g.

GET:PROPERTY

), or in case of multiple namespaces we will
further separate those with the vertical line character (e.g.

GET:PROPERTY|ELEMENT

), and finally we will refer to named operations
by separating the base operation and the name with the colon character (e.g.

GET:PROPERTY|ELEMENT:color

).

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Default Methods

Modifier and Type

Method

Description

default

NamedOperation

named

​(

Object

name)

Returns a

NamedOperation

using this operation as its base.

default

NamespaceOperation

withNamespace

​(

Namespace

namespace)

Returns a

NamespaceOperation

using this operation as its base.

default

NamespaceOperation

withNamespaces

​(

Namespace

... namespaces)

Returns a

NamespaceOperation

using this operation as its base.

Method Summary

All Methods

Instance Methods

Default Methods

Modifier and Type

Method

Description

default

NamedOperation

named

​(

Object

name)

Returns a

NamedOperation

using this operation as its base.

default

NamespaceOperation

withNamespace

​(

Namespace

namespace)

Returns a

NamespaceOperation

using this operation as its base.

default

NamespaceOperation

withNamespaces

​(

Namespace

... namespaces)

Returns a

NamespaceOperation

using this operation as its base.

---

#### Method Summary

Returns a

NamedOperation

using this operation as its base.

Returns a

NamespaceOperation

using this operation as its base.

============ METHOD DETAIL ==========

- Method Detail

- withNamespace

```java
default
NamespaceOperation
withNamespace​(
Namespace
namespace)
```

Returns a

NamespaceOperation

using this operation as its base.

**Parameters:** namespace

- the namespace that is the target of the namespace operation.
**Returns:** a

NamespaceOperation

with this operation as its base and the specified
namespace as its target.
**Throws:** IllegalArgumentException

- if this operation is already a namespace operation or a named operation.
**Throws:** NullPointerException

- if

namespace

is null.

- withNamespaces

```java
default
NamespaceOperation
withNamespaces​(
Namespace
... namespaces)
```

Returns a

NamespaceOperation

using this operation as its base.

**Parameters:** namespaces

- the namespaces that are the target of the namespace operation.
**Returns:** a

NamespaceOperation

with this operation as its base and the specified
namespaces as its targets.
**Throws:** IllegalArgumentException

- if this operation is already a namespace operation or a named operation.
**Throws:** NullPointerException

- if

namespace

or any of its elements is null.

- named

```java
default
NamedOperation
named​(
Object
name)
```

Returns a

NamedOperation

using this operation as its base.

**Parameters:** name

- the name that is the target of the named operation.
**Returns:** a

NamedOperation

with this operation as its base and the specified name.
**Throws:** IllegalArgumentException

- if this operation is already a named operation.
**Throws:** NullPointerException

- if

name

is null.

Method Detail

- withNamespace

```java
default
NamespaceOperation
withNamespace​(
Namespace
namespace)
```

Returns a

NamespaceOperation

using this operation as its base.

**Parameters:** namespace

- the namespace that is the target of the namespace operation.
**Returns:** a

NamespaceOperation

with this operation as its base and the specified
namespace as its target.
**Throws:** IllegalArgumentException

- if this operation is already a namespace operation or a named operation.
**Throws:** NullPointerException

- if

namespace

is null.

- withNamespaces

```java
default
NamespaceOperation
withNamespaces​(
Namespace
... namespaces)
```

Returns a

NamespaceOperation

using this operation as its base.

**Parameters:** namespaces

- the namespaces that are the target of the namespace operation.
**Returns:** a

NamespaceOperation

with this operation as its base and the specified
namespaces as its targets.
**Throws:** IllegalArgumentException

- if this operation is already a namespace operation or a named operation.
**Throws:** NullPointerException

- if

namespace

or any of its elements is null.

- named

```java
default
NamedOperation
named​(
Object
name)
```

Returns a

NamedOperation

using this operation as its base.

**Parameters:** name

- the name that is the target of the named operation.
**Returns:** a

NamedOperation

with this operation as its base and the specified name.
**Throws:** IllegalArgumentException

- if this operation is already a named operation.
**Throws:** NullPointerException

- if

name

is null.

---

#### Method Detail

withNamespace

```java
default
NamespaceOperation
withNamespace​(
Namespace
namespace)
```

Returns a

NamespaceOperation

using this operation as its base.

**Parameters:** namespace

- the namespace that is the target of the namespace operation.
**Returns:** a

NamespaceOperation

with this operation as its base and the specified
namespace as its target.
**Throws:** IllegalArgumentException

- if this operation is already a namespace operation or a named operation.
**Throws:** NullPointerException

- if

namespace

is null.

---

#### withNamespace

default

NamespaceOperation

withNamespace​(

Namespace

namespace)

Returns a

NamespaceOperation

using this operation as its base.

withNamespaces

```java
default
NamespaceOperation
withNamespaces​(
Namespace
... namespaces)
```

Returns a

NamespaceOperation

using this operation as its base.

**Parameters:** namespaces

- the namespaces that are the target of the namespace operation.
**Returns:** a

NamespaceOperation

with this operation as its base and the specified
namespaces as its targets.
**Throws:** IllegalArgumentException

- if this operation is already a namespace operation or a named operation.
**Throws:** NullPointerException

- if

namespace

or any of its elements is null.

---

#### withNamespaces

default

NamespaceOperation

withNamespaces​(

Namespace

... namespaces)

Returns a

NamespaceOperation

using this operation as its base.

named

```java
default
NamedOperation
named​(
Object
name)
```

Returns a

NamedOperation

using this operation as its base.

**Parameters:** name

- the name that is the target of the named operation.
**Returns:** a

NamedOperation

with this operation as its base and the specified name.
**Throws:** IllegalArgumentException

- if this operation is already a named operation.
**Throws:** NullPointerException

- if

name

is null.

---

#### named

default

NamedOperation

named​(

Object

name)

Returns a

NamedOperation

using this operation as its base.

---

