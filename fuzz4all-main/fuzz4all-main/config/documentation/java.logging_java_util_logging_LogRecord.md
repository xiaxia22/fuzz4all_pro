# Class LogRecord

**Source:** `java.logging\java\util\logging\LogRecord.html`

### Class Description

```java
public class
LogRecord

extends
Object

implements
Serializable
```

LogRecord objects are used to pass logging requests between
the logging framework and individual log Handlers.

When a LogRecord is passed into the logging framework it
logically belongs to the framework and should no longer be
used or updated by the client application.

Note that if the client application has not specified an
explicit source method name and source class name, then the
LogRecord class will infer them automatically when they are
first accessed (due to a call on getSourceMethodName or
getSourceClassName) by analyzing the call stack. Therefore,
if a logging Handler wants to pass off a LogRecord to another
thread, or to transmit it over RMI, and if it wishes to subsequently
obtain method name or class name information it should call
one of getSourceClassName or getSourceMethodName to force
the values to be filled in.

Serialization notes:

- The LogRecord class is serializable.

Because objects in the parameters array may not be serializable,
during serialization all objects in the parameters array are
written as the corresponding Strings (using Object.toString).

The ResourceBundle is not transmitted as part of the serialized
form, but the resource bundle name is, and the recipient object's
readObject method will attempt to locate a suitable resource bundle.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public LogRecord​(
Level
level,

String
msg)

Construct a LogRecord with the given level and message values.

The sequence property will be initialized with a new unique value.
These sequence values are allocated in increasing order within a VM.

Since JDK 9, the event time is represented by an

Instant

.
The instant property will be initialized to the

current instant

, using the best available

clock

on the system.

The thread ID property will be initialized with a unique ID for
the current thread.

All other properties will be initialized to "null".

**Parameters:**
- level

- a logging level value
- msg

- the raw non-localized logging message (may be null)

**See Also:**
- Clock.systemUTC()

---

### Method Details

#### public
String
getLoggerName()

Get the source Logger's name.

**Returns:**
- source logger name (may be null)

---

#### public void setLoggerName​(
String
name)

Set the source Logger's name.

**Parameters:**
- name

- the source logger name (may be null)

---

#### public
ResourceBundle
getResourceBundle()

Get the localization resource bundle

This is the ResourceBundle that should be used to localize
the message string before formatting it. The result may
be null if the message is not localizable, or if no suitable
ResourceBundle is available.

**Returns:**
- the localization resource bundle

---

#### public void setResourceBundle​(
ResourceBundle
bundle)

Set the localization resource bundle.

**Parameters:**
- bundle

- localization bundle (may be null)

---

#### public
String
getResourceBundleName()

Get the localization resource bundle name

This is the name for the ResourceBundle that should be
used to localize the message string before formatting it.
The result may be null if the message is not localizable.

**Returns:**
- the localization resource bundle name

---

#### public void setResourceBundleName​(
String
name)

Set the localization resource bundle name.

**Parameters:**
- name

- localization bundle name (may be null)

---

#### public
Level
getLevel()

Get the logging message level, for example Level.SEVERE.

**Returns:**
- the logging message level

---

#### public void setLevel​(
Level
level)

Set the logging message level, for example Level.SEVERE.

**Parameters:**
- level

- the logging message level

---

#### public long getSequenceNumber()

Get the sequence number.

Sequence numbers are normally assigned in the LogRecord
constructor, which assigns unique sequence numbers to
each new LogRecord in increasing order.

**Returns:**
- the sequence number

---

#### public void setSequenceNumber​(long seq)

Set the sequence number.

Sequence numbers are normally assigned in the LogRecord constructor,
so it should not normally be necessary to use this method.

**Parameters:**
- seq

- the sequence number

---

#### public
String
getSourceClassName()

Get the name of the class that (allegedly) issued the logging request.

Note that this sourceClassName is not verified and may be spoofed.
This information may either have been provided as part of the
logging call, or it may have been inferred automatically by the
logging framework. In the latter case, the information may only
be approximate and may in fact describe an earlier call on the
stack frame.

May be null if no information could be obtained.

**Returns:**
- the source class name

---

#### public void setSourceClassName​(
String
sourceClassName)

Set the name of the class that (allegedly) issued the logging request.

**Parameters:**
- sourceClassName

- the source class name (may be null)

---

#### public
String
getSourceMethodName()

Get the name of the method that (allegedly) issued the logging request.

Note that this sourceMethodName is not verified and may be spoofed.
This information may either have been provided as part of the
logging call, or it may have been inferred automatically by the
logging framework. In the latter case, the information may only
be approximate and may in fact describe an earlier call on the
stack frame.

May be null if no information could be obtained.

**Returns:**
- the source method name

---

#### public void setSourceMethodName​(
String
sourceMethodName)

Set the name of the method that (allegedly) issued the logging request.

**Parameters:**
- sourceMethodName

- the source method name (may be null)

---

#### public
String
getMessage()

Get the "raw" log message, before localization or formatting.

May be null, which is equivalent to the empty string "".

This message may be either the final text or a localization key.

During formatting, if the source logger has a localization
ResourceBundle and if that ResourceBundle has an entry for
this message string, then the message string is replaced
with the localized value.

**Returns:**
- the raw message string

---

#### public void setMessage​(
String
message)

Set the "raw" log message, before localization or formatting.

**Parameters:**
- message

- the raw message string (may be null)

---

#### public
Object
[] getParameters()

Get the parameters to the log message.

**Returns:**
- the log message parameters. May be null if
there are no parameters.

---

#### public void setParameters​(
Object
[] parameters)

Set the parameters to the log message.

**Parameters:**
- parameters

- the log message parameters. (may be null)

---

#### public int getThreadID()

Get an identifier for the thread where the message originated.

