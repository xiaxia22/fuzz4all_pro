# Interface StateFactory

**Source:** `java.naming\javax\naming\spi\StateFactory.html`

### Class Description

```java
public interface
StateFactory
```

This interface represents a factory for obtaining the state of an
object for binding.

The JNDI framework allows for object implementations to
be loaded in dynamically via

object factories

.
For example, when looking up a printer bound in the name space,
if the print service binds printer names to

Reference

s, the printer

Reference

could be used to create a printer object, so that
the caller of lookup can directly operate on the printer object
after the lookup.

An

ObjectFactory

is responsible
for creating objects of a specific type. In the above example,
you may have a

PrinterObjectFactory

for creating

Printer

objects.

For the reverse process, when an object is bound into the namespace,
JNDI provides

state factories

.
Continuing with the printer example, suppose the printer object is
updated and rebound:

```java
ctx.rebind("inky", printer);
```

The service provider for

ctx

uses a state factory
to obtain the state of

printer

for binding into its namespace.
A state factory for the

Printer

type object might return
a more compact object for storage in the naming system.

A state factory must implement the

StateFactory

interface.
In addition, the factory class must be public and must have a
public constructor that accepts no parameters.
Note that in cases where the factory is in a named module then it must be
in a package which is exported by that module to the

java.naming

module.

The

getStateToBind()

method of a state factory may
be invoked multiple times, possibly using different parameters.
The implementation is thread-safe.

StateFactory

is intended for use with service providers
that implement only the

Context

interface.

DirStateFactory

is intended for use with service providers
that implement the

DirContext

interface.

**All Known Subinterfaces:** DirStateFactory

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### Object
getStateToBind​(
Object
obj,

Name
name,

Context
nameCtx,

Hashtable
<?,​?> environment)
throws
NamingException

Retrieves the state of an object for binding.

NamingManager.getStateToBind()

successively loads in state factories and invokes this method
on them until one produces a non-null answer.

DirectoryManager.getStateToBind()

successively loads in state factories. If a factory implements

DirStateFactory

, then

DirectoryManager

invokes

DirStateFactory.getStateToBind()

; otherwise
it invokes

StateFactory.getStateToBind()

.

When an exception
is thrown by a factory, the exception is passed on to the caller
of

NamingManager.getStateToBind()

and

DirectoryManager.getStateToBind()

.
The search for other factories
that may produce a non-null answer is halted.
A factory should only throw an exception if it is sure that
it is the only intended factory and that no other factories
should be tried.
If this factory cannot create an object using the arguments supplied,
it should return null.

The

name

and

nameCtx

parameters may
optionally be used to specify the name of the object being created.
See the description of "Name and Context Parameters" in

ObjectFactory.getObjectInstance()

for details.
If a factory uses

nameCtx

it should synchronize its use
against concurrent access, since context implementations are not
guaranteed to be thread-safe.

The

name

and

environment

parameters
are owned by the caller.
The implementation will not modify these objects or keep references
to them, although it may keep references to clones or copies.

**Parameters:**
- obj

- A non-null object whose state is to be retrieved.
- name

- The name of this object relative to

nameCtx

,
or null if no name is specified.
- nameCtx

- The context relative to which the

name

parameter is specified, or null if

name

is
relative to the default initial context.
- environment

- The possibly null environment to
be used in the creation of the object's state.

**Returns:**
- The object's state for binding;
null if the factory is not returning any changes.

**Throws:**
- NamingException

- if this factory encountered an exception
while attempting to get the object's state, and no other factories are
to be tried.

**See Also:**
- NamingManager.getStateToBind(java.lang.Object, javax.naming.Name, javax.naming.Context, java.util.Hashtable<?, ?>)

,

DirectoryManager.getStateToBind(java.lang.Object, javax.naming.Name, javax.naming.Context, java.util.Hashtable<?, ?>, javax.naming.directory.Attributes)

---

### Additional Sections

#### Interface StateFactory

**All Known Subinterfaces:** DirStateFactory

```java
public interface
StateFactory
```

This interface represents a factory for obtaining the state of an
object for binding.

The JNDI framework allows for object implementations to
be loaded in dynamically via

object factories

.
For example, when looking up a printer bound in the name space,
if the print service binds printer names to

Reference

s, the printer

Reference

could be used to create a printer object, so that
the caller of lookup can directly operate on the printer object
after the lookup.

An

ObjectFactory

is responsible
for creating objects of a specific type. In the above example,
you may have a

PrinterObjectFactory

for creating

Printer

objects.

For the reverse process, when an object is bound into the namespace,
JNDI provides

