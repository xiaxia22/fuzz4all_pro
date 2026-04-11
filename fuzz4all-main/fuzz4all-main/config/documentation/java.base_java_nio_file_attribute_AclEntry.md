# Class AclEntry

**Source:** `java.base\java\nio\file\attribute\AclEntry.html`

### Class Description

```java
public final class
AclEntry

extends
Object
```

An entry in an access control list (ACL).

The ACL entry represented by this class is based on the ACL model
specified in

RFC 3530:
Network File System (NFS) version 4 Protocol

. Each entry has four
components as follows:

- The

type

component determines if the entry
grants or denies access.
- The

principal

component, sometimes called the
"who" component, is a

UserPrincipal

corresponding to the identity
that the entry grants or denies access
- The

permissions

component is a set of

permissions
- The

flags

component is a set of

flags

to indicate how entries are inherited and propagated

ACL entries are created using an associated

AclEntry.Builder

object by
invoking its

build

method.

ACL entries are immutable and are safe for use by multiple concurrent
threads.

**Since:** 1.7

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### public static
AclEntry.Builder
newBuilder()

Constructs a new builder. The initial value of the type and who
components is

null

. The initial value of the permissions and
flags components is the empty set.

**Returns:**
- a new builder

---

#### public static
AclEntry.Builder
newBuilder​(
AclEntry
entry)

Constructs a new builder with the components of an existing ACL entry.

**Parameters:**
- entry

- an ACL entry

**Returns:**
- a new builder

---

#### public
AclEntryType
type()

Returns the ACL entry type.

**Returns:**
- the ACL entry type

---

#### public
UserPrincipal
principal()

Returns the principal component.

**Returns:**
- the principal component

---

#### public
Set
<
AclEntryPermission
> permissions()

Returns a copy of the permissions component.

The returned set is a modifiable copy of the permissions.

**Returns:**
- the permissions component

---

#### public
Set
<
AclEntryFlag
> flags()

Returns a copy of the flags component.

The returned set is a modifiable copy of the flags.

**Returns:**
- the flags component

---

#### public boolean equals​(
Object
ob)

Compares the specified object with this ACL entry for equality.

If the given object is not an

AclEntry

then this method
immediately returns

false

.

For two ACL entries to be considered equals requires that they are
both the same type, their who components are equal, their permissions
components are equal, and their flags components are equal.

This method satisfies the general contract of the

Object.equals

method.

**Overrides:**
- equals

in class

Object

**Parameters:**
- ob

- the object to which this object is to be compared

**Returns:**
- true

if, and only if, the given object is an AclEntry that
is identical to this AclEntry

**See Also:**
- Object.hashCode()

,

HashMap

---

#### public int hashCode()

Returns the hash-code value for this ACL entry.

This method satisfies the general contract of the

Object.hashCode()

method.

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

Returns the string representation of this ACL entry.

**Overrides:**
- toString

in class

Object

**Returns:**
- the string representation of this entry

---

### Additional Sections

#### Class AclEntry

java.lang.Object

- java.nio.file.attribute.AclEntry

java.nio.file.attribute.AclEntry

```java
public final class
AclEntry

extends
Object
```

An entry in an access control list (ACL).

The ACL entry represented by this class is based on the ACL model
specified in

RFC 3530:
Network File System (NFS) version 4 Protocol

. Each entry has four
components as follows:

- The

type

component determines if the entry
grants or denies access.
- The

principal

component, sometimes called the
"who" component, is a

UserPrincipal

corresponding to the identity
that the entry grants or denies access
- The

permissions

component is a set of

permissions
- The

flags

component is a set of

flags

to indicate how entries are inherited and propagated

ACL entries are created using an associated

AclEntry.Builder

object by
invoking its

build

method.

ACL entries are immutable and are safe for use by multiple concurrent
threads.

**Since:** 1.7

public final class

AclEntry

extends

Object

An entry in an access control list (ACL).

The ACL entry represented by this class is based on the ACL model
specified in

