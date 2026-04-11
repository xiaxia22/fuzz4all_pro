# Interface XADataSource

**Source:** `java.sql\javax\sql\XADataSource.html`

### Class Description

```java
public interface
XADataSource

extends
CommonDataSource
```

A factory for

XAConnection

objects that is used internally.
An object that implements the

XADataSource

interface is
typically registered with a naming service that uses the
Java Naming and Directory Interface™
(JNDI).

An implementation of

XADataSource

must include a public no-arg
constructor.

**All Superinterfaces:** CommonDataSource

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### XAConnection
getXAConnection()
throws
SQLException

Attempts to establish a physical database connection that can be
used in a distributed transaction.

**Returns:**
- an

XAConnection

object, which represents a
physical connection to a data source, that can be used in
a distributed transaction

**Throws:**
- SQLException

- if a database access error occurs
- SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
- SQLTimeoutException

- when the driver has determined that the
timeout value specified by the

setLoginTimeout

method
has been exceeded and has at least tried to cancel the
current database connection attempt

**Since:**
- 1.4

---

#### XAConnection
getXAConnection​(
String
user,

String
password)
throws
SQLException

Attempts to establish a physical database connection, using the given
user name and password. The connection that is returned is one that
can be used in a distributed transaction.

**Parameters:**
- user

- the database user on whose behalf the connection is being made
- password

- the user's password

**Returns:**
- an

XAConnection

object, which represents a
physical connection to a data source, that can be used in
a distributed transaction

**Throws:**
- SQLException

- if a database access error occurs
- SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
- SQLTimeoutException

- when the driver has determined that the
timeout value specified by the

setLoginTimeout

method
has been exceeded and has at least tried to cancel the
current database connection attempt

**Since:**
- 1.4

---

#### PrintWriter
getLogWriter()
throws
SQLException

Retrieves the log writer for this

DataSource

object.

The log writer is a character output stream to which all logging
and tracing messages for this data source will be
printed. This includes messages printed by the methods of this
object, messages printed by methods of other objects manufactured
by this object, and so on. Messages printed to a data source
specific log writer are not printed to the log writer associated
with the

java.sql.DriverManager

class. When a

DataSource

object is
created, the log writer is initially null; in other words, the
default is for logging to be disabled.

**Specified by:**
- getLogWriter

in interface

CommonDataSource

**Returns:**
- the log writer for this data source or null if
logging is disabled

**Throws:**
- SQLException

- if a database access error occurs

**See Also:**
- CommonDataSource.setLogWriter(java.io.PrintWriter)

**Since:**
- 1.4

---

#### void setLogWriter​(
PrintWriter
out)
throws
SQLException

Sets the log writer for this

DataSource

object to the given

java.io.PrintWriter

object.

The log writer is a character output stream to which all logging
and tracing messages for this data source will be
printed. This includes messages printed by the methods of this
object, messages printed by methods of other objects manufactured
by this object, and so on. Messages printed to a data source-
specific log writer are not printed to the log writer associated
with the

java.sql.DriverManager

class. When a

DataSource

object is created the log writer is
initially null; in other words, the default is for logging to be
disabled.

**Specified by:**
- setLogWriter

in interface

CommonDataSource

**Parameters:**
- out

- the new log writer; to disable logging, set to null

**Throws:**
- SQLException

- if a database access error occurs

**See Also:**
- CommonDataSource.getLogWriter()

**Since:**
- 1.4

---

#### void setLoginTimeout​(int seconds)
throws
SQLException

Sets the maximum time in seconds that this data source will wait
while attempting to connect to a database. A value of zero
specifies that the timeout is the default system timeout
if there is one; otherwise, it specifies that there is no timeout.
When a

DataSource

object is created, the login timeout is
initially zero.

**Specified by:**
- setLoginTimeout

in interface

CommonDataSource

**Parameters:**
- seconds

- the data source login time limit

**Throws:**
- SQLException

- if a database access error occurs.

**See Also:**
- CommonDataSource.getLoginTimeout()

**Since:**
- 1.4

---

#### int getLoginTimeout()
throws
SQLException

Gets the maximum time in seconds that this data source can wait
while attempting to connect to a database. A value of zero
means that the timeout is the default system timeout
if there is one; otherwise, it means that there is no timeout.
When a

DataSource

