# Class Handler

**Source:** `java.logging\java\util\logging\Handler.html`

### Class Description

```java
public abstract class
Handler

extends
Object
```

A

Handler

object takes log messages from a

Logger

and
exports them. It might for example, write them to a console
or write them to a file, or send them to a network logging service,
or forward them to an OS log, or whatever.

A

Handler

can be disabled by doing a

setLevel(Level.OFF)

and can be re-enabled by doing a

setLevel

with an appropriate level.

Handler

classes typically use

LogManager

properties to set
default values for the

Handler

's

Filter

,

Formatter

,
and

Level

. See the specific documentation for each concrete

Handler

class.

**Direct Known Subclasses:** MemoryHandler

,

StreamHandler

---

### Field Details

*No entries found.*

### Constructor Details

#### protected Handler()

Default constructor. The resulting

Handler

has a log
level of

Level.ALL

, no

Formatter

, and no

Filter

. A default

ErrorManager

instance is installed
as the

ErrorManager

.

---

### Method Details

#### public abstract void publish​(
LogRecord
record)

Publish a

LogRecord

.

The logging request was made initially to a

Logger

object,
which initialized the

LogRecord

and forwarded it here.

The

Handler

is responsible for formatting the message, when and
if necessary. The formatting should include localization.

**Parameters:**
- record

- description of the log event. A null record is
silently ignored and is not published

---

#### public abstract void flush()

Flush any buffered output.

---

#### public abstract void close()
throws
SecurityException

Close the

Handler

and free all associated resources.

The close method will perform a

flush

and then close the

Handler

. After close has been called this

Handler

should no longer be used. Method calls may either be silently
ignored or may throw runtime exceptions.

**Throws:**
- SecurityException

- if a security manager exists and if
the caller does not have

LoggingPermission("control")

.

---

#### public void setFormatter​(
Formatter
newFormatter)
throws
SecurityException

Set a

Formatter

. This

Formatter

will be used
to format

LogRecords

for this

Handler

.

Some

Handlers

may not use

Formatters

, in
which case the

Formatter

will be remembered, but not used.

**Parameters:**
- newFormatter

- the

Formatter

to use (may not be null)

**Throws:**
- SecurityException

- if a security manager exists and if
the caller does not have

LoggingPermission("control")

.

---

#### public
Formatter
getFormatter()

Return the

Formatter

for this

Handler

.

**Returns:**
- the

Formatter

(may be null).

---

#### public void setEncoding​(
String
encoding)
throws
SecurityException
,

UnsupportedEncodingException

Set the character encoding used by this

Handler

.

The encoding should be set before any

LogRecords

are written
to the

Handler

.

**Parameters:**
- encoding

- The name of a supported character encoding.
May be null, to indicate the default platform encoding.

**Throws:**
- SecurityException

- if a security manager exists and if
the caller does not have

LoggingPermission("control")

.
- UnsupportedEncodingException

- if the named encoding is
not supported.

---

#### public
String
getEncoding()

Return the character encoding for this

Handler

.

**Returns:**
- The encoding name. May be null, which indicates the
default encoding should be used.

---

#### public void setFilter​(
Filter
newFilter)
throws
SecurityException

Set a

Filter

to control output on this

Handler

.

For each call of

publish

the

Handler

will call
this

Filter

(if it is non-null) to check if the

LogRecord

should be published or discarded.

**Parameters:**
- newFilter

- a

Filter

object (may be null)

**Throws:**
- SecurityException

- if a security manager exists and if
the caller does not have

LoggingPermission("control")

.

---

#### public
Filter
getFilter()

Get the current

Filter

for this

Handler

.

**Returns:**
- a

Filter

object (may be null)

---

#### public void setErrorManager​(
ErrorManager
em)

Define an ErrorManager for this Handler.

The ErrorManager's "error" method will be invoked if any
errors occur while using this Handler.

**Parameters:**
- em

- the new ErrorManager

**Throws:**
- SecurityException

