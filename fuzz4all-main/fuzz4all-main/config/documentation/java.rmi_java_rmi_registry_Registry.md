# Interface Registry

**Source:** `java.rmi\java\rmi\registry\Registry.html`

### Class Description

```java
public interface
Registry

extends
Remote
```

Registry

is a remote interface to a simple remote
object registry that provides methods for storing and retrieving
remote object references bound with arbitrary string names. The

bind

,

unbind

, and

rebind

methods are used to alter the name bindings in the registry, and
the

lookup

and

list

methods are used to
query the current name bindings.

In its typical usage, a

Registry

enables RMI client
bootstrapping: it provides a simple means for a client to obtain an
initial reference to a remote object. Therefore, a registry's
remote object implementation is typically exported with a
well-known address, such as with a well-known

ObjID

and TCP port number
(default is

1099

).

The

LocateRegistry

class provides a programmatic API for
constructing a bootstrap reference to a

Registry

at a
remote address (see the static

getRegistry

methods)
and for creating and exporting a

Registry

in the
current VM on a particular local address (see the static

createRegistry

methods).

A

Registry

implementation may choose to restrict
access to some or all of its methods (for example, methods that
mutate the registry's bindings may be restricted to calls
originating from the local host). If a

Registry

method chooses to deny access for a given invocation, its
implementation may throw

AccessException

, which
(because it extends

RemoteException

) will be
wrapped in a

ServerException

when caught by a
remote client.

The names used for bindings in a

Registry

are pure
strings, not parsed. A service which stores its remote reference
in a

Registry

may wish to use a package name as a
prefix in the name binding to reduce the likelihood of name
collisions in the registry.

**All Superinterfaces:** Remote

---

### Field Details

#### static final int REGISTRY_PORT

Well known port for registry.

**See Also:**
- Constant Field Values

---

### Constructor Details

*No entries found.*

### Method Details

#### Remote
lookup​(
String
name)
throws
RemoteException
,

NotBoundException
,

AccessException

Returns the remote reference bound to the specified

name

in this registry.

**Parameters:**
- name

- the name for the remote reference to look up

**Returns:**
- a reference to a remote object

**Throws:**
- NotBoundException

- if

name

is not currently bound
- RemoteException

- if remote communication with the
registry failed; if exception is a

ServerException

containing an

AccessException

, then the registry
denies the caller access to perform this operation
- AccessException

- if this registry is local and it denies
the caller access to perform this operation
- NullPointerException

- if

name

is

null

---

#### void bind​(
String
name,

Remote
obj)
throws
RemoteException
,

AlreadyBoundException
,

AccessException

Binds a remote reference to the specified

name

in
this registry.

**Parameters:**
- name

- the name to associate with the remote reference
- obj

- a reference to a remote object (usually a stub)

**Throws:**
- AlreadyBoundException

- if

name

is already bound
- RemoteException

- if remote communication with the
registry failed; if exception is a

ServerException

containing an

AccessException

, then the registry
denies the caller access to perform this operation (if
originating from a non-local host, for example)
- AccessException

- if this registry is local and it denies
the caller access to perform this operation
- NullPointerException

- if

name

is

null

, or if

obj

is

null

---

#### void unbind​(
String
name)
throws
RemoteException
,

NotBoundException
,

AccessException

Removes the binding for the specified

name

in
this registry.

**Parameters:**
- name

- the name of the binding to remove

**Throws:**
- NotBoundException

- if

name

is not currently bound
- RemoteException

- if remote communication with the
registry failed; if exception is a

ServerException

containing an

AccessException

, then the registry
denies the caller access to perform this operation (if
originating from a non-local host, for example)
- AccessException

- if this registry is local and it denies
the caller access to perform this operation
- NullPointerException

- if

name

is

null

---

#### void rebind​(
String
name,

Remote
obj)
throws
RemoteException
,

AccessException

Replaces the binding for the specified

name