object is created, the login timeout is
initially zero.

**Specified by:**
- getLoginTimeout

in interface

CommonDataSource

**Returns:**
- the data source login time limit

**Throws:**
- SQLException

- if a database access error occurs.

**See Also:**
- CommonDataSource.setLoginTimeout(int)

**Since:**
- 1.4

---

#### default
XAConnectionBuilder
createXAConnectionBuilder()
throws
SQLException

Creates a new

XAConnectionBuilder

instance

**Returns:**
- The XAConnectionBuilder instance that was created

**Throws:**
- SQLException

- if an error occurs creating the builder
- SQLFeatureNotSupportedException

- if the driver does not support sharding

**See Also:**
- XAConnectionBuilder

**Since:**
- 9

**Implementation Requirements:**
- The default implementation will throw a

SQLFeatureNotSupportedException

.

---

### Additional Sections

#### Interface XADataSource

**All Superinterfaces:** CommonDataSource

```java
public interface
XADataSource

extends
CommonDataSource
```

A factory for

XAConnection

objects that is used internally.
An object that implements the

XADataSource

interface is
typically registered with a naming service that uses the
Java Naming and Directory Interface™
(JNDI).

An implementation of

XADataSource

must include a public no-arg
constructor.

**Since:** 1.4

public interface

XADataSource

extends

CommonDataSource

A factory for

XAConnection

objects that is used internally.
An object that implements the

XADataSource

interface is
typically registered with a naming service that uses the
Java Naming and Directory Interface™
(JNDI).

An implementation of

XADataSource

must include a public no-arg
constructor.

An implementation of

XADataSource

must include a public no-arg
constructor.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Default Methods

Modifier and Type

Method

Description

default

XAConnectionBuilder

createXAConnectionBuilder

()

Creates a new

XAConnectionBuilder

instance

int

getLoginTimeout

()

Gets the maximum time in seconds that this data source can wait
while attempting to connect to a database.

PrintWriter

getLogWriter

()

Retrieves the log writer for this

DataSource

object.

XAConnection

getXAConnection

()

Attempts to establish a physical database connection that can be
used in a distributed transaction.

XAConnection

getXAConnection

​(

String

user,

String

password)

Attempts to establish a physical database connection, using the given
user name and password.

void

setLoginTimeout

​(int seconds)

Sets the maximum time in seconds that this data source will wait
while attempting to connect to a database.

void

setLogWriter

​(

PrintWriter

out)

Sets the log writer for this

DataSource

object to the given

java.io.PrintWriter

object.

- Methods declared in interface javax.sql.

CommonDataSource

createShardingKeyBuilder

,

getParentLogger

Method Summary

All Methods

Instance Methods

Abstract Methods

Default Methods

Modifier and Type

Method

Description

default

XAConnectionBuilder

createXAConnectionBuilder

()

Creates a new

XAConnectionBuilder

instance

int

getLoginTimeout

()

Gets the maximum time in seconds that this data source can wait
while attempting to connect to a database.

PrintWriter

getLogWriter

()

Retrieves the log writer for this

DataSource

object.

XAConnection

getXAConnection

()

Attempts to establish a physical database connection that can be
used in a distributed transaction.

XAConnection

getXAConnection

​(

String

user,

String

password)

Attempts to establish a physical database connection, using the given
user name and password.

void

setLoginTimeout

​(int seconds)

Sets the maximum time in seconds that this data source will wait
while attempting to connect to a database.

void

setLogWriter

​(

PrintWriter

out)

Sets the log writer for this

DataSource

object to the given

java.io.PrintWriter

object.

- Methods declared in interface javax.sql.

CommonDataSource

createShardingKeyBuilder

,

getParentLogger

---

#### Method Summary

Creates a new

XAConnectionBuilder

instance

Gets the maximum time in seconds that this data source can wait
while attempting to connect to a database.

Retrieves the log writer for this

DataSource

object.

Attempts to establish a physical database connection that can be
used in a distributed transaction.

Attempts to establish a physical database connection, using the given
user name and password.

Sets the maximum time in seconds that this data source will wait
while attempting to connect to a database.

Sets the log writer for this

DataSource

object to the given

java.io.PrintWriter

object.

Methods declared in interface javax.sql.

CommonDataSource

createShardingKeyBuilder

,

getParentLogger

---