This is a thread identifier within the Java VM and may or
may not map to any operating system ID.

**Returns:**
- thread ID

---

#### public void setThreadID​(int threadID)

Set an identifier for the thread where the message originated.

**Parameters:**
- threadID

- the thread ID

---

#### public long getMillis()

Get truncated event time in milliseconds since 1970.

**Returns:**
- truncated event time in millis since 1970

**See Also:**
- getInstant()

**API Note:**
- To get the full nanosecond resolution event time,
use

getInstant()

.

**Implementation Requirements:**
- This is equivalent to calling

getInstant().toEpochMilli()

.

---

#### @Deprecated

public void setMillis​(long millis)

Set event time.

**Parameters:**
- millis

- event time in millis since 1970.

**See Also:**
- setInstant(java.time.Instant)

**Implementation Requirements:**
- This is equivalent to calling

setInstant(Instant.ofEpochMilli(millis))

.

---

#### public
Instant
getInstant()

Gets the instant that the event occurred.

**Returns:**
- the instant that the event occurred.

**Since:**
- 9

---

#### public void setInstant​(
Instant
instant)

Sets the instant that the event occurred.

If the given

instant

represents a point on the time-line too
far in the future or past to fit in a

long

milliseconds and
nanoseconds adjustment, then an

ArithmeticException

will be
thrown.

**Parameters:**
- instant

- the instant that the event occurred.

**Throws:**
- NullPointerException

- if

instant

is null.
- ArithmeticException

- if numeric overflow would occur while
calling

instant.toEpochMilli()

.

**Since:**
- 9

---

#### public
Throwable
getThrown()

Get any throwable associated with the log record.

If the event involved an exception, this will be the
exception object. Otherwise null.

**Returns:**
- a throwable

---

#### public void setThrown​(
Throwable
thrown)

Set a throwable associated with the log event.

**Parameters:**
- thrown

- a throwable (may be null)

---

### Additional Sections

#### Class LogRecord

java.lang.Object

- java.util.logging.LogRecord

java.util.logging.LogRecord

**All Implemented Interfaces:** Serializable

```java
public class
LogRecord

extends
Object

implements
Serializable
```

LogRecord objects are used to pass logging requests between
the logging framework and individual log Handlers.

When a LogRecord is passed into the logging framework it
logically belongs to the framework and should no longer be
used or updated by the client application.

Note that if the client application has not specified an
explicit source method name and source class name, then the
LogRecord class will infer them automatically when they are
first accessed (due to a call on getSourceMethodName or
getSourceClassName) by analyzing the call stack. Therefore,
if a logging Handler wants to pass off a LogRecord to another
thread, or to transmit it over RMI, and if it wishes to subsequently
obtain method name or class name information it should call
one of getSourceClassName or getSourceMethodName to force
the values to be filled in.

Serialization notes:

- The LogRecord class is serializable.

Because objects in the parameters array may not be serializable,
during serialization all objects in the parameters array are
written as the corresponding Strings (using Object.toString).

The ResourceBundle is not transmitted as part of the serialized
form, but the resource bundle name is, and the recipient object's
readObject method will attempt to locate a suitable resource bundle.

**Since:** 1.4
**See Also:** Serialized Form

public class

LogRecord

extends

Object

implements

Serializable

LogRecord objects are used to pass logging requests between
the logging framework and individual log Handlers.

When a LogRecord is passed into the logging framework it
logically belongs to the framework and should no longer be
used or updated by the client application.

Note that if the client application has not specified an
explicit source method name and source class name, then the
LogRecord class will infer them automatically when they are
first accessed (due to a call on getSourceMethodName or
getSourceClassName) by analyzing the call stack. Therefore,
if a logging Handler wants to pass off a LogRecord to another
thread, or to transmit it over RMI, and if it wishes to subsequently
obtain method name or class name information it should call
one of getSourceClassName or getSourceMethodName to force
the values to be filled in.

Serialization notes:

- The LogRecord class is serializable.

Because objects in the parameters array may not be serializable,
during serialization all objects in the parameters array are
written as the corresponding Strings (using Object.toString).

The ResourceBundle is not transmitted as part of the serialized
form, but the resource bundle name is, and the recipient object's
readObject method will attempt to locate a suitable resource bundle.

When a LogRecord is passed into the logging framework it
logically belongs to the framework and should no longer be
used or updated by the client application.

Note that if the client application has not specified an
explicit source method name and source class name, then the
LogRecord class will infer them automatically when they are
first accessed (due to a call on getSourceMethodName or
getSourceClassName) by analyzing the call stack. Therefore,
if a logging Handler wants to pass off a LogRecord to another
thread, or to transmit it over RMI, and if it wishes to subsequently
obtain method name or class name information it should call
one of getSourceClassName or getSourceMethodName to force
the values to be filled in.

Serialization notes:

- The LogRecord class is serializable.

Because objects in the parameters array may not be serializable,
during serialization all objects in the parameters array are
written as the corresponding Strings (using Object.toString).

The ResourceBundle is not transmitted as part of the serialized
form, but the resource bundle name is, and the recipient object's
readObject method will attempt to locate a suitable resource bundle.

Note that if the client application has not specified an
explicit source method name and source class name, then the
LogRecord class will infer them automatically when they are
first accessed (due to a call on getSourceMethodName or
getSourceClassName) by analyzing the call stack. Therefore,
if a logging Handler wants to pass off a LogRecord to another
thread, or to transmit it over RMI, and if it wishes to subsequently
obtain method name or class name information it should call
one of getSourceClassName or getSourceMethodName to force
the values to be filled in.

Serialization notes:

- The LogRecord class is serializable.

Because objects in the parameters array may not be serializable,
during serialization all objects in the parameters array are
written as the corresponding Strings (using Object.toString).

