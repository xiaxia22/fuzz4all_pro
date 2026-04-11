# Class ModuleDescriptor.Opens

**Source:** `java.base\java\lang\module\ModuleDescriptor.Opens.html`

### Class Description

```java
public static final class
ModuleDescriptor.Opens

extends
Object

implements
Comparable
<
ModuleDescriptor.Opens
>
```

A package opened by a module, may be qualified or unqualified.

The

opens

directive in a module declaration declares a
package to be open to allow all types in the package, and all their
members, not just public types and their public members to be reflected
on by APIs that support private access or a way to bypass or suppress
default Java language access control checks.

**All Implemented Interfaces:** Comparable

<

ModuleDescriptor.Opens

>

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### public
Set
<
ModuleDescriptor.Opens.Modifier
> modifiers()

Returns the set of modifiers.

**Returns:**
- A possibly-empty unmodifiable set of modifiers

---

#### public boolean isQualified()

Returns

true

if this is a qualified opens.

**Returns:**
- true

if this is a qualified opens

---

#### public
String
source()

Returns the package name.

**Returns:**
- The package name

---

#### public
Set
<
String
> targets()

For a qualified opens, returns the non-empty and immutable set
of the module names to which the package is open. For an
unqualified opens, returns an empty set.

**Returns:**
- The set of target module names or for an unqualified
opens, an empty set

---

#### public int compareTo​(
ModuleDescriptor.Opens
that)

Compares this module opens to another.

Two

Opens

objects are compared by comparing the package
names lexicographically. Where the packages names are equal then the
sets of modifiers are compared in the same way that module modifiers
are compared (see

ModuleDescriptor.compareTo

). Where the package names are equal and
the set of modifiers are equal then the set of target modules are
compared. This is done by sorting the names of the target modules
in ascending order, and according to their natural ordering, and then
comparing the corresponding elements lexicographically. Where the
sets differ in size, and the larger set contains all elements of the
smaller set, then the larger set is considered to succeed the smaller
set.

**Specified by:**
- compareTo

in interface

Comparable

<

ModuleDescriptor.Opens

>

**Parameters:**
- that

- The module opens to compare

**Returns:**
- A negative integer, zero, or a positive integer if this module
opens is less than, equal to, or greater than the given
module opens

---

#### public int hashCode()

Computes a hash code for this module opens.

The hash code is based upon the modifiers, the package name,
and for a qualified opens, the set of modules names to which the
package is opened. It satisfies the general contract of the

Object.hashCode

method.

**Overrides:**
- hashCode

in class

Object

**Returns:**
- The hash-code value for this module opens

**See Also:**
- Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### public boolean equals​(
Object
ob)

Tests this module opens for equality with the given object.

If the given object is not an

Opens

then this method
returns

false

. Two

Opens

objects are equal if their
set of modifiers is equal, the package names are equal and the set
of target module names is equal.

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

if, and only if, the given object is a module
dependence that is equal to this module dependence

**See Also:**
- Object.hashCode()

,

HashMap

---

#### public
String
toString()

Returns a string describing the open package.

**Overrides:**
- toString

in class

Object

**Returns:**
- A string describing the open package

---

### Additional Sections

#### Class ModuleDescriptor.Opens

java.lang.Object

- java.lang.module.ModuleDescriptor.Opens

java.lang.module.ModuleDescriptor.Opens

**All Implemented Interfaces:** Comparable

<

ModuleDescriptor.Opens

>

**Enclosing class:** ModuleDescriptor

```java
public static final class
ModuleDescriptor.Opens

extends
Object

implements
Comparable
<
ModuleDescriptor.Opens
>
```

A package opened by a module, may be qualified or unqualified.

The

opens

directive in a module declaration declares a
package to be open to allow all types in the package, and all their
members, not just public types and their public members to be reflected
on by APIs that support private access or a way to bypass or suppress
default Java language access control checks.

**Since:** 9
**See Also:** ModuleDescriptor.opens()

public static final class

ModuleDescriptor.Opens

extends

Object

implements

Comparable

<

ModuleDescriptor.Opens

>

A package opened by a module, may be qualified or unqualified.

The

opens

directive in a module declaration declares a
package to be open to allow all types in the package, and all their
members, not just public types and their public members to be reflected
on by APIs that support private access or a way to bypass or suppress
default Java language access control checks.

