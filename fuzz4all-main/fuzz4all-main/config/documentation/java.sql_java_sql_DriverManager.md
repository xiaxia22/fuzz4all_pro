# Class DriverManager

**Source:** `java.sql\java\sql\DriverManager.html`

### Class Description

```java
public class
DriverManager

extends
Object
```

The basic service for managing a set of JDBC drivers.

NOTE:

The

DataSource

interface, provides
another way to connect to a data source.
The use of a

DataSource

object is the preferred means of
connecting to a data source.

As part of its initialization, the

DriverManager

class will
attempt to load available JDBC drivers by using:

- The

jdbc.drivers

system property which contains a
colon separated list of fully qualified class names of JDBC drivers. Each
driver is loaded using the

system class loader

:

- jdbc.drivers=foo.bah.Driver:wombat.sql.Driver:bad.taste.ourDriver

Service providers of the

java.sql.Driver

class, that are loaded
via the

service-provider loading

mechanism.

**Implementation Note:** DriverManager

initialization is done lazily and looks up service
providers using the thread context class loader. The drivers loaded and
available to an application will depend on the thread context class loader of
the thread that triggers driver initialization by

DriverManager

.

When the method

getConnection

is called,
the

DriverManager

will attempt to
locate a suitable driver from amongst those loaded at
initialization and those loaded explicitly using the same class loader
as the current application.
**Since:** 1.1
**See Also:** Driver

,

Connection

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### public static
PrintWriter
getLogWriter()

Retrieves the log writer.

The

getLogWriter

and

setLogWriter

methods should be used instead
of the

get/setlogStream

methods, which are deprecated.

**Returns:**
- a

java.io.PrintWriter

object

**See Also:**
- setLogWriter(java.io.PrintWriter)

**Since:**
- 1.2

---

#### public static void setLogWriter​(
PrintWriter
out)

Sets the logging/tracing

PrintWriter

object
that is used by the

DriverManager

and all drivers.

If a security manager exists, its

checkPermission

method is first called with a

SQLPermission("setLog")

permission to check that the caller is allowed to call

setLogWriter

.

**Parameters:**
- out

- the new logging/tracing

PrintStream

object;

null

to disable logging and tracing

**Throws:**
- SecurityException

- if a security manager exists and its

checkPermission

method denies permission to set the log writer.

**See Also:**
- SecurityManager.checkPermission(java.security.Permission)

,

getLogWriter()

**Since:**
- 1.2

---

#### public static
Connection
getConnection​(
String
url,

Properties
info)
throws
SQLException

Attempts to establish a connection to the given database URL.
The

DriverManager

attempts to select an appropriate driver from
the set of registered JDBC drivers.

Note:

If a property is specified as part of the

url

and
is also specified in the

Properties

object, it is
implementation-defined as to which value will take precedence.
For maximum portability, an application should only specify a
property once.

**Parameters:**
- url

- a database url of the form

jdbc:

subprotocol

:

subname
- info

- a list of arbitrary string tag/value pairs as
connection arguments; normally at least a "user" and
"password" property should be included

**Returns:**
- a Connection to the URL

**Throws:**
- SQLException

- if a database access error occurs or the url is

null
- SQLTimeoutException

- when the driver has determined that the
timeout value specified by the

setLoginTimeout

method
has been exceeded and has at least tried to cancel the
current database connection attempt

---

#### public static
Connection
getConnection​(
String
url,

String
user,

String
password)
throws
SQLException

Attempts to establish a connection to the given database URL.
The

DriverManager

attempts to select an appropriate driver from
the set of registered JDBC drivers.

Note:

If the

user

or

password

property are
also specified as part of the

url

, it is
implementation-defined as to which value will take precedence.
For maximum portability, an application should only specify a
property once.

**Parameters:**
- url

- a database url of the form

jdbc:

subprotocol

:

subname
- user

- the database user on whose behalf the connection is being
made
- password

- the user's password

**Returns:**
- a connection to the URL

**Throws:**
- SQLException

- if a database access error occurs or the url is

null
- SQLTimeoutException

- when the driver has determined that the
timeout value specified by the

setLoginTimeout

method
has been exceeded and has at least tried to cancel the
current database connection attempt

---

#### public static
Connection
getConnection​(
String
url)
throws
SQLException

Attempts to establish a connection to the given database URL.
The

DriverManager

attempts to select an appropriate driver from
the set of registered JDBC drivers.

**Parameters:**
- url

- a database url of the form

jdbc:

subprotocol

:

subname

**Returns:**
- a connection to the URL

**Throws:**
- SQLException

- if a database access error occurs or the url is

null
- SQLTimeoutException

- when the driver has determined that the
timeout value specified by the

setLoginTimeout

method
has been exceeded and has at least tried to cancel the
current database connection attempt

---

#### public static
Driver
getDriver​(
String
url)
throws
SQLException

Attempts to locate a driver that understands the given URL.
The

DriverManager

attempts to select an appropriate driver from
the set of registered JDBC drivers.

**Parameters:**
- url

- a database URL of the form

jdbc:

subprotocol

:

subname

**Returns:**
- a

Driver

object representing a driver
that can connect to the given URL

**Throws:**
- SQLException

- if a database access error occurs

---

#### public static void registerDriver​(
Driver
driver)
throws
SQLException

Registers the given driver with the

DriverManager

.
A newly-loaded driver class should call
the method

registerDriver

to make itself
known to the

DriverManager

. If the driver is currently
registered, no action is taken.

**Parameters:**
- driver

- the new JDBC Driver that is to be registered with the

DriverManager

**Throws:**
- SQLException

- if a database access error occurs
- NullPointerException

- if

driver

is null

---

#### public static void registerDriver​(
Driver
driver,

DriverAction
da)
throws
SQLException

Registers the given driver with the

DriverManager

.
A newly-loaded driver class should call
the method

registerDriver

to make itself
known to the

DriverManager

. If the driver is currently
registered, no action is taken.

**Parameters:**
- driver

- the new JDBC Driver that is to be registered with the

DriverManager
- da

- the

DriverAction

implementation to be used when

DriverManager#deregisterDriver

is called

