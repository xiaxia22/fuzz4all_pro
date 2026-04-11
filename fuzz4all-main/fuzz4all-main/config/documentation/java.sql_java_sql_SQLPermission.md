# Class SQLPermission

**Source:** `java.sql\java\sql\SQLPermission.html`

### Class Description

```java
public final class
SQLPermission

extends
BasicPermission
```

The permission for which the

SecurityManager

will check
when code that is running an application with a

SecurityManager

enabled, calls the

DriverManager.deregisterDriver

method,

DriverManager.setLogWriter

method,

DriverManager.setLogStream

(deprecated) method,

SyncFactory.setJNDIContext

method,

SyncFactory.setLogger

method,

Connection.setNetworkTimeout

method,
or the

Connection.abort

method.
If there is no

SQLPermission

object, these methods
throw a

java.lang.SecurityException

as a runtime exception.

A

SQLPermission

object contains
a name (also referred to as a "target name") but no actions
list; there is either a named permission or there is not.
The target name is the name of the permission (see below). The
naming convention follows the hierarchical property naming convention.
In addition, an asterisk
may appear at the end of the name, following a ".", or by itself, to
signify a wildcard match. For example:

loadLibrary.*

and

*

signify a wildcard match,
while

*loadLibrary

and

a*b

do not.

The following table lists all the possible

SQLPermission

target names.
The table gives a description of what the permission allows
and a discussion of the risks of granting code the permission.

permission target name, what the permission allows, and associated risks

Permission Target Name

What the Permission Allows

Risks of Allowing this Permission

setLog

Setting of the logging stream

This is a dangerous permission to grant.
The contents of the log may contain usernames and passwords,
SQL statements, and SQL data.

callAbort

Allows the invocation of the

Connection

method

abort

Permits an application to terminate a physical connection to a
database.

setSyncFactory

Allows the invocation of the

SyncFactory

methods

setJNDIContext

and

setLogger

Permits an application to specify the JNDI context from which the

SyncProvider

implementations can be retrieved from and the logging
object to be used by the

SyncProvider

implementation.

setNetworkTimeout

Allows the invocation of the

Connection

method

setNetworkTimeout

Permits an application to specify the maximum period a

Connection

or
objects created from the

Connection

will wait for the database to reply to any one request.

deregisterDriver

Allows the invocation of the

DriverManager

method

deregisterDriver

Permits an application to remove a JDBC driver from the list of
registered Drivers and release its resources.

**All Implemented Interfaces:** Serializable

,

Guard

---

### Field Details

*No entries found.*

### Constructor Details

#### public SQLPermission​(
String
name)

Creates a new

SQLPermission

object with the specified name.
The name is the symbolic name of the

SQLPermission

.

**Parameters:**
- name

- the name of this

SQLPermission

object, which must
be either

setLog

,

callAbort

,

setSyncFactory

,

deregisterDriver

, or

setNetworkTimeout

**Throws:**
- NullPointerException

- if

name

is

null

.
- IllegalArgumentException

- if

name

is empty.

---

#### public SQLPermission​(
String
name,

String
actions)

Creates a new

SQLPermission

object with the specified name.
The name is the symbolic name of the

SQLPermission

; the
actions

String

is currently unused and should be

null

.

**Parameters:**
- name

- the name of this

SQLPermission

object, which must
be either

setLog

,

callAbort

,

setSyncFactory

,

deregisterDriver

, or

setNetworkTimeout
- actions

- should be

null

**Throws:**
- NullPointerException

- if

name

is

null

.
- IllegalArgumentException

- if

name

is empty.

---

### Method Details

*No entries found.*

### Additional Sections

#### Class SQLPermission

java.lang.Object

- java.security.Permission
- - java.security.BasicPermission
- - java.sql.SQLPermission

java.security.Permission

- java.security.BasicPermission
- - java.sql.SQLPermission

java.security.BasicPermission

- java.sql.SQLPermission

java.sql.SQLPermission

**All Implemented Interfaces:** Serializable

,

Guard

```java
public final class
SQLPermission

extends
BasicPermission
```