#### Methods declared in interface javax.sql. CommonDataSource

============ METHOD DETAIL ==========

- Method Detail

- getXAConnection

```java
XAConnection
getXAConnection()
throws
SQLException
```

Attempts to establish a physical database connection that can be
used in a distributed transaction.

**Returns:** an

XAConnection

object, which represents a
physical connection to a data source, that can be used in
a distributed transaction
**Throws:** SQLException

- if a database access error occurs
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Throws:** SQLTimeoutException

- when the driver has determined that the
timeout value specified by the

setLoginTimeout

method
has been exceeded and has at least tried to cancel the
current database connection attempt
**Since:** 1.4

- getXAConnection

```java
XAConnection
getXAConnection​(
String
user,

String
password)
throws
SQLException
```

Attempts to establish a physical database connection, using the given
user name and password. The connection that is returned is one that
can be used in a distributed transaction.

**Parameters:** user

- the database user on whose behalf the connection is being made
**Parameters:** password

- the user's password
**Returns:** an

XAConnection

object, which represents a
physical connection to a data source, that can be used in
a distributed transaction
**Throws:** SQLException

- if a database access error occurs
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Throws:** SQLTimeoutException

- when the driver has determined that the
timeout value specified by the

setLoginTimeout

method
has been exceeded and has at least tried to cancel the
current database connection attempt
**Since:** 1.4

- getLogWriter

```java
PrintWriter
getLogWriter()
throws
SQLException
```

Retrieves the log writer for this

DataSource

object.

The log writer is a character output stream to which all logging
and tracing messages for this data source will be
printed. This includes messages printed by the methods of this
object, messages printed by methods of other objects manufactured
by this object, and so on. Messages printed to a data source
specific log writer are not printed to the log writer associated
with the

java.sql.DriverManager

class. When a

DataSource

object is
created, the log writer is initially null; in other words, the
default is for logging to be disabled.

**Specified by:** getLogWriter

in interface

CommonDataSource
**Returns:** the log writer for this data source or null if
logging is disabled
**Throws:** SQLException

- if a database access error occurs
**Since:** 1.4
**See Also:** CommonDataSource.setLogWriter(java.io.PrintWriter)

- setLogWriter

```java
void setLogWriter​(
PrintWriter
out)
throws
SQLException
```

Sets the log writer for this

DataSource

object to the given

java.io.PrintWriter

object.

The log writer is a character output stream to which all logging
and tracing messages for this data source will be
printed. This includes messages printed by the methods of this
object, messages printed by methods of other objects manufactured
by this object, and so on. Messages printed to a data source-
specific log writer are not printed to the log writer associated
with the

java.sql.DriverManager

class. When a

DataSource

object is created the log writer is
initially null; in other words, the default is for logging to be
disabled.

**Specified by:** setLogWriter

in interface

CommonDataSource
**Parameters:** out

- the new log writer; to disable logging, set to null
**Throws:** SQLException

- if a database access error occurs
**Since:** 1.4
**See Also:** CommonDataSource.getLogWriter()

- setLoginTimeout

```java
void setLoginTimeout​(int seconds)
throws
SQLException
```

Sets the maximum time in seconds that this data source will wait
while attempting to connect to a database. A value of zero
specifies that the timeout is the default system timeout
if there is one; otherwise, it specifies that there is no timeout.
When a

DataSource

object is created, the login timeout is
initially zero.

**Specified by:** setLoginTimeout

in interface

CommonDataSource
**Parameters:** seconds

- the data source login time limit
**Throws:** SQLException

- if a database access error occurs.
**Since:** 1.4
**See Also:** CommonDataSource.getLoginTimeout()

- getLoginTimeout

```java
int getLoginTimeout()
throws
SQLException
```

Gets the maximum time in seconds that this data source can wait
while attempting to connect to a database. A value of zero
means that the timeout is the default system timeout
if there is one; otherwise, it means that there is no timeout.
When a

DataSource

object is created, the login timeout is
initially zero.

**Specified by:** getLoginTimeout

in interface

CommonDataSource
**Returns:** the data source login time limit
**Throws:** SQLException

- if a database access error occurs.
**Since:** 1.4
**See Also:** CommonDataSource.setLoginTimeout(int)

- createXAConnectionBuilder

