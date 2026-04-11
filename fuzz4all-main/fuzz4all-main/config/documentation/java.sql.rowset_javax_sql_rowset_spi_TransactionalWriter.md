# Interface TransactionalWriter

**Source:** `java.sql.rowset\javax\sql\rowset\spi\TransactionalWriter.html`

### Class Description

```java
public interface
TransactionalWriter

extends
RowSetWriter
```

A specialized interface that facilitates an extension of the standard

SyncProvider

abstract class so that it has finer grained
transaction control.

If one or more disconnected

RowSet

objects are participating
in a global transaction, they may wish to coordinate their synchronization
commits to preserve data integrity and reduce the number of
synchronization exceptions. If this is the case, an application should set
the

CachedRowSet

constant

COMMIT_ON_ACCEPT_CHANGES

to

false

and use the

commit

and

rollback

methods defined in this interface to manage transaction boundaries.

**All Superinterfaces:** RowSetWriter

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### void commit()
throws
SQLException

Makes permanent all changes that have been performed by the

acceptChanges

method since the last call to either the

commit

or

rollback

methods.
This method should be used only when auto-commit mode has been disabled.

**Throws:**
- SQLException

- if a database access error occurs or the

Connection

object within this

CachedRowSet

object is in auto-commit mode

---

#### void rollback()
throws
SQLException

Undoes all changes made in the current transaction. This method should be
used only when auto-commit mode has been disabled.

**Throws:**
- SQLException

- if a database access error occurs or the

Connection

object within this

CachedRowSet

object is in auto-commit mode

---

#### void rollback​(
Savepoint
s)
throws
SQLException

Undoes all changes made in the current transaction made prior to the given

Savepoint

object. This method should be used only when auto-commit
mode has been disabled.

**Parameters:**
- s

- a

Savepoint

object marking a savepoint in the current
transaction. All changes made before

s

was set will be undone.
All changes made after

s

was set will be made permanent.

**Throws:**
- SQLException

- if a database access error occurs or the

Connection

object within this

CachedRowSet

object is in auto-commit mode

---

### Additional Sections

#### Interface TransactionalWriter

**All Superinterfaces:** RowSetWriter

```java
public interface
TransactionalWriter

extends
RowSetWriter
```

A specialized interface that facilitates an extension of the standard

SyncProvider

abstract class so that it has finer grained
transaction control.

If one or more disconnected

RowSet

objects are participating
in a global transaction, they may wish to coordinate their synchronization
commits to preserve data integrity and reduce the number of
synchronization exceptions. If this is the case, an application should set
the

CachedRowSet

constant

COMMIT_ON_ACCEPT_CHANGES

to

false

and use the

commit

and

rollback

methods defined in this interface to manage transaction boundaries.

**Since:** 1.5

public interface

TransactionalWriter

extends

RowSetWriter

A specialized interface that facilitates an extension of the standard

SyncProvider

abstract class so that it has finer grained
transaction control.

If one or more disconnected

RowSet

objects are participating
in a global transaction, they may wish to coordinate their synchronization
commits to preserve data integrity and reduce the number of
synchronization exceptions. If this is the case, an application should set
the

CachedRowSet

constant

COMMIT_ON_ACCEPT_CHANGES

to

false

and use the

commit

and

rollback

methods defined in this interface to manage transaction boundaries.

If one or more disconnected

RowSet

objects are participating
in a global transaction, they may wish to coordinate their synchronization
commits to preserve data integrity and reduce the number of
synchronization exceptions. If this is the case, an application should set
the

CachedRowSet

constant

COMMIT_ON_ACCEPT_CHANGES

to

false

and use the

commit

and

rollback

methods defined in this interface to manage transaction boundaries.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

commit

()

Makes permanent all changes that have been performed by the

acceptChanges

method since the last call to either the

commit

or

rollback

methods.

void

rollback

()

Undoes all changes made in the current transaction.

void

rollback

​(

Savepoint

s)

Undoes all changes made in the current transaction made prior to the given

Savepoint

object.

- Methods declared in interface javax.sql.

RowSetWriter

writeData

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

commit

()

Makes permanent all changes that have been performed by the

acceptChanges

method since the last call to either the

commit

or

rollback

methods.

void

rollback

()

Undoes all changes made in the current transaction.

void

rollback

​(

Savepoint

s)

Undoes all changes made in the current transaction made prior to the given

Savepoint

object.

- Methods declared in interface javax.sql.

RowSetWriter

writeData

---

