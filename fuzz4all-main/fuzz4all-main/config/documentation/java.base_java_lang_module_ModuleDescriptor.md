# Class ModuleDescriptor

**Source:** `java.base\java\lang\module\ModuleDescriptor.html`

### Class Description

```java
public class
ModuleDescriptor

extends
Object

implements
Comparable
<
ModuleDescriptor
>
```

A module descriptor.

A module descriptor describes a named module and defines methods to
obtain each of its components. The module descriptor for a named module
in the Java virtual machine is obtained by invoking the

Module

's

getDescriptor

method. Module descriptors can also be created using the

ModuleDescriptor.Builder

class or by reading the binary form of a
module declaration (

module-info.class

) using the

read

methods defined here.

A module descriptor describes a

normal

, open, or automatic
module.

Normal

modules and open modules describe their

dependences

,

exported-packages

, the services
that they

use

or

provide

, and other
components.

Normal

modules may

open

specific
packages. The module descriptor for an open modules does not declare any
open packages (its

opens

method returns an empty set) but when
instantiated in the Java virtual machine then it is treated as if all
packages are open. The module descriptor for an automatic module does not
declare any dependences (except for the mandatory dependency on

java.base

), and does not declare any exported or open packages. Automatic
module receive special treatment during resolution so that they read all
other modules in the configuration. When an automatic module is instantiated
in the Java virtual machine then it reads every unnamed module and is
treated as if all packages are exported and open.

ModuleDescriptor

objects are immutable and safe for use by
multiple concurrent threads.

**All Implemented Interfaces:** Comparable

<

ModuleDescriptor

>

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### public
String
name()

Returns the module name.

**Returns:**
- The module name

---

#### public
Set
<
ModuleDescriptor.Modifier
> modifiers()

Returns the set of module modifiers.

**Returns:**
- A possibly-empty unmodifiable set of modifiers

---

#### public boolean isOpen()

Returns

true

if this is an open module.

This method is equivalent to testing if the set of

modifiers

contains the

OPEN

modifier.

**Returns:**
- true

if this is an open module

---

#### public boolean isAutomatic()

Returns

true

if this is an automatic module.

This method is equivalent to testing if the set of

modifiers

contains the

AUTOMATIC

modifier.

**Returns:**
- true

if this is an automatic module

---

#### public
Set
<
ModuleDescriptor.Requires
> requires()

Returns the set of

Requires

objects representing the module
dependences.

The set includes a dependency on "

java.base

" when this
module is not named "

java.base

". If this module is an automatic
module then it does not have a dependency on any module other than
"

java.base

".

**Returns:**
- A possibly-empty unmodifiable set of

ModuleDescriptor.Requires

objects

---

#### public
Set
<
ModuleDescriptor.Exports
> exports()

Returns the set of

Exports

objects representing the exported
packages.

If this module is an automatic module then the set of exports
is empty.

**Returns:**
- A possibly-empty unmodifiable set of exported packages

---

#### public
Set
<
ModuleDescriptor.Opens
> opens()

Returns the set of

Opens

objects representing the open
packages.

If this module is an open module or an automatic module then the
set of open packages is empty.

**Returns:**
- A possibly-empty unmodifiable set of open packages

---

#### public
Set
<
String
> uses()

Returns the set of service dependences.

If this module is an automatic module then the set of service
dependences is empty.

**Returns:**
- A possibly-empty unmodifiable set of the fully qualified class
names of the service types used

---

#### public
Set
<
ModuleDescriptor.Provides
> provides()

Returns the set of

Provides

objects representing the
services that the module provides.

**Returns:**
- The possibly-empty unmodifiable set of the services that this
module provides

---

#### public
Optional
<
ModuleDescriptor.Version
> version()

Returns the module version.

**Returns:**
- This module's version, or an empty

Optional

if the
module does not have a version or the version is

unparseable

---

#### public
Optional
<
String
> rawVersion()

Returns the string with the possibly-unparseable version of the
module

**Returns:**
- The string containing the version of the module or an empty

Optional

if the module does not have a version

**See Also:**
- version()

---

#### public
String
toNameAndVersion()

Returns a string containing the module name and, if present, its
version.

**Returns:**
- A string containing the module name and, if present, its
version

---

#### public
Optional
<
String
> mainClass()

Returns the module main class.

**Returns:**
- The fully qualified class name of the module's main class

---

#### public
Set
<
String
> packages()

Returns the set of packages in the module.

The set of packages includes all exported and open packages, as well
as the packages of any service providers, and the package for the main
class.

**Returns:**
- A possibly-empty unmodifiable set of the packages in the module

---

#### public int compareTo​(
ModuleDescriptor
that)

Compares this module descriptor to another.

Two

ModuleDescriptor

objects are compared by comparing their
module names lexicographically. Where the module names are equal then the
module versions are compared. When comparing the module versions then a
module descriptor with a version is considered to succeed a module
descriptor that does not have a version. If both versions are

unparseable

then the

raw version strings

are compared lexicographically. Where the module names
are equal and the versions are equal (or not present in both), then the
set of modifiers are compared. Sets of modifiers are compared by comparing
a

binary value

computed for each set. If a modifier is present
in the set then the bit at the position of its ordinal is

1

in the binary value, otherwise

0

. If the two set of modifiers
are also equal then the other components of the module descriptors are
compared in a manner that is consistent with

equals

.

**Specified by:**
- compareTo

in interface

Comparable

<

ModuleDescriptor

>

**Parameters:**
- that

- The module descriptor to compare

**Returns:**
- A negative integer, zero, or a positive integer if this module
descriptor is less than, equal to, or greater than the given
module descriptor

---

#### public boolean equals​(
Object
ob)

Tests this module descriptor for equality with the given object.

If the given object is not a

ModuleDescriptor

then this
method returns

false

. Two module descriptors are equal if each
of their corresponding components is equal.

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
descriptor that is equal to this module descriptor

**See Also:**
- Object.hashCode()

,

HashMap

---

#### public int hashCode()

Computes a hash code for this module descriptor.

The hash code is based upon the components of the module descriptor,
and satisfies the general contract of the

Object.hashCode

method.

**Overrides:**
- hashCode

in class

Object

**Returns:**
- The hash-code value for this module descriptor

**See Also:**
- Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### public
String
toString()

Returns a string describing the module.

**Overrides:**
- toString

in class

Object

**Returns:**
- A string describing the module

---

#### public static
ModuleDescriptor.Builder
newModule​(
String
name,

Set
<
ModuleDescriptor.Modifier
> ms)

Instantiates a builder to build a module descriptor.

**Parameters:**
- name

- The module name
- ms

- The set of module modifiers

**Returns:**
- A new builder

**Throws:**
- IllegalArgumentException

- If the module name is

null

or is not a legal module
name, or the set of modifiers contains

AUTOMATIC

with other modifiers

---

#### public static
ModuleDescriptor.Builder
newModule​(
String
name)

Instantiates a builder to build a module descriptor for a

normal

module. This method is equivalent to invoking

newModule

with an empty set of

modifiers

.

**Parameters:**
- name

- The module name

**Returns:**
- A new builder

**Throws:**
- IllegalArgumentException

- If the module name is

null

or is not a legal module
name

---

#### public static
ModuleDescriptor.Builder
newOpenModule​(
String
name)

Instantiates a builder to build a module descriptor for an open module.
This method is equivalent to invoking

newModule

with the

OPEN

modifier.

The builder for an open module cannot be used to declare any open
packages.

**Parameters:**
- name

- The module name

**Returns:**
- A new builder that builds an open module

**Throws:**
- IllegalArgumentException

- If the module name is

null

or is not a legal module
name

---

#### public static
ModuleDescriptor.Builder
newAutomaticModule​(
String
name)

Instantiates a builder to build a module descriptor for an automatic
module. This method is equivalent to invoking

newModule

with the

AUTOMATIC

modifier.

The builder for an automatic module cannot be used to declare module
or service dependences. It also cannot be used to declare any exported
or open packages.

**Parameters:**
- name

- The module name

**Returns:**
- A new builder that builds an automatic module

**Throws:**
- IllegalArgumentException

- If the module name is

null

or is not a legal module
name

**See Also:**
- ModuleFinder.of(Path[])

---

#### public static
ModuleDescriptor
read​(
InputStream
in,

Supplier
<
Set
<
String
>> packageFinder)
throws
IOException

Reads the binary form of a module declaration from an input stream
as a module descriptor.

If the descriptor encoded in the input stream does not indicate a
set of packages in the module then the

