# Class Configuration

**Source:** `java.base\java\lang\module\Configuration.html`

### Class Description

```java
public final class
Configuration

extends
Object
```

A configuration that is the result of

resolution

or resolution with

service binding

.

A configuration encapsulates the

readability graph

that is the
output of resolution. A readability graph is a directed graph whose vertices
are of type

ResolvedModule

and the edges represent the readability
amongst the modules.

Configuration

defines the

modules()

method to get the set of resolved modules in the graph.

ResolvedModule

defines the

reads()

method to
get the set of modules that a resolved module reads. The modules that are
read may be in the same configuration or may be in

parent

configurations.

Configuration defines the

resolve

method to resolve a collection of root modules, and the

resolveAndBind

method to do resolution with service binding. There are instance and
static variants of both methods. The instance methods create a configuration
with the receiver as the parent configuration. The static methods are for
more advanced cases where there can be more than one parent configuration.

Each

layer

of modules in the Java virtual
machine is created from a configuration. The configuration for the

boot

layer is obtained by invoking

ModuleLayer.boot().configuration()

. The configuration for the boot layer
will often be the parent when creating new configurations.

Example

The following example uses the

resolve

method to resolve a
module named

myapp

with the configuration for the boot layer as the
parent configuration. It prints the name of each resolved module and the
names of the modules that each module reads.

```java
ModuleFinder finder = ModuleFinder.of(dir1, dir2, dir3);

Configuration parent = ModuleLayer.boot().configuration();

Configuration cf = parent.resolve(finder, ModuleFinder.of(), Set.of("myapp"));
cf.modules().forEach(m -> {
System.out.format("%s -> %s%n",
m.name(),
m.reads().stream()
.map(ResolvedModule::name)
.collect(Collectors.joining(", ")));
});
```

**Since:** 9
**See Also:** ModuleLayer

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### public
Configuration
resolve​(
ModuleFinder
before,

ModuleFinder
after,

Collection
<
String
> roots)

Resolves a collection of root modules, with this configuration as its
parent, to create a new configuration. This method works exactly as
specified by the static

resolve

method when invoked with this configuration as the parent. In other words,
if this configuration is

cf

then this method is equivalent to
invoking:

```java
Configuration.resolve(before, List.of(cf), after, roots);
```

**Parameters:**
- before

- The

before

module finder to find modules
- after

- The

after

module finder to locate modules when not
located by the

before

module finder or in parent
configurations
- roots

- The possibly-empty collection of module names of the modules
to resolve

**Returns:**
- The configuration that is the result of resolving the given
root modules

**Throws:**
- FindException

- If resolution fails for any of the observability-related reasons
specified by the static

resolve

method
- ResolutionException

- If resolution fails any of the consistency checks specified by
the static

resolve

method
- SecurityException

- If locating a module is denied by the security manager

---

#### public
Configuration
resolveAndBind​(
ModuleFinder
before,

ModuleFinder
after,

Collection
<
String
> roots)

Resolves a collection of root modules, with service binding, and with
this configuration as its parent, to create a new configuration.
This method works exactly as specified by the static

resolveAndBind

method when invoked with this configuration
as the parent. In other words, if this configuration is

cf

then
this method is equivalent to invoking:

```java
Configuration.resolveAndBind(before, List.of(cf), after, roots);
```

**Parameters:**
- before

- The

before

module finder to find modules
- after

- The

after

module finder to locate modules when not
located by the

before

module finder or in parent
configurations
- roots

- The possibly-empty collection of module names of the modules
to resolve

**Returns:**
- The configuration that is the result of resolving, with service
binding, the given root modules

**Throws:**
- FindException

- If resolution fails for any of the observability-related reasons
specified by the static

resolve

method
- ResolutionException

- If resolution fails any of the consistency checks specified by
the static

resolve

method
- SecurityException

- If locating a module is denied by the security manager

---

#### public static
Configuration
resolve​(
ModuleFinder
before,

List
<
Configuration
> parents,

ModuleFinder
after,

Collection
<
String
> roots)

Resolves a collection of root modules to create a configuration.

Each root module is located using the given

before

module
finder. If a module is not found then it is located in the parent
configuration as if by invoking the

findModule

method on each parent in iteration order. If not found then
the module is located using the given

after

module finder. The
same search order is used to locate transitive dependences. Root modules
or dependences that are located in a parent configuration are resolved
no further and are not included in the resulting configuration.

When all modules have been enumerated then a readability graph
is computed, and in conjunction with the module exports and service use,
checked for consistency.

Resolution may fail with

FindException

for the following

observability-related

reasons:

- A root module, or a direct or transitive dependency, is not
found.
- An error occurs when attempting to find a module.
Possible errors include I/O errors, errors detected parsing a module
descriptor (

module-info.class

) or two versions of the same
module are found in the same directory.

Resolution may fail with

ResolutionException

if any of the
following consistency checks fail:

- A cycle is detected, say where module

m1

requires
module

m2

and

m2

requires

m1

.
- A module reads two or more modules with the same name. This
includes the case where a module reads another with the same name as
itself.
- Two or more modules in the configuration export the same
package to a module that reads both. This includes the case where a
module

M

containing package

p

reads another module
that exports

p

to

M

.
- A module

M

declares that it "

uses p.S

" or
"

provides p.S with ...

" but package

p

is neither in
module

M

nor exported to

M

by any module that

M

reads.

**Parameters:**
- before

- The

before

module finder to find modules
- parents

- The list parent configurations in search order
- after

- The

after

module finder to locate modules when not
located by the

before

module finder or in parent
configurations
- roots

- The possibly-empty collection of module names of the modules
to resolve

**Returns:**
- The configuration that is the result of resolving the given
root modules

**Throws:**
- FindException

- If resolution fails for any of observability-related reasons
specified above
- ResolutionException

- If resolution fails for any of the consistency checks specified
above
- IllegalArgumentException

- If the list of parents is empty, or the list has two or more
parents with modules for different target operating systems,
architectures, or versions
- SecurityException