#### Method Summary

Makes permanent all changes that have been performed by the

acceptChanges

method since the last call to either the

commit

or

rollback

methods.

Undoes all changes made in the current transaction.

Undoes all changes made in the current transaction made prior to the given

Savepoint

object.

Methods declared in interface javax.sql.

RowSetWriter

writeData

---

#### Methods declared in interface javax.sql. RowSetWriter

============ METHOD DETAIL ==========

- Method Detail

- commit

```java
void commit()
throws
SQLException
```

Makes permanent all changes that have been performed by the

acceptChanges

method since the last call to either the

commit

or

rollback

methods.
This method should be used only when auto-commit mode has been disabled.

**Throws:** SQLException

- if a database access error occurs or the

Connection

object within this

CachedRowSet

object is in auto-commit mode

- rollback

```java
void rollback()
throws
SQLException
```

Undoes all changes made in the current transaction. This method should be
used only when auto-commit mode has been disabled.

**Throws:** SQLException

- if a database access error occurs or the

Connection

object within this

CachedRowSet

object is in auto-commit mode

- rollback

```java
void rollback​(
Savepoint
s)
throws
SQLException
```

Undoes all changes made in the current transaction made prior to the given

Savepoint

object. This method should be used only when auto-commit
mode has been disabled.

**Parameters:** s

- a

Savepoint

object marking a savepoint in the current
transaction. All changes made before

s

was set will be undone.
All changes made after

s

was set will be made permanent.
**Throws:** SQLException

- if a database access error occurs or the

Connection

object within this

CachedRowSet

object is in auto-commit mode

Method Detail

- commit

```java
void commit()
throws
SQLException
```

Makes permanent all changes that have been performed by the

acceptChanges

method since the last call to either the

commit

or

rollback

methods.
This method should be used only when auto-commit mode has been disabled.

**Throws:** SQLException

- if a database access error occurs or the

Connection

object within this

CachedRowSet

object is in auto-commit mode

- rollback

```java
void rollback()
throws
SQLException
```

Undoes all changes made in the current transaction. This method should be
used only when auto-commit mode has been disabled.

**Throws:** SQLException

- if a database access error occurs or the

Connection

object within this

CachedRowSet

object is in auto-commit mode

- rollback

```java
void rollback​(
Savepoint
s)
throws
SQLException
```

Undoes all changes made in the current transaction made prior to the given

Savepoint

object. This method should be used only when auto-commit
mode has been disabled.

**Parameters:** s

- a

Savepoint

object marking a savepoint in the current
transaction. All changes made before

s

was set will be undone.
All changes made after

s

was set will be made permanent.
**Throws:** SQLException

- if a database access error occurs or the

Connection

object within this

CachedRowSet

object is in auto-commit mode

---

#### Method Detail

commit

```java
void commit()
throws
SQLException
```

Makes permanent all changes that have been performed by the

acceptChanges

method since the last call to either the

commit

or

rollback

methods.
This method should be used only when auto-commit mode has been disabled.

**Throws:** SQLException

- if a database access error occurs or the

Connection

object within this

CachedRowSet

object is in auto-commit mode

---

#### commit

void commit()
throws

SQLException

Makes permanent all changes that have been performed by the

acceptChanges

method since the last call to either the

commit

or

rollback

methods.
This method should be used only when auto-commit mode has been disabled.

rollback

```java
void rollback()
throws
SQLException
```

Undoes all changes made in the current transaction. This method should be
used only when auto-commit mode has been disabled.

**Throws:** SQLException

- if a database access error occurs or the

Connection

object within this

CachedRowSet

object is in auto-commit mode

---

#### rollback

void rollback()
throws

SQLException

Undoes all changes made in the current transaction. This method should be
used only when auto-commit mode has been disabled.

rollback

```java
void rollback​(
Savepoint
s)
throws
SQLException
```

Undoes all changes made in the current transaction made prior to the given

Savepoint

object. This method should be used only when auto-commit
mode has been disabled.

**Parameters:** s

- a

Savepoint

object marking a savepoint in the current
transaction. All changes made before

s

was set will be undone.
All changes made after

s

was set will be made permanent.
**Throws:** SQLException

- if a database access error occurs or the

Connection

object within this

CachedRowSet

object is in auto-commit mode

---

#### rollback

void rollback​(

Savepoint

s)
throws

SQLException

Undoes all changes made in the current transaction made prior to the given

Savepoint

object. This method should be used only when auto-commit
mode has been disabled.

---