packageFinder

will be
invoked. The set of packages that the

packageFinder

returns
must include all the packages that the module exports, opens, as well
as the packages of the service implementations that the module provides,
and the package of the main class (if the module has a main class). If
the

packageFinder

throws an

UncheckedIOException

then

IOException

cause will be re-thrown.

If there are bytes following the module descriptor then it is
implementation specific as to whether those bytes are read, ignored,
or reported as an

InvalidModuleDescriptorException

. If this
method fails with an

InvalidModuleDescriptorException

or

IOException

then it may do so after some, but not all, bytes have
been read from the input stream. It is strongly recommended that the
stream be promptly closed and discarded if an exception occurs.

**Parameters:**
- in

- The input stream
- packageFinder

- A supplier that can produce the set of packages

**Returns:**
- The module descriptor

**Throws:**
- InvalidModuleDescriptorException

- If an invalid module descriptor is detected or the set of
packages returned by the

packageFinder

does not include
all of the packages obtained from the module descriptor
- IOException

- If an I/O error occurs reading from the input stream or

UncheckedIOException

is thrown by the package finder

**API Note:**
- The

packageFinder

parameter is for use when reading
module descriptors from legacy module-artifact formats that do not
record the set of packages in the descriptor itself.

---

#### public static
ModuleDescriptor
read​(
InputStream
in)
throws
IOException

Reads the binary form of a module declaration from an input stream as a
module descriptor. This method works exactly as specified by the 2-arg

read

method with the exception that
a packager finder is not used to find additional packages when the
module descriptor read from the stream does not indicate the set of
packages.

**Parameters:**
- in

- The input stream

**Returns:**
- The module descriptor

**Throws:**
- InvalidModuleDescriptorException

- If an invalid module descriptor is detected
- IOException

- If an I/O error occurs reading from the input stream

---

#### public static
ModuleDescriptor
read​(
ByteBuffer
bb,

Supplier
<
Set
<
String
>> packageFinder)

Reads the binary form of a module declaration from a byte buffer
as a module descriptor.

If the descriptor encoded in the byte buffer does not indicate a
set of packages in the module then the

packageFinder

will be
invoked. The set of packages that the

packageFinder

returns
must include all the packages that the module exports, opens, as well
as the packages of the service implementations that the module provides,
and the package of the main class (if the module has a main class). If
the

packageFinder

throws an

UncheckedIOException

then

IOException

cause will be re-thrown.

The module descriptor is read from the buffer starting at index

p

, where

p

is the buffer's

position

when this method is invoked. Upon return the buffer's position
will be equal to

p + n

where

n

is the number of bytes
read from the buffer.

If there are bytes following the module descriptor then it is
implementation specific as to whether those bytes are read, ignored,
or reported as an

InvalidModuleDescriptorException

. If this
method fails with an

InvalidModuleDescriptorException

then it
may do so after some, but not all, bytes have been read.

**Parameters:**
- bb

- The byte buffer
- packageFinder

- A supplier that can produce the set of packages

**Returns:**
- The module descriptor

**Throws:**
- InvalidModuleDescriptorException

- If an invalid module descriptor is detected or the set of
packages returned by the

packageFinder

does not include
all of the packages obtained from the module descriptor

**API Note:**
- The

packageFinder

parameter is for use when reading
module descriptors from legacy module-artifact formats that do not
record the set of packages in the descriptor itself.

---

#### public static
ModuleDescriptor
read​(
ByteBuffer
bb)

Reads the binary form of a module declaration from a byte buffer as a
module descriptor. This method works exactly as specified by the 2-arg

read

method with the exception that a
packager finder is not used to find additional packages when the module
descriptor encoded in the buffer does not indicate the set of packages.

**Parameters:**
- bb

- The byte buffer

**Returns:**
- The module descriptor

**Throws:**
- InvalidModuleDescriptorException

- If an invalid module descriptor is detected

---

### Additional Sections

#### Class ModuleDescriptor

java.lang.Object

- java.lang.module.ModuleDescriptor

java.lang.module.ModuleDescriptor

**All Implemented Interfaces:** Comparable

<

ModuleDescriptor

>

```java
public class
ModuleDescriptor

extends
Object

implements
Comparable
<
ModuleDescriptor
>
```

A module descriptor.

A module descriptor describes a named module and defines methods to
obtain each of its components. The module descriptor for a named module
in the Java virtual machine is obtained by invoking the

Module

's

getDescriptor

method. Module descriptors can also be created using the

ModuleDescriptor.Builder

class or by reading the binary form of a
module declaration (

module-info.class

) using the

read

methods defined here.

A module descriptor describes a

normal

, open, or automatic
module.

Normal

modules and open modules describe their

dependences

,

exported-packages

, the services
that they

use

or

provide

, and other
components.

Normal

modules may

open

specific
packages. The module descriptor for an open modules does not declare any
open packages (its

opens

method returns an empty set) but when
instantiated in the Java virtual machine then it is treated as if all
packages are open. The module descriptor for an automatic module does not
declare any dependences (except for the mandatory dependency on

java.base

), and does not declare any exported or open packages. Automatic
module receive special treatment during resolution so that they read all
other modules in the configuration. When an automatic module is instantiated
in the Java virtual machine then it reads every unnamed module and is
treated as if all packages are exported and open.

ModuleDescriptor

objects are immutable and safe for use by
multiple concurrent threads.

**Since:** 9
**See Also:** Module

public class

ModuleDescriptor

extends

Object

implements

Comparable

<

ModuleDescriptor

>

A module descriptor.

A module descriptor describes a named module and defines methods to
obtain each of its components. The module descriptor for a named module
in the Java virtual machine is obtained by invoking the

Module

's

getDescriptor

method. Module descriptors can also be created using the

ModuleDescriptor.Builder

class or by reading the binary form of a
module declaration (

module-info.class

) using the

read

methods defined here.

A module descriptor describes a

normal

, open, or automatic
module.

Normal

modules and open modules describe their

dependences

,

exported-packages

, the services
that they

use

or

provide

, and other
components.

Normal

modules may

open

specific
packages. The module descriptor for an open modules does not declare any
open packages (its

opens

method returns an empty set) but when
instantiated in the Java virtual machine then it is treated as if all
packages are open. The module descriptor for an automatic module does not
declare any dependences (except for the mandatory dependency on

java.base

), and does not declare any exported or open packages. Automatic
module receive special treatment during resolution so that they read all
other modules in the configuration. When an automatic module is instantiated
in the Java virtual machine then it reads every unnamed module and is
treated as if all packages are exported and open.

ModuleDescriptor

objects are immutable and safe for use by
multiple concurrent threads.

A module descriptor describes a named module and defines methods to
obtain each of its components. The module descriptor for a named module
in the Java virtual machine is obtained by invoking the

Module

's

getDescriptor

method. Module descriptors can also be created using the

ModuleDescriptor.Builder

class or by reading the binary form of a
module declaration (

module-info.class

) using the

read

methods defined here.

A module descriptor describes a

normal

, open, or automatic
module.

Normal

modules and open modules describe their

dependences

,

exported-packages

, the services
that they

use

or

provide

, and other
components.

Normal

modules may

open

specific
packages. The module descriptor for an open modules does not declare any
open packages (its

opens

method returns an empty set) but when
instantiated in the Java virtual machine then it is treated as if all
packages are open. The module descriptor for an automatic module does not
declare any dependences (except for the mandatory dependency on

java.base

), and does not declare any exported or open packages. Automatic
module receive special treatment during resolution so that they read all
other modules in the configuration. When an automatic module is instantiated
in the Java virtual machine then it reads every unnamed module and is
treated as if all packages are exported and open.

ModuleDescriptor

objects are immutable and safe for use by
multiple concurrent threads.

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

static class

ModuleDescriptor.Builder

A builder for building

ModuleDescriptor

objects.

static class

ModuleDescriptor.Exports

A package exported by a module, may be qualified or unqualified.

static class

ModuleDescriptor.Modifier

A modifier on a module.

static class

ModuleDescriptor.Opens

A package opened by a module, may be qualified or unqualified.

static class

ModuleDescriptor.Provides

A service that a module provides one or more implementations of.

static class

ModuleDescriptor.Requires

A dependence upon a module

static class

ModuleDescriptor.Version

A module's version string.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

int

compareTo

​(

ModuleDescriptor

that)

Compares this module descriptor to another.

boolean

equals

​(

Object

ob)

Tests this module descriptor for equality with the given object.

