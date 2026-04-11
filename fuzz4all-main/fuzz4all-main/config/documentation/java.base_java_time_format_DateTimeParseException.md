# Class DateTimeParseException

**Source:** `java.base\java\time\format\DateTimeParseException.html`

### Class Description

```java
public class
DateTimeParseException

extends
DateTimeException
```

An exception thrown when an error occurs during parsing.

This exception includes the text being parsed and the error index.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public DateTimeParseException​(
String
message,

CharSequence
parsedData,
int errorIndex)

Constructs a new exception with the specified message.

**Parameters:**
- message

- the message to use for this exception, may be null
- parsedData

- the parsed text, should not be null
- errorIndex

- the index in the parsed string that was invalid, should be a valid index

---

#### public DateTimeParseException​(
String
message,

CharSequence
parsedData,
int errorIndex,

Throwable
cause)

Constructs a new exception with the specified message and cause.

**Parameters:**
- message

- the message to use for this exception, may be null
- parsedData

- the parsed text, should not be null
- errorIndex

- the index in the parsed string that was invalid, should be a valid index
- cause

- the cause exception, may be null

---

### Method Details

#### public
String
getParsedString()

Returns the string that was being parsed.

**Returns:**
- the string that was being parsed, should not be null.

---

#### public int getErrorIndex()

Returns the index where the error was found.

**Returns:**
- the index in the parsed string that was invalid, should be a valid index

---

### Additional Sections

#### Class DateTimeParseException

java.lang.Object

- java.lang.Throwable
- - java.lang.Exception
- - java.lang.RuntimeException
- - java.time.DateTimeException
- - java.time.format.DateTimeParseException

java.lang.Throwable

- java.lang.Exception
- - java.lang.RuntimeException
- - java.time.DateTimeException
- - java.time.format.DateTimeParseException

java.lang.Exception

- java.lang.RuntimeException
- - java.time.DateTimeException
- - java.time.format.DateTimeParseException

java.lang.RuntimeException

- java.time.DateTimeException
- - java.time.format.DateTimeParseException

java.time.DateTimeException

- java.time.format.DateTimeParseException

java.time.format.DateTimeParseException

**All Implemented Interfaces:** Serializable

```java
public class
DateTimeParseException

extends
DateTimeException
```

An exception thrown when an error occurs during parsing.

This exception includes the text being parsed and the error index.

**Implementation Requirements:** This class is intended for use in a single thread.
**Since:** 1.8
**See Also:** Serialized Form

public class

DateTimeParseException

extends

DateTimeException

An exception thrown when an error occurs during parsing.

This exception includes the text being parsed and the error index.

This exception includes the text being parsed and the error index.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

DateTimeParseException

​(

String

message,

CharSequence

parsedData,
int errorIndex)

Constructs a new exception with the specified message.

DateTimeParseException

​(

String

message,

CharSequence

parsedData,
int errorIndex,

Throwable

cause)

Constructs a new exception with the specified message and cause.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

int

getErrorIndex

()

Returns the index where the error was found.

String

getParsedString

()

Returns the string that was being parsed.

- Methods declared in class java.lang.

Throwable

addSuppressed

,

fillInStackTrace

,

getCause

,

getLocalizedMessage

,

getMessage

,

getStackTrace

,

getSuppressed

,

initCause

,

printStackTrace

,

printStackTrace

,

printStackTrace

,

setStackTrace

,

toString

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

wait

,

wait

,

wait

Constructor Summary

Constructors

Constructor

Description

DateTimeParseException

​(

String

message,

CharSequence

parsedData,
int errorIndex)

Constructs a new exception with the specified message.

DateTimeParseException

​(

String

message,

CharSequence

parsedData,
int errorIndex,

Throwable

cause)

Constructs a new exception with the specified message and cause.

---

#### Constructor Summary

Constructs a new exception with the specified message.

Constructs a new exception with the specified message and cause.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

int

getErrorIndex

()

Returns the index where the error was found.

String

getParsedString

()

Returns the string that was being parsed.

- Methods declared in class java.lang.

Throwable

addSuppressed

,

fillInStackTrace

,

getCause

,

getLocalizedMessage

,

getMessage

,

getStackTrace

,

getSuppressed

,

initCause

,

printStackTrace

,

printStackTrace

,

printStackTrace

,

setStackTrace

,

toString

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

wait

,

wait

,

wait

---

#### Method Summary

Returns the index where the error was found.

Returns the string that was being parsed.

Methods declared in class java.lang.

Throwable