```java
default
XAConnectionBuilder
createXAConnectionBuilder()
throws
SQLException
```

Creates a new

XAConnectionBuilder

instance

**Implementation Requirements:** The default implementation will throw a

SQLFeatureNotSupportedException

.
**Returns:** The XAConnectionBuilder instance that was created
**Throws:** SQLException

- if an error occurs creating the builder
**Throws:** SQLFeatureNotSupportedException

- if the driver does not support sharding
**Since:** 9
**See Also:** XAConnectionBuilder

Method Detail

- getXAConnection

```java
XAConnection
getXAConnection()
throws
SQLException
```

Attempts to establish a physical database connection that can be
used in a distributed transaction.

**Returns:** an

XAConnection

object, which represents a
physical connection to a data source, that can be used in
a distributed transaction
**Throws:** SQLException

- if a database access error occurs
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Throws:** SQLTimeoutException

- when the driver has determined that the
timeout value specified by the

setLoginTimeout

method
has been exceeded and has at least tried to cancel the
current database connection attempt
**Since:** 1.4

- getXAConnection

```java
XAConnection
getXAConnection​(
String
user,

String
password)
throws
SQLException
```

Attempts to establish a physical database connection, using the given
user name and password. The connection that is returned is one that
can be used in a distributed transaction.

**Parameters:** user

- the database user on whose behalf the connection is being made
**Parameters:** password

- the user's password
**Returns:** an

XAConnection

object, which represents a
physical connection to a data source, that can be used in
a distributed transaction
**Throws:** SQLException

- if a database access error occurs
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Throws:** SQLTimeoutException

- when the driver has determined that the
timeout value specified by the

setLoginTimeout

method
has been exceeded and has at least tried to cancel the
current database connection attempt
**Since:** 1.4

- getLogWriter

```java
PrintWriter
getLogWriter()
throws
SQLException
```

Retrieves the log writer for this

DataSource

object.

The log writer is a character output stream to which all logging
and tracing messages for this data source will be
printed. This includes messages printed by the methods of this
object, messages printed by methods of other objects manufactured
by this object, and so on. Messages printed to a data source
specific log writer are not printed to the log writer associated
with the

java.sql.DriverManager

class. When a

DataSource

object is
created, the log writer is initially null; in other words, the
default is for logging to be disabled.

**Specified by:** getLogWriter

in interface

CommonDataSource
**Returns:** the log writer for this data source or null if
logging is disabled
**Throws:** SQLException

- if a database access error occurs
**Since:** 1.4
**See Also:** CommonDataSource.setLogWriter(java.io.PrintWriter)

- setLogWriter

```java
void setLogWriter​(
PrintWriter
out)
throws
SQLException
```

Sets the log writer for this

DataSource

object to the given

java.io.PrintWriter

object.

The log writer is a character output stream to which all logging
and tracing messages for this data source will be
printed. This includes messages printed by the methods of this
object, messages printed by methods of other objects manufactured
by this object, and so on. Messages printed to a data source-
specific log writer are not printed to the log writer associated
with the

java.sql.DriverManager

class. When a

DataSource

object is created the log writer is
initially null; in other words, the default is for logging to be
disabled.

**Specified by:** setLogWriter

in interface

CommonDataSource
**Parameters:** out

- the new log writer; to disable logging, set to null
**Throws:** SQLException

- if a database access error occurs
**Since:** 1.4
**See Also:** CommonDataSource.getLogWriter()

- setLoginTimeout

```java
void setLoginTimeout​(int seconds)
throws
SQLException
```

Sets the maximum time in seconds that this data source will wait
while attempting to connect to a database. A value of zero
specifies that the timeout is the default system timeout
if there is one; otherwise, it specifies that there is no timeout.
When a

DataSource

object is created, the login timeout is
initially zero.

**Specified by:** setLoginTimeout

in interface

CommonDataSource
**Parameters:** seconds

- the data source login time limit
**Throws:** SQLException

- if a database access error occurs.
**Since:** 1.4
**See Also:** CommonDataSource.getLoginTimeout()

- getLoginTimeout

```java
int getLoginTimeout()
throws
SQLException
```

Gets the maximum time in seconds that this data source can wait
while attempting to connect to a database. A value of zero
means that the timeout is the default system timeout
if there is one; otherwise, it means that there is no timeout.
When a

DataSource

