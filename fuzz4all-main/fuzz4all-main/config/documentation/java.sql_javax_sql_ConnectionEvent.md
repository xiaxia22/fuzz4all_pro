# Class ConnectionEvent

**Source:** `java.sql\javax\sql\ConnectionEvent.html`

### Class Description

```java
public class
ConnectionEvent

extends
EventObject
```

An

Event

object that provides information about the
source of a connection-related event.

ConnectionEvent

objects are generated when an application closes a pooled connection
and when an error occurs. The

ConnectionEvent

object
contains two kinds of information:

- The pooled connection closed by the application

In the case of an error event, the

SQLException

about to be thrown to the application

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public ConnectionEvent​(
PooledConnection
con)

Constructs a

ConnectionEvent

object initialized with
the given

PooledConnection

object.

SQLException

defaults to

null

.

**Parameters:**
- con

- the pooled connection that is the source of the event

**Throws:**
- IllegalArgumentException

- if

con

is null.

---

#### public ConnectionEvent​(
PooledConnection
con,

SQLException
ex)

Constructs a

ConnectionEvent

object initialized with
the given

PooledConnection

object and

SQLException

object.

**Parameters:**
- con

- the pooled connection that is the source of the event
- ex

- the SQLException about to be thrown to the application

**Throws:**
- IllegalArgumentException

- if

con

is null.

---

### Method Details

#### public
SQLException
getSQLException()

Retrieves the

SQLException

for this

ConnectionEvent

object. May be

null

.

**Returns:**
- the SQLException about to be thrown or

null

---

### Additional Sections

#### Class ConnectionEvent

java.lang.Object

- java.util.EventObject
- - javax.sql.ConnectionEvent

java.util.EventObject

- javax.sql.ConnectionEvent

javax.sql.ConnectionEvent

**All Implemented Interfaces:** Serializable

```java
public class
ConnectionEvent

extends
EventObject
```

An

Event

object that provides information about the
source of a connection-related event.

ConnectionEvent

objects are generated when an application closes a pooled connection
and when an error occurs. The

ConnectionEvent

object
contains two kinds of information:

- The pooled connection closed by the application

In the case of an error event, the

SQLException

about to be thrown to the application

**Since:** 1.4
**See Also:** Serialized Form

public class

ConnectionEvent

extends

EventObject

An

Event

object that provides information about the
source of a connection-related event.

ConnectionEvent

objects are generated when an application closes a pooled connection
and when an error occurs. The

ConnectionEvent

object
contains two kinds of information:

- The pooled connection closed by the application

In the case of an error event, the

SQLException

about to be thrown to the application

The pooled connection closed by the application

In the case of an error event, the

SQLException

about to be thrown to the application

=========== FIELD SUMMARY ===========

- Field Summary

- Fields declared in class java.util.

EventObject

source

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

ConnectionEvent

​(

PooledConnection

con)

Constructs a

ConnectionEvent

object initialized with
the given

PooledConnection

object.

ConnectionEvent

​(

PooledConnection

con,

SQLException

ex)

Constructs a

ConnectionEvent

object initialized with
the given

PooledConnection

object and

SQLException

object.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

SQLException

getSQLException

()

Retrieves the

SQLException

for this

ConnectionEvent

object.

- Methods declared in class java.util.

EventObject

getSource

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

Field Summary

- Fields declared in class java.util.

EventObject

source

---

#### Field Summary

Fields declared in class java.util.

EventObject

source

---

#### Fields declared in class java.util. EventObject

Constructor Summary

Constructors

Constructor

Description

ConnectionEvent

​(

PooledConnection

con)

Constructs a

ConnectionEvent

object initialized with
the given

PooledConnection

object.

ConnectionEvent

​(

PooledConnection

con,

SQLException

ex)

Constructs a

ConnectionEvent

object initialized with
the given

PooledConnection

object and

SQLException

object.

---

#### Constructor Summary

Constructs a

ConnectionEvent

object initialized with
the given

PooledConnection

object.

Constructs a

