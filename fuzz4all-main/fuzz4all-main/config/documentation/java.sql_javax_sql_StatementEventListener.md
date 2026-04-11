# Interface StatementEventListener

**Source:** `java.sql\javax\sql\StatementEventListener.html`

### Class Description

```java
public interface
StatementEventListener

extends
EventListener
```

An object that registers to be notified of events that occur on PreparedStatements
that are in the Statement pool.

The JDBC 3.0 specification added the maxStatements

ConnectionPooledDataSource

property to provide a standard mechanism for
enabling the pooling of

PreparedStatements

and to specify the size of the statement
pool. However, there was no way for a driver to notify an external
statement pool when a

PreparedStatement

becomes invalid. For some databases, a
statement becomes invalid if a DDL operation is performed that affects the
table. For example an application may create a temporary table to do some work
on the table and then destroy it. It may later recreate the same table when
it is needed again. Some databases will invalidate any prepared statements
that reference the temporary table when the table is dropped.

Similar to the methods defined in the

ConnectionEventListener

interface,
the driver will call the

StatementEventListener.statementErrorOccurred

method prior to throwing any exceptions when it detects a statement is invalid.
The driver will also call the

StatementEventListener.statementClosed

method when a

PreparedStatement

is closed.

Methods which allow a component to register a StatementEventListener with a

PooledConnection

have been added to the

PooledConnection

interface.

**All Superinterfaces:** EventListener

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### void statementClosed​(
StatementEvent
event)

The driver calls this method on all

StatementEventListener

s registered on the connection when it detects that a

PreparedStatement

is closed.

**Parameters:**
- event

- an event object describing the source of
the event and that the

PreparedStatement

was closed.

**Since:**
- 1.6

---

#### void statementErrorOccurred​(
StatementEvent
event)

The driver calls this method on all

StatementEventListener

s
registered on the connection when it detects that a

PreparedStatement

is invalid. The driver calls this method
just before it throws the

SQLException

,
contained in the given event, to the application.

**Parameters:**
- event

- an event object describing the source of the event,
the statement that is invalid and the exception the
driver is about to throw. The source of the event is
the

PooledConnection

which the invalid

PreparedStatement

is associated with.

**Since:**
- 1.6

---

### Additional Sections

#### Interface StatementEventListener

**All Superinterfaces:** EventListener

```java
public interface
StatementEventListener

extends
EventListener
```

An object that registers to be notified of events that occur on PreparedStatements
that are in the Statement pool.

The JDBC 3.0 specification added the maxStatements

ConnectionPooledDataSource

property to provide a standard mechanism for
enabling the pooling of

PreparedStatements

and to specify the size of the statement
pool. However, there was no way for a driver to notify an external
statement pool when a

PreparedStatement

becomes invalid. For some databases, a
statement becomes invalid if a DDL operation is performed that affects the
table. For example an application may create a temporary table to do some work
on the table and then destroy it. It may later recreate the same table when
it is needed again. Some databases will invalidate any prepared statements
that reference the temporary table when the table is dropped.

Similar to the methods defined in the

ConnectionEventListener

interface,
the driver will call the

StatementEventListener.statementErrorOccurred

method prior to throwing any exceptions when it detects a statement is invalid.
The driver will also call the

StatementEventListener.statementClosed

method when a

PreparedStatement

is closed.

Methods which allow a component to register a StatementEventListener with a

PooledConnection

have been added to the

PooledConnection

interface.

**Since:** 1.6

public interface

StatementEventListener

extends

EventListener

An object that registers to be notified of events that occur on PreparedStatements
that are in the Statement pool.

The JDBC 3.0 specification added the maxStatements

ConnectionPooledDataSource

property to provide a standard mechanism for
enabling the pooling of

PreparedStatements

and to specify the size of the statement
pool. However, there was no way for a driver to notify an external
statement pool when a

PreparedStatement

becomes invalid. For some databases, a
statement becomes invalid if a DDL operation is performed that affects the
table. For example an application may create a temporary table to do some work
on the table and then destroy it. It may later recreate the same table when
it is needed again. Some databases will invalidate any prepared statements
that reference the temporary table when the table is dropped.

Similar to the methods defined in the

ConnectionEventListener

interface,
the driver will call the

StatementEventListener.statementErrorOccurred

method prior to throwing any exceptions when it detects a statement is invalid.
The driver will also call the

StatementEventListener.statementClosed

method when a

PreparedStatement

is closed.

Methods which allow a component to register a StatementEventListener with a

PooledConnection

have been added to the

PooledConnection

interface.

The JDBC 3.0 specification added the maxStatements

ConnectionPooledDataSource

property to provide a standard mechanism for
enabling the pooling of

PreparedStatements

and to specify the size of the statement
pool. However, there was no way for a driver to notify an external
statement pool when a

PreparedStatement

becomes invalid. For some databases, a
statement becomes invalid if a DDL operation is performed that affects the
table. For example an application may create a temporary table to do some work
on the table and then destroy it. It may later recreate the same table when
it is needed again. Some databases will invalidate any prepared statements
that reference the temporary table when the table is dropped.

