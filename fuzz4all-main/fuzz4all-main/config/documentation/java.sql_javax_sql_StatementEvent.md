# Class StatementEvent

**Source:** `java.sql\javax\sql\StatementEvent.html`

### Class Description

```java
public class
StatementEvent

extends
EventObject
```

A

StatementEvent

is sent to all

StatementEventListener

s which were
registered with a

PooledConnection

. This occurs when the driver determines that a

PreparedStatement

that is associated with the

PooledConnection

has been closed or the driver determines
is invalid.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public StatementEvent​(
PooledConnection
con,

PreparedStatement
statement)

Constructs a

StatementEvent

with the specified

PooledConnection

and

PreparedStatement

. The

SQLException

contained in the event defaults to
null.

**Parameters:**
- con

- The

PooledConnection

that the closed or invalid

PreparedStatement

is associated with.
- statement

- The

PreparedStatement

that is being closed or is invalid

**Throws:**
- IllegalArgumentException

- if

con

is null.

**Since:**
- 1.6

---

#### public StatementEvent​(
PooledConnection
con,

PreparedStatement
statement,

SQLException
exception)

Constructs a

StatementEvent

with the specified

PooledConnection

,

PreparedStatement

and

SQLException

**Parameters:**
- con

- The

PooledConnection

that the closed or invalid

PreparedStatement

is associated with.
- statement

- The

PreparedStatement

that is being closed or is invalid
- exception

- The

SQLException

the driver is about to throw to
the application

**Throws:**
- IllegalArgumentException

- if

con

is null.

**Since:**
- 1.6

---

### Method Details

#### public
PreparedStatement
getStatement()

Returns the

PreparedStatement

that is being closed or is invalid

**Returns:**
- The

PreparedStatement

that is being closed or is invalid

**Since:**
- 1.6

---

#### public
SQLException
getSQLException()

Returns the

SQLException

the driver is about to throw

**Returns:**
- The

SQLException

the driver is about to throw

**Since:**
- 1.6

---

### Additional Sections

#### Class StatementEvent

java.lang.Object

- java.util.EventObject
- - javax.sql.StatementEvent

java.util.EventObject

- javax.sql.StatementEvent

javax.sql.StatementEvent

**All Implemented Interfaces:** Serializable

```java
public class
StatementEvent

extends
EventObject
```

A

StatementEvent

is sent to all

StatementEventListener

s which were
registered with a

PooledConnection

. This occurs when the driver determines that a

PreparedStatement

that is associated with the

PooledConnection

has been closed or the driver determines
is invalid.

**Since:** 1.6
**See Also:** Serialized Form

public class

StatementEvent

extends

EventObject

A

StatementEvent

is sent to all

StatementEventListener

s which were
registered with a

PooledConnection

. This occurs when the driver determines that a

PreparedStatement

that is associated with the

PooledConnection

has been closed or the driver determines
is invalid.

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

StatementEvent

​(

PooledConnection

con,

PreparedStatement

statement)

Constructs a

StatementEvent

with the specified

PooledConnection

and

PreparedStatement

.

StatementEvent

​(

PooledConnection

con,

PreparedStatement

statement,

SQLException

exception)

Constructs a

StatementEvent

with the specified

PooledConnection

,

PreparedStatement

and

SQLException

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

Returns the

SQLException

the driver is about to throw

PreparedStatement

getStatement

()

Returns the

PreparedStatement

that is being closed or is invalid

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

StatementEvent

​(

PooledConnection

con,

PreparedStatement

statement)

Constructs a

StatementEvent

with the specified

PooledConnection

and

PreparedStatement

.

StatementEvent

​(

PooledConnection

con,

PreparedStatement

statement,

SQLException

exception)

Constructs a

StatementEvent

with the specified

PooledConnection

,

PreparedStatement

and

SQLException

---

#### Constructor Summary

Constructs a

StatementEvent

with the specified

PooledConnection

and

PreparedStatement

.

Constructs a

StatementEvent

with the specified

PooledConnection

,

PreparedStatement

and

SQLException

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

Returns the

SQLException

the driver is about to throw

PreparedStatement

getStatement

()

Returns the

PreparedStatement

that is being closed or is invalid

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

Returns the

SQLException

the driver is about to throw

Returns the

PreparedStatement

that is being closed or is invalid

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

- StatementEvent

```java
public StatementEvent​(
PooledConnection
con,

PreparedStatement
statement)
```

Constructs a

StatementEvent

with the specified

PooledConnection

and

PreparedStatement

. The

SQLException

contained in the event defaults to
null.

**Parameters:** con

- The

PooledConnection

that the closed or invalid

PreparedStatement

is associated with.
**Parameters:** statement

- The

PreparedStatement

that is being closed or is invalid
**Throws:** IllegalArgumentException

- if

con

is null.
**Since:** 1.6

- StatementEvent

