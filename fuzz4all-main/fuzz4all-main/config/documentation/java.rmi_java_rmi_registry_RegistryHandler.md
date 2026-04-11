# Interface RegistryHandler

**Source:** `java.rmi\java\rmi\registry\RegistryHandler.html`

### Class Description

```java
@Deprecated

public interface
RegistryHandler
```

RegistryHandler

is an interface used internally by the RMI
runtime in previous implementation versions. It should never be accessed
by application code.

**Since:** 1.1

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### @Deprecated

Registry
registryStub​(
String
host,
int port)
throws
RemoteException
,

UnknownHostException

Returns a "stub" for contacting a remote registry
on the specified host and port.

**Parameters:**
- host

- name of remote registry host
- port

- remote registry port

**Returns:**
- remote registry stub

**Throws:**
- RemoteException

- if a remote error occurs
- UnknownHostException

- if unable to resolve given hostname

---

#### @Deprecated

Registry
registryImpl​(int port)
throws
RemoteException

Constructs and exports a Registry on the specified port.
The port must be non-zero.

**Parameters:**
- port

- port to export registry on

**Returns:**
- registry stub

**Throws:**
- RemoteException

- if a remote error occurs

---

### Additional Sections

#### Interface RegistryHandler

```java
@Deprecated

public interface
RegistryHandler
```

Deprecated.

no replacement

RegistryHandler

is an interface used internally by the RMI
runtime in previous implementation versions. It should never be accessed
by application code.

**Since:** 1.1

@Deprecated

public interface

RegistryHandler

RegistryHandler

is an interface used internally by the RMI
runtime in previous implementation versions. It should never be accessed
by application code.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Deprecated Methods

Modifier and Type

Method

Description

Registry

registryImpl

​(int port)

Deprecated.

no replacement.

Registry

registryStub

​(

String

host,
int port)

Deprecated.

no replacement.

Method Summary

All Methods

Instance Methods

Abstract Methods

Deprecated Methods

Modifier and Type

Method

Description

Registry

registryImpl

​(int port)

Deprecated.

no replacement.

Registry

registryStub

​(

String

host,
int port)

Deprecated.

no replacement.

---

#### Method Summary

Deprecated.

no replacement.

============ METHOD DETAIL ==========

- Method Detail

- registryStub

```java
@Deprecated

Registry
registryStub​(
String
host,
int port)
throws
RemoteException
,

UnknownHostException
```

Deprecated.

no replacement. As of the Java 2 platform v1.2, RMI no
longer uses the

RegistryHandler

to obtain the registry's
stub.

Returns a "stub" for contacting a remote registry
on the specified host and port.

**Parameters:** host

- name of remote registry host
**Parameters:** port

- remote registry port
**Returns:** remote registry stub
**Throws:** RemoteException

- if a remote error occurs
**Throws:** UnknownHostException

- if unable to resolve given hostname

- registryImpl

```java
@Deprecated

Registry
registryImpl​(int port)
throws
RemoteException
```

Deprecated.

no replacement. As of the Java 2 platform v1.2, RMI no
longer uses the

RegistryHandler

to obtain the registry's
implementation.

Constructs and exports a Registry on the specified port.
The port must be non-zero.

**Parameters:** port

- port to export registry on
**Returns:** registry stub
**Throws:** RemoteException

- if a remote error occurs

Method Detail

- registryStub

```java
@Deprecated

Registry
registryStub​(
String
host,
int port)
throws
RemoteException
,

UnknownHostException
```

Deprecated.

no replacement. As of the Java 2 platform v1.2, RMI no
longer uses the

RegistryHandler

to obtain the registry's
stub.

Returns a "stub" for contacting a remote registry
on the specified host and port.

**Parameters:** host

- name of remote registry host
**Parameters:** port

- remote registry port
**Returns:** remote registry stub
**Throws:** RemoteException

- if a remote error occurs
**Throws:** UnknownHostException

- if unable to resolve given hostname

- registryImpl

```java
@Deprecated

Registry
registryImpl​(int port)
throws
RemoteException
```

Deprecated.

no replacement. As of the Java 2 platform v1.2, RMI no
longer uses the

RegistryHandler

to obtain the registry's
implementation.

Constructs and exports a Registry on the specified port.
The port must be non-zero.

**Parameters:** port

- port to export registry on
**Returns:** registry stub
**Throws:** RemoteException

- if a remote error occurs

---

#### Method Detail

registryStub

```java
@Deprecated

Registry
registryStub​(
String
host,
int port)
throws
RemoteException
,

UnknownHostException
```

Deprecated.

no replacement. As of the Java 2 platform v1.2, RMI no
longer uses the

RegistryHandler

to obtain the registry's
stub.

Returns a "stub" for contacting a remote registry
on the specified host and port.

**Parameters:** host

- name of remote registry host
**Parameters:** port

- remote registry port
**Returns:** remote registry stub
**Throws:** RemoteException

- if a remote error occurs
**Throws:** UnknownHostException

- if unable to resolve given hostname

---

#### registryStub

@Deprecated

Registry

registryStub​(

String

host,
int port)
throws

RemoteException

,

UnknownHostException

Returns a "stub" for contacting a remote registry
on the specified host and port.

registryImpl

```java
@Deprecated

Registry
registryImpl​(int port)
throws
RemoteException
```

Deprecated.

no replacement. As of the Java 2 platform v1.2, RMI no
longer uses the

RegistryHandler

to obtain the registry's
implementation.

Constructs and exports a Registry on the specified port.
The port must be non-zero.

**Parameters:** port

- port to export registry on
**Returns:** registry stub
**Throws:** RemoteException

- if a remote error occurs

---

#### registryImpl

@Deprecated

Registry

registryImpl​(int port)
throws

RemoteException

Constructs and exports a Registry on the specified port.
The port must be non-zero.

---