- if a security manager exists and if
the caller does not have

LoggingPermission("control")

.

---

#### public
ErrorManager
getErrorManager()

Retrieves the ErrorManager for this Handler.

**Returns:**
- the ErrorManager for this Handler

**Throws:**
- SecurityException

- if a security manager exists and if
the caller does not have

LoggingPermission("control")

.

---

#### protected void reportError​(
String
msg,

Exception
ex,
int code)

Protected convenience method to report an error to this Handler's
ErrorManager. Note that this method retrieves and uses the ErrorManager
without doing a security check. It can therefore be used in
environments where the caller may be non-privileged.

**Parameters:**
- msg

- a descriptive string (may be null)
- ex

- an exception (may be null)
- code

- an error code defined in ErrorManager

---

#### public void setLevel​(
Level
newLevel)
throws
SecurityException

Set the log level specifying which message levels will be
logged by this

Handler

. Message levels lower than this
value will be discarded.

The intention is to allow developers to turn on voluminous
logging, but to limit the messages that are sent to certain

Handlers

.

**Parameters:**
- newLevel

- the new value for the log level

**Throws:**
- SecurityException

- if a security manager exists and if
the caller does not have

LoggingPermission("control")

.

---

#### public
Level
getLevel()

Get the log level specifying which messages will be
logged by this

Handler

. Message levels lower
than this level will be discarded.

**Returns:**
- the level of messages being logged.

---

#### public boolean isLoggable​(
LogRecord
record)

Check if this

Handler

would actually log a given

LogRecord

.

This method checks if the

LogRecord

has an appropriate

Level

and whether it satisfies any

Filter

. It also
may make other

Handler

specific checks that might prevent a
handler from logging the

LogRecord

. It will return false if
the

LogRecord

is null.

**Parameters:**
- record

- a

LogRecord

**Returns:**
- true if the

LogRecord

would be logged.

---

### Additional Sections

#### Class Handler

java.lang.Object

- java.util.logging.Handler

java.util.logging.Handler

**Direct Known Subclasses:** MemoryHandler

,

StreamHandler

```java
public abstract class
Handler

extends
Object
```

A

Handler

object takes log messages from a

Logger

and
exports them. It might for example, write them to a console
or write them to a file, or send them to a network logging service,
or forward them to an OS log, or whatever.

A

Handler

can be disabled by doing a

setLevel(Level.OFF)

and can be re-enabled by doing a

setLevel

with an appropriate level.

Handler

classes typically use

LogManager

properties to set
default values for the

Handler

's

Filter

,

Formatter

,
and

Level

. See the specific documentation for each concrete

Handler

class.

**Since:** 1.4

public abstract class

Handler

extends

Object

A

Handler

object takes log messages from a

Logger

and
exports them. It might for example, write them to a console
or write them to a file, or send them to a network logging service,
or forward them to an OS log, or whatever.

A

Handler

can be disabled by doing a

setLevel(Level.OFF)

and can be re-enabled by doing a

setLevel

with an appropriate level.

Handler

classes typically use

LogManager

properties to set
default values for the

Handler

's

Filter

,

Formatter

,
and

Level

. See the specific documentation for each concrete

Handler

class.

A

Handler

can be disabled by doing a

setLevel(Level.OFF)

and can be re-enabled by doing a

setLevel

with an appropriate level.

Handler

classes typically use

LogManager

properties to set
default values for the

Handler

's

Filter

,

Formatter

,
and

Level

. See the specific documentation for each concrete

Handler

class.

Handler

classes typically use

LogManager

properties to set
default values for the

Handler

's

Filter

,

Formatter

,
and

Level

. See the specific documentation for each concrete

Handler

class.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

Handler

()

Default constructor.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

abstract void

close

()

Close the

Handler

and free all associated resources.

abstract void

flush

()

Flush any buffered output.

String

getEncoding

()

Return the character encoding for this

Handler

.

ErrorManager

getErrorManager

()