The ResourceBundle is not transmitted as part of the serialized
form, but the resource bundle name is, and the recipient object's
readObject method will attempt to locate a suitable resource bundle.

Serialization notes:

- The LogRecord class is serializable.

Because objects in the parameters array may not be serializable,
during serialization all objects in the parameters array are
written as the corresponding Strings (using Object.toString).

The ResourceBundle is not transmitted as part of the serialized
form, but the resource bundle name is, and the recipient object's
readObject method will attempt to locate a suitable resource bundle.

The LogRecord class is serializable.

Because objects in the parameters array may not be serializable,
during serialization all objects in the parameters array are
written as the corresponding Strings (using Object.toString).

The ResourceBundle is not transmitted as part of the serialized
form, but the resource bundle name is, and the recipient object's
readObject method will attempt to locate a suitable resource bundle.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

LogRecord

​(

Level

level,

String

msg)

Construct a LogRecord with the given level and message values.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Deprecated Methods

Modifier and Type

Method

Description

Instant

getInstant

()

Gets the instant that the event occurred.

Level

getLevel

()

Get the logging message level, for example Level.SEVERE.

String

getLoggerName

()

Get the source Logger's name.

String

getMessage

()

Get the "raw" log message, before localization or formatting.

long

getMillis

()

Get truncated event time in milliseconds since 1970.

Object

[]

getParameters

()

Get the parameters to the log message.

ResourceBundle

getResourceBundle

()

Get the localization resource bundle

String

getResourceBundleName

()

Get the localization resource bundle name

long

getSequenceNumber

()

Get the sequence number.

String

getSourceClassName

()

Get the name of the class that (allegedly) issued the logging request.

String

getSourceMethodName

()

Get the name of the method that (allegedly) issued the logging request.

int

getThreadID

()

Get an identifier for the thread where the message originated.

Throwable

getThrown

()

Get any throwable associated with the log record.

void

setInstant

​(

Instant

instant)

Sets the instant that the event occurred.

void

setLevel

​(

Level

level)

Set the logging message level, for example Level.SEVERE.

void

setLoggerName

​(

String

name)

Set the source Logger's name.

void

setMessage

​(

String

message)

Set the "raw" log message, before localization or formatting.

void

setMillis

​(long millis)

Deprecated.

LogRecord maintains timestamps with nanosecond resolution,
using

Instant

values.

void

setParameters

​(

Object

[] parameters)

Set the parameters to the log message.

void

setResourceBundle

​(

ResourceBundle

bundle)

Set the localization resource bundle.

void

setResourceBundleName

​(

String

name)

Set the localization resource bundle name.

void

setSequenceNumber

​(long seq)

Set the sequence number.

void

setSourceClassName

​(

String

sourceClassName)

Set the name of the class that (allegedly) issued the logging request.

void

setSourceMethodName

​(

String

sourceMethodName)

Set the name of the method that (allegedly) issued the logging request.

void

setThreadID

​(int threadID)

Set an identifier for the thread where the message originated.

void

setThrown

​(

Throwable

thrown)

Set a throwable associated with the log event.

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

Constructor Summary

Constructors

Constructor

Description

LogRecord

​(

Level

level,

String

msg)

Construct a LogRecord with the given level and message values.

---

#### Constructor Summary

Construct a LogRecord with the given level and message values.

Method Summary

All Methods

Instance Methods

Concrete Methods

Deprecated Methods

Modifier and Type

Method

Description

Instant

getInstant

()

Gets the instant that the event occurred.

Level

getLevel

()

Get the logging message level, for example Level.SEVERE.

String

getLoggerName

()

Get the source Logger's name.

String

getMessage

()

Get the "raw" log message, before localization or formatting.

long

getMillis

()

Get truncated event time in milliseconds since 1970.

Object

[]

getParameters

()

Get the parameters to the log message.

ResourceBundle

getResourceBundle

()

Get the localization resource bundle

String

getResourceBundleName

()

Get the localization resource bundle name

long

getSequenceNumber

()

Get the sequence number.

String

getSourceClassName

()

Get the name of the class that (allegedly) issued the logging request.

String

getSourceMethodName

()

Get the name of the method that (allegedly) issued the logging request.

int

getThreadID

()

Get an identifier for the thread where the message originated.

Throwable

getThrown

()

Get any throwable associated with the log record.

void

setInstant

​(

Instant

instant)

Sets the instant that the event occurred.

void

setLevel

​(

Level

level)

Set the logging message level, for example Level.SEVERE.

void

setLoggerName

​(

String

name)

Set the source Logger's name.

void

setMessage

​(

String

message)

Set the "raw" log message, before localization or formatting.

void

setMillis

​(long millis)

Deprecated.

LogRecord maintains timestamps with nanosecond resolution,
using

Instant

values.

void

setParameters

​(

Object

[] parameters)

Set the parameters to the log message.

void

setResourceBundle

​(

ResourceBundle

bundle)

Set the localization resource bundle.

void

setResourceBundleName

​(

String

name)

Set the localization resource bundle name.

void

setSequenceNumber

​(long seq)

Set the sequence number.

void

setSourceClassName

​(

String

sourceClassName)

Set the name of the class that (allegedly) issued the logging request.

void

setSourceMethodName

​(

String

sourceMethodName)

Set the name of the method that (allegedly) issued the logging request.

void

setThreadID

​(int threadID)

Set an identifier for the thread where the message originated.

void

setThrown

​(

Throwable

thrown)

Set a throwable associated with the log event.

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

Gets the instant that the event occurred.

Get the logging message level, for example Level.SEVERE.

Get the source Logger's name.

Get the "raw" log message, before localization or formatting.

Get truncated event time in milliseconds since 1970.

Get the parameters to the log message.

Get the localization resource bundle

Get the localization resource bundle name

Get the sequence number.