Set

<

ModuleDescriptor.Exports

>

exports

()

Returns the set of

Exports

objects representing the exported
packages.

int

hashCode

()

Computes a hash code for this module descriptor.

boolean

isAutomatic

()

Returns

true

if this is an automatic module.

boolean

isOpen

()

Returns

true

if this is an open module.

Optional

<

String

>

mainClass

()

Returns the module main class.

Set

<

ModuleDescriptor.Modifier

>

modifiers

()

Returns the set of module modifiers.

String

name

()

Returns the module name.

static

ModuleDescriptor.Builder

newAutomaticModule

​(

String

name)

Instantiates a builder to build a module descriptor for an automatic
module.

static

ModuleDescriptor.Builder

newModule

​(

String

name)

Instantiates a builder to build a module descriptor for a

normal

module.

static

ModuleDescriptor.Builder

newModule

​(

String

name,

Set

<

ModuleDescriptor.Modifier

> ms)

Instantiates a builder to build a module descriptor.

static

ModuleDescriptor.Builder

newOpenModule

​(

String

name)

Instantiates a builder to build a module descriptor for an open module.

Set

<

ModuleDescriptor.Opens

>

opens

()

Returns the set of

Opens

objects representing the open
packages.

Set

<

String

>

packages

()

Returns the set of packages in the module.

Set

<

ModuleDescriptor.Provides

>

provides

()

Returns the set of

Provides

objects representing the
services that the module provides.

Optional

<

String

>

rawVersion

()

Returns the string with the possibly-unparseable version of the
module

static

ModuleDescriptor

read

​(

InputStream

in)

Reads the binary form of a module declaration from an input stream as a
module descriptor.

static

ModuleDescriptor

read

​(

InputStream

in,

Supplier

<

Set

<

String

>> packageFinder)

Reads the binary form of a module declaration from an input stream
as a module descriptor.

static

ModuleDescriptor

read

​(

ByteBuffer

bb)

Reads the binary form of a module declaration from a byte buffer as a
module descriptor.

static

ModuleDescriptor

read

​(

ByteBuffer

bb,

Supplier

<

Set

<

String

>> packageFinder)

Reads the binary form of a module declaration from a byte buffer
as a module descriptor.

Set

<

ModuleDescriptor.Requires

>

requires

()

Returns the set of

Requires

objects representing the module
dependences.

String

toNameAndVersion

()

Returns a string containing the module name and, if present, its
version.

String

toString

()

Returns a string describing the module.

Set

<

String

>

uses

()

Returns the set of service dependences.

Optional

<

ModuleDescriptor.Version

>

version

()

Returns the module version.

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

ModuleDescriptor.Builder

A builder for building

ModuleDescriptor

objects.

static class

ModuleDescriptor.Exports

A package exported by a module, may be qualified or unqualified.

static class

ModuleDescriptor.Modifier

A modifier on a module.

static class

ModuleDescriptor.Opens

A package opened by a module, may be qualified or unqualified.

static class

ModuleDescriptor.Provides

A service that a module provides one or more implementations of.

static class

ModuleDescriptor.Requires

A dependence upon a module

static class

ModuleDescriptor.Version

A module's version string.

---

#### Nested Class Summary

A builder for building

ModuleDescriptor

objects.

A package exported by a module, may be qualified or unqualified.

A modifier on a module.

A package opened by a module, may be qualified or unqualified.

A service that a module provides one or more implementations of.

A dependence upon a module

A module's version string.

Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

int

compareTo

​(

ModuleDescriptor

that)

Compares this module descriptor to another.

boolean

equals

​(

Object

ob)

Tests this module descriptor for equality with the given object.

Set

<

ModuleDescriptor.Exports

>

exports

()

Returns the set of

Exports

objects representing the exported
packages.

int

hashCode

()

Computes a hash code for this module descriptor.

boolean

isAutomatic

()

Returns

true

if this is an automatic module.

boolean

isOpen

()

Returns

true

if this is an open module.

Optional

<

String

>

mainClass

()

Returns the module main class.

Set

<

ModuleDescriptor.Modifier

>

modifiers

()

Returns the set of module modifiers.

String

name

()

Returns the module name.

static

ModuleDescriptor.Builder

newAutomaticModule

​(

String

name)

Instantiates a builder to build a module descriptor for an automatic
module.

static

ModuleDescriptor.Builder

newModule

​(

String

name)

Instantiates a builder to build a module descriptor for a

normal

module.

static

ModuleDescriptor.Builder

newModule

​(

String

name,

Set

<

ModuleDescriptor.Modifier

> ms)

Instantiates a builder to build a module descriptor.

static

ModuleDescriptor.Builder

newOpenModule

​(

String

name)

Instantiates a builder to build a module descriptor for an open module.

Set

<

ModuleDescriptor.Opens

>

opens

()

Returns the set of

Opens

objects representing the open
packages.

Set

<

String

>

packages

()

Returns the set of packages in the module.

Set

<

ModuleDescriptor.Provides

>

provides

()

Returns the set of

Provides

objects representing the
services that the module provides.

Optional

<

String

>

rawVersion

()

Returns the string with the possibly-unparseable version of the
module

static

ModuleDescriptor

read

​(

InputStream

in)

Reads the binary form of a module declaration from an input stream as a
module descriptor.

static

ModuleDescriptor

read

​(

InputStream

in,

Supplier

<

Set

<

String

>> packageFinder)

Reads the binary form of a module declaration from an input stream
as a module descriptor.

static

ModuleDescriptor

read

​(

ByteBuffer

bb)

Reads the binary form of a module declaration from a byte buffer as a
module descriptor.

static

ModuleDescriptor

read

​(

ByteBuffer

bb,

Supplier

<

Set

<

String

>> packageFinder)

Reads the binary form of a module declaration from a byte buffer
as a module descriptor.

Set

<

ModuleDescriptor.Requires

>

requires

()

Returns the set of

Requires

objects representing the module
dependences.

String

toNameAndVersion

()

Returns a string containing the module name and, if present, its
version.

String

toString

()

Returns a string describing the module.

Set

<

String

>

uses

()

Returns the set of service dependences.

Optional

<

ModuleDescriptor.Version

>

version

()

Returns the module version.

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

Compares this module descriptor to another.

Tests this module descriptor for equality with the given object.

Returns the set of

Exports

objects representing the exported
packages.

Computes a hash code for this module descriptor.

Returns

true

if this is an automatic module.

Returns

true

if this is an open module.

Returns the module main class.

Returns the set of module modifiers.

Returns the module name.

Instantiates a builder to build a module descriptor for an automatic
module.

Instantiates a builder to build a module descriptor for a

normal

module.

Instantiates a builder to build a module descriptor.

Instantiates a builder to build a module descriptor for an open module.

Returns the set of

Opens

objects representing the open
packages.

Returns the set of packages in the module.

Returns the set of

Provides

objects representing the
services that the module provides.

Returns the string with the possibly-unparseable version of the
module

Reads the binary form of a module declaration from an input stream as a
module descriptor.

Reads the binary form of a module declaration from an input stream
as a module descriptor.

Reads the binary form of a module declaration from a byte buffer as a
module descriptor.

Reads the binary form of a module declaration from a byte buffer
as a module descriptor.

Returns the set of

Requires

objects representing the module
dependences.

Returns a string containing the module name and, if present, its
version.

Returns a string describing the module.

Returns the set of service dependences.

Returns the module version.

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

- name

```java
public
String
name()
```

Returns the module name.

**Returns:** The module name

- modifiers

```java
public
Set
<
ModuleDescriptor.Modifier
> modifiers()
```

Returns the set of module modifiers.

**Returns:** A possibly-empty unmodifiable set of modifiers

- isOpen

```java
public boolean isOpen()
```

Returns

true

if this is an open module.

This method is equivalent to testing if the set of

modifiers

contains the

OPEN

modifier.

**Returns:** true

if this is an open module

- isAutomatic

```java
public boolean isAutomatic()
```

Returns

true

if this is an automatic module.

This method is equivalent to testing if the set of

modifiers

contains the

AUTOMATIC

modifier.

**Returns:** true

if this is an automatic module

- requires

```java
public
Set
<
ModuleDescriptor.Requires
> requires()
```

Returns the set of

Requires

objects representing the module
dependences.

The set includes a dependency on "

java.base

" when this
module is not named "

java.base

". If this module is an automatic
module then it does not have a dependency on any module other than
"

java.base

".

**Returns:** A possibly-empty unmodifiable set of

