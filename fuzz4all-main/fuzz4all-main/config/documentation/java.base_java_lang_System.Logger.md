# Interface System.Logger

**Source:** `java.base\java\lang\System.Logger.html`

### Class Description

```java
public static interface
System.Logger
```

System.Logger

instances log messages that will be
routed to the underlying logging framework the

LoggerFinder

uses.

System.Logger

instances are typically obtained from
the

System

class, by calling

System.getLogger(loggerName)

or

System.getLogger(loggerName, bundle)

.

**Enclosing class:** System

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### String
getName()

Returns the name of this logger.

**Returns:**
- the logger name.

---

#### boolean isLoggable​(
System.Logger.Level
level)

Checks if a message of the given level would be logged by
this logger.

**Parameters:**
- level

- the log message level.

**Returns:**
- true

if the given log message level is currently
being logged.

**Throws:**
- NullPointerException

- if

level

is

null

.

---

#### default void log​(
System.Logger.Level
level,

String
msg)

Logs a message.

**Parameters:**
- level

- the log message level.
- msg

- the string message (or a key in the message catalog, if
this logger is a

localized logger

);
can be

null

.

**Throws:**
- NullPointerException

- if

level

is

null

.

**Implementation Requirements:**
- The default implementation for this method calls

this.log(level, (ResourceBundle)null, msg, (Object[])null);

---

#### default void log​(
System.Logger.Level
level,

Supplier
<
String
> msgSupplier)

Logs a lazily supplied message.

If the logger is currently enabled for the given log message level
then a message is logged that is the result produced by the
given supplier function. Otherwise, the supplier is not operated on.

**Parameters:**
- level

- the log message level.
- msgSupplier

- a supplier function that produces a message.

**Throws:**
- NullPointerException

- if

level

is

null

,
or

msgSupplier

is

null

.

**Implementation Requirements:**
- When logging is enabled for the given level, the default
implementation for this method calls

this.log(level, (ResourceBundle)null, msgSupplier.get(), (Object[])null);

---

#### default void log​(
System.Logger.Level
level,

Object
obj)

Logs a message produced from the given object.

If the logger is currently enabled for the given log message level then
a message is logged that, by default, is the result produced from
calling toString on the given object.
Otherwise, the object is not operated on.

**Parameters:**
- level

- the log message level.
- obj

- the object to log.

**Throws:**
- NullPointerException

- if

level

is

null

, or

obj

is

null

.

**Implementation Requirements:**
- When logging is enabled for the given level, the default
implementation for this method calls

this.log(level, (ResourceBundle)null, obj.toString(), (Object[])null);

---

#### default void log​(
System.Logger.Level
level,

String
msg,

Throwable
thrown)

Logs a message associated with a given throwable.

**Parameters:**
- level

- the log message level.
- msg

- the string message (or a key in the message catalog, if
this logger is a

localized logger

);
can be

null

.
- thrown

- a

Throwable

associated with the log message;
can be

null

.

**Throws:**
- NullPointerException

- if

level

is

null

.

**Implementation Requirements:**
- The default implementation for this method calls

this.log(level, (ResourceBundle)null, msg, thrown);

---

#### default void log​(
System.Logger.Level
level,

Supplier
<
String
> msgSupplier,

Throwable
thrown)

Logs a lazily supplied message associated with a given throwable.

If the logger is currently enabled for the given log message level
then a message is logged that is the result produced by the
given supplier function. Otherwise, the supplier is not operated on.

**Parameters:**
- level

- one of the log message level identifiers.
- msgSupplier

- a supplier function that produces a message.
- thrown

- a

Throwable

associated with log message;
can be

null

.

**Throws:**
- NullPointerException

- if

level

is

null

, or

msgSupplier

is

null

.

**Implementation Requirements:**
- When logging is enabled for the given level, the default
implementation for this method calls

this.log(level, (ResourceBundle)null, msgSupplier.get(), thrown);

---

#### default void log​(
System.Logger.Level
level,

String
format,

Object
... params)

Logs a message with an optional list of parameters.

**Parameters:**
- level

