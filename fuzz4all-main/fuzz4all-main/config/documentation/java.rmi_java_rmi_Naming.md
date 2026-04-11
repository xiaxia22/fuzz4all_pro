# Class Naming

**Source:** `java.rmi\java\rmi\Naming.html`

### Class Description

```java
public final class
Naming

extends
Object
```

The

Naming

class provides methods for storing and obtaining
references to remote objects in a remote object registry. Each method of
the

Naming

class takes as one of its arguments a name that
is a

java.lang.String

in URL format (without the
scheme component) of the form:

```java
//host:port/name
```

where

host

is the host (remote or local) where the registry
is located,

port

is the port number on which the registry
accepts calls, and where

name

is a simple string uninterpreted
by the registry. Both

host

and

port

are optional.
If

host

is omitted, the host defaults to the local host. If

port

is omitted, then the port defaults to 1099, the
"well-known" port that RMI's registry,

rmiregistry

, uses.

Binding

a name for a remote object is associating or
registering a name for a remote object that can be used at a later time to
look up that remote object. A remote object can be associated with a name
using the

Naming

class's

bind

or

rebind

methods.

Once a remote object is registered (bound) with the RMI registry on the
local host, callers on a remote (or local) host can lookup the remote
object by name, obtain its reference, and then invoke remote methods on the
object. A registry may be shared by all servers running on a host or an
individual server process may create and use its own registry if desired
(see

java.rmi.registry.LocateRegistry.createRegistry

method
for details).

**Since:** 1.1
**See Also:** Registry

,

LocateRegistry

,

LocateRegistry.createRegistry(int)

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### public static
Remote
lookup​(
String
name)
throws
NotBoundException
,

MalformedURLException
,

RemoteException

Returns a reference, a stub, for the remote object associated
with the specified

name

.

**Parameters:**
- name

- a name in URL format (without the scheme component)

**Returns:**
- a reference for a remote object

**Throws:**
- NotBoundException

- if name is not currently bound
- RemoteException

- if registry could not be contacted
- AccessException

- if this operation is not permitted
- MalformedURLException

- if the name is not an appropriately
formatted URL

**Since:**
- 1.1

---

#### public static void bind​(
String
name,

Remote
obj)
throws
AlreadyBoundException
,

MalformedURLException
,

RemoteException

Binds the specified

name

to a remote object.

**Parameters:**
- name

- a name in URL format (without the scheme component)
- obj

- a reference for the remote object (usually a stub)

**Throws:**
- AlreadyBoundException

- if name is already bound
- MalformedURLException

- if the name is not an appropriately
formatted URL
- RemoteException

- if registry could not be contacted
- AccessException

- if this operation is not permitted (if
originating from a non-local host, for example)

**Since:**
- 1.1

---

#### public static void unbind​(
String
name)
throws
RemoteException
,

NotBoundException
,

MalformedURLException

Destroys the binding for the specified name that is associated
with a remote object.

**Parameters:**
- name

- a name in URL format (without the scheme component)

**Throws:**
- NotBoundException

- if name is not currently bound
- MalformedURLException

- if the name is not an appropriately
formatted URL
- RemoteException

- if registry could not be contacted
- AccessException

- if this operation is not permitted (if
originating from a non-local host, for example)

**Since:**
- 1.1

---

#### public static void rebind​(
String
name,

Remote
obj)
throws
RemoteException
,

MalformedURLException

Rebinds the specified name to a new remote object. Any existing
binding for the name is replaced.

**Parameters:**
- name

- a name in URL format (without the scheme component)
- obj

- new remote object to associate with the name

**Throws:**
- MalformedURLException

- if the name is not an appropriately
formatted URL
- RemoteException

- if registry could not be contacted
- AccessException

- if this operation is not permitted (if
originating from a non-local host, for example)

**Since:**
- 1.1

---

#### public static
String
[] list​(
String
name)
throws
RemoteException
,

MalformedURLException

Returns an array of the names bound in the registry. The names are
URL-formatted (without the scheme component) strings. The array contains
a snapshot of the names present in the registry at the time of the
call.

