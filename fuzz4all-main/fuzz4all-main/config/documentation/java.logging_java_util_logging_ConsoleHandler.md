# Class ConsoleHandler

**Source:** `java.logging\java\util\logging\ConsoleHandler.html`

### Class Description

```java
public class
ConsoleHandler

extends
StreamHandler
```

This

Handler

publishes log records to

System.err

.
By default the

SimpleFormatter

is used to generate brief summaries.

Configuration:

By default each

ConsoleHandler

is initialized using the following

LogManager

configuration properties where

<handler-name>

refers to the fully-qualified class name of the handler.
If properties are not defined
(or have invalid values) then the specified default values are used.

- <handler-name>.level
specifies the default level for the

Handler

(defaults to

Level.INFO

).
- <handler-name>.filter
specifies the name of a

Filter

class to use
(defaults to no

Filter

).
- <handler-name>.formatter
specifies the name of a

Formatter

class to use
(defaults to

java.util.logging.SimpleFormatter

).
- <handler-name>.encoding
the name of the character set encoding to use (defaults to
the default platform encoding).

For example, the properties for

ConsoleHandler

would be:

- java.util.logging.ConsoleHandler.level=INFO
- java.util.logging.ConsoleHandler.formatter=java.util.logging.SimpleFormatter

For a custom handler, e.g. com.foo.MyHandler, the properties would be:

- com.foo.MyHandler.level=INFO
- com.foo.MyHandler.formatter=java.util.logging.SimpleFormatter

**Since:** 1.4

---

### Field Details

*No entries found.*

### Constructor Details

#### public ConsoleHandler()

Create a

ConsoleHandler

for

System.err

.

The

ConsoleHandler

is configured based on

LogManager

properties (or their default values).

---

### Method Details

#### public void publish​(
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

**Overrides:**
- publish

in class

StreamHandler

**Parameters:**
- record

- description of the log event. A null record is
silently ignored and is not published

---

#### public void close()

Override

StreamHandler.close

to do a flush but not
to close the output stream. That is, we do

not

close

System.err

.

**Overrides:**
- close

in class

StreamHandler

---

### Additional Sections

#### Class ConsoleHandler

java.lang.Object

- java.util.logging.Handler
- - java.util.logging.StreamHandler
- - java.util.logging.ConsoleHandler

java.util.logging.Handler

- java.util.logging.StreamHandler
- - java.util.logging.ConsoleHandler

java.util.logging.StreamHandler

- java.util.logging.ConsoleHandler

java.util.logging.ConsoleHandler

```java
public class
ConsoleHandler

extends
StreamHandler
```

This

Handler

publishes log records to

System.err

.
By default the

SimpleFormatter

is used to generate brief summaries.

Configuration:

By default each

ConsoleHandler

is initialized using the following

LogManager

configuration properties where

<handler-name>

refers to the fully-qualified class name of the handler.
If properties are not defined
(or have invalid values) then the specified default values are used.

- <handler-name>.level
specifies the default level for the

Handler

(defaults to

Level.INFO

).
- <handler-name>.filter
specifies the name of a

Filter

class to use
(defaults to no

Filter

).
- <handler-name>.formatter
specifies the name of a

Formatter

class to use
(defaults to

java.util.logging.SimpleFormatter

).
- <handler-name>.encoding
the name of the character set encoding to use (defaults to
the default platform encoding).

For example, the properties for

ConsoleHandler

would be:

- java.util.logging.ConsoleHandler.level=INFO
- java.util.logging.ConsoleHandler.formatter=java.util.logging.SimpleFormatter

For a custom handler, e.g. com.foo.MyHandler, the properties would be:

- com.foo.MyHandler.level=INFO
- com.foo.MyHandler.formatter=java.util.logging.SimpleFormatter

**Since:** 1.4

public class

ConsoleHandler

extends

StreamHandler

This

Handler

publishes log records to

System.err

.
By default the

SimpleFormatter

is used to generate brief summaries.

Configuration:

By default each

ConsoleHandler

is initialized using the following

LogManager

configuration properties where

<handler-name>

refers to the fully-qualified class name of the handler.
If properties are not defined
(or have invalid values) then the specified default values are used.

- <handler-name>.level
specifies the default level for the

Handler

(defaults to

Level.INFO

).
- <handler-name>.filter
specifies the name of a

Filter

class to use
(defaults to no

Filter

).
- <handler-name>.formatter
specifies the name of a

Formatter

class to use
(defaults to

java.util.logging.SimpleFormatter

).
- <handler-name>.encoding
the name of the character set encoding to use (defaults to
the default platform encoding).

For example, the properties for

ConsoleHandler

would be:

- java.util.logging.ConsoleHandler.level=INFO
- java.util.logging.ConsoleHandler.formatter=java.util.logging.SimpleFormatter

For a custom handler, e.g. com.foo.MyHandler, the properties would be:

- com.foo.MyHandler.level=INFO
- com.foo.MyHandler.formatter=java.util.logging.SimpleFormatter

Configuration:

By default each

ConsoleHandler

is initialized using the following

LogManager

configuration properties where

<handler-name>

refers to the fully-qualified class name of the handler.
If properties are not defined
(or have invalid values) then the specified default values are used.

- <handler-name>.level
specifies the default level for the

Handler

(defaults to

Level.INFO

).
- <handler-name>.filter
specifies the name of a

Filter

class to use
(defaults to no

Filter

).
- <handler-name>.formatter
specifies the name of a

Formatter

class to use
(defaults to

java.util.logging.SimpleFormatter

).
- <handler-name>.encoding
the name of the character set encoding to use (defaults to
the default platform encoding).

For example, the properties for

ConsoleHandler

would be:

- java.util.logging.ConsoleHandler.level=INFO
- java.util.logging.ConsoleHandler.formatter=java.util.logging.SimpleFormatter

