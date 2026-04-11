# Interface PlatformLoggingMXBean

**Source:** `java.management\java\lang\management\PlatformLoggingMXBean.html`

### Class Description

```java
public interface
PlatformLoggingMXBean

extends
PlatformManagedObject
```

The management interface for the

logging

facility.

There is a single global instance of the

PlatformLoggingMXBean

.
The

ManagementFactory.getPlatformMXBean

method can be used to obtain
the

PlatformLoggingMXBean

object as follows:

```java
PlatformLoggingMXBean logging = ManagementFactory.getPlatformMXBean(PlatformLoggingMXBean.class);
```

The

PlatformLoggingMXBean

object is also registered with the
platform

MBeanServer

.
The

ObjectName

for uniquely
identifying the

PlatformLoggingMXBean

within an MBeanServer is:

```java
java.util.logging:type=Logging
```

**All Superinterfaces:** PlatformManagedObject

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### List
<
String
> getLoggerNames()

Returns the list of the currently registered

logger

names. This method
calls

LogManager.getLoggerNames()

and
returns a list of the logger names.

**Returns:**
- A list of

String

each of which is a
currently registered

Logger

name.

---

#### String
getLoggerLevel​(
String
loggerName)

Gets the name of the log

level

associated with the specified logger.
If the specified logger does not exist,

null

is returned.
This method first finds the logger of the given name and
then returns the name of the log level by calling:

Logger.getLevel()

.

getName()

;

If the

Level

of the specified logger is

null

,
which means that this logger's effective level is inherited
from its parent, an empty string will be returned.

**Parameters:**
- loggerName

- The name of the

Logger

to be retrieved.

**Returns:**
- The name of the log level of the specified logger; or
an empty string if the log level of the specified logger
is

null

. If the specified logger does not
exist,

null

is returned.

**See Also:**
- Logger.getLevel()

---

#### void setLoggerLevel​(
String
loggerName,

String
levelName)

Sets the specified logger to the specified new

level

.
If the

levelName

is not

null

, the level
of the specified logger is set to the parsed

Level

matching the

levelName

.
If the

levelName

is

null

, the level
of the specified logger is set to

null

and
the effective level of the logger is inherited from
its nearest ancestor with a specific (non-null) level value.

**Parameters:**
- loggerName

- The name of the

Logger

to be set.
Must be non-null.
- levelName

- The name of the level to set on the specified logger,
or

null

if setting the level to inherit
from its nearest ancestor.

**Throws:**
- IllegalArgumentException

- if the specified logger
does not exist, or

levelName

is not a valid level name.
- SecurityException

- if a security manager exists and if
the caller does not have LoggingPermission("control").

**See Also:**
- Logger.setLevel(java.util.logging.Level)

---

#### String
getParentLoggerName​(
String
loggerName)

Returns the name of the

parent

for the specified logger.
If the specified logger does not exist,

null

is returned.
If the specified logger is the root

Logger

in the namespace,
the result will be an empty string.

**Parameters:**
- loggerName

- The name of a

Logger

.

**Returns:**
- the name of the nearest existing parent logger;
an empty string if the specified logger is the root logger.
If the specified logger does not exist,

null

is returned.

---

### Additional Sections

#### Interface PlatformLoggingMXBean

**All Superinterfaces:** PlatformManagedObject

```java
public interface
PlatformLoggingMXBean

extends
PlatformManagedObject
```

The management interface for the

logging

facility.

There is a single global instance of the

PlatformLoggingMXBean

.
The

ManagementFactory.getPlatformMXBean

method can be used to obtain
the

PlatformLoggingMXBean

object as follows:

```java
PlatformLoggingMXBean logging = ManagementFactory.getPlatformMXBean(PlatformLoggingMXBean.class);
```

The

PlatformLoggingMXBean

object is also registered with the
platform

MBeanServer

.
The

ObjectName

for uniquely
identifying the

PlatformLoggingMXBean

within an MBeanServer is:

```java
java.util.logging:type=Logging
```

**Since:** 1.7

public interface

PlatformLoggingMXBean

extends

PlatformManagedObject

The management interface for the

logging

facility.

There is a single global instance of the

PlatformLoggingMXBean

.
The

ManagementFactory.getPlatformMXBean

method can be used to obtain
the

PlatformLoggingMXBean

object as follows:

```java
PlatformLoggingMXBean logging = ManagementFactory.getPlatformMXBean(PlatformLoggingMXBean.class);
```

The

PlatformLoggingMXBean

object is also registered with the
platform

MBeanServer

.
The

ObjectName

for uniquely
identifying the

PlatformLoggingMXBean

within an MBeanServer is:

```java
java.util.logging:type=Logging
```

There is a single global instance of the

PlatformLoggingMXBean

.
The

ManagementFactory.getPlatformMXBean

method can be used to obtain
the

PlatformLoggingMXBean

object as follows:

```java
PlatformLoggingMXBean logging = ManagementFactory.getPlatformMXBean(PlatformLoggingMXBean.class);
```

The

PlatformLoggingMXBean

object is also registered with the
platform

MBeanServer

.
The

ObjectName

