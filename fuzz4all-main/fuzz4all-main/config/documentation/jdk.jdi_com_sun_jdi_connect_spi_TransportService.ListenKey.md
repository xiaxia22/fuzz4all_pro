# Class TransportService.ListenKey

**Source:** `jdk.jdi\com\sun\jdi\connect\spi\TransportService.ListenKey.html`

### Class Description

```java
public abstract static class
TransportService.ListenKey

extends
Object
```

A

listen key

.

A

TransportService

may listen on multiple, yet
different, addresses at the same time. To uniquely identify
each

listener

a listen key is created each time that

startListening

is called. The listen
key is used in calls to the

accept

method
to accept inbound connections to that listener. A listen
key is valid until it is used as an argument to

stopListening

to stop the transport
service from listening on an address.

**Enclosing class:** TransportService

---

### Field Details

*No entries found.*

### Constructor Details

#### public ListenKey()

*No description found.*

---

### Method Details

#### public abstract
String
address()

Returns a string representation of the listen key.

---

### Additional Sections

#### Class TransportService.ListenKey

java.lang.Object

- com.sun.jdi.connect.spi.TransportService.ListenKey

com.sun.jdi.connect.spi.TransportService.ListenKey

**Enclosing class:** TransportService

```java
public abstract static class
TransportService.ListenKey

extends
Object
```

A

listen key

.

A

TransportService

may listen on multiple, yet
different, addresses at the same time. To uniquely identify
each

listener

a listen key is created each time that

startListening

is called. The listen
key is used in calls to the

accept

method
to accept inbound connections to that listener. A listen
key is valid until it is used as an argument to

stopListening

to stop the transport
service from listening on an address.

public abstract static class

TransportService.ListenKey

extends

Object

A

listen key

.

A

TransportService

may listen on multiple, yet
different, addresses at the same time. To uniquely identify
each

listener

a listen key is created each time that

startListening

is called. The listen
key is used in calls to the

accept

method
to accept inbound connections to that listener. A listen
key is valid until it is used as an argument to

stopListening

to stop the transport
service from listening on an address.

A

TransportService

may listen on multiple, yet
different, addresses at the same time. To uniquely identify
each

listener

a listen key is created each time that

startListening

is called. The listen
key is used in calls to the

accept

method
to accept inbound connections to that listener. A listen
key is valid until it is used as an argument to

stopListening

to stop the transport
service from listening on an address.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

ListenKey

()

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

abstract

String

address

()

Returns a string representation of the listen key.

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

ListenKey

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

abstract

String

address

()

Returns a string representation of the listen key.

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

Returns a string representation of the listen key.

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

- ListenKey

```java
public ListenKey()
```

============ METHOD DETAIL ==========

- Method Detail

- address

```java
public abstract
String
address()
```

Returns a string representation of the listen key.

Constructor Detail

- ListenKey

```java
public ListenKey()
```

---

#### Constructor Detail

ListenKey

```java
public ListenKey()
```

---

#### ListenKey

public ListenKey()

Method Detail

- address

```java
public abstract
String
address()
```

Returns a string representation of the listen key.

---

#### Method Detail

address

```java
public abstract
String
address()
```

Returns a string representation of the listen key.

---

#### address

public abstract

String

address()

Returns a string representation of the listen key.

---

