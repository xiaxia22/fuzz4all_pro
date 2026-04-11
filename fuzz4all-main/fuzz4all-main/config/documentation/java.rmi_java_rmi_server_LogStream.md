# Class LogStream

**Source:** `java.rmi\java\rmi\server\LogStream.html`

### Class Description

```java
@Deprecated

public class
LogStream

extends
PrintStream
```

LogStream

provides a mechanism for logging errors that are
of possible interest to those monitoring a system.

**All Implemented Interfaces:** Closeable

,

Flushable

,

Appendable

,

AutoCloseable

---

### Field Details

#### public static final int SILENT

log level constant (no logging).

**See Also:**
- Constant Field Values

---

#### public static final int BRIEF

log level constant (brief logging).

**See Also:**
- Constant Field Values

---

#### public static final int VERBOSE

log level constant (verbose logging).

**See Also:**
- Constant Field Values

---

### Constructor Details

*No entries found.*

### Method Details

#### @Deprecated

public static
LogStream
log​(
String
name)

Return the LogStream identified by the given name. If
a log corresponding to "name" does not exist, a log using
the default stream is created.

**Parameters:**
- name

- name identifying the desired LogStream

**Returns:**
- log associated with given name

**Since:**
- 1.1

---

#### @Deprecated

public static
PrintStream
getDefaultStream()

Return the current default stream for new logs.

**Returns:**
- default log stream

**See Also:**
- setDefaultStream(java.io.PrintStream)

**Since:**
- 1.1

---

#### @Deprecated

public static void setDefaultStream​(
PrintStream
newDefault)

Set the default stream for new logs.

**Parameters:**
- newDefault

- new default log stream

**See Also:**
- getDefaultStream()

**Since:**
- 1.1

---

#### @Deprecated

public
OutputStream
getOutputStream()

Return the current stream to which output from this log is sent.

**Returns:**
- output stream for this log

**See Also:**
- setOutputStream(java.io.OutputStream)

**Since:**
- 1.1

---

#### @Deprecated

public void setOutputStream​(
OutputStream
out)

Set the stream to which output from this log is sent.

**Parameters:**
- out

- new output stream for this log

**See Also:**
- getOutputStream()

**Since:**
- 1.1

---

#### @Deprecated

public void write​(int b)

Write a byte of data to the stream. If it is not a newline, then
the byte is appended to the internal buffer. If it is a newline,
then the currently buffered line is sent to the log's output
stream, prefixed with the appropriate logging information.

**Overrides:**
- write

in class

PrintStream

**Parameters:**
- b

- The byte to be written

**See Also:**
- PrintStream.print(char)

,

PrintStream.println(char)

**Since:**
- 1.1

---

#### @Deprecated

public void write​(byte[] b,
int off,
int len)

Write a subarray of bytes. Pass each through write byte method.

**Overrides:**
- write

in class

PrintStream

**Parameters:**
- b

- A byte array
- off

- Offset from which to start taking bytes
- len

- Number of bytes to write

**See Also:**
- FilterOutputStream.write(int)

**Since:**
- 1.1

---

#### @Deprecated

public
String
toString()

Return log name as string representation.

**Overrides:**
- toString

in class

Object

**Returns:**
- log name

**Since:**
- 1.1

---

#### @Deprecated

public static int parseLevel​(
String
s)

Convert a string name of a logging level to its internal
integer representation.

**Parameters:**
- s

- name of logging level (e.g., 'SILENT', 'BRIEF', 'VERBOSE')

**Returns:**
- corresponding integer log level

**Since:**
- 1.1

---

### Additional Sections

#### Class LogStream

java.lang.Object

- java.io.OutputStream
- - java.io.FilterOutputStream
- - java.io.PrintStream
- - java.rmi.server.LogStream

java.io.OutputStream

- java.io.FilterOutputStream
- - java.io.PrintStream
- - java.rmi.server.LogStream

java.io.FilterOutputStream

- java.io.PrintStream
- - java.rmi.server.LogStream

java.io.PrintStream

- java.rmi.server.LogStream