Retrieves the ErrorManager for this Handler.

Filter

getFilter

()

Get the current

Filter

for this

Handler

.

Formatter

getFormatter

()

Return the

Formatter

for this

Handler

.

Level

getLevel

()

Get the log level specifying which messages will be
logged by this

Handler

.

boolean

isLoggable

​(

LogRecord

record)

Check if this

Handler

would actually log a given

LogRecord

.

abstract void

publish

​(

LogRecord

record)

Publish a

LogRecord

.

protected void

reportError

​(

String

msg,

Exception

ex,
int code)

Protected convenience method to report an error to this Handler's
ErrorManager.

void

setEncoding

​(

String

encoding)

Set the character encoding used by this

Handler

.

void

setErrorManager

​(

ErrorManager

em)

Define an ErrorManager for this Handler.

void

setFilter

​(

Filter

newFilter)

Set a

Filter

to control output on this

Handler

.

void

setFormatter

​(

Formatter

newFormatter)

Set a

Formatter

.

void

setLevel

​(

Level

newLevel)

Set the log level specifying which message levels will be
logged by this

Handler

.

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

Modifier

Constructor

Description

protected

Handler

()

Default constructor.

---

#### Constructor Summary

Default constructor.

Method Summary

All Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

abstract void

close

()

Close the

Handler

and free all associated resources.

abstract void

flush

()

Flush any buffered output.

String

getEncoding

()

Return the character encoding for this

Handler

.

ErrorManager

getErrorManager

()

Retrieves the ErrorManager for this Handler.

Filter

getFilter

()

Get the current

Filter

for this

Handler

.

Formatter

getFormatter

()

Return the

Formatter

for this

Handler

.

Level

getLevel

()

Get the log level specifying which messages will be
logged by this

Handler

.

boolean

isLoggable

​(

LogRecord

record)

Check if this

Handler

would actually log a given

LogRecord

.

abstract void

publish

​(

LogRecord

record)

Publish a

LogRecord

.

protected void

reportError

​(

String

msg,

Exception

ex,
int code)

Protected convenience method to report an error to this Handler's
ErrorManager.

void

setEncoding

​(

String

encoding)

Set the character encoding used by this

Handler

.

void

setErrorManager

​(

ErrorManager

em)

Define an ErrorManager for this Handler.

void

setFilter

​(

Filter

newFilter)

Set a

Filter

to control output on this

Handler

.

void

setFormatter

​(

Formatter

newFormatter)

Set a

Formatter

.

void

setLevel

​(

Level

newLevel)

Set the log level specifying which message levels will be
logged by this

Handler

.

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

Close the

Handler

and free all associated resources.

Flush any buffered output.

Return the character encoding for this

Handler

.

Retrieves the ErrorManager for this Handler.

Get the current

Filter

for this

Handler

.

Return the

Formatter

for this

Handler

.

Get the log level specifying which messages will be
logged by this

Handler

.

Check if this

Handler

would actually log a given

LogRecord

.

Publish a

LogRecord

.

Protected convenience method to report an error to this Handler's
ErrorManager.

Set the character encoding used by this

Handler

.

Define an ErrorManager for this Handler.

Set a

Filter

to control output on this

Handler

.

Set a

Formatter

.

Set the log level specifying which message levels will be
logged by this

Handler

.

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

- Handler

```java
protected Handler()
```

Default constructor. The resulting

Handler

has a log
level of

Level.ALL

, no

Formatter

, and no

Filter

. A default

ErrorManager

instance is installed
as the

ErrorManager

.

============ METHOD DETAIL ==========

- Method Detail

- publish

```java
public abstract void publish​(
LogRecord
record)
```

Publish a

LogRecord

.

The logging request was made initially to a

Logger

object,
which initialized the

LogRecord

and forwarded it here.

The

Handler

is responsible for formatting the message, when and
if necessary. The formatting should include localization.

**Parameters:** record

- description of the log event. A null record is
silently ignored and is not published

- flush