**Throws:**
- SQLException

- if a database access error occurs
- NullPointerException

- if

driver

is null

**Since:**
- 1.8

---

#### public static void deregisterDriver​(
Driver
driver)
throws
SQLException

Removes the specified driver from the

DriverManager

's list of
registered drivers.

If a

null

value is specified for the driver to be removed, then no
action is taken.

If a security manager exists, its

checkPermission

method is first called with a

SQLPermission("deregisterDriver")

permission to check that the caller is allowed to deregister a JDBC Driver.

If the specified driver is not found in the list of registered drivers,
then no action is taken. If the driver was found, it will be removed
from the list of registered drivers.

If a

DriverAction

instance was specified when the JDBC driver was
registered, its deregister method will be called
prior to the driver being removed from the list of registered drivers.

**Parameters:**
- driver

- the JDBC Driver to remove

**Throws:**
- SQLException

- if a database access error occurs
- SecurityException

- if a security manager exists and its

checkPermission

method denies permission to deregister a driver.

**See Also:**
- SecurityManager.checkPermission(java.security.Permission)

---

#### public static
Enumeration
<
Driver
> getDrivers()

Retrieves an Enumeration with all of the currently loaded JDBC drivers
to which the current caller has access.

Note:

The classname of a driver can be found using

d.getClass().getName()

**Returns:**
- the list of JDBC Drivers loaded by the caller's class loader

**See Also:**
- drivers()

---

#### public static
Stream
<
Driver
> drivers()

Retrieves a Stream with all of the currently loaded JDBC drivers
to which the current caller has access.

**Returns:**
- the stream of JDBC Drivers loaded by the caller's class loader

**Since:**
- 9

---

#### public static void setLoginTimeout​(int seconds)

Sets the maximum time in seconds that a driver will wait
while attempting to connect to a database once the driver has
been identified.

**Parameters:**
- seconds

- the login time limit in seconds; zero means there is no limit

**See Also:**
- getLoginTimeout()

---

#### public static int getLoginTimeout()

Gets the maximum time in seconds that a driver can wait
when attempting to log in to a database.

**Returns:**
- the driver login time limit in seconds

**See Also:**
- setLoginTimeout(int)

---

#### @Deprecated
(
since
="1.2")
public static void setLogStream​(
PrintStream
out)

Sets the logging/tracing PrintStream that is used
by the

DriverManager

and all drivers.

If a security manager exists, its

checkPermission

method is first called with a

SQLPermission("setLog")

permission to check that the caller is allowed to call

setLogStream

.

**Parameters:**
- out

- the new logging/tracing PrintStream; to disable, set to

null

**Throws:**
- SecurityException

- if a security manager exists and its

checkPermission

method denies permission to set the log stream.

**See Also:**
- SecurityManager.checkPermission(java.security.Permission)

,

getLogStream()

---

#### @Deprecated
(
since
="1.2")
public static
PrintStream
getLogStream()

Retrieves the logging/tracing PrintStream that is used by the

DriverManager

and all drivers.

**Returns:**
- the logging/tracing PrintStream; if disabled, is

null

**See Also:**
- setLogStream(java.io.PrintStream)

---

#### public static void println​(
String
message)

Prints a message to the current JDBC log stream.

**Parameters:**
- message

- a log or tracing message

---

### Additional Sections

#### Class DriverManager

java.lang.Object

- java.sql.DriverManager

java.sql.DriverManager

```java
public class
DriverManager

extends
Object
```

The basic service for managing a set of JDBC drivers.

NOTE:

The

DataSource

interface, provides
another way to connect to a data source.
The use of a

DataSource

object is the preferred means of
connecting to a data source.

As part of its initialization, the

DriverManager

class will
attempt to load available JDBC drivers by using:

- The

jdbc.drivers

system property which contains a
colon separated list of fully qualified class names of JDBC drivers. Each
driver is loaded using the

system class loader

:

- jdbc.drivers=foo.bah.Driver:wombat.sql.Driver:bad.taste.ourDriver

Service providers of the

java.sql.Driver

class, that are loaded
via the

service-provider loading

mechanism.

**Implementation Note:** DriverManager

initialization is done lazily and looks up service
providers using the thread context class loader. The drivers loaded and
available to an application will depend on the thread context class loader of
the thread that triggers driver initialization by

DriverManager

.

When the method

getConnection

is called,
the

DriverManager

will attempt to
locate a suitable driver from amongst those loaded at
initialization and those loaded explicitly using the same class loader
as the current application.
**Since:** 1.1
**See Also:** Driver

,

Connection

public class

DriverManager

extends

Object

The basic service for managing a set of JDBC drivers.

NOTE:

The

DataSource

interface, provides
another way to connect to a data source.
The use of a

DataSource

object is the preferred means of
connecting to a data source.

As part of its initialization, the

DriverManager

class will
attempt to load available JDBC drivers by using:

- The

jdbc.drivers

system property which contains a
colon separated list of fully qualified class names of JDBC drivers. Each
driver is loaded using the

system class loader

:

- jdbc.drivers=foo.bah.Driver:wombat.sql.Driver:bad.taste.ourDriver

Service providers of the

java.sql.Driver

class, that are loaded
via the

service-provider loading

mechanism.

NOTE:

The

DataSource

interface, provides
another way to connect to a data source.
The use of a

DataSource

object is the preferred means of
connecting to a data source.

As part of its initialization, the

DriverManager

class will
attempt to load available JDBC drivers by using:

- The

jdbc.drivers

system property which contains a
colon separated list of fully qualified class names of JDBC drivers. Each
driver is loaded using the

system class loader

:

- jdbc.drivers=foo.bah.Driver:wombat.sql.Driver:bad.taste.ourDriver

Service providers of the

java.sql.Driver

class, that are loaded
via the

service-provider loading

mechanism.

As part of its initialization, the

DriverManager

class will
attempt to load available JDBC drivers by using:

- The

jdbc.drivers

system property which contains a
colon separated list of fully qualified class names of JDBC drivers. Each
driver is loaded using the

system class loader

:

- jdbc.drivers=foo.bah.Driver:wombat.sql.Driver:bad.taste.ourDriver