- one of the log message level identifiers.
- format

- the string message format in

MessageFormat

format, (or a key in the message
catalog, if this logger is a

localized logger

);
can be

null

.
- params

- an optional list of parameters to the message (may be
none).

**Throws:**
- NullPointerException

- if

level

is

null

.

**Implementation Requirements:**
- The default implementation for this method calls

this.log(level, (ResourceBundle)null, format, params);

---

#### void log​(
System.Logger.Level
level,

ResourceBundle
bundle,

String
msg,

Throwable
thrown)

Logs a localized message associated with a given throwable.

If the given resource bundle is non-

null

, the

msg

string is localized using the given resource bundle.
Otherwise the

msg

string is not localized.

**Parameters:**
- level

- the log message level.
- bundle

- a resource bundle to localize

msg

; can be

null

.
- msg

- the string message (or a key in the message catalog,
if

bundle

is not

null

); can be

null

.
- thrown

- a

Throwable

associated with the log message;
can be

null

.

**Throws:**
- NullPointerException

- if

level

is

null

.

---

#### void log​(
System.Logger.Level
level,

ResourceBundle
bundle,

String
format,

Object
... params)

Logs a message with resource bundle and an optional list of
parameters.

If the given resource bundle is non-

null

, the

format

string is localized using the given resource bundle.
Otherwise the

format

string is not localized.

**Parameters:**
- level

- the log message level.
- bundle

- a resource bundle to localize

format

; can be

null

.
- format

- the string message format in

MessageFormat

format, (or a key in the message
catalog if

bundle

is not

null

); can be

null

.
- params

- an optional list of parameters to the message (may be
none).

**Throws:**
- NullPointerException

- if

level

is

null

.

---

### Additional Sections

#### Interface System.Logger

**Enclosing class:** System

```java
public static interface
System.Logger
```

System.Logger

instances log messages that will be
routed to the underlying logging framework the

LoggerFinder

uses.

System.Logger

instances are typically obtained from
the

System

class, by calling

System.getLogger(loggerName)

or

System.getLogger(loggerName, bundle)

.

**Since:** 9
**See Also:** System.getLogger(java.lang.String)

,

System.getLogger(java.lang.String, java.util.ResourceBundle)

,

System.LoggerFinder

public static interface

System.Logger

System.Logger

instances log messages that will be
routed to the underlying logging framework the

LoggerFinder

uses.

System.Logger

instances are typically obtained from
the

System

class, by calling

System.getLogger(loggerName)

or

System.getLogger(loggerName, bundle)

.

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

Nested Classes

Modifier and Type

Interface

Description

static class

System.Logger.Level

System

loggers

levels.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Default Methods

Modifier and Type

Method

Description

String

getName

()

Returns the name of this logger.

boolean

isLoggable

​(

System.Logger.Level

level)

Checks if a message of the given level would be logged by
this logger.

default void

log

​(

System.Logger.Level

level,

Object

obj)

Logs a message produced from the given object.

default void

log

​(

System.Logger.Level

level,

String

msg)

Logs a message.

default void

log

​(

System.Logger.Level

level,

String

format,

Object

... params)

Logs a message with an optional list of parameters.

default void

log

​(

System.Logger.Level

level,

String

msg,

Throwable

thrown)

Logs a message associated with a given throwable.

default void

log

​(

System.Logger.Level

level,

Supplier

<

String

> msgSupplier)

Logs a lazily supplied message.

default void

log

​(

System.Logger.Level

level,

Supplier

<

String

> msgSupplier,

Throwable

thrown)

Logs a lazily supplied message associated with a given throwable.

void

log

​(

System.Logger.Level

level,

ResourceBundle

bundle,

String

format,

Object

... params)

Logs a message with resource bundle and an optional list of
parameters.

void

log

​(

System.Logger.Level

level,

ResourceBundle

bundle,

String

msg,

Throwable

thrown)

Logs a localized message associated with a given throwable.

Nested Class Summary

Nested Classes

Modifier and Type

Interface

Description

static class

System.Logger.Level

System

loggers