A package opened by a module, may be qualified or unqualified.

The

opens

directive in a module declaration declares a
package to be open to allow all types in the package, and all their
members, not just public types and their public members to be reflected
on by APIs that support private access or a way to bypass or suppress
default Java language access control checks.

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

static class

ModuleDescriptor.Opens.Modifier

A modifier on an open package.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

int

compareTo

​(

ModuleDescriptor.Opens

that)

Compares this module opens to another.

boolean

equals

​(

Object

ob)

Tests this module opens for equality with the given object.

int

hashCode

()

Computes a hash code for this module opens.

boolean

isQualified

()

Returns

true

if this is a qualified opens.

Set

<

ModuleDescriptor.Opens.Modifier

>

modifiers

()

Returns the set of modifiers.

String

source

()

Returns the package name.

Set

<

String

>

targets

()

For a qualified opens, returns the non-empty and immutable set
of the module names to which the package is open.

String

toString

()

Returns a string describing the open package.

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

ModuleDescriptor.Opens.Modifier

A modifier on an open package.

---

#### Nested Class Summary

A modifier on an open package.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

int

compareTo

​(

ModuleDescriptor.Opens

that)

Compares this module opens to another.

boolean

equals

​(

Object

ob)

Tests this module opens for equality with the given object.

int

hashCode

()

Computes a hash code for this module opens.

boolean

isQualified

()

Returns

true

if this is a qualified opens.

Set

<

ModuleDescriptor.Opens.Modifier

>

modifiers

()

Returns the set of modifiers.

String

source

()

Returns the package name.

Set

<

String

>

targets

()

For a qualified opens, returns the non-empty and immutable set
of the module names to which the package is open.

String

toString

()

Returns a string describing the open package.

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

Compares this module opens to another.

Tests this module opens for equality with the given object.

Computes a hash code for this module opens.

Returns

true

if this is a qualified opens.

Returns the set of modifiers.

Returns the package name.

For a qualified opens, returns the non-empty and immutable set
of the module names to which the package is open.

Returns a string describing the open package.

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

- modifiers

```java
public
Set
<
ModuleDescriptor.Opens.Modifier
> modifiers()
```

Returns the set of modifiers.

**Returns:** A possibly-empty unmodifiable set of modifiers

- isQualified

```java
public boolean isQualified()
```

Returns

true

if this is a qualified opens.

**Returns:** true

if this is a qualified opens

- source

```java
public
String
source()
```

Returns the package name.

**Returns:** The package name

- targets

```java
public
Set
<
String
> targets()
```

For a qualified opens, returns the non-empty and immutable set
of the module names to which the package is open. For an
unqualified opens, returns an empty set.

**Returns:** The set of target module names or for an unqualified
opens, an empty set

- compareTo

```java
public int compareTo​(
ModuleDescriptor.Opens
that)
```

Compares this module opens to another.

Two

Opens

objects are compared by comparing the package
names lexicographically. Where the packages names are equal then the
sets of modifiers are compared in the same way that module modifiers
are compared (see

ModuleDescriptor.compareTo

). Where the package names are equal and
the set of modifiers are equal then the set of target modules are
compared. This is done by sorting the names of the target modules
in ascending order, and according to their natural ordering, and then
comparing the corresponding elements lexicographically. Where the
sets differ in size, and the larger set contains all elements of the
smaller set, then the larger set is considered to succeed the smaller
set.

**Specified by:** compareTo

in interface

Comparable

<

ModuleDescriptor.Opens

>
**Parameters:** that

- The module opens to compare
**Returns:** A negative integer, zero, or a positive integer if this module
opens is less than, equal to, or greater than the given
module opens

- hashCode

```java
public int hashCode()
```

Computes a hash code for this module opens.

The hash code is based upon the modifiers, the package name,
and for a qualified opens, the set of modules names to which the
package is opened. It satisfies the general contract of the

Object.hashCode

method.

**Overrides:** hashCode

in class

Object
**Returns:** The hash-code value for this module opens
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

- equals

```java
public boolean equals​(
Object
ob)
```

Tests this module opens for equality with the given object.

If the given object is not an

Opens

then this method
returns

false

. Two

Opens

