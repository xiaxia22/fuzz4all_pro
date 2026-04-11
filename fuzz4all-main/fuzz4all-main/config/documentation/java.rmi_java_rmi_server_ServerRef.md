# Interface ServerRef

**Source:** `java.rmi\java\rmi\server\ServerRef.html`

### Class Description

```java
@Deprecated

public interface
ServerRef

extends
RemoteRef
```

A ServerRef represents the server-side handle for a remote object
implementation.

**All Superinterfaces:** Externalizable

,

RemoteRef

,

Serializable

---

### Field Details

#### static final long serialVersionUID

indicate compatibility with JDK 1.1.x version of class.

**See Also:**
- Constant Field Values

---

### Constructor Details

*No entries found.*

### Method Details

#### RemoteStub
exportObject​(
Remote
obj,

Object
data)
throws
RemoteException

Creates a client stub object for the supplied Remote object.
If the call completes successfully, the remote object should
be able to accept incoming calls from clients.

**Parameters:**
- obj

- the remote object implementation
- data

- information necessary to export the object

**Returns:**
- the stub for the remote object

**Throws:**
- RemoteException

- if an exception occurs attempting
to export the object (e.g., stub class could not be found)

**Since:**
- 1.1

---

#### String
getClientHost()
throws
ServerNotActiveException

Returns the hostname of the current client. When called from a
thread actively handling a remote method invocation the
hostname of the client is returned.

**Returns:**
- the client's host name

**Throws:**
- ServerNotActiveException

- if called outside of servicing
a remote method invocation

**Since:**
- 1.1

---

### Additional Sections

#### Interface ServerRef

**All Superinterfaces:** Externalizable

,

RemoteRef

,

Serializable

```java
@Deprecated

public interface
ServerRef

extends
RemoteRef
```

Deprecated.

No replacement. This interface is unused and is obsolete.

A ServerRef represents the server-side handle for a remote object
implementation.

**Since:** 1.1

@Deprecated

public interface

ServerRef

extends

RemoteRef

A ServerRef represents the server-side handle for a remote object
implementation.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static long

serialVersionUID

Deprecated.

indicate compatibility with JDK 1.1.x version of class.

- Fields declared in interface java.rmi.server.

RemoteRef

packagePrefix

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Deprecated Methods

Modifier and Type

Method

Description

RemoteStub

exportObject

​(

Remote

obj,

Object

data)

Deprecated.

Creates a client stub object for the supplied Remote object.

String

getClientHost

()

Deprecated.

Returns the hostname of the current client.

- Methods declared in interface java.io.

Externalizable

readExternal

,

writeExternal

- Methods declared in interface java.rmi.server.

RemoteRef

done

,

getRefClass

,

invoke

,

invoke

,

newCall

,

remoteEquals

,

remoteHashCode

,

remoteToString

Field Summary

Fields

Modifier and Type

Field

Description

static long

serialVersionUID

Deprecated.

indicate compatibility with JDK 1.1.x version of class.

- Fields declared in interface java.rmi.server.

RemoteRef

packagePrefix

---

#### Field Summary

Deprecated.

indicate compatibility with JDK 1.1.x version of class.

Fields declared in interface java.rmi.server.

RemoteRef

packagePrefix

---

#### Fields declared in interface java.rmi.server. RemoteRef

Method Summary

All Methods

Instance Methods

Abstract Methods

Deprecated Methods

Modifier and Type

Method

Description

RemoteStub

exportObject

​(

Remote

obj,

Object

data)

Deprecated.

Creates a client stub object for the supplied Remote object.

String

getClientHost

()

Deprecated.

Returns the hostname of the current client.

- Methods declared in interface java.io.

Externalizable

readExternal

,

writeExternal

- Methods declared in interface java.rmi.server.

RemoteRef

done

,

getRefClass

,

invoke

,

invoke

,

newCall

,

remoteEquals

,

remoteHashCode

,

remoteToString

---

#### Method Summary

Deprecated.

Creates a client stub object for the supplied Remote object.

Returns the hostname of the current client.

Methods declared in interface java.io.

Externalizable

readExternal

,

writeExternal

---

#### Methods declared in interface java.io. Externalizable