levels.

---

#### Nested Class Summary

System

loggers

levels.

Method Summary

All Methods

Instance Methods

Abstract Methods

Default Methods

Modifier and Type

Method

Description

String

getName

()

Returns the name of this logger.

boolean

isLoggable

​(

System.Logger.Level

level)

Checks if a message of the given level would be logged by
this logger.

default void

log

​(

System.Logger.Level

level,

Object

obj)

Logs a message produced from the given object.

default void

log

​(

System.Logger.Level

level,

String

msg)

Logs a message.

default void

log

​(

System.Logger.Level

level,

String

format,

Object

... params)

Logs a message with an optional list of parameters.

default void

log

​(

System.Logger.Level

level,

String

msg,

Throwable

thrown)

Logs a message associated with a given throwable.

default void

log

​(

System.Logger.Level

level,

Supplier

<

String

> msgSupplier)

Logs a lazily supplied message.

default void

log

​(

System.Logger.Level

level,

Supplier

<

String

> msgSupplier,

Throwable

thrown)

Logs a lazily supplied message associated with a given throwable.

void

log

​(

System.Logger.Level

level,

ResourceBundle

bundle,

String

format,

Object

... params)

Logs a message with resource bundle and an optional list of
parameters.

void

log

​(

System.Logger.Level

level,

ResourceBundle

bundle,

String

msg,

Throwable

thrown)

Logs a localized message associated with a given throwable.

---

#### Method Summary

Returns the name of this logger.

Checks if a message of the given level would be logged by
this logger.

Logs a message produced from the given object.

Logs a message.

Logs a message with an optional list of parameters.

Logs a message associated with a given throwable.

Logs a lazily supplied message.

Logs a lazily supplied message associated with a given throwable.

Logs a message with resource bundle and an optional list of
parameters.

Logs a localized message associated with a given throwable.

============ METHOD DETAIL ==========

- Method Detail

- getName

```java
String
getName()
```

Returns the name of this logger.

**Returns:** the logger name.

- isLoggable

```java
boolean isLoggable​(
System.Logger.Level
level)
```

Checks if a message of the given level would be logged by
this logger.

**Parameters:** level

- the log message level.
**Returns:** true

if the given log message level is currently
being logged.
**Throws:** NullPointerException

- if

level

is

null

.

- log

```java
default void log​(
System.Logger.Level
level,

String
msg)
```

Logs a message.

**Implementation Requirements:** The default implementation for this method calls

this.log(level, (ResourceBundle)null, msg, (Object[])null);
**Parameters:** level

- the log message level.
**Parameters:** msg

- the string message (or a key in the message catalog, if
this logger is a

localized logger

);
can be

null

.
**Throws:** NullPointerException

- if

level

is

null

.

- log

```java
default void log​(
System.Logger.Level
level,

Supplier
<
String
> msgSupplier)
```

Logs a lazily supplied message.

If the logger is currently enabled for the given log message level
then a message is logged that is the result produced by the
given supplier function. Otherwise, the supplier is not operated on.

**Implementation Requirements:** When logging is enabled for the given level, the default
implementation for this method calls

this.log(level, (ResourceBundle)null, msgSupplier.get(), (Object[])null);
**Parameters:** level

- the log message level.
**Parameters:** msgSupplier

- a supplier function that produces a message.
**Throws:** NullPointerException

- if

level

is

null

,
or

msgSupplier

is

null

.

- log

```java
default void log​(
System.Logger.Level
level,

Object
obj)
```

Logs a message produced from the given object.

If the logger is currently enabled for the given log message level then
a message is logged that, by default, is the result produced from
calling toString on the given object.
Otherwise, the object is not operated on.

**Implementation Requirements:** When logging is enabled for the given level, the default
implementation for this method calls

this.log(level, (ResourceBundle)null, obj.toString(), (Object[])null);
**Parameters:** level

- the log message level.
**Parameters:** obj

- the object to log.
**Throws:** NullPointerException

- if

level

is

null

, or

obj

is

null

.

- log