ModuleDescriptor.Requires

objects

- exports

```java
public
Set
<
ModuleDescriptor.Exports
> exports()
```

Returns the set of

Exports

objects representing the exported
packages.

If this module is an automatic module then the set of exports
is empty.

**Returns:** A possibly-empty unmodifiable set of exported packages

- opens

```java
public
Set
<
ModuleDescriptor.Opens
> opens()
```

Returns the set of

Opens

objects representing the open
packages.

If this module is an open module or an automatic module then the
set of open packages is empty.

**Returns:** A possibly-empty unmodifiable set of open packages

- uses

```java
public
Set
<
String
> uses()
```

Returns the set of service dependences.

If this module is an automatic module then the set of service
dependences is empty.

**Returns:** A possibly-empty unmodifiable set of the fully qualified class
names of the service types used

- provides

```java
public
Set
<
ModuleDescriptor.Provides
> provides()
```

Returns the set of

Provides

objects representing the
services that the module provides.

**Returns:** The possibly-empty unmodifiable set of the services that this
module provides

- version

```java
public
Optional
<
ModuleDescriptor.Version
> version()
```

Returns the module version.

**Returns:** This module's version, or an empty

Optional

if the
module does not have a version or the version is

unparseable

- rawVersion

```java
public
Optional
<
String
> rawVersion()
```

Returns the string with the possibly-unparseable version of the
module

**Returns:** The string containing the version of the module or an empty

Optional

if the module does not have a version
**See Also:** version()

- toNameAndVersion

```java
public
String
toNameAndVersion()
```

Returns a string containing the module name and, if present, its
version.

**Returns:** A string containing the module name and, if present, its
version

- mainClass

```java
public
Optional
<
String
> mainClass()
```

Returns the module main class.

**Returns:** The fully qualified class name of the module's main class

- packages

```java
public
Set
<
String
> packages()
```

Returns the set of packages in the module.

The set of packages includes all exported and open packages, as well
as the packages of any service providers, and the package for the main
class.

**Returns:** A possibly-empty unmodifiable set of the packages in the module

- compareTo

```java
public int compareTo​(
ModuleDescriptor
that)
```

Compares this module descriptor to another.

Two

ModuleDescriptor

objects are compared by comparing their
module names lexicographically. Where the module names are equal then the
module versions are compared. When comparing the module versions then a
module descriptor with a version is considered to succeed a module
descriptor that does not have a version. If both versions are

unparseable

then the

raw version strings

are compared lexicographically. Where the module names
are equal and the versions are equal (or not present in both), then the
set of modifiers are compared. Sets of modifiers are compared by comparing
a

binary value

computed for each set. If a modifier is present
in the set then the bit at the position of its ordinal is

1

in the binary value, otherwise

0

. If the two set of modifiers
are also equal then the other components of the module descriptors are
compared in a manner that is consistent with

equals

.

**Specified by:** compareTo

in interface

Comparable

<

ModuleDescriptor

>
**Parameters:** that

- The module descriptor to compare
**Returns:** A negative integer, zero, or a positive integer if this module
descriptor is less than, equal to, or greater than the given
module descriptor

- equals

```java
public boolean equals​(
Object
ob)
```

Tests this module descriptor for equality with the given object.

If the given object is not a

ModuleDescriptor

then this
method returns

false