- If locating a module is denied by the security manager

**Implementation Note:**
- In the implementation then observability of modules may depend
on referential integrity or other checks that ensure different builds of
tightly coupled modules or modules for specific operating systems or
architectures are not combined in the same configuration.

---

#### public static
Configuration
resolveAndBind​(
ModuleFinder
before,

List
<
Configuration
> parents,

ModuleFinder
after,

Collection
<
String
> roots)

Resolves a collection of root modules, with service binding, to create
configuration.

This method works exactly as specified by

resolve

except that the graph of resolved modules is augmented
with modules induced by the service-use dependence relation.

More specifically, the root modules are
resolved as if by calling

resolve

. The resolved modules, and
all modules in the parent configurations, with

service dependences

are then examined. All modules found by the given
module finders that

provide

an
implementation of one or more of the service types are added to the
module graph and then resolved as if by calling the

resolve

method. Adding modules to the module graph may introduce new
service-use dependences and so the process works iteratively until no
more modules are added.

As service binding involves resolution then it may fail with

FindException

or

ResolutionException

for exactly the same
reasons specified in

resolve

.

**Parameters:**
- before

- The

before

module finder to find modules
- parents

- The list parent configurations in search order
- after

- The

after

module finder to locate modules when not
located by the

before

module finder or in parent
configurations
- roots

- The possibly-empty collection of module names of the modules
to resolve

**Returns:**
- The configuration that is the result of resolving, with service
binding, the given root modules

**Throws:**
- FindException

- If resolution fails for any of the observability-related reasons
specified by the static

resolve

method
- ResolutionException

- If resolution fails any of the consistency checks specified by
the static

resolve

method
- IllegalArgumentException

- If the list of parents is empty, or the list has two or more
parents with modules for different target operating systems,
architectures, or versions
- SecurityException

- If locating a module is denied by the security manager

---

#### public static
Configuration
empty()

Returns the

empty

configuration. There are no modules in the
empty configuration. It has no parents.

**Returns:**
- The empty configuration

---

#### public
List
<
Configuration
> parents()

Returns an unmodifiable list of this configuration's parents, in search
order. If this is the

empty configuration

then an
empty list is returned.

**Returns:**
- A possibly-empty unmodifiable list of this parent configurations

---

#### public
Set
<
ResolvedModule
> modules()

Returns an immutable set of the resolved modules in this configuration.

**Returns:**
- A possibly-empty unmodifiable set of the resolved modules
in this configuration

---

#### public
Optional
<
ResolvedModule
> findModule​(
String
name)

Finds a resolved module in this configuration, or if not in this
configuration, the

parent

configurations.
Finding a module in parent configurations is equivalent to invoking

findModule

on each parent, in search order, until the module
is found or all parents have been searched. In a

tree of
configurations

then this is equivalent to a depth-first search.

**Parameters:**
- name

- The module name of the resolved module to find

**Returns:**
- The resolved module with the given name or an empty

Optional

if there isn't a module with this name in this
configuration or any parent configurations

---

#### public
String
toString()

Returns a string describing this configuration.

**Overrides:**
- toString

in class

Object

**Returns:**
- A possibly empty string describing this configuration

---

### Additional Sections

#### Class Configuration

java.lang.Object

- java.lang.module.Configuration

java.lang.module.Configuration

```java
public final class
Configuration

extends
Object
```

A configuration that is the result of

resolution

or resolution with

service binding

.

A configuration encapsulates the

readability graph

that is the
output of resolution. A readability graph is a directed graph whose vertices
are of type

ResolvedModule

and the edges represent the readability
amongst the modules.

Configuration

defines the

modules()

method to get the set of resolved modules in the graph.

ResolvedModule

defines the

reads()

method to
get the set of modules that a resolved module reads. The modules that are
read may be in the same configuration or may be in

parent

configurations.

Configuration defines the

resolve

method to resolve a collection of root modules, and the

resolveAndBind

method to do resolution with service binding. There are instance and
static variants of both methods. The instance methods create a configuration
with the receiver as the parent configuration. The static methods are for
more advanced cases where there can be more than one parent configuration.

Each

layer

of modules in the Java virtual
machine is created from a configuration. The configuration for the

boot

layer is obtained by invoking

ModuleLayer.boot().configuration()

. The configuration for the boot layer
will often be the parent when creating new configurations.

Example

The following example uses the

resolve

method to resolve a
module named

myapp

with the configuration for the boot layer as the
parent configuration. It prints the name of each resolved module and the
names of the modules that each module reads.

```java
ModuleFinder finder = ModuleFinder.of(dir1, dir2, dir3);

Configuration parent = ModuleLayer.boot().configuration();

Configuration cf = parent.resolve(finder, ModuleFinder.of(), Set.of("myapp"));
cf.modules().forEach(m -> {
System.out.format("%s -> %s%n",
m.name(),
m.reads().stream()
.map(ResolvedModule::name)
.collect(Collectors.joining(", ")));
});
```

**Since:** 9
**See Also:** ModuleLayer

public final class

Configuration

extends

Object

A configuration that is the result of

resolution

or resolution with

service binding

.

A configuration encapsulates the

readability graph

that is the
output of resolution. A readability graph is a directed graph whose vertices
are of type

ResolvedModule

and the edges represent the readability
amongst the modules.

Configuration

defines the

modules()

method to get the set of resolved modules in the graph.

ResolvedModule

defines the

reads()

method to
get the set of modules that a resolved module reads. The modules that are
read may be in the same configuration or may be in

parent

configurations.

Configuration defines the

resolve

method to resolve a collection of root modules, and the

resolveAndBind

method to do resolution with service binding. There are instance and
static variants of both methods. The instance methods create a configuration
with the receiver as the parent configuration. The static methods are for
more advanced cases where there can be more than one parent configuration.

Each

layer

of modules in the Java virtual
machine is created from a configuration. The configuration for the

boot

layer is obtained by invoking