in
this registry with the supplied remote reference. If there is
an existing binding for the specified

name

, it is
discarded.

**Parameters:**
- name

- the name to associate with the remote reference
- obj

- a reference to a remote object (usually a stub)

**Throws:**
- RemoteException

- if remote communication with the
registry failed; if exception is a

ServerException

containing an

AccessException

, then the registry
denies the caller access to perform this operation (if
originating from a non-local host, for example)
- AccessException

- if this registry is local and it denies
the caller access to perform this operation
- NullPointerException

- if

name

is

null

, or if

obj

is

null

---

#### String
[] list()
throws
RemoteException
,

AccessException

Returns an array of the names bound in this registry. The
array will contain a snapshot of the names bound in this
registry at the time of the given invocation of this method.

**Returns:**
- an array of the names bound in this registry

**Throws:**
- RemoteException

- if remote communication with the
registry failed; if exception is a

ServerException

containing an

AccessException

, then the registry
denies the caller access to perform this operation
- AccessException

- if this registry is local and it denies
the caller access to perform this operation

---

### Additional Sections

#### Interface Registry

**All Superinterfaces:** Remote

```java
public interface
Registry

extends
Remote
```

Registry

is a remote interface to a simple remote
object registry that provides methods for storing and retrieving
remote object references bound with arbitrary string names. The

bind

,

unbind

, and

rebind

methods are used to alter the name bindings in the registry, and
the

lookup

and

list

methods are used to
query the current name bindings.

In its typical usage, a

Registry

enables RMI client
bootstrapping: it provides a simple means for a client to obtain an
initial reference to a remote object. Therefore, a registry's
remote object implementation is typically exported with a
well-known address, such as with a well-known

ObjID

and TCP port number
(default is

1099

).

The

LocateRegistry

class provides a programmatic API for
constructing a bootstrap reference to a

Registry

at a
remote address (see the static

getRegistry

methods)
and for creating and exporting a

Registry

in the
current VM on a particular local address (see the static

createRegistry

methods).

A

Registry

implementation may choose to restrict
access to some or all of its methods (for example, methods that
mutate the registry's bindings may be restricted to calls
originating from the local host). If a

Registry

method chooses to deny access for a given invocation, its
implementation may throw

AccessException

, which
(because it extends

RemoteException

) will be
wrapped in a

ServerException

when caught by a
remote client.

The names used for bindings in a

Registry

are pure
strings, not parsed. A service which stores its remote reference
in a

Registry

may wish to use a package name as a
prefix in the name binding to reduce the likelihood of name
collisions in the registry.

**Since:** 1.1
**See Also:** LocateRegistry

public interface

Registry

extends

Remote

Registry

is a remote interface to a simple remote
object registry that provides methods for storing and retrieving
remote object references bound with arbitrary string names. The

bind

,

unbind

, and

rebind

methods are used to alter the name bindings in the registry, and
the

lookup

and

list

methods are used to
query the current name bindings.

In its typical usage, a

Registry

enables RMI client
bootstrapping: it provides a simple means for a client to obtain an
initial reference to a remote object. Therefore, a registry's
remote object implementation is typically exported with a
well-known address, such as with a well-known

ObjID

and TCP port number
(default is

1099

).

The

LocateRegistry

class provides a programmatic API for
constructing a bootstrap reference to a

Registry

at a
remote address (see the static

getRegistry

methods)
and for creating and exporting a

Registry

in the
current VM on a particular local address (see the static

createRegistry

methods).

A

Registry

implementation may choose to restrict
access to some or all of its methods (for example, methods that
mutate the registry's bindings may be restricted to calls
originating from the local host). If a

Registry

method chooses to deny access for a given invocation, its
implementation may throw

AccessException

, which
(because it extends

RemoteException

) will be
wrapped in a

ServerException

when caught by a
remote client.

The names used for bindings in a

Registry

are pure
strings, not parsed. A service which stores its remote reference
in a

Registry