```java
default void log​(
System.Logger.Level
level,

String
msg,

Throwable
thrown)
```

Logs a message associated with a given throwable.

**Implementation Requirements:** The default implementation for this method calls

this.log(level, (ResourceBundle)null, msg, thrown);
**Parameters:** level

- the log message level.
**Parameters:** msg

- the string message (or a key in the message catalog, if
this logger is a

localized logger

);
can be

null

.
**Parameters:** thrown

- a

Throwable

associated with the log message;
can be

null

.
**Throws:** NullPointerException

- if

level

is

null

.

- log

```java
default void log​(
System.Logger.Level
level,

Supplier
<
String
> msgSupplier,

Throwable
thrown)
```

Logs a lazily supplied message associated with a given throwable.

If the logger is currently enabled for the given log message level
then a message is logged that is the result produced by the
given supplier function. Otherwise, the supplier is not operated on.

**Implementation Requirements:** When logging is enabled for the given level, the default
implementation for this method calls

this.log(level, (ResourceBundle)null, msgSupplier.get(), thrown);
**Parameters:** level

- one of the log message level identifiers.
**Parameters:** msgSupplier

- a supplier function that produces a message.
**Parameters:** thrown

- a

Throwable

associated with log message;
can be

null

.
**Throws:** NullPointerException

- if

level

is

null

, or

msgSupplier

is

null

.

- log

```java
default void log​(
System.Logger.Level
level,

String
format,

Object
... params)
```

Logs a message with an optional list of parameters.

**Implementation Requirements:** The default implementation for this method calls

this.log(level, (ResourceBundle)null, format, params);
**Parameters:** level

- one of the log message level identifiers.
**Parameters:** format

- the string message format in

MessageFormat

format, (or a key in the message
catalog, if this logger is a

localized logger

);
can be

null

.
**Parameters:** params

- an optional list of parameters to the message (may be
none).
**Throws:** NullPointerException

- if

level

is

null

.

- log

```java
void log​(
System.Logger.Level
level,

ResourceBundle
bundle,

String
msg,

Throwable
thrown)
```

Logs a localized message associated with a given throwable.

If the given resource bundle is non-

null

, the

msg

string is localized using the given resource bundle.
Otherwise the

msg

string is not localized.

**Parameters:** level

- the log message level.
**Parameters:** bundle

- a resource bundle to localize

msg

; can be

null

.
**Parameters:** msg

- the string message (or a key in the message catalog,
if

bundle

is not

null

); can be

null

.
**Parameters:** thrown

- a

Throwable

associated with the log message;
can be

null

.
**Throws:** NullPointerException

- if

level

is

null

.

- log

```java
void log​(
System.Logger.Level
level,

ResourceBundle
bundle,

String
format,

Object
... params)
```

Logs a message with resource bundle and an optional list of
parameters.

If the given resource bundle is non-

null

, the

format

string is localized using the given resource bundle.
Otherwise the

format

string is not localized.

**Parameters:** level

- the log message level.
**Parameters:** bundle

- a resource bundle to localize

format

; can be

null

.
**Parameters:** format

- the string message format in

MessageFormat

format, (or a key in the message
catalog if

bundle

is not

null

); can be

null

.
**Parameters:** params

- an optional list of parameters to the message (may be
none).
**Throws:** NullPointerException

- if

level

is

null

.

Method Detail

- getName

```java
String
getName()
```

Returns the name of this logger.

**Returns:** the logger name.

- isLoggable

```java
boolean isLoggable​(
System.Logger.Level
level)
```

Checks if a message of the given level would be logged by
this logger.

**Parameters:** level

- the log message level.
**Returns:** true

if the given log message level is currently
being logged.
**Throws:** NullPointerException

- if

level

is

null

.

- log

```java
default void log​(
System.Logger.Level
level,

String
msg)
```

Logs a message.

**Implementation Requirements:** The default implementation for this method calls

this.log(level, (ResourceBundle)null, msg, (Object[])null);
**Parameters:** level

- the log message level.
**Parameters:** msg

- the string message (or a key in the message catalog, if
this logger is a

localized logger

);
can be