ModuleLayer.boot().configuration()

. The configuration for the boot layer
will often be the parent when creating new configurations.

Example

The following example uses the

resolve

method to resolve a
module named

myapp

with the configuration for the boot layer as the
parent configuration. It prints the name of each resolved module and the
names of the modules that each module reads.

```java
ModuleFinder finder = ModuleFinder.of(dir1, dir2, dir3);

Configuration parent = ModuleLayer.boot().configuration();

Configuration cf = parent.resolve(finder, ModuleFinder.of(), Set.of("myapp"));
cf.modules().forEach(m -> {
System.out.format("%s -> %s%n",
m.name(),
m.reads().stream()
.map(ResolvedModule::name)
.collect(Collectors.joining(", ")));
});
```

A configuration encapsulates the

readability graph

that is the
output of resolution. A readability graph is a directed graph whose vertices
are of type

ResolvedModule

and the edges represent the readability
amongst the modules.

Configuration

defines the

modules()

method to get the set of resolved modules in the graph.

ResolvedModule

defines the

reads()

method to
get the set of modules that a resolved module reads. The modules that are
read may be in the same configuration or may be in

parent

configurations.

Configuration defines the

resolve

method to resolve a collection of root modules, and the

resolveAndBind

method to do resolution with service binding. There are instance and
static variants of both methods. The instance methods create a configuration
with the receiver as the parent configuration. The static methods are for
more advanced cases where there can be more than one parent configuration.

Each

layer

of modules in the Java virtual
machine is created from a configuration. The configuration for the

boot

layer is obtained by invoking

ModuleLayer.boot().configuration()

. The configuration for the boot layer
will often be the parent when creating new configurations.

---

#### Example

The following example uses the

resolve

method to resolve a
module named

myapp

with the configuration for the boot layer as the
parent configuration. It prints the name of each resolved module and the
names of the modules that each module reads.

ModuleFinder finder = ModuleFinder.of(dir1, dir2, dir3);

Configuration parent = ModuleLayer.boot().configuration();

Configuration cf = parent.resolve(finder, ModuleFinder.of(), Set.of("myapp"));
cf.modules().forEach(m -> {
System.out.format("%s -> %s%n",
m.name(),
m.reads().stream()
.map(ResolvedModule::name)
.collect(Collectors.joining(", ")));
});

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

static

Configuration

empty

()

Returns the

empty

configuration.

Optional

<

ResolvedModule

>

findModule

​(

String

name)

Finds a resolved module in this configuration, or if not in this
configuration, the

parent

configurations.

Set

<

ResolvedModule

>

modules

()

Returns an immutable set of the resolved modules in this configuration.

List

<

Configuration

>

parents

()

Returns an unmodifiable list of this configuration's parents, in search
order.

Configuration

resolve

​(

ModuleFinder

before,

ModuleFinder

after,

Collection

<

String

> roots)

Resolves a collection of root modules, with this configuration as its
parent, to create a new configuration.

static

Configuration

resolve

​(

ModuleFinder

before,

List

<

Configuration

> parents,

ModuleFinder

after,

Collection

<

String

> roots)

Resolves a collection of root modules to create a configuration.

Configuration

resolveAndBind

​(

ModuleFinder

before,

ModuleFinder

after,

Collection

<

String

> roots)

Resolves a collection of root modules, with service binding, and with
this configuration as its parent, to create a new configuration.

static

Configuration

resolveAndBind

​(

ModuleFinder

before,

List

<

Configuration

> parents,

ModuleFinder

after,

Collection

<

String

> roots)

Resolves a collection of root modules, with service binding, to create
configuration.

String

toString

()

Returns a string describing this configuration.

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

wait

,

wait

,

wait

Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

static

Configuration

empty

()

Returns the

empty

configuration.

Optional

<

ResolvedModule

>

findModule

​(

String

name)

Finds a resolved module in this configuration, or if not in this
configuration, the

parent

configurations.

Set

<

ResolvedModule

>

modules

()

Returns an immutable set of the resolved modules in this configuration.

List

<

Configuration

>

parents

()

Returns an unmodifiable list of this configuration's parents, in search
order.

Configuration

resolve

​(

ModuleFinder

before,

ModuleFinder

after,

Collection

<

String

> roots)

Resolves a collection of root modules, with this configuration as its
parent, to create a new configuration.

static

Configuration

resolve

​(

ModuleFinder

before,

List

<

Configuration

> parents,

ModuleFinder

after,

Collection

<

String

> roots)

Resolves a collection of root modules to create a configuration.

Configuration

resolveAndBind

​(

ModuleFinder

before,

ModuleFinder

after,

Collection

<

String

> roots)

Resolves a collection of root modules, with service binding, and with
this configuration as its parent, to create a new configuration.

static

Configuration

resolveAndBind

​(

ModuleFinder

before,

List

<

Configuration

> parents,

ModuleFinder

after,

Collection

<

String

> roots)

Resolves a collection of root modules, with service binding, to create
configuration.

String

toString

()

Returns a string describing this configuration.

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

wait

,

wait

,

wait

---

#### Method Summary

Returns the

empty

configuration.

Finds a resolved module in this configuration, or if not in this
configuration, the

parent

configurations.

Returns an immutable set of the resolved modules in this configuration.

Returns an unmodifiable list of this configuration's parents, in search
order.

Resolves a collection of root modules, with this configuration as its
parent, to create a new configuration.

Resolves a collection of root modules to create a configuration.

Resolves a collection of root modules, with service binding, and with
this configuration as its parent, to create a new configuration.

Resolves a collection of root modules, with service binding, to create
configuration.

Returns a string describing this configuration.

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

wait

,

wait

,

wait

---

#### Methods declared in class java.lang. Object

============ METHOD DETAIL ==========

- Method Detail

- resolve

```java
public
Configuration
resolve​(
ModuleFinder
before,

ModuleFinder
after,

Collection
<
String
> roots)
```