may wish to use a package name as a
prefix in the name binding to reduce the likelihood of name
collisions in the registry.

In its typical usage, a

Registry

enables RMI client
bootstrapping: it provides a simple means for a client to obtain an
initial reference to a remote object. Therefore, a registry's
remote object implementation is typically exported with a
well-known address, such as with a well-known

ObjID

and TCP port number
(default is

1099

).

The

LocateRegistry

class provides a programmatic API for
constructing a bootstrap reference to a

Registry

at a
remote address (see the static

getRegistry

methods)
and for creating and exporting a

Registry

in the
current VM on a particular local address (see the static

createRegistry

methods).

A

Registry

implementation may choose to restrict
access to some or all of its methods (for example, methods that
mutate the registry's bindings may be restricted to calls
originating from the local host). If a

Registry

method chooses to deny access for a given invocation, its
implementation may throw

AccessException

, which
(because it extends

RemoteException

) will be
wrapped in a

ServerException

when caught by a
remote client.

The names used for bindings in a

Registry

are pure
strings, not parsed. A service which stores its remote reference
in a

Registry

may wish to use a package name as a
prefix in the name binding to reduce the likelihood of name
collisions in the registry.

The

LocateRegistry

class provides a programmatic API for
constructing a bootstrap reference to a

Registry

at a
remote address (see the static

getRegistry

methods)
and for creating and exporting a

Registry

in the
current VM on a particular local address (see the static

createRegistry

methods).

A

Registry

implementation may choose to restrict
access to some or all of its methods (for example, methods that
mutate the registry's bindings may be restricted to calls
originating from the local host). If a

Registry

method chooses to deny access for a given invocation, its
implementation may throw

AccessException

, which
(because it extends

RemoteException

) will be
wrapped in a

ServerException

when caught by a
remote client.

The names used for bindings in a

Registry

are pure
strings, not parsed. A service which stores its remote reference
in a

Registry

may wish to use a package name as a
prefix in the name binding to reduce the likelihood of name
collisions in the registry.

A

Registry

implementation may choose to restrict
access to some or all of its methods (for example, methods that
mutate the registry's bindings may be restricted to calls
originating from the local host). If a

Registry

method chooses to deny access for a given invocation, its
implementation may throw

AccessException

, which
(because it extends

RemoteException

) will be
wrapped in a

ServerException

when caught by a
remote client.

The names used for bindings in a

Registry

are pure
strings, not parsed. A service which stores its remote reference
in a

Registry

may wish to use a package name as a
prefix in the name binding to reduce the likelihood of name
collisions in the registry.

The names used for bindings in a

Registry

are pure
strings, not parsed. A service which stores its remote reference
in a

Registry

may wish to use a package name as a
prefix in the name binding to reduce the likelihood of name
collisions in the registry.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static int

REGISTRY_PORT

Well known port for registry.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

bind

​(

String

name,

Remote

obj)

Binds a remote reference to the specified

name

in
this registry.

String

[]

list

()

Returns an array of the names bound in this registry.

Remote

lookup

​(

String

name)

Returns the remote reference bound to the specified

name

in this registry.

void

rebind

​(

String

name,

Remote

obj)

Replaces the binding for the specified

name

in
this registry with the supplied remote reference.

void

unbind

​(

String

name)

Removes the binding for the specified

name

in
this registry.

Field Summary

Fields

Modifier and Type

Field

Description

static int

REGISTRY_PORT

Well known port for registry.

---

#### Field Summary

Well known port for registry.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

bind

​(

String

name,

Remote

obj)

Binds a remote reference to the specified

name

in
this registry.

String

[]

list

()

Returns an array of the names bound in this registry.

Remote

lookup

​(

String

name)

Returns the remote reference bound to the specified

name

in this registry.

void

rebind

​(

String

name,

Remote

obj)

Replaces the binding for the specified

name

in
this registry with the supplied remote reference.

void

unbind

​(

String

name)

Removes the binding for the specified

name

in
this registry.