Get the name of the class that (allegedly) issued the logging request.

Get the name of the method that (allegedly) issued the logging request.

Get an identifier for the thread where the message originated.

Get any throwable associated with the log record.

Sets the instant that the event occurred.

Set the logging message level, for example Level.SEVERE.

Set the source Logger's name.

Set the "raw" log message, before localization or formatting.

Deprecated.

LogRecord maintains timestamps with nanosecond resolution,
using

Instant

values.

Set the parameters to the log message.

Set the localization resource bundle.

Set the localization resource bundle name.

Set the sequence number.

Set the name of the class that (allegedly) issued the logging request.

Set the name of the method that (allegedly) issued the logging request.

Set an identifier for the thread where the message originated.

Set a throwable associated with the log event.

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

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- LogRecord

```java
public LogRecord​(
Level
level,

String
msg)
```

Construct a LogRecord with the given level and message values.

The sequence property will be initialized with a new unique value.
These sequence values are allocated in increasing order within a VM.

Since JDK 9, the event time is represented by an

Instant

.
The instant property will be initialized to the

current instant

, using the best available

clock

on the system.

The thread ID property will be initialized with a unique ID for
the current thread.

All other properties will be initialized to "null".

**Parameters:** level

- a logging level value
**Parameters:** msg

- the raw non-localized logging message (may be null)
**See Also:** Clock.systemUTC()

============ METHOD DETAIL ==========

- Method Detail

- getLoggerName

```java
public
String
getLoggerName()
```

Get the source Logger's name.

**Returns:** source logger name (may be null)

- setLoggerName

```java
public void setLoggerName​(
String
name)
```

Set the source Logger's name.

**Parameters:** name

- the source logger name (may be null)

- getResourceBundle

```java
public
ResourceBundle
getResourceBundle()
```

Get the localization resource bundle

This is the ResourceBundle that should be used to localize
the message string before formatting it. The result may
be null if the message is not localizable, or if no suitable
ResourceBundle is available.

**Returns:** the localization resource bundle

- setResourceBundle

```java
public void setResourceBundle​(
ResourceBundle
bundle)
```

Set the localization resource bundle.

**Parameters:** bundle

- localization bundle (may be null)

- getResourceBundleName

```java
public
String
getResourceBundleName()
```

Get the localization resource bundle name

This is the name for the ResourceBundle that should be
used to localize the message string before formatting it.
The result may be null if the message is not localizable.

**Returns:** the localization resource bundle name

- setResourceBundleName

```java
public void setResourceBundleName​(
String
name)
```

Set the localization resource bundle name.

**Parameters:** name

- localization bundle name (may be null)

- getLevel

```java
public
Level
getLevel()
```

Get the logging message level, for example Level.SEVERE.

**Returns:** the logging message level

- setLevel

```java
public void setLevel​(
Level
level)
```

Set the logging message level, for example Level.SEVERE.

**Parameters:** level

- the logging message level

- getSequenceNumber

```java
public long getSequenceNumber()
```

Get the sequence number.

Sequence numbers are normally assigned in the LogRecord
constructor, which assigns unique sequence numbers to
each new LogRecord in increasing order.

**Returns:** the sequence number

- setSequenceNumber

```java
public void setSequenceNumber​(long seq)
```

Set the sequence number.

Sequence numbers are normally assigned in the LogRecord constructor,
so it should not normally be necessary to use this method.

**Parameters:** seq

- the sequence number

- getSourceClassName

```java
public
String
getSourceClassName()
```

Get the name of the class that (allegedly) issued the logging request.

Note that this sourceClassName is not verified and may be spoofed.
This information may either have been provided as part of the
logging call, or it may have been inferred automatically by the
logging framework. In the latter case, the information may only
be approximate and may in fact describe an earlier call on the
stack frame.

May be null if no information could be obtained.

**Returns:** the source class name

- setSourceClassName

```java
public void setSourceClassName​(
String
sourceClassName)
```

Set the name of the class that (allegedly) issued the logging request.

**Parameters:** sourceClassName

- the source class name (may be null)

- getSourceMethodName

```java
public
String
getSourceMethodName()
```

Get the name of the method that (allegedly) issued the logging request.

Note that this sourceMethodName is not verified and may be spoofed.
This information may either have been provided as part of the
logging call, or it may have been inferred automatically by the
logging framework. In the latter case, the information may only
be approximate and may in fact describe an earlier call on the
stack frame.

May be null if no information could be obtained.

**Returns:** the source method name

- setSourceMethodName

```java
public void setSourceMethodName​(
String
sourceMethodName)
```

Set the name of the method that (allegedly) issued the logging request.

**Parameters:** sourceMethodName

- the source method name (may be null)

- getMessage

```java
public
String
getMessage()
```

Get the "raw" log message, before localization or formatting.

May be null, which is equivalent to the empty string "".

This message may be either the final text or a localization key.

During formatting, if the source logger has a localization
ResourceBundle and if that ResourceBundle has an entry for
this message string, then the message string is replaced
with the localized value.

**Returns:** the raw message string

- setMessage

```java
public void setMessage​(
String
message)
```

Set the "raw" log message, before localization or formatting.

**Parameters:** message

- the raw message string (may be null)

- getParameters

```java
public
Object
[] getParameters()
```

Get the parameters to the log message.

**Returns:** the log message parameters. May be null if
there are no parameters.

- setParameters

```java
public void setParameters​(
Object
[] parameters)
```

Set the parameters to the log message.

**Parameters:** parameters

- the log message parameters. (may be null)

- getThreadID

```java
public int getThreadID()
```

Get an identifier for the thread where the message originated.

This is a thread identifier within the Java VM and may or
may not map to any operating system ID.

**Returns:** thread ID

- setThreadID

```java
public void setThreadID​(int threadID)
```

Set an identifier for the thread where the message originated.