Service providers of the

java.sql.Driver

class, that are loaded
via the

service-provider loading

mechanism.

The

jdbc.drivers

system property which contains a
colon separated list of fully qualified class names of JDBC drivers. Each
driver is loaded using the

system class loader

:

- jdbc.drivers=foo.bah.Driver:wombat.sql.Driver:bad.taste.ourDriver

Service providers of the

java.sql.Driver

class, that are loaded
via the

service-provider loading

mechanism.

jdbc.drivers=foo.bah.Driver:wombat.sql.Driver:bad.taste.ourDriver

When the method

getConnection

is called,
the

DriverManager

will attempt to
locate a suitable driver from amongst those loaded at
initialization and those loaded explicitly using the same class loader
as the current application.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Concrete Methods

Deprecated Methods

Modifier and Type

Method

Description

static void

deregisterDriver

​(

Driver

driver)

Removes the specified driver from the

DriverManager

's list of
registered drivers.

static

Stream

<

Driver

>

drivers

()

Retrieves a Stream with all of the currently loaded JDBC drivers
to which the current caller has access.

static

Connection

getConnection

​(

String

url)

Attempts to establish a connection to the given database URL.

static

Connection

getConnection

​(

String

url,

String

user,

String

password)

Attempts to establish a connection to the given database URL.

static

Connection

getConnection

​(

String

url,

Properties

info)

Attempts to establish a connection to the given database URL.

static

Driver

getDriver

​(

String

url)

Attempts to locate a driver that understands the given URL.

static

Enumeration

<

Driver

>

getDrivers

()

Retrieves an Enumeration with all of the currently loaded JDBC drivers
to which the current caller has access.

static int

getLoginTimeout

()

Gets the maximum time in seconds that a driver can wait
when attempting to log in to a database.

static

PrintStream

getLogStream

()

Deprecated.

Use

getLogWriter

static

PrintWriter

getLogWriter

()

Retrieves the log writer.

static void

println

​(

String

message)

Prints a message to the current JDBC log stream.

static void

registerDriver

​(

Driver

driver)

Registers the given driver with the

DriverManager

.

static void

registerDriver

​(

Driver

driver,

DriverAction

da)

Registers the given driver with the

DriverManager

.

static void

setLoginTimeout

​(int seconds)

Sets the maximum time in seconds that a driver will wait
while attempting to connect to a database once the driver has
been identified.

static void

setLogStream

​(

PrintStream

out)

Deprecated.

Use

setLogWriter

static void

setLogWriter

​(

PrintWriter

out)

Sets the logging/tracing

PrintWriter

object
that is used by the

DriverManager

and all drivers.

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

Method Summary

All Methods

Static Methods

Concrete Methods

Deprecated Methods

Modifier and Type

Method

Description

static void

deregisterDriver

​(

Driver

driver)

Removes the specified driver from the

DriverManager

's list of
registered drivers.

static

Stream

<

Driver

>

drivers

()

Retrieves a Stream with all of the currently loaded JDBC drivers
to which the current caller has access.

static

Connection

getConnection

​(

String

url)

Attempts to establish a connection to the given database URL.

static

Connection

getConnection

​(

String

url,

String

user,

String

password)

Attempts to establish a connection to the given database URL.

static

Connection

getConnection

​(

String

url,

Properties

info)

Attempts to establish a connection to the given database URL.

static

Driver

getDriver

​(

String

url)

Attempts to locate a driver that understands the given URL.

static

Enumeration

<

Driver

>

getDrivers

()

Retrieves an Enumeration with all of the currently loaded JDBC drivers
to which the current caller has access.

static int

getLoginTimeout

()

Gets the maximum time in seconds that a driver can wait
when attempting to log in to a database.

static

PrintStream

getLogStream

()

Deprecated.

Use

getLogWriter

static

PrintWriter

getLogWriter

()

Retrieves the log writer.

static void

println

​(

String

message)

Prints a message to the current JDBC log stream.

static void

registerDriver

​(

Driver

driver)

Registers the given driver with the

DriverManager

.

static void

registerDriver

​(

Driver

driver,

DriverAction

da)

Registers the given driver with the

DriverManager

.

static void

setLoginTimeout

​(int seconds)

Sets the maximum time in seconds that a driver will wait
while attempting to connect to a database once the driver has
been identified.

static void

setLogStream

​(

PrintStream

out)

Deprecated.

Use

setLogWriter

static void

setLogWriter

​(

PrintWriter

out)

Sets the logging/tracing

PrintWriter

object
that is used by the

DriverManager

and all drivers.

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

Removes the specified driver from the

DriverManager

's list of
registered drivers.

Retrieves a Stream with all of the currently loaded JDBC drivers
to which the current caller has access.

Attempts to establish a connection to the given database URL.

Attempts to locate a driver that understands the given URL.

Retrieves an Enumeration with all of the currently loaded JDBC drivers
to which the current caller has access.

Gets the maximum time in seconds that a driver can wait
when attempting to log in to a database.

Deprecated.

Use

getLogWriter

Retrieves the log writer.

Prints a message to the current JDBC log stream.

Registers the given driver with the

DriverManager

.

Sets the maximum time in seconds that a driver will wait
while attempting to connect to a database once the driver has
been identified.

Deprecated.

Use

setLogWriter

Sets the logging/tracing

PrintWriter

object
that is used by the

DriverManager

and all drivers.

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

============ METHOD DETAIL ==========

- Method Detail

- getLogWriter

```java
public static
PrintWriter
getLogWriter()
```

Retrieves the log writer.

The

getLogWriter

and

setLogWriter

methods should be used instead
of the

get/setlogStream

methods, which are deprecated.

**Returns:** a

java.io.PrintWriter

object
**Since:** 1.2
**See Also:** setLogWriter(java.io.PrintWriter)

- setLogWriter

```java
public static void setLogWriter​(
PrintWriter
out)
```

Sets the logging/tracing

PrintWriter

object
that is used by the

DriverManager

and all drivers.

If a security manager exists, its

checkPermission

method is first called with a

SQLPermission("setLog")

permission to check that the caller is allowed to call

setLogWriter

.

**Parameters:** out

