# Class TransportService.Capabilities

**Source:** `jdk.jdi\com\sun\jdi\connect\spi\TransportService.Capabilities.html`

### Class Description

```java
public abstract static class
TransportService.Capabilities

extends
Object
```

The transport service capabilities.

**Enclosing class:** TransportService

---

### Field Details

*No entries found.*

### Constructor Details

#### public Capabilities()

*No description found.*

---

### Method Details

#### public abstract boolean supportsMultipleConnections()

Tells whether or not this transport service can support
multiple concurrent connections to a single address that
it is listening on.

**Returns:**
- true

if, and only if, this transport
service supports multiple connections.

---

#### public abstract boolean supportsAttachTimeout()

Tell whether or not this transport service supports a timeout
when attaching to a target VM.

**Returns:**
- true

if, and only if, this transport
service supports attaching with a timeout.

**See Also:**
- TransportService.attach(String,long,long)

---

#### public abstract boolean supportsAcceptTimeout()

Tell whether or not this transport service supports a
timeout while waiting for a target VM to connect.

**Returns:**
- true

if, and only if, this transport
service supports timeout while waiting for
a target VM to connect.

**See Also:**
- TransportService.accept(TransportService.ListenKey,long,long)

---

#### public abstract boolean supportsHandshakeTimeout()

Tells whether or not this transport service supports a
timeout when handshaking with the target VM.

**Returns:**
- true

if, and only if, this transport
service supports a timeout while handshaking
with the target VM.

**See Also:**
- TransportService.attach(String,long,long)

,

TransportService.accept(TransportService.ListenKey,long,long)

---

### Additional Sections

#### Class TransportService.Capabilities

java.lang.Object

- com.sun.jdi.connect.spi.TransportService.Capabilities

com.sun.jdi.connect.spi.TransportService.Capabilities

**Enclosing class:** TransportService

```java
public abstract static class
TransportService.Capabilities

extends
Object
```

The transport service capabilities.

public abstract static class

TransportService.Capabilities

extends

Object

The transport service capabilities.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

Capabilities

()

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

abstract boolean

supportsAcceptTimeout

()

Tell whether or not this transport service supports a
timeout while waiting for a target VM to connect.

abstract boolean

supportsAttachTimeout

()

Tell whether or not this transport service supports a timeout
when attaching to a target VM.

abstract boolean

supportsHandshakeTimeout

()

Tells whether or not this transport service supports a
timeout when handshaking with the target VM.

abstract boolean

supportsMultipleConnections

()

Tells whether or not this transport service can support
multiple concurrent connections to a single address that
it is listening on.

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

Constructor Summary

Constructors

Constructor

Description

Capabilities

()

---

#### Constructor Summary

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

abstract boolean

supportsAcceptTimeout

()

Tell whether or not this transport service supports a
timeout while waiting for a target VM to connect.

abstract boolean

supportsAttachTimeout

()

Tell whether or not this transport service supports a timeout
when attaching to a target VM.

abstract boolean

supportsHandshakeTimeout

()

Tells whether or not this transport service supports a
timeout when handshaking with the target VM.

abstract boolean

supportsMultipleConnections

()

Tells whether or not this transport service can support
multiple concurrent connections to a single address that
it is listening on.

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

Tell whether or not this transport service supports a
timeout while waiting for a target VM to connect.

Tell whether or not this transport service supports a timeout
when attaching to a target VM.

Tells whether or not this transport service supports a
timeout when handshaking with the target VM.

Tells whether or not this transport service can support
multiple concurrent connections to a single address that
it is listening on.

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

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- Capabilities

```java
public Capabilities()
```

============ METHOD DETAIL ==========

- Method Detail

- supportsMultipleConnections

```java
public abstract boolean supportsMultipleConnections()
```

Tells whether or not this transport service can support
multiple concurrent connections to a single address that
it is listening on.

**Returns:** true

if, and only if, this transport
service supports multiple connections.

- supportsAttachTimeout

```java
public abstract boolean supportsAttachTimeout()
```

Tell whether or not this transport service supports a timeout
when attaching to a target VM.

**Returns:** true

if, and only if, this transport
service supports attaching with a timeout.
**See Also:** TransportService.attach(String,long,long)