Resolves a collection of root modules, with this configuration as its
parent, to create a new configuration. This method works exactly as
specified by the static

resolve

method when invoked with this configuration as the parent. In other words,
if this configuration is

cf

then this method is equivalent to
invoking:

```java
Configuration.resolve(before, List.of(cf), after, roots);
```

**Parameters:** before

- The

before

module finder to find modules
**Parameters:** after

- The

after

module finder to locate modules when not
located by the

before

module finder or in parent
configurations
**Parameters:** roots

- The possibly-empty collection of module names of the modules
to resolve
**Returns:** The configuration that is the result of resolving the given
root modules
**Throws:** FindException

- If resolution fails for any of the observability-related reasons
specified by the static

resolve

method
**Throws:** ResolutionException

- If resolution fails any of the consistency checks specified by
the static

resolve

method
**Throws:** SecurityException

- If locating a module is denied by the security manager

- resolveAndBind

```java
public
Configuration
resolveAndBind​(
ModuleFinder
before,

ModuleFinder
after,

Collection
<
String
> roots)
```

Resolves a collection of root modules, with service binding, and with
this configuration as its parent, to create a new configuration.
This method works exactly as specified by the static

resolveAndBind

method when invoked with this configuration
as the parent. In other words, if this configuration is

cf

then
this method is equivalent to invoking:

```java
Configuration.resolveAndBind(before, List.of(cf), after, roots);
```

**Parameters:** before

- The

before

module finder to find modules
**Parameters:** after

- The

after

module finder to locate modules when not
located by the

before

module finder or in parent
configurations
**Parameters:** roots

- The possibly-empty collection of module names of the modules
to resolve
**Returns:** The configuration that is the result of resolving, with service
binding, the given root modules
**Throws:** FindException

- If resolution fails for any of the observability-related reasons
specified by the static

resolve

method
**Throws:** ResolutionException

- If resolution fails any of the consistency checks specified by
the static

resolve

method
**Throws:** SecurityException

- If locating a module is denied by the security manager

- resolve

```java
public static
Configuration
resolve​(
ModuleFinder
before,

List
<
Configuration
> parents,

ModuleFinder
after,

Collection
<
String
> roots)
```

Resolves a collection of root modules to create a configuration.

Each root module is located using the given

before

module
finder. If a module is not found then it is located in the parent
configuration as if by invoking the

findModule

method on each parent in iteration order. If not found then
the module is located using the given

after

module finder. The
same search order is used to locate transitive dependences. Root modules
or dependences that are located in a parent configuration are resolved
no further and are not included in the resulting configuration.

When all modules have been enumerated then a readability graph
is computed, and in conjunction with the module exports and service use,
checked for consistency.

Resolution may fail with

FindException

for the following

observability-related

reasons:

- A root module, or a direct or transitive dependency, is not
found.
- An error occurs when attempting to find a module.
Possible errors include I/O errors, errors detected parsing a module
descriptor (

module-info.class

) or two versions of the same
module are found in the same directory.

Resolution may fail with

ResolutionException

if any of the
following consistency checks fail:

- A cycle is detected, say where module

m1

requires
module

m2

and

m2

requires

m1

.
- A module reads two or more modules with the same name. This
includes the case where a module reads another with the same name as
itself.
- Two or more modules in the configuration export the same
package to a module that reads both. This includes the case where a
module

M

containing package

p

reads another module
that exports

p

to

M

.
- A module

M

declares that it "

uses p.S

" or
"

provides p.S with ...

" but package

p

is neither in
module

M

nor exported to

M

by any module that

M

reads.

**Implementation Note:** In the implementation then observability of modules may depend
on referential integrity or other checks that ensure different builds of
tightly coupled modules or modules for specific operating systems or
architectures are not combined in the same configuration.
**Parameters:** before

- The

before

module finder to find modules
**Parameters:** parents

- The list parent configurations in search order
**Parameters:** after

- The

after

module finder to locate modules when not
located by the

before

module finder or in parent
configurations
**Parameters:** roots

- The possibly-empty collection of module names of the modules
to resolve
**Returns:** The configuration that is the result of resolving the given
root modules
**Throws:** FindException

- If resolution fails for any of observability-related reasons
specified above
**Throws:** ResolutionException

- If resolution fails for any of the consistency checks specified
above
**Throws:** IllegalArgumentException

- If the list of parents is empty, or the list has two or more
parents with modules for different target operating systems,
architectures, or versions
**Throws:** SecurityException

- If locating a module is denied by the security manager

- resolveAndBind

```java
public static
Configuration
resolveAndBind​(
ModuleFinder
before,

List
<
Configuration
> parents,

ModuleFinder
after,

Collection
<
String
> roots)
```

Resolves a collection of root modules, with service binding, to create
configuration.

This method works exactly as specified by

resolve

except that the graph of resolved modules is augmented
with modules induced by the service-use dependence relation.

More specifically, the root modules are
resolved as if by calling

resolve

. The resolved modules, and
all modules in the parent configurations, with

service dependences

are then examined. All modules found by the given
module finders that

provide

an
implementation of one or more of the service types are added to the
module graph and then resolved as if by calling the

resolve

method. Adding modules to the module graph may introduce new
service-use dependences and so the process works iteratively until no
more modules are added.

As service binding involves resolution then it may fail with

FindException

or

ResolutionException

for exactly the same
reasons specified in

resolve

.

**Parameters:** before

- The

before

module finder to find modules
**Parameters:** parents

- The list parent configurations in search order
**Parameters:** after

- The

after

module finder to locate modules when not
located by the

before

module finder or in parent
configurations
**Parameters:** roots

- The possibly-empty collection of module names of the modules
to resolve
**Returns:** The configuration that is the result of resolving, with service
binding, the given root modules
**Throws:** FindException

- If resolution fails for any of the observability-related reasons
specified by the static

resolve

method
**Throws:** ResolutionException

- If resolution fails any of the consistency checks specified by
the static

resolve

method
**Throws:** IllegalArgumentException

