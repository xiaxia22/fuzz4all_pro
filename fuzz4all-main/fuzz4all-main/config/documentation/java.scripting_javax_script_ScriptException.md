# Class ScriptException

**Source:** `java.scripting\javax\script\ScriptException.html`

### Class Description

```java
public class
ScriptException

extends
Exception
```

The generic

Exception

class for the Scripting APIs. Checked
exception types thrown by underlying scripting implementations must be wrapped in instances of

ScriptException

. The class has members to store line and column numbers and
filenames if this information is available.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public ScriptException​(
String
s)

Creates a

ScriptException

with a String to be used in its message.
Filename, and line and column numbers are unspecified.

**Parameters:**
- s

- The String to use in the message.

---

#### public ScriptException​(
Exception
e)

Creates a

ScriptException

wrapping an

Exception

thrown by an underlying
interpreter. Line and column numbers and filename are unspecified.

**Parameters:**
- e

- The wrapped

Exception

.

---

#### public ScriptException​(
String
message,

String
fileName,
int lineNumber)

Creates a

ScriptException

with message, filename and linenumber to
be used in error messages.

**Parameters:**
- message

- The string to use in the message
- fileName

- The file or resource name describing the location of a script error
causing the

ScriptException

to be thrown.
- lineNumber

- A line number describing the location of a script error causing
the

ScriptException

to be thrown.

---

#### public ScriptException​(
String
message,

String
fileName,
int lineNumber,
int columnNumber)

ScriptException

constructor specifying message, filename, line number
and column number.

**Parameters:**
- message

- The message.
- fileName

- The filename
- lineNumber

- the line number.
- columnNumber

- the column number.

---

### Method Details

#### public
String
getMessage()

Returns a message containing the String passed to a constructor as well as
line and column numbers and filename if any of these are known.

**Overrides:**
- getMessage

in class

Throwable

**Returns:**
- The error message.

---

#### public int getLineNumber()

Get the line number on which an error occurred.

**Returns:**
- The line number. Returns -1 if a line number is unavailable.

---

#### public int getColumnNumber()

Get the column number on which an error occurred.

**Returns:**
- The column number. Returns -1 if a column number is unavailable.

---

#### public
String
getFileName()

Get the source of the script causing the error.

**Returns:**
- The file name of the script or some other string describing the script
source. May return some implementation-defined string such as

<unknown>

if a description of the source is unavailable.

---

### Additional Sections

#### Class ScriptException

java.lang.Object

- java.lang.Throwable
- - java.lang.Exception
- - javax.script.ScriptException

java.lang.Throwable

- java.lang.Exception
- - javax.script.ScriptException

java.lang.Exception

- javax.script.ScriptException

javax.script.ScriptException

**All Implemented Interfaces:** Serializable

```java
public class
ScriptException

extends
Exception
```

The generic

Exception

class for the Scripting APIs. Checked
exception types thrown by underlying scripting implementations must be wrapped in instances of

ScriptException

. The class has members to store line and column numbers and
filenames if this information is available.

**Since:** 1.6
**See Also:** Serialized Form

public class

ScriptException

extends

Exception

The generic

Exception

class for the Scripting APIs. Checked
exception types thrown by underlying scripting implementations must be wrapped in instances of

ScriptException

. The class has members to store line and column numbers and
filenames if this information is available.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

ScriptException

​(

Exception

e)

Creates a

ScriptException

wrapping an

Exception

thrown by an underlying
interpreter.

ScriptException

​(

String

s)

Creates a

ScriptException

with a String to be used in its message.

ScriptException

​(

String

message,

String

fileName,
int lineNumber)

Creates a

ScriptException

with message, filename and linenumber to
be used in error messages.

ScriptException

​(

String

message,

String

fileName,
int lineNumber,
int columnNumber)

ScriptException

constructor specifying message, filename, line number
and column number.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

int

getColumnNumber

()

Get the column number on which an error occurred.

String

getFileName

()

Get the source of the script causing the error.

int

getLineNumber

()

Get the line number on which an error occurred.

String

getMessage

()

Returns a message containing the String passed to a constructor as well as
line and column numbers and filename if any of these are known.

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

ScriptException

​(

Exception

e)

Creates a

ScriptException

wrapping an

Exception

thrown by an underlying
interpreter.

ScriptException