null

.
**Throws:** NullPointerException

- if

level

is

null

.

- log

```java
default void log​(
System.Logger.Level
level,

Supplier
<
String
> msgSupplier)
```

Logs a lazily supplied message.

If the logger is currently enabled for the given log message level
then a message is logged that is the result produced by the
given supplier function. Otherwise, the supplier is not operated on.

**Implementation Requirements:** When logging is enabled for the given level, the default
implementation for this method calls

this.log(level, (ResourceBundle)null, msgSupplier.get(), (Object[])null);
**Parameters:** level

- the log message level.
**Parameters:** msgSupplier

- a supplier function that produces a message.
**Throws:** NullPointerException

- if

level

is

null

,
or

msgSupplier

is

null

.

- log

```java
default void log​(
System.Logger.Level
level,

Object
obj)
```

Logs a message produced from the given object.

If the logger is currently enabled for the given log message level then
a message is logged that, by default, is the result produced from
calling toString on the given object.
Otherwise, the object is not operated on.

**Implementation Requirements:** When logging is enabled for the given level, the default
implementation for this method calls

this.log(level, (ResourceBundle)null, obj.toString(), (Object[])null);
**Parameters:** level

- the log message level.
**Parameters:** obj

- the object to log.
**Throws:** NullPointerException

- if

level

is

null

, or

obj

is

null

.

- log

```java
default void log​(
System.Logger.Level
level,

String
msg,

Throwable
thrown)
```

Logs a message associated with a given throwable.

**Implementation Requirements:** The default implementation for this method calls

this.log(level, (ResourceBundle)null, msg, thrown);
**Parameters:** level

- the log message level.
**Parameters:** msg

- the string message (or a key in the message catalog, if
this logger is a

localized logger

);
can be

null

.
**Parameters:** thrown

- a

Throwable

associated with the log message;
can be

null

.
**Throws:** NullPointerException

- if

level

is

null

.

- log

```java
default void log​(
System.Logger.Level
level,

Supplier
<
String
> msgSupplier,

Throwable
thrown)
```

Logs a lazily supplied message associated with a given throwable.

If the logger is currently enabled for the given log message level
then a message is logged that is the result produced by the
given supplier function. Otherwise, the supplier is not operated on.

**Implementation Requirements:** When logging is enabled for the given level, the default
implementation for this method calls

this.log(level, (ResourceBundle)null, msgSupplier.get(), thrown);
**Parameters:** level

- one of the log message level identifiers.
**Parameters:** msgSupplier

- a supplier function that produces a message.
**Parameters:** thrown

- a

Throwable

associated with log message;
can be

null

.
**Throws:** NullPointerException

- if

level

is

null

, or

msgSupplier

is

null

.

- log

```java
default void log​(
System.Logger.Level
level,

String
format,

Object
... params)
```

Logs a message with an optional list of parameters.

**Implementation Requirements:** The default implementation for this method calls

this.log(level, (ResourceBundle)null, format, params);
**Parameters:** level

- one of the log message level identifiers.
**Parameters:** format

- the string message format in

MessageFormat

format, (or a key in the message
catalog, if this logger is a

localized logger

);
can be

null

.
**Parameters:** params

- an optional list of parameters to the message (may be
none).
**Throws:** NullPointerException

- if

level

is

null

.

- log

```java
void log​(
System.Logger.Level
level,

ResourceBundle
bundle,

String
msg,

Throwable
thrown)
```

Logs a localized message associated with a given throwable.

If the given resource bundle is non-

null

, the

msg

string is localized using the given resource bundle.
Otherwise the

msg

string is not localized.

**Parameters:** level

- the log message level.
**Parameters:** bundle

- a resource bundle to localize

msg

; can be

null

.
**Parameters:** msg

- the string message (or a key in the message catalog,
if

bundle

is not

null

); can be

null

.
**Parameters:** thrown

- a

Throwable

associated with the log message;
can be

null

.
**Throws:** NullPointerException

- if

level

is

null

.

- log