---

#### Method Summary

Binds a remote reference to the specified

name

in
this registry.

Returns an array of the names bound in this registry.

Returns the remote reference bound to the specified

name

in this registry.

Replaces the binding for the specified

name

in
this registry with the supplied remote reference.

Removes the binding for the specified

name

in
this registry.

============ FIELD DETAIL ===========

- Field Detail

- REGISTRY_PORT

```java
static final int REGISTRY_PORT
```

Well known port for registry.

**See Also:** Constant Field Values

============ METHOD DETAIL ==========

- Method Detail

- lookup

```java
Remote
lookup​(
String
name)
throws
RemoteException
,

NotBoundException
,

AccessException
```

Returns the remote reference bound to the specified

name

in this registry.

**Parameters:** name

- the name for the remote reference to look up
**Returns:** a reference to a remote object
**Throws:** NotBoundException

- if

name

is not currently bound
**Throws:** RemoteException

- if remote communication with the
registry failed; if exception is a

ServerException

containing an

AccessException

, then the registry
denies the caller access to perform this operation
**Throws:** AccessException

- if this registry is local and it denies
the caller access to perform this operation
**Throws:** NullPointerException

- if

name

is

null

- bind

```java
void bind​(
String
name,

Remote
obj)
throws
RemoteException
,

AlreadyBoundException
,

AccessException
```

Binds a remote reference to the specified

name

in
this registry.

**Parameters:** name

- the name to associate with the remote reference
**Parameters:** obj

- a reference to a remote object (usually a stub)
**Throws:** AlreadyBoundException

- if

name

is already bound
**Throws:** RemoteException

- if remote communication with the
registry failed; if exception is a

ServerException

containing an

AccessException

, then the registry
denies the caller access to perform this operation (if
originating from a non-local host, for example)
**Throws:** AccessException

- if this registry is local and it denies
the caller access to perform this operation
**Throws:** NullPointerException

- if

name

is

null

, or if

obj

is

null

- unbind

```java
void unbind​(
String
name)
throws
RemoteException
,

NotBoundException
,

AccessException
```

Removes the binding for the specified

name

in
this registry.

**Parameters:** name

- the name of the binding to remove
**Throws:** NotBoundException

- if

name

is not currently bound
**Throws:** RemoteException

- if remote communication with the
registry failed; if exception is a

ServerException

containing an

AccessException

, then the registry
denies the caller access to perform this operation (if
originating from a non-local host, for example)
**Throws:** AccessException

- if this registry is local and it denies
the caller access to perform this operation
**Throws:** NullPointerException

- if

name

is

null

- rebind

```java
void rebind​(
String
name,

Remote
obj)
throws
RemoteException
,

AccessException
```

Replaces the binding for the specified

name

in
this registry with the supplied remote reference. If there is
an existing binding for the specified

name

, it is
discarded.

**Parameters:** name

- the name to associate with the remote reference
**Parameters:** obj

- a reference to a remote object (usually a stub)
**Throws:** RemoteException

- if remote communication with the
registry failed; if exception is a

ServerException

containing an

AccessException

, then the registry
denies the caller access to perform this operation (if
originating from a non-local host, for example)
**Throws:** AccessException

- if this registry is local and it denies
the caller access to perform this operation
**Throws:** NullPointerException

- if

name

is

null

, or if

obj

is

null

- list

```java
String
[] list()
throws
RemoteException
,

AccessException
```

Returns an array of the names bound in this registry. The
array will contain a snapshot of the names bound in this
registry at the time of the given invocation of this method.

**Returns:** an array of the names bound in this registry
**Throws:** RemoteException

- if remote communication with the
registry failed; if exception is a

ServerException

containing an

AccessException

, then the registry
denies the caller access to perform this operation
**Throws:** AccessException

- if this registry is local and it denies
the caller access to perform this operation

Field Detail

- REGISTRY_PORT

```java
static final int REGISTRY_PORT
```