- the new logging/tracing

PrintStream

object;

null

to disable logging and tracing
**Throws:** SecurityException

- if a security manager exists and its

checkPermission

method denies permission to set the log writer.
**Since:** 1.2
**See Also:** SecurityManager.checkPermission(java.security.Permission)

,

getLogWriter()

- getConnection

```java
public static
Connection
getConnection​(
String
url,

Properties
info)
throws
SQLException
```

Attempts to establish a connection to the given database URL.
The

DriverManager

attempts to select an appropriate driver from
the set of registered JDBC drivers.

Note:

If a property is specified as part of the

url

and
is also specified in the

Properties

object, it is
implementation-defined as to which value will take precedence.
For maximum portability, an application should only specify a
property once.

**Parameters:** url

- a database url of the form

jdbc:

subprotocol

:

subname
**Parameters:** info

- a list of arbitrary string tag/value pairs as
connection arguments; normally at least a "user" and
"password" property should be included
**Returns:** a Connection to the URL
**Throws:** SQLException

- if a database access error occurs or the url is

null
**Throws:** SQLTimeoutException

- when the driver has determined that the
timeout value specified by the

setLoginTimeout

method
has been exceeded and has at least tried to cancel the
current database connection attempt

- getConnection

```java
public static
Connection
getConnection​(
String
url,

String
user,

String
password)
throws
SQLException
```

Attempts to establish a connection to the given database URL.
The

DriverManager

attempts to select an appropriate driver from
the set of registered JDBC drivers.

Note:

If the

user

or

password

property are
also specified as part of the

url

, it is
implementation-defined as to which value will take precedence.
For maximum portability, an application should only specify a
property once.

**Parameters:** url

- a database url of the form

jdbc:

subprotocol

:

subname
**Parameters:** user

- the database user on whose behalf the connection is being
made
**Parameters:** password

- the user's password
**Returns:** a connection to the URL
**Throws:** SQLException

- if a database access error occurs or the url is

null
**Throws:** SQLTimeoutException

- when the driver has determined that the
timeout value specified by the

setLoginTimeout

method
has been exceeded and has at least tried to cancel the
current database connection attempt

- getConnection

```java
public static
Connection
getConnection​(
String
url)
throws
SQLException
```

Attempts to establish a connection to the given database URL.
The

DriverManager

attempts to select an appropriate driver from
the set of registered JDBC drivers.

**Parameters:** url

- a database url of the form

jdbc:

subprotocol

:

subname
**Returns:** a connection to the URL
**Throws:** SQLException

- if a database access error occurs or the url is

null
**Throws:** SQLTimeoutException

- when the driver has determined that the
timeout value specified by the

setLoginTimeout

method
has been exceeded and has at least tried to cancel the
current database connection attempt

- getDriver

```java
public static
Driver
getDriver​(
String
url)
throws
SQLException
```

Attempts to locate a driver that understands the given URL.
The

DriverManager

attempts to select an appropriate driver from
the set of registered JDBC drivers.

**Parameters:** url

- a database URL of the form

jdbc:

subprotocol

:

subname
**Returns:** a

Driver

object representing a driver
that can connect to the given URL
**Throws:** SQLException

- if a database access error occurs

- registerDriver

```java
public static void registerDriver​(
Driver
driver)
throws
SQLException
```

Registers the given driver with the

DriverManager

.
A newly-loaded driver class should call
the method

registerDriver

to make itself
known to the

DriverManager

. If the driver is currently
registered, no action is taken.

**Parameters:** driver

- the new JDBC Driver that is to be registered with the

DriverManager
**Throws:** SQLException

- if a database access error occurs
**Throws:** NullPointerException

- if

driver

is null

- registerDriver

```java
public static void registerDriver​(
Driver
driver,

DriverAction
da)
throws
SQLException
```

Registers the given driver with the

DriverManager

.
A newly-loaded driver class should call
the method

registerDriver

to make itself
known to the

DriverManager

. If the driver is currently
registered, no action is taken.

**Parameters:** driver

- the new JDBC Driver that is to be registered with the

DriverManager
**Parameters:** da

- the

DriverAction

implementation to be used when

DriverManager#deregisterDriver

is called
**Throws:** SQLException

- if a database access error occurs
**Throws:** NullPointerException

- if

driver

is null
**Since:** 1.8

- deregisterDriver

```java
public static void deregisterDriver​(
Driver
driver)
throws
SQLException
```

Removes the specified driver from the

DriverManager

's list of
registered drivers.

If a

null

value is specified for the driver to be removed, then no
action is taken.

If a security manager exists, its

checkPermission

method is first called with a

SQLPermission("deregisterDriver")

permission to check that the caller is allowed to deregister a JDBC Driver.

If the specified driver is not found in the list of registered drivers,
then no action is taken. If the driver was found, it will be removed
from the list of registered drivers.

If a

DriverAction

instance was specified when the JDBC driver was
registered, its deregister method will be called
prior to the driver being removed from the list of registered drivers.

**Parameters:** driver

- the JDBC Driver to remove
**Throws:** SQLException

- if a database access error occurs
**Throws:** SecurityException

- if a security manager exists and its

checkPermission

method denies permission to deregister a driver.
**See Also:** SecurityManager.checkPermission(java.security.Permission)

- getDrivers

```java
public static
Enumeration
<
Driver
> getDrivers()
```

Retrieves an Enumeration with all of the currently loaded JDBC drivers
to which the current caller has access.

Note:

The classname of a driver can be found using

d.getClass().getName()

**Returns:** the list of JDBC Drivers loaded by the caller's class loader
**See Also:** drivers()

- drivers

```java
public static
Stream
<
Driver
> drivers()
```

Retrieves a Stream with all of the currently loaded JDBC drivers
to which the current caller has access.

**Returns:** the stream of JDBC Drivers loaded by the caller's class loader
**Since:** 9

- setLoginTimeout

```java
public static void setLoginTimeout​(int seconds)
```

Sets the maximum time in seconds that a driver will wait
while attempting to connect to a database once the driver has
been identified.

**Parameters:** seconds

- the login time limit in seconds; zero means there is no limit
**See Also:** getLoginTimeout()

