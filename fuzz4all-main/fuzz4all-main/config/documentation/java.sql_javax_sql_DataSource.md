# Interface DataSource

**Source:** `java.sql\javax\sql\DataSource.html`

### Class Description

```java
public interface
DataSource

extends
CommonDataSource
,
Wrapper
```

A factory for connections to the physical data source that this

DataSource

object represents. An alternative to the

DriverManager

facility, a

DataSource

object
is the preferred means of getting a connection. An object that implements
the

DataSource

interface will typically be
registered with a naming service based on the
Java™ Naming and Directory (JNDI) API.

The

DataSource

interface is implemented by a driver vendor.
There are three types of implementations:

- Basic implementation -- produces a standard

Connection

object

Connection pooling implementation -- produces a

Connection

object that will automatically participate in connection pooling. This
implementation works with a middle-tier connection pooling manager.

Distributed transaction implementation -- produces a

Connection

object that may be used for distributed
transactions and almost always participates in connection pooling.
This implementation works with a middle-tier
transaction manager and almost always with a connection
pooling manager.

A

DataSource

object has properties that can be modified
when necessary. For example, if the data source is moved to a different
server, the property for the server can be changed. The benefit is that
because the data source's properties can be changed, any code accessing
that data source does not need to be changed.

A driver that is accessed via a

DataSource

object does not
register itself with the

DriverManager

. Rather, a

DataSource

object is retrieved through a lookup operation
and then used to create a

Connection

object. With a basic
implementation, the connection obtained through a

DataSource

object is identical to a connection obtained through the

DriverManager

facility.

An implementation of

DataSource

must include a public no-arg
constructor.

**All Superinterfaces:** CommonDataSource

,

Wrapper

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### Connection
getConnection()
throws
SQLException

Attempts to establish a connection with the data source that
this

DataSource

object represents.

**Returns:**
- a connection to the data source

**Throws:**
- SQLException

- if a database access error occurs
- SQLTimeoutException

- when the driver has determined that the
timeout value specified by the

setLoginTimeout

method
has been exceeded and has at least tried to cancel the
current database connection attempt

---

#### Connection
getConnection​(
String
username,

String
password)
throws
SQLException

Attempts to establish a connection with the data source that
this

DataSource

object represents.

**Parameters:**
- username

- the database user on whose behalf the connection is
being made
- password

- the user's password

**Returns:**
- a connection to the data source

**Throws:**
- SQLException

- if a database access error occurs
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
ConnectionBuilder
createConnectionBuilder()
throws
SQLException

Create a new

ConnectionBuilder

instance

**Returns:**
- The ConnectionBuilder instance that was created

**Throws:**
- SQLException

- if an error occurs creating the builder
- SQLFeatureNotSupportedException

- if the driver does not support sharding

**See Also:**
- ConnectionBuilder

**Since:**
- 9

**Implementation Requirements:**
- The default implementation will throw a

SQLFeatureNotSupportedException

---

### Additional Sections

#### Interface DataSource

**All Superinterfaces:** CommonDataSource

,

Wrapper

```java
public interface
DataSource

extends
CommonDataSource
,
Wrapper
```

A factory for connections to the physical data source that this

DataSource

object represents. An alternative to the

DriverManager

facility, a

DataSource

object
is the preferred means of getting a connection. An object that implements
the

DataSource

interface will typically be
registered with a naming service based on the
Java™ Naming and Directory (JNDI) API.

The

DataSource

interface is implemented by a driver vendor.
There are three types of implementations:

- Basic implementation -- produces a standard

Connection

object

Connection pooling implementation -- produces a

Connection

object that will automatically participate in connection pooling. This
implementation works with a middle-tier connection pooling manager.

Distributed transaction implementation -- produces a

Connection

object that may be used for distributed
transactions and almost always participates in connection pooling.
This implementation works with a middle-tier
transaction manager and almost always with a connection
pooling manager.

A

DataSource

object has properties that can be modified
when necessary. For example, if the data source is moved to a different
server, the property for the server can be changed. The benefit is that
because the data source's properties can be changed, any code accessing
that data source does not need to be changed.

A driver that is accessed via a

DataSource

object does not
register itself with the

DriverManager

. Rather, a

DataSource

object is retrieved through a lookup operation
and then used to create a

Connection

object. With a basic
implementation, the connection obtained through a

DataSource

object is identical to a connection obtained through the

DriverManager

facility.

An implementation of

DataSource

must include a public no-arg
constructor.

**Since:** 1.4

public interface

DataSource

extends

CommonDataSource

,

Wrapper

A factory for connections to the physical data source that this

DataSource

object represents. An alternative to the

DriverManager

facility, a

DataSource

object
is the preferred means of getting a connection. An object that implements
the

DataSource