**Parameters:** threadID

- the thread ID

- getMillis

```java
public long getMillis()
```

Get truncated event time in milliseconds since 1970.

**API Note:** To get the full nanosecond resolution event time,
use

getInstant()

.
**Implementation Requirements:** This is equivalent to calling

getInstant().toEpochMilli()

.
**Returns:** truncated event time in millis since 1970
**See Also:** getInstant()

- setMillis

```java
@Deprecated

public void setMillis​(long millis)
```

Deprecated.

LogRecord maintains timestamps with nanosecond resolution,
using

Instant

values. For this reason,

setInstant()

should be used in preference to

setMillis()

.

Set event time.

**Implementation Requirements:** This is equivalent to calling

setInstant(Instant.ofEpochMilli(millis))

.
**Parameters:** millis

- event time in millis since 1970.
**See Also:** setInstant(java.time.Instant)

- getInstant

```java
public
Instant
getInstant()
```

Gets the instant that the event occurred.

**Returns:** the instant that the event occurred.
**Since:** 9

- setInstant

```java
public void setInstant​(
Instant
instant)
```

Sets the instant that the event occurred.

If the given

instant

represents a point on the time-line too
far in the future or past to fit in a

long

milliseconds and
nanoseconds adjustment, then an

ArithmeticException

will be
thrown.

**Parameters:** instant

- the instant that the event occurred.
**Throws:** NullPointerException

- if

instant

is null.
**Throws:** ArithmeticException

- if numeric overflow would occur while
calling

instant.toEpochMilli()

.
**Since:** 9

- getThrown

```java
public
Throwable
getThrown()
```

Get any throwable associated with the log record.

If the event involved an exception, this will be the
exception object. Otherwise null.

**Returns:** a throwable

- setThrown

```java
public void setThrown​(
Throwable
thrown)
```

Set a throwable associated with the log event.

**Parameters:** thrown

- a throwable (may be null)

Constructor Detail

- LogRecord

```java
public LogRecord​(
Level
level,

String
msg)
```

Construct a LogRecord with the given level and message values.

The sequence property will be initialized with a new unique value.
These sequence values are allocated in increasing order within a VM.

Since JDK 9, the event time is represented by an

Instant

.
The instant property will be initialized to the

current instant

, using the best available

clock

on the system.

The thread ID property will be initialized with a unique ID for
the current thread.

All other properties will be initialized to "null".

**Parameters:** level

- a logging level value
**Parameters:** msg

- the raw non-localized logging message (may be null)
**See Also:** Clock.systemUTC()

---

#### Constructor Detail

LogRecord

```java
public LogRecord​(
Level
level,

String
msg)
```

Construct a LogRecord with the given level and message values.

The sequence property will be initialized with a new unique value.
These sequence values are allocated in increasing order within a VM.

Since JDK 9, the event time is represented by an

Instant

.
The instant property will be initialized to the

current instant

, using the best available

clock

on the system.

The thread ID property will be initialized with a unique ID for
the current thread.

All other properties will be initialized to "null".

**Parameters:** level

- a logging level value
**Parameters:** msg

- the raw non-localized logging message (may be null)
**See Also:** Clock.systemUTC()

---

#### LogRecord

public LogRecord​(

Level

level,

String

msg)

Construct a LogRecord with the given level and message values.

The sequence property will be initialized with a new unique value.
These sequence values are allocated in increasing order within a VM.

Since JDK 9, the event time is represented by an

Instant

.
The instant property will be initialized to the

current instant

, using the best available

clock

on the system.

The thread ID property will be initialized with a unique ID for
the current thread.

All other properties will be initialized to "null".

The sequence property will be initialized with a new unique value.
These sequence values are allocated in increasing order within a VM.

Since JDK 9, the event time is represented by an

Instant

.
The instant property will be initialized to the

current instant

, using the best available

clock

on the system.

The thread ID property will be initialized with a unique ID for
the current thread.

All other properties will be initialized to "null".

Since JDK 9, the event time is represented by an

Instant

.
The instant property will be initialized to the

current instant

, using the best available

clock

on the system.

The thread ID property will be initialized with a unique ID for
the current thread.

All other properties will be initialized to "null".

The thread ID property will be initialized with a unique ID for
the current thread.

All other properties will be initialized to "null".

All other properties will be initialized to "null".

Method Detail

- getLoggerName

```java
public
String
getLoggerName()
```

Get the source Logger's name.

**Returns:** source logger name (may be null)

- setLoggerName

```java
public void setLoggerName​(
String
name)
```

Set the source Logger's name.

**Parameters:** name

- the source logger name (may be null)

- getResourceBundle

```java
public
ResourceBundle
getResourceBundle()
```

Get the localization resource bundle

This is the ResourceBundle that should be used to localize
the message string before formatting it. The result may
be null if the message is not localizable, or if no suitable
ResourceBundle is available.

**Returns:** the localization resource bundle

- setResourceBundle

```java
public void setResourceBundle​(
ResourceBundle
bundle)
```

Set the localization resource bundle.

**Parameters:** bundle

- localization bundle (may be null)

- getResourceBundleName

```java
public
String
getResourceBundleName()
```

Get the localization resource bundle name

This is the name for the ResourceBundle that should be
used to localize the message string before formatting it.
The result may be null if the message is not localizable.

**Returns:** the localization resource bundle name

- setResourceBundleName

```java
public void setResourceBundleName​(
String
name)
```

Set the localization resource bundle name.

**Parameters:** name

- localization bundle name (may be null)

- getLevel

```java
public
Level
getLevel()
```

Get the logging message level, for example Level.SEVERE.

**Returns:** the logging message level

- setLevel

```java
public void setLevel​(
Level
level)
```

Set the logging message level, for example Level.SEVERE.

**Parameters:** level

