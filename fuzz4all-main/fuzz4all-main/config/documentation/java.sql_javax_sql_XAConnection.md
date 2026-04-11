# Interface XAConnection

**Source:** `java.sql\javax\sql\XAConnection.html`

### Class Description

```java
public interface
XAConnection

extends
PooledConnection
```

An object that provides support for distributed transactions. An

XAConnection

object may be enlisted in a distributed transaction
by means of an

XAResource

object. A transaction manager, usually
part of a middle tier server, manages an

XAConnection

object
through the

XAResource

object.

An application programmer does not use this interface directly; rather, it is
used by a transaction manager working in the middle tier server.

**All Superinterfaces:** PooledConnection

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### XAResource
getXAResource()
throws
SQLException

Retrieves an

XAResource

object that the transaction manager
will use to manage this

XAConnection

object's participation
in a distributed transaction.

**Returns:**
- the

XAResource

object

**Throws:**
- SQLException

- if a database access error occurs
- SQLFeatureNotSupportedException

- if the JDBC driver does not
support this method

**Since:**
- 1.4

---

### Additional Sections

#### Interface XAConnection

**All Superinterfaces:** PooledConnection

```java
public interface
XAConnection

extends
PooledConnection
```

An object that provides support for distributed transactions. An

XAConnection

object may be enlisted in a distributed transaction
by means of an

XAResource

object. A transaction manager, usually
part of a middle tier server, manages an

XAConnection

object
through the

XAResource

object.

An application programmer does not use this interface directly; rather, it is
used by a transaction manager working in the middle tier server.

**Since:** 1.4

public interface

XAConnection

extends

PooledConnection

An object that provides support for distributed transactions. An

XAConnection

object may be enlisted in a distributed transaction
by means of an

XAResource

object. A transaction manager, usually
part of a middle tier server, manages an

XAConnection

object
through the

XAResource

object.

An application programmer does not use this interface directly; rather, it is
used by a transaction manager working in the middle tier server.

An application programmer does not use this interface directly; rather, it is
used by a transaction manager working in the middle tier server.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

XAResource

getXAResource

()

Retrieves an

XAResource

object that the transaction manager
will use to manage this

XAConnection

object's participation
in a distributed transaction.

- Methods declared in interface javax.sql.

PooledConnection

addConnectionEventListener

,

addStatementEventListener

,

close

,

getConnection

,

removeConnectionEventListener

,

removeStatementEventListener

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

XAResource

getXAResource

()

Retrieves an

XAResource

object that the transaction manager
will use to manage this

XAConnection

object's participation
in a distributed transaction.

- Methods declared in interface javax.sql.

PooledConnection

addConnectionEventListener

,

addStatementEventListener

,

close

,

getConnection

,

removeConnectionEventListener

,

removeStatementEventListener

---

#### Method Summary

Retrieves an

XAResource

object that the transaction manager
will use to manage this

XAConnection

object's participation
in a distributed transaction.

Methods declared in interface javax.sql.

PooledConnection

addConnectionEventListener

,

addStatementEventListener

,

close

,

getConnection

,

removeConnectionEventListener

,

removeStatementEventListener

---

#### Methods declared in interface javax.sql. PooledConnection

============ METHOD DETAIL ==========

- Method Detail

- getXAResource

```java
XAResource
getXAResource()
throws
SQLException
```

Retrieves an

XAResource

object that the transaction manager
will use to manage this

XAConnection

object's participation
in a distributed transaction.

**Returns:** the

XAResource

object
**Throws:** SQLException

- if a database access error occurs
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not
support this method
**Since:** 1.4

Method Detail

- getXAResource

```java
XAResource
getXAResource()
throws
SQLException
```

Retrieves an

XAResource

object that the transaction manager
will use to manage this

XAConnection

object's participation
in a distributed transaction.

**Returns:** the

XAResource

object
**Throws:** SQLException

- if a database access error occurs
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not
support this method
**Since:** 1.4

---

#### Method Detail

getXAResource

```java
XAResource
getXAResource()
throws
SQLException
```

Retrieves an

XAResource

object that the transaction manager
will use to manage this

XAConnection

object's participation
in a distributed transaction.

**Returns:** the

XAResource

object
**Throws:** SQLException

- if a database access error occurs
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not
support this method
**Since:** 1.4

---

#### getXAResource

XAResource

getXAResource()
throws

SQLException

Retrieves an

XAResource

object that the transaction manager
will use to manage this

XAConnection

object's participation
in a distributed transaction.

---