```java
public abstract void flush()
```

Flush any buffered output.

- close

```java
public abstract void close()
throws
SecurityException
```

Close the

Handler

and free all associated resources.

The close method will perform a

flush

and then close the

Handler

. After close has been called this

Handler

should no longer be used. Method calls may either be silently
ignored or may throw runtime exceptions.

**Throws:** SecurityException

- if a security manager exists and if
the caller does not have

LoggingPermission("control")

.

- setFormatter

```java
public void setFormatter​(
Formatter
newFormatter)
throws
SecurityException
```

Set a

Formatter

. This

Formatter

will be used
to format

LogRecords

for this

Handler

.

Some

Handlers

may not use

Formatters

, in
which case the

Formatter

will be remembered, but not used.

**Parameters:** newFormatter

- the

Formatter

to use (may not be null)
**Throws:** SecurityException

- if a security manager exists and if
the caller does not have

LoggingPermission("control")

.

- getFormatter

```java
public
Formatter
getFormatter()
```

Return the

Formatter

for this

Handler

.

**Returns:** the

Formatter

(may be null).

- setEncoding

```java
public void setEncoding​(
String
encoding)
throws
SecurityException
,

UnsupportedEncodingException
```

Set the character encoding used by this

Handler

.

The encoding should be set before any

LogRecords

are written
to the

Handler

.

**Parameters:** encoding

- The name of a supported character encoding.
May be null, to indicate the default platform encoding.
**Throws:** SecurityException

- if a security manager exists and if
the caller does not have

LoggingPermission("control")

.
**Throws:** UnsupportedEncodingException

- if the named encoding is
not supported.

- getEncoding

```java
public
String
getEncoding()
```

Return the character encoding for this

Handler

.

**Returns:** The encoding name. May be null, which indicates the
default encoding should be used.

- setFilter

```java
public void setFilter​(
Filter
newFilter)
throws
SecurityException
```

Set a

Filter

to control output on this

Handler

.

For each call of

publish

the

Handler

will call
this

Filter

(if it is non-null) to check if the

LogRecord

should be published or discarded.

**Parameters:** newFilter

- a

Filter

object (may be null)
**Throws:** SecurityException

- if a security manager exists and if
the caller does not have

LoggingPermission("control")

.

- getFilter

```java
public
Filter
getFilter()
```

Get the current

Filter

for this

Handler

.

**Returns:** a

Filter

object (may be null)

- setErrorManager

```java
public void setErrorManager​(
ErrorManager
em)
```

Define an ErrorManager for this Handler.

The ErrorManager's "error" method will be invoked if any
errors occur while using this Handler.

**Parameters:** em

- the new ErrorManager
**Throws:** SecurityException

- if a security manager exists and if
the caller does not have

LoggingPermission("control")

.

- getErrorManager

```java
public
ErrorManager
getErrorManager()
```

Retrieves the ErrorManager for this Handler.

**Returns:** the ErrorManager for this Handler
**Throws:** SecurityException

- if a security manager exists and if
the caller does not have

LoggingPermission("control")

.

- reportError

```java
protected void reportError​(
String
msg,

Exception
ex,
int code)
```

Protected convenience method to report an error to this Handler's
ErrorManager. Note that this method retrieves and uses the ErrorManager
without doing a security check. It can therefore be used in
environments where the caller may be non-privileged.

**Parameters:** msg

- a descriptive string (may be null)
**Parameters:** ex

- an exception (may be null)
**Parameters:** code

- an error code defined in ErrorManager

- setLevel

```java
public void setLevel​(
Level
newLevel)
throws
SecurityException
```

Set the log level specifying which message levels will be
logged by this

Handler

. Message levels lower than this
value will be discarded.

The intention is to allow developers to turn on voluminous
logging, but to limit the messages that are sent to certain

Handlers

.

**Parameters:** newLevel

- the new value for the log level
**Throws:** SecurityException

- if a security manager exists and if
the caller does not have

LoggingPermission("control")

