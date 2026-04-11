# Class ModuleDescriptor.Exports

**Source:** `java.base\java\lang\module\ModuleDescriptor.Exports.html`

### Class Description

```java
public static final class
ModuleDescriptor.Exports

extends
Object

implements
Comparable
<
ModuleDescriptor.Exports
>
```

A package exported by a module, may be qualified or unqualified.

**All Implemented Interfaces:** Comparable

<

ModuleDescriptor.Exports

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
ModuleDescriptor.Exports.Modifier
> modifiers()

Returns the set of modifiers.

**Returns:**
- A possibly-empty unmodifiable set of modifiers

---

#### public boolean isQualified()

Returns

true

if this is a qualified export.

**Returns:**
- true

if this is a qualified export

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

For a qualified export, returns the non-empty and immutable set
of the module names to which the package is exported. For an
unqualified export, returns an empty set.

**Returns:**
- The set of target module names or for an unqualified
export, an empty set

---

#### public int compareTo​(
ModuleDescriptor.Exports
that)

Compares this module export to another.

Two

Exports

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

ModuleDescriptor.Exports

>

**Parameters:**
- that

- The module export to compare

**Returns:**
- A negative integer, zero, or a positive integer if this module
export is less than, equal to, or greater than the given
export dependence

---

#### public int hashCode()

Computes a hash code for this module export.

The hash code is based upon the modifiers, the package name,
and for a qualified export, the set of modules names to which the
package is exported. It satisfies the general contract of the

Object.hashCode

method.

**Overrides:**
- hashCode

in class

Object

**Returns:**
- The hash-code value for this module export

**See Also:**
- Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### public boolean equals​(
Object
ob)

Tests this module export for equality with the given object.

If the given object is not an

Exports

then this method
returns

false

. Two module exports objects are equal if their
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

Returns a string describing the exported package.

**Overrides:**
- toString

in class

Object

**Returns:**
- A string describing the exported package

---

### Additional Sections

#### Class ModuleDescriptor.Exports

java.lang.Object

- java.lang.module.ModuleDescriptor.Exports

java.lang.module.ModuleDescriptor.Exports

**All Implemented Interfaces:** Comparable

<

ModuleDescriptor.Exports

>

**Enclosing class:** ModuleDescriptor

```java
public static final class
ModuleDescriptor.Exports

extends
Object

implements
Comparable
<
ModuleDescriptor.Exports
>
```

A package exported by a module, may be qualified or unqualified.

**Since:** 9
**See Also:** ModuleDescriptor.exports()

public static final class

ModuleDescriptor.Exports

extends

Object

implements

Comparable

<

ModuleDescriptor.Exports

>

A package exported by a module, may be qualified or unqualified.

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

static class

ModuleDescriptor.Exports.Modifier

A modifier on an exported package.

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

ModuleDescriptor.Exports

that)

Compares this module export to another.

boolean

equals

​(

Object

ob)

Tests this module export for equality with the given object.

int

hashCode

()

Computes a hash code for this module export.

boolean

isQualified

()

Returns

true

if this is a qualified export.

Set

<

ModuleDescriptor.Exports.Modifier

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

For a qualified export, returns the non-empty and immutable set
of the module names to which the package is exported.

String

toString

()

Returns a string describing the exported package.

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

ModuleDescriptor.Exports.Modifier

A modifier on an exported package.

---

#### Nested Class Summary

A modifier on an exported package.

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

ModuleDescriptor.Exports

that)

Compares this module export to another.

boolean

equals

​(

Object

ob)

Tests this module export for equality with the given object.

int

hashCode

()

Computes a hash code for this module export.

boolean

isQualified

()

Returns

true

if this is a qualified export.

Set

<

ModuleDescriptor.Exports.Modifier

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

For a qualified export, returns the non-empty and immutable set
of the module names to which the package is exported.

String

toString

()

Returns a string describing the exported package.

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

Compares this module export to another.

Tests this module export for equality with the given object.

Computes a hash code for this module export.

Returns

true

if this is a qualified export.

Returns the set of modifiers.

Returns the package name.

For a qualified export, returns the non-empty and immutable set
of the module names to which the package is exported.

Returns a string describing the exported package.

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
ModuleDescriptor.Exports.Modifier
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

if this is a qualified export.

**Returns:** true

if this is a qualified export

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

For a qualified export, returns the non-empty and immutable set
of the module names to which the package is exported. For an
unqualified export, returns an empty set.

**Returns:** The set of target module names or for an unqualified
export, an empty set

- compareTo

```java
public int compareTo​(
ModuleDescriptor.Exports
that)
```

Compares this module export to another.

Two

Exports

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

ModuleDescriptor.Exports

>
**Parameters:** that

- The module export to compare
**Returns:** A negative integer, zero, or a positive integer if this module
export is less than, equal to, or greater than the given
export dependence

