# Class ModuleDescriptor.Builder

**Source:** `java.base\java\lang\module\ModuleDescriptor.Builder.html`

### Class Description

```java
public static final class
ModuleDescriptor.Builder

extends
Object
```

A builder for building

ModuleDescriptor

objects.

ModuleDescriptor

defines the

newModule

,

newOpenModule

, and

newAutomaticModule

methods to create builders for building

normal

, open, and automatic modules.

The set of packages in the module are accumulated by the

Builder

as the

exports

,

opens

,

packages

,

provides

, and

mainClass

methods are
invoked.

The module names, package names, and class names that are parameters
specified to the builder methods are the module names, package names,
and qualified names of classes (in named packages) as defined in the

The Java™ Language Specification

.

Example usage:

```java
ModuleDescriptor descriptor = ModuleDescriptor.newModule("stats.core")
.requires("java.base")
.exports("org.acme.stats.core.clustering")
.exports("org.acme.stats.core.regression")
.packages(Set.of("org.acme.stats.core.internal"))
.build();
```

**Enclosing class:** ModuleDescriptor

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### public
ModuleDescriptor.Builder
requires​(
ModuleDescriptor.Requires
req)

Adds a dependence on a module.

**Parameters:**
- req

- The dependence

**Returns:**
- This builder

**Throws:**
- IllegalArgumentException

- If the dependence is on the module that this builder was
initialized to build
- IllegalStateException

- If the dependence on the module has already been declared
or this builder is for an automatic module

---

#### public
ModuleDescriptor.Builder
requires​(
Set
<
ModuleDescriptor.Requires.Modifier
> ms,

String
mn,

ModuleDescriptor.Version
compiledVersion)

Adds a dependence on a module with the given (and possibly empty)
set of modifiers. The dependence includes the version of the
module that was recorded at compile-time.

**Parameters:**
- ms

- The set of modifiers
- mn

- The module name
- compiledVersion

- The version of the module recorded at compile-time

**Returns:**
- This builder

**Throws:**
- IllegalArgumentException

- If the module name is

null

, is not a legal module
name, or is equal to the module name that this builder
was initialized to build
- IllegalStateException

- If the dependence on the module has already been declared
or this builder is for an automatic module

---

#### public
ModuleDescriptor.Builder
requires​(
Set
<
ModuleDescriptor.Requires.Modifier
> ms,

String
mn)

Adds a dependence on a module with the given (and possibly empty)
set of modifiers.

**Parameters:**
- ms

- The set of modifiers
- mn

- The module name

**Returns:**
- This builder

**Throws:**
- IllegalArgumentException

- If the module name is

null

, is not a legal module
name, or is equal to the module name that this builder
was initialized to build
- IllegalStateException

- If the dependence on the module has already been declared
or this builder is for an automatic module

---

#### public
ModuleDescriptor.Builder
requires​(
String
mn)

Adds a dependence on a module with an empty set of modifiers.

**Parameters:**
- mn

- The module name

**Returns:**
- This builder

**Throws:**
- IllegalArgumentException

- If the module name is

null

, is not a legal module
name, or is equal to the module name that this builder
was initialized to build
- IllegalStateException

- If the dependence on the module has already been declared
or this builder is for an automatic module

---

#### public
ModuleDescriptor.Builder
exports​(
ModuleDescriptor.Exports
e)

Adds an exported package.

**Parameters:**
- e

- The export

**Returns:**
- This builder

**Throws:**
- IllegalStateException

- If the

package

is already declared as
exported or this builder is for an automatic module

---

#### public
ModuleDescriptor.Builder
exports​(
Set
<
ModuleDescriptor.Exports.Modifier
> ms,

String
pn,

Set
<
String
> targets)

Adds an exported package with the given (and possibly empty) set of
modifiers. The package is exported to a set of target modules.

**Parameters:**
- ms

- The set of modifiers
- pn

- The package name
- targets

- The set of target modules names

**Returns:**
- This builder

**Throws:**
- IllegalArgumentException

- If the package name is

null

or is not a legal
package name, the set of target modules is empty, or the set
of target modules contains a name that is not a legal module
name
- IllegalStateException

- If the package is already declared as exported
or this builder is for an automatic module

---

#### public
ModuleDescriptor.Builder
exports​(
Set
<
ModuleDescriptor.Exports.Modifier
> ms,

String
pn)

Adds an exported package with the given (and possibly empty) set of
modifiers. The package is exported to all modules.

**Parameters:**
- ms

- The set of modifiers
- pn

- The package name

**Returns:**
- This builder

**Throws:**
- IllegalArgumentException

- If the package name is

null

or is not a legal
package name
- IllegalStateException

- If the package is already declared as exported
or this builder is for an automatic module

---

#### public
ModuleDescriptor.Builder
exports​(
String
pn,

Set
<
String
> targets)

Adds an exported package. The package is exported to a set of target
modules.

**Parameters:**
- pn

- The package name
- targets

- The set of target modules names

**Returns:**
- This builder

**Throws:**
- IllegalArgumentException

- If the package name is

null

or is not a legal
package name, the set of target modules is empty, or the set
of target modules contains a name that is not a legal module
name
- IllegalStateException

- If the package is already declared as exported
or this builder is for an automatic module

---

#### public
ModuleDescriptor.Builder
exports​(
String
pn)

Adds an exported package. The package is exported to all modules.

**Parameters:**
- pn

- The package name

**Returns:**
- This builder

**Throws:**
- IllegalArgumentException

- If the package name is

null

or is not a legal
package name
- IllegalStateException

- If the package is already declared as exported
or this builder is for an automatic module

---

#### public
ModuleDescriptor.Builder
opens​(
ModuleDescriptor.Opens
obj)

Adds an open package.

**Parameters:**
- obj

- The

Opens

object

**Returns:**
- This builder

**Throws:**
- IllegalStateException

- If the package is already declared as open, or this is a
builder for an open module or automatic module

---

#### public
ModuleDescriptor.Builder
opens​(
Set
<
ModuleDescriptor.Opens.Modifier
> ms,

String
pn,

Set
<
String
> targets)

Adds an open package with the given (and possibly empty) set of
modifiers. The package is open to a set of target modules.

**Parameters:**
- ms

- The set of modifiers
- pn

- The package name
- targets

- The set of target modules names

**Returns:**
- This builder

**Throws:**
- IllegalArgumentException

- If the package name is

null

or is not a legal
package name, the set of target modules is empty, or the set
of target modules contains a name that is not a legal module
name
- IllegalStateException

- If the package is already declared as open, or this is a
builder for an open module or automatic module

---

#### public
ModuleDescriptor.Builder
opens​(
Set
<
ModuleDescriptor.Opens.Modifier
> ms,

String
pn)

Adds an open package with the given (and possibly empty) set of
modifiers. The package is open to all modules.

**Parameters:**
- ms

- The set of modifiers
- pn

- The package name

**Returns:**
- This builder