.

- getLevel

```java
public
Level
getLevel()
```

Get the log level specifying which messages will be
logged by this

Handler

. Message levels lower
than this level will be discarded.

**Returns:** the level of messages being logged.

- isLoggable

```java
public boolean isLoggable​(
LogRecord
record)
```

Check if this

Handler

would actually log a given

LogRecord

.

This method checks if the

LogRecord

has an appropriate

Level

and whether it satisfies any

Filter

. It also
may make other

Handler

specific checks that might prevent a
handler from logging the

LogRecord

. It will return false if
the

LogRecord

is null.

**Parameters:** record

- a

LogRecord
**Returns:** true if the

LogRecord

would be logged.

Constructor Detail

- Handler

```java
protected Handler()
```

Default constructor. The resulting

Handler

has a log
level of

Level.ALL

, no

Formatter

, and no

Filter

. A default

ErrorManager

instance is installed
as the

ErrorManager

.

---

#### Constructor Detail

Handler

```java
protected Handler()
```

Default constructor. The resulting

Handler

has a log
level of

Level.ALL

, no

Formatter

, and no

Filter

. A default

ErrorManager

instance is installed
as the

ErrorManager

.

---

#### Handler

protected Handler()

Default constructor. The resulting

Handler

has a log
level of

Level.ALL

, no

Formatter

, and no

Filter

. A default

ErrorManager

instance is installed
as the

ErrorManager

.

Method Detail

- publish

```java
public abstract void publish​(
LogRecord
record)
```

Publish a

LogRecord

.

The logging request was made initially to a

Logger

object,
which initialized the

LogRecord

and forwarded it here.

The

Handler

is responsible for formatting the message, when and
if necessary. The formatting should include localization.

**Parameters:** record

- description of the log event. A null record is
silently ignored and is not published

- flush

```java
public abstract void flush()
```

Flush any buffered output.

- close

```java
public abstract void close()
throws
SecurityException
```

Close the

Handler

and free all associated resources.

The close method will perform a

flush

and then close the

Handler

. After close has been called this

Handler

should no longer be used. Method calls may either be silently
ignored or may throw runtime exceptions.

**Throws:** SecurityException

- if a security manager exists and if
the caller does not have

LoggingPermission("control")

.

- setFormatter

```java
public void setFormatter​(
Formatter
newFormatter)
throws
SecurityException
```

Set a

Formatter

. This

Formatter

will be used
to format

LogRecords

for this

Handler

.

Some

Handlers

may not use

Formatters

, in
which case the

Formatter

will be remembered, but not used.

**Parameters:** newFormatter

- the

Formatter

to use (may not be null)
**Throws:** SecurityException

- if a security manager exists and if
the caller does not have

LoggingPermission("control")

.

- getFormatter

```java
public
Formatter
getFormatter()
```

Return the

Formatter

for this

Handler

.

**Returns:** the

Formatter

(may be null).

- setEncoding

```java
public void setEncoding​(
String
encoding)
throws
SecurityException
,

UnsupportedEncodingException
```

Set the character encoding used by this

Handler

.

The encoding should be set before any

LogRecords

are written
to the

Handler

.

**Parameters:** encoding

- The name of a supported character encoding.
May be null, to indicate the default platform encoding.
**Throws:** SecurityException

- if a security manager exists and if
the caller does not have

LoggingPermission("control")

.
**Throws:** UnsupportedEncodingException

- if the named encoding is
not supported.

- getEncoding

```java
public
String
getEncoding()
```

Return the character encoding for this

Handler

.

**Returns:** The encoding name. May be null, which indicates the
default encoding should be used.

- setFilter

```java
public void setFilter​(
Filter
newFilter)
throws
SecurityException
```

Set a

Filter

to control output on this

Handler

.

For each call of

publish

the

Handler

will call
this

Filter

(if it is non-null) to check if the

LogRecord

should be published or discarded.

**Parameters:** newFilter

- a

Filter