RFC 3530:
Network File System (NFS) version 4 Protocol

. Each entry has four
components as follows:

- The

type

component determines if the entry
grants or denies access.
- The

principal

component, sometimes called the
"who" component, is a

UserPrincipal

corresponding to the identity
that the entry grants or denies access
- The

permissions

component is a set of

permissions
- The

flags

component is a set of

flags

to indicate how entries are inherited and propagated

ACL entries are created using an associated

AclEntry.Builder

object by
invoking its

build

method.

ACL entries are immutable and are safe for use by multiple concurrent
threads.

The ACL entry represented by this class is based on the ACL model
specified in

RFC 3530:
Network File System (NFS) version 4 Protocol

. Each entry has four
components as follows:

- The

type

component determines if the entry
grants or denies access.
- The

principal

component, sometimes called the
"who" component, is a

UserPrincipal

corresponding to the identity
that the entry grants or denies access
- The

permissions

component is a set of

permissions
- The

flags

component is a set of

flags

to indicate how entries are inherited and propagated

ACL entries are created using an associated

AclEntry.Builder

object by
invoking its

build

method.

ACL entries are immutable and are safe for use by multiple concurrent
threads.

The

type

component determines if the entry
grants or denies access.

The

principal

component, sometimes called the
"who" component, is a

UserPrincipal

corresponding to the identity
that the entry grants or denies access

The

permissions

component is a set of

permissions

The

flags

component is a set of

flags

to indicate how entries are inherited and propagated

The

type

component determines if the entry
grants or denies access.

The

principal

component, sometimes called the
"who" component, is a

UserPrincipal

corresponding to the identity
that the entry grants or denies access

The

permissions

component is a set of

permissions

The

flags

component is a set of

flags

to indicate how entries are inherited and propagated

ACL entries are created using an associated

AclEntry.Builder

object by
invoking its

build

method.

ACL entries are immutable and are safe for use by multiple concurrent
threads.

ACL entries are immutable and are safe for use by multiple concurrent
threads.

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

static class

AclEntry.Builder

A builder of

AclEntry

objects.

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

equals

​(

Object

ob)

Compares the specified object with this ACL entry for equality.

Set

<

AclEntryFlag

>

flags

()

Returns a copy of the flags component.

int

hashCode

()

Returns the hash-code value for this ACL entry.

static

AclEntry.Builder

newBuilder

()

Constructs a new builder.

static

AclEntry.Builder

newBuilder

​(

AclEntry

entry)

Constructs a new builder with the components of an existing ACL entry.

Set

<

AclEntryPermission

>

permissions

()

Returns a copy of the permissions component.

UserPrincipal

principal

()

Returns the principal component.

String

toString

()

Returns the string representation of this ACL entry.

AclEntryType

type

()

Returns the ACL entry type.

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

Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

static class

AclEntry.Builder

A builder of

AclEntry

objects.

---

#### Nested Class Summary

A builder of

AclEntry

objects.

Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

boolean

equals

​(

Object

ob)

Compares the specified object with this ACL entry for equality.

Set

<

AclEntryFlag

>

flags

()

Returns a copy of the flags component.

int

hashCode

()

Returns the hash-code value for this ACL entry.

static

AclEntry.Builder

newBuilder

()

Constructs a new builder.

static

AclEntry.Builder

newBuilder

​(

AclEntry

entry)

Constructs a new builder with the components of an existing ACL entry.

Set

<

AclEntryPermission

>

permissions

()

Returns a copy of the permissions component.

UserPrincipal

principal

()

Returns the principal component.

String

toString

()

Returns the string representation of this ACL entry.

AclEntryType

type

()

Returns the ACL entry type.

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

---

#### Method Summary

Compares the specified object with this ACL entry for equality.

Returns a copy of the flags component.

Returns the hash-code value for this ACL entry.

Constructs a new builder.

Constructs a new builder with the components of an existing ACL entry.

Returns a copy of the permissions component.

Returns the principal component.