**Parameters:**
- name

- a registry name in URL format (without the scheme
component)

**Returns:**
- an array of names (in the appropriate format) bound
in the registry

**Throws:**
- MalformedURLException

- if the name is not an appropriately
formatted URL
- RemoteException

- if registry could not be contacted.

**Since:**
- 1.1

---

### Additional Sections

#### Class Naming

java.lang.Object

- java.rmi.Naming

java.rmi.Naming

```java
public final class
Naming

extends
Object
```

The

Naming

class provides methods for storing and obtaining
references to remote objects in a remote object registry. Each method of
the

Naming

class takes as one of its arguments a name that
is a

java.lang.String

in URL format (without the
scheme component) of the form:

```java
//host:port/name
```

where

host

is the host (remote or local) where the registry
is located,

port

is the port number on which the registry
accepts calls, and where

name

is a simple string uninterpreted
by the registry. Both

host

and

port

are optional.
If

host

is omitted, the host defaults to the local host. If

port

is omitted, then the port defaults to 1099, the
"well-known" port that RMI's registry,

rmiregistry

, uses.

Binding

a name for a remote object is associating or
registering a name for a remote object that can be used at a later time to
look up that remote object. A remote object can be associated with a name
using the

Naming

class's

bind

or

rebind

methods.

Once a remote object is registered (bound) with the RMI registry on the
local host, callers on a remote (or local) host can lookup the remote
object by name, obtain its reference, and then invoke remote methods on the
object. A registry may be shared by all servers running on a host or an
individual server process may create and use its own registry if desired
(see

java.rmi.registry.LocateRegistry.createRegistry

method
for details).

**Since:** 1.1
**See Also:** Registry

,

LocateRegistry

,

LocateRegistry.createRegistry(int)

public final class

Naming

extends

Object

The

Naming

class provides methods for storing and obtaining
references to remote objects in a remote object registry. Each method of
the

Naming

class takes as one of its arguments a name that
is a

java.lang.String

in URL format (without the
scheme component) of the form:

```java
//host:port/name
```

where

host

is the host (remote or local) where the registry
is located,

port

is the port number on which the registry
accepts calls, and where

name

is a simple string uninterpreted
by the registry. Both

host

and

port

are optional.
If

host

is omitted, the host defaults to the local host. If

port

is omitted, then the port defaults to 1099, the
"well-known" port that RMI's registry,

rmiregistry

, uses.

Binding

a name for a remote object is associating or
registering a name for a remote object that can be used at a later time to
look up that remote object. A remote object can be associated with a name
using the

Naming

class's

bind

or

rebind

methods.

Once a remote object is registered (bound) with the RMI registry on the
local host, callers on a remote (or local) host can lookup the remote
object by name, obtain its reference, and then invoke remote methods on the
object. A registry may be shared by all servers running on a host or an
individual server process may create and use its own registry if desired
(see

java.rmi.registry.LocateRegistry.createRegistry

method
for details).

//host:port/name

where

host

is the host (remote or local) where the registry
is located,

port

is the port number on which the registry
accepts calls, and where

name

is a simple string uninterpreted
by the registry. Both

host

and

port

are optional.
If

host

is omitted, the host defaults to the local host. If

port

is omitted, then the port defaults to 1099, the
"well-known" port that RMI's registry,

rmiregistry

, uses.

Binding

a name for a remote object is associating or
registering a name for a remote object that can be used at a later time to
look up that remote object. A remote object can be associated with a name
using the

Naming

class's

bind

or

rebind

methods.

Once a remote object is registered (bound) with the RMI registry on the
local host, callers on a remote (or local) host can lookup the remote
object by name, obtain its reference, and then invoke remote methods on the
object. A registry may be shared by all servers running on a host or an
individual server process may create and use its own registry if desired
(see

java.rmi.registry.LocateRegistry.createRegistry

method
for details).

Binding

a name for a remote object is associating or
registering a name for a remote object that can be used at a later time to
look up that remote object. A remote object can be associated with a name
using the