state factories

.
Continuing with the printer example, suppose the printer object is
updated and rebound:

```java
ctx.rebind("inky", printer);
```

The service provider for

ctx

uses a state factory
to obtain the state of

printer

for binding into its namespace.
A state factory for the

Printer

type object might return
a more compact object for storage in the naming system.

A state factory must implement the

StateFactory

interface.
In addition, the factory class must be public and must have a
public constructor that accepts no parameters.
Note that in cases where the factory is in a named module then it must be
in a package which is exported by that module to the

java.naming

module.

The

getStateToBind()

method of a state factory may
be invoked multiple times, possibly using different parameters.
The implementation is thread-safe.

StateFactory

is intended for use with service providers
that implement only the

Context

interface.

DirStateFactory

is intended for use with service providers
that implement the

DirContext

interface.

**Since:** 1.3
**See Also:** NamingManager.getStateToBind(java.lang.Object, javax.naming.Name, javax.naming.Context, java.util.Hashtable<?, ?>)

,

DirectoryManager.getStateToBind(java.lang.Object, javax.naming.Name, javax.naming.Context, java.util.Hashtable<?, ?>, javax.naming.directory.Attributes)

,

ObjectFactory

,

DirStateFactory

public interface

StateFactory

This interface represents a factory for obtaining the state of an
object for binding.

The JNDI framework allows for object implementations to
be loaded in dynamically via

object factories

.
For example, when looking up a printer bound in the name space,
if the print service binds printer names to

Reference

s, the printer

Reference

could be used to create a printer object, so that
the caller of lookup can directly operate on the printer object
after the lookup.

An

ObjectFactory

is responsible
for creating objects of a specific type. In the above example,
you may have a

PrinterObjectFactory

for creating

Printer

objects.

For the reverse process, when an object is bound into the namespace,
JNDI provides

state factories

.
Continuing with the printer example, suppose the printer object is
updated and rebound:

```java
ctx.rebind("inky", printer);
```

The service provider for

ctx

uses a state factory
to obtain the state of

printer

for binding into its namespace.
A state factory for the

Printer

type object might return
a more compact object for storage in the naming system.

A state factory must implement the

StateFactory

interface.
In addition, the factory class must be public and must have a
public constructor that accepts no parameters.
Note that in cases where the factory is in a named module then it must be
in a package which is exported by that module to the

java.naming

module.

The

getStateToBind()

method of a state factory may
be invoked multiple times, possibly using different parameters.
The implementation is thread-safe.

StateFactory

is intended for use with service providers
that implement only the

Context

interface.

DirStateFactory

is intended for use with service providers
that implement the

DirContext

interface.

The JNDI framework allows for object implementations to
be loaded in dynamically via

object factories

.
For example, when looking up a printer bound in the name space,
if the print service binds printer names to

Reference

s, the printer

Reference

could be used to create a printer object, so that
the caller of lookup can directly operate on the printer object
after the lookup.

An

ObjectFactory

is responsible
for creating objects of a specific type. In the above example,
you may have a

PrinterObjectFactory

for creating

Printer

objects.

For the reverse process, when an object is bound into the namespace,
JNDI provides

state factories

.
Continuing with the printer example, suppose the printer object is
updated and rebound:

```java
ctx.rebind("inky", printer);
```

The service provider for

ctx

uses a state factory
to obtain the state of

printer

for binding into its namespace.
A state factory for the

Printer

type object might return
a more compact object for storage in the naming system.

A state factory must implement the

StateFactory

interface.
In addition, the factory class must be public and must have a
public constructor that accepts no parameters.
Note that in cases where the factory is in a named module then it must be
in a package which is exported by that module to the

java.naming

module.

The

getStateToBind()

method of a state factory may
be invoked multiple times, possibly using different parameters.
The implementation is thread-safe.

StateFactory

is intended for use with service providers
that implement only the

Context

interface.

DirStateFactory

is intended for use with service providers
that implement the

DirContext

interface.

An

ObjectFactory

is responsible
for creating objects of a specific type. In the above example,
you may have a

PrinterObjectFactory

for creating

Printer

objects.

For the reverse process, when an object is bound into the namespace,
JNDI provides

state factories

.
Continuing with the printer example, suppose the printer object is
updated and rebound:

```java
ctx.rebind("inky", printer);
```

The service provider for

ctx

uses a state factory
to obtain the state of

printer

for binding into its namespace.
A state factory for the

Printer

type object might return
a more compact object for storage in the naming system.

A state factory must implement the

StateFactory