Returns the string representation of this ACL entry.

Returns the ACL entry type.

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

============ METHOD DETAIL ==========

- Method Detail

- newBuilder

```java
public static
AclEntry.Builder
newBuilder()
```

Constructs a new builder. The initial value of the type and who
components is

null

. The initial value of the permissions and
flags components is the empty set.

**Returns:** a new builder

- newBuilder

```java
public static
AclEntry.Builder
newBuilder​(
AclEntry
entry)
```

Constructs a new builder with the components of an existing ACL entry.

**Parameters:** entry

- an ACL entry
**Returns:** a new builder

- type

```java
public
AclEntryType
type()
```

Returns the ACL entry type.

**Returns:** the ACL entry type

- principal

```java
public
UserPrincipal
principal()
```

Returns the principal component.

**Returns:** the principal component

- permissions

```java
public
Set
<
AclEntryPermission
> permissions()
```

Returns a copy of the permissions component.

The returned set is a modifiable copy of the permissions.

**Returns:** the permissions component

- flags

```java
public
Set
<
AclEntryFlag
> flags()
```

Returns a copy of the flags component.

The returned set is a modifiable copy of the flags.

**Returns:** the flags component

- equals

```java
public boolean equals​(
Object
ob)
```

Compares the specified object with this ACL entry for equality.

If the given object is not an

AclEntry

then this method
immediately returns

false

.

For two ACL entries to be considered equals requires that they are
both the same type, their who components are equal, their permissions
components are equal, and their flags components are equal.

This method satisfies the general contract of the

Object.equals

method.

**Overrides:** equals

in class

Object
**Parameters:** ob

- the object to which this object is to be compared
**Returns:** true

if, and only if, the given object is an AclEntry that
is identical to this AclEntry
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
public int hashCode()
```

Returns the hash-code value for this ACL entry.

This method satisfies the general contract of the

Object.hashCode()

method.

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

Returns the string representation of this ACL entry.

**Overrides:** toString

in class

Object
**Returns:** the string representation of this entry

Method Detail

- newBuilder

```java
public static
AclEntry.Builder
newBuilder()
```

Constructs a new builder. The initial value of the type and who
components is

null

. The initial value of the permissions and
flags components is the empty set.

**Returns:** a new builder

- newBuilder

```java
public static
AclEntry.Builder
newBuilder​(
AclEntry
entry)
```

Constructs a new builder with the components of an existing ACL entry.

**Parameters:** entry

- an ACL entry
**Returns:** a new builder

- type

```java
public
AclEntryType
type()
```

Returns the ACL entry type.

**Returns:** the ACL entry type

- principal

```java
public
UserPrincipal
principal()
```

Returns the principal component.

**Returns:** the principal component

- permissions

```java
public
Set
<
AclEntryPermission
> permissions()
```

Returns a copy of the permissions component.

The returned set is a modifiable copy of the permissions.

**Returns:** the permissions component

- flags

```java
public
Set
<
AclEntryFlag
> flags()
```

Returns a copy of the flags component.

The returned set is a modifiable copy of the flags.

**Returns:** the flags component

- equals

```java
public boolean equals​(
Object
ob)
```

Compares the specified object with this ACL entry for equality.

If the given object is not an

AclEntry

then this method
immediately returns

false

.

For two ACL entries to be considered equals requires that they are
both the same type, their who components are equal, their permissions
components are equal, and their flags components are equal.

This method satisfies the general contract of the

Object.equals

method.

**Overrides:** equals

in class

Object
**Parameters:** ob

- the object to which this object is to be compared
**Returns:** true

if, and only if, the given object is an AclEntry that
is identical to this AclEntry
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
public int hashCode()
```

Returns the hash-code value for this ACL entry.

This method satisfies the general contract of the

Object.hashCode()

method.

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

Returns the string representation of this ACL entry.

**Overrides:** toString

in class

Object
**Returns:** the string representation of this entry

---

#### Method Detail

newBuilder