java.rmi.server.LogStream

**All Implemented Interfaces:** Closeable

,

Flushable

,

Appendable

,

AutoCloseable

```java
@Deprecated

public class
LogStream

extends
PrintStream
```

Deprecated.

no replacement

LogStream

provides a mechanism for logging errors that are
of possible interest to those monitoring a system.

**Since:** 1.1

@Deprecated

public class

LogStream

extends

PrintStream

LogStream

provides a mechanism for logging errors that are
of possible interest to those monitoring a system.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static int

BRIEF

Deprecated.

log level constant (brief logging).

static int

SILENT

Deprecated.

log level constant (no logging).

static int

VERBOSE

Deprecated.

log level constant (verbose logging).

- Fields declared in class java.io.

FilterOutputStream

out

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Deprecated Methods

Modifier and Type

Method

Description

static

PrintStream

getDefaultStream

()

Deprecated.

no replacement

OutputStream

getOutputStream

()

Deprecated.

no replacement

static

LogStream

log

​(

String

name)

Deprecated.

no replacement

static int

parseLevel

​(

String

s)

Deprecated.

no replacement

static void

setDefaultStream

​(

PrintStream

newDefault)

Deprecated.

no replacement

void

setOutputStream

​(

OutputStream

out)

Deprecated.

no replacement

String

toString

()

Deprecated.

no replacement

void

write

​(byte[] b,
int off,
int len)

Deprecated.

no replacement

void

write

​(int b)

Deprecated.

no replacement

- Methods declared in class java.io.

PrintStream

append

,

append

,

append

,

checkError

,

clearError

,

close

,

flush

,

format

,

format

,

print

,

print

,

print

,

print

,

print

,

print

,

print

,

print

,

print

,

printf

,

printf

,

println

,

println

,

println

,

println

,

println

,

println

,

println

,

println

,

println

,

println

,

setError

- Methods declared in class java.io.

FilterOutputStream

write

- Methods declared in class java.io.

OutputStream

nullOutputStream

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

Field Summary

Fields

Modifier and Type

Field

Description

static int

BRIEF

Deprecated.

log level constant (brief logging).

static int

SILENT

Deprecated.

log level constant (no logging).

static int

VERBOSE

Deprecated.

log level constant (verbose logging).

- Fields declared in class java.io.

FilterOutputStream

out

---

#### Field Summary

Deprecated.

log level constant (brief logging).

log level constant (no logging).

log level constant (verbose logging).

Fields declared in class java.io.

FilterOutputStream

out

---

#### Fields declared in class java.io. FilterOutputStream

Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Deprecated Methods

Modifier and Type

Method

Description

static

PrintStream

getDefaultStream

()

Deprecated.

no replacement

OutputStream

getOutputStream

()

Deprecated.

no replacement

static

LogStream

log

​(

String

name)

Deprecated.

no replacement

static int

parseLevel

​(

String

s)

Deprecated.

no replacement

static void

setDefaultStream

​(

PrintStream

newDefault)

Deprecated.

no replacement

void

setOutputStream

​(

OutputStream

out)

Deprecated.

no replacement

String

toString

()

Deprecated.

no replacement

void

write

​(byte[] b,
int off,
int len)

Deprecated.

no replacement

void

write

​(int b)

Deprecated.

no replacement

- Methods declared in class java.io.

PrintStream

append

,

append

,

append

,

checkError

,

clearError

,

close

,

flush

,

format

,

format

,

print

,

print

,

print

,

print

,

print

,

print

,

print

,

print

,

print

,

printf

,

printf

,

println

,

println

,

println

,

println

,

println

,

println

,

println

,

println

,

println

,

println

,

setError

- Methods declared in class java.io.

FilterOutputStream

write

- Methods declared in class java.io.

OutputStream

nullOutputStream

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

Deprecated.

no replacement

Methods declared in class java.io.

PrintStream

append

,

append

,

append

,

checkError

,

clearError

,

close

,

flush

,

format

,

format

,

print

,

print

,

print

,

print

,

print

,

print

,

print

,

print

,

print

,

printf