- getLoginTimeout

```java
public static int getLoginTimeout()
```

Gets the maximum time in seconds that a driver can wait
when attempting to log in to a database.

**Returns:** the driver login time limit in seconds
**See Also:** setLoginTimeout(int)

- setLogStream

```java
@Deprecated
(
since
="1.2")
public static void setLogStream​(
PrintStream
out)
```

Deprecated.

Use

setLogWriter

Sets the logging/tracing PrintStream that is used
by the

DriverManager

and all drivers.

If a security manager exists, its

checkPermission

method is first called with a

SQLPermission("setLog")

permission to check that the caller is allowed to call

setLogStream

.

**Parameters:** out

- the new logging/tracing PrintStream; to disable, set to

null
**Throws:** SecurityException

- if a security manager exists and its

checkPermission

method denies permission to set the log stream.
**See Also:** SecurityManager.checkPermission(java.security.Permission)

,

getLogStream()

- getLogStream

```java
@Deprecated
(
since
="1.2")
public static
PrintStream
getLogStream()
```

Deprecated.

Use

getLogWriter

Retrieves the logging/tracing PrintStream that is used by the

DriverManager

and all drivers.

**Returns:** the logging/tracing PrintStream; if disabled, is

null
**See Also:** setLogStream(java.io.PrintStream)

- println

```java
public static void println​(
String
message)
```

Prints a message to the current JDBC log stream.

**Parameters:** message

- a log or tracing message

Method Detail

- getLogWriter

```java
public static
PrintWriter
getLogWriter()
```

Retrieves the log writer.

The

getLogWriter

and

setLogWriter

methods should be used instead
of the

get/setlogStream

methods, which are deprecated.

**Returns:** a

java.io.PrintWriter

object
**Since:** 1.2
**See Also:** setLogWriter(java.io.PrintWriter)

- setLogWriter

```java
public static void setLogWriter​(
PrintWriter
out)
```

Sets the logging/tracing

PrintWriter

object
that is used by the

DriverManager

and all drivers.

If a security manager exists, its

checkPermission

method is first called with a

SQLPermission("setLog")

permission to check that the caller is allowed to call

setLogWriter

.

**Parameters:** out

- the new logging/tracing

PrintStream

object;

null

to disable logging and tracing
**Throws:** SecurityException

- if a security manager exists and its

checkPermission

method denies permission to set the log writer.
**Since:** 1.2
**See Also:** SecurityManager.checkPermission(java.security.Permission)

,

getLogWriter()

- getConnection

```java
public static
Connection
getConnection​(
String
url,

Properties
info)
throws
SQLException
```

Attempts to establish a connection to the given database URL.
The

DriverManager

attempts to select an appropriate driver from
the set of registered JDBC drivers.

Note:

If a property is specified as part of the

url

and
is also specified in the

Properties

object, it is
implementation-defined as to which value will take precedence.
For maximum portability, an application should only specify a
property once.

**Parameters:** url

- a database url of the form

jdbc:

subprotocol

:

subname
**Parameters:** info

- a list of arbitrary string tag/value pairs as
connection arguments; normally at least a "user" and
"password" property should be included
**Returns:** a Connection to the URL
**Throws:** SQLException

- if a database access error occurs or the url is

null
**Throws:** SQLTimeoutException

- when the driver has determined that the
timeout value specified by the

setLoginTimeout

method
has been exceeded and has at least tried to cancel the
current database connection attempt

- getConnection

```java
public static
Connection
getConnection​(
String
url,

String
user,

String
password)
throws
SQLException
```

Attempts to establish a connection to the given database URL.
The

DriverManager

attempts to select an appropriate driver from
the set of registered JDBC drivers.

Note:

If the

user

or

password

property are
also specified as part of the

url

, it is
implementation-defined as to which value will take precedence.
For maximum portability, an application should only specify a
property once.

**Parameters:** url

- a database url of the form

jdbc:

subprotocol

:

subname
**Parameters:** user

- the database user on whose behalf the connection is being
made
**Parameters:** password

- the user's password
**Returns:** a connection to the URL
**Throws:** SQLException

- if a database access error occurs or the url is

null
**Throws:** SQLTimeoutException

- when the driver has determined that the
timeout value specified by the

setLoginTimeout

method
has been exceeded and has at least tried to cancel the
current database connection attempt

- getConnection

```java
public static
Connection
getConnection​(
String
url)
throws
SQLException
```

Attempts to establish a connection to the given database URL.
The

DriverManager

attempts to select an appropriate driver from
the set of registered JDBC drivers.

**Parameters:** url

- a database url of the form

jdbc:

subprotocol

:

subname
**Returns:** a connection to the URL
**Throws:** SQLException

- if a database access error occurs or the url is

null
**Throws:** SQLTimeoutException

- when the driver has determined that the
timeout value specified by the

setLoginTimeout

method
has been exceeded and has at least tried to cancel the
current database connection attempt

- getDriver

```java
public static
Driver
getDriver​(
String
url)
throws
SQLException
```

Attempts to locate a driver that understands the given URL.
The

DriverManager

attempts to select an appropriate driver from
the set of registered JDBC drivers.

**Parameters:** url

- a database URL of the form

jdbc:

subprotocol

:

subname
**Returns:** a

Driver

object representing a driver
that can connect to the given URL
**Throws:** SQLException

- if a database access error occurs

- registerDriver

```java
public static void registerDriver​(
Driver
driver)
throws
SQLException
```

Registers the given driver with the

DriverManager

.
A newly-loaded driver class should call
the method

registerDriver

to make itself
known to the

DriverManager

. If the driver is currently
registered, no action is taken.

**Parameters:** driver

- the new JDBC Driver that is to be registered with the

DriverManager
**Throws:** SQLException

- if a database access error occurs
**Throws:** NullPointerException

- if

driver

is null

- registerDriver

```java
public static void registerDriver​(
Driver
driver,

DriverAction
da)
throws
SQLException
```

Registers the given driver with the

DriverManager

.
A newly-loaded driver class should call
the method

registerDriver

to make itself
known to the

DriverManager

. If the driver is currently
registered, no action is taken.

