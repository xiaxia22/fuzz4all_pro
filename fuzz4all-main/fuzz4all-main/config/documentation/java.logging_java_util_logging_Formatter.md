# Class Formatter

**Source:** `java.logging\java\util\logging\Formatter.html`

### Class Description

```java
public abstract class
Formatter

extends
Object
```

A Formatter provides support for formatting LogRecords.

Typically each logging Handler will have a Formatter associated
with it. The Formatter takes a LogRecord and converts it to
a string.

Some formatters (such as the XMLFormatter) need to wrap head
and tail strings around a set of formatted records. The getHeader
and getTail methods can be used to obtain these strings.

**Direct Known Subclasses:** SimpleFormatter

,

XMLFormatter

---

### Field Details

*No entries found.*

### Constructor Details

#### protected Formatter()

Construct a new formatter.

---

### Method Details

#### public abstract
String
format​(
LogRecord
record)

Format the given log record and return the formatted string.

The resulting formatted String will normally include a
localized and formatted version of the LogRecord's message field.
It is recommended to use the

formatMessage(java.util.logging.LogRecord)

convenience method to localize and format the message field.

**Parameters:**
- record

- the log record to be formatted.

**Returns:**
- the formatted log record

---

#### public
String
getHead​(
Handler
h)

Return the header string for a set of formatted records.

This base class returns an empty string, but this may be
overridden by subclasses.

**Parameters:**
- h

- The target handler (can be null)

**Returns:**
- header string

---

#### public
String
getTail​(
Handler
h)

Return the tail string for a set of formatted records.

This base class returns an empty string, but this may be
overridden by subclasses.

**Parameters:**
- h

- The target handler (can be null)

**Returns:**
- tail string

---

#### public
String
formatMessage​(
LogRecord
record)

Localize and format the message string from a log record. This
method is provided as a convenience for Formatter subclasses to
use when they are performing formatting.

The message string is first localized to a format string using
the record's ResourceBundle. (If there is no ResourceBundle,
or if the message key is not found, then the key is used as the
format string.) The format String uses java.text style
formatting.

- If there are no parameters, no formatter is used.

Otherwise, if the string contains "{<digit>"
where <digit> is in [0-9],
java.text.MessageFormat is used to format the string.

Otherwise no formatting is performed.

**Parameters:**
- record

- the log record containing the raw message

**Returns:**
- a localized and formatted message

---

### Additional Sections

#### Class Formatter

java.lang.Object

- java.util.logging.Formatter

java.util.logging.Formatter

**Direct Known Subclasses:** SimpleFormatter

,

XMLFormatter

```java
public abstract class
Formatter

extends
Object
```

A Formatter provides support for formatting LogRecords.

Typically each logging Handler will have a Formatter associated
with it. The Formatter takes a LogRecord and converts it to
a string.

Some formatters (such as the XMLFormatter) need to wrap head
and tail strings around a set of formatted records. The getHeader
and getTail methods can be used to obtain these strings.

**Since:** 1.4

public abstract class

Formatter

extends

Object

A Formatter provides support for formatting LogRecords.

Typically each logging Handler will have a Formatter associated
with it. The Formatter takes a LogRecord and converts it to
a string.

Some formatters (such as the XMLFormatter) need to wrap head
and tail strings around a set of formatted records. The getHeader
and getTail methods can be used to obtain these strings.

Typically each logging Handler will have a Formatter associated
with it. The Formatter takes a LogRecord and converts it to
a string.

Some formatters (such as the XMLFormatter) need to wrap head
and tail strings around a set of formatted records. The getHeader
and getTail methods can be used to obtain these strings.

Some formatters (such as the XMLFormatter) need to wrap head
and tail strings around a set of formatted records. The getHeader
and getTail methods can be used to obtain these strings.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

Formatter

()

Construct a new formatter.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

abstract

String

format

​(

LogRecord

record)

Format the given log record and return the formatted string.

String

formatMessage

​(

LogRecord

record)

Localize and format the message string from a log record.