- hashCode

```java
public int hashCode()
```

Computes a hash code for this module export.

The hash code is based upon the modifiers, the package name,
and for a qualified export, the set of modules names to which the
package is exported. It satisfies the general contract of the

Object.hashCode

method.

**Overrides:** hashCode

in class

Object
**Returns:** The hash-code value for this module export
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

- equals

```java
public boolean equals​(
Object
ob)
```

Tests this module export for equality with the given object.

If the given object is not an

Exports

then this method
returns

false

. Two module exports objects are equal if their
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

Returns a string describing the exported package.

**Overrides:** toString

in class

Object
**Returns:** A string describing the exported package

Method Detail

- modifiers

```java
public
Set
<
ModuleDescriptor.Exports.Modifier
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

if this is a qualified export.

**Returns:** true

if this is a qualified export

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

For a qualified export, returns the non-empty and immutable set
of the module names to which the package is exported. For an
unqualified export, returns an empty set.

**Returns:** The set of target module names or for an unqualified
export, an empty set

- compareTo

```java
public int compareTo​(
ModuleDescriptor.Exports
that)
```

Compares this module export to another.

Two

Exports

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

ModuleDescriptor.Exports

>
**Parameters:** that

- The module export to compare
**Returns:** A negative integer, zero, or a positive integer if this module
export is less than, equal to, or greater than the given
export dependence

- hashCode

```java
public int hashCode()
```

Computes a hash code for this module export.

The hash code is based upon the modifiers, the package name,
and for a qualified export, the set of modules names to which the
package is exported. It satisfies the general contract of the

Object.hashCode

method.

**Overrides:** hashCode

in class

Object
**Returns:** The hash-code value for this module export
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

- equals

```java
public boolean equals​(
Object
ob)
```

Tests this module export for equality with the given object.

If the given object is not an

Exports

then this method
returns

false

. Two module exports objects are equal if their
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

Returns a string describing the exported package.

**Overrides:** toString

in class

Object
**Returns:** A string describing the exported package

---

#### Method Detail

modifiers

```java
public
Set
<
ModuleDescriptor.Exports.Modifier
> modifiers()
```

Returns the set of modifiers.

**Returns:** A possibly-empty unmodifiable set of modifiers

---

#### modifiers

public

Set

<

ModuleDescriptor.Exports.Modifier

> modifiers()

Returns the set of modifiers.

isQualified

```java
public boolean isQualified()
```

Returns

true

if this is a qualified export.

**Returns:** true

if this is a qualified export

---

#### isQualified

public boolean isQualified()

Returns

true

if this is a qualified export.

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

For a qualified export, returns the non-empty and immutable set
of the module names to which the package is exported. For an
unqualified export, returns an empty set.

**Returns:** The set of target module names or for an unqualified
export, an empty set

---

#### targets

public

Set

<

String

> targets()

For a qualified export, returns the non-empty and immutable set
of the module names to which the package is exported. For an
unqualified export, returns an empty set.

compareTo

```java
public int compareTo​(
ModuleDescriptor.Exports
that)
```

Compares this module export to another.

Two

Exports

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

ModuleDescriptor.Exports

>
**Parameters:** that

- The module export to compare
**Returns:** A negative integer, zero, or a positive integer if this module
export is less than, equal to, or greater than the given
export dependence

---

#### compareTo

public int compareTo​(

ModuleDescriptor.Exports

that)

Compares this module export to another.

Two

Exports

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

Exports

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

Computes a hash code for this module export.

The hash code is based upon the modifiers, the package name,
and for a qualified export, the set of modules names to which the
package is exported. It satisfies the general contract of the

Object.hashCode

method.

**Overrides:** hashCode

in class

Object
**Returns:** The hash-code value for this module export
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### hashCode

public int hashCode()

Computes a hash code for this module export.

The hash code is based upon the modifiers, the package name,
and for a qualified export, the set of modules names to which the
package is exported. It satisfies the general contract of the

Object.hashCode

method.

The hash code is based upon the modifiers, the package name,
and for a qualified export, the set of modules names to which the
package is exported. It satisfies the general contract of the

Object.hashCode

method.

equals

```java
public boolean equals​(
Object
ob)
```

Tests this module export for equality with the given object.

If the given object is not an

Exports

then this method
returns

false

. Two module exports objects are equal if their
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

Tests this module export for equality with the given object.

If the given object is not an

Exports

then this method
returns

false

. Two module exports objects are equal if their
set of modifiers is equal, the package names are equal and the set
of target module names is equal.

This method satisfies the general contract of the

Object.equals

method.

If the given object is not an

Exports

then this method
returns

false

. Two module exports objects are equal if their
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

Returns a string describing the exported package.

**Overrides:** toString

in class

Object
**Returns:** A string describing the exported package

---

#### toString

public

String

toString()

Returns a string describing the exported package.

---