**Parameters:** driver

- the new JDBC Driver that is to be registered with the

DriverManager
**Parameters:** da

- the

DriverAction

implementation to be used when

DriverManager#deregisterDriver

is called
**Throws:** SQLException

- if a database access error occurs
**Throws:** NullPointerException

- if

driver

is null
**Since:** 1.8

- deregisterDriver

```java
public static void deregisterDriver​(
Driver
driver)
throws
SQLException
```

Removes the specified driver from the

DriverManager

's list of
registered drivers.

If a

null

value is specified for the driver to be removed, then no
action is taken.

If a security manager exists, its

checkPermission

method is first called with a

SQLPermission("deregisterDriver")

permission to check that the caller is allowed to deregister a JDBC Driver.

If the specified driver is not found in the list of registered drivers,
then no action is taken. If the driver was found, it will be removed
from the list of registered drivers.

If a

DriverAction

instance was specified when the JDBC driver was
registered, its deregister method will be called
prior to the driver being removed from the list of registered drivers.

**Parameters:** driver

- the JDBC Driver to remove
**Throws:** SQLException

- if a database access error occurs
**Throws:** SecurityException

- if a security manager exists and its

checkPermission

method denies permission to deregister a driver.
**See Also:** SecurityManager.checkPermission(java.security.Permission)

- getDrivers

```java
public static
Enumeration
<
Driver
> getDrivers()
```

Retrieves an Enumeration with all of the currently loaded JDBC drivers
to which the current caller has access.

Note:

The classname of a driver can be found using

d.getClass().getName()

**Returns:** the list of JDBC Drivers loaded by the caller's class loader
**See Also:** drivers()

- drivers

```java
public static
Stream
<
Driver
> drivers()
```

Retrieves a Stream with all of the currently loaded JDBC drivers
to which the current caller has access.

**Returns:** the stream of JDBC Drivers loaded by the caller's class loader
**Since:** 9

- setLoginTimeout

```java
public static void setLoginTimeout​(int seconds)
```

Sets the maximum time in seconds that a driver will wait
while attempting to connect to a database once the driver has
been identified.

**Parameters:** seconds

- the login time limit in seconds; zero means there is no limit
**See Also:** getLoginTimeout()

- getLoginTimeout

```java
public static int getLoginTimeout()
```

Gets the maximum time in seconds that a driver can wait
when attempting to log in to a database.

**Returns:** the driver login time limit in seconds
**See Also:** setLoginTimeout(int)

- setLogStream

```java
@Deprecated
(
since
="1.2")
public static void setLogStream​(
PrintStream
out)
```

Deprecated.

Use

setLogWriter

Sets the logging/tracing PrintStream that is used
by the

DriverManager

and all drivers.

If a security manager exists, its

checkPermission

method is first called with a

SQLPermission("setLog")

permission to check that the caller is allowed to call

setLogStream

.

**Parameters:** out

- the new logging/tracing PrintStream; to disable, set to

null
**Throws:** SecurityException

- if a security manager exists and its

checkPermission

method denies permission to set the log stream.
**See Also:** SecurityManager.checkPermission(java.security.Permission)

,

getLogStream()

- getLogStream

```java
@Deprecated
(
since
="1.2")
public static
PrintStream
getLogStream()
```

Deprecated.

Use

getLogWriter

Retrieves the logging/tracing PrintStream that is used by the

DriverManager

and all drivers.

**Returns:** the logging/tracing PrintStream; if disabled, is

null
**See Also:** setLogStream(java.io.PrintStream)

- println

```java
public static void println​(
String
message)
```

Prints a message to the current JDBC log stream.

**Parameters:** message

- a log or tracing message

---

#### Method Detail

getLogWriter

```java
public static
PrintWriter
getLogWriter()
```

Retrieves the log writer.

The

getLogWriter

and

setLogWriter

methods should be used instead
of the

get/setlogStream

methods, which are deprecated.

**Returns:** a

java.io.PrintWriter

object
**Since:** 1.2
**See Also:** setLogWriter(java.io.PrintWriter)

---

#### getLogWriter

public static

PrintWriter

getLogWriter()

Retrieves the log writer.

The

getLogWriter

and

setLogWriter

methods should be used instead
of the

get/setlogStream

methods, which are deprecated.

setLogWriter

```java
public static void setLogWriter​(
PrintWriter
out)
```

Sets the logging/tracing

PrintWriter

object
that is used by the

DriverManager

and all drivers.

If a security manager exists, its

checkPermission

method is first called with a

SQLPermission("setLog")

permission to check that the caller is allowed to call

setLogWriter

.

**Parameters:** out

- the new logging/tracing

PrintStream

object;

null

to disable logging and tracing
**Throws:** SecurityException

- if a security manager exists and its

checkPermission

method denies permission to set the log writer.
**Since:** 1.2
**See Also:** SecurityManager.checkPermission(java.security.Permission)

,

getLogWriter()

---

#### setLogWriter

public static void setLogWriter​(

PrintWriter

out)

Sets the logging/tracing

PrintWriter

object
that is used by the

DriverManager

and all drivers.

If a security manager exists, its

checkPermission

method is first called with a

SQLPermission("setLog")

permission to check that the caller is allowed to call

setLogWriter

.

If a security manager exists, its

checkPermission

method is first called with a

SQLPermission("setLog")

permission to check that the caller is allowed to call

setLogWriter

.

getConnection

```java
public static
Connection
getConnection​(
String
url,

Properties
info)
throws
SQLException
```

Attempts to establish a connection to the given database URL.
The

DriverManager

attempts to select an appropriate driver from
the set of registered JDBC drivers.

Note:

If a property is specified as part of the

url

and
is also specified in the

Properties

object, it is
implementation-defined as to which value will take precedence.
For maximum portability, an application should only specify a
property once.

**Parameters:** url

- a database url of the form

jdbc:

subprotocol

:

subname
**Parameters:** info

- a list of arbitrary string tag/value pairs as
connection arguments; normally at least a "user" and
"password" property should be included
**Returns:** a Connection to the URL
**Throws:** SQLException

- if a database access error occurs or the url is

null
**Throws:** SQLTimeoutException

