# Class XMLFormatter

**Source:** `java.logging\java\util\logging\XMLFormatter.html`

### Class Description

```java
public class
XMLFormatter

extends
Formatter
```

Format a LogRecord into a standard XML format.

The DTD specification is provided as Appendix A to the
Java Logging APIs specification.

The XMLFormatter can be used with arbitrary character encodings,
but it is recommended that it normally be used with UTF-8. The
character encoding can be set on the output Handler.

**Implementation Requirements:** Since JDK 9, instances of

LogRecord

contain
an

Instant

which can have nanoseconds below
the millisecond resolution.
The DTD specification has been updated to allow for an optional

<nanos>

element. By default, the XMLFormatter will compute the
nanosecond adjustment below the millisecond resolution (using

LogRecord.getInstant().getNano() % 1000_000

) - and if this is not 0,
this adjustment value will be printed in the new

<nanos>

element.
The event instant can then be reconstructed using

Instant.ofEpochSecond(millis/1000L, (millis % 1000L) * 1000_000L + nanos)

where

millis

and

nanos

represent the numbers serialized in
the

<millis>

and

<nanos>

elements, respectively.

The

<date>

element will now contain the whole instant as formatted
by the

DateTimeFormatter.ISO_INSTANT

formatter.

For compatibility with old parsers, XMLFormatters can
be configured to revert to the old format by specifying a

<xml-formatter-fully-qualified-class-name>.useInstant = false

property

in the
logging configuration. When

useInstant

is

false

, the old
formatting will be preserved. When

useInstant

is

true

(the default), the

<nanos>

element will be printed and the

<date>

element will contain the

formatted

instant.

For instance, in order to configure plain instances of XMLFormatter to omit
the new

<nano>

element,

java.util.logging.XMLFormatter.useInstant = false

can be specified
in the logging configuration.
**Since:** 1.4

---

### Field Details

*No entries found.*

### Constructor Details

#### public XMLFormatter()

Creates a new instance of XMLFormatter.

**Implementation Requirements:**
- Since JDK 9, the XMLFormatter will print out the record

event time

as an Instant. This instant
has the best resolution available on the system. The

<date>

element will contain the instant as formatted by the

DateTimeFormatter.ISO_INSTANT

.
In addition, an optional

<nanos>

element containing a
nanosecond adjustment will be printed if the instant contains some
nanoseconds below the millisecond resolution.

This new behavior can be turned off, and the old formatting restored,
by specifying a property in the

logging configuration

.
If

LogManager.getLogManager().getProperty(
this.getClass().getName()+".useInstant")

is

"false"

or

"0"

, the old formatting will be restored.

---

### Method Details

#### public
String
format​(
LogRecord
record)

Format the given message to XML.

This method can be overridden in a subclass.
It is recommended to use the

Formatter.formatMessage(java.util.logging.LogRecord)

convenience method to localize and format the message field.

**Specified by:**
- format

in class

Formatter

**Parameters:**
- record

- the log record to be formatted.

**Returns:**
- a formatted log record

---

#### public
String
getHead​(
Handler
h)

Return the header string for a set of XML formatted records.

**Overrides:**
- getHead

in class

Formatter

**Parameters:**
- h

- The target handler (can be null)

**Returns:**
- a valid XML string

---

#### public
String
getTail​(
Handler
h)

Return the tail string for a set of XML formatted records.

**Overrides:**
- getTail

in class

Formatter

**Parameters:**
- h

- The target handler (can be null)

**Returns:**
- a valid XML string

---

### Additional Sections

#### Class XMLFormatter

java.lang.Object

- java.util.logging.Formatter
- - java.util.logging.XMLFormatter

java.util.logging.Formatter

- java.util.logging.XMLFormatter

java.util.logging.XMLFormatter

```java
public class
XMLFormatter

extends
Formatter
```

Format a LogRecord into a standard XML format.

The DTD specification is provided as Appendix A to the
Java Logging APIs specification.

The XMLFormatter can be used with arbitrary character encodings,
but it is recommended that it normally be used with UTF-8. The
character encoding can be set on the output Handler.

**Implementation Requirements:** Since JDK 9, instances of

LogRecord

contain
an

Instant

which can have nanoseconds below
the millisecond resolution.
The DTD specification has been updated to allow for an optional

<nanos>

element. By default, the XMLFormatter will compute the
nanosecond adjustment below the millisecond resolution (using

LogRecord.getInstant().getNano() % 1000_000

) - and if this is not 0,
this adjustment value will be printed in the new

<nanos>

element.
The event instant can then be reconstructed using

Instant.ofEpochSecond(millis/1000L, (millis % 1000L) * 1000_000L + nanos)