```java
void log​(
System.Logger.Level
level,

ResourceBundle
bundle,

String
format,

Object
... params)
```

Logs a message with resource bundle and an optional list of
parameters.

If the given resource bundle is non-

null

, the

format

string is localized using the given resource bundle.
Otherwise the

format

string is not localized.

**Parameters:** level

- the log message level.
**Parameters:** bundle

- a resource bundle to localize

format

; can be

null

.
**Parameters:** format

- the string message format in

MessageFormat

format, (or a key in the message
catalog if

bundle

is not

null

); can be

null

.
**Parameters:** params

- an optional list of parameters to the message (may be
none).
**Throws:** NullPointerException

- if

level

is

null

.

---

#### Method Detail

getName

```java
String
getName()
```

Returns the name of this logger.

**Returns:** the logger name.

---

#### getName

String

getName()

Returns the name of this logger.

isLoggable

```java
boolean isLoggable​(
System.Logger.Level
level)
```

Checks if a message of the given level would be logged by
this logger.

**Parameters:** level

- the log message level.
**Returns:** true

if the given log message level is currently
being logged.
**Throws:** NullPointerException

- if

level

is

null

.

---

#### isLoggable

boolean isLoggable​(

System.Logger.Level

level)

Checks if a message of the given level would be logged by
this logger.

log

```java
default void log​(
System.Logger.Level
level,

String
msg)
```

Logs a message.

**Implementation Requirements:** The default implementation for this method calls

this.log(level, (ResourceBundle)null, msg, (Object[])null);
**Parameters:** level

- the log message level.
**Parameters:** msg

- the string message (or a key in the message catalog, if
this logger is a

localized logger

);
can be

null

.
**Throws:** NullPointerException

- if

level

is

null

.

---

#### log

default void log​(

System.Logger.Level

level,

String

msg)

Logs a message.

log

```java
default void log​(
System.Logger.Level
level,

Supplier
<
String
> msgSupplier)
```

Logs a lazily supplied message.

If the logger is currently enabled for the given log message level
then a message is logged that is the result produced by the
given supplier function. Otherwise, the supplier is not operated on.

**Implementation Requirements:** When logging is enabled for the given level, the default
implementation for this method calls

this.log(level, (ResourceBundle)null, msgSupplier.get(), (Object[])null);
**Parameters:** level

- the log message level.
**Parameters:** msgSupplier

- a supplier function that produces a message.
**Throws:** NullPointerException

- if

level

is

null

,
or

msgSupplier

is

null

.

---

#### log

default void log​(

System.Logger.Level

level,

Supplier

<

String

> msgSupplier)

Logs a lazily supplied message.

If the logger is currently enabled for the given log message level
then a message is logged that is the result produced by the
given supplier function. Otherwise, the supplier is not operated on.

log

```java
default void log​(
System.Logger.Level
level,

Object
obj)
```

Logs a message produced from the given object.

If the logger is currently enabled for the given log message level then
a message is logged that, by default, is the result produced from
calling toString on the given object.
Otherwise, the object is not operated on.

**Implementation Requirements:** When logging is enabled for the given level, the default
implementation for this method calls

this.log(level, (ResourceBundle)null, obj.toString(), (Object[])null);
**Parameters:** level

- the log message level.
**Parameters:** obj

- the object to log.
**Throws:** NullPointerException

- if

level

is

null

, or

obj

is

null

.

---

#### log

default void log​(

System.Logger.Level

level,

Object

obj)

Logs a message produced from the given object.

If the logger is currently enabled for the given log message level then
a message is logged that, by default, is the result produced from
calling toString on the given object.
Otherwise, the object is not operated on.

log

```java
default void log​(
System.Logger.Level
level,

String
msg,

Throwable
thrown)
```

Logs a message associated with a given throwable.

**Implementation Requirements:** The default implementation for this method calls

this.log(level, (ResourceBundle)null, msg, thrown);
**Parameters:** level

- the log message level.
**Parameters:** msg

- the string message (or a key in the message catalog, if
this logger is a

localized logger

);
can be

null

.
**Parameters:** thrown

- a

Throwable