object (may be null)
**Throws:** SecurityException

- if a security manager exists and if
the caller does not have

LoggingPermission("control")

.

- getFilter

```java
public
Filter
getFilter()
```

Get the current

Filter

for this

Handler

.

**Returns:** a

Filter

object (may be null)

- setErrorManager

```java
public void setErrorManager​(
ErrorManager
em)
```

Define an ErrorManager for this Handler.

The ErrorManager's "error" method will be invoked if any
errors occur while using this Handler.

**Parameters:** em

- the new ErrorManager
**Throws:** SecurityException

- if a security manager exists and if
the caller does not have

LoggingPermission("control")

.

- getErrorManager

```java
public
ErrorManager
getErrorManager()
```

Retrieves the ErrorManager for this Handler.

**Returns:** the ErrorManager for this Handler
**Throws:** SecurityException

- if a security manager exists and if
the caller does not have

LoggingPermission("control")

.

- reportError

```java
protected void reportError​(
String
msg,

Exception
ex,
int code)
```

Protected convenience method to report an error to this Handler's
ErrorManager. Note that this method retrieves and uses the ErrorManager
without doing a security check. It can therefore be used in
environments where the caller may be non-privileged.

**Parameters:** msg

- a descriptive string (may be null)
**Parameters:** ex

- an exception (may be null)
**Parameters:** code

- an error code defined in ErrorManager

- setLevel

```java
public void setLevel​(
Level
newLevel)
throws
SecurityException
```

Set the log level specifying which message levels will be
logged by this

Handler

. Message levels lower than this
value will be discarded.

The intention is to allow developers to turn on voluminous
logging, but to limit the messages that are sent to certain

Handlers

.

**Parameters:** newLevel

- the new value for the log level
**Throws:** SecurityException

- if a security manager exists and if
the caller does not have

LoggingPermission("control")

.

- getLevel

```java
public
Level
getLevel()
```

Get the log level specifying which messages will be
logged by this

Handler

. Message levels lower
than this level will be discarded.

**Returns:** the level of messages being logged.

- isLoggable

```java
public boolean isLoggable​(
LogRecord
record)
```

Check if this

Handler

would actually log a given

LogRecord

.

This method checks if the

LogRecord

has an appropriate

Level

and whether it satisfies any

Filter

. It also
may make other

Handler

specific checks that might prevent a
handler from logging the

LogRecord

. It will return false if
the

LogRecord

is null.

**Parameters:** record

- a

LogRecord
**Returns:** true if the

LogRecord

would be logged.

---

#### Method Detail

publish

```java
public abstract void publish​(
LogRecord
record)
```

Publish a

LogRecord

.

The logging request was made initially to a

Logger

object,
which initialized the

LogRecord

and forwarded it here.

The

Handler

is responsible for formatting the message, when and
if necessary. The formatting should include localization.

**Parameters:** record

- description of the log event. A null record is
silently ignored and is not published

---

#### publish

public abstract void publish​(

LogRecord

record)

Publish a

LogRecord

.

The logging request was made initially to a

Logger

object,
which initialized the

LogRecord

and forwarded it here.

The

Handler

is responsible for formatting the message, when and
if necessary. The formatting should include localization.

The logging request was made initially to a

Logger

object,
which initialized the

LogRecord

and forwarded it here.

The

Handler

is responsible for formatting the message, when and
if necessary. The formatting should include localization.

The

Handler

is responsible for formatting the message, when and
if necessary. The formatting should include localization.

flush

```java
public abstract void flush()
```

Flush any buffered output.

---

#### flush

public abstract void flush()

Flush any buffered output.

close

```java
public abstract void close()
throws
SecurityException
```

Close the

Handler

and free all associated resources.

The close method will perform a

flush

and then close the

Handler

. After close has been called this

Handler

should no longer be used. Method calls may either be silently
ignored or may throw runtime exceptions.

**Throws:** SecurityException

- if a security manager exists and if
the caller does not have