for uniquely
identifying the

PlatformLoggingMXBean

within an MBeanServer is:

```java
java.util.logging:type=Logging
```

PlatformLoggingMXBean logging = ManagementFactory.getPlatformMXBean(PlatformLoggingMXBean.class);

java.util.logging:type=Logging

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

String

getLoggerLevel

​(

String

loggerName)

Gets the name of the log

level

associated with the specified logger.

List

<

String

>

getLoggerNames

()

Returns the list of the currently registered

logger

names.

String

getParentLoggerName

​(

String

loggerName)

Returns the name of the

parent

for the specified logger.

void

setLoggerLevel

​(

String

loggerName,

String

levelName)

Sets the specified logger to the specified new

level

.

- Methods declared in interface java.lang.management.

PlatformManagedObject

getObjectName

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

String

getLoggerLevel

​(

String

loggerName)

Gets the name of the log

level

associated with the specified logger.

List

<

String

>

getLoggerNames

()

Returns the list of the currently registered

logger

names.

String

getParentLoggerName

​(

String

loggerName)

Returns the name of the

parent

for the specified logger.

void

setLoggerLevel

​(

String

loggerName,

String

levelName)

Sets the specified logger to the specified new

level

.

- Methods declared in interface java.lang.management.

PlatformManagedObject

getObjectName

---

#### Method Summary

Gets the name of the log

level

associated with the specified logger.

Returns the list of the currently registered

logger

names.

Returns the name of the

parent

for the specified logger.

Sets the specified logger to the specified new

level

.

Methods declared in interface java.lang.management.

PlatformManagedObject

getObjectName

---

#### Methods declared in interface java.lang.management. PlatformManagedObject

============ METHOD DETAIL ==========

- Method Detail

- getLoggerNames

```java
List
<
String
> getLoggerNames()
```

Returns the list of the currently registered

logger

names. This method
calls

LogManager.getLoggerNames()

and
returns a list of the logger names.

**Returns:** A list of

String

each of which is a
currently registered

Logger

name.

- getLoggerLevel

```java
String
getLoggerLevel​(
String
loggerName)
```

Gets the name of the log

level

associated with the specified logger.
If the specified logger does not exist,

null

is returned.
This method first finds the logger of the given name and
then returns the name of the log level by calling:

Logger.getLevel()

.

getName()

;

If the

Level

of the specified logger is

null

,
which means that this logger's effective level is inherited
from its parent, an empty string will be returned.

**Parameters:** loggerName

- The name of the

Logger

to be retrieved.
**Returns:** The name of the log level of the specified logger; or
an empty string if the log level of the specified logger
is

null

. If the specified logger does not
exist,

null

is returned.
**See Also:** Logger.getLevel()

- setLoggerLevel

```java
void setLoggerLevel​(
String
loggerName,

String
levelName)
```

Sets the specified logger to the specified new

level

.
If the

levelName

is not

null

, the level
of the specified logger is set to the parsed

Level

matching the

levelName

.
If the

levelName

is

null

, the level
of the specified logger is set to

null

and
the effective level of the logger is inherited from
its nearest ancestor with a specific (non-null) level value.

**Parameters:** loggerName

- The name of the

Logger

to be set.
Must be non-null.
**Parameters:** levelName

- The name of the level to set on the specified logger,
or

null

if setting the level to inherit
from its nearest ancestor.
**Throws:** IllegalArgumentException

- if the specified logger
does not exist, or

levelName

is not a valid level name.
**Throws:** SecurityException

- if a security manager exists and if
the caller does not have LoggingPermission("control").
**See Also:** Logger.setLevel(java.util.logging.Level)

- getParentLoggerName

```java
String
getParentLoggerName​(
String
loggerName)
```

Returns the name of the

parent

for the specified logger.
If the specified logger does not exist,

null

is returned.
If the specified logger is the root

Logger

in the namespace,
the result will be an empty string.

**Parameters:** loggerName

- The name of a

Logger

.
**Returns:** the name of the nearest existing parent logger;
an empty string if the specified logger is the root logger.
If the specified logger does not exist,

null

is returned.

Method Detail

- getLoggerNames

```java
List
<
String
> getLoggerNames()
```

Returns the list of the currently registered

logger

names. This method
calls

LogManager.getLoggerNames()

and
returns a list of the logger names.

**Returns:** A list of

String

each of which is a
currently registered

Logger

name.

- getLoggerLevel

```java
String
getLoggerLevel​(
String
loggerName)
```

Gets the name of the log

level

associated with the specified logger.
If the specified logger does not exist,

null

is returned.
This method first finds the logger of the given name and
then returns the name of the log level by calling:

Logger.getLevel()

.

getName()

;

If the

Level

of the specified logger is

null

,
which means that this logger's effective level is inherited
from its parent, an empty string will be returned.

**Parameters:** loggerName

- The name of the

Logger

to be retrieved.
**Returns:** The name of the log level of the specified logger; or
an empty string if the log level of the specified logger
is

null

. If the specified logger does not
exist,

null

is returned.
**See Also:** Logger.getLevel()

- setLoggerLevel

