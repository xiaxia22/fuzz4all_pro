# Class ModuleDescriptor.Requires

**Source:** `java.base\java\lang\module\ModuleDescriptor.Requires.html`

### Class Description

```java
public static final class
ModuleDescriptor.Requires

extends
Object

implements
Comparable
<
ModuleDescriptor.Requires
>
```

A dependence upon a module

**All Implemented Interfaces:** Comparable

<

ModuleDescriptor.Requires

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
ModuleDescriptor.Requires.Modifier
> modifiers()

Returns the set of modifiers.

**Returns:**
- A possibly-empty unmodifiable set of modifiers

---

#### public
String
name()

Return the module name.

**Returns:**
- The module name

---

#### public
Optional
<
ModuleDescriptor.Version
> compiledVersion()

Returns the version of the module if recorded at compile-time.

**Returns:**
- The version of the module if recorded at compile-time,
or an empty

Optional

if no version was recorded or
the version string recorded is

unparseable

---

#### public
Optional
<
String
> rawCompiledVersion()

Returns the string with the possibly-unparseable version of the module
if recorded at compile-time.

**Returns:**
- The string containing the version of the module if recorded
at compile-time, or an empty

Optional

if no version
was recorded

**See Also:**
- compiledVersion()

---

#### public int compareTo​(
ModuleDescriptor.Requires
that)

Compares this module dependence to another.

Two

Requires

objects are compared by comparing their
module names lexicographically. Where the module names are equal
then the sets of modifiers are compared in the same way that
module modifiers are compared (see

ModuleDescriptor.compareTo

). Where the module names are equal and
the set of modifiers are equal then the version of the modules
recorded at compile-time are compared. When comparing the versions
recorded at compile-time then a dependence that has a recorded
version is considered to succeed a dependence that does not have a
recorded version. If both recorded versions are

unparseable

then the

raw version strings

are compared
lexicographically.

**Specified by:**
- compareTo

in interface

Comparable

<

ModuleDescriptor.Requires

>

**Parameters:**
- that

- The module dependence to compare

**Returns:**
- A negative integer, zero, or a positive integer if this module
dependence is less than, equal to, or greater than the given
module dependence

---

#### public boolean equals​(
Object
ob)

Tests this module dependence for equality with the given object.

If the given object is not a

Requires

then this method
returns

false

. Two module dependence objects are equal if
the module names are equal, set of modifiers are equal, and the
compiled version of both modules is equal or not recorded for
both modules.

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

#### public int hashCode()

Computes a hash code for this module dependence.

The hash code is based upon the module name, modifiers, and the
module version if recorded at compile time. It satisfies the general
contract of the

Object.hashCode

method.

**Overrides:**
- hashCode

in class

Object

**Returns:**
- The hash-code value for this module dependence

**See Also:**
- Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### public
String
toString()

Returns a string describing this module dependence.

**Overrides:**
- toString

in class

Object

**Returns:**
- A string describing this module dependence

---

### Additional Sections

#### Class ModuleDescriptor.Requires

java.lang.Object

- java.lang.module.ModuleDescriptor.Requires

java.lang.module.ModuleDescriptor.Requires

**All Implemented Interfaces:** Comparable

<

ModuleDescriptor.Requires

>

**Enclosing class:** ModuleDescriptor

```java
public static final class
ModuleDescriptor.Requires

extends
Object

implements
Comparable
<
ModuleDescriptor.Requires
>
```

A dependence upon a module

**Since:** 9
**See Also:** ModuleDescriptor.requires()

public static final class

ModuleDescriptor.Requires

extends

Object

implements

Comparable

<

ModuleDescriptor.Requires

>

A dependence upon a module

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

static class

ModuleDescriptor.Requires.Modifier

A modifier on a module dependence.

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

ModuleDescriptor.Requires

that)

Compares this module dependence to another.

Optional

<

ModuleDescriptor.Version

>

compiledVersion

()

Returns the version of the module if recorded at compile-time.

boolean

equals

​(

Object

ob)