interface will typically be
registered with a naming service based on the
Java™ Naming and Directory (JNDI) API.

The

DataSource

interface is implemented by a driver vendor.
There are three types of implementations:

- Basic implementation -- produces a standard

Connection

object

Connection pooling implementation -- produces a

Connection

object that will automatically participate in connection pooling. This
implementation works with a middle-tier connection pooling manager.

Distributed transaction implementation -- produces a

Connection

object that may be used for distributed
transactions and almost always participates in connection pooling.
This implementation works with a middle-tier
transaction manager and almost always with a connection
pooling manager.

A

DataSource

object has properties that can be modified
when necessary. For example, if the data source is moved to a different
server, the property for the server can be changed. The benefit is that
because the data source's properties can be changed, any code accessing
that data source does not need to be changed.

A driver that is accessed via a

DataSource

object does not
register itself with the

DriverManager

. Rather, a

DataSource

object is retrieved through a lookup operation
and then used to create a

Connection

object. With a basic
implementation, the connection obtained through a

DataSource

object is identical to a connection obtained through the

DriverManager

facility.

An implementation of

DataSource

must include a public no-arg
constructor.

The

DataSource

interface is implemented by a driver vendor.
There are three types of implementations:

- Basic implementation -- produces a standard

Connection

object

Connection pooling implementation -- produces a

Connection

object that will automatically participate in connection pooling. This
implementation works with a middle-tier connection pooling manager.

Distributed transaction implementation -- produces a

Connection

object that may be used for distributed
transactions and almost always participates in connection pooling.
This implementation works with a middle-tier
transaction manager and almost always with a connection
pooling manager.

A

DataSource

object has properties that can be modified
when necessary. For example, if the data source is moved to a different
server, the property for the server can be changed. The benefit is that
because the data source's properties can be changed, any code accessing
that data source does not need to be changed.

A driver that is accessed via a

DataSource

object does not
register itself with the

DriverManager

. Rather, a

DataSource

object is retrieved through a lookup operation
and then used to create a

Connection

object. With a basic
implementation, the connection obtained through a

DataSource

object is identical to a connection obtained through the

DriverManager

facility.

An implementation of

DataSource

must include a public no-arg
constructor.

Basic implementation -- produces a standard

Connection

object

Connection pooling implementation -- produces a

Connection

object that will automatically participate in connection pooling. This
implementation works with a middle-tier connection pooling manager.

Distributed transaction implementation -- produces a

Connection

object that may be used for distributed
transactions and almost always participates in connection pooling.
This implementation works with a middle-tier
transaction manager and almost always with a connection
pooling manager.

A

DataSource

object has properties that can be modified
when necessary. For example, if the data source is moved to a different
server, the property for the server can be changed. The benefit is that
because the data source's properties can be changed, any code accessing
that data source does not need to be changed.

A driver that is accessed via a

DataSource

object does not
register itself with the

DriverManager

. Rather, a

DataSource

object is retrieved through a lookup operation
and then used to create a

Connection

object. With a basic
implementation, the connection obtained through a

DataSource

object is identical to a connection obtained through the

DriverManager

facility.

An implementation of

DataSource

must include a public no-arg
constructor.

A driver that is accessed via a

DataSource

object does not
register itself with the

DriverManager

. Rather, a

DataSource

object is retrieved through a lookup operation
and then used to create a

Connection

object. With a basic
implementation, the connection obtained through a

DataSource

object is identical to a connection obtained through the

DriverManager

facility.

An implementation of

DataSource

must include a public no-arg
constructor.

An implementation of

DataSource

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

ConnectionBuilder

createConnectionBuilder

()

Create a new

ConnectionBuilder

instance

Connection

getConnection

()

Attempts to establish a connection with the data source that
this

DataSource

object represents.

Connection

getConnection

​(

String

username,

String

password)

Attempts to establish a connection with the data source that
this

DataSource

object represents.

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

- Methods declared in interface java.sql.

Wrapper

isWrapperFor

,

unwrap

Method Summary

All Methods

Instance Methods

Abstract Methods

Default Methods

Modifier and Type

Method

Description

default

ConnectionBuilder

createConnectionBuilder

()

Create a new

ConnectionBuilder

instance

Connection

getConnection

()

Attempts to establish a connection with the data source that
this

DataSource

object represents.

Connection

getConnection

​(

String

username,

String

password)

Attempts to establish a connection with the data source that
this

DataSource

object represents.

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

- Methods declared in interface java.sql.

Wrapper

isWrapperFor

,

unwrap

---

#### Method Summary

Create a new

ConnectionBuilder

instance

Attempts to establish a connection with the data source that
this

DataSource

object represents.

Gets the maximum time in seconds that this data source can wait
while attempting to connect to a database.

Retrieves the log writer for this

DataSource

object.

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

Methods declared in interface java.sql.