- If the list of parents is empty, or the list has two or more
parents with modules for different target operating systems,
architectures, or versions
**Throws:** SecurityException

- If locating a module is denied by the security manager

- empty

```java
public static
Configuration
empty()
```

Returns the

empty

configuration. There are no modules in the
empty configuration. It has no parents.

**Returns:** The empty configuration

- parents

```java
public
List
<
Configuration
> parents()
```

Returns an unmodifiable list of this configuration's parents, in search
order. If this is the

empty configuration

then an
empty list is returned.

**Returns:** A possibly-empty unmodifiable list of this parent configurations

- modules

```java
public
Set
<
ResolvedModule
> modules()
```

Returns an immutable set of the resolved modules in this configuration.

**Returns:** A possibly-empty unmodifiable set of the resolved modules
in this configuration

- findModule

```java
public
Optional
<
ResolvedModule
> findModule​(
String
name)
```

Finds a resolved module in this configuration, or if not in this
configuration, the

parent

configurations.
Finding a module in parent configurations is equivalent to invoking

findModule

on each parent, in search order, until the module
is found or all parents have been searched. In a

tree of
configurations

then this is equivalent to a depth-first search.

**Parameters:** name

- The module name of the resolved module to find
**Returns:** The resolved module with the given name or an empty

Optional

if there isn't a module with this name in this
configuration or any parent configurations

- toString

```java
public
String
toString()
```

Returns a string describing this configuration.

**Overrides:** toString

in class

Object
**Returns:** A possibly empty string describing this configuration

Method Detail

- resolve

```java
public
Configuration
resolve​(
ModuleFinder
before,

ModuleFinder
after,

Collection
<
String
> roots)
```

Resolves a collection of root modules, with this configuration as its
parent, to create a new configuration. This method works exactly as
specified by the static

resolve

method when invoked with this configuration as the parent. In other words,
if this configuration is

cf

then this method is equivalent to
invoking:

```java
Configuration.resolve(before, List.of(cf), after, roots);
```

**Parameters:** before

- The

before

module finder to find modules
**Parameters:** after

- The

after

module finder to locate modules when not
located by the

before

module finder or in parent
configurations
**Parameters:** roots

- The possibly-empty collection of module names of the modules
to resolve
**Returns:** The configuration that is the result of resolving the given
root modules
**Throws:** FindException

- If resolution fails for any of the observability-related reasons
specified by the static

resolve

method
**Throws:** ResolutionException

- If resolution fails any of the consistency checks specified by
the static

resolve

method
**Throws:** SecurityException

- If locating a module is denied by the security manager

- resolveAndBind

```java
public
Configuration
resolveAndBind​(
ModuleFinder
before,

ModuleFinder
after,

Collection
<
String
> roots)
```

Resolves a collection of root modules, with service binding, and with
this configuration as its parent, to create a new configuration.
This method works exactly as specified by the static

resolveAndBind

method when invoked with this configuration
as the parent. In other words, if this configuration is

cf

then
this method is equivalent to invoking:

```java
Configuration.resolveAndBind(before, List.of(cf), after, roots);
```

**Parameters:** before

- The

before

module finder to find modules
**Parameters:** after

- The

after

module finder to locate modules when not
located by the

before

module finder or in parent
configurations
**Parameters:** roots

- The possibly-empty collection of module names of the modules
to resolve
**Returns:** The configuration that is the result of resolving, with service
binding, the given root modules
**Throws:** FindException

- If resolution fails for any of the observability-related reasons
specified by the static

resolve

method
**Throws:** ResolutionException

- If resolution fails any of the consistency checks specified by
the static

resolve

method
**Throws:** SecurityException

- If locating a module is denied by the security manager

- resolve

```java
public static
Configuration
resolve​(
ModuleFinder
before,

List
<
Configuration
> parents,

ModuleFinder
after,

Collection
<
String
> roots)
```

Resolves a collection of root modules to create a configuration.

Each root module is located using the given

before

module
finder. If a module is not found then it is located in the parent
configuration as if by invoking the

findModule

method on each parent in iteration order. If not found then
the module is located using the given

after

module finder. The
same search order is used to locate transitive dependences. Root modules
or dependences that are located in a parent configuration are resolved
no further and are not included in the resulting configuration.

When all modules have been enumerated then a readability graph
is computed, and in conjunction with the module exports and service use,
checked for consistency.

Resolution may fail with

FindException

for the following

observability-related

reasons:

- A root module, or a direct or transitive dependency, is not
found.
- An error occurs when attempting to find a module.
Possible errors include I/O errors, errors detected parsing a module
descriptor (

module-info.class

) or two versions of the same
module are found in the same directory.

Resolution may fail with

ResolutionException

if any of the
following consistency checks fail:

- A cycle is detected, say where module

m1

requires
module

m2

and

m2

requires

m1

.
- A module reads two or more modules with the same name. This
includes the case where a module reads another with the same name as
itself.
- Two or more modules in the configuration export the same
package to a module that reads both. This includes the case where a
module

M

containing package

p

reads another module
that exports

p

to

M

.
- A module

M

declares that it "

uses p.S

" or
"

provides p.S with ...

" but package

p

is neither in
module

M

nor exported to

M

by any module that

M

reads.

**Implementation Note:** In the implementation then observability of modules may depend
on referential integrity or other checks that ensure different builds of
tightly coupled modules or modules for specific operating systems or
architectures are not combined in the same configuration.
**Parameters:** before

- The

before

module finder to find modules
**Parameters:** parents

- The list parent configurations in search order
**Parameters:** after

- The

after

module finder to locate modules when not
located by the

before

module finder or in parent
configurations
**Parameters:** roots

- The possibly-empty collection of module names of the modules
to resolve
**Returns:** The configuration that is the result of resolving the given
root modules
**Throws:** FindException

- If resolution fails for any of observability-related reasons
specified above
**Throws:** ResolutionException

- If resolution fails for any of the consistency checks specified
above
**Throws:** IllegalArgumentException