Tests this module dependence for equality with the given object.

int

hashCode

()

Computes a hash code for this module dependence.

Set

<

ModuleDescriptor.Requires.Modifier

>

modifiers

()

Returns the set of modifiers.

String

name

()

Return the module name.

Optional

<

String

>

rawCompiledVersion

()

Returns the string with the possibly-unparseable version of the module
if recorded at compile-time.

String

toString

()

Returns a string describing this module dependence.

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

ModuleDescriptor.Requires.Modifier

A modifier on a module dependence.

---

#### Nested Class Summary

A modifier on a module dependence.

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

ModuleDescriptor.Requires

that)

Compares this module dependence to another.

Optional

<

ModuleDescriptor.Version

>

compiledVersion

()

Returns the version of the module if recorded at compile-time.

boolean

equals

​(

Object

ob)

Tests this module dependence for equality with the given object.

int

hashCode

()

Computes a hash code for this module dependence.

Set

<

ModuleDescriptor.Requires.Modifier

>

modifiers

()

Returns the set of modifiers.

String

name

()

Return the module name.

Optional

<

String

>

rawCompiledVersion

()

Returns the string with the possibly-unparseable version of the module
if recorded at compile-time.

String

toString

()

Returns a string describing this module dependence.

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

Compares this module dependence to another.

Returns the version of the module if recorded at compile-time.

Tests this module dependence for equality with the given object.

Computes a hash code for this module dependence.

Returns the set of modifiers.

Return the module name.

Returns the string with the possibly-unparseable version of the module
if recorded at compile-time.