where

millis

and

nanos

represent the numbers serialized in
the

<millis>

and

<nanos>

elements, respectively.

The

<date>

element will now contain the whole instant as formatted
by the

DateTimeFormatter.ISO_INSTANT

formatter.

For compatibility with old parsers, XMLFormatters can
be configured to revert to the old format by specifying a

<xml-formatter-fully-qualified-class-name>.useInstant = false

property

in the
logging configuration. When

useInstant

is

false

, the old
formatting will be preserved. When

useInstant

is

true

(the default), the

<nanos>

element will be printed and the

<date>

element will contain the

formatted

instant.

For instance, in order to configure plain instances of XMLFormatter to omit
the new

<nano>

element,

java.util.logging.XMLFormatter.useInstant = false

can be specified
in the logging configuration.
**Since:** 1.4

public class

XMLFormatter

extends

Formatter

Format a LogRecord into a standard XML format.

The DTD specification is provided as Appendix A to the
Java Logging APIs specification.

The XMLFormatter can be used with arbitrary character encodings,
but it is recommended that it normally be used with UTF-8. The
character encoding can be set on the output Handler.

The DTD specification is provided as Appendix A to the
Java Logging APIs specification.

The XMLFormatter can be used with arbitrary character encodings,
but it is recommended that it normally be used with UTF-8. The
character encoding can be set on the output Handler.

The XMLFormatter can be used with arbitrary character encodings,
but it is recommended that it normally be used with UTF-8. The
character encoding can be set on the output Handler.

For compatibility with old parsers, XMLFormatters can
be configured to revert to the old format by specifying a

<xml-formatter-fully-qualified-class-name>.useInstant = false

property

in the
logging configuration. When

useInstant

is

false

, the old
formatting will be preserved. When

useInstant

is

true

(the default), the

<nanos>

element will be printed and the

<date>

element will contain the

formatted

instant.

For instance, in order to configure plain instances of XMLFormatter to omit
the new

<nano>

element,

java.util.logging.XMLFormatter.useInstant = false

can be specified
in the logging configuration.

For instance, in order to configure plain instances of XMLFormatter to omit
the new

<nano>

element,

java.util.logging.XMLFormatter.useInstant = false

can be specified
in the logging configuration.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

XMLFormatter

()

Creates a new instance of XMLFormatter.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

String

format

​(

LogRecord

record)

Format the given message to XML.

String

getHead

​(

Handler

h)

Return the header string for a set of XML formatted records.

String

getTail

​(

Handler

h)

Return the tail string for a set of XML formatted records.

- Methods declared in class java.util.logging.

Formatter

formatMessage

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

XMLFormatter

()

Creates a new instance of XMLFormatter.

---

#### Constructor Summary

Creates a new instance of XMLFormatter.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

String

format

​(

LogRecord

record)

Format the given message to XML.

String

getHead

​(

Handler

h)

Return the header string for a set of XML formatted records.

String

getTail

​(

Handler

h)

Return the tail string for a set of XML formatted records.

- Methods declared in class java.util.logging.

Formatter

formatMessage

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

Format the given message to XML.

Return the header string for a set of XML formatted records.

Return the tail string for a set of XML formatted records.

Methods declared in class java.util.logging.

Formatter

formatMessage

---

#### Methods declared in class java.util.logging. Formatter

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

- XMLFormatter

```java
public XMLFormatter()
```

Creates a new instance of XMLFormatter.

**Implementation Requirements:** Since JDK 9, the XMLFormatter will print out the record

event time

as an Instant. This instant
has the best resolution available on the system. The

<date>

element will contain the instant as formatted by the

DateTimeFormatter.ISO_INSTANT

.
In addition, an optional

<nanos>

element containing a
nanosecond adjustment will be printed if the instant contains some
nanoseconds below the millisecond resolution.

This new behavior can be turned off, and the old formatting restored,
by specifying a property in the

logging configuration

.
If

LogManager.getLogManager().getProperty(
this.getClass().getName()+".useInstant")

is

"false"

or

"0"

, the old formatting will be restored.

============ METHOD DETAIL ==========

- Method Detail

- format

```java
public
String
format​(
LogRecord
record)
```

Format the given message to XML.

This method can be overridden in a subclass.
It is recommended to use the

Formatter.formatMessage(java.util.logging.LogRecord)

convenience method to localize and format the message field.

**Specified by:** format

in class

Formatter
**Parameters:** record

- the log record to be formatted.
**Returns:** a formatted log record

- getHead

```java
public
String
getHead​(
Handler
h)
```

Return the header string for a set of XML formatted records.