For a custom handler, e.g. com.foo.MyHandler, the properties would be:

- com.foo.MyHandler.level=INFO
- com.foo.MyHandler.formatter=java.util.logging.SimpleFormatter

<handler-name>.level
specifies the default level for the

Handler

(defaults to

Level.INFO

).

<handler-name>.filter
specifies the name of a

Filter

class to use
(defaults to no

Filter

).

<handler-name>.formatter
specifies the name of a

Formatter

class to use
(defaults to

java.util.logging.SimpleFormatter

).

<handler-name>.encoding
the name of the character set encoding to use (defaults to
the default platform encoding).

For example, the properties for

ConsoleHandler

would be:

- java.util.logging.ConsoleHandler.level=INFO
- java.util.logging.ConsoleHandler.formatter=java.util.logging.SimpleFormatter

For a custom handler, e.g. com.foo.MyHandler, the properties would be:

- com.foo.MyHandler.level=INFO
- com.foo.MyHandler.formatter=java.util.logging.SimpleFormatter

java.util.logging.ConsoleHandler.level=INFO

java.util.logging.ConsoleHandler.formatter=java.util.logging.SimpleFormatter

For a custom handler, e.g. com.foo.MyHandler, the properties would be:

- com.foo.MyHandler.level=INFO
- com.foo.MyHandler.formatter=java.util.logging.SimpleFormatter

com.foo.MyHandler.level=INFO

com.foo.MyHandler.formatter=java.util.logging.SimpleFormatter

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

ConsoleHandler

()

Create a

ConsoleHandler

for

System.err

.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

close

()

Override

StreamHandler.close

to do a flush but not
to close the output stream.

void

publish

​(

LogRecord

record)

Publish a

LogRecord

.

- Methods declared in class java.util.logging.

StreamHandler

flush

,

isLoggable

,

setEncoding

,

setOutputStream

- Methods declared in class java.util.logging.

Handler

getEncoding

,

getErrorManager

,

getFilter

,

getFormatter

,

getLevel

,

reportError

,

setErrorManager

,

setFilter

,

setFormatter

,

setLevel

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

ConsoleHandler

()

Create a

ConsoleHandler

for

System.err

.

---

#### Constructor Summary

Create a

ConsoleHandler

for

System.err

.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

close

()

Override

StreamHandler.close

to do a flush but not
to close the output stream.

void

publish

​(

LogRecord

record)

Publish a

LogRecord

.

- Methods declared in class java.util.logging.

StreamHandler

flush

,

isLoggable

,

setEncoding

,

setOutputStream

- Methods declared in class java.util.logging.

Handler

getEncoding

,

getErrorManager

,

getFilter

,

getFormatter

,

getLevel

,

reportError

,

setErrorManager

,

setFilter

,

setFormatter

,

setLevel

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

Override

StreamHandler.close

to do a flush but not
to close the output stream.

Publish a

LogRecord

.

Methods declared in class java.util.logging.

StreamHandler

flush

,

isLoggable

,

setEncoding

,

setOutputStream

---

#### Methods declared in class java.util.logging. StreamHandler

Methods declared in class java.util.logging.

Handler

getEncoding

,

getErrorManager

,

getFilter

,

getFormatter

,

getLevel

,

reportError

,

setErrorManager

,

setFilter

,

setFormatter

,

setLevel

---

#### Methods declared in class java.util.logging. Handler

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

- ConsoleHandler

```java
public ConsoleHandler()
```

Create a

ConsoleHandler

for

System.err

.

The

ConsoleHandler

is configured based on

LogManager

properties (or their default values).

============ METHOD DETAIL ==========

- Method Detail

- publish

```java
public void publish​(
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

**Overrides:** publish

in class

StreamHandler
**Parameters:** record

- description of the log event. A null record is
silently ignored and is not published

- close

```java
public void close()
```

Override

StreamHandler.close

to do a flush but not
to close the output stream. That is, we do

not

close

System.err

.

**Overrides:** close

in class

StreamHandler

Constructor Detail

- ConsoleHandler

```java
public ConsoleHandler()
```

Create a

ConsoleHandler

for

System.err

.

The

ConsoleHandler

is configured based on

LogManager

properties (or their default values).

---

#### Constructor Detail

ConsoleHandler

```java
public ConsoleHandler()
```

Create a

ConsoleHandler

for

System.err

.

The

ConsoleHandler

is configured based on

LogManager

properties (or their default values).

---

#### ConsoleHandler

public ConsoleHandler()

Create a

ConsoleHandler

for

System.err

.

The

ConsoleHandler

is configured based on

LogManager

properties (or their default values).

The

ConsoleHandler

is configured based on

LogManager

properties (or their default values).

Method Detail

- publish

```java
public void publish​(
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

**Overrides:** publish

in class

StreamHandler
**Parameters:** record

- description of the log event. A null record is
silently ignored and is not published

- close

```java
public void close()
```

Override

StreamHandler.close

to do a flush but not
to close the output stream. That is, we do

not

close

System.err

.

**Overrides:** close

in class

StreamHandler

---

#### Method Detail

publish

```java
public void publish​(
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

**Overrides:** publish

in class

StreamHandler
**Parameters:** record

- description of the log event. A null record is
silently ignored and is not published

---

#### publish

public void publish​(

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

The logging request was made initially to a

Logger

object,
which initialized the

LogRecord

and forwarded it here.

close

```java
public void close()
```

Override

StreamHandler.close

to do a flush but not
to close the output stream. That is, we do

not

close

System.err

.

**Overrides:** close

in class

StreamHandler

---

#### close

public void close()

Override

StreamHandler.close

to do a flush but not
to close the output stream. That is, we do

not

close

System.err

.

---