Naming

class's

bind

or

rebind

methods.

Once a remote object is registered (bound) with the RMI registry on the
local host, callers on a remote (or local) host can lookup the remote
object by name, obtain its reference, and then invoke remote methods on the
object. A registry may be shared by all servers running on a host or an
individual server process may create and use its own registry if desired
(see

java.rmi.registry.LocateRegistry.createRegistry

method
for details).

Once a remote object is registered (bound) with the RMI registry on the
local host, callers on a remote (or local) host can lookup the remote
object by name, obtain its reference, and then invoke remote methods on the
object. A registry may be shared by all servers running on a host or an
individual server process may create and use its own registry if desired
(see

java.rmi.registry.LocateRegistry.createRegistry

method
for details).

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static void

bind

​(

String

name,

Remote

obj)

Binds the specified

name

to a remote object.

static

String

[]

list

​(

String

name)

Returns an array of the names bound in the registry.

static

Remote

lookup

​(

String

name)

Returns a reference, a stub, for the remote object associated
with the specified

name

.

static void

rebind

​(

String

name,

Remote

obj)

Rebinds the specified name to a new remote object.

static void

unbind

​(

String

name)

Destroys the binding for the specified name that is associated
with a remote object.

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

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static void

bind

​(

String

name,

Remote

obj)

Binds the specified

name

to a remote object.

static

String

[]

list

​(

String

name)

Returns an array of the names bound in the registry.

static

Remote

lookup

​(

String

name)

Returns a reference, a stub, for the remote object associated
with the specified

name

.

static void

rebind

​(

String

name,

Remote

obj)

Rebinds the specified name to a new remote object.

static void

unbind

​(

String

name)

Destroys the binding for the specified name that is associated
with a remote object.

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

Binds the specified

name

to a remote object.

Returns an array of the names bound in the registry.

Returns a reference, a stub, for the remote object associated
with the specified

name

.

Rebinds the specified name to a new remote object.

Destroys the binding for the specified name that is associated
with a remote object.

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

- lookup

```java
public static
Remote
lookup​(
String
name)
throws
NotBoundException
,

MalformedURLException
,

RemoteException
```

Returns a reference, a stub, for the remote object associated
with the specified

name

.

**Parameters:** name

- a name in URL format (without the scheme component)
**Returns:** a reference for a remote object
**Throws:** NotBoundException

- if name is not currently bound
**Throws:** RemoteException

- if registry could not be contacted
**Throws:** AccessException

- if this operation is not permitted
**Throws:** MalformedURLException

- if the name is not an appropriately
formatted URL
**Since:** 1.1

- bind

```java
public static void bind​(
String
name,

Remote
obj)
throws
AlreadyBoundException
,

MalformedURLException
,

RemoteException
```

Binds the specified

name

to a remote object.

**Parameters:** name

- a name in URL format (without the scheme component)
**Parameters:** obj

- a reference for the remote object (usually a stub)
**Throws:** AlreadyBoundException

- if name is already bound
**Throws:** MalformedURLException

- if the name is not an appropriately
formatted URL
**Throws:** RemoteException

- if registry could not be contacted
**Throws:** AccessException

- if this operation is not permitted (if
originating from a non-local host, for example)
**Since:** 1.1

- unbind

```java
public static void unbind​(
String
name)
throws
RemoteException
,

NotBoundException
,

MalformedURLException
```

Destroys the binding for the specified name that is associated
with a remote object.

**Parameters:** name

- a name in URL format (without the scheme component)
**Throws:** NotBoundException

- if name is not currently bound
**Throws:** MalformedURLException

- if the name is not an appropriately
formatted URL
**Throws:** RemoteException

- if registry could not be contacted
**Throws:** AccessException

- if this operation is not permitted (if
originating from a non-local host, for example)
**Since:** 1.1

- rebind

```java
public static void rebind​(
String
name,

Remote
obj)
throws
RemoteException
,

MalformedURLException
```