- supportsAcceptTimeout

```java
public abstract boolean supportsAcceptTimeout()
```

Tell whether or not this transport service supports a
timeout while waiting for a target VM to connect.

**Returns:** true

if, and only if, this transport
service supports timeout while waiting for
a target VM to connect.
**See Also:** TransportService.accept(TransportService.ListenKey,long,long)

- supportsHandshakeTimeout

```java
public abstract boolean supportsHandshakeTimeout()
```

Tells whether or not this transport service supports a
timeout when handshaking with the target VM.

**Returns:** true

if, and only if, this transport
service supports a timeout while handshaking
with the target VM.
**See Also:** TransportService.attach(String,long,long)

,

TransportService.accept(TransportService.ListenKey,long,long)

Constructor Detail

- Capabilities

```java
public Capabilities()
```

---

#### Constructor Detail

Capabilities

```java
public Capabilities()
```

---

#### Capabilities

public Capabilities()

Method Detail

- supportsMultipleConnections

```java
public abstract boolean supportsMultipleConnections()
```

Tells whether or not this transport service can support
multiple concurrent connections to a single address that
it is listening on.

**Returns:** true

if, and only if, this transport
service supports multiple connections.

- supportsAttachTimeout

```java
public abstract boolean supportsAttachTimeout()
```

Tell whether or not this transport service supports a timeout
when attaching to a target VM.

**Returns:** true

if, and only if, this transport
service supports attaching with a timeout.
**See Also:** TransportService.attach(String,long,long)

- supportsAcceptTimeout

```java
public abstract boolean supportsAcceptTimeout()
```

Tell whether or not this transport service supports a
timeout while waiting for a target VM to connect.

**Returns:** true

if, and only if, this transport
service supports timeout while waiting for
a target VM to connect.
**See Also:** TransportService.accept(TransportService.ListenKey,long,long)

- supportsHandshakeTimeout

```java
public abstract boolean supportsHandshakeTimeout()
```

Tells whether or not this transport service supports a
timeout when handshaking with the target VM.

**Returns:** true

if, and only if, this transport
service supports a timeout while handshaking
with the target VM.
**See Also:** TransportService.attach(String,long,long)

,

TransportService.accept(TransportService.ListenKey,long,long)

---

#### Method Detail

supportsMultipleConnections

```java
public abstract boolean supportsMultipleConnections()
```

Tells whether or not this transport service can support
multiple concurrent connections to a single address that
it is listening on.

**Returns:** true

if, and only if, this transport
service supports multiple connections.

---

#### supportsMultipleConnections

public abstract boolean supportsMultipleConnections()

Tells whether or not this transport service can support
multiple concurrent connections to a single address that
it is listening on.

supportsAttachTimeout

```java
public abstract boolean supportsAttachTimeout()
```

Tell whether or not this transport service supports a timeout
when attaching to a target VM.

**Returns:** true

if, and only if, this transport
service supports attaching with a timeout.
**See Also:** TransportService.attach(String,long,long)

---

#### supportsAttachTimeout

public abstract boolean supportsAttachTimeout()

Tell whether or not this transport service supports a timeout
when attaching to a target VM.

supportsAcceptTimeout

```java
public abstract boolean supportsAcceptTimeout()
```

Tell whether or not this transport service supports a
timeout while waiting for a target VM to connect.

**Returns:** true

if, and only if, this transport
service supports timeout while waiting for
a target VM to connect.
**See Also:** TransportService.accept(TransportService.ListenKey,long,long)

---

#### supportsAcceptTimeout

public abstract boolean supportsAcceptTimeout()

Tell whether or not this transport service supports a
timeout while waiting for a target VM to connect.

supportsHandshakeTimeout

```java
public abstract boolean supportsHandshakeTimeout()
```

Tells whether or not this transport service supports a
timeout when handshaking with the target VM.

**Returns:** true

if, and only if, this transport
service supports a timeout while handshaking
with the target VM.
**See Also:** TransportService.attach(String,long,long)

,

TransportService.accept(TransportService.ListenKey,long,long)

---

#### supportsHandshakeTimeout

public abstract boolean supportsHandshakeTimeout()

Tells whether or not this transport service supports a
timeout when handshaking with the target VM.

---