interface.
In addition, the factory class must be public and must have a
public constructor that accepts no parameters.
Note that in cases where the factory is in a named module then it must be
in a package which is exported by that module to the

java.naming

module.

The

getStateToBind()

method of a state factory may
be invoked multiple times, possibly using different parameters.
The implementation is thread-safe.

StateFactory

is intended for use with service providers
that implement only the

Context

interface.

DirStateFactory

is intended for use with service providers
that implement the

DirContext

interface.

For the reverse process, when an object is bound into the namespace,
JNDI provides

state factories

.
Continuing with the printer example, suppose the printer object is
updated and rebound:

```java
ctx.rebind("inky", printer);
```

The service provider for

ctx

uses a state factory
to obtain the state of

printer

for binding into its namespace.
A state factory for the

Printer

type object might return
a more compact object for storage in the naming system.

A state factory must implement the

StateFactory

interface.
In addition, the factory class must be public and must have a
public constructor that accepts no parameters.
Note that in cases where the factory is in a named module then it must be
in a package which is exported by that module to the

java.naming

module.

The

getStateToBind()

method of a state factory may
be invoked multiple times, possibly using different parameters.
The implementation is thread-safe.

StateFactory

is intended for use with service providers
that implement only the

Context

interface.

DirStateFactory

is intended for use with service providers
that implement the

DirContext

interface.

ctx.rebind("inky", printer);

A state factory must implement the

StateFactory

interface.
In addition, the factory class must be public and must have a
public constructor that accepts no parameters.
Note that in cases where the factory is in a named module then it must be
in a package which is exported by that module to the

java.naming

module.

The

getStateToBind()

method of a state factory may
be invoked multiple times, possibly using different parameters.
The implementation is thread-safe.

StateFactory

is intended for use with service providers
that implement only the

Context

interface.

DirStateFactory

is intended for use with service providers
that implement the

DirContext

interface.

The

getStateToBind()

method of a state factory may
be invoked multiple times, possibly using different parameters.
The implementation is thread-safe.

StateFactory

is intended for use with service providers
that implement only the

Context

interface.

DirStateFactory

is intended for use with service providers
that implement the

DirContext

interface.

StateFactory

is intended for use with service providers
that implement only the

Context

interface.

DirStateFactory

is intended for use with service providers
that implement the

DirContext

interface.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

Object

getStateToBind

​(

Object

obj,

Name

name,

Context

nameCtx,

Hashtable

<?,​?> environment)

Retrieves the state of an object for binding.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

Object

getStateToBind

​(

Object

obj,

Name

name,

Context

nameCtx,

Hashtable

<?,​?> environment)

Retrieves the state of an object for binding.

---

#### Method Summary

Retrieves the state of an object for binding.

============ METHOD DETAIL ==========

- Method Detail

- getStateToBind

```java
Object
getStateToBind​(
Object
obj,

Name
name,

Context
nameCtx,

Hashtable
<?,​?> environment)
throws
NamingException
```

Retrieves the state of an object for binding.

NamingManager.getStateToBind()

successively loads in state factories and invokes this method
on them until one produces a non-null answer.

DirectoryManager.getStateToBind()

successively loads in state factories. If a factory implements

DirStateFactory

, then

DirectoryManager

invokes

DirStateFactory.getStateToBind()

; otherwise
it invokes

StateFactory.getStateToBind()

.

When an exception
is thrown by a factory, the exception is passed on to the caller
of

NamingManager.getStateToBind()

and

DirectoryManager.getStateToBind()

.
The search for other factories
that may produce a non-null answer is halted.
A factory should only throw an exception if it is sure that
it is the only intended factory and that no other factories
should be tried.
If this factory cannot create an object using the arguments supplied,
it should return null.

The

name

and

nameCtx

parameters may
optionally be used to specify the name of the object being created.
See the description of "Name and Context Parameters" in

ObjectFactory.getObjectInstance()

for details.
If a factory uses

nameCtx

it should synchronize its use
against concurrent access, since context implementations are not
guaranteed to be thread-safe.

The

name

and

environment

parameters
are owned by the caller.
The implementation will not modify these objects or keep references
to them, although it may keep references to clones or copies.

**Parameters:** obj

- A non-null object whose state is to be retrieved.
**Parameters:** name

- The name of this object relative to

nameCtx

,
or null if no name is specified.
**Parameters:** nameCtx

- The context relative to which the

name

parameter is specified, or null if

name

is
relative to the default initial context.
**Parameters:** environment

- The possibly null environment to
be used in the creation of the object's state.
**Returns:** The object's state for binding;
null if the factory is not returning any changes.
**Throws:** NamingException