. Two module descriptors are equal if each
of their corresponding components is equal.

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
descriptor that is equal to this module descriptor
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
public int hashCode()
```

Computes a hash code for this module descriptor.

The hash code is based upon the components of the module descriptor,
and satisfies the general contract of the

Object.hashCode

method.

**Overrides:** hashCode

in class

Object
**Returns:** The hash-code value for this module descriptor
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

- toString

```java
public
String
toString()
```

Returns a string describing the module.

**Overrides:** toString

in class

Object
**Returns:** A string describing the module

- newModule

```java
public static
ModuleDescriptor.Builder
newModule​(
String
name,

Set
<
ModuleDescriptor.Modifier
> ms)
```

Instantiates a builder to build a module descriptor.

**Parameters:** name

- The module name
**Parameters:** ms

- The set of module modifiers
**Returns:** A new builder
**Throws:** IllegalArgumentException

- If the module name is

null

or is not a legal module
name, or the set of modifiers contains

AUTOMATIC

with other modifiers

- newModule

```java
public static
ModuleDescriptor.Builder
newModule​(
String
name)
```

Instantiates a builder to build a module descriptor for a

normal

module. This method is equivalent to invoking

newModule

with an empty set of

modifiers

.

**Parameters:** name

- The module name
**Returns:** A new builder
**Throws:** IllegalArgumentException

- If the module name is

null

or is not a legal module
name

- newOpenModule

```java
public static
ModuleDescriptor.Builder
newOpenModule​(
String
name)
```

Instantiates a builder to build a module descriptor for an open module.
This method is equivalent to invoking

newModule

with the

OPEN

modifier.

The builder for an open module cannot be used to declare any open
packages.

**Parameters:** name

- The module name
**Returns:** A new builder that builds an open module
**Throws:** IllegalArgumentException

- If the module name is

null

or is not a legal module
name

- newAutomaticModule

```java
public static
ModuleDescriptor.Builder
newAutomaticModule​(
String
name)
```

Instantiates a builder to build a module descriptor for an automatic
module. This method is equivalent to invoking

newModule

with the

AUTOMATIC

modifier.

The builder for an automatic module cannot be used to declare module
or service dependences. It also cannot be used to declare any exported
or open packages.

**Parameters:** name

- The module name
**Returns:** A new builder that builds an automatic module
**Throws:** IllegalArgumentException

- If the module name is

null

or is not a legal module
name
**See Also:** ModuleFinder.of(Path[])

- read

```java
public static
ModuleDescriptor
read​(
InputStream
in,

Supplier
<
Set
<
String
>> packageFinder)
throws
IOException
```

Reads the binary form of a module declaration from an input stream
as a module descriptor.

If the descriptor encoded in the input stream does not indicate a
set of packages in the module then the

packageFinder

will be
invoked. The set of packages that the

packageFinder

returns
must include all the packages that the module exports, opens, as well
as the packages of the service implementations that the module provides,
and the package of the main class (if the module has a main class). If
the

packageFinder

throws an

UncheckedIOException

then

IOException

cause will be re-thrown.

If there are bytes following the module descriptor then it is
implementation specific as to whether those bytes are read, ignored,
or reported as an

InvalidModuleDescriptorException

. If this
method fails with an

InvalidModuleDescriptorException

or

IOException

then it may do so after some, but not all, bytes have
been read from the input stream. It is strongly recommended that the
stream be promptly closed and discarded if an exception occurs.

**API Note:** The

packageFinder

parameter is for use when reading
module descriptors from legacy module-artifact formats that do not
record the set of packages in the descriptor itself.
**Parameters:** in

- The input stream
**Parameters:** packageFinder

- A supplier that can produce the set of packages
**Returns:** The module descriptor
**Throws:** InvalidModuleDescriptorException

- If an invalid module descriptor is detected or the set of
packages returned by the

packageFinder

does not include
all of the packages obtained from the module descriptor
**Throws:** IOException

- If an I/O error occurs reading from the input stream or

UncheckedIOException

is thrown by the package finder

- read

```java
public static
ModuleDescriptor
read​(
InputStream
in)
throws
IOException
```

Reads the binary form of a module declaration from an input stream as a
module descriptor. This method works exactly as specified by the 2-arg

read

method with the exception that
a packager finder is not used to find additional packages when the
module descriptor read from the stream does not indicate the set of
packages.

**Parameters:** in

- The input stream
**Returns:** The module descriptor
**Throws:** InvalidModuleDescriptorException

- If an invalid module descriptor is detected
**Throws:** IOException

- If an I/O error occurs reading from the input stream

- read

```java
public static
ModuleDescriptor
read​(
ByteBuffer
bb,

Supplier
<
Set
<
String
>> packageFinder)
```

Reads the binary form of a module declaration from a byte buffer
as a module descriptor.

If the descriptor encoded in the byte buffer does not indicate a
set of packages in the module then the

packageFinder

will be
invoked. The set of packages that the

packageFinder

returns
must include all the packages that the module exports, opens, as well
as the packages of the service implementations that the module provides,
and the package of the main class (if the module has a main class). If
the

packageFinder

throws an

UncheckedIOException

then

IOException

cause will be re-thrown.

The module descriptor is read from the buffer starting at index

p

, where

p

is the buffer's

position

when this method is invoked. Upon return the buffer's position
will be equal to

p + n

where

n

is the number of bytes
read from the buffer.

If there are bytes following the module descriptor then it is
implementation specific as to whether those bytes are read, ignored,
or reported as an

InvalidModuleDescriptorException

. If this
method fails with an

InvalidModuleDescriptorException

then it
may do so after some, but not all, bytes have been read.

**API Note:** The

packageFinder

parameter is for use when reading
module descriptors from legacy module-artifact formats that do not
record the set of packages in the descriptor itself.
**Parameters:** bb

- The byte buffer
**Parameters:** packageFinder

- A supplier that can produce the set of packages
**Returns:** The module descriptor
**Throws:** InvalidModuleDescriptorException

- If an invalid module descriptor is detected or the set of
packages returned by the

packageFinder

does not include
all of the packages obtained from the module descriptor

- read

```java
public static
ModuleDescriptor
read​(
ByteBuffer
bb)
```

Reads the binary form of a module declaration from a byte buffer as a
module descriptor. This method works exactly as specified by the 2-arg

read

method with the exception that a
packager finder is not used to find additional packages when the module
descriptor encoded in the buffer does not indicate the set of packages.

**Parameters:** bb

- The byte buffer
**Returns:** The module descriptor
**Throws:** InvalidModuleDescriptorException

- If an invalid module descriptor is detected

Method Detail

- name

```java
public
String
name()
```

Returns the module name.

**Returns:** The module name

- modifiers

```java
public
Set
<
ModuleDescriptor.Modifier
> modifiers()
```

Returns the set of module modifiers.

**Returns:** A possibly-empty unmodifiable set of modifiers

- isOpen

```java
public boolean isOpen()
```

Returns

true

if this is an open module.

This method is equivalent to testing if the set of

modifiers

contains the

OPEN

modifier.

**Returns:** true

if this is an open module

- isAutomatic

```java
public boolean isAutomatic()
```

Returns

true

if this is an automatic module.

This method is equivalent to testing if the set of

modifiers

contains the

AUTOMATIC

modifier.

**Returns:** true

if this is an automatic module

- requires

```java
public
Set
<
ModuleDescriptor.Requires
> requires()
```

Returns the set of

Requires

objects representing the module
dependences.

The set includes a dependency on "

java.base

" when this
module is not named "

java.base

". If this module is an automatic
module then it does not have a dependency on any module other than
"

java.base

".

**Returns:** A possibly-empty unmodifiable set of

ModuleDescriptor.Requires

objects

- exports

```java
public
Set
<
ModuleDescriptor.Exports
> exports()
```

Returns the set of

Exports

objects representing the exported
packages.

If this module is an automatic module then the set of exports
is empty.

**Returns:** A possibly-empty unmodifiable set of exported packages

- opens

```java
public
Set
<
ModuleDescriptor.Opens
> opens()
```

Returns the set of

Opens

objects representing the open
packages.

If this module is an open module or an automatic module then the
set of open packages is empty.

**Returns:** A possibly-empty unmodifiable set of open packages

- uses

```java
public
Set
<
String
> uses()
```

Returns the set of service dependences.

If this module is an automatic module then the set of service
dependences is empty.

**Returns:** A possibly-empty unmodifiable set of the fully qualified class
names of the service types used

- provides

```java
public
Set
<
ModuleDescriptor.Provides
> provides()
```

Returns the set of

Provides

objects representing the
services that the module provides.

**Returns:** The possibly-empty unmodifiable set of the services that this
module provides

- version

```java
public
Optional
<
ModuleDescriptor.Version
> version()
```

Returns the module version.

**Returns:** This module's version, or an empty

Optional

if the
module does not have a version or the version is

unparseable

- rawVersion

```java
public
Optional
<
String
> rawVersion()
```

Returns the string with the possibly-unparseable version of the
module

**Returns:** The string containing the version of the module or an empty

Optional

if the module does not have a version
**See Also:** version()

- toNameAndVersion

```java
public
String
toNameAndVersion()
```

Returns a string containing the module name and, if present, its
version.

**Returns:** A string containing the module name and, if present, its
version

- mainClass

```java
public
Optional
<
String
> mainClass()
```

Returns the module main class.

**Returns:** The fully qualified class name of the module's main class

- packages

```java
public
Set
<
String
> packages()
```

Returns the set of packages in the module.

The set of packages includes all exported and open packages, as well
as the packages of any service providers, and the package for the main
class.

**Returns:** A possibly-empty unmodifiable set of the packages in the module

- compareTo

```java
public int compareTo​(
ModuleDescriptor
that)
```

Compares this module descriptor to another.

Two

ModuleDescriptor

objects are compared by comparing their
module names lexicographically. Where the module names are equal then the
module versions are compared. When comparing the module versions then a
module descriptor with a version is considered to succeed a module
descriptor that does not have a version. If both versions are

unparseable

then the

raw version strings

are compared lexicographically. Where the module names
are equal and the versions are equal (or not present in both), then the
set of modifiers are compared. Sets of modifiers are compared by comparing
a

binary value

computed for each set. If a modifier is present
in the set then the bit at the position of its ordinal is

1

in the binary value, otherwise

0

. If the two set of modifiers
are also equal then the other components of the module descriptors are
compared in a manner that is consistent with

equals

.

**Specified by:** compareTo

in interface

Comparable

<

ModuleDescriptor

>
**Parameters:** that

- The module descriptor to compare
**Returns:** A negative integer, zero, or a positive integer if this module
descriptor is less than, equal to, or greater than the given
module descriptor

- equals

```java
public boolean equals​(
Object
ob)
```

Tests this module descriptor for equality with the given object.

If the given object is not a

ModuleDescriptor

then this
method returns

false

. Two module descriptors are equal if each
of their corresponding components is equal.

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
descriptor that is equal to this module descriptor
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
public int hashCode()
```

Computes a hash code for this module descriptor.

The hash code is based upon the components of the module descriptor,
and satisfies the general contract of the

Object.hashCode

method.

**Overrides:** hashCode

in class

Object
**Returns:** The hash-code value for this module descriptor
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

- toString

```java
public
String
toString()
```

Returns a string describing the module.

**Overrides:** toString

in class

Object
**Returns:** A string describing the module

- newModule

```java
public static
ModuleDescriptor.Builder
newModule​(
String
name,

Set
<
ModuleDescriptor.Modifier
> ms)
```

Instantiates a builder to build a module descriptor.

**Parameters:** name

- The module name
**Parameters:** ms

- The set of module modifiers
**Returns:** A new builder
**Throws:** IllegalArgumentException

- If the module name is

null

or is not a legal module
name, or the set of modifiers contains

AUTOMATIC

with other modifiers

- newModule

```java
public static
ModuleDescriptor.Builder
newModule​(
String
name)
```

Instantiates a builder to build a module descriptor for a

normal

module. This method is equivalent to invoking

newModule

with an empty set of

modifiers

.

**Parameters:** name

- The module name
**Returns:** A new builder
**Throws:** IllegalArgumentException

- If the module name is

null

or is not a legal module
name

- newOpenModule

```java
public static
ModuleDescriptor.Builder
newOpenModule​(
String
name)
```

Instantiates a builder to build a module descriptor for an open module.
This method is equivalent to invoking

newModule

with the

OPEN

modifier.

The builder for an open module cannot be used to declare any open
packages.

**Parameters:** name

- The module name
**Returns:** A new builder that builds an open module
**Throws:** IllegalArgumentException

- If the module name is

null

or is not a legal module
name

- newAutomaticModule

```java
public static
ModuleDescriptor.Builder
newAutomaticModule​(
String
name)
```

Instantiates a builder to build a module descriptor for an automatic
module. This method is equivalent to invoking

newModule

with the

AUTOMATIC

modifier.

The builder for an automatic module cannot be used to declare module
or service dependences. It also cannot be used to declare any exported
or open packages.

**Parameters:** name

- The module name
**Returns:** A new builder that builds an automatic module
**Throws:** IllegalArgumentException

- If the module name is

null

or is not a legal module
name
**See Also:** ModuleFinder.of(Path[])

- read

```java
public static
ModuleDescriptor
read​(
InputStream
in,

Supplier
<
Set
<
String
>> packageFinder)
throws
IOException
```

Reads the binary form of a module declaration from an input stream
as a module descriptor.

If the descriptor encoded in the input stream does not indicate a
set of packages in the module then the

packageFinder

will be
invoked. The set of packages that the

packageFinder