,

printf

,

println

,

println

,

println

,

println

,

println

,

println

,

println

,

println

,

println

,

println

,

setError

---

#### Methods declared in class java.io. PrintStream

Methods declared in class java.io.

FilterOutputStream

write

---

#### Methods declared in class java.io. FilterOutputStream

Methods declared in class java.io.

OutputStream

nullOutputStream

---

#### Methods declared in class java.io. OutputStream

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

============ FIELD DETAIL ===========

- Field Detail

- SILENT

```java
public static final int SILENT
```

Deprecated.

log level constant (no logging).

**See Also:** Constant Field Values

- BRIEF

```java
public static final int BRIEF
```

Deprecated.

log level constant (brief logging).

**See Also:** Constant Field Values

- VERBOSE

```java
public static final int VERBOSE
```

Deprecated.

log level constant (verbose logging).

**See Also:** Constant Field Values

============ METHOD DETAIL ==========

- Method Detail

- log

```java
@Deprecated

public static
LogStream
log​(
String
name)
```

Deprecated.

no replacement

Return the LogStream identified by the given name. If
a log corresponding to "name" does not exist, a log using
the default stream is created.

**Parameters:** name

- name identifying the desired LogStream
**Returns:** log associated with given name
**Since:** 1.1

- getDefaultStream

```java
@Deprecated

public static
PrintStream
getDefaultStream()
```

Deprecated.

no replacement

Return the current default stream for new logs.

**Returns:** default log stream
**Since:** 1.1
**See Also:** setDefaultStream(java.io.PrintStream)

- setDefaultStream

```java
@Deprecated

public static void setDefaultStream​(
PrintStream
newDefault)
```

Deprecated.

no replacement

Set the default stream for new logs.

**Parameters:** newDefault

- new default log stream
**Since:** 1.1
**See Also:** getDefaultStream()

- getOutputStream

```java
@Deprecated

public
OutputStream
getOutputStream()
```

Deprecated.

no replacement

Return the current stream to which output from this log is sent.

**Returns:** output stream for this log
**Since:** 1.1
**See Also:** setOutputStream(java.io.OutputStream)

- setOutputStream

```java
@Deprecated

public void setOutputStream​(
OutputStream
out)
```

Deprecated.

no replacement

Set the stream to which output from this log is sent.

**Parameters:** out

- new output stream for this log
**Since:** 1.1
**See Also:** getOutputStream()

- write

```java
@Deprecated

public void write​(int b)
```

Deprecated.

no replacement

Write a byte of data to the stream. If it is not a newline, then
the byte is appended to the internal buffer. If it is a newline,
then the currently buffered line is sent to the log's output
stream, prefixed with the appropriate logging information.

**Overrides:** write

in class

PrintStream
**Parameters:** b

- The byte to be written
**Since:** 1.1
**See Also:** PrintStream.print(char)

,

PrintStream.println(char)

- write

```java
@Deprecated

public void write​(byte[] b,
int off,
int len)
```

Deprecated.

no replacement

Write a subarray of bytes. Pass each through write byte method.

**Overrides:** write

in class

PrintStream
**Parameters:** b

- A byte array
**Parameters:** off

- Offset from which to start taking bytes
**Parameters:** len

- Number of bytes to write
**Since:** 1.1
**See Also:** FilterOutputStream.write(int)

- toString

```java
@Deprecated

public
String
toString()
```

Deprecated.

no replacement

Return log name as string representation.

**Overrides:** toString

in class

Object
**Returns:** log name
**Since:** 1.1

- parseLevel

```java
@Deprecated

public static int parseLevel​(
String
s)
```

Deprecated.

no replacement

Convert a string name of a logging level to its internal
integer representation.

**Parameters:** s

- name of logging level (e.g., 'SILENT', 'BRIEF', 'VERBOSE')
**Returns:** corresponding integer log level
**Since:** 1.1

Field Detail

- SILENT

```java
public static final int SILENT
```

Deprecated.

log level constant (no logging).

**See Also:** Constant Field Values

- BRIEF

```java
public static final int BRIEF
```