- the logging message level

- getSequenceNumber

```java
public long getSequenceNumber()
```

Get the sequence number.

Sequence numbers are normally assigned in the LogRecord
constructor, which assigns unique sequence numbers to
each new LogRecord in increasing order.

**Returns:** the sequence number

- setSequenceNumber

```java
public void setSequenceNumber​(long seq)
```

Set the sequence number.

Sequence numbers are normally assigned in the LogRecord constructor,
so it should not normally be necessary to use this method.

**Parameters:** seq

- the sequence number

- getSourceClassName

```java
public
String
getSourceClassName()
```

Get the name of the class that (allegedly) issued the logging request.

Note that this sourceClassName is not verified and may be spoofed.
This information may either have been provided as part of the
logging call, or it may have been inferred automatically by the
logging framework. In the latter case, the information may only
be approximate and may in fact describe an earlier call on the
stack frame.

May be null if no information could be obtained.

**Returns:** the source class name

- setSourceClassName

```java
public void setSourceClassName​(
String
sourceClassName)
```

Set the name of the class that (allegedly) issued the logging request.

**Parameters:** sourceClassName

- the source class name (may be null)

- getSourceMethodName

```java
public
String
getSourceMethodName()
```

Get the name of the method that (allegedly) issued the logging request.

Note that this sourceMethodName is not verified and may be spoofed.
This information may either have been provided as part of the
logging call, or it may have been inferred automatically by the
logging framework. In the latter case, the information may only
be approximate and may in fact describe an earlier call on the
stack frame.

May be null if no information could be obtained.

**Returns:** the source method name

- setSourceMethodName

```java
public void setSourceMethodName​(
String
sourceMethodName)
```

Set the name of the method that (allegedly) issued the logging request.

**Parameters:** sourceMethodName

- the source method name (may be null)

- getMessage

```java
public
String
getMessage()
```

Get the "raw" log message, before localization or formatting.

May be null, which is equivalent to the empty string "".

This message may be either the final text or a localization key.

During formatting, if the source logger has a localization
ResourceBundle and if that ResourceBundle has an entry for
this message string, then the message string is replaced
with the localized value.

**Returns:** the raw message string

- setMessage

```java
public void setMessage​(
String
message)
```

Set the "raw" log message, before localization or formatting.

**Parameters:** message

- the raw message string (may be null)

- getParameters

```java
public
Object
[] getParameters()
```

Get the parameters to the log message.

**Returns:** the log message parameters. May be null if
there are no parameters.

- setParameters

```java
public void setParameters​(
Object
[] parameters)
```

Set the parameters to the log message.

**Parameters:** parameters

- the log message parameters. (may be null)

- getThreadID

```java
public int getThreadID()
```

Get an identifier for the thread where the message originated.

This is a thread identifier within the Java VM and may or
may not map to any operating system ID.

**Returns:** thread ID

- setThreadID

```java
public void setThreadID​(int threadID)
```

Set an identifier for the thread where the message originated.

**Parameters:** threadID

- the thread ID

- getMillis

```java
public long getMillis()
```

Get truncated event time in milliseconds since 1970.

**API Note:** To get the full nanosecond resolution event time,
use

getInstant()

.
**Implementation Requirements:** This is equivalent to calling

getInstant().toEpochMilli()

.
**Returns:** truncated event time in millis since 1970
**See Also:** getInstant()

- setMillis

```java
@Deprecated

public void setMillis​(long millis)
```

Deprecated.

LogRecord maintains timestamps with nanosecond resolution,
using

Instant

values. For this reason,

setInstant()

should be used in preference to

setMillis()

.

Set event time.

**Implementation Requirements:** This is equivalent to calling

setInstant(Instant.ofEpochMilli(millis))

.
**Parameters:** millis

- event time in millis since 1970.
**See Also:** setInstant(java.time.Instant)

- getInstant

```java
public
Instant
getInstant()
```

Gets the instant that the event occurred.

**Returns:** the instant that the event occurred.
**Since:** 9

- setInstant

```java
public void setInstant​(
Instant
instant)
```

Sets the instant that the event occurred.

If the given

instant

represents a point on the time-line too
far in the future or past to fit in a

long

milliseconds and
nanoseconds adjustment, then an

ArithmeticException

will be
thrown.

**Parameters:** instant

- the instant that the event occurred.
**Throws:** NullPointerException

- if

instant

is null.
**Throws:** ArithmeticException

- if numeric overflow would occur while
calling

instant.toEpochMilli()

.
**Since:** 9

- getThrown

```java
public
Throwable
getThrown()
```

Get any throwable associated with the log record.

If the event involved an exception, this will be the
exception object. Otherwise null.

**Returns:** a throwable

- setThrown

```java
public void setThrown​(
Throwable
thrown)
```

Set a throwable associated with the log event.

**Parameters:** thrown

- a throwable (may be null)

---

#### Method Detail

getLoggerName

```java
public
String
getLoggerName()
```

Get the source Logger's name.

**Returns:** source logger name (may be null)

---

#### getLoggerName

public

String

getLoggerName()

Get the source Logger's name.

setLoggerName

```java
public void setLoggerName​(
String
name)
```

Set the source Logger's name.

**Parameters:** name

- the source logger name (may be null)

---

#### setLoggerName

public void setLoggerName​(

String

name)

Set the source Logger's name.

getResourceBundle

```java
public
ResourceBundle
getResourceBundle()
```

Get the localization resource bundle

This is the ResourceBundle that should be used to localize
the message string before formatting it. The result may
be null if the message is not localizable, or if no suitable
ResourceBundle is available.

**Returns:** the localization resource bundle

---

#### getResourceBundle

public

ResourceBundle

getResourceBundle()

Get the localization resource bundle