returns
must include all the packages that the module exports, opens, as well
as the packages of the service implementations that the module provides,
and the package of the main class (if the module has a main class). If
the

packageFinder

throws an

UncheckedIOException

then

IOException

cause will be re-thrown.

If there are bytes following the module descriptor then it is
implementation specific as to whether those bytes are read, ignored,
or reported as an

InvalidModuleDescriptorException

. If this
method fails with an

InvalidModuleDescriptorException

or

IOException

then it may do so after some, but not all, bytes have
been read from the input stream. It is strongly recommended that the
stream be promptly closed and discarded if an exception occurs.

**API Note:** The

packageFinder

parameter is for use when reading
module descriptors from legacy module-artifact formats that do not
record the set of packages in the descriptor itself.
**Parameters:** in

- The input stream
**Parameters:** packageFinder

- A supplier that can produce the set of packages
**Returns:** The module descriptor
**Throws:** InvalidModuleDescriptorException

- If an invalid module descriptor is detected or the set of
packages returned by the

packageFinder

does not include
all of the packages obtained from the module descriptor
**Throws:** IOException

- If an I/O error occurs reading from the input stream or

UncheckedIOException

is thrown by the package finder

- read

```java
public static
ModuleDescriptor
read​(
InputStream
in)
throws
IOException
```

Reads the binary form of a module declaration from an input stream as a
module descriptor. This method works exactly as specified by the 2-arg

read

method with the exception that
a packager finder is not used to find additional packages when the
module descriptor read from the stream does not indicate the set of
packages.

**Parameters:** in

- The input stream
**Returns:** The module descriptor
**Throws:** InvalidModuleDescriptorException

- If an invalid module descriptor is detected
**Throws:** IOException

- If an I/O error occurs reading from the input stream

- read

```java
public static
ModuleDescriptor
read​(
ByteBuffer
bb,

Supplier
<
Set
<
String
>> packageFinder)
```

Reads the binary form of a module declaration from a byte buffer
as a module descriptor.

If the descriptor encoded in the byte buffer does not indicate a
set of packages in the module then the

packageFinder

will be
invoked. The set of packages that the

packageFinder

returns
must include all the packages that the module exports, opens, as well
as the packages of the service implementations that the module provides,
and the package of the main class (if the module has a main class). If
the

packageFinder

throws an

UncheckedIOException

then

IOException

cause will be re-thrown.

The module descriptor is read from the buffer starting at index

p

, where

p

is the buffer's

position

when this method is invoked. Upon return the buffer's position
will be equal to

p + n

where

n

is the number of bytes
read from the buffer.

If there are bytes following the module descriptor then it is
implementation specific as to whether those bytes are read, ignored,
or reported as an

InvalidModuleDescriptorException

. If this
method fails with an

InvalidModuleDescriptorException

then it
may do so after some, but not all, bytes have been read.

**API Note:** The

packageFinder

parameter is for use when reading
module descriptors from legacy module-artifact formats that do not
record the set of packages in the descriptor itself.
**Parameters:** bb

- The byte buffer
**Parameters:** packageFinder

- A supplier that can produce the set of packages
**Returns:** The module descriptor
**Throws:** InvalidModuleDescriptorException

- If an invalid module descriptor is detected or the set of
packages returned by the

packageFinder

does not include
all of the packages obtained from the module descriptor

- read

```java
public static
ModuleDescriptor
read​(
ByteBuffer
bb)
```

Reads the binary form of a module declaration from a byte buffer as a
module descriptor. This method works exactly as specified by the 2-arg

read

method with the exception that a
packager finder is not used to find additional packages when the module
descriptor encoded in the buffer does not indicate the set of packages.

**Parameters:** bb

- The byte buffer
**Returns:** The module descriptor
**Throws:** InvalidModuleDescriptorException

- If an invalid module descriptor is detected

---

#### Method Detail

name

```java
public
String
name()
```

Returns the module name.

**Returns:** The module name

---

#### name

public

String

name()

Returns the module name.

modifiers

```java
public
Set
<
ModuleDescriptor.Modifier
> modifiers()
```

Returns the set of module modifiers.

**Returns:** A possibly-empty unmodifiable set of modifiers

---

#### modifiers

public

Set

<

ModuleDescriptor.Modifier

> modifiers()

Returns the set of module modifiers.

isOpen

```java
public boolean isOpen()
```

Returns

true

if this is an open module.

This method is equivalent to testing if the set of

modifiers

contains the

OPEN

modifier.

**Returns:** true

if this is an open module

---

#### isOpen

public boolean isOpen()

Returns

true

if this is an open module.

This method is equivalent to testing if the set of

modifiers

contains the

OPEN

modifier.

Returns

true

if this is an open module.

This method is equivalent to testing if the set of

modifiers

contains the

OPEN

modifier.

isAutomatic

```java
public boolean isAutomatic()
```

Returns

true

if this is an automatic module.

This method is equivalent to testing if the set of

modifiers

contains the

AUTOMATIC

modifier.

**Returns:** true

if this is an automatic module

---

#### isAutomatic

public boolean isAutomatic()

Returns

true

if this is an automatic module.

This method is equivalent to testing if the set of

modifiers

contains the

AUTOMATIC

modifier.

Returns

true

if this is an automatic module.

This method is equivalent to testing if the set of

modifiers

contains the

AUTOMATIC

modifier.

requires

```java
public
Set
<
ModuleDescriptor.Requires
> requires()
```

Returns the set of

Requires

objects representing the module
dependences.

The set includes a dependency on "

java.base

" when this
module is not named "

java.base

". If this module is an automatic
module then it does not have a dependency on any module other than
"

java.base

".

**Returns:** A possibly-empty unmodifiable set of

ModuleDescriptor.Requires

objects

---

#### requires

public

Set

<

ModuleDescriptor.Requires

> requires()

Returns the set of

Requires

objects representing the module
dependences.

The set includes a dependency on "

java.base

" when this
module is not named "

java.base

". If this module is an automatic
module then it does not have a dependency on any module other than
"

java.base

".

Returns the set of

Requires

objects representing the module
dependences.

The set includes a dependency on "

java.base

" when this
module is not named "

java.base

". If this module is an automatic
module then it does not have a dependency on any module other than
"

java.base

".

exports

```java
public
Set
<
ModuleDescriptor.Exports
> exports()
```

Returns the set of

Exports

objects representing the exported
packages.

If this module is an automatic module then the set of exports
is empty.

**Returns:** A possibly-empty unmodifiable set of exported packages

---

#### exports

public

Set

<

ModuleDescriptor.Exports

> exports()

Returns the set of

Exports

objects representing the exported
packages.

If this module is an automatic module then the set of exports
is empty.

Returns the set of

Exports

objects representing the exported
packages.

If this module is an automatic module then the set of exports
is empty.

opens

```java
public
Set
<
ModuleDescriptor.Opens
> opens()
```

Returns the set of

Opens

objects representing the open
packages.

If this module is an open module or an automatic module then the
set of open packages is empty.

**Returns:** A possibly-empty unmodifiable set of open packages

---

#### opens

public

Set

<

ModuleDescriptor.Opens

> opens()

Returns the set of

Opens

objects representing the open
packages.

If this module is an open module or an automatic module then the
set of open packages is empty.

Returns the set of

Opens

objects representing the open
packages.

If this module is an open module or an automatic module then the
set of open packages is empty.

uses

```java
public
Set
<
String
> uses()
```

Returns the set of service dependences.

If this module is an automatic module then the set of service
dependences is empty.

**Returns:** A possibly-empty unmodifiable set of the fully qualified class
names of the service types used

---

#### uses

public

Set

<

String

> uses()

Returns the set of service dependences.

If this module is an automatic module then the set of service
dependences is empty.

Returns the set of service dependences.

If this module is an automatic module then the set of service
dependences is empty.

provides

```java
public
Set
<
ModuleDescriptor.Provides
> provides()
```

Returns the set of

Provides

objects representing the
services that the module provides.

**Returns:** The possibly-empty unmodifiable set of the services that this
module provides

---

#### provides

public

Set

<

ModuleDescriptor.Provides

> provides()

Returns the set of

Provides

objects representing the
services that the module provides.

version

```java
public
Optional
<
ModuleDescriptor.Version
> version()
```

Returns the module version.

**Returns:** This module's version, or an empty

Optional

if the
module does not have a version or the version is

unparseable

---

#### version

public

Optional

<

ModuleDescriptor.Version

> version()

Returns the module version.

rawVersion