Rebinds the specified name to a new remote object. Any existing
binding for the name is replaced.

**Parameters:** name

- a name in URL format (without the scheme component)
**Parameters:** obj

- new remote object to associate with the name
**Throws:** MalformedURLException

- if the name is not an appropriately
formatted URL
**Throws:** RemoteException

- if registry could not be contacted
**Throws:** AccessException

- if this operation is not permitted (if
originating from a non-local host, for example)
**Since:** 1.1

- list

```java
public static
String
[] list​(
String
name)
throws
RemoteException
,

MalformedURLException
```

Returns an array of the names bound in the registry. The names are
URL-formatted (without the scheme component) strings. The array contains
a snapshot of the names present in the registry at the time of the
call.

**Parameters:** name

- a registry name in URL format (without the scheme
component)
**Returns:** an array of names (in the appropriate format) bound
in the registry
**Throws:** MalformedURLException

- if the name is not an appropriately
formatted URL
**Throws:** RemoteException

- if registry could not be contacted.
**Since:** 1.1

Method Detail

- lookup

```java
public static
Remote
lookup​(
String
name)
throws
NotBoundException
,

MalformedURLException
,

RemoteException
```

Returns a reference, a stub, for the remote object associated
with the specified

name

.

**Parameters:** name

- a name in URL format (without the scheme component)
**Returns:** a reference for a remote object
**Throws:** NotBoundException

- if name is not currently bound
**Throws:** RemoteException

- if registry could not be contacted
**Throws:** AccessException

- if this operation is not permitted
**Throws:** MalformedURLException

- if the name is not an appropriately
formatted URL
**Since:** 1.1

- bind

```java
public static void bind​(
String
name,

Remote
obj)
throws
AlreadyBoundException
,

MalformedURLException
,

RemoteException
```

Binds the specified

name

to a remote object.

**Parameters:** name

- a name in URL format (without the scheme component)
**Parameters:** obj

- a reference for the remote object (usually a stub)
**Throws:** AlreadyBoundException

- if name is already bound
**Throws:** MalformedURLException

- if the name is not an appropriately
formatted URL
**Throws:** RemoteException

- if registry could not be contacted
**Throws:** AccessException

- if this operation is not permitted (if
originating from a non-local host, for example)
**Since:** 1.1

- unbind

```java
public static void unbind​(
String
name)
throws
RemoteException
,

NotBoundException
,

MalformedURLException
```

Destroys the binding for the specified name that is associated
with a remote object.

**Parameters:** name

- a name in URL format (without the scheme component)
**Throws:** NotBoundException

- if name is not currently bound
**Throws:** MalformedURLException

- if the name is not an appropriately
formatted URL
**Throws:** RemoteException

- if registry could not be contacted
**Throws:** AccessException

- if this operation is not permitted (if
originating from a non-local host, for example)
**Since:** 1.1

- rebind

```java
public static void rebind​(
String
name,

Remote
obj)
throws
RemoteException
,

MalformedURLException
```

Rebinds the specified name to a new remote object. Any existing
binding for the name is replaced.

**Parameters:** name

- a name in URL format (without the scheme component)
**Parameters:** obj

- new remote object to associate with the name
**Throws:** MalformedURLException

- if the name is not an appropriately
formatted URL
**Throws:** RemoteException

- if registry could not be contacted
**Throws:** AccessException

- if this operation is not permitted (if
originating from a non-local host, for example)
**Since:** 1.1

- list

```java
public static
String
[] list​(
String
name)
throws
RemoteException
,

MalformedURLException
```

Returns an array of the names bound in the registry. The names are
URL-formatted (without the scheme component) strings. The array contains
a snapshot of the names present in the registry at the time of the
call.

**Parameters:** name

- a registry name in URL format (without the scheme
component)
**Returns:** an array of names (in the appropriate format) bound
in the registry
**Throws:** MalformedURLException

- if the name is not an appropriately
formatted URL
**Throws:** RemoteException

- if registry could not be contacted.
**Since:** 1.1

---

#### Method Detail