associated with the log message;
can be

null

.
**Throws:** NullPointerException

- if

level

is

null

.

---

#### log

default void log​(

System.Logger.Level

level,

String

msg,

Throwable

thrown)

Logs a message associated with a given throwable.

log

```java
default void log​(
System.Logger.Level
level,

Supplier
<
String
> msgSupplier,

Throwable
thrown)
```

Logs a lazily supplied message associated with a given throwable.

If the logger is currently enabled for the given log message level
then a message is logged that is the result produced by the
given supplier function. Otherwise, the supplier is not operated on.

**Implementation Requirements:** When logging is enabled for the given level, the default
implementation for this method calls

this.log(level, (ResourceBundle)null, msgSupplier.get(), thrown);
**Parameters:** level

- one of the log message level identifiers.
**Parameters:** msgSupplier

- a supplier function that produces a message.
**Parameters:** thrown

- a

Throwable

associated with log message;
can be

null

.
**Throws:** NullPointerException

- if

level

is

null

, or

msgSupplier

is

null

.

---

#### log

default void log​(

System.Logger.Level

level,

Supplier

<

String

> msgSupplier,

Throwable

thrown)

Logs a lazily supplied message associated with a given throwable.

If the logger is currently enabled for the given log message level
then a message is logged that is the result produced by the
given supplier function. Otherwise, the supplier is not operated on.

log

```java
default void log​(
System.Logger.Level
level,

String
format,

Object
... params)
```

Logs a message with an optional list of parameters.

**Implementation Requirements:** The default implementation for this method calls

this.log(level, (ResourceBundle)null, format, params);
**Parameters:** level

- one of the log message level identifiers.
**Parameters:** format

- the string message format in

MessageFormat

format, (or a key in the message
catalog, if this logger is a

localized logger

);
can be

null

.
**Parameters:** params

- an optional list of parameters to the message (may be
none).
**Throws:** NullPointerException

- if

level

is

null

.

---

#### log

default void log​(

System.Logger.Level

level,

String

format,

Object

... params)

Logs a message with an optional list of parameters.

log

```java
void log​(
System.Logger.Level
level,

ResourceBundle
bundle,

String
msg,

Throwable
thrown)
```

Logs a localized message associated with a given throwable.

If the given resource bundle is non-

null

, the

msg

string is localized using the given resource bundle.
Otherwise the

msg

string is not localized.

**Parameters:** level

- the log message level.
**Parameters:** bundle

- a resource bundle to localize

msg

; can be

null

.
**Parameters:** msg

- the string message (or a key in the message catalog,
if

bundle

is not

null

); can be

null

.
**Parameters:** thrown

- a

Throwable

associated with the log message;
can be

null

.
**Throws:** NullPointerException

- if

level

is

null

.

---

#### log

void log​(

System.Logger.Level

level,

ResourceBundle

bundle,

String

msg,

Throwable

thrown)

Logs a localized message associated with a given throwable.

If the given resource bundle is non-

null

, the

msg

string is localized using the given resource bundle.
Otherwise the

msg

string is not localized.

log

```java
void log​(
System.Logger.Level
level,

ResourceBundle
bundle,

String
format,

Object
... params)
```

Logs a message with resource bundle and an optional list of
parameters.

If the given resource bundle is non-

null

, the

format

string is localized using the given resource bundle.
Otherwise the

format

string is not localized.

**Parameters:** level

- the log message level.
**Parameters:** bundle

- a resource bundle to localize

format

; can be

null

.
**Parameters:** format

- the string message format in

MessageFormat

format, (or a key in the message
catalog if

bundle

is not

null

); can be

null

.
**Parameters:** params

- an optional list of parameters to the message (may be
none).
**Throws:** NullPointerException

- if

level

is

null

.

---

#### log

void log​(

System.Logger.Level

level,

ResourceBundle

bundle,

String

format,

Object

... params)

Logs a message with resource bundle and an optional list of
parameters.

If the given resource bundle is non-

null

, the

format

string is localized using the given resource bundle.
Otherwise the

format

string is not localized.

---