```java
public
Optional
<
String
> rawVersion()
```

Returns the string with the possibly-unparseable version of the
module

**Returns:** The string containing the version of the module or an empty

Optional

if the module does not have a version
**See Also:** version()

---

#### rawVersion

public

Optional

<

String

> rawVersion()

Returns the string with the possibly-unparseable version of the
module

toNameAndVersion

```java
public
String
toNameAndVersion()
```

Returns a string containing the module name and, if present, its
version.

**Returns:** A string containing the module name and, if present, its
version

---

#### toNameAndVersion

public

String

toNameAndVersion()

Returns a string containing the module name and, if present, its
version.

mainClass

```java
public
Optional
<
String
> mainClass()
```

Returns the module main class.

**Returns:** The fully qualified class name of the module's main class

---

#### mainClass

public

Optional

<

String

> mainClass()

Returns the module main class.

packages

```java
public
Set
<
String
> packages()
```

Returns the set of packages in the module.

The set of packages includes all exported and open packages, as well
as the packages of any service providers, and the package for the main
class.

**Returns:** A possibly-empty unmodifiable set of the packages in the module

---

#### packages

public

Set

<

String

> packages()

Returns the set of packages in the module.

The set of packages includes all exported and open packages, as well
as the packages of any service providers, and the package for the main
class.

The set of packages includes all exported and open packages, as well
as the packages of any service providers, and the package for the main
class.

compareTo

```java
public int compareTo​(
ModuleDescriptor
that)
```

Compares this module descriptor to another.

Two

ModuleDescriptor

objects are compared by comparing their
module names lexicographically. Where the module names are equal then the
module versions are compared. When comparing the module versions then a
module descriptor with a version is considered to succeed a module
descriptor that does not have a version. If both versions are

unparseable

then the

raw version strings

are compared lexicographically. Where the module names
are equal and the versions are equal (or not present in both), then the
set of modifiers are compared. Sets of modifiers are compared by comparing
a

binary value

computed for each set. If a modifier is present
in the set then the bit at the position of its ordinal is

1

in the binary value, otherwise

0

. If the two set of modifiers
are also equal then the other components of the module descriptors are
compared in a manner that is consistent with

equals

.

**Specified by:** compareTo

in interface

Comparable

<

ModuleDescriptor

>
**Parameters:** that

- The module descriptor to compare
**Returns:** A negative integer, zero, or a positive integer if this module
descriptor is less than, equal to, or greater than the given
module descriptor

---

#### compareTo

public int compareTo​(

ModuleDescriptor

that)

Compares this module descriptor to another.

Two

ModuleDescriptor

objects are compared by comparing their
module names lexicographically. Where the module names are equal then the
module versions are compared. When comparing the module versions then a
module descriptor with a version is considered to succeed a module
descriptor that does not have a version. If both versions are

unparseable

then the

raw version strings

are compared lexicographically. Where the module names
are equal and the versions are equal (or not present in both), then the
set of modifiers are compared. Sets of modifiers are compared by comparing
a

binary value

computed for each set. If a modifier is present
in the set then the bit at the position of its ordinal is

1

in the binary value, otherwise

0

. If the two set of modifiers
are also equal then the other components of the module descriptors are
compared in a manner that is consistent with

equals

.

Two

ModuleDescriptor

objects are compared by comparing their
module names lexicographically. Where the module names are equal then the
module versions are compared. When comparing the module versions then a
module descriptor with a version is considered to succeed a module
descriptor that does not have a version. If both versions are

unparseable

then the

raw version strings

are compared lexicographically. Where the module names
are equal and the versions are equal (or not present in both), then the
set of modifiers are compared. Sets of modifiers are compared by comparing
a

binary value

computed for each set. If a modifier is present
in the set then the bit at the position of its ordinal is

1

in the binary value, otherwise

0

. If the two set of modifiers
are also equal then the other components of the module descriptors are
compared in a manner that is consistent with

equals

.

equals

```java
public boolean equals​(
Object
ob)
```

Tests this module descriptor for equality with the given object.

If the given object is not a

ModuleDescriptor

then this
method returns

false

. Two module descriptors are equal if each
of their corresponding components is equal.

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
descriptor that is equal to this module descriptor
**See Also:** Object.hashCode()

,

HashMap

---

#### equals

public boolean equals​(

Object

ob)

Tests this module descriptor for equality with the given object.

If the given object is not a

ModuleDescriptor

then this
method returns

false

. Two module descriptors are equal if each
of their corresponding components is equal.

This method satisfies the general contract of the

Object.equals

method.

If the given object is not a

ModuleDescriptor

then this
method returns

false

. Two module descriptors are equal if each
of their corresponding components is equal.

This method satisfies the general contract of the

Object.equals

method.

hashCode

```java
public int hashCode()
```

Computes a hash code for this module descriptor.

The hash code is based upon the components of the module descriptor,
and satisfies the general contract of the

Object.hashCode

method.

**Overrides:** hashCode

in class

Object
**Returns:** The hash-code value for this module descriptor
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### hashCode

public int hashCode()

Computes a hash code for this module descriptor.

The hash code is based upon the components of the module descriptor,
and satisfies the general contract of the

Object.hashCode

method.

The hash code is based upon the components of the module descriptor,
and satisfies the general contract of the

Object.hashCode

method.

toString

```java
public
String
toString()
```

Returns a string describing the module.

**Overrides:** toString

in class

Object
**Returns:** A string describing the module

---

#### toString

public

String

toString()

Returns a string describing the module.

newModule

```java
public static
ModuleDescriptor.Builder
newModule​(
String
name,

Set
<
ModuleDescriptor.Modifier
> ms)
```

Instantiates a builder to build a module descriptor.

**Parameters:** name

- The module name
**Parameters:** ms

- The set of module modifiers
**Returns:** A new builder
**Throws:** IllegalArgumentException

- If the module name is

null

or is not a legal module
name, or the set of modifiers contains

AUTOMATIC

with other modifiers

---

#### newModule

public static

ModuleDescriptor.Builder

newModule​(

String

name,

Set

<

ModuleDescriptor.Modifier

> ms)

Instantiates a builder to build a module descriptor.

newModule

```java
public static
ModuleDescriptor.Builder
newModule​(
String
name)
```

Instantiates a builder to build a module descriptor for a

normal

module. This method is equivalent to invoking

newModule

with an empty set of

modifiers

.

**Parameters:** name

- The module name
**Returns:** A new builder
**Throws:** IllegalArgumentException

- If the module name is

null

or is not a legal module
name

---

#### newModule

public static

ModuleDescriptor.Builder

newModule​(

String

name)

Instantiates a builder to build a module descriptor for a

normal

module. This method is equivalent to invoking

newModule

with an empty set of

modifiers

.

newOpenModule

```java
public static
ModuleDescriptor.Builder
newOpenModule​(
String
name)
```

Instantiates a builder to build a module descriptor for an open module.
This method is equivalent to invoking

newModule

with the

OPEN

modifier.

The builder for an open module cannot be used to declare any open
packages.

**Parameters:** name

- The module name
**Returns:** A new builder that builds an open module
**Throws:** IllegalArgumentException

- If the module name is

null

or is not a legal module
name

---

#### newOpenModule

public static

ModuleDescriptor.Builder

newOpenModule​(

String

name)

Instantiates a builder to build a module descriptor for an open module.
This method is equivalent to invoking

newModule

with the

OPEN

modifier.

The builder for an open module cannot be used to declare any open
packages.

The builder for an open module cannot be used to declare any open
packages.

newAutomaticModule

```java
public static
ModuleDescriptor.Builder
newAutomaticModule​(
String
name)
```

Instantiates a builder to build a module descriptor for an automatic
module. This method is equivalent to invoking

newModule

with the

AUTOMATIC

modifier.

The builder for an automatic module cannot be used to declare module
or service dependences. It also cannot be used to declare any exported
or open packages.

**Parameters:** name

- The module name
**Returns:** A new builder that builds an automatic module
**Throws:** IllegalArgumentException

- If the module name is

null

or is not a legal module
name
**See Also:** ModuleFinder.of(Path[])

---

#### newAutomaticModule

public static

ModuleDescriptor.Builder

newAutomaticModule​(

String

name)

Instantiates a builder to build a module descriptor for an automatic
module. This method is equivalent to invoking

newModule

with the

AUTOMATIC

modifier.

The builder for an automatic module cannot be used to declare module
or service dependences. It also cannot be used to declare any exported
or open packages.