​(

String

s)

Creates a

ScriptException

with a String to be used in its message.

ScriptException

​(

String

message,

String

fileName,
int lineNumber)

Creates a

ScriptException

with message, filename and linenumber to
be used in error messages.

ScriptException

​(

String

message,

String

fileName,
int lineNumber,
int columnNumber)

ScriptException

constructor specifying message, filename, line number
and column number.

---

#### Constructor Summary

Creates a

ScriptException

wrapping an

Exception

thrown by an underlying
interpreter.

Creates a

ScriptException

with a String to be used in its message.

Creates a

ScriptException

with message, filename and linenumber to
be used in error messages.

ScriptException

constructor specifying message, filename, line number
and column number.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

int

getColumnNumber

()

Get the column number on which an error occurred.

String

getFileName

()

Get the source of the script causing the error.

int

getLineNumber

()

Get the line number on which an error occurred.

String

getMessage

()

Returns a message containing the String passed to a constructor as well as
line and column numbers and filename if any of these are known.

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

Get the column number on which an error occurred.

Get the source of the script causing the error.

Get the line number on which an error occurred.

Returns a message containing the String passed to a constructor as well as
line and column numbers and filename if any of these are known.

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

- ScriptException

```java
public ScriptException​(
String
s)
```

Creates a

ScriptException

with a String to be used in its message.
Filename, and line and column numbers are unspecified.

**Parameters:** s

- The String to use in the message.

- ScriptException

```java
public ScriptException​(
Exception
e)
```

Creates a

ScriptException

wrapping an

Exception

thrown by an underlying
interpreter. Line and column numbers and filename are unspecified.

**Parameters:** e

- The wrapped

Exception

.

- ScriptException

```java
public ScriptException​(
String
message,

String
fileName,
int lineNumber)
```

Creates a

ScriptException

with message, filename and linenumber to
be used in error messages.

**Parameters:** message

- The string to use in the message
**Parameters:** fileName

- The file or resource name describing the location of a script error
causing the

ScriptException

to be thrown.
**Parameters:** lineNumber

- A line number describing the location of a script error causing
the

ScriptException

to be thrown.

- ScriptException

```java
public ScriptException​(
String
message,

String
fileName,
int lineNumber,
int columnNumber)
```

ScriptException

constructor specifying message, filename, line number
and column number.

**Parameters:** message

- The message.
**Parameters:** fileName

- The filename
**Parameters:** lineNumber

- the line number.
**Parameters:** columnNumber

- the column number.

============ METHOD DETAIL ==========

- Method Detail

- getMessage

```java
public
String
getMessage()
```

Returns a message containing the String passed to a constructor as well as
line and column numbers and filename if any of these are known.

**Overrides:** getMessage

in class

Throwable
**Returns:** The error message.

- getLineNumber

```java
public int getLineNumber()
```

Get the line number on which an error occurred.

**Returns:** The line number. Returns -1 if a line number is unavailable.

- getColumnNumber

```java
public int getColumnNumber()
```

Get the column number on which an error occurred.

**Returns:** The column number. Returns -1 if a column number is unavailable.

- getFileName

```java
public
String
getFileName()
```

Get the source of the script causing the error.

**Returns:** The file name of the script or some other string describing the script
source. May return some implementation-defined string such as

<unknown>

if a description of the source is unavailable.

Constructor Detail

- ScriptException

```java
public ScriptException​(
String
s)
```

Creates a

ScriptException

with a String to be used in its message.
Filename, and line and column numbers are unspecified.

**Parameters:** s

- The String to use in the message.

- ScriptException

```java
public ScriptException​(
Exception
e)
```

Creates a

ScriptException

wrapping an

Exception

thrown by an underlying
interpreter. Line and column numbers and filename are unspecified.

**Parameters:** e

- The wrapped

Exception

.

- ScriptException

```java
public ScriptException​(
String
message,

String
fileName,
int lineNumber)
```

Creates a

ScriptException

with message, filename and linenumber to
be used in error messages.

**Parameters:** message

- The string to use in the message
**Parameters:** fileName

- The file or resource name describing the location of a script error
causing the

ScriptException

to be thrown.
**Parameters:** lineNumber

- A line number describing the location of a script error causing
the

ScriptException

to be thrown.

- ScriptException