Methods declared in interface java.rmi.server.

RemoteRef

done

,

getRefClass

,

invoke

,

invoke

,

newCall

,

remoteEquals

,

remoteHashCode

,

remoteToString

---

#### Methods declared in interface java.rmi.server. RemoteRef

============ FIELD DETAIL ===========

- Field Detail

- serialVersionUID

```java
static final long serialVersionUID
```

Deprecated.

indicate compatibility with JDK 1.1.x version of class.

**See Also:** Constant Field Values

============ METHOD DETAIL ==========

- Method Detail

- exportObject

```java
RemoteStub
exportObject​(
Remote
obj,

Object
data)
throws
RemoteException
```

Deprecated.

Creates a client stub object for the supplied Remote object.
If the call completes successfully, the remote object should
be able to accept incoming calls from clients.

**Parameters:** obj

- the remote object implementation
**Parameters:** data

- information necessary to export the object
**Returns:** the stub for the remote object
**Throws:** RemoteException

- if an exception occurs attempting
to export the object (e.g., stub class could not be found)
**Since:** 1.1

- getClientHost

```java
String
getClientHost()
throws
ServerNotActiveException
```

Deprecated.

Returns the hostname of the current client. When called from a
thread actively handling a remote method invocation the
hostname of the client is returned.

**Returns:** the client's host name
**Throws:** ServerNotActiveException

- if called outside of servicing
a remote method invocation
**Since:** 1.1

Field Detail

- serialVersionUID

```java
static final long serialVersionUID
```

Deprecated.

indicate compatibility with JDK 1.1.x version of class.

**See Also:** Constant Field Values

---

#### Field Detail

serialVersionUID

```java
static final long serialVersionUID
```

Deprecated.

indicate compatibility with JDK 1.1.x version of class.

**See Also:** Constant Field Values

---

#### serialVersionUID

static final long serialVersionUID

indicate compatibility with JDK 1.1.x version of class.

Method Detail

- exportObject

```java
RemoteStub
exportObject​(
Remote
obj,

Object
data)
throws
RemoteException
```

Deprecated.

Creates a client stub object for the supplied Remote object.
If the call completes successfully, the remote object should
be able to accept incoming calls from clients.

**Parameters:** obj

- the remote object implementation
**Parameters:** data

- information necessary to export the object
**Returns:** the stub for the remote object
**Throws:** RemoteException

- if an exception occurs attempting
to export the object (e.g., stub class could not be found)
**Since:** 1.1

- getClientHost

```java
String
getClientHost()
throws
ServerNotActiveException
```

Deprecated.

Returns the hostname of the current client. When called from a
thread actively handling a remote method invocation the
hostname of the client is returned.

**Returns:** the client's host name
**Throws:** ServerNotActiveException

- if called outside of servicing
a remote method invocation
**Since:** 1.1

---

#### Method Detail

exportObject

```java
RemoteStub
exportObject​(
Remote
obj,

Object
data)
throws
RemoteException
```

Deprecated.

Creates a client stub object for the supplied Remote object.
If the call completes successfully, the remote object should
be able to accept incoming calls from clients.

**Parameters:** obj

- the remote object implementation
**Parameters:** data

- information necessary to export the object
**Returns:** the stub for the remote object
**Throws:** RemoteException

- if an exception occurs attempting
to export the object (e.g., stub class could not be found)
**Since:** 1.1

---

#### exportObject

RemoteStub

exportObject​(

Remote

obj,

Object

data)
throws

RemoteException

Creates a client stub object for the supplied Remote object.
If the call completes successfully, the remote object should
be able to accept incoming calls from clients.

getClientHost

```java
String
getClientHost()
throws
ServerNotActiveException
```

Deprecated.

Returns the hostname of the current client. When called from a
thread actively handling a remote method invocation the
hostname of the client is returned.

**Returns:** the client's host name
**Throws:** ServerNotActiveException

- if called outside of servicing
a remote method invocation
**Since:** 1.1

---

#### getClientHost

String

getClientHost()
throws

ServerNotActiveException

Returns the hostname of the current client. When called from a
thread actively handling a remote method invocation the
hostname of the client is returned.

---

