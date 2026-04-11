# Class RemoteServer

**Source:** `java.rmi\java\rmi\server\RemoteServer.html`

### Class Description

```java
public abstract class
RemoteServer

extends
RemoteObject
```

The

RemoteServer

class is the common superclass to server
implementations and provides the framework to support a wide range
of remote reference semantics. Specifically, the functions needed
to create and export remote objects (i.e. to make them remotely
available) are provided abstractly by

RemoteServer

and
concretely by its subclass(es).

**All Implemented Interfaces:** Serializable

,

Remote

---

### Field Details

*No entries found.*

### Constructor Details

#### protected RemoteServer()

Constructs a

RemoteServer

.

**Since:**
- 1.1

---

#### protected RemoteServer​(
RemoteRef
ref)

Constructs a

RemoteServer

with the given reference type.

**Parameters:**
- ref

- the remote reference

**Since:**
- 1.1

---

### Method Details

#### public static
String
getClientHost()
throws
ServerNotActiveException

Returns a string representation of the client host for the
remote method invocation being processed in the current thread.

**Returns:**
- a string representation of the client host

**Throws:**
- ServerNotActiveException

- if no remote method invocation
is being processed in the current thread

**Since:**
- 1.1

---

#### public static void setLog​(
OutputStream
out)

Log RMI calls to the output stream

out

. If

out

is

null

, call logging is turned off.

If there is a security manager, its

checkPermission

method will be invoked with a

java.util.logging.LoggingPermission("control")

permission; this could result in a

SecurityException

.

**Parameters:**
- out

- the output stream to which RMI calls should be logged

**Throws:**
- SecurityException

- if there is a security manager and
the invocation of its

checkPermission

method
fails

**See Also:**
- getLog()

**Since:**
- 1.1

---

#### public static
PrintStream
getLog()

Returns stream for the RMI call log.

**Returns:**
- the call log

**See Also:**
- setLog(java.io.OutputStream)

**Since:**
- 1.1

---

### Additional Sections

#### Class RemoteServer

java.lang.Object

- java.rmi.server.RemoteObject
- - java.rmi.server.RemoteServer

java.rmi.server.RemoteObject

- java.rmi.server.RemoteServer

java.rmi.server.RemoteServer

**All Implemented Interfaces:** Serializable

,

Remote

**Direct Known Subclasses:** Activatable

,

UnicastRemoteObject

```java
public abstract class
RemoteServer

extends
RemoteObject
```

The

RemoteServer

class is the common superclass to server
implementations and provides the framework to support a wide range
of remote reference semantics. Specifically, the functions needed
to create and export remote objects (i.e. to make them remotely
available) are provided abstractly by

RemoteServer

and
concretely by its subclass(es).

**Since:** 1.1
**See Also:** Serialized Form

public abstract class

RemoteServer

extends

RemoteObject

The

RemoteServer

class is the common superclass to server
implementations and provides the framework to support a wide range
of remote reference semantics. Specifically, the functions needed
to create and export remote objects (i.e. to make them remotely
available) are provided abstractly by

RemoteServer

and
concretely by its subclass(es).

=========== FIELD SUMMARY ===========

- Field Summary

- Fields declared in class java.rmi.server.

RemoteObject

ref

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

RemoteServer

()

Constructs a

RemoteServer

.

protected

RemoteServer

​(

RemoteRef

ref)

Constructs a

RemoteServer

with the given reference type.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

String

getClientHost

()

Returns a string representation of the client host for the
remote method invocation being processed in the current thread.

static

PrintStream

getLog

()

Returns stream for the RMI call log.

static void

setLog

​(

OutputStream

out)

Log RMI calls to the output stream

out

.

- Methods declared in class java.rmi.server.

RemoteObject

equals

,

getRef

,

hashCode

,

toString

,

toStub

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

Field Summary

- Fields declared in class java.rmi.server.

RemoteObject

ref

---

#### Field Summary

Fields declared in class java.rmi.server.

RemoteObject

ref

---

#### Fields declared in class java.rmi.server. RemoteObject

Constructor Summary

Constructors

Modifier

Constructor

Description

protected

RemoteServer

()

Constructs a

RemoteServer

.

protected

RemoteServer

​(

RemoteRef

ref)

Constructs a

RemoteServer

with the given reference type.

---

#### Constructor Summary

Constructs a

RemoteServer

.

Constructs a

RemoteServer

with the given reference type.

Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

String

getClientHost

()

Returns a string representation of the client host for the
remote method invocation being processed in the current thread.

static

PrintStream

getLog

()

Returns stream for the RMI call log.

static void

setLog

​(

OutputStream

out)

Log RMI calls to the output stream

out

.

- Methods declared in class java.rmi.server.

RemoteObject

equals

,

getRef

,

hashCode

,

toString

,

toStub

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

Returns a string representation of the client host for the
remote method invocation being processed in the current thread.

Returns stream for the RMI call log.

Log RMI calls to the output stream

out

.

Methods declared in class java.rmi.server.

RemoteObject

equals

,

getRef

,

hashCode

,

toString

,

toStub

---

#### Methods declared in class java.rmi.server. RemoteObject

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

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- RemoteServer

