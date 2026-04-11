# Interface Transport

**Source:** `jdk.jdi\com\sun\jdi\connect\Transport.html`

### Class Description

```java
public interface
Transport
```

A method of communication between a debugger and a target VM.

A Transport represents the transport mechanism used by a

Connector

to establish a connection with a
target VM. It consists of a name which is obtained by invoking
the

name()

method. Furthermore, a Transport encapsulates a

TransportService

which is the underlying
service used to establish connections and exchange
Java Debug Wire Protocol (JDWP) packets with a target VM.

**Since:** 1.3

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### String
name()

Returns a short identifier for the transport.

**Returns:**
- the name of this transport.

---

### Additional Sections

#### Interface Transport

```java
public interface
Transport
```

A method of communication between a debugger and a target VM.

A Transport represents the transport mechanism used by a

Connector

to establish a connection with a
target VM. It consists of a name which is obtained by invoking
the

name()

method. Furthermore, a Transport encapsulates a

TransportService

which is the underlying
service used to establish connections and exchange
Java Debug Wire Protocol (JDWP) packets with a target VM.

**Since:** 1.3

public interface

Transport

A method of communication between a debugger and a target VM.

A Transport represents the transport mechanism used by a

Connector

to establish a connection with a
target VM. It consists of a name which is obtained by invoking
the

name()

method. Furthermore, a Transport encapsulates a

TransportService

which is the underlying
service used to establish connections and exchange
Java Debug Wire Protocol (JDWP) packets with a target VM.

A Transport represents the transport mechanism used by a

Connector

to establish a connection with a
target VM. It consists of a name which is obtained by invoking
the

name()

method. Furthermore, a Transport encapsulates a

TransportService

which is the underlying
service used to establish connections and exchange
Java Debug Wire Protocol (JDWP) packets with a target VM.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

String

name

()

Returns a short identifier for the transport.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

String

name

()

Returns a short identifier for the transport.

---

#### Method Summary

Returns a short identifier for the transport.

============ METHOD DETAIL ==========

- Method Detail

- name

```java
String
name()
```

Returns a short identifier for the transport.

**Returns:** the name of this transport.

Method Detail

- name

```java
String
name()
```

Returns a short identifier for the transport.

**Returns:** the name of this transport.

---

#### Method Detail

name

```java
String
name()
```

Returns a short identifier for the transport.

**Returns:** the name of this transport.

---

#### name

String

name()

Returns a short identifier for the transport.

---