Well known port for registry.

**See Also:** Constant Field Values

---

#### Field Detail

REGISTRY_PORT

```java
static final int REGISTRY_PORT
```

Well known port for registry.

**See Also:** Constant Field Values

---

#### REGISTRY_PORT

static final int REGISTRY_PORT

Well known port for registry.

Method Detail

- lookup

```java
Remote
lookup​(
String
name)
throws
RemoteException
,

NotBoundException
,

AccessException
```

Returns the remote reference bound to the specified

name

in this registry.

**Parameters:** name

- the name for the remote reference to look up
**Returns:** a reference to a remote object
**Throws:** NotBoundException

- if

name

is not currently bound
**Throws:** RemoteException

- if remote communication with the
registry failed; if exception is a

ServerException

containing an

AccessException

, then the registry
denies the caller access to perform this operation
**Throws:** AccessException

- if this registry is local and it denies
the caller access to perform this operation
**Throws:** NullPointerException

- if

name

is

null

- bind

```java
void bind​(
String
name,

Remote
obj)
throws
RemoteException
,

AlreadyBoundException
,

AccessException
```

Binds a remote reference to the specified

name

in
this registry.

**Parameters:** name

- the name to associate with the remote reference
**Parameters:** obj

- a reference to a remote object (usually a stub)
**Throws:** AlreadyBoundException

- if

name

is already bound
**Throws:** RemoteException

- if remote communication with the
registry failed; if exception is a

ServerException

containing an

AccessException

, then the registry
denies the caller access to perform this operation (if
originating from a non-local host, for example)
**Throws:** AccessException

- if this registry is local and it denies
the caller access to perform this operation
**Throws:** NullPointerException

- if

name

is

null

, or if

obj

is

null

- unbind

```java
void unbind​(
String
name)
throws
RemoteException
,

NotBoundException
,

AccessException
```

Removes the binding for the specified

name

in
this registry.

**Parameters:** name

- the name of the binding to remove
**Throws:** NotBoundException

- if

name

is not currently bound
**Throws:** RemoteException

- if remote communication with the
registry failed; if exception is a

ServerException

containing an

AccessException

, then the registry
denies the caller access to perform this operation (if
originating from a non-local host, for example)
**Throws:** AccessException

- if this registry is local and it denies
the caller access to perform this operation
**Throws:** NullPointerException

- if

name

is

null

- rebind

```java
void rebind​(
String
name,

Remote
obj)
throws
RemoteException
,

AccessException
```

Replaces the binding for the specified

name

in
this registry with the supplied remote reference. If there is
an existing binding for the specified

name

, it is
discarded.

**Parameters:** name

- the name to associate with the remote reference
**Parameters:** obj

- a reference to a remote object (usually a stub)
**Throws:** RemoteException

- if remote communication with the
registry failed; if exception is a

ServerException

containing an

AccessException

, then the registry
denies the caller access to perform this operation (if
originating from a non-local host, for example)
**Throws:** AccessException

- if this registry is local and it denies
the caller access to perform this operation
**Throws:** NullPointerException

- if

name

is

null

, or if

obj

is

null

- list

```java
String
[] list()
throws
RemoteException
,

AccessException
```

Returns an array of the names bound in this registry. The
array will contain a snapshot of the names bound in this
registry at the time of the given invocation of this method.

**Returns:** an array of the names bound in this registry
**Throws:** RemoteException

- if remote communication with the
registry failed; if exception is a

ServerException

containing an

AccessException

, then the registry
denies the caller access to perform this operation
**Throws:** AccessException

- if this registry is local and it denies
the caller access to perform this operation

---

#### Method Detail

lookup

```java
Remote
lookup​(
String
name)
throws
RemoteException
,

NotBoundException
,

AccessException
```

Returns the remote reference bound to the specified

name

in this registry.

**Parameters:** name

- the name for the remote reference to look up
**Returns:** a reference to a remote object
**Throws:** NotBoundException

- if