Similar to the methods defined in the

ConnectionEventListener

interface,
the driver will call the

StatementEventListener.statementErrorOccurred

method prior to throwing any exceptions when it detects a statement is invalid.
The driver will also call the

StatementEventListener.statementClosed

method when a

PreparedStatement

is closed.

Methods which allow a component to register a StatementEventListener with a

PooledConnection

have been added to the

PooledConnection

interface.

Similar to the methods defined in the

ConnectionEventListener

interface,
the driver will call the

StatementEventListener.statementErrorOccurred

method prior to throwing any exceptions when it detects a statement is invalid.
The driver will also call the

StatementEventListener.statementClosed

method when a

PreparedStatement

is closed.

Methods which allow a component to register a StatementEventListener with a

PooledConnection

have been added to the

PooledConnection

interface.

Methods which allow a component to register a StatementEventListener with a

PooledConnection

have been added to the

PooledConnection

interface.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

statementClosed

​(

StatementEvent

event)

The driver calls this method on all

StatementEventListener

s registered on the connection when it detects that a

PreparedStatement

is closed.

void

statementErrorOccurred

​(

StatementEvent

event)

The driver calls this method on all

StatementEventListener

s
registered on the connection when it detects that a

PreparedStatement

is invalid.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

statementClosed

​(

StatementEvent

event)

The driver calls this method on all

StatementEventListener

s registered on the connection when it detects that a

PreparedStatement

is closed.

void

statementErrorOccurred

​(

StatementEvent

event)

The driver calls this method on all

StatementEventListener

s
registered on the connection when it detects that a

PreparedStatement

is invalid.

---

#### Method Summary

The driver calls this method on all

StatementEventListener

s registered on the connection when it detects that a

PreparedStatement

is closed.

The driver calls this method on all

StatementEventListener

s
registered on the connection when it detects that a

PreparedStatement

is invalid.

============ METHOD DETAIL ==========

- Method Detail

- statementClosed

```java
void statementClosed​(
StatementEvent
event)
```

The driver calls this method on all

StatementEventListener

s registered on the connection when it detects that a

PreparedStatement

is closed.

**Parameters:** event

- an event object describing the source of
the event and that the

PreparedStatement

was closed.
**Since:** 1.6

- statementErrorOccurred

```java
void statementErrorOccurred​(
StatementEvent
event)
```

The driver calls this method on all

StatementEventListener

s
registered on the connection when it detects that a

PreparedStatement

is invalid. The driver calls this method
just before it throws the

SQLException

,
contained in the given event, to the application.

**Parameters:** event

- an event object describing the source of the event,
the statement that is invalid and the exception the
driver is about to throw. The source of the event is
the

PooledConnection

which the invalid

PreparedStatement

is associated with.
**Since:** 1.6

Method Detail

- statementClosed

```java
void statementClosed​(
StatementEvent
event)
```

The driver calls this method on all

StatementEventListener

s registered on the connection when it detects that a

PreparedStatement

is closed.

**Parameters:** event

- an event object describing the source of
the event and that the

PreparedStatement

was closed.
**Since:** 1.6

- statementErrorOccurred

```java
void statementErrorOccurred​(
StatementEvent
event)
```

The driver calls this method on all

StatementEventListener

s
registered on the connection when it detects that a

PreparedStatement

is invalid. The driver calls this method
just before it throws the

SQLException

,
contained in the given event, to the application.

**Parameters:** event

- an event object describing the source of the event,
the statement that is invalid and the exception the
driver is about to throw. The source of the event is
the

PooledConnection

which the invalid

PreparedStatement

is associated with.
**Since:** 1.6

---

#### Method Detail

statementClosed

```java
void statementClosed​(
StatementEvent
event)
```

The driver calls this method on all

StatementEventListener

s registered on the connection when it detects that a

PreparedStatement

is closed.

**Parameters:** event

- an event object describing the source of
the event and that the

PreparedStatement

was closed.
**Since:** 1.6

---

#### statementClosed

void statementClosed​(

StatementEvent

event)

The driver calls this method on all

StatementEventListener

s registered on the connection when it detects that a

PreparedStatement

is closed.

statementErrorOccurred

```java
void statementErrorOccurred​(
StatementEvent
event)
```

The driver calls this method on all

StatementEventListener

s
registered on the connection when it detects that a

PreparedStatement

is invalid. The driver calls this method
just before it throws the

SQLException

,
contained in the given event, to the application.

**Parameters:** event

- an event object describing the source of the event,
the statement that is invalid and the exception the
driver is about to throw. The source of the event is
the

PooledConnection

which the invalid

PreparedStatement

is associated with.
**Since:** 1.6

---

#### statementErrorOccurred

void statementErrorOccurred​(

StatementEvent

event)

The driver calls this method on all

StatementEventListener

s
registered on the connection when it detects that a

PreparedStatement

is invalid. The driver calls this method
just before it throws the

SQLException

,
contained in the given event, to the application.

---