```java
void setLoggerLevel​(
String
loggerName,

String
levelName)
```

Sets the specified logger to the specified new

level

.
If the

levelName

is not

null

, the level
of the specified logger is set to the parsed

Level

matching the

levelName

.
If the

levelName

is

null

, the level
of the specified logger is set to

null

and
the effective level of the logger is inherited from
its nearest ancestor with a specific (non-null) level value.

**Parameters:** loggerName

- The name of the

Logger

to be set.
Must be non-null.
**Parameters:** levelName

- The name of the level to set on the specified logger,
or

null

if setting the level to inherit
from its nearest ancestor.
**Throws:** IllegalArgumentException

- if the specified logger
does not exist, or

levelName

is not a valid level name.
**Throws:** SecurityException

- if a security manager exists and if
the caller does not have LoggingPermission("control").
**See Also:** Logger.setLevel(java.util.logging.Level)

- getParentLoggerName

```java
String
getParentLoggerName​(
String
loggerName)
```

Returns the name of the

parent

for the specified logger.
If the specified logger does not exist,

null

is returned.
If the specified logger is the root

Logger

in the namespace,
the result will be an empty string.

**Parameters:** loggerName

- The name of a

Logger

.
**Returns:** the name of the nearest existing parent logger;
an empty string if the specified logger is the root logger.
If the specified logger does not exist,

null

is returned.

---

#### Method Detail

getLoggerNames

```java
List
<
String
> getLoggerNames()
```

Returns the list of the currently registered

logger

names. This method
calls

LogManager.getLoggerNames()

and
returns a list of the logger names.

**Returns:** A list of

String

each of which is a
currently registered

Logger

name.

---

#### getLoggerNames

List

<

String

> getLoggerNames()

Returns the list of the currently registered

logger

names. This method
calls

LogManager.getLoggerNames()

and
returns a list of the logger names.

getLoggerLevel

```java
String
getLoggerLevel​(
String
loggerName)
```

Gets the name of the log

level

associated with the specified logger.
If the specified logger does not exist,

null

is returned.
This method first finds the logger of the given name and
then returns the name of the log level by calling:

Logger.getLevel()

.

getName()

;

If the

Level

of the specified logger is

null

,
which means that this logger's effective level is inherited
from its parent, an empty string will be returned.

**Parameters:** loggerName

- The name of the

Logger

to be retrieved.
**Returns:** The name of the log level of the specified logger; or
an empty string if the log level of the specified logger
is

null

. If the specified logger does not
exist,

null

is returned.
**See Also:** Logger.getLevel()

---

#### getLoggerLevel

String

getLoggerLevel​(

String

loggerName)

Gets the name of the log

level

associated with the specified logger.
If the specified logger does not exist,

null

is returned.
This method first finds the logger of the given name and
then returns the name of the log level by calling:

Logger.getLevel()

.

getName()

;

If the

Level

of the specified logger is

null

,
which means that this logger's effective level is inherited
from its parent, an empty string will be returned.

If the

Level

of the specified logger is

null

,
which means that this logger's effective level is inherited
from its parent, an empty string will be returned.

setLoggerLevel

```java
void setLoggerLevel​(
String
loggerName,

String
levelName)
```

Sets the specified logger to the specified new

level

.
If the

levelName

is not

null

, the level
of the specified logger is set to the parsed

Level

matching the

levelName

.
If the

levelName

is

null

, the level
of the specified logger is set to

null

and
the effective level of the logger is inherited from
its nearest ancestor with a specific (non-null) level value.

**Parameters:** loggerName

- The name of the

Logger

to be set.
Must be non-null.
**Parameters:** levelName

- The name of the level to set on the specified logger,
or

null

if setting the level to inherit
from its nearest ancestor.
**Throws:** IllegalArgumentException

- if the specified logger
does not exist, or

levelName

is not a valid level name.
**Throws:** SecurityException

- if a security manager exists and if
the caller does not have LoggingPermission("control").
**See Also:** Logger.setLevel(java.util.logging.Level)

---

#### setLoggerLevel

void setLoggerLevel​(

String

loggerName,

String

levelName)

Sets the specified logger to the specified new

level

.
If the

levelName

is not

null

, the level
of the specified logger is set to the parsed

Level

matching the

levelName

.
If the

levelName

is

null

, the level
of the specified logger is set to

null

and
the effective level of the logger is inherited from
its nearest ancestor with a specific (non-null) level value.

getParentLoggerName

```java
String
getParentLoggerName​(
String
loggerName)
```

Returns the name of the

parent

for the specified logger.
If the specified logger does not exist,

null

is returned.
If the specified logger is the root

Logger

in the namespace,
the result will be an empty string.

**Parameters:** loggerName

- The name of a

Logger

.
**Returns:** the name of the nearest existing parent logger;
an empty string if the specified logger is the root logger.
If the specified logger does not exist,

null

is returned.

---

#### getParentLoggerName

String

getParentLoggerName​(

String

loggerName)

Returns the name of the

parent

for the specified logger.
If the specified logger does not exist,

null

is returned.
If the specified logger is the root

Logger

in the namespace,
the result will be an empty string.

---