Deprecated.

log level constant (brief logging).

**See Also:** Constant Field Values

- VERBOSE

```java
public static final int VERBOSE
```

Deprecated.

log level constant (verbose logging).

**See Also:** Constant Field Values

---

#### Field Detail

SILENT

```java
public static final int SILENT
```

Deprecated.

log level constant (no logging).

**See Also:** Constant Field Values

---

#### SILENT

public static final int SILENT

log level constant (no logging).

BRIEF

```java
public static final int BRIEF
```

Deprecated.

log level constant (brief logging).

**See Also:** Constant Field Values

---

#### BRIEF

public static final int BRIEF

log level constant (brief logging).

VERBOSE

```java
public static final int VERBOSE
```

Deprecated.

log level constant (verbose logging).

**See Also:** Constant Field Values

---

#### VERBOSE

public static final int VERBOSE

log level constant (verbose logging).

Method Detail

- log

```java
@Deprecated

public static
LogStream
log​(
String
name)
```

Deprecated.

no replacement

Return the LogStream identified by the given name. If
a log corresponding to "name" does not exist, a log using
the default stream is created.

**Parameters:** name

- name identifying the desired LogStream
**Returns:** log associated with given name
**Since:** 1.1

- getDefaultStream

```java
@Deprecated

public static
PrintStream
getDefaultStream()
```

Deprecated.

no replacement

Return the current default stream for new logs.

**Returns:** default log stream
**Since:** 1.1
**See Also:** setDefaultStream(java.io.PrintStream)

- setDefaultStream

```java
@Deprecated

public static void setDefaultStream​(
PrintStream
newDefault)
```

Deprecated.

no replacement

Set the default stream for new logs.

**Parameters:** newDefault

- new default log stream
**Since:** 1.1
**See Also:** getDefaultStream()

- getOutputStream

```java
@Deprecated

public
OutputStream
getOutputStream()
```

Deprecated.

no replacement

Return the current stream to which output from this log is sent.

**Returns:** output stream for this log
**Since:** 1.1
**See Also:** setOutputStream(java.io.OutputStream)

- setOutputStream

```java
@Deprecated

public void setOutputStream​(
OutputStream
out)
```

Deprecated.

no replacement

Set the stream to which output from this log is sent.

**Parameters:** out

- new output stream for this log
**Since:** 1.1
**See Also:** getOutputStream()

- write

```java
@Deprecated

public void write​(int b)
```

Deprecated.

no replacement

Write a byte of data to the stream. If it is not a newline, then
the byte is appended to the internal buffer. If it is a newline,
then the currently buffered line is sent to the log's output
stream, prefixed with the appropriate logging information.

**Overrides:** write

in class

PrintStream
**Parameters:** b

- The byte to be written
**Since:** 1.1
**See Also:** PrintStream.print(char)

,

PrintStream.println(char)

- write

```java
@Deprecated

public void write​(byte[] b,
int off,
int len)
```

Deprecated.

no replacement

Write a subarray of bytes. Pass each through write byte method.

**Overrides:** write

in class

PrintStream
**Parameters:** b

- A byte array
**Parameters:** off

- Offset from which to start taking bytes
**Parameters:** len

- Number of bytes to write
**Since:** 1.1
**See Also:** FilterOutputStream.write(int)

- toString

```java
@Deprecated

public
String
toString()
```

Deprecated.

no replacement

Return log name as string representation.

**Overrides:** toString

in class

Object
**Returns:** log name
**Since:** 1.1

- parseLevel

```java
@Deprecated

public static int parseLevel​(
String
s)
```

Deprecated.

no replacement

Convert a string name of a logging level to its internal
integer representation.

**Parameters:** s

- name of logging level (e.g., 'SILENT', 'BRIEF', 'VERBOSE')
**Returns:** corresponding integer log level
**Since:** 1.1

---

#### Method Detail

log

```java
@Deprecated

public static
LogStream
log​(
String
name)
```

Deprecated.

no replacement

Return the LogStream identified by the given name. If
a log corresponding to "name" does not exist, a log using
the default stream is created.