lookup

```java
public static
Remote
lookup​(
String
name)
throws
NotBoundException
,

MalformedURLException
,

RemoteException
```

Returns a reference, a stub, for the remote object associated
with the specified

name

.

**Parameters:** name

- a name in URL format (without the scheme component)
**Returns:** a reference for a remote object
**Throws:** NotBoundException

- if name is not currently bound
**Throws:** RemoteException

- if registry could not be contacted
**Throws:** AccessException

- if this operation is not permitted
**Throws:** MalformedURLException

- if the name is not an appropriately
formatted URL
**Since:** 1.1

---

#### lookup

public static

Remote

lookup​(

String

name)
throws

NotBoundException

,

MalformedURLException

,

RemoteException

Returns a reference, a stub, for the remote object associated
with the specified

name

.

bind

```java
public static void bind​(
String
name,

Remote
obj)
throws
AlreadyBoundException
,

MalformedURLException
,

RemoteException
```

Binds the specified

name

to a remote object.

**Parameters:** name

- a name in URL format (without the scheme component)
**Parameters:** obj

- a reference for the remote object (usually a stub)
**Throws:** AlreadyBoundException

- if name is already bound
**Throws:** MalformedURLException

- if the name is not an appropriately
formatted URL
**Throws:** RemoteException

- if registry could not be contacted
**Throws:** AccessException

- if this operation is not permitted (if
originating from a non-local host, for example)
**Since:** 1.1

---

#### bind

public static void bind​(

String

name,

Remote

obj)
throws

AlreadyBoundException

,

MalformedURLException

,

RemoteException

Binds the specified

name

to a remote object.

unbind

```java
public static void unbind​(
String
name)
throws
RemoteException
,

NotBoundException
,

MalformedURLException
```

Destroys the binding for the specified name that is associated
with a remote object.

**Parameters:** name

- a name in URL format (without the scheme component)
**Throws:** NotBoundException

- if name is not currently bound
**Throws:** MalformedURLException

- if the name is not an appropriately
formatted URL
**Throws:** RemoteException

- if registry could not be contacted
**Throws:** AccessException

- if this operation is not permitted (if
originating from a non-local host, for example)
**Since:** 1.1

---

#### unbind

public static void unbind​(

String

name)
throws

RemoteException

,

NotBoundException

,

MalformedURLException

Destroys the binding for the specified name that is associated
with a remote object.

rebind

```java
public static void rebind​(
String
name,

Remote
obj)
throws
RemoteException
,

MalformedURLException
```

Rebinds the specified name to a new remote object. Any existing
binding for the name is replaced.

**Parameters:** name

- a name in URL format (without the scheme component)
**Parameters:** obj

- new remote object to associate with the name
**Throws:** MalformedURLException

- if the name is not an appropriately
formatted URL
**Throws:** RemoteException

- if registry could not be contacted
**Throws:** AccessException

- if this operation is not permitted (if
originating from a non-local host, for example)
**Since:** 1.1

---

#### rebind

public static void rebind​(

String

name,

Remote

obj)
throws

RemoteException

,

MalformedURLException

Rebinds the specified name to a new remote object. Any existing
binding for the name is replaced.

list

```java
public static
String
[] list​(
String
name)
throws
RemoteException
,

MalformedURLException
```

Returns an array of the names bound in the registry. The names are
URL-formatted (without the scheme component) strings. The array contains
a snapshot of the names present in the registry at the time of the
call.

**Parameters:** name

- a registry name in URL format (without the scheme
component)
**Returns:** an array of names (in the appropriate format) bound
in the registry
**Throws:** MalformedURLException

- if the name is not an appropriately
formatted URL
**Throws:** RemoteException

- if registry could not be contacted.
**Since:** 1.1

---

#### list

public static

String

[] list​(

String

name)
throws

RemoteException

,

MalformedURLException

Returns an array of the names bound in the registry. The names are
URL-formatted (without the scheme component) strings. The array contains
a snapshot of the names present in the registry at the time of the
call.

---