addSuppressed

,

fillInStackTrace

,

getCause

,

getLocalizedMessage

,

getMessage

,

getStackTrace

,

getSuppressed

,

initCause

,

printStackTrace

,

printStackTrace

,

printStackTrace

,

setStackTrace

,

toString

---

#### Methods declared in class java.lang. Throwable

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

wait

,

wait

,

wait

---

#### Methods declared in class java.lang. Object

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- DateTimeParseException

```java
public DateTimeParseException​(
String
message,

CharSequence
parsedData,
int errorIndex)
```

Constructs a new exception with the specified message.

**Parameters:** message

- the message to use for this exception, may be null
**Parameters:** parsedData

- the parsed text, should not be null
**Parameters:** errorIndex

- the index in the parsed string that was invalid, should be a valid index

- DateTimeParseException

```java
public DateTimeParseException​(
String
message,

CharSequence
parsedData,
int errorIndex,

Throwable
cause)
```

Constructs a new exception with the specified message and cause.

**Parameters:** message

- the message to use for this exception, may be null
**Parameters:** parsedData

- the parsed text, should not be null
**Parameters:** errorIndex

- the index in the parsed string that was invalid, should be a valid index
**Parameters:** cause

- the cause exception, may be null

============ METHOD DETAIL ==========

- Method Detail

- getParsedString

```java
public
String
getParsedString()
```

Returns the string that was being parsed.

**Returns:** the string that was being parsed, should not be null.

- getErrorIndex

```java
public int getErrorIndex()
```

Returns the index where the error was found.

**Returns:** the index in the parsed string that was invalid, should be a valid index

Constructor Detail

- DateTimeParseException

```java
public DateTimeParseException​(
String
message,

CharSequence
parsedData,
int errorIndex)
```

Constructs a new exception with the specified message.

**Parameters:** message

- the message to use for this exception, may be null
**Parameters:** parsedData

- the parsed text, should not be null
**Parameters:** errorIndex

- the index in the parsed string that was invalid, should be a valid index

- DateTimeParseException

```java
public DateTimeParseException​(
String
message,

CharSequence
parsedData,
int errorIndex,

Throwable
cause)
```

Constructs a new exception with the specified message and cause.

**Parameters:** message

- the message to use for this exception, may be null
**Parameters:** parsedData

- the parsed text, should not be null
**Parameters:** errorIndex

- the index in the parsed string that was invalid, should be a valid index
**Parameters:** cause

- the cause exception, may be null

---

#### Constructor Detail

DateTimeParseException

```java
public DateTimeParseException​(
String
message,

CharSequence
parsedData,
int errorIndex)
```

Constructs a new exception with the specified message.

**Parameters:** message

- the message to use for this exception, may be null
**Parameters:** parsedData

- the parsed text, should not be null
**Parameters:** errorIndex

- the index in the parsed string that was invalid, should be a valid index

---

#### DateTimeParseException

public DateTimeParseException​(

String

message,

CharSequence

parsedData,
int errorIndex)

Constructs a new exception with the specified message.

DateTimeParseException

```java
public DateTimeParseException​(
String
message,

CharSequence
parsedData,
int errorIndex,

Throwable
cause)
```

Constructs a new exception with the specified message and cause.

**Parameters:** message

- the message to use for this exception, may be null
**Parameters:** parsedData

- the parsed text, should not be null
**Parameters:** errorIndex

- the index in the parsed string that was invalid, should be a valid index
**Parameters:** cause

- the cause exception, may be null

---

#### DateTimeParseException

public DateTimeParseException​(

String

message,

CharSequence

parsedData,
int errorIndex,

Throwable

cause)

Constructs a new exception with the specified message and cause.

Method Detail

- getParsedString

```java
public
String
getParsedString()
```

Returns the string that was being parsed.

**Returns:** the string that was being parsed, should not be null.

- getErrorIndex

```java
public int getErrorIndex()
```

Returns the index where the error was found.

**Returns:** the index in the parsed string that was invalid, should be a valid index

---

#### Method Detail

getParsedString

```java
public
String
getParsedString()
```

Returns the string that was being parsed.

**Returns:** the string that was being parsed, should not be null.

---

#### getParsedString

public

String

getParsedString()

Returns the string that was being parsed.

getErrorIndex

```java
public int getErrorIndex()
```

Returns the index where the error was found.

**Returns:** the index in the parsed string that was invalid, should be a valid index

---

#### getErrorIndex

public int getErrorIndex()

Returns the index where the error was found.

---