**Parameters:** name

- name identifying the desired LogStream
**Returns:** log associated with given name
**Since:** 1.1

---

#### log

@Deprecated

public static

LogStream

log​(

String

name)

Return the LogStream identified by the given name. If
a log corresponding to "name" does not exist, a log using
the default stream is created.

getDefaultStream

```java
@Deprecated

public static
PrintStream
getDefaultStream()
```

Deprecated.

no replacement

Return the current default stream for new logs.

**Returns:** default log stream
**Since:** 1.1
**See Also:** setDefaultStream(java.io.PrintStream)

---

#### getDefaultStream

@Deprecated

public static

PrintStream

getDefaultStream()

Return the current default stream for new logs.

setDefaultStream

```java
@Deprecated

public static void setDefaultStream​(
PrintStream
newDefault)
```

Deprecated.

no replacement

Set the default stream for new logs.

**Parameters:** newDefault

- new default log stream
**Since:** 1.1
**See Also:** getDefaultStream()

---

#### setDefaultStream

@Deprecated

public static void setDefaultStream​(

PrintStream

newDefault)

Set the default stream for new logs.

getOutputStream

```java
@Deprecated

public
OutputStream
getOutputStream()
```

Deprecated.

no replacement

Return the current stream to which output from this log is sent.

**Returns:** output stream for this log
**Since:** 1.1
**See Also:** setOutputStream(java.io.OutputStream)

---

#### getOutputStream

@Deprecated

public

OutputStream

getOutputStream()

Return the current stream to which output from this log is sent.

setOutputStream

```java
@Deprecated

public void setOutputStream​(
OutputStream
out)
```

Deprecated.

no replacement

Set the stream to which output from this log is sent.

**Parameters:** out

- new output stream for this log
**Since:** 1.1
**See Also:** getOutputStream()

---

#### setOutputStream

@Deprecated

public void setOutputStream​(

OutputStream

out)

Set the stream to which output from this log is sent.

write

```java
@Deprecated

public void write​(int b)
```

Deprecated.

no replacement

Write a byte of data to the stream. If it is not a newline, then
the byte is appended to the internal buffer. If it is a newline,
then the currently buffered line is sent to the log's output
stream, prefixed with the appropriate logging information.

**Overrides:** write

in class

PrintStream
**Parameters:** b

- The byte to be written
**Since:** 1.1
**See Also:** PrintStream.print(char)

,

PrintStream.println(char)

---

#### write

@Deprecated

public void write​(int b)

Write a byte of data to the stream. If it is not a newline, then
the byte is appended to the internal buffer. If it is a newline,
then the currently buffered line is sent to the log's output
stream, prefixed with the appropriate logging information.

write

```java
@Deprecated

public void write​(byte[] b,
int off,
int len)
```

Deprecated.

no replacement

Write a subarray of bytes. Pass each through write byte method.

**Overrides:** write

in class

PrintStream
**Parameters:** b

- A byte array
**Parameters:** off

- Offset from which to start taking bytes
**Parameters:** len

- Number of bytes to write
**Since:** 1.1
**See Also:** FilterOutputStream.write(int)

---

#### write

@Deprecated

public void write​(byte[] b,
int off,
int len)

Write a subarray of bytes. Pass each through write byte method.

toString

```java
@Deprecated

public
String
toString()
```

Deprecated.

no replacement

Return log name as string representation.

**Overrides:** toString

in class

Object
**Returns:** log name
**Since:** 1.1

---

#### toString

@Deprecated

public

String

toString()

Return log name as string representation.

parseLevel

```java
@Deprecated

public static int parseLevel​(
String
s)
```

Deprecated.

no replacement

Convert a string name of a logging level to its internal
integer representation.

**Parameters:** s

- name of logging level (e.g., 'SILENT', 'BRIEF', 'VERBOSE')
**Returns:** corresponding integer log level
**Since:** 1.1

---

#### parseLevel

@Deprecated

public static int parseLevel​(

String

s)

Convert a string name of a logging level to its internal
integer representation.

---