- If the list of parents is empty, or the list has two or more
parents with modules for different target operating systems,
architectures, or versions
**Throws:** SecurityException

- If locating a module is denied by the security manager

- resolveAndBind

```java
public static
Configuration
resolveAndBind​(
ModuleFinder
before,

List
<
Configuration
> parents,

ModuleFinder
after,

Collection
<
String
> roots)
```

Resolves a collection of root modules, with service binding, to create
configuration.

This method works exactly as specified by

resolve

except that the graph of resolved modules is augmented
with modules induced by the service-use dependence relation.

More specifically, the root modules are
resolved as if by calling

resolve

. The resolved modules, and
all modules in the parent configurations, with

service dependences

are then examined. All modules found by the given
module finders that

provide

an
implementation of one or more of the service types are added to the
module graph and then resolved as if by calling the

resolve

method. Adding modules to the module graph may introduce new
service-use dependences and so the process works iteratively until no
more modules are added.

As service binding involves resolution then it may fail with

FindException

or

ResolutionException

for exactly the same
reasons specified in

resolve

.

**Parameters:** before

- The

before

module finder to find modules
**Parameters:** parents

- The list parent configurations in search order
**Parameters:** after

- The

after

module finder to locate modules when not
located by the

before

module finder or in parent
configurations
**Parameters:** roots

- The possibly-empty collection of module names of the modules
to resolve
**Returns:** The configuration that is the result of resolving, with service
binding, the given root modules
**Throws:** FindException

- If resolution fails for any of the observability-related reasons
specified by the static

resolve

method
**Throws:** ResolutionException

- If resolution fails any of the consistency checks specified by
the static

resolve

method
**Throws:** IllegalArgumentException

- If the list of parents is empty, or the list has two or more
parents with modules for different target operating systems,
architectures, or versions
**Throws:** SecurityException

- If locating a module is denied by the security manager

- empty

```java
public static
Configuration
empty()
```

Returns the

empty

configuration. There are no modules in the
empty configuration. It has no parents.

**Returns:** The empty configuration

- parents

```java
public
List
<
Configuration
> parents()
```

Returns an unmodifiable list of this configuration's parents, in search
order. If this is the

empty configuration

then an
empty list is returned.

**Returns:** A possibly-empty unmodifiable list of this parent configurations

- modules

```java
public
Set
<
ResolvedModule
> modules()
```

Returns an immutable set of the resolved modules in this configuration.

**Returns:** A possibly-empty unmodifiable set of the resolved modules
in this configuration

- findModule

```java
public
Optional
<
ResolvedModule
> findModule​(
String
name)
```

Finds a resolved module in this configuration, or if not in this
configuration, the

parent

configurations.
Finding a module in parent configurations is equivalent to invoking

findModule

on each parent, in search order, until the module
is found or all parents have been searched. In a

tree of
configurations

then this is equivalent to a depth-first search.

**Parameters:** name

- The module name of the resolved module to find
**Returns:** The resolved module with the given name or an empty

Optional

if there isn't a module with this name in this
configuration or any parent configurations

- toString

```java
public
String
toString()
```

Returns a string describing this configuration.

**Overrides:** toString

in class

Object
**Returns:** A possibly empty string describing this configuration

---

#### Method Detail

resolve

```java
public
Configuration
resolve​(
ModuleFinder
before,

ModuleFinder
after,

Collection
<
String
> roots)
```

Resolves a collection of root modules, with this configuration as its
parent, to create a new configuration. This method works exactly as
specified by the static

resolve

method when invoked with this configuration as the parent. In other words,
if this configuration is

cf

then this method is equivalent to
invoking:

```java
Configuration.resolve(before, List.of(cf), after, roots);
```

**Parameters:** before

- The

before

module finder to find modules
**Parameters:** after

- The

after

module finder to locate modules when not
located by the

before

module finder or in parent
configurations
**Parameters:** roots

- The possibly-empty collection of module names of the modules
to resolve
**Returns:** The configuration that is the result of resolving the given
root modules
**Throws:** FindException

- If resolution fails for any of the observability-related reasons
specified by the static

resolve

method
**Throws:** ResolutionException

- If resolution fails any of the consistency checks specified by
the static

resolve

method
**Throws:** SecurityException

- If locating a module is denied by the security manager

---

#### resolve

public

Configuration

resolve​(

ModuleFinder

before,

ModuleFinder

after,

Collection

<

String

> roots)

Resolves a collection of root modules, with this configuration as its
parent, to create a new configuration. This method works exactly as
specified by the static

resolve

method when invoked with this configuration as the parent. In other words,
if this configuration is

cf

then this method is equivalent to
invoking:

```java
Configuration.resolve(before, List.of(cf), after, roots);
```

Configuration.resolve(before, List.of(cf), after, roots);

resolveAndBind

```java
public
Configuration
resolveAndBind​(
ModuleFinder
before,

ModuleFinder
after,

Collection
<
String
> roots)
```

Resolves a collection of root modules, with service binding, and with
this configuration as its parent, to create a new configuration.
This method works exactly as specified by the static

resolveAndBind

method when invoked with this configuration
as the parent. In other words, if this configuration is

cf

then
this method is equivalent to invoking:

```java
Configuration.resolveAndBind(before, List.of(cf), after, roots);
```

**Parameters:** before

- The

before

module finder to find modules
**Parameters:** after

- The

after

module finder to locate modules when not
located by the

before

module finder or in parent
configurations
**Parameters:** roots

- The possibly-empty collection of module names of the modules
to resolve
**Returns:** The configuration that is the result of resolving, with service
binding, the given root modules
**Throws:** FindException

- If resolution fails for any of the observability-related reasons
specified by the static

resolve

method
**Throws:** ResolutionException

- If resolution fails any of the consistency checks specified by
the static

resolve

method
**Throws:** SecurityException

- If locating a module is denied by the security manager

---

#### resolveAndBind

public

Configuration