objects are equal if their
set of modifiers is equal, the package names are equal and the set
of target module names is equal.

This method satisfies the general contract of the

Object.equals

method.

**Overrides:** equals

in class

Object
**Parameters:** ob

- the object to which this object is to be compared
**Returns:** true

if, and only if, the given object is a module
dependence that is equal to this module dependence
**See Also:** Object.hashCode()

,

HashMap

- toString

```java
public
String
toString()
```

Returns a string describing the open package.

**Overrides:** toString

in class

Object
**Returns:** A string describing the open package

Method Detail

- modifiers

```java
public
Set
<
ModuleDescriptor.Opens.Modifier
> modifiers()
```

Returns the set of modifiers.

**Returns:** A possibly-empty unmodifiable set of modifiers

- isQualified

```java
public boolean isQualified()
```

Returns

true

if this is a qualified opens.

**Returns:** true

if this is a qualified opens

- source

```java
public
String
source()
```

Returns the package name.

**Returns:** The package name

- targets

```java
public
Set
<
String
> targets()
```

For a qualified opens, returns the non-empty and immutable set
of the module names to which the package is open. For an
unqualified opens, returns an empty set.

**Returns:** The set of target module names or for an unqualified
opens, an empty set

- compareTo

```java
public int compareTo​(
ModuleDescriptor.Opens
that)
```

Compares this module opens to another.

Two

Opens

objects are compared by comparing the package
names lexicographically. Where the packages names are equal then the
sets of modifiers are compared in the same way that module modifiers
are compared (see

ModuleDescriptor.compareTo

). Where the package names are equal and
the set of modifiers are equal then the set of target modules are
compared. This is done by sorting the names of the target modules
in ascending order, and according to their natural ordering, and then
comparing the corresponding elements lexicographically. Where the
sets differ in size, and the larger set contains all elements of the
smaller set, then the larger set is considered to succeed the smaller
set.

**Specified by:** compareTo

in interface

Comparable

<

ModuleDescriptor.Opens

>
**Parameters:** that

- The module opens to compare
**Returns:** A negative integer, zero, or a positive integer if this module
opens is less than, equal to, or greater than the given
module opens

- hashCode

```java
public int hashCode()
```

Computes a hash code for this module opens.

The hash code is based upon the modifiers, the package name,
and for a qualified opens, the set of modules names to which the
package is opened. It satisfies the general contract of the

Object.hashCode

method.

**Overrides:** hashCode

in class

Object
**Returns:** The hash-code value for this module opens
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

- equals

```java
public boolean equals​(
Object
ob)
```

Tests this module opens for equality with the given object.

If the given object is not an

Opens

then this method
returns

false

. Two

Opens

objects are equal if their
set of modifiers is equal, the package names are equal and the set
of target module names is equal.

This method satisfies the general contract of the

Object.equals

method.

**Overrides:** equals

in class

Object
**Parameters:** ob

- the object to which this object is to be compared
**Returns:** true

if, and only if, the given object is a module
dependence that is equal to this module dependence
**See Also:** Object.hashCode()

,

HashMap

- toString

```java
public
String
toString()
```

Returns a string describing the open package.

**Overrides:** toString

in class

Object
**Returns:** A string describing the open package

---

#### Method Detail

modifiers

```java
public
Set
<
ModuleDescriptor.Opens.Modifier
> modifiers()
```

Returns the set of modifiers.

**Returns:** A possibly-empty unmodifiable set of modifiers

---

#### modifiers

public

Set

<

ModuleDescriptor.Opens.Modifier

> modifiers()

Returns the set of modifiers.

isQualified

```java
public boolean isQualified()
```

Returns

true

if this is a qualified opens.

**Returns:** true

if this is a qualified opens

---

#### isQualified

public boolean isQualified()

Returns

true

if this is a qualified opens.

source

```java
public
String
source()
```

Returns the package name.

**Returns:** The package name

---

#### source

public

String

source()

Returns the package name.

targets

```java
public
Set
<
String
> targets()
```

For a qualified opens, returns the non-empty and immutable set
of the module names to which the package is open. For an
unqualified opens, returns an empty set.

**Returns:** The set of target module names or for an unqualified
opens, an empty set

---

#### targets

public

Set

<

String

> targets()