- if this factory encountered an exception
while attempting to get the object's state, and no other factories are
to be tried.
**See Also:** NamingManager.getStateToBind(java.lang.Object, javax.naming.Name, javax.naming.Context, java.util.Hashtable<?, ?>)

,

DirectoryManager.getStateToBind(java.lang.Object, javax.naming.Name, javax.naming.Context, java.util.Hashtable<?, ?>, javax.naming.directory.Attributes)

Method Detail

- getStateToBind

```java
Object
getStateToBind​(
Object
obj,

Name
name,

Context
nameCtx,

Hashtable
<?,​?> environment)
throws
NamingException
```

Retrieves the state of an object for binding.

NamingManager.getStateToBind()

successively loads in state factories and invokes this method
on them until one produces a non-null answer.

DirectoryManager.getStateToBind()

successively loads in state factories. If a factory implements

DirStateFactory

, then

DirectoryManager

invokes

DirStateFactory.getStateToBind()

; otherwise
it invokes

StateFactory.getStateToBind()

.

When an exception
is thrown by a factory, the exception is passed on to the caller
of

NamingManager.getStateToBind()

and

DirectoryManager.getStateToBind()

.
The search for other factories
that may produce a non-null answer is halted.
A factory should only throw an exception if it is sure that
it is the only intended factory and that no other factories
should be tried.
If this factory cannot create an object using the arguments supplied,
it should return null.

The

name

and

nameCtx

parameters may
optionally be used to specify the name of the object being created.
See the description of "Name and Context Parameters" in

ObjectFactory.getObjectInstance()

for details.
If a factory uses

nameCtx

it should synchronize its use
against concurrent access, since context implementations are not
guaranteed to be thread-safe.

The

name

and

environment

parameters
are owned by the caller.
The implementation will not modify these objects or keep references
to them, although it may keep references to clones or copies.

**Parameters:** obj

- A non-null object whose state is to be retrieved.
**Parameters:** name

- The name of this object relative to

nameCtx

,
or null if no name is specified.
**Parameters:** nameCtx

- The context relative to which the

name

parameter is specified, or null if

name

is
relative to the default initial context.
**Parameters:** environment

- The possibly null environment to
be used in the creation of the object's state.
**Returns:** The object's state for binding;
null if the factory is not returning any changes.
**Throws:** NamingException

- if this factory encountered an exception
while attempting to get the object's state, and no other factories are
to be tried.
**See Also:** NamingManager.getStateToBind(java.lang.Object, javax.naming.Name, javax.naming.Context, java.util.Hashtable<?, ?>)

,

DirectoryManager.getStateToBind(java.lang.Object, javax.naming.Name, javax.naming.Context, java.util.Hashtable<?, ?>, javax.naming.directory.Attributes)

---

#### Method Detail

getStateToBind

```java
Object
getStateToBind​(
Object
obj,

Name
name,

Context
nameCtx,

Hashtable
<?,​?> environment)
throws
NamingException
```

Retrieves the state of an object for binding.

NamingManager.getStateToBind()

successively loads in state factories and invokes this method
on them until one produces a non-null answer.

DirectoryManager.getStateToBind()

successively loads in state factories. If a factory implements

DirStateFactory

, then

DirectoryManager

invokes

DirStateFactory.getStateToBind()

; otherwise
it invokes

StateFactory.getStateToBind()

.

When an exception
is thrown by a factory, the exception is passed on to the caller
of

NamingManager.getStateToBind()

and

DirectoryManager.getStateToBind()

.
The search for other factories
that may produce a non-null answer is halted.
A factory should only throw an exception if it is sure that
it is the only intended factory and that no other factories
should be tried.
If this factory cannot create an object using the arguments supplied,
it should return null.

The

name

and

nameCtx

parameters may
optionally be used to specify the name of the object being created.
See the description of "Name and Context Parameters" in

ObjectFactory.getObjectInstance()

for details.
If a factory uses

nameCtx

it should synchronize its use
against concurrent access, since context implementations are not
guaranteed to be thread-safe.

The

name

and

environment

parameters
are owned by the caller.
The implementation will not modify these objects or keep references
to them, although it may keep references to clones or copies.

**Parameters:** obj

- A non-null object whose state is to be retrieved.
**Parameters:** name

- The name of this object relative to

nameCtx

,
or null if no name is specified.
**Parameters:** nameCtx

- The context relative to which the

name

parameter is specified, or null if

name

is
relative to the default initial context.
**Parameters:** environment