**Overrides:** getHead

in class

Formatter
**Parameters:** h

- The target handler (can be null)
**Returns:** a valid XML string

- getTail

```java
public
String
getTail​(
Handler
h)
```

Return the tail string for a set of XML formatted records.

**Overrides:** getTail

in class

Formatter
**Parameters:** h

- The target handler (can be null)
**Returns:** a valid XML string

Constructor Detail

- XMLFormatter

```java
public XMLFormatter()
```

Creates a new instance of XMLFormatter.

**Implementation Requirements:** Since JDK 9, the XMLFormatter will print out the record

event time

as an Instant. This instant
has the best resolution available on the system. The

<date>

element will contain the instant as formatted by the

DateTimeFormatter.ISO_INSTANT

.
In addition, an optional

<nanos>

element containing a
nanosecond adjustment will be printed if the instant contains some
nanoseconds below the millisecond resolution.

This new behavior can be turned off, and the old formatting restored,
by specifying a property in the

logging configuration

.
If

LogManager.getLogManager().getProperty(
this.getClass().getName()+".useInstant")

is

"false"

or

"0"

, the old formatting will be restored.

---

#### Constructor Detail

XMLFormatter

```java
public XMLFormatter()
```

Creates a new instance of XMLFormatter.

**Implementation Requirements:** Since JDK 9, the XMLFormatter will print out the record

event time

as an Instant. This instant
has the best resolution available on the system. The

<date>

element will contain the instant as formatted by the

DateTimeFormatter.ISO_INSTANT

.
In addition, an optional

<nanos>

element containing a
nanosecond adjustment will be printed if the instant contains some
nanoseconds below the millisecond resolution.

This new behavior can be turned off, and the old formatting restored,
by specifying a property in the

logging configuration

.
If

LogManager.getLogManager().getProperty(
this.getClass().getName()+".useInstant")

is

"false"

or

"0"

, the old formatting will be restored.

---

#### XMLFormatter

public XMLFormatter()

Creates a new instance of XMLFormatter.

This new behavior can be turned off, and the old formatting restored,
by specifying a property in the

logging configuration

.
If

LogManager.getLogManager().getProperty(
this.getClass().getName()+".useInstant")

is

"false"

or

"0"

, the old formatting will be restored.

Method Detail

- format

```java
public
String
format​(
LogRecord
record)
```

Format the given message to XML.

This method can be overridden in a subclass.
It is recommended to use the

Formatter.formatMessage(java.util.logging.LogRecord)

convenience method to localize and format the message field.

**Specified by:** format

in class

Formatter
**Parameters:** record

- the log record to be formatted.
**Returns:** a formatted log record

- getHead

```java
public
String
getHead​(
Handler
h)
```

Return the header string for a set of XML formatted records.

**Overrides:** getHead

in class

Formatter
**Parameters:** h

- The target handler (can be null)
**Returns:** a valid XML string

- getTail

```java
public
String
getTail​(
Handler
h)
```

Return the tail string for a set of XML formatted records.

**Overrides:** getTail

in class

Formatter
**Parameters:** h

- The target handler (can be null)
**Returns:** a valid XML string

---

#### Method Detail

format

```java
public
String
format​(
LogRecord
record)
```

Format the given message to XML.

This method can be overridden in a subclass.
It is recommended to use the

Formatter.formatMessage(java.util.logging.LogRecord)

convenience method to localize and format the message field.

**Specified by:** format

in class

Formatter
**Parameters:** record

- the log record to be formatted.
**Returns:** a formatted log record

---

#### format

public

String

format​(

LogRecord

record)

Format the given message to XML.

This method can be overridden in a subclass.
It is recommended to use the

Formatter.formatMessage(java.util.logging.LogRecord)

convenience method to localize and format the message field.

This method can be overridden in a subclass.
It is recommended to use the

Formatter.formatMessage(java.util.logging.LogRecord)

convenience method to localize and format the message field.

getHead

```java
public
String
getHead​(
Handler
h)
```

Return the header string for a set of XML formatted records.

**Overrides:** getHead

in class

Formatter
**Parameters:** h

- The target handler (can be null)
**Returns:** a valid XML string

---

#### getHead

public

String

getHead​(

Handler

h)

Return the header string for a set of XML formatted records.

getTail

```java
public
String
getTail​(
Handler
h)
```

Return the tail string for a set of XML formatted records.

**Overrides:** getTail

in class

Formatter
**Parameters:** h

- The target handler (can be null)
**Returns:** a valid XML string

---

#### getTail

public

String

getTail​(

Handler

h)

Return the tail string for a set of XML formatted records.

---