This is the ResourceBundle that should be used to localize
the message string before formatting it. The result may
be null if the message is not localizable, or if no suitable
ResourceBundle is available.

This is the ResourceBundle that should be used to localize
the message string before formatting it. The result may
be null if the message is not localizable, or if no suitable
ResourceBundle is available.

setResourceBundle

```java
public void setResourceBundle​(
ResourceBundle
bundle)
```

Set the localization resource bundle.

**Parameters:** bundle

- localization bundle (may be null)

---

#### setResourceBundle

public void setResourceBundle​(

ResourceBundle

bundle)

Set the localization resource bundle.

getResourceBundleName

```java
public
String
getResourceBundleName()
```

Get the localization resource bundle name

This is the name for the ResourceBundle that should be
used to localize the message string before formatting it.
The result may be null if the message is not localizable.

**Returns:** the localization resource bundle name

---

#### getResourceBundleName

public

String

getResourceBundleName()

Get the localization resource bundle name

This is the name for the ResourceBundle that should be
used to localize the message string before formatting it.
The result may be null if the message is not localizable.

This is the name for the ResourceBundle that should be
used to localize the message string before formatting it.
The result may be null if the message is not localizable.

setResourceBundleName

```java
public void setResourceBundleName​(
String
name)
```

Set the localization resource bundle name.

**Parameters:** name

- localization bundle name (may be null)

---

#### setResourceBundleName

public void setResourceBundleName​(

String

name)

Set the localization resource bundle name.

getLevel

```java
public
Level
getLevel()
```

Get the logging message level, for example Level.SEVERE.

**Returns:** the logging message level

---

#### getLevel

public

Level

getLevel()

Get the logging message level, for example Level.SEVERE.

setLevel

```java
public void setLevel​(
Level
level)
```

Set the logging message level, for example Level.SEVERE.

**Parameters:** level

- the logging message level

---

#### setLevel

public void setLevel​(

Level

level)

Set the logging message level, for example Level.SEVERE.

getSequenceNumber

```java
public long getSequenceNumber()
```

Get the sequence number.

Sequence numbers are normally assigned in the LogRecord
constructor, which assigns unique sequence numbers to
each new LogRecord in increasing order.

**Returns:** the sequence number

---

#### getSequenceNumber

public long getSequenceNumber()

Get the sequence number.

Sequence numbers are normally assigned in the LogRecord
constructor, which assigns unique sequence numbers to
each new LogRecord in increasing order.

Sequence numbers are normally assigned in the LogRecord
constructor, which assigns unique sequence numbers to
each new LogRecord in increasing order.

setSequenceNumber

```java
public void setSequenceNumber​(long seq)
```

Set the sequence number.

Sequence numbers are normally assigned in the LogRecord constructor,
so it should not normally be necessary to use this method.

**Parameters:** seq

- the sequence number

---

#### setSequenceNumber

public void setSequenceNumber​(long seq)

Set the sequence number.

Sequence numbers are normally assigned in the LogRecord constructor,
so it should not normally be necessary to use this method.

Sequence numbers are normally assigned in the LogRecord constructor,
so it should not normally be necessary to use this method.

getSourceClassName

```java
public
String
getSourceClassName()
```

Get the name of the class that (allegedly) issued the logging request.

Note that this sourceClassName is not verified and may be spoofed.
This information may either have been provided as part of the
logging call, or it may have been inferred automatically by the
logging framework. In the latter case, the information may only
be approximate and may in fact describe an earlier call on the
stack frame.

May be null if no information could be obtained.

**Returns:** the source class name

---

#### getSourceClassName

public

String

getSourceClassName()

Get the name of the class that (allegedly) issued the logging request.

Note that this sourceClassName is not verified and may be spoofed.
This information may either have been provided as part of the
logging call, or it may have been inferred automatically by the
logging framework. In the latter case, the information may only
be approximate and may in fact describe an earlier call on the
stack frame.

May be null if no information could be obtained.

Note that this sourceClassName is not verified and may be spoofed.
This information may either have been provided as part of the
logging call, or it may have been inferred automatically by the
logging framework. In the latter case, the information may only
be approximate and may in fact describe an earlier call on the
stack frame.

May be null if no information could be obtained.

May be null if no information could be obtained.

setSourceClassName

```java
public void setSourceClassName​(
String
sourceClassName)
```

Set the name of the class that (allegedly) issued the logging request.

**Parameters:** sourceClassName

- the source class name (may be null)

---

#### setSourceClassName

public void setSourceClassName​(

String

sourceClassName)

Set the name of the class that (allegedly) issued the logging request.

getSourceMethodName

```java
public
String
getSourceMethodName()
```

Get the name of the method that (allegedly) issued the logging request.

Note that this sourceMethodName is not verified and may be spoofed.
This information may either have been provided as part of the
logging call, or it may have been inferred automatically by the
logging framework. In the latter case, the information may only
be approximate and may in fact describe an earlier call on the
stack frame.

May be null if no information could be obtained.

**Returns:** the source method name

---

#### getSourceMethodName

public

String

getSourceMethodName()

Get the name of the method that (allegedly) issued the logging request.

Note that this sourceMethodName is not verified and may be spoofed.
This information may either have been provided as part of the
logging call, or it may have been inferred automatically by the
logging framework. In the latter case, the information may only
be approximate and may in fact describe an earlier call on the
stack frame.

May be null if no information could be obtained.

Note that this sourceMethodName is not verified and may be spoofed.
This information may either have been provided as part of the
logging call, or it may have been inferred automatically by the
logging framework. In the latter case, the information may only
be approximate and may in fact describe an earlier call on the
stack frame.

May be null if no information could be obtained.

May be null if no information could be obtained.

setSourceMethodName

```java
public void setSourceMethodName​(
String
sourceMethodName)
```

Set the name of the method that (allegedly) issued the logging request.