The builder for an automatic module cannot be used to declare module
or service dependences. It also cannot be used to declare any exported
or open packages.

read

```java
public static
ModuleDescriptor
read​(
InputStream
in,

Supplier
<
Set
<
String
>> packageFinder)
throws
IOException
```

Reads the binary form of a module declaration from an input stream
as a module descriptor.

If the descriptor encoded in the input stream does not indicate a
set of packages in the module then the

packageFinder

will be
invoked. The set of packages that the

packageFinder

returns
must include all the packages that the module exports, opens, as well
as the packages of the service implementations that the module provides,
and the package of the main class (if the module has a main class). If
the

packageFinder

throws an

UncheckedIOException

then

IOException

cause will be re-thrown.

If there are bytes following the module descriptor then it is
implementation specific as to whether those bytes are read, ignored,
or reported as an

InvalidModuleDescriptorException

. If this
method fails with an

InvalidModuleDescriptorException

or

IOException

then it may do so after some, but not all, bytes have
been read from the input stream. It is strongly recommended that the
stream be promptly closed and discarded if an exception occurs.

**API Note:** The

packageFinder

parameter is for use when reading
module descriptors from legacy module-artifact formats that do not
record the set of packages in the descriptor itself.
**Parameters:** in

- The input stream
**Parameters:** packageFinder

- A supplier that can produce the set of packages
**Returns:** The module descriptor
**Throws:** InvalidModuleDescriptorException

- If an invalid module descriptor is detected or the set of
packages returned by the

packageFinder

does not include
all of the packages obtained from the module descriptor
**Throws:** IOException

- If an I/O error occurs reading from the input stream or

UncheckedIOException

is thrown by the package finder

---

#### read

public static

ModuleDescriptor

read​(

InputStream

in,

Supplier

<

Set

<

String

>> packageFinder)
throws

IOException

Reads the binary form of a module declaration from an input stream
as a module descriptor.

If the descriptor encoded in the input stream does not indicate a
set of packages in the module then the

packageFinder

will be
invoked. The set of packages that the

packageFinder

returns
must include all the packages that the module exports, opens, as well
as the packages of the service implementations that the module provides,
and the package of the main class (if the module has a main class). If
the

packageFinder

throws an

UncheckedIOException

then

IOException

cause will be re-thrown.

If there are bytes following the module descriptor then it is
implementation specific as to whether those bytes are read, ignored,
or reported as an

InvalidModuleDescriptorException

. If this
method fails with an

InvalidModuleDescriptorException

or

IOException

then it may do so after some, but not all, bytes have
been read from the input stream. It is strongly recommended that the
stream be promptly closed and discarded if an exception occurs.

If the descriptor encoded in the input stream does not indicate a
set of packages in the module then the

packageFinder

will be
invoked. The set of packages that the

packageFinder

returns
must include all the packages that the module exports, opens, as well
as the packages of the service implementations that the module provides,
and the package of the main class (if the module has a main class). If
the

packageFinder

throws an

UncheckedIOException

then

IOException

cause will be re-thrown.

If there are bytes following the module descriptor then it is
implementation specific as to whether those bytes are read, ignored,
or reported as an

InvalidModuleDescriptorException

. If this
method fails with an

InvalidModuleDescriptorException

or

IOException

then it may do so after some, but not all, bytes have
been read from the input stream. It is strongly recommended that the
stream be promptly closed and discarded if an exception occurs.

read

```java
public static
ModuleDescriptor
read​(
InputStream
in)
throws
IOException
```

Reads the binary form of a module declaration from an input stream as a
module descriptor. This method works exactly as specified by the 2-arg

read

method with the exception that
a packager finder is not used to find additional packages when the
module descriptor read from the stream does not indicate the set of
packages.

**Parameters:** in

- The input stream
**Returns:** The module descriptor
**Throws:** InvalidModuleDescriptorException

- If an invalid module descriptor is detected
**Throws:** IOException

- If an I/O error occurs reading from the input stream

---

#### read

public static

ModuleDescriptor

read​(

InputStream

in)
throws

IOException

Reads the binary form of a module declaration from an input stream as a
module descriptor. This method works exactly as specified by the 2-arg

read

method with the exception that
a packager finder is not used to find additional packages when the
module descriptor read from the stream does not indicate the set of
packages.

read

```java
public static
ModuleDescriptor
read​(
ByteBuffer
bb,

Supplier
<
Set
<
String
>> packageFinder)
```

Reads the binary form of a module declaration from a byte buffer
as a module descriptor.

If the descriptor encoded in the byte buffer does not indicate a
set of packages in the module then the

packageFinder

will be
invoked. The set of packages that the

packageFinder

returns
must include all the packages that the module exports, opens, as well
as the packages of the service implementations that the module provides,
and the package of the main class (if the module has a main class). If
the

packageFinder

throws an

UncheckedIOException

then

IOException

cause will be re-thrown.

The module descriptor is read from the buffer starting at index

p

, where

p

is the buffer's

position

when this method is invoked. Upon return the buffer's position
will be equal to

p + n

where

n

is the number of bytes
read from the buffer.

If there are bytes following the module descriptor then it is
implementation specific as to whether those bytes are read, ignored,
or reported as an

InvalidModuleDescriptorException

. If this
method fails with an

InvalidModuleDescriptorException

then it
may do so after some, but not all, bytes have been read.

**API Note:** The

packageFinder

parameter is for use when reading
module descriptors from legacy module-artifact formats that do not
record the set of packages in the descriptor itself.
**Parameters:** bb

- The byte buffer
**Parameters:** packageFinder

- A supplier that can produce the set of packages
**Returns:** The module descriptor
**Throws:** InvalidModuleDescriptorException

- If an invalid module descriptor is detected or the set of
packages returned by the

packageFinder

does not include
all of the packages obtained from the module descriptor

---

#### read

public static

ModuleDescriptor

read​(

ByteBuffer

bb,

Supplier

<

Set

<

String

>> packageFinder)

Reads the binary form of a module declaration from a byte buffer
as a module descriptor.

If the descriptor encoded in the byte buffer does not indicate a
set of packages in the module then the

packageFinder

will be
invoked. The set of packages that the

packageFinder

returns
must include all the packages that the module exports, opens, as well
as the packages of the service implementations that the module provides,
and the package of the main class (if the module has a main class). If
the

packageFinder

throws an

UncheckedIOException

then

IOException

cause will be re-thrown.

The module descriptor is read from the buffer starting at index

p

, where

p

is the buffer's

position

when this method is invoked. Upon return the buffer's position
will be equal to

p + n

where

n

is the number of bytes
read from the buffer.

If there are bytes following the module descriptor then it is
implementation specific as to whether those bytes are read, ignored,
or reported as an

InvalidModuleDescriptorException

. If this
method fails with an

InvalidModuleDescriptorException

then it
may do so after some, but not all, bytes have been read.

If the descriptor encoded in the byte buffer does not indicate a
set of packages in the module then the

packageFinder

will be
invoked. The set of packages that the

packageFinder

returns
must include all the packages that the module exports, opens, as well
as the packages of the service implementations that the module provides,
and the package of the main class (if the module has a main class). If
the

packageFinder

throws an

UncheckedIOException

then

IOException

cause will be re-thrown.

The module descriptor is read from the buffer starting at index

p

, where

p

is the buffer's

position

when this method is invoked. Upon return the buffer's position
will be equal to

p + n

where

n

is the number of bytes
read from the buffer.

If there are bytes following the module descriptor then it is
implementation specific as to whether those bytes are read, ignored,
or reported as an

InvalidModuleDescriptorException

. If this
method fails with an

InvalidModuleDescriptorException

then it
may do so after some, but not all, bytes have been read.

read

```java
public static
ModuleDescriptor
read​(
ByteBuffer
bb)
```

Reads the binary form of a module declaration from a byte buffer as a
module descriptor. This method works exactly as specified by the 2-arg

read

method with the exception that a
packager finder is not used to find additional packages when the module
descriptor encoded in the buffer does not indicate the set of packages.

**Parameters:** bb

- The byte buffer
**Returns:** The module descriptor
**Throws:** InvalidModuleDescriptorException

- If an invalid module descriptor is detected

---

#### read

public static

ModuleDescriptor

read​(

ByteBuffer

bb)

Reads the binary form of a module declaration from a byte buffer as a
module descriptor. This method works exactly as specified by the 2-arg

read

method with the exception that a
packager finder is not used to find additional packages when the module
descriptor encoded in the buffer does not indicate the set of packages.

---