- The possibly null environment to
be used in the creation of the object's state.
**Returns:** The object's state for binding;
null if the factory is not returning any changes.
**Throws:** NamingException

- if this factory encountered an exception
while attempting to get the object's state, and no other factories are
to be tried.
**See Also:** NamingManager.getStateToBind(java.lang.Object, javax.naming.Name, javax.naming.Context, java.util.Hashtable<?, ?>)

,

DirectoryManager.getStateToBind(java.lang.Object, javax.naming.Name, javax.naming.Context, java.util.Hashtable<?, ?>, javax.naming.directory.Attributes)

---

#### getStateToBind

Object

getStateToBind​(

Object

obj,

Name

name,

Context

nameCtx,

Hashtable

<?,​?> environment)
throws

NamingException

Retrieves the state of an object for binding.

NamingManager.getStateToBind()

successively loads in state factories and invokes this method
on them until one produces a non-null answer.

DirectoryManager.getStateToBind()

successively loads in state factories. If a factory implements

DirStateFactory

, then

DirectoryManager

invokes

DirStateFactory.getStateToBind()

; otherwise
it invokes

StateFactory.getStateToBind()

.

When an exception
is thrown by a factory, the exception is passed on to the caller
of

NamingManager.getStateToBind()

and

DirectoryManager.getStateToBind()

.
The search for other factories
that may produce a non-null answer is halted.
A factory should only throw an exception if it is sure that
it is the only intended factory and that no other factories
should be tried.
If this factory cannot create an object using the arguments supplied,
it should return null.

The

name

and

nameCtx

parameters may
optionally be used to specify the name of the object being created.
See the description of "Name and Context Parameters" in

ObjectFactory.getObjectInstance()

for details.
If a factory uses

nameCtx

it should synchronize its use
against concurrent access, since context implementations are not
guaranteed to be thread-safe.

The

name

and

environment

parameters
are owned by the caller.
The implementation will not modify these objects or keep references
to them, although it may keep references to clones or copies.

NamingManager.getStateToBind()

successively loads in state factories and invokes this method
on them until one produces a non-null answer.

DirectoryManager.getStateToBind()

successively loads in state factories. If a factory implements

DirStateFactory

, then

DirectoryManager

invokes

DirStateFactory.getStateToBind()

; otherwise
it invokes

StateFactory.getStateToBind()

.

When an exception
is thrown by a factory, the exception is passed on to the caller
of

NamingManager.getStateToBind()

and

DirectoryManager.getStateToBind()

.
The search for other factories
that may produce a non-null answer is halted.
A factory should only throw an exception if it is sure that
it is the only intended factory and that no other factories
should be tried.
If this factory cannot create an object using the arguments supplied,
it should return null.

The

name

and

nameCtx

parameters may
optionally be used to specify the name of the object being created.
See the description of "Name and Context Parameters" in

ObjectFactory.getObjectInstance()

for details.
If a factory uses

nameCtx

it should synchronize its use
against concurrent access, since context implementations are not
guaranteed to be thread-safe.

The

name

and

environment

parameters
are owned by the caller.
The implementation will not modify these objects or keep references
to them, although it may keep references to clones or copies.

When an exception
is thrown by a factory, the exception is passed on to the caller
of

NamingManager.getStateToBind()

and

DirectoryManager.getStateToBind()

.
The search for other factories
that may produce a non-null answer is halted.
A factory should only throw an exception if it is sure that
it is the only intended factory and that no other factories
should be tried.
If this factory cannot create an object using the arguments supplied,
it should return null.

The

name

and

nameCtx

parameters may
optionally be used to specify the name of the object being created.
See the description of "Name and Context Parameters" in

ObjectFactory.getObjectInstance()

for details.
If a factory uses

nameCtx

it should synchronize its use
against concurrent access, since context implementations are not
guaranteed to be thread-safe.

The

name

and

environment

parameters
are owned by the caller.
The implementation will not modify these objects or keep references
to them, although it may keep references to clones or copies.

The

name

and

nameCtx

parameters may
optionally be used to specify the name of the object being created.
See the description of "Name and Context Parameters" in

ObjectFactory.getObjectInstance()

for details.
If a factory uses

nameCtx

it should synchronize its use
against concurrent access, since context implementations are not
guaranteed to be thread-safe.

The

name

and

environment

parameters
are owned by the caller.
The implementation will not modify these objects or keep references
to them, although it may keep references to clones or copies.

The

name

and

environment

parameters
are owned by the caller.
The implementation will not modify these objects or keep references
to them, although it may keep references to clones or copies.

---