ConnectionEvent

object initialized with
the given

PooledConnection

object and

SQLException

object.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

SQLException

getSQLException

()

Retrieves the

SQLException

for this

ConnectionEvent

object.

- Methods declared in class java.util.

EventObject

getSource

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

Retrieves the

SQLException

for this

ConnectionEvent

object.

Methods declared in class java.util.

EventObject

getSource

,

toString

---

#### Methods declared in class java.util. EventObject

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

- ConnectionEvent

```java
public ConnectionEvent​(
PooledConnection
con)
```

Constructs a

ConnectionEvent

object initialized with
the given

PooledConnection

object.

SQLException

defaults to

null

.

**Parameters:** con

- the pooled connection that is the source of the event
**Throws:** IllegalArgumentException

- if

con

is null.

- ConnectionEvent

```java
public ConnectionEvent​(
PooledConnection
con,

SQLException
ex)
```

Constructs a

ConnectionEvent

object initialized with
the given

PooledConnection

object and

SQLException

object.

**Parameters:** con

- the pooled connection that is the source of the event
**Parameters:** ex

- the SQLException about to be thrown to the application
**Throws:** IllegalArgumentException

- if

con

is null.

============ METHOD DETAIL ==========

- Method Detail

- getSQLException

```java
public
SQLException
getSQLException()
```

Retrieves the

SQLException

for this

ConnectionEvent

object. May be

null

.

**Returns:** the SQLException about to be thrown or

null

Constructor Detail

- ConnectionEvent

```java
public ConnectionEvent​(
PooledConnection
con)
```

Constructs a

ConnectionEvent

object initialized with
the given

PooledConnection

object.

SQLException

defaults to

null

.

**Parameters:** con

- the pooled connection that is the source of the event
**Throws:** IllegalArgumentException

- if

con

is null.

- ConnectionEvent

```java
public ConnectionEvent​(
PooledConnection
con,

SQLException
ex)
```

Constructs a

ConnectionEvent

object initialized with
the given

PooledConnection

object and

SQLException

object.

**Parameters:** con

- the pooled connection that is the source of the event
**Parameters:** ex

- the SQLException about to be thrown to the application
**Throws:** IllegalArgumentException

- if

con

is null.

---

#### Constructor Detail

ConnectionEvent

```java
public ConnectionEvent​(
PooledConnection
con)
```

Constructs a

ConnectionEvent

object initialized with
the given

PooledConnection

object.

SQLException

defaults to

null

.

**Parameters:** con

- the pooled connection that is the source of the event
**Throws:** IllegalArgumentException

- if

con

is null.

---

#### ConnectionEvent

public ConnectionEvent​(

PooledConnection

con)

Constructs a

ConnectionEvent

object initialized with
the given

PooledConnection

object.

SQLException

defaults to

null

.

ConnectionEvent

```java
public ConnectionEvent​(
PooledConnection
con,

SQLException
ex)
```

Constructs a

ConnectionEvent

object initialized with
the given

PooledConnection

object and

SQLException

object.

**Parameters:** con

- the pooled connection that is the source of the event
**Parameters:** ex

- the SQLException about to be thrown to the application
**Throws:** IllegalArgumentException

- if

con

is null.

---

#### ConnectionEvent

public ConnectionEvent​(

PooledConnection

con,

SQLException

ex)

Constructs a

ConnectionEvent

object initialized with
the given

PooledConnection

object and

SQLException

object.

Method Detail

- getSQLException

```java
public
SQLException
getSQLException()
```

Retrieves the

SQLException

for this

ConnectionEvent

object. May be

null

.

**Returns:** the SQLException about to be thrown or

null

---

#### Method Detail

getSQLException

```java
public
SQLException
getSQLException()
```

Retrieves the

SQLException

for this

ConnectionEvent

object. May be

null

.

**Returns:** the SQLException about to be thrown or

null

---

#### getSQLException

public

SQLException

getSQLException()

Retrieves the

SQLException

for this

ConnectionEvent

object. May be

null

.

---