```java
public ScriptException​(
String
message,

String
fileName,
int lineNumber,
int columnNumber)
```

ScriptException

constructor specifying message, filename, line number
and column number.

**Parameters:** message

- The message.
**Parameters:** fileName

- The filename
**Parameters:** lineNumber

- the line number.
**Parameters:** columnNumber

- the column number.

---

#### Constructor Detail

ScriptException

```java
public ScriptException​(
String
s)
```

Creates a

ScriptException

with a String to be used in its message.
Filename, and line and column numbers are unspecified.

**Parameters:** s

- The String to use in the message.

---

#### ScriptException

public ScriptException​(

String

s)

Creates a

ScriptException

with a String to be used in its message.
Filename, and line and column numbers are unspecified.

ScriptException

```java
public ScriptException​(
Exception
e)
```

Creates a

ScriptException

wrapping an

Exception

thrown by an underlying
interpreter. Line and column numbers and filename are unspecified.

**Parameters:** e

- The wrapped

Exception

.

---

#### ScriptException

public ScriptException​(

Exception

e)

Creates a

ScriptException

wrapping an

Exception

thrown by an underlying
interpreter. Line and column numbers and filename are unspecified.

ScriptException

```java
public ScriptException​(
String
message,

String
fileName,
int lineNumber)
```

Creates a

ScriptException

with message, filename and linenumber to
be used in error messages.

**Parameters:** message

- The string to use in the message
**Parameters:** fileName

- The file or resource name describing the location of a script error
causing the

ScriptException

to be thrown.
**Parameters:** lineNumber

- A line number describing the location of a script error causing
the

ScriptException

to be thrown.

---

#### ScriptException

public ScriptException​(

String

message,

String

fileName,
int lineNumber)

Creates a

ScriptException

with message, filename and linenumber to
be used in error messages.

ScriptException

```java
public ScriptException​(
String
message,

String
fileName,
int lineNumber,
int columnNumber)
```

ScriptException

constructor specifying message, filename, line number
and column number.

**Parameters:** message

- The message.
**Parameters:** fileName

- The filename
**Parameters:** lineNumber

- the line number.
**Parameters:** columnNumber

- the column number.

---

#### ScriptException

public ScriptException​(

String

message,

String

fileName,
int lineNumber,
int columnNumber)

ScriptException

constructor specifying message, filename, line number
and column number.

Method Detail

- getMessage

```java
public
String
getMessage()
```

Returns a message containing the String passed to a constructor as well as
line and column numbers and filename if any of these are known.

**Overrides:** getMessage

in class

Throwable
**Returns:** The error message.

- getLineNumber

```java
public int getLineNumber()
```

Get the line number on which an error occurred.

**Returns:** The line number. Returns -1 if a line number is unavailable.

- getColumnNumber

```java
public int getColumnNumber()
```

Get the column number on which an error occurred.

**Returns:** The column number. Returns -1 if a column number is unavailable.

- getFileName

```java
public
String
getFileName()
```

Get the source of the script causing the error.

**Returns:** The file name of the script or some other string describing the script
source. May return some implementation-defined string such as

<unknown>

if a description of the source is unavailable.

---

#### Method Detail

getMessage

```java
public
String
getMessage()
```

Returns a message containing the String passed to a constructor as well as
line and column numbers and filename if any of these are known.

**Overrides:** getMessage

in class

Throwable
**Returns:** The error message.

---

#### getMessage

public

String

getMessage()

Returns a message containing the String passed to a constructor as well as
line and column numbers and filename if any of these are known.

getLineNumber

```java
public int getLineNumber()
```

Get the line number on which an error occurred.

**Returns:** The line number. Returns -1 if a line number is unavailable.

---

#### getLineNumber

public int getLineNumber()

Get the line number on which an error occurred.

getColumnNumber

```java
public int getColumnNumber()
```

Get the column number on which an error occurred.

**Returns:** The column number. Returns -1 if a column number is unavailable.

---

#### getColumnNumber

public int getColumnNumber()

Get the column number on which an error occurred.

getFileName

```java
public
String
getFileName()
```

Get the source of the script causing the error.

**Returns:** The file name of the script or some other string describing the script
source. May return some implementation-defined string such as

<unknown>

if a description of the source is unavailable.

---

#### getFileName

public

String

getFileName()

Get the source of the script causing the error.

---