LoggingPermission("control")

.

---

#### close

public abstract void close()
throws

SecurityException

Close the

Handler

and free all associated resources.

The close method will perform a

flush

and then close the

Handler

. After close has been called this

Handler

should no longer be used. Method calls may either be silently
ignored or may throw runtime exceptions.

The close method will perform a

flush

and then close the

Handler

. After close has been called this

Handler

should no longer be used. Method calls may either be silently
ignored or may throw runtime exceptions.

setFormatter

```java
public void setFormatter​(
Formatter
newFormatter)
throws
SecurityException
```

Set a

Formatter

. This

Formatter

will be used
to format

LogRecords

for this

Handler

.

Some

Handlers

may not use

Formatters

, in
which case the

Formatter

will be remembered, but not used.

**Parameters:** newFormatter

- the

Formatter

to use (may not be null)
**Throws:** SecurityException

- if a security manager exists and if
the caller does not have

LoggingPermission("control")

.

---

#### setFormatter

public void setFormatter​(

Formatter

newFormatter)
throws

SecurityException

Set a

Formatter

. This

Formatter

will be used
to format

LogRecords

for this

Handler

.

Some

Handlers

may not use

Formatters

, in
which case the

Formatter

will be remembered, but not used.

Some

Handlers

may not use

Formatters

, in
which case the

Formatter

will be remembered, but not used.

getFormatter

```java
public
Formatter
getFormatter()
```

Return the

Formatter

for this

Handler

.

**Returns:** the

Formatter

(may be null).

---

#### getFormatter

public

Formatter

getFormatter()

Return the

Formatter

for this

Handler

.

setEncoding

```java
public void setEncoding​(
String
encoding)
throws
SecurityException
,

UnsupportedEncodingException
```

Set the character encoding used by this

Handler

.

The encoding should be set before any

LogRecords

are written
to the

Handler

.

**Parameters:** encoding

- The name of a supported character encoding.
May be null, to indicate the default platform encoding.
**Throws:** SecurityException

- if a security manager exists and if
the caller does not have

LoggingPermission("control")

.
**Throws:** UnsupportedEncodingException

- if the named encoding is
not supported.

---

#### setEncoding

public void setEncoding​(

String

encoding)
throws

SecurityException

,

UnsupportedEncodingException

Set the character encoding used by this

Handler

.

The encoding should be set before any

LogRecords

are written
to the

Handler

.

The encoding should be set before any

LogRecords

are written
to the

Handler

.

getEncoding

```java
public
String
getEncoding()
```

Return the character encoding for this

Handler

.

**Returns:** The encoding name. May be null, which indicates the
default encoding should be used.

---

#### getEncoding

public

String

getEncoding()

Return the character encoding for this

Handler

.

setFilter

```java
public void setFilter​(
Filter
newFilter)
throws
SecurityException
```

Set a

Filter

to control output on this

Handler

.

For each call of

publish

the

Handler

will call
this

Filter

(if it is non-null) to check if the

LogRecord

should be published or discarded.

**Parameters:** newFilter

- a

Filter

object (may be null)
**Throws:** SecurityException

- if a security manager exists and if
the caller does not have

LoggingPermission("control")

.

---

#### setFilter

public void setFilter​(

Filter

newFilter)
throws

SecurityException

Set a

Filter

to control output on this

Handler

.

For each call of

publish

the

Handler

will call
this

Filter

(if it is non-null) to check if the

LogRecord

should be published or discarded.

For each call of

publish

the

Handler

will call
this

Filter

(if it is non-null) to check if the

LogRecord

should be published or discarded.

getFilter

```java
public
Filter
getFilter()
```

Get the current

Filter

for this

Handler

.

**Returns:** a

Filter

object (may be null)

---

#### getFilter

public

Filter

getFilter()

Get the current

Filter

for this

Handler

.

setErrorManager

```java
public void setErrorManager​(
ErrorManager
em)
```

Define an ErrorManager for this Handler.