String

getHead

​(

Handler

h)

Return the header string for a set of formatted records.

String

getTail

​(

Handler

h)

Return the tail string for a set of formatted records.

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

Formatter

()

Construct a new formatter.

---

#### Constructor Summary

Construct a new formatter.

Method Summary

All Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

abstract

String

format

​(

LogRecord

record)

Format the given log record and return the formatted string.

String

formatMessage

​(

LogRecord

record)

Localize and format the message string from a log record.

String

getHead

​(

Handler

h)

Return the header string for a set of formatted records.

String

getTail

​(

Handler

h)

Return the tail string for a set of formatted records.

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

Format the given log record and return the formatted string.

Localize and format the message string from a log record.

Return the header string for a set of formatted records.

Return the tail string for a set of formatted records.

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

- Formatter

```java
protected Formatter()
```

Construct a new formatter.

============ METHOD DETAIL ==========

- Method Detail

- format

```java
public abstract
String
format​(
LogRecord
record)
```

Format the given log record and return the formatted string.

The resulting formatted String will normally include a
localized and formatted version of the LogRecord's message field.
It is recommended to use the

formatMessage(java.util.logging.LogRecord)

convenience method to localize and format the message field.

**Parameters:** record

- the log record to be formatted.
**Returns:** the formatted log record

- getHead

```java
public
String
getHead​(
Handler
h)
```

Return the header string for a set of formatted records.

This base class returns an empty string, but this may be
overridden by subclasses.

**Parameters:** h

- The target handler (can be null)
**Returns:** header string

- getTail

```java
public
String
getTail​(
Handler
h)
```

Return the tail string for a set of formatted records.

This base class returns an empty string, but this may be
overridden by subclasses.

**Parameters:** h

- The target handler (can be null)
**Returns:** tail string

- formatMessage

```java
public
String
formatMessage​(
LogRecord
record)
```

Localize and format the message string from a log record. This
method is provided as a convenience for Formatter subclasses to
use when they are performing formatting.

The message string is first localized to a format string using
the record's ResourceBundle. (If there is no ResourceBundle,
or if the message key is not found, then the key is used as the
format string.) The format String uses java.text style
formatting.

- If there are no parameters, no formatter is used.

Otherwise, if the string contains "{<digit>"
where <digit> is in [0-9],
java.text.MessageFormat is used to format the string.

Otherwise no formatting is performed.

**Parameters:** record

- the log record containing the raw message
**Returns:** a localized and formatted message

Constructor Detail

- Formatter

```java
protected Formatter()
```

Construct a new formatter.

---

#### Constructor Detail

Formatter

```java
protected Formatter()
```

Construct a new formatter.

---

#### Formatter

protected Formatter()

Construct a new formatter.

Method Detail

- format

```java
public abstract
String
format​(
LogRecord
record)
```

Format the given log record and return the formatted string.

The resulting formatted String will normally include a
localized and formatted version of the LogRecord's message field.
It is recommended to use the

formatMessage(java.util.logging.LogRecord)

convenience method to localize and format the message field.

**Parameters:** record

- the log record to be formatted.
**Returns:** the formatted log record

- getHead

```java
public
String
getHead​(
Handler
h)
```

Return the header string for a set of formatted records.

This base class returns an empty string, but this may be
overridden by subclasses.

**Parameters:** h

- The target handler (can be null)
**Returns:** header string

- getTail

```java
public
String
getTail​(
Handler
h)
```

Return the tail string for a set of formatted records.

This base class returns an empty string, but this may be
overridden by subclasses.

**Parameters:** h

- The target handler (can be null)
**Returns:** tail string

- formatMessage

```java
public
String
formatMessage​(
LogRecord
record)
```

Localize and format the message string from a log record. This
method is provided as a convenience for Formatter subclasses to
use when they are performing formatting.

The message string is first localized to a format string using
the record's ResourceBundle. (If there is no ResourceBundle,
or if the message key is not found, then the key is used as the
format string.) The format String uses java.text style
formatting.