```java
protected RemoteServer()
```

Constructs a

RemoteServer

.

**Since:** 1.1

- RemoteServer

```java
protected RemoteServer​(
RemoteRef
ref)
```

Constructs a

RemoteServer

with the given reference type.

**Parameters:** ref

- the remote reference
**Since:** 1.1

============ METHOD DETAIL ==========

- Method Detail

- getClientHost

```java
public static
String
getClientHost()
throws
ServerNotActiveException
```

Returns a string representation of the client host for the
remote method invocation being processed in the current thread.

**Returns:** a string representation of the client host
**Throws:** ServerNotActiveException

- if no remote method invocation
is being processed in the current thread
**Since:** 1.1

- setLog

```java
public static void setLog​(
OutputStream
out)
```

Log RMI calls to the output stream

out

. If

out

is

null

, call logging is turned off.

If there is a security manager, its

checkPermission

method will be invoked with a

java.util.logging.LoggingPermission("control")

permission; this could result in a

SecurityException

.

**Parameters:** out

- the output stream to which RMI calls should be logged
**Throws:** SecurityException

- if there is a security manager and
the invocation of its

checkPermission

method
fails
**Since:** 1.1
**See Also:** getLog()

- getLog

```java
public static
PrintStream
getLog()
```

Returns stream for the RMI call log.

**Returns:** the call log
**Since:** 1.1
**See Also:** setLog(java.io.OutputStream)

Constructor Detail

- RemoteServer

```java
protected RemoteServer()
```

Constructs a

RemoteServer

.

**Since:** 1.1

- RemoteServer

```java
protected RemoteServer​(
RemoteRef
ref)
```

Constructs a

RemoteServer

with the given reference type.

**Parameters:** ref

- the remote reference
**Since:** 1.1

---

#### Constructor Detail

RemoteServer

```java
protected RemoteServer()
```

Constructs a

RemoteServer

.

**Since:** 1.1

---

#### RemoteServer

protected RemoteServer()

Constructs a

RemoteServer

.

RemoteServer

```java
protected RemoteServer​(
RemoteRef
ref)
```

Constructs a

RemoteServer

with the given reference type.

**Parameters:** ref

- the remote reference
**Since:** 1.1

---

#### RemoteServer

protected RemoteServer​(

RemoteRef

ref)

Constructs a

RemoteServer

with the given reference type.

Method Detail

- getClientHost

```java
public static
String
getClientHost()
throws
ServerNotActiveException
```

Returns a string representation of the client host for the
remote method invocation being processed in the current thread.

**Returns:** a string representation of the client host
**Throws:** ServerNotActiveException

- if no remote method invocation
is being processed in the current thread
**Since:** 1.1

- setLog

```java
public static void setLog​(
OutputStream
out)
```

Log RMI calls to the output stream

out

. If

out

is

null

, call logging is turned off.

If there is a security manager, its

checkPermission

method will be invoked with a

java.util.logging.LoggingPermission("control")

permission; this could result in a

SecurityException

.

**Parameters:** out

- the output stream to which RMI calls should be logged
**Throws:** SecurityException

- if there is a security manager and
the invocation of its

checkPermission

method
fails
**Since:** 1.1
**See Also:** getLog()

- getLog

```java
public static
PrintStream
getLog()
```

Returns stream for the RMI call log.

**Returns:** the call log
**Since:** 1.1
**See Also:** setLog(java.io.OutputStream)

---

#### Method Detail

getClientHost

```java
public static
String
getClientHost()
throws
ServerNotActiveException
```

Returns a string representation of the client host for the
remote method invocation being processed in the current thread.

**Returns:** a string representation of the client host
**Throws:** ServerNotActiveException

- if no remote method invocation
is being processed in the current thread
**Since:** 1.1

---

#### getClientHost

public static

String

getClientHost()
throws

ServerNotActiveException

Returns a string representation of the client host for the
remote method invocation being processed in the current thread.

setLog

```java
public static void setLog​(
OutputStream
out)
```

Log RMI calls to the output stream

out

. If

out

is

null

, call logging is turned off.

If there is a security manager, its

checkPermission

method will be invoked with a

java.util.logging.LoggingPermission("control")

permission; this could result in a

SecurityException

.

**Parameters:** out

- the output stream to which RMI calls should be logged
**Throws:** SecurityException

- if there is a security manager and
the invocation of its

checkPermission

method
fails
**Since:** 1.1
**See Also:** getLog()

---

#### setLog

public static void setLog​(

OutputStream

out)

Log RMI calls to the output stream

out

. If

out

is

null

, call logging is turned off.

If there is a security manager, its

checkPermission

method will be invoked with a

java.util.logging.LoggingPermission("control")

permission; this could result in a

SecurityException

.

If there is a security manager, its

checkPermission

method will be invoked with a

java.util.logging.LoggingPermission("control")

permission; this could result in a

SecurityException

.

getLog

```java
public static
PrintStream
getLog()
```

Returns stream for the RMI call log.

**Returns:** the call log
**Since:** 1.1
**See Also:** setLog(java.io.OutputStream)

---

#### getLog

public static

PrintStream

getLog()

Returns stream for the RMI call log.

---

