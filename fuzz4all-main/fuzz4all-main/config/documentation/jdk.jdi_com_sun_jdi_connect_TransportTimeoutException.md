# Class TransportTimeoutException

**Source:** `jdk.jdi\com\sun\jdi\connect\TransportTimeoutException.html`

### Class Description

```java
public class
TransportTimeoutException

extends
IOException
```

This exception may be thrown as a result of a timeout
when attaching to a target VM, or waiting to accept a
connection from a target VM.

When attaching to a target VM, using

attach

this
exception may be thrown if the connector supports a timeout

connector argument

. Similiarly,
when waiting to accept a connection from a target VM,
using

accept

this
exception may be thrown if the connector supports a
timeout connector argument when accepting.

In addition, for developers creating

TransportService

implementations this exception is thrown when

attach

times out when establishing a
connection to a target VM, or

accept

times out while waiting for a target VM to connect.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public TransportTimeoutException()

Constructs a

TransportTimeoutException

with no detail
message.

---

#### public TransportTimeoutException​(
String
message)

Constructs a

TransportTimeoutException

with the
specified detail message.

**Parameters:**
- message

- the detail message pertaining to this exception.

---

### Method Details

*No entries found.*

### Additional Sections

#### Class TransportTimeoutException

java.lang.Object

- java.lang.Throwable
- - java.lang.Exception
- - java.io.IOException
- - com.sun.jdi.connect.TransportTimeoutException

java.lang.Throwable

- java.lang.Exception
- - java.io.IOException
- - com.sun.jdi.connect.TransportTimeoutException

java.lang.Exception

- java.io.IOException
- - com.sun.jdi.connect.TransportTimeoutException

java.io.IOException

- com.sun.jdi.connect.TransportTimeoutException

com.sun.jdi.connect.TransportTimeoutException

**All Implemented Interfaces:** Serializable

```java
public class
TransportTimeoutException

extends
IOException
```

This exception may be thrown as a result of a timeout
when attaching to a target VM, or waiting to accept a
connection from a target VM.

When attaching to a target VM, using

attach

this
exception may be thrown if the connector supports a timeout

connector argument

. Similiarly,
when waiting to accept a connection from a target VM,
using

accept

this
exception may be thrown if the connector supports a
timeout connector argument when accepting.

In addition, for developers creating

TransportService

implementations this exception is thrown when

attach

times out when establishing a
connection to a target VM, or

accept

times out while waiting for a target VM to connect.

**Since:** 1.5
**See Also:** AttachingConnector.attach(java.util.Map<java.lang.String, ? extends com.sun.jdi.connect.Connector.Argument>)

,

ListeningConnector.accept(java.util.Map<java.lang.String, ? extends com.sun.jdi.connect.Connector.Argument>)

,

TransportService.attach(java.lang.String, long, long)

,

TransportService.accept(com.sun.jdi.connect.spi.TransportService.ListenKey, long, long)

,

Serialized Form

public class

TransportTimeoutException

extends

IOException

This exception may be thrown as a result of a timeout
when attaching to a target VM, or waiting to accept a
connection from a target VM.

When attaching to a target VM, using

attach

this
exception may be thrown if the connector supports a timeout

connector argument

. Similiarly,
when waiting to accept a connection from a target VM,
using

accept

this
exception may be thrown if the connector supports a
timeout connector argument when accepting.

In addition, for developers creating

TransportService

implementations this exception is thrown when

attach

times out when establishing a
connection to a target VM, or

accept

times out while waiting for a target VM to connect.

When attaching to a target VM, using

attach

this
exception may be thrown if the connector supports a timeout

connector argument

. Similiarly,
when waiting to accept a connection from a target VM,
using

accept

this
exception may be thrown if the connector supports a
timeout connector argument when accepting.

In addition, for developers creating

TransportService

implementations this exception is thrown when

attach

times out when establishing a
connection to a target VM, or

accept

times out while waiting for a target VM to connect.

In addition, for developers creating

TransportService

implementations this exception is thrown when

attach

times out when establishing a
connection to a target VM, or

accept

times out while waiting for a target VM to connect.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

TransportTimeoutException

()

Constructs a

TransportTimeoutException

with no detail
message.

TransportTimeoutException

​(

String

message)

Constructs a

TransportTimeoutException

with the
specified detail message.

========== METHOD SUMMARY ===========

- Method Summary

- Methods declared in class java.lang.

Throwable

addSuppressed

,

fillInStackTrace

,

getCause

,

getLocalizedMessage

,

getMessage

,

getStackTrace

,

getSuppressed

,

initCause

,

printStackTrace

,

printStackTrace

,

printStackTrace

,

setStackTrace

,

toString

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

Constructor Summary

Constructors

Constructor

Description

TransportTimeoutException

()

Constructs a

TransportTimeoutException

with no detail
message.

TransportTimeoutException

​(

String

message)

Constructs a

TransportTimeoutException

with the
specified detail message.

---

#### Constructor Summary

Constructs a

TransportTimeoutException

with no detail
message.

Constructs a

TransportTimeoutException

with the
specified detail message.

Method Summary

- Methods declared in class java.lang.

Throwable

addSuppressed

,

fillInStackTrace

,

getCause

,

getLocalizedMessage

,

getMessage

,

getStackTrace

,

getSuppressed

,

initCause

,

printStackTrace

,

printStackTrace

,

printStackTrace

,

setStackTrace

,

toString

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

Methods declared in class java.lang.

Throwable

addSuppressed

,

fillInStackTrace

,

getCause

,

getLocalizedMessage

,

getMessage

,

getStackTrace

,

getSuppressed

,

initCause

,

printStackTrace

,

printStackTrace

,

printStackTrace

,

setStackTrace

,

toString

---

#### Methods declared in class java.lang. Throwable

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

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- TransportTimeoutException

```java
public TransportTimeoutException()
```

Constructs a

TransportTimeoutException

with no detail
message.

- TransportTimeoutException

```java
public TransportTimeoutException​(
String
message)
```

Constructs a

TransportTimeoutException

with the
specified detail message.

**Parameters:** message

- the detail message pertaining to this exception.

Constructor Detail

- TransportTimeoutException

```java
public TransportTimeoutException()
```

Constructs a

TransportTimeoutException

with no detail
message.

- TransportTimeoutException

```java
public TransportTimeoutException​(
String
message)
```

Constructs a

TransportTimeoutException

with the
specified detail message.

**Parameters:** message

- the detail message pertaining to this exception.

---

#### Constructor Detail

TransportTimeoutException

```java
public TransportTimeoutException()
```

Constructs a

TransportTimeoutException

with no detail
message.

---

#### TransportTimeoutException

public TransportTimeoutException()

Constructs a

TransportTimeoutException

with no detail
message.

TransportTimeoutException

```java
public TransportTimeoutException​(
String
message)
```

Constructs a

TransportTimeoutException

with the
specified detail message.

**Parameters:** message

- the detail message pertaining to this exception.

---

#### TransportTimeoutException

public TransportTimeoutException​(

String

message)

Constructs a

TransportTimeoutException

with the
specified detail message.

---

