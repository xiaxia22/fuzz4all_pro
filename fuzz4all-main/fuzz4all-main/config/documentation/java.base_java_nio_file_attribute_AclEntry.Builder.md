# Class AclEntry.Builder

**Source:** `java.base\java\nio\file\attribute\AclEntry.Builder.html`

### Class Description

```java
public static final class
AclEntry.Builder

extends
Object
```

A builder of

AclEntry

objects.

A

Builder

object is obtained by invoking one of the

newBuilder

methods defined by the

AclEntry

class.

Builder objects are mutable and are not safe for use by multiple
concurrent threads without appropriate synchronization.

**Enclosing class:** AclEntry

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### public
AclEntry
build()

Constructs an

AclEntry

from the components of this builder.
The type and who components are required to have been set in order
to construct an

AclEntry

.

**Returns:**
- a new ACL entry

**Throws:**
- IllegalStateException

- if the type or who component have not been set

---

#### public
AclEntry.Builder
setType​(
AclEntryType
type)

Sets the type component of this builder.

**Parameters:**
- type

- the component type

**Returns:**
- this builder

---

#### public
AclEntry.Builder
setPrincipal​(
UserPrincipal
who)

Sets the principal component of this builder.

**Parameters:**
- who

- the principal component

**Returns:**
- this builder

---

#### public
AclEntry.Builder
setPermissions​(
Set
<
AclEntryPermission
> perms)

Sets the permissions component of this builder. On return, the
permissions component of this builder is a copy of the given set.

**Parameters:**
- perms

- the permissions component

**Returns:**
- this builder

**Throws:**
- ClassCastException

- if the set contains elements that are not of type

AclEntryPermission

---

#### public
AclEntry.Builder
setPermissions​(
AclEntryPermission
... perms)

Sets the permissions component of this builder. On return, the
permissions component of this builder is a copy of the permissions in
the given array.

**Parameters:**
- perms

- the permissions component

**Returns:**
- this builder

---

#### public
AclEntry.Builder
setFlags​(
Set
<
AclEntryFlag
> flags)

Sets the flags component of this builder. On return, the flags
component of this builder is a copy of the given set.

**Parameters:**
- flags

- the flags component

**Returns:**
- this builder

**Throws:**
- ClassCastException

- if the set contains elements that are not of type

AclEntryFlag

---

#### public
AclEntry.Builder
setFlags​(
AclEntryFlag
... flags)

Sets the flags component of this builder. On return, the flags
component of this builder is a copy of the flags in the given
array.

**Parameters:**
- flags

- the flags component

**Returns:**
- this builder

---

### Additional Sections

#### Class AclEntry.Builder

java.lang.Object

- java.nio.file.attribute.AclEntry.Builder

java.nio.file.attribute.AclEntry.Builder

**Enclosing class:** AclEntry

```java
public static final class
AclEntry.Builder

extends
Object
```

A builder of

AclEntry

objects.

A

Builder

object is obtained by invoking one of the

newBuilder

methods defined by the

AclEntry

class.

Builder objects are mutable and are not safe for use by multiple
concurrent threads without appropriate synchronization.

**Since:** 1.7

public static final class

AclEntry.Builder

extends

Object

A builder of

AclEntry

objects.

A

Builder

object is obtained by invoking one of the

newBuilder

methods defined by the

AclEntry

class.

Builder objects are mutable and are not safe for use by multiple
concurrent threads without appropriate synchronization.

A

Builder

object is obtained by invoking one of the

newBuilder

methods defined by the

AclEntry

class.

Builder objects are mutable and are not safe for use by multiple
concurrent threads without appropriate synchronization.

Builder objects are mutable and are not safe for use by multiple
concurrent threads without appropriate synchronization.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

AclEntry

build

()

Constructs an

AclEntry

from the components of this builder.

AclEntry.Builder

setFlags

​(

AclEntryFlag

... flags)

Sets the flags component of this builder.

AclEntry.Builder

setFlags

​(

Set

<

AclEntryFlag

> flags)

Sets the flags component of this builder.

AclEntry.Builder

setPermissions

​(

AclEntryPermission

... perms)

Sets the permissions component of this builder.

AclEntry.Builder

setPermissions

​(

Set

<

AclEntryPermission

> perms)

Sets the permissions component of this builder.

AclEntry.Builder