```java
public StatementEvent​(
PooledConnection
con,

PreparedStatement
statement,

SQLException
exception)
```

Constructs a

StatementEvent

with the specified

PooledConnection

,

PreparedStatement

and

SQLException

**Parameters:** con

- The

PooledConnection

that the closed or invalid

PreparedStatement

is associated with.
**Parameters:** statement

- The

PreparedStatement

that is being closed or is invalid
**Parameters:** exception

- The

SQLException

the driver is about to throw to
the application
**Throws:** IllegalArgumentException

- if

con

is null.
**Since:** 1.6

============ METHOD DETAIL ==========

- Method Detail

- getStatement

```java
public
PreparedStatement
getStatement()
```

Returns the

PreparedStatement

that is being closed or is invalid

**Returns:** The

PreparedStatement

that is being closed or is invalid
**Since:** 1.6

- getSQLException

```java
public
SQLException
getSQLException()
```

Returns the

SQLException

the driver is about to throw

**Returns:** The

SQLException

the driver is about to throw
**Since:** 1.6

Constructor Detail

- StatementEvent

```java
public StatementEvent​(
PooledConnection
con,

PreparedStatement
statement)
```

Constructs a

StatementEvent

with the specified

PooledConnection

and

PreparedStatement

. The

SQLException

contained in the event defaults to
null.

**Parameters:** con

- The

PooledConnection

that the closed or invalid

PreparedStatement

is associated with.
**Parameters:** statement

- The

PreparedStatement

that is being closed or is invalid
**Throws:** IllegalArgumentException

- if

con

is null.
**Since:** 1.6

- StatementEvent

```java
public StatementEvent​(
PooledConnection
con,

PreparedStatement
statement,

SQLException
exception)
```

Constructs a

StatementEvent

with the specified

PooledConnection

,

PreparedStatement

and

SQLException

**Parameters:** con

- The

PooledConnection

that the closed or invalid

PreparedStatement

is associated with.
**Parameters:** statement

- The

PreparedStatement

that is being closed or is invalid
**Parameters:** exception

- The

SQLException

the driver is about to throw to
the application
**Throws:** IllegalArgumentException

- if

con

is null.
**Since:** 1.6

---

#### Constructor Detail

StatementEvent

```java
public StatementEvent​(
PooledConnection
con,

PreparedStatement
statement)
```

Constructs a

StatementEvent

with the specified

PooledConnection

and

PreparedStatement

. The

SQLException

contained in the event defaults to
null.

**Parameters:** con

- The

PooledConnection

that the closed or invalid

PreparedStatement

is associated with.
**Parameters:** statement

- The

PreparedStatement

that is being closed or is invalid
**Throws:** IllegalArgumentException

- if

con

is null.
**Since:** 1.6

---

#### StatementEvent

public StatementEvent​(

PooledConnection

con,

PreparedStatement

statement)

Constructs a

StatementEvent

with the specified

PooledConnection

and

PreparedStatement

. The

SQLException

contained in the event defaults to
null.

StatementEvent

```java
public StatementEvent​(
PooledConnection
con,

PreparedStatement
statement,

SQLException
exception)
```

Constructs a

StatementEvent

with the specified

PooledConnection

,

PreparedStatement

and

SQLException

**Parameters:** con

- The

PooledConnection

that the closed or invalid

PreparedStatement

is associated with.
**Parameters:** statement

- The

PreparedStatement

that is being closed or is invalid
**Parameters:** exception

- The

SQLException

the driver is about to throw to
the application
**Throws:** IllegalArgumentException

- if

con

is null.
**Since:** 1.6

---

#### StatementEvent

public StatementEvent​(

PooledConnection

con,

PreparedStatement

statement,

SQLException

exception)

Constructs a

StatementEvent

with the specified

PooledConnection

,

PreparedStatement

and

SQLException

Method Detail

- getStatement

```java
public
PreparedStatement
getStatement()
```

Returns the

PreparedStatement

that is being closed or is invalid

**Returns:** The

PreparedStatement

that is being closed or is invalid
**Since:** 1.6

- getSQLException

```java
public
SQLException
getSQLException()
```

Returns the

SQLException

the driver is about to throw

**Returns:** The

SQLException

the driver is about to throw
**Since:** 1.6

---

#### Method Detail

getStatement

```java
public
PreparedStatement
getStatement()
```

Returns the

PreparedStatement

that is being closed or is invalid

**Returns:** The

PreparedStatement

that is being closed or is invalid
**Since:** 1.6

---

#### getStatement

public

PreparedStatement

getStatement()

Returns the

PreparedStatement

that is being closed or is invalid

getSQLException

```java
public
SQLException
getSQLException()
```

Returns the

SQLException

the driver is about to throw

**Returns:** The

SQLException

the driver is about to throw
**Since:** 1.6

---

#### getSQLException

public

SQLException

getSQLException()

Returns the

SQLException

the driver is about to throw

---