**Parameters:** sourceMethodName

- the source method name (may be null)

---

#### setSourceMethodName

public void setSourceMethodName​(

String

sourceMethodName)

Set the name of the method that (allegedly) issued the logging request.

getMessage

```java
public
String
getMessage()
```

Get the "raw" log message, before localization or formatting.

May be null, which is equivalent to the empty string "".

This message may be either the final text or a localization key.

During formatting, if the source logger has a localization
ResourceBundle and if that ResourceBundle has an entry for
this message string, then the message string is replaced
with the localized value.

**Returns:** the raw message string

---

#### getMessage

public

String

getMessage()

Get the "raw" log message, before localization or formatting.

May be null, which is equivalent to the empty string "".

This message may be either the final text or a localization key.

During formatting, if the source logger has a localization
ResourceBundle and if that ResourceBundle has an entry for
this message string, then the message string is replaced
with the localized value.

May be null, which is equivalent to the empty string "".

This message may be either the final text or a localization key.

During formatting, if the source logger has a localization
ResourceBundle and if that ResourceBundle has an entry for
this message string, then the message string is replaced
with the localized value.

This message may be either the final text or a localization key.

During formatting, if the source logger has a localization
ResourceBundle and if that ResourceBundle has an entry for
this message string, then the message string is replaced
with the localized value.

During formatting, if the source logger has a localization
ResourceBundle and if that ResourceBundle has an entry for
this message string, then the message string is replaced
with the localized value.

setMessage

```java
public void setMessage​(
String
message)
```

Set the "raw" log message, before localization or formatting.

**Parameters:** message

- the raw message string (may be null)

---

#### setMessage

public void setMessage​(

String

message)

Set the "raw" log message, before localization or formatting.

getParameters

```java
public
Object
[] getParameters()
```

Get the parameters to the log message.

**Returns:** the log message parameters. May be null if
there are no parameters.

---

#### getParameters

public

Object

[] getParameters()

Get the parameters to the log message.

setParameters

```java
public void setParameters​(
Object
[] parameters)
```

Set the parameters to the log message.

**Parameters:** parameters

- the log message parameters. (may be null)

---

#### setParameters

public void setParameters​(

Object

[] parameters)

Set the parameters to the log message.

getThreadID

```java
public int getThreadID()
```

Get an identifier for the thread where the message originated.

This is a thread identifier within the Java VM and may or
may not map to any operating system ID.

**Returns:** thread ID

---

#### getThreadID

public int getThreadID()

Get an identifier for the thread where the message originated.

This is a thread identifier within the Java VM and may or
may not map to any operating system ID.

This is a thread identifier within the Java VM and may or
may not map to any operating system ID.

setThreadID

```java
public void setThreadID​(int threadID)
```

Set an identifier for the thread where the message originated.

**Parameters:** threadID

- the thread ID

---

#### setThreadID

public void setThreadID​(int threadID)

Set an identifier for the thread where the message originated.

getMillis

```java
public long getMillis()
```

Get truncated event time in milliseconds since 1970.

**API Note:** To get the full nanosecond resolution event time,
use

getInstant()

.
**Implementation Requirements:** This is equivalent to calling

getInstant().toEpochMilli()

.
**Returns:** truncated event time in millis since 1970
**See Also:** getInstant()

---

#### getMillis

public long getMillis()

Get truncated event time in milliseconds since 1970.

setMillis

```java
@Deprecated

public void setMillis​(long millis)
```

Deprecated.

LogRecord maintains timestamps with nanosecond resolution,
using

Instant

values. For this reason,

setInstant()

should be used in preference to

setMillis()

.

Set event time.

**Implementation Requirements:** This is equivalent to calling

setInstant(Instant.ofEpochMilli(millis))

.
**Parameters:** millis

- event time in millis since 1970.
**See Also:** setInstant(java.time.Instant)

---

#### setMillis

@Deprecated

public void setMillis​(long millis)

Set event time.

getInstant

```java
public
Instant
getInstant()
```

Gets the instant that the event occurred.

**Returns:** the instant that the event occurred.
**Since:** 9

---

#### getInstant

public

Instant

getInstant()

Gets the instant that the event occurred.

setInstant

```java
public void setInstant​(
Instant
instant)
```

Sets the instant that the event occurred.

If the given

instant

represents a point on the time-line too
far in the future or past to fit in a

long

milliseconds and
nanoseconds adjustment, then an

ArithmeticException

will be
thrown.

**Parameters:** instant

- the instant that the event occurred.
**Throws:** NullPointerException

- if

instant

is null.
**Throws:** ArithmeticException

- if numeric overflow would occur while
calling

instant.toEpochMilli()

.
**Since:** 9

---

#### setInstant

public void setInstant​(

Instant

instant)

Sets the instant that the event occurred.

If the given

instant

represents a point on the time-line too
far in the future or past to fit in a

long

milliseconds and
nanoseconds adjustment, then an

ArithmeticException

will be
thrown.

If the given

instant

represents a point on the time-line too
far in the future or past to fit in a

long

milliseconds and
nanoseconds adjustment, then an

ArithmeticException

will be
thrown.

getThrown

```java
public
Throwable
getThrown()
```

Get any throwable associated with the log record.

If the event involved an exception, this will be the
exception object. Otherwise null.

**Returns:** a throwable

---

#### getThrown

public

Throwable

getThrown()

Get any throwable associated with the log record.

If the event involved an exception, this will be the
exception object. Otherwise null.

If the event involved an exception, this will be the
exception object. Otherwise null.

setThrown

```java
public void setThrown​(
Throwable
thrown)
```

Set a throwable associated with the log event.

**Parameters:** thrown

- a throwable (may be null)

---

#### setThrown

public void setThrown​(

Throwable

thrown)

Set a throwable associated with the log event.

---