Wrapper

isWrapperFor

,

unwrap

---

#### Methods declared in interface java.sql. Wrapper

============ METHOD DETAIL ==========

- Method Detail

- getConnection

```java
Connection
getConnection()
throws
SQLException
```

Attempts to establish a connection with the data source that
this

DataSource

object represents.

**Returns:** a connection to the data source
**Throws:** SQLException

- if a database access error occurs
**Throws:** SQLTimeoutException

- when the driver has determined that the
timeout value specified by the

setLoginTimeout

method
has been exceeded and has at least tried to cancel the
current database connection attempt

- getConnection

```java
Connection
getConnection​(
String
username,

String
password)
throws
SQLException
```

Attempts to establish a connection with the data source that
this

DataSource

object represents.

**Parameters:** username

- the database user on whose behalf the connection is
being made
**Parameters:** password

- the user's password
**Returns:** a connection to the data source
**Throws:** SQLException

- if a database access error occurs
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

- createConnectionBuilder

```java
default
ConnectionBuilder
createConnectionBuilder()
throws
SQLException
```

Create a new

ConnectionBuilder

instance

**Implementation Requirements:** The default implementation will throw a

SQLFeatureNotSupportedException
**Returns:** The ConnectionBuilder instance that was created
**Throws:** SQLException

- if an error occurs creating the builder
**Throws:** SQLFeatureNotSupportedException

- if the driver does not support sharding
**Since:** 9
**See Also:** ConnectionBuilder

Method Detail

- getConnection

```java
Connection
getConnection()
throws
SQLException
```

Attempts to establish a connection with the data source that
this

DataSource

object represents.

**Returns:** a connection to the data source
**Throws:** SQLException

- if a database access error occurs
**Throws:** SQLTimeoutException

- when the driver has determined that the
timeout value specified by the

setLoginTimeout

method
has been exceeded and has at least tried to cancel the
current database connection attempt

- getConnection

```java
Connection
getConnection​(
String
username,

String
password)
throws
SQLException
```

Attempts to establish a connection with the data source that
this

DataSource

object represents.

**Parameters:** username

- the database user on whose behalf the connection is
being made
**Parameters:** password

- the user's password
**Returns:** a connection to the data source
**Throws:** SQLException

- if a database access error occurs
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

- createConnectionBuilder

```java
default
ConnectionBuilder
createConnectionBuilder()
throws
SQLException
```

Create a new

ConnectionBuilder

instance

**Implementation Requirements:** The default implementation will throw a

SQLFeatureNotSupportedException
**Returns:** The ConnectionBuilder instance that was created
**Throws:** SQLException

- if an error occurs creating the builder
**Throws:** SQLFeatureNotSupportedException

- if the driver does not support sharding
**Since:** 9
**See Also:** ConnectionBuilder

---

#### Method Detail

getConnection

```java
Connection
getConnection()
throws
SQLException
```

Attempts to establish a connection with the data source that
this

DataSource

object represents.

**Returns:** a connection to the data source
**Throws:** SQLException

- if a database access error occurs
**Throws:** SQLTimeoutException

- when the driver has determined that the
timeout value specified by the

setLoginTimeout

method
has been exceeded and has at least tried to cancel the
current database connection attempt

---

#### getConnection

Connection

getConnection()
throws

SQLException

Attempts to establish a connection with the data source that
this

DataSource

object represents.

getConnection

```java
Connection
getConnection​(
String
username,

String
password)
throws
SQLException
```

Attempts to establish a connection with the data source that
this

DataSource

object represents.

**Parameters:** username

- the database user on whose behalf the connection is
being made
**Parameters:** password

- the user's password
**Returns:** a connection to the data source
**Throws:** SQLException

- if a database access error occurs
**Throws:** SQLTimeoutException

- when the driver has determined that the
timeout value specified by the

setLoginTimeout

method
has been exceeded and has at least tried to cancel the
current database connection attempt
**Since:** 1.4

---

#### getConnection

Connection

getConnection​(

String

username,

String

password)
throws

SQLException

Attempts to establish a connection with the data source that
this

DataSource

object represents.

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

createConnectionBuilder

```java
default
ConnectionBuilder
createConnectionBuilder()
throws
SQLException
```

Create a new

ConnectionBuilder

instance

**Implementation Requirements:** The default implementation will throw a

SQLFeatureNotSupportedException
**Returns:** The ConnectionBuilder instance that was created
**Throws:** SQLException

- if an error occurs creating the builder
**Throws:** SQLFeatureNotSupportedException

- if the driver does not support sharding
**Since:** 9
**See Also:** ConnectionBuilder

---

#### createConnectionBuilder

default

ConnectionBuilder

createConnectionBuilder()
throws

SQLException

Create a new

ConnectionBuilder

instance

---