setPrincipal

​(

UserPrincipal

who)

Sets the principal component of this builder.

AclEntry.Builder

setType

​(

AclEntryType

type)

Sets the type component of this builder.

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

toString

,

wait

,

wait

,

wait

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

AclEntry

build

()

Constructs an

AclEntry

from the components of this builder.

AclEntry.Builder

setFlags

​(

AclEntryFlag

... flags)

Sets the flags component of this builder.

AclEntry.Builder

setFlags

​(

Set

<

AclEntryFlag

> flags)

Sets the flags component of this builder.

AclEntry.Builder

setPermissions

​(

AclEntryPermission

... perms)

Sets the permissions component of this builder.

AclEntry.Builder

setPermissions

​(

Set

<

AclEntryPermission

> perms)

Sets the permissions component of this builder.

AclEntry.Builder

setPrincipal

​(

UserPrincipal

who)

Sets the principal component of this builder.

AclEntry.Builder

setType

​(

AclEntryType

type)

Sets the type component of this builder.

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

toString

,

wait

,

wait

,

wait

---

#### Method Summary

Constructs an

AclEntry

from the components of this builder.

Sets the flags component of this builder.

Sets the permissions component of this builder.

Sets the principal component of this builder.

Sets the type component of this builder.

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

toString

,

wait

,

wait

,

wait

---

#### Methods declared in class java.lang. Object

============ METHOD DETAIL ==========

- Method Detail

- build

```java
public
AclEntry
build()
```

Constructs an

AclEntry

from the components of this builder.
The type and who components are required to have been set in order
to construct an

AclEntry

.

**Returns:** a new ACL entry
**Throws:** IllegalStateException

- if the type or who component have not been set

- setType

```java
public
AclEntry.Builder
setType​(
AclEntryType
type)
```

Sets the type component of this builder.

**Parameters:** type

- the component type
**Returns:** this builder

- setPrincipal

```java
public
AclEntry.Builder
setPrincipal​(
UserPrincipal
who)
```

Sets the principal component of this builder.

**Parameters:** who

- the principal component
**Returns:** this builder

- setPermissions

```java
public
AclEntry.Builder
setPermissions​(
Set
<
AclEntryPermission
> perms)
```

Sets the permissions component of this builder. On return, the
permissions component of this builder is a copy of the given set.

**Parameters:** perms

- the permissions component
**Returns:** this builder
**Throws:** ClassCastException

- if the set contains elements that are not of type

AclEntryPermission

- setPermissions

```java
public
AclEntry.Builder
setPermissions​(
AclEntryPermission
... perms)
```

Sets the permissions component of this builder. On return, the
permissions component of this builder is a copy of the permissions in
the given array.

**Parameters:** perms

- the permissions component
**Returns:** this builder

- setFlags

```java
public
AclEntry.Builder
setFlags​(
Set
<
AclEntryFlag
> flags)
```

Sets the flags component of this builder. On return, the flags
component of this builder is a copy of the given set.

**Parameters:** flags

- the flags component
**Returns:** this builder
**Throws:** ClassCastException

- if the set contains elements that are not of type

AclEntryFlag

- setFlags

```java
public
AclEntry.Builder
setFlags​(
AclEntryFlag
... flags)
```

Sets the flags component of this builder. On return, the flags
component of this builder is a copy of the flags in the given
array.

**Parameters:** flags

- the flags component
**Returns:** this builder

Method Detail

- build

```java
public
AclEntry
build()
```

Constructs an

AclEntry

from the components of this builder.
The type and who components are required to have been set in order
to construct an

AclEntry

.

**Returns:** a new ACL entry
**Throws:** IllegalStateException

- if the type or who component have not been set

- setType

```java
public
AclEntry.Builder
setType​(
AclEntryType
type)
```

Sets the type component of this builder.

**Parameters:** type

- the component type
**Returns:** this builder

- setPrincipal

```java
public
AclEntry.Builder
setPrincipal​(
UserPrincipal
who)
```

Sets the principal component of this builder.

**Parameters:** who

- the principal component
**Returns:** this builder

- setPermissions

```java
public
AclEntry.Builder
setPermissions​(
Set
<
AclEntryPermission
> perms)
```

Sets the permissions component of this builder. On return, the
permissions component of this builder is a copy of the given set.

**Parameters:** perms