- when the driver has determined that the
timeout value specified by the

setLoginTimeout

method
has been exceeded and has at least tried to cancel the
current database connection attempt

---

#### getConnection

public static

Connection

getConnection​(

String

url,

Properties

info)
throws

SQLException

Attempts to establish a connection to the given database URL.
The

DriverManager

attempts to select an appropriate driver from
the set of registered JDBC drivers.

Note:

If a property is specified as part of the

url

and
is also specified in the

Properties

object, it is
implementation-defined as to which value will take precedence.
For maximum portability, an application should only specify a
property once.

Note:

If a property is specified as part of the

url

and
is also specified in the

Properties

object, it is
implementation-defined as to which value will take precedence.
For maximum portability, an application should only specify a
property once.

getConnection

```java
public static
Connection
getConnection​(
String
url,

String
user,

String
password)
throws
SQLException
```

Attempts to establish a connection to the given database URL.
The

DriverManager

attempts to select an appropriate driver from
the set of registered JDBC drivers.

Note:

If the

user

or

password

property are
also specified as part of the

url

, it is
implementation-defined as to which value will take precedence.
For maximum portability, an application should only specify a
property once.

**Parameters:** url

- a database url of the form

jdbc:

subprotocol

:

subname
**Parameters:** user

- the database user on whose behalf the connection is being
made
**Parameters:** password

- the user's password
**Returns:** a connection to the URL
**Throws:** SQLException

- if a database access error occurs or the url is

null
**Throws:** SQLTimeoutException

- when the driver has determined that the
timeout value specified by the

setLoginTimeout

method
has been exceeded and has at least tried to cancel the
current database connection attempt

---

#### getConnection

public static

Connection

getConnection​(

String

url,

String

user,

String

password)
throws

SQLException

Attempts to establish a connection to the given database URL.
The

DriverManager

attempts to select an appropriate driver from
the set of registered JDBC drivers.

Note:

If the

user

or

password

property are
also specified as part of the

url

, it is
implementation-defined as to which value will take precedence.
For maximum portability, an application should only specify a
property once.

Note:

If the

user

or

password

property are
also specified as part of the

url

, it is
implementation-defined as to which value will take precedence.
For maximum portability, an application should only specify a
property once.

getConnection

```java
public static
Connection
getConnection​(
String
url)
throws
SQLException
```

Attempts to establish a connection to the given database URL.
The

DriverManager

attempts to select an appropriate driver from
the set of registered JDBC drivers.

**Parameters:** url

- a database url of the form

jdbc:

subprotocol

:

subname
**Returns:** a connection to the URL
**Throws:** SQLException

- if a database access error occurs or the url is

null
**Throws:** SQLTimeoutException

- when the driver has determined that the
timeout value specified by the

setLoginTimeout

method
has been exceeded and has at least tried to cancel the
current database connection attempt

---

#### getConnection

public static

Connection

getConnection​(

String

url)
throws

SQLException

Attempts to establish a connection to the given database URL.
The

DriverManager

attempts to select an appropriate driver from
the set of registered JDBC drivers.

getDriver

```java
public static
Driver
getDriver​(
String
url)
throws
SQLException
```

Attempts to locate a driver that understands the given URL.
The

DriverManager

attempts to select an appropriate driver from
the set of registered JDBC drivers.

**Parameters:** url

- a database URL of the form

jdbc:

subprotocol

:

subname
**Returns:** a

Driver

object representing a driver
that can connect to the given URL
**Throws:** SQLException

- if a database access error occurs

---

#### getDriver

public static

Driver

getDriver​(

String

url)
throws

SQLException

Attempts to locate a driver that understands the given URL.
The

DriverManager

attempts to select an appropriate driver from
the set of registered JDBC drivers.

registerDriver

```java
public static void registerDriver​(
Driver
driver)
throws
SQLException
```

Registers the given driver with the

DriverManager

.
A newly-loaded driver class should call
the method

registerDriver

to make itself
known to the

DriverManager

. If the driver is currently
registered, no action is taken.

**Parameters:** driver

- the new JDBC Driver that is to be registered with the

DriverManager
**Throws:** SQLException

- if a database access error occurs
**Throws:** NullPointerException

- if

driver

is null

---

#### registerDriver

public static void registerDriver​(

Driver

driver)
throws

SQLException

Registers the given driver with the

DriverManager

.
A newly-loaded driver class should call
the method

registerDriver

to make itself
known to the

DriverManager

. If the driver is currently
registered, no action is taken.

registerDriver

```java
public static void registerDriver​(
Driver
driver,

DriverAction
da)
throws
SQLException
```

Registers the given driver with the

DriverManager

.
A newly-loaded driver class should call
the method

registerDriver

to make itself
known to the

DriverManager

. If the driver is currently
registered, no action is taken.

**Parameters:** driver

- the new JDBC Driver that is to be registered with the

DriverManager
**Parameters:** da

- the

DriverAction

implementation to be used when

DriverManager#deregisterDriver

is called
**Throws:** SQLException

- if a database access error occurs
**Throws:** NullPointerException

- if

driver

is null
**Since:** 1.8

---

#### registerDriver

public static void registerDriver​(

Driver

driver,

DriverAction

da)
throws

SQLException

Registers the given driver with the

DriverManager

.
A newly-loaded driver class should call
the method

registerDriver

to make itself
known to the

DriverManager

. If the driver is currently
registered, no action is taken.

deregisterDriver

```java
public static void deregisterDriver​(
Driver
driver)
throws
SQLException
```

Removes the specified driver from the

DriverManager

's list of
registered drivers.

If a

null

value is specified for the driver to be removed, then no
action is taken.

If a security manager exists, its

checkPermission

method is first called with a

SQLPermission("deregisterDriver")

permission to check that the caller is allowed to deregister a JDBC Driver.

If the specified driver is not found in the list of registered drivers,
then no action is taken. If the driver was found, it will be removed
from the list of registered drivers.

If a

DriverAction

instance was specified when the JDBC driver was
registered, its deregister method will be called
prior to the driver being removed from the list of registered drivers.

**Parameters:** driver

- the JDBC Driver to remove
**Throws:** SQLException