resolveAndBind​(

ModuleFinder

before,

ModuleFinder

after,

Collection

<

String

> roots)

Resolves a collection of root modules, with service binding, and with
this configuration as its parent, to create a new configuration.
This method works exactly as specified by the static

resolveAndBind

method when invoked with this configuration
as the parent. In other words, if this configuration is

cf

then
this method is equivalent to invoking:

```java
Configuration.resolveAndBind(before, List.of(cf), after, roots);
```

Configuration.resolveAndBind(before, List.of(cf), after, roots);

resolve

```java
public static
Configuration
resolve​(
ModuleFinder
before,

List
<
Configuration
> parents,

ModuleFinder
after,

Collection
<
String
> roots)
```

Resolves a collection of root modules to create a configuration.

Each root module is located using the given

before

module
finder. If a module is not found then it is located in the parent
configuration as if by invoking the

findModule

method on each parent in iteration order. If not found then
the module is located using the given

after

module finder. The
same search order is used to locate transitive dependences. Root modules
or dependences that are located in a parent configuration are resolved
no further and are not included in the resulting configuration.

When all modules have been enumerated then a readability graph
is computed, and in conjunction with the module exports and service use,
checked for consistency.

Resolution may fail with

FindException

for the following

observability-related

reasons:

- A root module, or a direct or transitive dependency, is not
found.
- An error occurs when attempting to find a module.
Possible errors include I/O errors, errors detected parsing a module
descriptor (

module-info.class

) or two versions of the same
module are found in the same directory.

Resolution may fail with

ResolutionException

if any of the
following consistency checks fail:

- A cycle is detected, say where module

m1

requires
module

m2

and

m2

requires

m1

.
- A module reads two or more modules with the same name. This
includes the case where a module reads another with the same name as
itself.
- Two or more modules in the configuration export the same
package to a module that reads both. This includes the case where a
module

M

containing package

p

reads another module
that exports

p

to

M

.
- A module

M

declares that it "

uses p.S

" or
"

provides p.S with ...

" but package

p

is neither in
module

M

nor exported to

M

by any module that

M

reads.

**Implementation Note:** In the implementation then observability of modules may depend
on referential integrity or other checks that ensure different builds of
tightly coupled modules or modules for specific operating systems or
architectures are not combined in the same configuration.
**Parameters:** before

- The

before

module finder to find modules
**Parameters:** parents

- The list parent configurations in search order
**Parameters:** after

- The

after

module finder to locate modules when not
located by the

before

module finder or in parent
configurations
**Parameters:** roots

- The possibly-empty collection of module names of the modules
to resolve
**Returns:** The configuration that is the result of resolving the given
root modules
**Throws:** FindException

- If resolution fails for any of observability-related reasons
specified above
**Throws:** ResolutionException

- If resolution fails for any of the consistency checks specified
above
**Throws:** IllegalArgumentException

- If the list of parents is empty, or the list has two or more
parents with modules for different target operating systems,
architectures, or versions
**Throws:** SecurityException

- If locating a module is denied by the security manager

---

#### resolve

public static

Configuration

resolve​(

ModuleFinder

before,

List

<

Configuration

> parents,

ModuleFinder

after,

Collection

<

String

> roots)

Resolves a collection of root modules to create a configuration.

Each root module is located using the given

before

module
finder. If a module is not found then it is located in the parent
configuration as if by invoking the

findModule

method on each parent in iteration order. If not found then
the module is located using the given

after

module finder. The
same search order is used to locate transitive dependences. Root modules
or dependences that are located in a parent configuration are resolved
no further and are not included in the resulting configuration.

When all modules have been enumerated then a readability graph
is computed, and in conjunction with the module exports and service use,
checked for consistency.

Resolution may fail with

FindException

for the following

observability-related

reasons:

- A root module, or a direct or transitive dependency, is not
found.
- An error occurs when attempting to find a module.
Possible errors include I/O errors, errors detected parsing a module
descriptor (

module-info.class

) or two versions of the same
module are found in the same directory.

Resolution may fail with

ResolutionException

if any of the
following consistency checks fail:

- A cycle is detected, say where module

m1

requires
module

m2

and

m2

requires

m1

.
- A module reads two or more modules with the same name. This
includes the case where a module reads another with the same name as
itself.
- Two or more modules in the configuration export the same
package to a module that reads both. This includes the case where a
module

M

containing package

p

reads another module
that exports

p

to

M

.
- A module

M

declares that it "

uses p.S

" or
"

provides p.S with ...

" but package

p

is neither in
module

M

nor exported to

M

by any module that

M

reads.

Each root module is located using the given

before

module
finder. If a module is not found then it is located in the parent
configuration as if by invoking the

findModule

method on each parent in iteration order. If not found then
the module is located using the given

after

module finder. The
same search order is used to locate transitive dependences. Root modules
or dependences that are located in a parent configuration are resolved
no further and are not included in the resulting configuration.

When all modules have been enumerated then a readability graph
is computed, and in conjunction with the module exports and service use,
checked for consistency.

Resolution may fail with

FindException

for the following

observability-related

reasons:

A root module, or a direct or transitive dependency, is not
found.

An error occurs when attempting to find a module.
Possible errors include I/O errors, errors detected parsing a module
descriptor (

module-info.class

) or two versions of the same
module are found in the same directory.

A root module, or a direct or transitive dependency, is not
found.

An error occurs when attempting to find a module.
Possible errors include I/O errors, errors detected parsing a module
descriptor (

module-info.class

) or two versions of the same
module are found in the same directory.

Resolution may fail with

ResolutionException

if any of the
following consistency checks fail:

A cycle is detected, say where module

m1

requires
module

m2

and

m2

requires

m1

.

A module reads two or more modules with the same name. This
includes the case where a module reads another with the same name as
itself.

Two or more modules in the configuration export the same
package to a module that reads both. This includes the case where a
module

M

containing package

p

reads another module
that exports

p

to

M

.

A module

M

declares that it "

uses p.S

" or
"

provides p.S with ...

" but package