- If there are no parameters, no formatter is used.

Otherwise, if the string contains "{<digit>"
where <digit> is in [0-9],
java.text.MessageFormat is used to format the string.

Otherwise no formatting is performed.

**Parameters:** record

- the log record containing the raw message
**Returns:** a localized and formatted message

---

#### Method Detail

format

```java
public abstract
String
format​(
LogRecord
record)
```

Format the given log record and return the formatted string.

The resulting formatted String will normally include a
localized and formatted version of the LogRecord's message field.
It is recommended to use the

formatMessage(java.util.logging.LogRecord)

convenience method to localize and format the message field.

**Parameters:** record

- the log record to be formatted.
**Returns:** the formatted log record

---

#### format

public abstract

String

format​(

LogRecord

record)

Format the given log record and return the formatted string.

The resulting formatted String will normally include a
localized and formatted version of the LogRecord's message field.
It is recommended to use the

formatMessage(java.util.logging.LogRecord)

convenience method to localize and format the message field.

The resulting formatted String will normally include a
localized and formatted version of the LogRecord's message field.
It is recommended to use the

formatMessage(java.util.logging.LogRecord)

convenience method to localize and format the message field.

getHead

```java
public
String
getHead​(
Handler
h)
```

Return the header string for a set of formatted records.

This base class returns an empty string, but this may be
overridden by subclasses.

**Parameters:** h

- The target handler (can be null)
**Returns:** header string

---

#### getHead

public

String

getHead​(

Handler

h)

Return the header string for a set of formatted records.

This base class returns an empty string, but this may be
overridden by subclasses.

This base class returns an empty string, but this may be
overridden by subclasses.

getTail

```java
public
String
getTail​(
Handler
h)
```

Return the tail string for a set of formatted records.

This base class returns an empty string, but this may be
overridden by subclasses.

**Parameters:** h

- The target handler (can be null)
**Returns:** tail string

---

#### getTail

public

String

getTail​(

Handler

h)

Return the tail string for a set of formatted records.

This base class returns an empty string, but this may be
overridden by subclasses.

This base class returns an empty string, but this may be
overridden by subclasses.

formatMessage

```java
public
String
formatMessage​(
LogRecord
record)
```

Localize and format the message string from a log record. This
method is provided as a convenience for Formatter subclasses to
use when they are performing formatting.

The message string is first localized to a format string using
the record's ResourceBundle. (If there is no ResourceBundle,
or if the message key is not found, then the key is used as the
format string.) The format String uses java.text style
formatting.

- If there are no parameters, no formatter is used.

Otherwise, if the string contains "{<digit>"
where <digit> is in [0-9],
java.text.MessageFormat is used to format the string.

Otherwise no formatting is performed.

**Parameters:** record

- the log record containing the raw message
**Returns:** a localized and formatted message

---

#### formatMessage

public

String

formatMessage​(

LogRecord

record)

Localize and format the message string from a log record. This
method is provided as a convenience for Formatter subclasses to
use when they are performing formatting.

The message string is first localized to a format string using
the record's ResourceBundle. (If there is no ResourceBundle,
or if the message key is not found, then the key is used as the
format string.) The format String uses java.text style
formatting.

- If there are no parameters, no formatter is used.

Otherwise, if the string contains "{<digit>"
where <digit> is in [0-9],
java.text.MessageFormat is used to format the string.

Otherwise no formatting is performed.

The message string is first localized to a format string using
the record's ResourceBundle. (If there is no ResourceBundle,
or if the message key is not found, then the key is used as the
format string.) The format String uses java.text style
formatting.

- If there are no parameters, no formatter is used.

Otherwise, if the string contains "{<digit>"
where <digit> is in [0-9],
java.text.MessageFormat is used to format the string.

Otherwise no formatting is performed.

If there are no parameters, no formatter is used.

Otherwise, if the string contains "{<digit>"
where <digit> is in [0-9],
java.text.MessageFormat is used to format the string.

Otherwise no formatting is performed.

---

