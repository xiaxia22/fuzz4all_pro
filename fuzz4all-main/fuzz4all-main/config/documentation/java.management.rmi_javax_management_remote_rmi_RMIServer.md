# Interface RMIServer

**Source:** `java.management.rmi\javax\management\remote\rmi\RMIServer.html`

### Class Description

```java
public interface
RMIServer

extends
Remote
```

RMI object used to establish connections to an RMI connector.
There is one Remote object implementing this interface for each RMI
connector.

User code does not usually refer to this interface. It is
specified as part of the public API so that different
implementations of that API will interoperate.

**All Superinterfaces:** Remote

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### String
getVersion()
throws
RemoteException

The version of the RMI Connector Protocol understood by this
connector server. This is a string with the following format:

```java
protocol-version

implementation-name
```

The

protocol-version

is a series of
two or more non-negative integers separated by periods
(

.

). An implementation of the version described
by this documentation must use the string

1.0

here.

After the protocol version there must be a space, followed
by the implementation name. The format of the implementation
name is unspecified. It is recommended that it include an
implementation version number. An implementation can use an
empty string as its implementation name, for example for
security reasons.

**Returns:**
- a string with the format described here.

**Throws:**
- RemoteException

- if there is a communication
exception during the remote method call.

---

#### RMIConnection
newClient​(
Object
credentials)
throws
IOException

Makes a new connection through this RMI connector. Each
remote client calls this method to obtain a new RMI object
representing its connection.

**Parameters:**
- credentials

- this object specifies the user-defined credentials
to be passed in to the server in order to authenticate the user before
creating the

RMIConnection

. Can be null.

**Returns:**
- the newly-created connection object.

**Throws:**
- IOException

- if the new client object cannot be
created or exported, or if there is a communication exception
during the remote method call.
- SecurityException

- if the given credentials do not
allow the server to authenticate the caller successfully.

---

### Additional Sections

#### Interface RMIServer

**All Superinterfaces:** Remote

**All Known Implementing Classes:** RMIIIOPServerImpl

,

RMIJRMPServerImpl

,

RMIServerImpl

,

RMIServerImpl_Stub

```java
public interface
RMIServer

extends
Remote
```

RMI object used to establish connections to an RMI connector.
There is one Remote object implementing this interface for each RMI
connector.

User code does not usually refer to this interface. It is
specified as part of the public API so that different
implementations of that API will interoperate.

**Since:** 1.5

public interface

RMIServer

extends

Remote

RMI object used to establish connections to an RMI connector.
There is one Remote object implementing this interface for each RMI
connector.

User code does not usually refer to this interface. It is
specified as part of the public API so that different
implementations of that API will interoperate.

RMI object used to establish connections to an RMI connector.
There is one Remote object implementing this interface for each RMI
connector.

User code does not usually refer to this interface. It is
specified as part of the public API so that different
implementations of that API will interoperate.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

String

getVersion

()

The version of the RMI Connector Protocol understood by this
connector server.

RMIConnection

newClient

​(

Object

credentials)

Makes a new connection through this RMI connector.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

String

getVersion

()

The version of the RMI Connector Protocol understood by this
connector server.

RMIConnection

newClient

​(

Object

credentials)

Makes a new connection through this RMI connector.

---

#### Method Summary

The version of the RMI Connector Protocol understood by this
connector server.

Makes a new connection through this RMI connector.

============ METHOD DETAIL ==========

- Method Detail

- getVersion

```java
String
getVersion()
throws
RemoteException
```

The version of the RMI Connector Protocol understood by this
connector server. This is a string with the following format:

```java
protocol-version

implementation-name
```

The

protocol-version

is a series of
two or more non-negative integers separated by periods
(

.

). An implementation of the version described
by this documentation must use the string

1.0

here.

After the protocol version there must be a space, followed
by the implementation name. The format of the implementation
name is unspecified. It is recommended that it include an
implementation version number. An implementation can use an
empty string as its implementation name, for example for
security reasons.

**Returns:** a string with the format described here.
**Throws:** RemoteException

- if there is a communication
exception during the remote method call.

- newClient

```java
RMIConnection
newClient​(
Object
credentials)
throws
IOException
```

Makes a new connection through this RMI connector. Each
remote client calls this method to obtain a new RMI object
representing its connection.