The permission for which the

SecurityManager

will check
when code that is running an application with a

SecurityManager

enabled, calls the

DriverManager.deregisterDriver

method,

DriverManager.setLogWriter

method,

DriverManager.setLogStream

(deprecated) method,

SyncFactory.setJNDIContext

method,

SyncFactory.setLogger

method,

Connection.setNetworkTimeout

method,
or the

Connection.abort

method.
If there is no

SQLPermission

object, these methods
throw a

java.lang.SecurityException

as a runtime exception.

A

SQLPermission

object contains
a name (also referred to as a "target name") but no actions
list; there is either a named permission or there is not.
The target name is the name of the permission (see below). The
naming convention follows the hierarchical property naming convention.
In addition, an asterisk
may appear at the end of the name, following a ".", or by itself, to
signify a wildcard match. For example:

loadLibrary.*

and

*

signify a wildcard match,
while

*loadLibrary

and

a*b

do not.

The following table lists all the possible

SQLPermission

target names.
The table gives a description of what the permission allows
and a discussion of the risks of granting code the permission.

permission target name, what the permission allows, and associated risks

Permission Target Name

What the Permission Allows

Risks of Allowing this Permission

setLog

Setting of the logging stream

This is a dangerous permission to grant.
The contents of the log may contain usernames and passwords,
SQL statements, and SQL data.

callAbort

Allows the invocation of the

Connection

method

abort

Permits an application to terminate a physical connection to a
database.

setSyncFactory

Allows the invocation of the

SyncFactory

methods

setJNDIContext

and

setLogger

Permits an application to specify the JNDI context from which the

SyncProvider

implementations can be retrieved from and the logging
object to be used by the

SyncProvider

implementation.

setNetworkTimeout

Allows the invocation of the

Connection

method

setNetworkTimeout

Permits an application to specify the maximum period a

Connection

or
objects created from the

Connection

will wait for the database to reply to any one request.

deregisterDriver

Allows the invocation of the

DriverManager

method

deregisterDriver

Permits an application to remove a JDBC driver from the list of
registered Drivers and release its resources.

**Since:** 1.3
**See Also:** BasicPermission

,

Permission

,

Permissions

,

PermissionCollection

,

SecurityManager

,

Serialized Form

public final class

SQLPermission

extends

BasicPermission

The permission for which the

SecurityManager

will check
when code that is running an application with a

SecurityManager

enabled, calls the

DriverManager.deregisterDriver

method,

DriverManager.setLogWriter

method,

DriverManager.setLogStream

(deprecated) method,

SyncFactory.setJNDIContext

method,

SyncFactory.setLogger

method,

Connection.setNetworkTimeout

method,
or the

Connection.abort

method.
If there is no

SQLPermission

object, these methods
throw a

java.lang.SecurityException

as a runtime exception.

A

SQLPermission

object contains
a name (also referred to as a "target name") but no actions
list; there is either a named permission or there is not.
The target name is the name of the permission (see below). The
naming convention follows the hierarchical property naming convention.
In addition, an asterisk
may appear at the end of the name, following a ".", or by itself, to
signify a wildcard match. For example:

loadLibrary.*

and

*

signify a wildcard match,
while

*loadLibrary

and

a*b

do not.

The following table lists all the possible

SQLPermission

target names.
The table gives a description of what the permission allows
and a discussion of the risks of granting code the permission.

permission target name, what the permission allows, and associated risks

Permission Target Name

What the Permission Allows

Risks of Allowing this Permission

setLog

Setting of the logging stream

This is a dangerous permission to grant.
The contents of the log may contain usernames and passwords,
SQL statements, and SQL data.

callAbort

Allows the invocation of the

Connection

method

abort

Permits an application to terminate a physical connection to a
database.

setSyncFactory

Allows the invocation of the

SyncFactory

methods

setJNDIContext

and

setLogger

Permits an application to specify the JNDI context from which the

SyncProvider

implementations can be retrieved from and the logging
object to be used by the

SyncProvider

implementation.

setNetworkTimeout

Allows the invocation of the