Returns a string describing this module dependence.

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
ModuleDescriptor.Requires.Modifier
> modifiers()
```

Returns the set of modifiers.

**Returns:** A possibly-empty unmodifiable set of modifiers

- name

```java
public
String
name()
```

Return the module name.

**Returns:** The module name

- compiledVersion

```java
public
Optional
<
ModuleDescriptor.Version
> compiledVersion()
```

Returns the version of the module if recorded at compile-time.

**Returns:** The version of the module if recorded at compile-time,
or an empty

Optional

if no version was recorded or
the version string recorded is

unparseable

- rawCompiledVersion

```java
public
Optional
<
String
> rawCompiledVersion()
```

Returns the string with the possibly-unparseable version of the module
if recorded at compile-time.

**Returns:** The string containing the version of the module if recorded
at compile-time, or an empty

Optional

if no version
was recorded
**See Also:** compiledVersion()

- compareTo

```java
public int compareTo​(
ModuleDescriptor.Requires
that)
```

Compares this module dependence to another.

Two

Requires

objects are compared by comparing their
module names lexicographically. Where the module names are equal
then the sets of modifiers are compared in the same way that
module modifiers are compared (see

ModuleDescriptor.compareTo

). Where the module names are equal and
the set of modifiers are equal then the version of the modules
recorded at compile-time are compared. When comparing the versions
recorded at compile-time then a dependence that has a recorded
version is considered to succeed a dependence that does not have a
recorded version. If both recorded versions are

unparseable

then the

raw version strings

are compared
lexicographically.

**Specified by:** compareTo

in interface

Comparable

<

ModuleDescriptor.Requires

>
**Parameters:** that

- The module dependence to compare
**Returns:** A negative integer, zero, or a positive integer if this module
dependence is less than, equal to, or greater than the given
module dependence

- equals

```java
public boolean equals​(
Object
ob)
```

Tests this module dependence for equality with the given object.

If the given object is not a

Requires

then this method
returns

false

. Two module dependence objects are equal if
the module names are equal, set of modifiers are equal, and the
compiled version of both modules is equal or not recorded for
both modules.

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

- hashCode

```java
public int hashCode()
```

Computes a hash code for this module dependence.

The hash code is based upon the module name, modifiers, and the
module version if recorded at compile time. It satisfies the general
contract of the

Object.hashCode

method.

**Overrides:** hashCode

in class

Object
**Returns:** The hash-code value for this module dependence
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

- toString

```java
public
String
toString()
```

Returns a string describing this module dependence.

**Overrides:** toString

in class

Object
**Returns:** A string describing this module dependence

Method Detail

- modifiers

```java
public
Set
<
ModuleDescriptor.Requires.Modifier
> modifiers()
```

Returns the set of modifiers.

**Returns:** A possibly-empty unmodifiable set of modifiers

- name

```java
public
String
name()
```

Return the module name.

**Returns:** The module name

- compiledVersion

```java
public
Optional
<
ModuleDescriptor.Version
> compiledVersion()
```

Returns the version of the module if recorded at compile-time.

**Returns:** The version of the module if recorded at compile-time,
or an empty

Optional

if no version was recorded or
the version string recorded is

unparseable

- rawCompiledVersion

```java
public
Optional
<
String
> rawCompiledVersion()
```

Returns the string with the possibly-unparseable version of the module
if recorded at compile-time.

**Returns:** The string containing the version of the module if recorded
at compile-time, or an empty

Optional

if no version
was recorded
**See Also:** compiledVersion()

- compareTo

```java
public int compareTo​(
ModuleDescriptor.Requires
that)
```

Compares this module dependence to another.

Two

Requires

objects are compared by comparing their
module names lexicographically. Where the module names are equal
then the sets of modifiers are compared in the same way that
module modifiers are compared (see

ModuleDescriptor.compareTo

). Where the module names are equal and
the set of modifiers are equal then the version of the modules
recorded at compile-time are compared. When comparing the versions
recorded at compile-time then a dependence that has a recorded
version is considered to succeed a dependence that does not have a
recorded version. If both recorded versions are

unparseable

then the

raw version strings

are compared
lexicographically.

**Specified by:** compareTo

in interface

Comparable

<

ModuleDescriptor.Requires

>
**Parameters:** that

- The module dependence to compare
**Returns:** A negative integer, zero, or a positive integer if this module
dependence is less than, equal to, or greater than the given
module dependence

- equals

```java
public boolean equals​(
Object
ob)
```

Tests this module dependence for equality with the given object.

If the given object is not a

Requires

then this method
returns

false

. Two module dependence objects are equal if
the module names are equal, set of modifiers are equal, and the
compiled version of both modules is equal or not recorded for
both modules.

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

- hashCode

```java
public int hashCode()
```

Computes a hash code for this module dependence.

The hash code is based upon the module name, modifiers, and the
module version if recorded at compile time. It satisfies the general
contract of the

Object.hashCode

method.

**Overrides:** hashCode

in class

Object
**Returns:** The hash-code value for this module dependence
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

- toString

```java
public
String
toString()
```

Returns a string describing this module dependence.

**Overrides:** toString

in class

Object
**Returns:** A string describing this module dependence

---

#### Method Detail

modifiers

```java
public
Set
<
ModuleDescriptor.Requires.Modifier
> modifiers()
```

Returns the set of modifiers.

**Returns:** A possibly-empty unmodifiable set of modifiers

---

#### modifiers

public

Set

<

ModuleDescriptor.Requires.Modifier

> modifiers()

Returns the set of modifiers.

name

```java
public
String
name()
```

Return the module name.

**Returns:** The module name

---

#### name

public

String

name()

Return the module name.

compiledVersion

```java
public
Optional
<
ModuleDescriptor.Version
> compiledVersion()
```

Returns the version of the module if recorded at compile-time.

**Returns:** The version of the module if recorded at compile-time,
or an empty

Optional

if no version was recorded or
the version string recorded is

unparseable

---

#### compiledVersion

public

Optional

<

ModuleDescriptor.Version

> compiledVersion()

Returns the version of the module if recorded at compile-time.

rawCompiledVersion

```java
public
Optional
<
String
> rawCompiledVersion()
```

Returns the string with the possibly-unparseable version of the module
if recorded at compile-time.

**Returns:** The string containing the version of the module if recorded
at compile-time, or an empty

Optional

if no version
was recorded
**See Also:** compiledVersion()

---

#### rawCompiledVersion

public

Optional

<

String

> rawCompiledVersion()

Returns the string with the possibly-unparseable version of the module
if recorded at compile-time.

compareTo

```java
public int compareTo​(
ModuleDescriptor.Requires
that)
```

Compares this module dependence to another.

Two

Requires

objects are compared by comparing their
module names lexicographically. Where the module names are equal
then the sets of modifiers are compared in the same way that
module modifiers are compared (see

ModuleDescriptor.compareTo

). Where the module names are equal and
the set of modifiers are equal then the version of the modules
recorded at compile-time are compared. When comparing the versions
recorded at compile-time then a dependence that has a recorded
version is considered to succeed a dependence that does not have a
recorded version. If both recorded versions are

unparseable

then the

raw version strings

are compared
lexicographically.

**Specified by:** compareTo

in interface

Comparable

<

ModuleDescriptor.Requires

>
**Parameters:** that

- The module dependence to compare
**Returns:** A negative integer, zero, or a positive integer if this module
dependence is less than, equal to, or greater than the given
module dependence

---

#### compareTo

public int compareTo​(

ModuleDescriptor.Requires

that)

Compares this module dependence to another.

Two

Requires

objects are compared by comparing their
module names lexicographically. Where the module names are equal
then the sets of modifiers are compared in the same way that
module modifiers are compared (see

ModuleDescriptor.compareTo

). Where the module names are equal and
the set of modifiers are equal then the version of the modules
recorded at compile-time are compared. When comparing the versions
recorded at compile-time then a dependence that has a recorded
version is considered to succeed a dependence that does not have a
recorded version. If both recorded versions are

unparseable

then the

raw version strings

are compared
lexicographically.

Two

Requires

objects are compared by comparing their
module names lexicographically. Where the module names are equal
then the sets of modifiers are compared in the same way that
module modifiers are compared (see

ModuleDescriptor.compareTo

). Where the module names are equal and
the set of modifiers are equal then the version of the modules
recorded at compile-time are compared. When comparing the versions
recorded at compile-time then a dependence that has a recorded
version is considered to succeed a dependence that does not have a
recorded version. If both recorded versions are

unparseable

then the

raw version strings

are compared
lexicographically.

equals

```java
public boolean equals​(
Object
ob)
```

Tests this module dependence for equality with the given object.

If the given object is not a

Requires

then this method
returns

false

. Two module dependence objects are equal if
the module names are equal, set of modifiers are equal, and the
compiled version of both modules is equal or not recorded for
both modules.

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

Tests this module dependence for equality with the given object.

If the given object is not a

Requires

then this method
returns

false

. Two module dependence objects are equal if
the module names are equal, set of modifiers are equal, and the
compiled version of both modules is equal or not recorded for
both modules.

This method satisfies the general contract of the

Object.equals

method.

If the given object is not a

Requires

then this method
returns

false

. Two module dependence objects are equal if
the module names are equal, set of modifiers are equal, and the
compiled version of both modules is equal or not recorded for
both modules.

This method satisfies the general contract of the

Object.equals

method.

hashCode

```java
public int hashCode()
```

Computes a hash code for this module dependence.

The hash code is based upon the module name, modifiers, and the
module version if recorded at compile time. It satisfies the general
contract of the

Object.hashCode

method.

**Overrides:** hashCode

in class

Object
**Returns:** The hash-code value for this module dependence
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### hashCode

public int hashCode()

Computes a hash code for this module dependence.

The hash code is based upon the module name, modifiers, and the
module version if recorded at compile time. It satisfies the general
contract of the

Object.hashCode

method.

The hash code is based upon the module name, modifiers, and the
module version if recorded at compile time. It satisfies the general
contract of the

Object.hashCode

method.

toString

```java
public
String
toString()
```

Returns a string describing this module dependence.

**Overrides:** toString

in class

Object
**Returns:** A string describing this module dependence

---

#### toString

public

String

toString()

Returns a string describing this module dependence.

---