p

is neither in
module

M

nor exported to

M

by any module that

M

reads.

A cycle is detected, say where module

m1

requires
module

m2

and

m2

requires

m1

.

A module reads two or more modules with the same name. This
includes the case where a module reads another with the same name as
itself.

Two or more modules in the configuration export the same
package to a module that reads both. This includes the case where a
module

M

containing package

p

reads another module
that exports

p

to

M

.

A module

M

declares that it "

uses p.S

" or
"

provides p.S with ...

" but package

p

is neither in
module

M

nor exported to

M

by any module that

M

reads.

resolveAndBind

```java
public static
Configuration
resolveAndBind​(
ModuleFinder
before,

List
<
Configuration
> parents,

ModuleFinder
after,

Collection
<
String
> roots)
```

Resolves a collection of root modules, with service binding, to create
configuration.

This method works exactly as specified by

resolve

except that the graph of resolved modules is augmented
with modules induced by the service-use dependence relation.

More specifically, the root modules are
resolved as if by calling

resolve

. The resolved modules, and
all modules in the parent configurations, with

service dependences

are then examined. All modules found by the given
module finders that

provide

an
implementation of one or more of the service types are added to the
module graph and then resolved as if by calling the

resolve

method. Adding modules to the module graph may introduce new
service-use dependences and so the process works iteratively until no
more modules are added.

As service binding involves resolution then it may fail with

FindException

or

ResolutionException

for exactly the same
reasons specified in

resolve

.

**Parameters:** before

- The

before

module finder to find modules
**Parameters:** parents

- The list parent configurations in search order
**Parameters:** after

- The

after

module finder to locate modules when not
located by the

before

module finder or in parent
configurations
**Parameters:** roots

- The possibly-empty collection of module names of the modules
to resolve
**Returns:** The configuration that is the result of resolving, with service
binding, the given root modules
**Throws:** FindException

- If resolution fails for any of the observability-related reasons
specified by the static

resolve

method
**Throws:** ResolutionException

- If resolution fails any of the consistency checks specified by
the static

resolve

method
**Throws:** IllegalArgumentException

- If the list of parents is empty, or the list has two or more
parents with modules for different target operating systems,
architectures, or versions
**Throws:** SecurityException

- If locating a module is denied by the security manager

---

#### resolveAndBind

public static

Configuration

resolveAndBind​(

ModuleFinder

before,

List

<

Configuration

> parents,

ModuleFinder

after,

Collection

<

String

> roots)

Resolves a collection of root modules, with service binding, to create
configuration.

This method works exactly as specified by

resolve

except that the graph of resolved modules is augmented
with modules induced by the service-use dependence relation.

More specifically, the root modules are
resolved as if by calling

resolve

. The resolved modules, and
all modules in the parent configurations, with

service dependences

are then examined. All modules found by the given
module finders that

provide

an
implementation of one or more of the service types are added to the
module graph and then resolved as if by calling the

resolve

method. Adding modules to the module graph may introduce new
service-use dependences and so the process works iteratively until no
more modules are added.

As service binding involves resolution then it may fail with

FindException

or

ResolutionException

for exactly the same
reasons specified in

resolve

.

This method works exactly as specified by

resolve

except that the graph of resolved modules is augmented
with modules induced by the service-use dependence relation.

More specifically, the root modules are
resolved as if by calling

resolve

. The resolved modules, and
all modules in the parent configurations, with

service dependences

are then examined. All modules found by the given
module finders that

provide

an
implementation of one or more of the service types are added to the
module graph and then resolved as if by calling the

resolve

method. Adding modules to the module graph may introduce new
service-use dependences and so the process works iteratively until no
more modules are added.

As service binding involves resolution then it may fail with

FindException

or

ResolutionException

for exactly the same
reasons specified in

resolve

.

empty

```java
public static
Configuration
empty()
```

Returns the

empty

configuration. There are no modules in the
empty configuration. It has no parents.

**Returns:** The empty configuration

---

#### empty

public static

Configuration

empty()

Returns the

empty

configuration. There are no modules in the
empty configuration. It has no parents.

parents

```java
public
List
<
Configuration
> parents()
```

Returns an unmodifiable list of this configuration's parents, in search
order. If this is the

empty configuration

then an
empty list is returned.

**Returns:** A possibly-empty unmodifiable list of this parent configurations

---

#### parents

public

List

<

Configuration

> parents()

Returns an unmodifiable list of this configuration's parents, in search
order. If this is the

empty configuration

then an
empty list is returned.

modules

```java
public
Set
<
ResolvedModule
> modules()
```

Returns an immutable set of the resolved modules in this configuration.

**Returns:** A possibly-empty unmodifiable set of the resolved modules
in this configuration

---

#### modules

public

Set

<

ResolvedModule

> modules()

Returns an immutable set of the resolved modules in this configuration.

findModule

```java
public
Optional
<
ResolvedModule
> findModule​(
String
name)
```

Finds a resolved module in this configuration, or if not in this
configuration, the

parent

configurations.
Finding a module in parent configurations is equivalent to invoking

findModule

on each parent, in search order, until the module
is found or all parents have been searched. In a

tree of
configurations

then this is equivalent to a depth-first search.

**Parameters:** name

- The module name of the resolved module to find
**Returns:** The resolved module with the given name or an empty

Optional

if there isn't a module with this name in this
configuration or any parent configurations

---

#### findModule

public

Optional

<

ResolvedModule

> findModule​(

String

name)

Finds a resolved module in this configuration, or if not in this
configuration, the

parent

configurations.
Finding a module in parent configurations is equivalent to invoking

findModule

on each parent, in search order, until the module
is found or all parents have been searched. In a

tree of
configurations

then this is equivalent to a depth-first search.

toString

```java
public
String
toString()
```

Returns a string describing this configuration.

**Overrides:** toString

in class

Object
**Returns:** A possibly empty string describing this configuration

---

#### toString

public

String

toString()

Returns a string describing this configuration.

---