Connection

method

setNetworkTimeout

Permits an application to specify the maximum period a

Connection

or
objects created from the

Connection

will wait for the database to reply to any one request.

deregisterDriver

Allows the invocation of the

DriverManager

method

deregisterDriver

Permits an application to remove a JDBC driver from the list of
registered Drivers and release its resources.

A

SQLPermission

object contains
a name (also referred to as a "target name") but no actions
list; there is either a named permission or there is not.
The target name is the name of the permission (see below). The
naming convention follows the hierarchical property naming convention.
In addition, an asterisk
may appear at the end of the name, following a ".", or by itself, to
signify a wildcard match. For example:

loadLibrary.*

and

*

signify a wildcard match,
while

*loadLibrary

and

a*b

do not.

The following table lists all the possible

SQLPermission

target names.
The table gives a description of what the permission allows
and a discussion of the risks of granting code the permission.

permission target name, what the permission allows, and associated risks

Permission Target Name

What the Permission Allows

Risks of Allowing this Permission

setLog

Setting of the logging stream

This is a dangerous permission to grant.
The contents of the log may contain usernames and passwords,
SQL statements, and SQL data.

callAbort

Allows the invocation of the

Connection

method

abort

Permits an application to terminate a physical connection to a
database.

setSyncFactory

Allows the invocation of the

SyncFactory

methods

setJNDIContext

and

setLogger

Permits an application to specify the JNDI context from which the

SyncProvider

implementations can be retrieved from and the logging
object to be used by the

SyncProvider

implementation.

setNetworkTimeout

Allows the invocation of the

Connection

method

setNetworkTimeout

Permits an application to specify the maximum period a

Connection

or
objects created from the

Connection

will wait for the database to reply to any one request.

deregisterDriver

Allows the invocation of the

DriverManager

method

deregisterDriver

Permits an application to remove a JDBC driver from the list of
registered Drivers and release its resources.

The following table lists all the possible

SQLPermission

target names.
The table gives a description of what the permission allows
and a discussion of the risks of granting code the permission.

permission target name, what the permission allows, and associated risks

Permission Target Name

What the Permission Allows

Risks of Allowing this Permission

setLog

Setting of the logging stream

This is a dangerous permission to grant.
The contents of the log may contain usernames and passwords,
SQL statements, and SQL data.

callAbort

Allows the invocation of the

Connection

method

abort

Permits an application to terminate a physical connection to a
database.

setSyncFactory

Allows the invocation of the

SyncFactory

methods

setJNDIContext

and

setLogger

Permits an application to specify the JNDI context from which the

SyncProvider

implementations can be retrieved from and the logging
object to be used by the

SyncProvider

implementation.

setNetworkTimeout

Allows the invocation of the

Connection

method

setNetworkTimeout

Permits an application to specify the maximum period a

Connection

or
objects created from the

Connection

will wait for the database to reply to any one request.

deregisterDriver

Allows the invocation of the

DriverManager

method

deregisterDriver

Permits an application to remove a JDBC driver from the list of
registered Drivers and release its resources.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

SQLPermission

​(

String

name)

Creates a new

SQLPermission

object with the specified name.

SQLPermission

​(

String

name,

String

actions)

Creates a new

SQLPermission

object with the specified name.

========== METHOD SUMMARY ===========

- Method Summary

- Methods declared in class java.security.

BasicPermission

equals

,

getActions

,

hashCode

,

implies

,

newPermissionCollection

- Methods declared in class java.security.

Permission

checkGuard

,

getName

,

toString

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

Constructor Summary

Constructors

Constructor

Description

SQLPermission

​(

String

name)

Creates a new

SQLPermission

object with the specified name.

SQLPermission

​(

String

name,

String

actions)

Creates a new

SQLPermission

object with the specified name.

---

#### Constructor Summary

Creates a new

SQLPermission

object with the specified name.

Method Summary

- Methods declared in class java.security.

BasicPermission

equals

,

getActions

,

hashCode

,

implies

,

newPermissionCollection

- Methods declared in class java.security.

Permission