- the permissions component
**Returns:** this builder
**Throws:** ClassCastException

- if the set contains elements that are not of type

AclEntryPermission

- setPermissions

```java
public
AclEntry.Builder
setPermissions​(
AclEntryPermission
... perms)
```

Sets the permissions component of this builder. On return, the
permissions component of this builder is a copy of the permissions in
the given array.

**Parameters:** perms

- the permissions component
**Returns:** this builder

- setFlags

```java
public
AclEntry.Builder
setFlags​(
Set
<
AclEntryFlag
> flags)
```

Sets the flags component of this builder. On return, the flags
component of this builder is a copy of the given set.

**Parameters:** flags

- the flags component
**Returns:** this builder
**Throws:** ClassCastException

- if the set contains elements that are not of type

AclEntryFlag

- setFlags

```java
public
AclEntry.Builder
setFlags​(
AclEntryFlag
... flags)
```

Sets the flags component of this builder. On return, the flags
component of this builder is a copy of the flags in the given
array.

**Parameters:** flags

- the flags component
**Returns:** this builder

---

#### Method Detail

build

```java
public
AclEntry
build()
```

Constructs an

AclEntry

from the components of this builder.
The type and who components are required to have been set in order
to construct an

AclEntry

.

**Returns:** a new ACL entry
**Throws:** IllegalStateException

- if the type or who component have not been set

---

#### build

public

AclEntry

build()

Constructs an

AclEntry

from the components of this builder.
The type and who components are required to have been set in order
to construct an

AclEntry

.

setType

```java
public
AclEntry.Builder
setType​(
AclEntryType
type)
```

Sets the type component of this builder.

**Parameters:** type

- the component type
**Returns:** this builder

---

#### setType

public

AclEntry.Builder

setType​(

AclEntryType

type)

Sets the type component of this builder.

setPrincipal

```java
public
AclEntry.Builder
setPrincipal​(
UserPrincipal
who)
```

Sets the principal component of this builder.

**Parameters:** who

- the principal component
**Returns:** this builder

---

#### setPrincipal

public

AclEntry.Builder

setPrincipal​(

UserPrincipal

who)

Sets the principal component of this builder.

setPermissions

```java
public
AclEntry.Builder
setPermissions​(
Set
<
AclEntryPermission
> perms)
```

Sets the permissions component of this builder. On return, the
permissions component of this builder is a copy of the given set.

**Parameters:** perms

- the permissions component
**Returns:** this builder
**Throws:** ClassCastException

- if the set contains elements that are not of type

AclEntryPermission

---

#### setPermissions

public

AclEntry.Builder

setPermissions​(

Set

<

AclEntryPermission

> perms)

Sets the permissions component of this builder. On return, the
permissions component of this builder is a copy of the given set.

setPermissions

```java
public
AclEntry.Builder
setPermissions​(
AclEntryPermission
... perms)
```

Sets the permissions component of this builder. On return, the
permissions component of this builder is a copy of the permissions in
the given array.

**Parameters:** perms

- the permissions component
**Returns:** this builder

---

#### setPermissions

public

AclEntry.Builder

setPermissions​(

AclEntryPermission

... perms)

Sets the permissions component of this builder. On return, the
permissions component of this builder is a copy of the permissions in
the given array.

setFlags

```java
public
AclEntry.Builder
setFlags​(
Set
<
AclEntryFlag
> flags)
```

Sets the flags component of this builder. On return, the flags
component of this builder is a copy of the given set.

**Parameters:** flags

- the flags component
**Returns:** this builder
**Throws:** ClassCastException

- if the set contains elements that are not of type

AclEntryFlag

---

#### setFlags

public

AclEntry.Builder

setFlags​(

Set

<

AclEntryFlag

> flags)

Sets the flags component of this builder. On return, the flags
component of this builder is a copy of the given set.

setFlags

```java
public
AclEntry.Builder
setFlags​(
AclEntryFlag
... flags)
```

Sets the flags component of this builder. On return, the flags
component of this builder is a copy of the flags in the given
array.

**Parameters:** flags

- the flags component
**Returns:** this builder

---

#### setFlags

public

AclEntry.Builder

setFlags​(

AclEntryFlag

... flags)

Sets the flags component of this builder. On return, the flags
component of this builder is a copy of the flags in the given
array.

---