For a qualified opens, returns the non-empty and immutable set
of the module names to which the package is open. For an
unqualified opens, returns an empty set.

compareTo

```java
public int compareTo​(
ModuleDescriptor.Opens
that)
```

Compares this module opens to another.

Two

Opens

objects are compared by comparing the package
names lexicographically. Where the packages names are equal then the
sets of modifiers are compared in the same way that module modifiers
are compared (see

ModuleDescriptor.compareTo

). Where the package names are equal and
the set of modifiers are equal then the set of target modules are
compared. This is done by sorting the names of the target modules
in ascending order, and according to their natural ordering, and then
comparing the corresponding elements lexicographically. Where the
sets differ in size, and the larger set contains all elements of the
smaller set, then the larger set is considered to succeed the smaller
set.

**Specified by:** compareTo

in interface

Comparable

<

ModuleDescriptor.Opens

>
**Parameters:** that

- The module opens to compare
**Returns:** A negative integer, zero, or a positive integer if this module
opens is less than, equal to, or greater than the given
module opens

---

#### compareTo

public int compareTo​(

ModuleDescriptor.Opens

that)

Compares this module opens to another.

Two

Opens

objects are compared by comparing the package
names lexicographically. Where the packages names are equal then the
sets of modifiers are compared in the same way that module modifiers
are compared (see

ModuleDescriptor.compareTo

). Where the package names are equal and
the set of modifiers are equal then the set of target modules are
compared. This is done by sorting the names of the target modules
in ascending order, and according to their natural ordering, and then
comparing the corresponding elements lexicographically. Where the
sets differ in size, and the larger set contains all elements of the
smaller set, then the larger set is considered to succeed the smaller
set.

Two

Opens

objects are compared by comparing the package
names lexicographically. Where the packages names are equal then the
sets of modifiers are compared in the same way that module modifiers
are compared (see

ModuleDescriptor.compareTo

). Where the package names are equal and
the set of modifiers are equal then the set of target modules are
compared. This is done by sorting the names of the target modules
in ascending order, and according to their natural ordering, and then
comparing the corresponding elements lexicographically. Where the
sets differ in size, and the larger set contains all elements of the
smaller set, then the larger set is considered to succeed the smaller
set.

hashCode

```java
public int hashCode()
```

Computes a hash code for this module opens.

The hash code is based upon the modifiers, the package name,
and for a qualified opens, the set of modules names to which the
package is opened. It satisfies the general contract of the

Object.hashCode

method.

**Overrides:** hashCode

in class

Object
**Returns:** The hash-code value for this module opens
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### hashCode

public int hashCode()

Computes a hash code for this module opens.

The hash code is based upon the modifiers, the package name,
and for a qualified opens, the set of modules names to which the
package is opened. It satisfies the general contract of the

Object.hashCode

method.

The hash code is based upon the modifiers, the package name,
and for a qualified opens, the set of modules names to which the
package is opened. It satisfies the general contract of the

Object.hashCode

method.

equals

```java
public boolean equals​(
Object
ob)
```

Tests this module opens for equality with the given object.

If the given object is not an

Opens

then this method
returns

false

. Two

Opens

objects are equal if their
set of modifiers is equal, the package names are equal and the set
of target module names is equal.

This method satisfies the general contract of the

Object.equals

method.

**Overrides:** equals

in class

Object
**Parameters:** ob

- the object to which this object is to be compared
**Returns:** true

if, and only if, the given object is a module
dependence that is equal to this module dependence
**See Also:** Object.hashCode()

,

HashMap

---

#### equals

public boolean equals​(

Object

ob)

Tests this module opens for equality with the given object.

If the given object is not an

Opens

then this method
returns

false

. Two

Opens

objects are equal if their
set of modifiers is equal, the package names are equal and the set
of target module names is equal.

This method satisfies the general contract of the

Object.equals

method.

If the given object is not an

Opens

then this method
returns

false

. Two

Opens

objects are equal if their
set of modifiers is equal, the package names are equal and the set
of target module names is equal.

This method satisfies the general contract of the

Object.equals

method.

toString

```java
public
String
toString()
```

Returns a string describing the open package.

**Overrides:** toString

in class

Object
**Returns:** A string describing the open package

---

#### toString

public

String

toString()

Returns a string describing the open package.

---