**Throws:**
- IllegalArgumentException

- If the package name is

null

or is not a legal
package name
- IllegalStateException

- If the package is already declared as open, or this is a
builder for an open module or automatic module

---

#### public
ModuleDescriptor.Builder
opens​(
String
pn,

Set
<
String
> targets)

Adds an open package. The package is open to a set of target modules.

**Parameters:**
- pn

- The package name
- targets

- The set of target modules names

**Returns:**
- This builder

**Throws:**
- IllegalArgumentException

- If the package name is

null

or is not a legal
package name, the set of target modules is empty, or the set
of target modules contains a name that is not a legal module
name
- IllegalStateException

- If the package is already declared as open, or this is a
builder for an open module or automatic module

---

#### public
ModuleDescriptor.Builder
opens​(
String
pn)

Adds an open package. The package is open to all modules.

**Parameters:**
- pn

- The package name

**Returns:**
- This builder

**Throws:**
- IllegalArgumentException

- If the package name is

null

or is not a legal
package name
- IllegalStateException

- If the package is already declared as open, or this is a
builder for an open module or automatic module

---

#### public
ModuleDescriptor.Builder
uses​(
String
service)

Adds a service dependence.

**Parameters:**
- service

- The service type

**Returns:**
- This builder

**Throws:**
- IllegalArgumentException

- If the service type is

null

or not a qualified name of
a class in a named package
- IllegalStateException

- If a dependency on the service type has already been declared
or this is a builder for an automatic module

---

#### public
ModuleDescriptor.Builder
provides​(
ModuleDescriptor.Provides
p)

Provides a service with one or more implementations. The package for
each

provider

(or provider factory) is
added to the module if not already added.

**Parameters:**
- p

- The provides

**Returns:**
- This builder

**Throws:**
- IllegalStateException

- If the providers for the service type have already been
declared

---

#### public
ModuleDescriptor.Builder
provides​(
String
service,

List
<
String
> providers)

Provides implementations of a service. The package for each provider
(or provider factory) is added to the module if not already added.

**Parameters:**
- service

- The service type
- providers

- The list of provider or provider factory class names

**Returns:**
- This builder

**Throws:**
- IllegalArgumentException

- If the service type or any of the provider class names is

null

or not a qualified name of a class in a named
package, or the list of provider class names is empty
- IllegalStateException

- If the providers for the service type have already been
declared

---

#### public
ModuleDescriptor.Builder
packages​(
Set
<
String
> pns)

Adds packages to the module. All packages in the set of package names
that are not in the module are added to module.

**Parameters:**
- pns

- The (possibly empty) set of package names

**Returns:**
- This builder

**Throws:**
- IllegalArgumentException

- If any of the package names is

null

or is not a
legal package name

---

#### public
ModuleDescriptor.Builder
version​(
ModuleDescriptor.Version
v)

Sets the module version.

**Parameters:**
- v

- The version

**Returns:**
- This builder

---

#### public
ModuleDescriptor.Builder
version​(
String
vs)

Sets the module version.

**Parameters:**
- vs

- The version string to parse

**Returns:**
- This builder

**Throws:**
- IllegalArgumentException

- If

vs

is

null

or cannot be parsed as a
version string

**See Also:**
- ModuleDescriptor.Version.parse(String)

---

#### public
ModuleDescriptor.Builder
mainClass​(
String
mc)

Sets the module main class. The package for the main class is added
to the module if not already added. In other words, this method is
equivalent to first invoking this builder's

packages

method to add the package name of the main class.

**Parameters:**
- mc

- The module main class

**Returns:**
- This builder

**Throws:**
- IllegalArgumentException

- If

mainClass

is

null

or not a qualified
name of a class in a named package

---

#### public
ModuleDescriptor
build()

Builds and returns a

ModuleDescriptor

from its components.

The module will require "

java.base

