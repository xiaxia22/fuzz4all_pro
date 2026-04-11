# Class ParseException

**Source:** `java.base\java\text\ParseException.html`

### Class Description

```java
public class
ParseException

extends
Exception
```

Signals that an error has been reached unexpectedly
while parsing.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public ParseException​(
String
s,
int errorOffset)

Constructs a ParseException with the specified detail message and
offset.
A detail message is a String that describes this particular exception.

**Parameters:**
- s

- the detail message
- errorOffset

- the position where the error is found while parsing.

---

### Method Details

#### public int getErrorOffset()

Returns the position where the error was found.

**Returns:**
- the position where the error was found

---

### Additional Sections

#### Class ParseException

java.lang.Object

- java.lang.Throwable
- - java.lang.Exception
- - java.text.ParseException

java.lang.Throwable

- java.lang.Exception
- - java.text.ParseException

java.lang.Exception

- java.text.ParseException

java.text.ParseException

**All Implemented Interfaces:** Serializable

```java
public class
ParseException

extends
Exception
```

Signals that an error has been reached unexpectedly
while parsing.

**Since:** 1.1
**See Also:** Exception

,

Format

,

FieldPosition

,

Serialized Form

public class

ParseException

extends

Exception

Signals that an error has been reached unexpectedly
while parsing.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

ParseException

​(

String

s,
int errorOffset)

Constructs a ParseException with the specified detail message and
offset.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

int

getErrorOffset

()

Returns the position where the error was found.

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

ParseException

​(

String

s,
int errorOffset)

Constructs a ParseException with the specified detail message and
offset.

---

#### Constructor Summary

Constructs a ParseException with the specified detail message and
offset.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

int

getErrorOffset

()

Returns the position where the error was found.

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

Returns the position where the error was found.

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

- ParseException

```java
public ParseException​(
String
s,
int errorOffset)
```

Constructs a ParseException with the specified detail message and
offset.
A detail message is a String that describes this particular exception.

**Parameters:** s

- the detail message
**Parameters:** errorOffset

- the position where the error is found while parsing.

============ METHOD DETAIL ==========

- Method Detail

- getErrorOffset

```java
public int getErrorOffset()
```

Returns the position where the error was found.

**Returns:** the position where the error was found

Constructor Detail

- ParseException

```java
public ParseException​(
String
s,
int errorOffset)
```

Constructs a ParseException with the specified detail message and
offset.
A detail message is a String that describes this particular exception.

**Parameters:** s

- the detail message
**Parameters:** errorOffset

- the position where the error is found while parsing.

---

#### Constructor Detail

ParseException

```java
public ParseException​(
String
s,
int errorOffset)
```

Constructs a ParseException with the specified detail message and
offset.
A detail message is a String that describes this particular exception.

**Parameters:** s

- the detail message
**Parameters:** errorOffset

- the position where the error is found while parsing.

---

#### ParseException

public ParseException​(

String

s,
int errorOffset)

Constructs a ParseException with the specified detail message and
offset.
A detail message is a String that describes this particular exception.

Method Detail

- getErrorOffset

```java
public int getErrorOffset()
```

Returns the position where the error was found.

**Returns:** the position where the error was found

---

#### Method Detail

getErrorOffset

```java
public int getErrorOffset()
```

Returns the position where the error was found.

**Returns:** the position where the error was found

---

#### getErrorOffset

public int getErrorOffset()

Returns the position where the error was found.

---