**Parameters:** credentials

- this object specifies the user-defined credentials
to be passed in to the server in order to authenticate the user before
creating the

RMIConnection

. Can be null.
**Returns:** the newly-created connection object.
**Throws:** IOException

- if the new client object cannot be
created or exported, or if there is a communication exception
during the remote method call.
**Throws:** SecurityException

- if the given credentials do not
allow the server to authenticate the caller successfully.

Method Detail

- getVersion

```java
String
getVersion()
throws
RemoteException
```

The version of the RMI Connector Protocol understood by this
connector server. This is a string with the following format:

```java
protocol-version

implementation-name
```

The

protocol-version

is a series of
two or more non-negative integers separated by periods
(

.

). An implementation of the version described
by this documentation must use the string

1.0

here.

After the protocol version there must be a space, followed
by the implementation name. The format of the implementation
name is unspecified. It is recommended that it include an
implementation version number. An implementation can use an
empty string as its implementation name, for example for
security reasons.

**Returns:** a string with the format described here.
**Throws:** RemoteException

- if there is a communication
exception during the remote method call.

- newClient

```java
RMIConnection
newClient​(
Object
credentials)
throws
IOException
```

Makes a new connection through this RMI connector. Each
remote client calls this method to obtain a new RMI object
representing its connection.

**Parameters:** credentials

- this object specifies the user-defined credentials
to be passed in to the server in order to authenticate the user before
creating the

RMIConnection

. Can be null.
**Returns:** the newly-created connection object.
**Throws:** IOException

- if the new client object cannot be
created or exported, or if there is a communication exception
during the remote method call.
**Throws:** SecurityException

- if the given credentials do not
allow the server to authenticate the caller successfully.

---

#### Method Detail

getVersion

```java
String
getVersion()
throws
RemoteException
```

The version of the RMI Connector Protocol understood by this
connector server. This is a string with the following format:

```java
protocol-version

implementation-name
```

The

protocol-version

is a series of
two or more non-negative integers separated by periods
(

.

). An implementation of the version described
by this documentation must use the string

1.0

here.

After the protocol version there must be a space, followed
by the implementation name. The format of the implementation
name is unspecified. It is recommended that it include an
implementation version number. An implementation can use an
empty string as its implementation name, for example for
security reasons.

**Returns:** a string with the format described here.
**Throws:** RemoteException

- if there is a communication
exception during the remote method call.

---

#### getVersion

String

getVersion()
throws

RemoteException

The version of the RMI Connector Protocol understood by this
connector server. This is a string with the following format:

```java
protocol-version

implementation-name
```

The

protocol-version

is a series of
two or more non-negative integers separated by periods
(

.

). An implementation of the version described
by this documentation must use the string

1.0

here.

After the protocol version there must be a space, followed
by the implementation name. The format of the implementation
name is unspecified. It is recommended that it include an
implementation version number. An implementation can use an
empty string as its implementation name, for example for
security reasons.

The version of the RMI Connector Protocol understood by this
connector server. This is a string with the following format:

protocol-version

implementation-name

The

protocol-version

is a series of
two or more non-negative integers separated by periods
(

.

). An implementation of the version described
by this documentation must use the string

1.0

here.

After the protocol version there must be a space, followed
by the implementation name. The format of the implementation
name is unspecified. It is recommended that it include an
implementation version number. An implementation can use an
empty string as its implementation name, for example for
security reasons.

newClient

```java
RMIConnection
newClient​(
Object
credentials)
throws
IOException
```

Makes a new connection through this RMI connector. Each
remote client calls this method to obtain a new RMI object
representing its connection.

**Parameters:** credentials

- this object specifies the user-defined credentials
to be passed in to the server in order to authenticate the user before
creating the

RMIConnection

. Can be null.
**Returns:** the newly-created connection object.
**Throws:** IOException

- if the new client object cannot be
created or exported, or if there is a communication exception
during the remote method call.
**Throws:** SecurityException

- if the given credentials do not
allow the server to authenticate the caller successfully.

---

#### newClient

RMIConnection

newClient​(

Object

credentials)
throws

IOException

Makes a new connection through this RMI connector. Each
remote client calls this method to obtain a new RMI object
representing its connection.

---