checkGuard

,

getName

,

toString

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

Methods declared in class java.security.

BasicPermission

equals

,

getActions

,

hashCode

,

implies

,

newPermissionCollection

---

#### Methods declared in class java.security. BasicPermission

Methods declared in class java.security.

Permission

checkGuard

,

getName

,

toString

---

#### Methods declared in class java.security. Permission

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

- SQLPermission

```java
public SQLPermission​(
String
name)
```

Creates a new

SQLPermission

object with the specified name.
The name is the symbolic name of the

SQLPermission

.

**Parameters:** name

- the name of this

SQLPermission

object, which must
be either

setLog

,

callAbort

,

setSyncFactory

,

deregisterDriver

, or

setNetworkTimeout
**Throws:** NullPointerException

- if

name

is

null

.
**Throws:** IllegalArgumentException

- if

name

is empty.

- SQLPermission

```java
public SQLPermission​(
String
name,

String
actions)
```

Creates a new

SQLPermission

object with the specified name.
The name is the symbolic name of the

SQLPermission

; the
actions

String

is currently unused and should be

null

.

**Parameters:** name

- the name of this

SQLPermission

object, which must
be either

setLog

,

callAbort

,

setSyncFactory

,

deregisterDriver

, or

setNetworkTimeout
**Parameters:** actions

- should be

null
**Throws:** NullPointerException

- if

name

is

null

.
**Throws:** IllegalArgumentException

- if

name

is empty.

Constructor Detail

- SQLPermission

```java
public SQLPermission​(
String
name)
```

Creates a new

SQLPermission

object with the specified name.
The name is the symbolic name of the

SQLPermission

.

**Parameters:** name

- the name of this

SQLPermission

object, which must
be either

setLog

,

callAbort

,

setSyncFactory

,

deregisterDriver

, or

setNetworkTimeout
**Throws:** NullPointerException

- if

name

is

null

.
**Throws:** IllegalArgumentException

- if

name

is empty.

- SQLPermission

```java
public SQLPermission​(
String
name,

String
actions)
```

Creates a new

SQLPermission

object with the specified name.
The name is the symbolic name of the

SQLPermission

; the
actions

String

is currently unused and should be

null

.

**Parameters:** name

- the name of this

SQLPermission

object, which must
be either

setLog

,

callAbort

,

setSyncFactory

,

deregisterDriver

, or

setNetworkTimeout
**Parameters:** actions

- should be

null
**Throws:** NullPointerException

- if

name

is

null

.
**Throws:** IllegalArgumentException

- if

name

is empty.

---

#### Constructor Detail

SQLPermission

```java
public SQLPermission​(
String
name)
```

Creates a new

SQLPermission

object with the specified name.
The name is the symbolic name of the

SQLPermission

.

**Parameters:** name

- the name of this

SQLPermission

object, which must
be either

setLog

,

callAbort

,

setSyncFactory

,

deregisterDriver

, or

setNetworkTimeout
**Throws:** NullPointerException

- if

name

is

null

.
**Throws:** IllegalArgumentException

- if

name

is empty.

---

#### SQLPermission

public SQLPermission​(

String

name)

Creates a new

SQLPermission

object with the specified name.
The name is the symbolic name of the

SQLPermission

.

SQLPermission

```java
public SQLPermission​(
String
name,

String
actions)
```

Creates a new

SQLPermission

object with the specified name.
The name is the symbolic name of the

SQLPermission

; the
actions

String

is currently unused and should be

null

.

**Parameters:** name

- the name of this

SQLPermission

object, which must
be either

setLog

,

callAbort

,

setSyncFactory

,

deregisterDriver

, or

setNetworkTimeout
**Parameters:** actions

- should be

null
**Throws:** NullPointerException

- if

name

is

null

.
**Throws:** IllegalArgumentException

- if

name

is empty.

---

#### SQLPermission

public SQLPermission​(

String

name,

String

actions)

Creates a new

SQLPermission

object with the specified name.
The name is the symbolic name of the

SQLPermission

; the
actions

String

is currently unused and should be

null

.

---