The ErrorManager's "error" method will be invoked if any
errors occur while using this Handler.

**Parameters:** em

- the new ErrorManager
**Throws:** SecurityException

- if a security manager exists and if
the caller does not have

LoggingPermission("control")

.

---

#### setErrorManager

public void setErrorManager​(

ErrorManager

em)

Define an ErrorManager for this Handler.

The ErrorManager's "error" method will be invoked if any
errors occur while using this Handler.

The ErrorManager's "error" method will be invoked if any
errors occur while using this Handler.

getErrorManager

```java
public
ErrorManager
getErrorManager()
```

Retrieves the ErrorManager for this Handler.

**Returns:** the ErrorManager for this Handler
**Throws:** SecurityException

- if a security manager exists and if
the caller does not have

LoggingPermission("control")

.

---

#### getErrorManager

public

ErrorManager

getErrorManager()

Retrieves the ErrorManager for this Handler.

reportError

```java
protected void reportError​(
String
msg,

Exception
ex,
int code)
```

Protected convenience method to report an error to this Handler's
ErrorManager. Note that this method retrieves and uses the ErrorManager
without doing a security check. It can therefore be used in
environments where the caller may be non-privileged.

**Parameters:** msg

- a descriptive string (may be null)
**Parameters:** ex

- an exception (may be null)
**Parameters:** code

- an error code defined in ErrorManager

---

#### reportError

protected void reportError​(

String

msg,

Exception

ex,
int code)

Protected convenience method to report an error to this Handler's
ErrorManager. Note that this method retrieves and uses the ErrorManager
without doing a security check. It can therefore be used in
environments where the caller may be non-privileged.

setLevel

```java
public void setLevel​(
Level
newLevel)
throws
SecurityException
```

Set the log level specifying which message levels will be
logged by this

Handler

. Message levels lower than this
value will be discarded.

The intention is to allow developers to turn on voluminous
logging, but to limit the messages that are sent to certain

Handlers

.

**Parameters:** newLevel

- the new value for the log level
**Throws:** SecurityException

- if a security manager exists and if
the caller does not have

LoggingPermission("control")

.

---

#### setLevel

public void setLevel​(

Level

newLevel)
throws

SecurityException

Set the log level specifying which message levels will be
logged by this

Handler

. Message levels lower than this
value will be discarded.

The intention is to allow developers to turn on voluminous
logging, but to limit the messages that are sent to certain

Handlers

.

The intention is to allow developers to turn on voluminous
logging, but to limit the messages that are sent to certain

Handlers

.

getLevel

```java
public
Level
getLevel()
```

Get the log level specifying which messages will be
logged by this

Handler

. Message levels lower
than this level will be discarded.

**Returns:** the level of messages being logged.

---

#### getLevel

public

Level

getLevel()

Get the log level specifying which messages will be
logged by this

Handler

. Message levels lower
than this level will be discarded.

isLoggable

```java
public boolean isLoggable​(
LogRecord
record)
```

Check if this

Handler

would actually log a given

LogRecord

.

This method checks if the

LogRecord

has an appropriate

Level

and whether it satisfies any

Filter

. It also
may make other

Handler

specific checks that might prevent a
handler from logging the

LogRecord

. It will return false if
the

LogRecord

is null.

**Parameters:** record

- a

LogRecord
**Returns:** true if the

LogRecord

would be logged.

---

#### isLoggable

public boolean isLoggable​(

LogRecord

record)

Check if this

Handler

would actually log a given

LogRecord

.

This method checks if the

LogRecord

has an appropriate

Level

and whether it satisfies any

Filter

. It also
may make other

Handler

specific checks that might prevent a
handler from logging the

LogRecord

. It will return false if
the

LogRecord

is null.

This method checks if the

LogRecord

has an appropriate

Level

and whether it satisfies any

Filter

. It also
may make other

Handler

specific checks that might prevent a
handler from logging the

LogRecord

. It will return false if
the

LogRecord

is null.

---