```java
public static
AclEntry.Builder
newBuilder()
```

Constructs a new builder. The initial value of the type and who
components is

null

. The initial value of the permissions and
flags components is the empty set.

**Returns:** a new builder

---

#### newBuilder

public static

AclEntry.Builder

newBuilder()

Constructs a new builder. The initial value of the type and who
components is

null

. The initial value of the permissions and
flags components is the empty set.

newBuilder

```java
public static
AclEntry.Builder
newBuilder​(
AclEntry
entry)
```

Constructs a new builder with the components of an existing ACL entry.

**Parameters:** entry

- an ACL entry
**Returns:** a new builder

---

#### newBuilder

public static

AclEntry.Builder

newBuilder​(

AclEntry

entry)

Constructs a new builder with the components of an existing ACL entry.

type

```java
public
AclEntryType
type()
```

Returns the ACL entry type.

**Returns:** the ACL entry type

---

#### type

public

AclEntryType

type()

Returns the ACL entry type.

principal

```java
public
UserPrincipal
principal()
```

Returns the principal component.

**Returns:** the principal component

---

#### principal

public

UserPrincipal

principal()

Returns the principal component.

permissions

```java
public
Set
<
AclEntryPermission
> permissions()
```

Returns a copy of the permissions component.

The returned set is a modifiable copy of the permissions.

**Returns:** the permissions component

---

#### permissions

public

Set

<

AclEntryPermission

> permissions()

Returns a copy of the permissions component.

The returned set is a modifiable copy of the permissions.

The returned set is a modifiable copy of the permissions.

flags

```java
public
Set
<
AclEntryFlag
> flags()
```

Returns a copy of the flags component.

The returned set is a modifiable copy of the flags.

**Returns:** the flags component

---

#### flags

public

Set

<

AclEntryFlag

> flags()

Returns a copy of the flags component.

The returned set is a modifiable copy of the flags.

The returned set is a modifiable copy of the flags.

equals

```java
public boolean equals​(
Object
ob)
```

Compares the specified object with this ACL entry for equality.

If the given object is not an

AclEntry

then this method
immediately returns

false

.

For two ACL entries to be considered equals requires that they are
both the same type, their who components are equal, their permissions
components are equal, and their flags components are equal.

This method satisfies the general contract of the

Object.equals

method.

**Overrides:** equals

in class

Object
**Parameters:** ob

- the object to which this object is to be compared
**Returns:** true

if, and only if, the given object is an AclEntry that
is identical to this AclEntry
**See Also:** Object.hashCode()

,

HashMap

---

#### equals

public boolean equals​(

Object

ob)

Compares the specified object with this ACL entry for equality.

If the given object is not an

AclEntry

then this method
immediately returns

false

.

For two ACL entries to be considered equals requires that they are
both the same type, their who components are equal, their permissions
components are equal, and their flags components are equal.

This method satisfies the general contract of the

Object.equals

method.

If the given object is not an

AclEntry

then this method
immediately returns

false

.

For two ACL entries to be considered equals requires that they are
both the same type, their who components are equal, their permissions
components are equal, and their flags components are equal.

This method satisfies the general contract of the

Object.equals

method.

For two ACL entries to be considered equals requires that they are
both the same type, their who components are equal, their permissions
components are equal, and their flags components are equal.

This method satisfies the general contract of the

Object.equals

method.

This method satisfies the general contract of the

Object.equals

method.

hashCode

```java
public int hashCode()
```

Returns the hash-code value for this ACL entry.

This method satisfies the general contract of the

Object.hashCode()

method.

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

Returns the hash-code value for this ACL entry.

This method satisfies the general contract of the

Object.hashCode()

method.

This method satisfies the general contract of the

Object.hashCode()

method.

toString

```java
public
String
toString()
```

Returns the string representation of this ACL entry.

**Overrides:** toString

in class

Object
**Returns:** the string representation of this entry

---

#### toString

public

String

toString()

Returns the string representation of this ACL entry.

---