name

is not currently bound
**Throws:** RemoteException

- if remote communication with the
registry failed; if exception is a

ServerException

containing an

AccessException

, then the registry
denies the caller access to perform this operation
**Throws:** AccessException

- if this registry is local and it denies
the caller access to perform this operation
**Throws:** NullPointerException

- if

name

is

null

---

#### lookup

Remote

lookup​(

String

name)
throws

RemoteException

,

NotBoundException

,

AccessException

Returns the remote reference bound to the specified

name

in this registry.

bind

```java
void bind​(
String
name,

Remote
obj)
throws
RemoteException
,

AlreadyBoundException
,

AccessException
```

Binds a remote reference to the specified

name

in
this registry.

**Parameters:** name

- the name to associate with the remote reference
**Parameters:** obj

- a reference to a remote object (usually a stub)
**Throws:** AlreadyBoundException

- if

name

is already bound
**Throws:** RemoteException

- if remote communication with the
registry failed; if exception is a

ServerException

containing an

AccessException

, then the registry
denies the caller access to perform this operation (if
originating from a non-local host, for example)
**Throws:** AccessException

- if this registry is local and it denies
the caller access to perform this operation
**Throws:** NullPointerException

- if

name

is

null

, or if

obj

is

null

---

#### bind

void bind​(

String

name,

Remote

obj)
throws

RemoteException

,

AlreadyBoundException

,

AccessException

Binds a remote reference to the specified

name

in
this registry.

unbind

```java
void unbind​(
String
name)
throws
RemoteException
,

NotBoundException
,

AccessException
```

Removes the binding for the specified

name

in
this registry.

**Parameters:** name

- the name of the binding to remove
**Throws:** NotBoundException

- if

name

is not currently bound
**Throws:** RemoteException

- if remote communication with the
registry failed; if exception is a

ServerException

containing an

AccessException

, then the registry
denies the caller access to perform this operation (if
originating from a non-local host, for example)
**Throws:** AccessException

- if this registry is local and it denies
the caller access to perform this operation
**Throws:** NullPointerException

- if

name

is

null

---

#### unbind

void unbind​(

String

name)
throws

RemoteException

,

NotBoundException

,

AccessException

Removes the binding for the specified

name

in
this registry.

rebind

```java
void rebind​(
String
name,

Remote
obj)
throws
RemoteException
,

AccessException
```

Replaces the binding for the specified

name

in
this registry with the supplied remote reference. If there is
an existing binding for the specified

name

, it is
discarded.

**Parameters:** name

- the name to associate with the remote reference
**Parameters:** obj

- a reference to a remote object (usually a stub)
**Throws:** RemoteException

- if remote communication with the
registry failed; if exception is a

ServerException

containing an

AccessException

, then the registry
denies the caller access to perform this operation (if
originating from a non-local host, for example)
**Throws:** AccessException

- if this registry is local and it denies
the caller access to perform this operation
**Throws:** NullPointerException

- if

name

is

null

, or if

obj

is

null

---

#### rebind

void rebind​(

String

name,

Remote

obj)
throws

RemoteException

,

AccessException

Replaces the binding for the specified

name

in
this registry with the supplied remote reference. If there is
an existing binding for the specified

name

, it is
discarded.

list

```java
String
[] list()
throws
RemoteException
,

AccessException
```

Returns an array of the names bound in this registry. The
array will contain a snapshot of the names bound in this
registry at the time of the given invocation of this method.

**Returns:** an array of the names bound in this registry
**Throws:** RemoteException

- if remote communication with the
registry failed; if exception is a

ServerException

containing an

AccessException

, then the registry
denies the caller access to perform this operation
**Throws:** AccessException

- if this registry is local and it denies
the caller access to perform this operation

---

#### list

String

[] list()
throws

RemoteException

,

AccessException

Returns an array of the names bound in this registry. The
array will contain a snapshot of the names bound in this
registry at the time of the given invocation of this method.

---