object is created, the login timeout is
initially zero.

**Specified by:** getLoginTimeout

in interface

CommonDataSource
**Returns:** the data source login time limit
**Throws:** SQLException

- if a database access error occurs.
**Since:** 1.4
**See Also:** CommonDataSource.setLoginTimeout(int)

- createXAConnectionBuilder

```java
default
XAConnectionBuilder
createXAConnectionBuilder()
throws
SQLException
```

Creates a new

XAConnectionBuilder

instance

**Implementation Requirements:** The default implementation will throw a

SQLFeatureNotSupportedException

.
**Returns:** The XAConnectionBuilder instance that was created
**Throws:** SQLException

- if an error occurs creating the builder
**Throws:** SQLFeatureNotSupportedException

- if the driver does not support sharding
**Since:** 9
**See Also:** XAConnectionBuilder

---

#### Method Detail

getXAConnection

```java
XAConnection
getXAConnection()
throws
SQLException
```

Attempts to establish a physical database connection that can be
used in a distributed transaction.

**Returns:** an

XAConnection

object, which represents a
physical connection to a data source, that can be used in
a distributed transaction
**Throws:** SQLException

- if a database access error occurs
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Throws:** SQLTimeoutException

- when the driver has determined that the
timeout value specified by the

setLoginTimeout

method
has been exceeded and has at least tried to cancel the
current database connection attempt
**Since:** 1.4

---

#### getXAConnection

XAConnection

getXAConnection()
throws

SQLException

Attempts to establish a physical database connection that can be
used in a distributed transaction.

getXAConnection

```java
XAConnection
getXAConnection​(
String
user,

String
password)
throws
SQLException
```

Attempts to establish a physical database connection, using the given
user name and password. The connection that is returned is one that
can be used in a distributed transaction.

**Parameters:** user

- the database user on whose behalf the connection is being made
**Parameters:** password

- the user's password
**Returns:** an

XAConnection

object, which represents a
physical connection to a data source, that can be used in
a distributed transaction
**Throws:** SQLException

- if a database access error occurs
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Throws:** SQLTimeoutException

- when the driver has determined that the
timeout value specified by the

setLoginTimeout

method
has been exceeded and has at least tried to cancel the
current database connection attempt
**Since:** 1.4

---

#### getXAConnection

XAConnection

getXAConnection​(

String

user,

String

password)
throws

SQLException

Attempts to establish a physical database connection, using the given
user name and password. The connection that is returned is one that
can be used in a distributed transaction.

getLogWriter

```java
PrintWriter
getLogWriter()
throws
SQLException
```

Retrieves the log writer for this

DataSource

object.

The log writer is a character output stream to which all logging
and tracing messages for this data source will be
printed. This includes messages printed by the methods of this
object, messages printed by methods of other objects manufactured
by this object, and so on. Messages printed to a data source
specific log writer are not printed to the log writer associated
with the

java.sql.DriverManager

class. When a

DataSource

object is
created, the log writer is initially null; in other words, the
default is for logging to be disabled.

**Specified by:** getLogWriter

in interface

CommonDataSource
**Returns:** the log writer for this data source or null if
logging is disabled
**Throws:** SQLException

- if a database access error occurs
**Since:** 1.4
**See Also:** CommonDataSource.setLogWriter(java.io.PrintWriter)

---

#### getLogWriter

PrintWriter

getLogWriter()
throws

SQLException

Retrieves the log writer for this

DataSource

object.

The log writer is a character output stream to which all logging
and tracing messages for this data source will be
printed. This includes messages printed by the methods of this
object, messages printed by methods of other objects manufactured
by this object, and so on. Messages printed to a data source
specific log writer are not printed to the log writer associated
with the

java.sql.DriverManager

class. When a

DataSource

object is
created, the log writer is initially null; in other words, the
default is for logging to be disabled.

The log writer is a character output stream to which all logging
and tracing messages for this data source will be
printed. This includes messages printed by the methods of this
object, messages printed by methods of other objects manufactured
by this object, and so on. Messages printed to a data source
specific log writer are not printed to the log writer associated
with the

java.sql.DriverManager

class. When a

DataSource

object is
created, the log writer is initially null; in other words, the
default is for logging to be disabled.

setLogWriter

```java
void setLogWriter​(
PrintWriter
out)
throws
SQLException
```