" even if the dependence
has not been declared (the exception is when building a module named
"

java.base

" as it cannot require itself). The dependence on
"

java.base

" will have the

MANDATED

modifier if the dependence was not declared.

**Returns:**
- The module descriptor

---

### Additional Sections

#### Class ModuleDescriptor.Builder

java.lang.Object

- java.lang.module.ModuleDescriptor.Builder

java.lang.module.ModuleDescriptor.Builder

**Enclosing class:** ModuleDescriptor

```java
public static final class
ModuleDescriptor.Builder

extends
Object
```

A builder for building

ModuleDescriptor

objects.

ModuleDescriptor

defines the

newModule

,

newOpenModule

, and

newAutomaticModule

methods to create builders for building

normal

, open, and automatic modules.

The set of packages in the module are accumulated by the

Builder

as the

exports

,

opens

,

packages

,

provides

, and

mainClass

methods are
invoked.

The module names, package names, and class names that are parameters
specified to the builder methods are the module names, package names,
and qualified names of classes (in named packages) as defined in the

The Java™ Language Specification

.

Example usage:

```java
ModuleDescriptor descriptor = ModuleDescriptor.newModule("stats.core")
.requires("java.base")
.exports("org.acme.stats.core.clustering")
.exports("org.acme.stats.core.regression")
.packages(Set.of("org.acme.stats.core.internal"))
.build();
```

**API Note:** A

Builder

checks the components and invariants as
components are added to the builder. The rationale for this is to detect
errors as early as possible and not defer all validation to the

build

method.
**Since:** 9

public static final class

ModuleDescriptor.Builder

extends

Object

A builder for building

ModuleDescriptor

objects.

ModuleDescriptor

defines the

newModule

,

newOpenModule

, and

newAutomaticModule

methods to create builders for building

normal

, open, and automatic modules.

The set of packages in the module are accumulated by the

Builder

as the

exports

,

opens

,

packages

,

provides

, and

mainClass

methods are
invoked.

The module names, package names, and class names that are parameters
specified to the builder methods are the module names, package names,
and qualified names of classes (in named packages) as defined in the

The Java™ Language Specification

.

Example usage:

```java
ModuleDescriptor descriptor = ModuleDescriptor.newModule("stats.core")
.requires("java.base")
.exports("org.acme.stats.core.clustering")
.exports("org.acme.stats.core.regression")
.packages(Set.of("org.acme.stats.core.internal"))
.build();
```

ModuleDescriptor

defines the

newModule

,

newOpenModule

, and

newAutomaticModule

methods to create builders for building

normal

, open, and automatic modules.

The set of packages in the module are accumulated by the

Builder

as the

exports

,

opens

,

packages

,

provides

, and

mainClass

methods are
invoked.

The module names, package names, and class names that are parameters
specified to the builder methods are the module names, package names,
and qualified names of classes (in named packages) as defined in the

The Java™ Language Specification

.

Example usage:

ModuleDescriptor descriptor = ModuleDescriptor.newModule("stats.core")
.requires("java.base")
.exports("org.acme.stats.core.clustering")
.exports("org.acme.stats.core.regression")
.packages(Set.of("org.acme.stats.core.internal"))
.build();

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

ModuleDescriptor

build

()

Builds and returns a

ModuleDescriptor

from its components.

ModuleDescriptor.Builder

exports

​(

ModuleDescriptor.Exports

e)

Adds an exported package.

ModuleDescriptor.Builder

exports

​(

String

pn)

Adds an exported package.

ModuleDescriptor.Builder

exports

​(

String

pn,

Set

<

String

> targets)

Adds an exported package.

ModuleDescriptor.Builder

exports

​(

Set

<

ModuleDescriptor.Exports.Modifier

> ms,

String

pn)

Adds an exported package with the given (and possibly empty) set of
modifiers.

ModuleDescriptor.Builder

exports

​(

Set

<

ModuleDescriptor.Exports.Modifier

> ms,

String

pn,

Set

<

String

> targets)

Adds an exported package with the given (and possibly empty) set of
modifiers.

ModuleDescriptor.Builder

mainClass

​(

String

mc)

Sets the module main class.

ModuleDescriptor.Builder

opens

​(

ModuleDescriptor.Opens

obj)

Adds an open package.

ModuleDescriptor.Builder

opens

​(

String

pn)

Adds an open package.

ModuleDescriptor.Builder

opens

​(

String

pn,

Set

<

String

> targets)

Adds an open package.

ModuleDescriptor.Builder

opens

​(

Set

<

ModuleDescriptor.Opens.Modifier

> ms,

String

pn)

Adds an open package with the given (and possibly empty) set of
modifiers.

ModuleDescriptor.Builder

opens

​(

Set

<

ModuleDescriptor.Opens.Modifier

> ms,

String

pn,

Set

<

String

> targets)

Adds an open package with the given (and possibly empty) set of
modifiers.

ModuleDescriptor.Builder

packages

​(

Set

<

String

> pns)

Adds packages to the module.

ModuleDescriptor.Builder

provides

​(

ModuleDescriptor.Provides

p)

Provides a service with one or more implementations.

ModuleDescriptor.Builder

provides

​(

String

service,

List

<

String

> providers)

Provides implementations of a service.

ModuleDescriptor.Builder

requires

​(

ModuleDescriptor.Requires

req)

Adds a dependence on a module.

ModuleDescriptor.Builder

requires

​(

String

mn)

Adds a dependence on a module with an empty set of modifiers.

ModuleDescriptor.Builder

requires

​(

Set

<

ModuleDescriptor.Requires.Modifier

> ms,

String

mn)

Adds a dependence on a module with the given (and possibly empty)
set of modifiers.

ModuleDescriptor.Builder

requires

​(

Set

<

ModuleDescriptor.Requires.Modifier

> ms,

String

mn,

ModuleDescriptor.Version

compiledVersion)

Adds a dependence on a module with the given (and possibly empty)
set of modifiers.

ModuleDescriptor.Builder

uses

​(

String

service)

Adds a service dependence.

ModuleDescriptor.Builder

version

​(

ModuleDescriptor.Version

v)

Sets the module version.

ModuleDescriptor.Builder

version

​(

String

vs)

Sets the module version.

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

ModuleDescriptor

build

()

Builds and returns a

ModuleDescriptor

from its components.

ModuleDescriptor.Builder

exports

​(

ModuleDescriptor.Exports

e)

Adds an exported package.

ModuleDescriptor.Builder

exports

​(

String

pn)

Adds an exported package.

ModuleDescriptor.Builder

exports

​(

String

pn,

Set

<

String

> targets)

Adds an exported package.

ModuleDescriptor.Builder

exports

​(

Set

<

ModuleDescriptor.Exports.Modifier

> ms,

String

pn)

Adds an exported package with the given (and possibly empty) set of
modifiers.

ModuleDescriptor.Builder

exports

​(

Set

<

ModuleDescriptor.Exports.Modifier

> ms,

String

pn,

Set

<

String

> targets)

Adds an exported package with the given (and possibly empty) set of
modifiers.

ModuleDescriptor.Builder

mainClass

​(

String

mc)

Sets the module main class.

ModuleDescriptor.Builder

opens

​(

ModuleDescriptor.Opens

obj)

Adds an open package.

ModuleDescriptor.Builder

opens

​(

String

pn)

Adds an open package.

ModuleDescriptor.Builder

opens

​(

String

pn,

Set

<

String

> targets)

Adds an open package.

ModuleDescriptor.Builder

opens

​(

Set

<

ModuleDescriptor.Opens.Modifier

> ms,

String

pn)

Adds an open package with the given (and possibly empty) set of
modifiers.

ModuleDescriptor.Builder

opens

​(

Set

<

ModuleDescriptor.Opens.Modifier

> ms,

String

pn,

Set

<

String

> targets)

Adds an open package with the given (and possibly empty) set of
modifiers.

ModuleDescriptor.Builder

packages

​(

Set

<

String

> pns)

Adds packages to the module.

ModuleDescriptor.Builder

provides

​(

ModuleDescriptor.Provides

p)

Provides a service with one or more implementations.

ModuleDescriptor.Builder

provides

​(

String

service,

List

<

String

> providers)

Provides implementations of a service.

ModuleDescriptor.Builder

requires

​(

ModuleDescriptor.Requires

req)

Adds a dependence on a module.

ModuleDescriptor.Builder

requires

​(

String

mn)

Adds a dependence on a module with an empty set of modifiers.

ModuleDescriptor.Builder

requires

​(

Set

<

ModuleDescriptor.Requires.Modifier

> ms,

String

mn)

Adds a dependence on a module with the given (and possibly empty)
set of modifiers.

ModuleDescriptor.Builder

requires

​(

Set

<

ModuleDescriptor.Requires.Modifier

> ms,

String

mn,

ModuleDescriptor.Version

compiledVersion)

Adds a dependence on a module with the given (and possibly empty)
set of modifiers.

ModuleDescriptor.Builder

uses

​(

String

service)

Adds a service dependence.

ModuleDescriptor.Builder

version

​(

ModuleDescriptor.Version

v)

Sets the module version.

ModuleDescriptor.Builder

version

​(

String

vs)

Sets the module version.

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

Builds and returns a

ModuleDescriptor

from its components.

Adds an exported package.

Adds an exported package with the given (and possibly empty) set of
modifiers.

Sets the module main class.

Adds an open package.

Adds an open package with the given (and possibly empty) set of
modifiers.

Adds packages to the module.

Provides a service with one or more implementations.

Provides implementations of a service.

Adds a dependence on a module.

Adds a dependence on a module with an empty set of modifiers.

Adds a dependence on a module with the given (and possibly empty)
set of modifiers.

Adds a service dependence.

Sets the module version.

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

- requires

```java
public
ModuleDescriptor.Builder
requires​(
ModuleDescriptor.Requires
req)
```

Adds a dependence on a module.

**Parameters:** req

- The dependence
**Returns:** This builder
**Throws:** IllegalArgumentException

- If the dependence is on the module that this builder was
initialized to build
**Throws:** IllegalStateException

- If the dependence on the module has already been declared
or this builder is for an automatic module

- requires

```java
public
ModuleDescriptor.Builder
requires​(
Set
<
ModuleDescriptor.Requires.Modifier
> ms,

String
mn,

ModuleDescriptor.Version
compiledVersion)
```

Adds a dependence on a module with the given (and possibly empty)
set of modifiers. The dependence includes the version of the
module that was recorded at compile-time.

**Parameters:** ms

- The set of modifiers
**Parameters:** mn

- The module name
**Parameters:** compiledVersion

- The version of the module recorded at compile-time
**Returns:** This builder
**Throws:** IllegalArgumentException

- If the module name is

null

, is not a legal module
name, or is equal to the module name that this builder
was initialized to build
**Throws:** IllegalStateException

- If the dependence on the module has already been declared
or this builder is for an automatic module

- requires

```java
public
ModuleDescriptor.Builder
requires​(
Set
<
ModuleDescriptor.Requires.Modifier
> ms,

String
mn)
```

Adds a dependence on a module with the given (and possibly empty)
set of modifiers.

**Parameters:** ms

- The set of modifiers
**Parameters:** mn

- The module name
**Returns:** This builder
**Throws:** IllegalArgumentException

- If the module name is

null

, is not a legal module
name, or is equal to the module name that this builder
was initialized to build
**Throws:** IllegalStateException

- If the dependence on the module has already been declared
or this builder is for an automatic module

- requires

```java
public
ModuleDescriptor.Builder
requires​(
String
mn)
```

Adds a dependence on a module with an empty set of modifiers.

**Parameters:** mn

- The module name
**Returns:** This builder
**Throws:** IllegalArgumentException

- If the module name is

null

, is not a legal module
name, or is equal to the module name that this builder
was initialized to build
**Throws:** IllegalStateException

- If the dependence on the module has already been declared
or this builder is for an automatic module

- exports

```java
public
ModuleDescriptor.Builder
exports​(
ModuleDescriptor.Exports
e)
```

Adds an exported package.

**Parameters:** e

- The export
**Returns:** This builder
**Throws:** IllegalStateException

- If the

package

is already declared as
exported or this builder is for an automatic module

- exports

```java
public
ModuleDescriptor.Builder
exports​(
Set
<
ModuleDescriptor.Exports.Modifier
> ms,

String
pn,

Set
<
String
> targets)
```

Adds an exported package with the given (and possibly empty) set of
modifiers. The package is exported to a set of target modules.

**Parameters:** ms

- The set of modifiers
**Parameters:** pn

- The package name
**Parameters:** targets

- The set of target modules names
**Returns:** This builder
**Throws:** IllegalArgumentException

- If the package name is

null

or is not a legal
package name, the set of target modules is empty, or the set
of target modules contains a name that is not a legal module
name
**Throws:** IllegalStateException

- If the package is already declared as exported
or this builder is for an automatic module

- exports

```java
public
ModuleDescriptor.Builder
exports​(
Set
<
ModuleDescriptor.Exports.Modifier
> ms,

String
pn)
```

Adds an exported package with the given (and possibly empty) set of
modifiers. The package is exported to all modules.

**Parameters:** ms

- The set of modifiers
**Parameters:** pn

- The package name
**Returns:** This builder
**Throws:** IllegalArgumentException

- If the package name is

null

or is not a legal
package name
**Throws:** IllegalStateException

- If the package is already declared as exported
or this builder is for an automatic module

- exports

```java
public
ModuleDescriptor.Builder
exports​(
String
pn,

Set
<
String
> targets)
```

Adds an exported package. The package is exported to a set of target
modules.

**Parameters:** pn

- The package name
**Parameters:** targets

- The set of target modules names
**Returns:** This builder
**Throws:** IllegalArgumentException

- If the package name is

null

or is not a legal
package name, the set of target modules is empty, or the set
of target modules contains a name that is not a legal module
name
**Throws:** IllegalStateException

- If the package is already declared as exported
or this builder is for an automatic module

- exports

```java
public
ModuleDescriptor.Builder
exports​(
String
pn)
```

Adds an exported package. The package is exported to all modules.

**Parameters:** pn

- The package name
**Returns:** This builder
**Throws:** IllegalArgumentException

- If the package name is

null

or is not a legal
package name
**Throws:** IllegalStateException

- If the package is already declared as exported
or this builder is for an automatic module

- opens

```java
public
ModuleDescriptor.Builder
opens​(
ModuleDescriptor.Opens
obj)
```

Adds an open package.

**Parameters:** obj

- The

Opens

object
**Returns:** This builder
**Throws:** IllegalStateException

- If the package is already declared as open, or this is a
builder for an open module or automatic module

- opens

```java
public
ModuleDescriptor.Builder
opens​(
Set
<
ModuleDescriptor.Opens.Modifier
> ms,

String
pn,

Set
<
String
> targets)
```

Adds an open package with the given (and possibly empty) set of
modifiers. The package is open to a set of target modules.

**Parameters:** ms

- The set of modifiers
**Parameters:** pn

- The package name
**Parameters:** targets

- The set of target modules names
**Returns:** This builder
**Throws:** IllegalArgumentException

- If the package name is

null

or is not a legal
package name, the set of target modules is empty, or the set
of target modules contains a name that is not a legal module
name
**Throws:** IllegalStateException

- If the package is already declared as open, or this is a
builder for an open module or automatic module

- opens

```java
public
ModuleDescriptor.Builder
opens​(
Set
<
ModuleDescriptor.Opens.Modifier
> ms,

String
pn)
```

Adds an open package with the given (and possibly empty) set of
modifiers. The package is open to all modules.

**Parameters:** ms

- The set of modifiers
**Parameters:** pn

- The package name
**Returns:** This builder
**Throws:** IllegalArgumentException

- If the package name is

null

or is not a legal
package name
**Throws:** IllegalStateException

- If the package is already declared as open, or this is a
builder for an open module or automatic module

- opens

```java
public
ModuleDescriptor.Builder
opens​(
String
pn,

Set
<
String
> targets)
```

Adds an open package. The package is open to a set of target modules.

**Parameters:** pn

- The package name
**Parameters:** targets

- The set of target modules names
**Returns:** This builder
**Throws:** IllegalArgumentException

- If the package name is

null

or is not a legal
package name, the set of target modules is empty, or the set
of target modules contains a name that is not a legal module
name
**Throws:** IllegalStateException

- If the package is already declared as open, or this is a
builder for an open module or automatic module

- opens

```java
public
ModuleDescriptor.Builder
opens​(
String
pn)
```

Adds an open package. The package is open to all modules.

**Parameters:** pn

- The package name
**Returns:** This builder
**Throws:** IllegalArgumentException

- If the package name is

null

or is not a legal
package name
**Throws:** IllegalStateException

- If the package is already declared as open, or this is a
builder for an open module or automatic module

- uses

```java
public
ModuleDescriptor.Builder
uses​(
String
service)
```

Adds a service dependence.

**Parameters:** service

- The service type
**Returns:** This builder
**Throws:** IllegalArgumentException

- If the service type is

null

or not a qualified name of
a class in a named package
**Throws:** IllegalStateException

- If a dependency on the service type has already been declared
or this is a builder for an automatic module

- provides

```java
public
ModuleDescriptor.Builder
provides​(
ModuleDescriptor.Provides
p)
```

Provides a service with one or more implementations. The package for
each

provider

(or provider factory) is
added to the module if not already added.

**Parameters:** p

- The provides
**Returns:** This builder
**Throws:** IllegalStateException

- If the providers for the service type have already been
declared

- provides

```java
public
ModuleDescriptor.Builder
provides​(
String
service,

List
<
String
> providers)
```

Provides implementations of a service. The package for each provider
(or provider factory) is added to the module if not already added.

**Parameters:** service

- The service type
**Parameters:** providers

- The list of provider or provider factory class names
**Returns:** This builder
**Throws:** IllegalArgumentException

- If the service type or any of the provider class names is

null

or not a qualified name of a class in a named
package, or the list of provider class names is empty
**Throws:** IllegalStateException

- If the providers for the service type have already been
declared

- packages

```java
public
ModuleDescriptor.Builder
packages​(
Set
<
String
> pns)
```

Adds packages to the module. All packages in the set of package names
that are not in the module are added to module.

**Parameters:** pns

- The (possibly empty) set of package names
**Returns:** This builder
**Throws:** IllegalArgumentException

- If any of the package names is

null

or is not a
legal package name

- version

```java
public
ModuleDescriptor.Builder
version​(
ModuleDescriptor.Version
v)
```

Sets the module version.

**Parameters:** v

- The version
**Returns:** This builder

- version

```java
public
ModuleDescriptor.Builder
version​(
String
vs)
```

Sets the module version.

**Parameters:** vs

- The version string to parse
**Returns:** This builder
**Throws:** IllegalArgumentException

- If

vs

is

null

or cannot be parsed as a
version string
**See Also:** ModuleDescriptor.Version.parse(String)

- mainClass

```java
public
ModuleDescriptor.Builder
mainClass​(
String
mc)
```

Sets the module main class. The package for the main class is added
to the module if not already added. In other words, this method is
equivalent to first invoking this builder's

packages

method to add the package name of the main class.

**Parameters:** mc

- The module main class
**Returns:** This builder
**Throws:** IllegalArgumentException

- If

mainClass

is

null

or not a qualified
name of a class in a named package

- build

```java
public
ModuleDescriptor
build()
```

Builds and returns a

ModuleDescriptor

from its components.

The module will require "

java.base

" even if the dependence
has not been declared (the exception is when building a module named
"

java.base

" as it cannot require itself). The dependence on
"

java.base

" will have the

MANDATED

modifier if the dependence was not declared.

**Returns:** The module descriptor

Method Detail

- requires

```java
public
ModuleDescriptor.Builder
requires​(
ModuleDescriptor.Requires
req)
```

Adds a dependence on a module.

**Parameters:** req

- The dependence
**Returns:** This builder
**Throws:** IllegalArgumentException

- If the dependence is on the module that this builder was
initialized to build
**Throws:** IllegalStateException

- If the dependence on the module has already been declared
or this builder is for an automatic module

- requires

```java
public
ModuleDescriptor.Builder
requires​(
Set
<
ModuleDescriptor.Requires.Modifier
> ms,

String
mn,

ModuleDescriptor.Version
compiledVersion)
```

Adds a dependence on a module with the given (and possibly empty)
set of modifiers. The dependence includes the version of the
module that was recorded at compile-time.

**Parameters:** ms

- The set of modifiers
**Parameters:** mn

- The module name
**Parameters:** compiledVersion

- The version of the module recorded at compile-time
**Returns:** This builder
**Throws:** IllegalArgumentException

- If the module name is

null

, is not a legal module
name, or is equal to the module name that this builder
was initialized to build
**Throws:** IllegalStateException

- If the dependence on the module has already been declared
or this builder is for an automatic module

- requires

```java
public
ModuleDescriptor.Builder
requires​(
Set
<
ModuleDescriptor.Requires.Modifier
> ms,

String
mn)
```

Adds a dependence on a module with the given (and possibly empty)
set of modifiers.

**Parameters:** ms

- The set of modifiers
**Parameters:** mn

- The module name
**Returns:** This builder
**Throws:** IllegalArgumentException

- If the module name is

null

, is not a legal module
name, or is equal to the module name that this builder
was initialized to build
**Throws:** IllegalStateException

- If the dependence on the module has already been declared
or this builder is for an automatic module

- requires

```java
public
ModuleDescriptor.Builder
requires​(
String
mn)
```

Adds a dependence on a module with an empty set of modifiers.

**Parameters:** mn

- The module name
**Returns:** This builder
**Throws:** IllegalArgumentException

- If the module name is

null

, is not a legal module
name, or is equal to the module name that this builder
was initialized to build
**Throws:** IllegalStateException

- If the dependence on the module has already been declared
or this builder is for an automatic module

- exports

```java
public
ModuleDescriptor.Builder
exports​(
ModuleDescriptor.Exports
e)
```

Adds an exported package.

**Parameters:** e

- The export
**Returns:** This builder
**Throws:** IllegalStateException

- If the

package

is already declared as
exported or this builder is for an automatic module

- exports

```java
public
ModuleDescriptor.Builder
exports​(
Set
<
ModuleDescriptor.Exports.Modifier
> ms,

String
pn,

Set
<
String
> targets)
```

Adds an exported package with the given (and possibly empty) set of
modifiers. The package is exported to a set of target modules.

**Parameters:** ms

- The set of modifiers
**Parameters:** pn

- The package name
**Parameters:** targets

- The set of target modules names
**Returns:** This builder
**Throws:** IllegalArgumentException

- If the package name is

null

or is not a legal
package name, the set of target modules is empty, or the set
of target modules contains a name that is not a legal module
name
**Throws:** IllegalStateException

- If the package is already declared as exported
or this builder is for an automatic module

- exports

```java
public
ModuleDescriptor.Builder
exports​(
Set
<
ModuleDescriptor.Exports.Modifier
> ms,

String
pn)
```

Adds an exported package with the given (and possibly empty) set of
modifiers. The package is exported to all modules.

**Parameters:** ms

- The set of modifiers
**Parameters:** pn

- The package name
**Returns:** This builder
**Throws:** IllegalArgumentException

- If the package name is

null

or is not a legal
package name
**Throws:** IllegalStateException

- If the package is already declared as exported
or this builder is for an automatic module

- exports

```java
public
ModuleDescriptor.Builder
exports​(
String
pn,

Set
<
String
> targets)
```

Adds an exported package. The package is exported to a set of target
modules.

**Parameters:** pn

- The package name
**Parameters:** targets

- The set of target modules names
**Returns:** This builder
**Throws:** IllegalArgumentException

- If the package name is

null

or is not a legal
package name, the set of target modules is empty, or the set
of target modules contains a name that is not a legal module
name
**Throws:** IllegalStateException

- If the package is already declared as exported
or this builder is for an automatic module

- exports

```java
public
ModuleDescriptor.Builder
exports​(
String
pn)
```

Adds an exported package. The package is exported to all modules.

**Parameters:** pn

- The package name
**Returns:** This builder
**Throws:** IllegalArgumentException

- If the package name is

null

or is not a legal
package name
**Throws:** IllegalStateException

- If the package is already declared as exported
or this builder is for an automatic module

- opens

```java
public
ModuleDescriptor.Builder
opens​(
ModuleDescriptor.Opens
obj)
```

Adds an open package.

**Parameters:** obj

- The

Opens

object
**Returns:** This builder
**Throws:** IllegalStateException

- If the package is already declared as open, or this is a
builder for an open module or automatic module

- opens

```java
public
ModuleDescriptor.Builder
opens​(
Set
<
ModuleDescriptor.Opens.Modifier
> ms,

String
pn,

Set
<
String
> targets)
```

Adds an open package with the given (and possibly empty) set of
modifiers. The package is open to a set of target modules.

**Parameters:** ms

- The set of modifiers
**Parameters:** pn

- The package name
**Parameters:** targets

- The set of target modules names
**Returns:** This builder
**Throws:** IllegalArgumentException

- If the package name is

null

or is not a legal
package name, the set of target modules is empty, or the set
of target modules contains a name that is not a legal module
name
**Throws:** IllegalStateException

- If the package is already declared as open, or this is a
builder for an open module or automatic module

- opens

```java
public
ModuleDescriptor.Builder
opens​(
Set
<
ModuleDescriptor.Opens.Modifier
> ms,

String
pn)
```

Adds an open package with the given (and possibly empty) set of
modifiers. The package is open to all modules.

**Parameters:** ms

- The set of modifiers
**Parameters:** pn

- The package name
**Returns:** This builder
**Throws:** IllegalArgumentException

- If the package name is

null

or is not a legal
package name
**Throws:** IllegalStateException

- If the package is already declared as open, or this is a
builder for an open module or automatic module

- opens

```java
public
ModuleDescriptor.Builder
opens​(
String
pn,

Set
<
String
> targets)
```

Adds an open package. The package is open to a set of target modules.

**Parameters:** pn

- The package name
**Parameters:** targets

- The set of target modules names
**Returns:** This builder
**Throws:** IllegalArgumentException

- If the package name is

null

or is not a legal
package name, the set of target modules is empty, or the set
of target modules contains a name that is not a legal module
name
**Throws:** IllegalStateException

- If the package is already declared as open, or this is a
builder for an open module or automatic module

- opens

```java
public
ModuleDescriptor.Builder
opens​(
String
pn)
```

Adds an open package. The package is open to all modules.

**Parameters:** pn

- The package name
**Returns:** This builder
**Throws:** IllegalArgumentException

- If the package name is

null

or is not a legal
package name
**Throws:** IllegalStateException

- If the package is already declared as open, or this is a
builder for an open module or automatic module

- uses

```java
public
ModuleDescriptor.Builder
uses​(
String
service)
```

Adds a service dependence.

**Parameters:** service

- The service type
**Returns:** This builder
**Throws:** IllegalArgumentException

- If the service type is

null

or not a qualified name of
a class in a named package
**Throws:** IllegalStateException

- If a dependency on the service type has already been declared
or this is a builder for an automatic module

- provides

```java
public
ModuleDescriptor.Builder
provides​(
ModuleDescriptor.Provides
p)
```

Provides a service with one or more implementations. The package for
each

provider

(or provider factory) is
added to the module if not already added.

**Parameters:** p

- The provides
**Returns:** This builder
**Throws:** IllegalStateException

- If the providers for the service type have already been
declared

- provides

```java
public
ModuleDescriptor.Builder
provides​(
String
service,

List
<
String
> providers)
```

Provides implementations of a service. The package for each provider
(or provider factory) is added to the module if not already added.

**Parameters:** service

- The service type
**Parameters:** providers

- The list of provider or provider factory class names
**Returns:** This builder
**Throws:** IllegalArgumentException

- If the service type or any of the provider class names is

null

or not a qualified name of a class in a named
package, or the list of provider class names is empty
**Throws:** IllegalStateException

- If the providers for the service type have already been
declared

- packages

```java
public
ModuleDescriptor.Builder
packages​(
Set
<
String
> pns)
```

Adds packages to the module. All packages in the set of package names
that are not in the module are added to module.

**Parameters:** pns

- The (possibly empty) set of package names
**Returns:** This builder
**Throws:** IllegalArgumentException

- If any of the package names is

null

or is not a
legal package name

- version

```java
public
ModuleDescriptor.Builder
version​(
ModuleDescriptor.Version
v)
```

Sets the module version.

**Parameters:** v

- The version
**Returns:** This builder

- version

```java
public
ModuleDescriptor.Builder
version​(
String
vs)
```

Sets the module version.

**Parameters:** vs

- The version string to parse
**Returns:** This builder
**Throws:** IllegalArgumentException

- If

vs

is

null

or cannot be parsed as a
version string
**See Also:** ModuleDescriptor.Version.parse(String)

- mainClass

```java
public
ModuleDescriptor.Builder
mainClass​(
String
mc)
```

Sets the module main class. The package for the main class is added
to the module if not already added. In other words, this method is
equivalent to first invoking this builder's

packages

method to add the package name of the main class.

**Parameters:** mc

- The module main class
**Returns:** This builder
**Throws:** IllegalArgumentException

- If

mainClass

is

null

or not a qualified
name of a class in a named package

- build

```java
public
ModuleDescriptor
build()
```

Builds and returns a

ModuleDescriptor

from its components.

The module will require "

java.base

" even if the dependence
has not been declared (the exception is when building a module named
"

java.base

" as it cannot require itself). The dependence on
"

java.base

" will have the

MANDATED

modifier if the dependence was not declared.

**Returns:** The module descriptor

---

#### Method Detail

requires

```java
public
ModuleDescriptor.Builder
requires​(
ModuleDescriptor.Requires
req)
```

Adds a dependence on a module.

**Parameters:** req

- The dependence
**Returns:** This builder
**Throws:** IllegalArgumentException

- If the dependence is on the module that this builder was
initialized to build
**Throws:** IllegalStateException

- If the dependence on the module has already been declared
or this builder is for an automatic module

---

#### requires

public

ModuleDescriptor.Builder

requires​(

ModuleDescriptor.Requires

req)

Adds a dependence on a module.

requires

```java
public
ModuleDescriptor.Builder
requires​(
Set
<
ModuleDescriptor.Requires.Modifier
> ms,

String
mn,

ModuleDescriptor.Version
compiledVersion)
```

Adds a dependence on a module with the given (and possibly empty)
set of modifiers. The dependence includes the version of the
module that was recorded at compile-time.

**Parameters:** ms

- The set of modifiers
**Parameters:** mn

- The module name
**Parameters:** compiledVersion

- The version of the module recorded at compile-time
**Returns:** This builder
**Throws:** IllegalArgumentException

- If the module name is

null

, is not a legal module
name, or is equal to the module name that this builder
was initialized to build
**Throws:** IllegalStateException

- If the dependence on the module has already been declared
or this builder is for an automatic module

---

#### requires

public

ModuleDescriptor.Builder

requires​(

Set

<

ModuleDescriptor.Requires.Modifier

> ms,

String

mn,

ModuleDescriptor.Version

compiledVersion)

Adds a dependence on a module with the given (and possibly empty)
set of modifiers. The dependence includes the version of the
module that was recorded at compile-time.

requires

```java
public
ModuleDescriptor.Builder
requires​(
Set
<
ModuleDescriptor.Requires.Modifier
> ms,

String
mn)
```

Adds a dependence on a module with the given (and possibly empty)
set of modifiers.

**Parameters:** ms

- The set of modifiers
**Parameters:** mn

- The module name
**Returns:** This builder
**Throws:** IllegalArgumentException

- If the module name is

null

, is not a legal module
name, or is equal to the module name that this builder
was initialized to build
**Throws:** IllegalStateException

- If the dependence on the module has already been declared
or this builder is for an automatic module

---

#### requires

public

ModuleDescriptor.Builder

requires​(

Set

<

ModuleDescriptor.Requires.Modifier

> ms,

String

mn)

Adds a dependence on a module with the given (and possibly empty)
set of modifiers.

requires

```java
public
ModuleDescriptor.Builder
requires​(
String
mn)
```

Adds a dependence on a module with an empty set of modifiers.

**Parameters:** mn

- The module name
**Returns:** This builder
**Throws:** IllegalArgumentException

- If the module name is

null

, is not a legal module
name, or is equal to the module name that this builder
was initialized to build
**Throws:** IllegalStateException

- If the dependence on the module has already been declared
or this builder is for an automatic module

---

#### requires

public

ModuleDescriptor.Builder

requires​(

String

mn)

Adds a dependence on a module with an empty set of modifiers.

exports

```java
public
ModuleDescriptor.Builder
exports​(
ModuleDescriptor.Exports
e)
```

Adds an exported package.

**Parameters:** e

- The export
**Returns:** This builder
**Throws:** IllegalStateException

- If the

package

is already declared as
exported or this builder is for an automatic module

---

#### exports

public

ModuleDescriptor.Builder

exports​(

ModuleDescriptor.Exports

e)

Adds an exported package.

exports

```java
public
ModuleDescriptor.Builder
exports​(
Set
<
ModuleDescriptor.Exports.Modifier
> ms,

String
pn,

Set
<
String
> targets)
```

Adds an exported package with the given (and possibly empty) set of
modifiers. The package is exported to a set of target modules.

**Parameters:** ms

- The set of modifiers
**Parameters:** pn

- The package name
**Parameters:** targets

- The set of target modules names
**Returns:** This builder
**Throws:** IllegalArgumentException

- If the package name is

null

or is not a legal
package name, the set of target modules is empty, or the set
of target modules contains a name that is not a legal module
name
**Throws:** IllegalStateException

- If the package is already declared as exported
or this builder is for an automatic module

---

#### exports

public

ModuleDescriptor.Builder

exports​(

Set

<

ModuleDescriptor.Exports.Modifier

> ms,

String

pn,

Set

<

String

> targets)

Adds an exported package with the given (and possibly empty) set of
modifiers. The package is exported to a set of target modules.

exports

```java
public
ModuleDescriptor.Builder
exports​(
Set
<
ModuleDescriptor.Exports.Modifier
> ms,

String
pn)
```

Adds an exported package with the given (and possibly empty) set of
modifiers. The package is exported to all modules.

**Parameters:** ms

- The set of modifiers
**Parameters:** pn

- The package name
**Returns:** This builder
**Throws:** IllegalArgumentException

- If the package name is

null

or is not a legal
package name
**Throws:** IllegalStateException

- If the package is already declared as exported
or this builder is for an automatic module

---

#### exports

public

ModuleDescriptor.Builder

exports​(

Set

<

ModuleDescriptor.Exports.Modifier

> ms,

String

pn)

Adds an exported package with the given (and possibly empty) set of
modifiers. The package is exported to all modules.

exports

```java
public
ModuleDescriptor.Builder
exports​(
String
pn,

Set
<
String
> targets)
```

Adds an exported package. The package is exported to a set of target
modules.

**Parameters:** pn

- The package name
**Parameters:** targets

- The set of target modules names
**Returns:** This builder
**Throws:** IllegalArgumentException

- If the package name is

null

or is not a legal
package name, the set of target modules is empty, or the set
of target modules contains a name that is not a legal module
name
**Throws:** IllegalStateException

- If the package is already declared as exported
or this builder is for an automatic module

---

#### exports

public

ModuleDescriptor.Builder

exports​(

String

pn,

Set

<

String

> targets)

Adds an exported package. The package is exported to a set of target
modules.

exports

```java
public
ModuleDescriptor.Builder
exports​(
String
pn)
```

Adds an exported package. The package is exported to all modules.

**Parameters:** pn

- The package name
**Returns:** This builder
**Throws:** IllegalArgumentException

- If the package name is

null

or is not a legal
package name
**Throws:** IllegalStateException

- If the package is already declared as exported
or this builder is for an automatic module

---

#### exports

public

ModuleDescriptor.Builder

exports​(

String

pn)

Adds an exported package. The package is exported to all modules.

opens

```java
public
ModuleDescriptor.Builder
opens​(
ModuleDescriptor.Opens
obj)
```

Adds an open package.

**Parameters:** obj

- The

Opens

object
**Returns:** This builder
**Throws:** IllegalStateException

- If the package is already declared as open, or this is a
builder for an open module or automatic module

---

#### opens

public

ModuleDescriptor.Builder

opens​(

ModuleDescriptor.Opens

obj)

Adds an open package.

opens

```java
public
ModuleDescriptor.Builder
opens​(
Set
<
ModuleDescriptor.Opens.Modifier
> ms,

String
pn,

Set
<
String
> targets)
```

Adds an open package with the given (and possibly empty) set of
modifiers. The package is open to a set of target modules.

**Parameters:** ms

- The set of modifiers
**Parameters:** pn

- The package name
**Parameters:** targets

- The set of target modules names
**Returns:** This builder
**Throws:** IllegalArgumentException

- If the package name is

null

or is not a legal
package name, the set of target modules is empty, or the set
of target modules contains a name that is not a legal module
name
**Throws:** IllegalStateException

- If the package is already declared as open, or this is a
builder for an open module or automatic module

---

#### opens

public

ModuleDescriptor.Builder

opens​(

Set

<

ModuleDescriptor.Opens.Modifier

> ms,

String

pn,

Set

<

String

> targets)

Adds an open package with the given (and possibly empty) set of
modifiers. The package is open to a set of target modules.

opens

```java
public
ModuleDescriptor.Builder
opens​(
Set
<
ModuleDescriptor.Opens.Modifier
> ms,

String
pn)
```

Adds an open package with the given (and possibly empty) set of
modifiers. The package is open to all modules.

**Parameters:** ms

- The set of modifiers
**Parameters:** pn

- The package name
**Returns:** This builder
**Throws:** IllegalArgumentException

- If the package name is

null

or is not a legal
package name
**Throws:** IllegalStateException

- If the package is already declared as open, or this is a
builder for an open module or automatic module

---

#### opens

public

ModuleDescriptor.Builder

opens​(

Set

<

ModuleDescriptor.Opens.Modifier

> ms,

String

pn)

Adds an open package with the given (and possibly empty) set of
modifiers. The package is open to all modules.

opens

```java
public
ModuleDescriptor.Builder
opens​(
String
pn,

Set
<
String
> targets)
```

Adds an open package. The package is open to a set of target modules.

**Parameters:** pn

- The package name
**Parameters:** targets

- The set of target modules names
**Returns:** This builder
**Throws:** IllegalArgumentException

- If the package name is

null

or is not a legal
package name, the set of target modules is empty, or the set
of target modules contains a name that is not a legal module
name
**Throws:** IllegalStateException

- If the package is already declared as open, or this is a
builder for an open module or automatic module

---

#### opens

public

ModuleDescriptor.Builder

opens​(

String

pn,

Set

<

String

> targets)

Adds an open package. The package is open to a set of target modules.

opens

```java
public
ModuleDescriptor.Builder
opens​(
String
pn)
```

Adds an open package. The package is open to all modules.

**Parameters:** pn

- The package name
**Returns:** This builder
**Throws:** IllegalArgumentException

- If the package name is

null

or is not a legal
package name
**Throws:** IllegalStateException

- If the package is already declared as open, or this is a
builder for an open module or automatic module

---

#### opens

public

ModuleDescriptor.Builder

opens​(

String

pn)

Adds an open package. The package is open to all modules.

uses

```java
public
ModuleDescriptor.Builder
uses​(
String
service)
```

Adds a service dependence.

**Parameters:** service

- The service type
**Returns:** This builder
**Throws:** IllegalArgumentException

- If the service type is

null

or not a qualified name of
a class in a named package
**Throws:** IllegalStateException

- If a dependency on the service type has already been declared
or this is a builder for an automatic module

---

#### uses

public

ModuleDescriptor.Builder

uses​(

String

service)

Adds a service dependence.

provides

```java
public
ModuleDescriptor.Builder
provides​(
ModuleDescriptor.Provides
p)
```

Provides a service with one or more implementations. The package for
each

provider

(or provider factory) is
added to the module if not already added.

**Parameters:** p

- The provides
**Returns:** This builder
**Throws:** IllegalStateException

- If the providers for the service type have already been
declared

---

#### provides

public

ModuleDescriptor.Builder

provides​(

ModuleDescriptor.Provides

p)

Provides a service with one or more implementations. The package for
each

provider

(or provider factory) is
added to the module if not already added.

provides

```java
public
ModuleDescriptor.Builder
provides​(
String
service,

List
<
String
> providers)
```

Provides implementations of a service. The package for each provider
(or provider factory) is added to the module if not already added.

**Parameters:** service

- The service type
**Parameters:** providers

- The list of provider or provider factory class names
**Returns:** This builder
**Throws:** IllegalArgumentException

- If the service type or any of the provider class names is

null

or not a qualified name of a class in a named
package, or the list of provider class names is empty
**Throws:** IllegalStateException

- If the providers for the service type have already been
declared

---

#### provides

public

ModuleDescriptor.Builder

provides​(

String

service,

List

<

String

> providers)

Provides implementations of a service. The package for each provider
(or provider factory) is added to the module if not already added.

packages

```java
public
ModuleDescriptor.Builder
packages​(
Set
<
String
> pns)
```

Adds packages to the module. All packages in the set of package names
that are not in the module are added to module.

**Parameters:** pns

- The (possibly empty) set of package names
**Returns:** This builder
**Throws:** IllegalArgumentException

- If any of the package names is

null

or is not a
legal package name

---

#### packages

public

ModuleDescriptor.Builder

packages​(

Set

<

String

> pns)

Adds packages to the module. All packages in the set of package names
that are not in the module are added to module.

version

```java
public
ModuleDescriptor.Builder
version​(
ModuleDescriptor.Version
v)
```

Sets the module version.

**Parameters:** v

- The version
**Returns:** This builder

---

#### version

public

ModuleDescriptor.Builder

version​(

ModuleDescriptor.Version

v)

Sets the module version.

version

```java
public
ModuleDescriptor.Builder
version​(
String
vs)
```

Sets the module version.

**Parameters:** vs

- The version string to parse
**Returns:** This builder
**Throws:** IllegalArgumentException

- If

vs

is

null

or cannot be parsed as a
version string
**See Also:** ModuleDescriptor.Version.parse(String)

---

#### version

public

ModuleDescriptor.Builder

version​(

String

vs)

Sets the module version.

mainClass

```java
public
ModuleDescriptor.Builder
mainClass​(
String
mc)
```

Sets the module main class. The package for the main class is added
to the module if not already added. In other words, this method is
equivalent to first invoking this builder's

packages

method to add the package name of the main class.

**Parameters:** mc

- The module main class
**Returns:** This builder
**Throws:** IllegalArgumentException

- If

mainClass

is

null

or not a qualified
name of a class in a named package

---

#### mainClass

public

ModuleDescriptor.Builder

mainClass​(

String

mc)

Sets the module main class. The package for the main class is added
to the module if not already added. In other words, this method is
equivalent to first invoking this builder's

packages

method to add the package name of the main class.

build

```java
public
ModuleDescriptor
build()
```

Builds and returns a

ModuleDescriptor

from its components.

The module will require "

java.base

" even if the dependence
has not been declared (the exception is when building a module named
"

java.base

" as it cannot require itself). The dependence on
"

java.base

" will have the

MANDATED

modifier if the dependence was not declared.

**Returns:** The module descriptor

---

#### build

public

ModuleDescriptor

build()

Builds and returns a

ModuleDescriptor

from its components.

The module will require "

java.base

" even if the dependence
has not been declared (the exception is when building a module named
"

java.base

" as it cannot require itself). The dependence on
"

java.base

" will have the

MANDATED

modifier if the dependence was not declared.

The module will require "

java.base

" even if the dependence
has not been declared (the exception is when building a module named
"

java.base

" as it cannot require itself). The dependence on
"

java.base

" will have the

MANDATED

modifier if the dependence was not declared.

---