- if a database access error occurs
**Throws:** SecurityException

- if a security manager exists and its

checkPermission

method denies permission to deregister a driver.
**See Also:** SecurityManager.checkPermission(java.security.Permission)

---

#### deregisterDriver

public static void deregisterDriver​(

Driver

driver)
throws

SQLException

Removes the specified driver from the

DriverManager

's list of
registered drivers.

If a

null

value is specified for the driver to be removed, then no
action is taken.

If a security manager exists, its

checkPermission

method is first called with a

SQLPermission("deregisterDriver")

permission to check that the caller is allowed to deregister a JDBC Driver.

If the specified driver is not found in the list of registered drivers,
then no action is taken. If the driver was found, it will be removed
from the list of registered drivers.

If a

DriverAction

instance was specified when the JDBC driver was
registered, its deregister method will be called
prior to the driver being removed from the list of registered drivers.

If a

null

value is specified for the driver to be removed, then no
action is taken.

If a security manager exists, its

checkPermission

method is first called with a

SQLPermission("deregisterDriver")

permission to check that the caller is allowed to deregister a JDBC Driver.

If the specified driver is not found in the list of registered drivers,
then no action is taken. If the driver was found, it will be removed
from the list of registered drivers.

If a

DriverAction

instance was specified when the JDBC driver was
registered, its deregister method will be called
prior to the driver being removed from the list of registered drivers.

If a security manager exists, its

checkPermission

method is first called with a

SQLPermission("deregisterDriver")

permission to check that the caller is allowed to deregister a JDBC Driver.

If the specified driver is not found in the list of registered drivers,
then no action is taken. If the driver was found, it will be removed
from the list of registered drivers.

If a

DriverAction

instance was specified when the JDBC driver was
registered, its deregister method will be called
prior to the driver being removed from the list of registered drivers.

If the specified driver is not found in the list of registered drivers,
then no action is taken. If the driver was found, it will be removed
from the list of registered drivers.

If a

DriverAction

instance was specified when the JDBC driver was
registered, its deregister method will be called
prior to the driver being removed from the list of registered drivers.

If a

DriverAction

instance was specified when the JDBC driver was
registered, its deregister method will be called
prior to the driver being removed from the list of registered drivers.

getDrivers

```java
public static
Enumeration
<
Driver
> getDrivers()
```

Retrieves an Enumeration with all of the currently loaded JDBC drivers
to which the current caller has access.

Note:

The classname of a driver can be found using

d.getClass().getName()

**Returns:** the list of JDBC Drivers loaded by the caller's class loader
**See Also:** drivers()

---

#### getDrivers

public static

Enumeration

<

Driver

> getDrivers()

Retrieves an Enumeration with all of the currently loaded JDBC drivers
to which the current caller has access.

Note:

The classname of a driver can be found using

d.getClass().getName()

Note:

The classname of a driver can be found using

d.getClass().getName()

drivers

```java
public static
Stream
<
Driver
> drivers()
```

Retrieves a Stream with all of the currently loaded JDBC drivers
to which the current caller has access.

**Returns:** the stream of JDBC Drivers loaded by the caller's class loader
**Since:** 9

---

#### drivers

public static

Stream

<

Driver

> drivers()

Retrieves a Stream with all of the currently loaded JDBC drivers
to which the current caller has access.

setLoginTimeout

```java
public static void setLoginTimeout​(int seconds)
```

Sets the maximum time in seconds that a driver will wait
while attempting to connect to a database once the driver has
been identified.

**Parameters:** seconds

- the login time limit in seconds; zero means there is no limit
**See Also:** getLoginTimeout()

---

#### setLoginTimeout

public static void setLoginTimeout​(int seconds)

Sets the maximum time in seconds that a driver will wait
while attempting to connect to a database once the driver has
been identified.

getLoginTimeout

```java
public static int getLoginTimeout()
```

Gets the maximum time in seconds that a driver can wait
when attempting to log in to a database.

**Returns:** the driver login time limit in seconds
**See Also:** setLoginTimeout(int)

---

#### getLoginTimeout

public static int getLoginTimeout()

Gets the maximum time in seconds that a driver can wait
when attempting to log in to a database.

setLogStream

```java
@Deprecated
(
since
="1.2")
public static void setLogStream​(
PrintStream
out)
```

Deprecated.

Use

setLogWriter

Sets the logging/tracing PrintStream that is used
by the

DriverManager

and all drivers.

If a security manager exists, its

checkPermission

method is first called with a

SQLPermission("setLog")

permission to check that the caller is allowed to call

setLogStream

.

**Parameters:** out

- the new logging/tracing PrintStream; to disable, set to

null
**Throws:** SecurityException

- if a security manager exists and its

checkPermission

method denies permission to set the log stream.
**See Also:** SecurityManager.checkPermission(java.security.Permission)

,

getLogStream()

---

#### setLogStream

@Deprecated

(

since

="1.2")
public static void setLogStream​(

PrintStream

out)

Sets the logging/tracing PrintStream that is used
by the

DriverManager

and all drivers.

If a security manager exists, its

checkPermission

method is first called with a

SQLPermission("setLog")

permission to check that the caller is allowed to call

setLogStream

.

If a security manager exists, its

checkPermission

method is first called with a

SQLPermission("setLog")

permission to check that the caller is allowed to call

setLogStream

.

getLogStream

```java
@Deprecated
(
since
="1.2")
public static
PrintStream
getLogStream()
```

Deprecated.

Use

getLogWriter

Retrieves the logging/tracing PrintStream that is used by the

DriverManager

and all drivers.

**Returns:** the logging/tracing PrintStream; if disabled, is

null
**See Also:** setLogStream(java.io.PrintStream)

---

#### getLogStream

@Deprecated

(

since

="1.2")
public static

PrintStream

getLogStream()

Retrieves the logging/tracing PrintStream that is used by the

DriverManager

and all drivers.

println

```java
public static void println​(
String
message)
```

Prints a message to the current JDBC log stream.

**Parameters:** message

- a log or tracing message

---

#### println

public static void println​(

String

message)

Prints a message to the current JDBC log stream.

---