Sets the log writer for this

DataSource

object to the given

java.io.PrintWriter

object.

The log writer is a character output stream to which all logging
and tracing messages for this data source will be
printed. This includes messages printed by the methods of this
object, messages printed by methods of other objects manufactured
by this object, and so on. Messages printed to a data source-
specific log writer are not printed to the log writer associated
with the

java.sql.DriverManager

class. When a

DataSource

object is created the log writer is
initially null; in other words, the default is for logging to be
disabled.

**Specified by:** setLogWriter

in interface

CommonDataSource
**Parameters:** out

- the new log writer; to disable logging, set to null
**Throws:** SQLException

- if a database access error occurs
**Since:** 1.4
**See Also:** CommonDataSource.getLogWriter()

---

#### setLogWriter

void setLogWriter​(

PrintWriter

out)
throws

SQLException

Sets the log writer for this

DataSource

object to the given

java.io.PrintWriter

object.

The log writer is a character output stream to which all logging
and tracing messages for this data source will be
printed. This includes messages printed by the methods of this
object, messages printed by methods of other objects manufactured
by this object, and so on. Messages printed to a data source-
specific log writer are not printed to the log writer associated
with the

java.sql.DriverManager

class. When a

DataSource

object is created the log writer is
initially null; in other words, the default is for logging to be
disabled.

The log writer is a character output stream to which all logging
and tracing messages for this data source will be
printed. This includes messages printed by the methods of this
object, messages printed by methods of other objects manufactured
by this object, and so on. Messages printed to a data source-
specific log writer are not printed to the log writer associated
with the

java.sql.DriverManager

class. When a

DataSource

object is created the log writer is
initially null; in other words, the default is for logging to be
disabled.

setLoginTimeout

```java
void setLoginTimeout​(int seconds)
throws
SQLException
```

Sets the maximum time in seconds that this data source will wait
while attempting to connect to a database. A value of zero
specifies that the timeout is the default system timeout
if there is one; otherwise, it specifies that there is no timeout.
When a

DataSource

object is created, the login timeout is
initially zero.

**Specified by:** setLoginTimeout

in interface

CommonDataSource
**Parameters:** seconds

- the data source login time limit
**Throws:** SQLException

- if a database access error occurs.
**Since:** 1.4
**See Also:** CommonDataSource.getLoginTimeout()

---

#### setLoginTimeout

void setLoginTimeout​(int seconds)
throws

SQLException

Sets the maximum time in seconds that this data source will wait
while attempting to connect to a database. A value of zero
specifies that the timeout is the default system timeout
if there is one; otherwise, it specifies that there is no timeout.
When a

DataSource

object is created, the login timeout is
initially zero.

getLoginTimeout

```java
int getLoginTimeout()
throws
SQLException
```

Gets the maximum time in seconds that this data source can wait
while attempting to connect to a database. A value of zero
means that the timeout is the default system timeout
if there is one; otherwise, it means that there is no timeout.
When a

DataSource

object is created, the login timeout is
initially zero.

**Specified by:** getLoginTimeout

in interface

CommonDataSource
**Returns:** the data source login time limit
**Throws:** SQLException

- if a database access error occurs.
**Since:** 1.4
**See Also:** CommonDataSource.setLoginTimeout(int)

---

#### getLoginTimeout

int getLoginTimeout()
throws

SQLException

Gets the maximum time in seconds that this data source can wait
while attempting to connect to a database. A value of zero
means that the timeout is the default system timeout
if there is one; otherwise, it means that there is no timeout.
When a

DataSource

object is created, the login timeout is
initially zero.

createXAConnectionBuilder

```java
default
XAConnectionBuilder
createXAConnectionBuilder()
throws
SQLException
```

Creates a new

XAConnectionBuilder

instance

**Implementation Requirements:** The default implementation will throw a

SQLFeatureNotSupportedException

.
**Returns:** The XAConnectionBuilder instance that was created
**Throws:** SQLException

- if an error occurs creating the builder
**Throws:** SQLFeatureNotSupportedException

- if the driver does not support sharding
**Since:** 9
**See Also:** XAConnectionBuilder

---

#### createXAConnectionBuilder

default

XAConnectionBuilder

createXAConnectionBuilder()
throws

SQLException

Creates a new

XAConnectionBuilder

instance

---

