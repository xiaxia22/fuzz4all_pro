# Class FilterWriter

**Source:** `java.base\java\io\FilterWriter.html`

### Class Description

```java
public abstract class
FilterWriter

extends
Writer
```

Abstract class for writing filtered character streams.
The abstract class

FilterWriter

itself
provides default methods that pass all requests to the
contained stream. Subclasses of

FilterWriter

should override some of these methods and may also
provide additional methods and fields.

**All Implemented Interfaces:** Closeable

,

Flushable

,

Appendable

,

AutoCloseable

---

### Field Details

#### protected
Writer
out

The underlying character-output stream.

---

### Constructor Details

#### protected FilterWriter​(
Writer
out)

Create a new filtered writer.

**Parameters:**
- out

- a Writer object to provide the underlying stream.

**Throws:**
- NullPointerException

- if

out

is

null

---

### Method Details

#### public void write​(int c)
throws
IOException

Writes a single character.

**Overrides:**
- write

in class

Writer

**Parameters:**
- c

- int specifying a character to be written

**Throws:**
- IOException

- If an I/O error occurs

---

#### public void write​(char[] cbuf,
int off,
int len)
throws
IOException

Writes a portion of an array of characters.

**Specified by:**
- write

in class

Writer

**Parameters:**
- cbuf

- Buffer of characters to be written
- off

- Offset from which to start reading characters
- len

- Number of characters to be written

**Throws:**
- IndexOutOfBoundsException

- If the values of the

off

and

len

parameters
cause the corresponding method of the underlying

Writer

to throw an

IndexOutOfBoundsException
- IOException

- If an I/O error occurs

---

#### public void write​(
String
str,
int off,
int len)
throws
IOException

Writes a portion of a string.

**Overrides:**
- write

in class

Writer

**Parameters:**
- str

- String to be written
- off

- Offset from which to start reading characters
- len

- Number of characters to be written

**Throws:**
- IndexOutOfBoundsException

- If the values of the

off

and

len

parameters
cause the corresponding method of the underlying

Writer

to throw an

IndexOutOfBoundsException
- IOException

- If an I/O error occurs

---

#### public void flush()
throws
IOException

Flushes the stream.

**Specified by:**
- flush

in interface

Flushable
- flush

in class

Writer

**Throws:**
- IOException

- If an I/O error occurs

---

### Additional Sections

#### Class FilterWriter

java.lang.Object

- java.io.Writer
- - java.io.FilterWriter

java.io.Writer

- java.io.FilterWriter

java.io.FilterWriter

**All Implemented Interfaces:** Closeable

,

Flushable

,

Appendable

,

AutoCloseable

```java
public abstract class
FilterWriter

extends
Writer
```

Abstract class for writing filtered character streams.
The abstract class

FilterWriter

itself
provides default methods that pass all requests to the
contained stream. Subclasses of

FilterWriter

should override some of these methods and may also
provide additional methods and fields.

**Since:** 1.1

public abstract class

FilterWriter

extends

Writer

Abstract class for writing filtered character streams.
The abstract class

FilterWriter

itself
provides default methods that pass all requests to the
contained stream. Subclasses of

FilterWriter

should override some of these methods and may also
provide additional methods and fields.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

protected

Writer

out

The underlying character-output stream.

- Fields declared in class java.io.

Writer

lock

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

FilterWriter

​(

Writer

out)

Create a new filtered writer.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

flush

()

Flushes the stream.

void

write

​(char[] cbuf,
int off,
int len)

Writes a portion of an array of characters.

void

write

​(int c)

Writes a single character.

void

write

​(

String

str,
int off,
int len)

Writes a portion of a string.

- Methods declared in class java.io.

Writer

append

,

append

,

append

,

close

,

nullWriter

,

write

,

write

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

Field Summary

Fields

Modifier and Type

Field

Description

protected

Writer

out

The underlying character-output stream.

- Fields declared in class java.io.

Writer

lock

---

#### Field Summary

The underlying character-output stream.

Fields declared in class java.io.

Writer

lock

---

#### Fields declared in class java.io. Writer

Constructor Summary

Constructors

Modifier

Constructor

Description

protected

FilterWriter

​(

Writer

out)

Create a new filtered writer.

---

#### Constructor Summary

Create a new filtered writer.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

flush

()

Flushes the stream.

void

write

​(char[] cbuf,
int off,
int len)

Writes a portion of an array of characters.

void

write

​(int c)

Writes a single character.

void

write

​(

String

str,
int off,
int len)

Writes a portion of a string.

- Methods declared in class java.io.

Writer

append

,

append

,

append

,

close

,

nullWriter

,

write

,

write

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

Flushes the stream.

Writes a portion of an array of characters.

Writes a single character.

Writes a portion of a string.

Methods declared in class java.io.

Writer

append

,

append

,

append

,

close

,

nullWriter

,

write

,

write

---

#### Methods declared in class java.io. Writer

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

============ FIELD DETAIL ===========

- Field Detail

- out

```java
protected
Writer
out
```

The underlying character-output stream.

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- FilterWriter

```java
protected FilterWriter​(
Writer
out)
```

Create a new filtered writer.

**Parameters:** out

- a Writer object to provide the underlying stream.
**Throws:** NullPointerException

- if

out

is

null

============ METHOD DETAIL ==========

- Method Detail

- write

```java
public void write​(int c)
throws
IOException
```

Writes a single character.

**Overrides:** write

in class

Writer
**Parameters:** c

- int specifying a character to be written
**Throws:** IOException

- If an I/O error occurs

- write

```java
public void write​(char[] cbuf,
int off,
int len)
throws
IOException
```

Writes a portion of an array of characters.

**Specified by:** write

in class

Writer
**Parameters:** cbuf

- Buffer of characters to be written
**Parameters:** off

- Offset from which to start reading characters
**Parameters:** len

- Number of characters to be written
**Throws:** IndexOutOfBoundsException

- If the values of the

off

and

len

parameters
cause the corresponding method of the underlying

Writer

to throw an

IndexOutOfBoundsException
**Throws:** IOException

- If an I/O error occurs

- write

```java
public void write​(
String
str,
int off,
int len)
throws
IOException
```

Writes a portion of a string.

**Overrides:** write

in class

Writer
**Parameters:** str

- String to be written
**Parameters:** off

- Offset from which to start reading characters
**Parameters:** len

- Number of characters to be written
**Throws:** IndexOutOfBoundsException

- If the values of the

off

and

len

parameters
cause the corresponding method of the underlying

Writer

to throw an

IndexOutOfBoundsException
**Throws:** IOException

- If an I/O error occurs

- flush

```java
public void flush()
throws
IOException
```

Flushes the stream.

**Specified by:** flush

in interface

Flushable
**Specified by:** flush

in class

Writer
**Throws:** IOException

- If an I/O error occurs

Field Detail

- out

```java
protected
Writer
out
```

The underlying character-output stream.

---

#### Field Detail

out

```java
protected
Writer
out
```

The underlying character-output stream.

---

#### out

protected

Writer

out

The underlying character-output stream.

Constructor Detail

- FilterWriter

```java
protected FilterWriter​(
Writer
out)
```

Create a new filtered writer.

**Parameters:** out

- a Writer object to provide the underlying stream.
**Throws:** NullPointerException

- if

out

is

null

---

#### Constructor Detail

FilterWriter

```java
protected FilterWriter​(
Writer
out)
```

Create a new filtered writer.

**Parameters:** out

- a Writer object to provide the underlying stream.
**Throws:** NullPointerException

- if

out

is

null

---

#### FilterWriter

protected FilterWriter​(

Writer

out)

Create a new filtered writer.

Method Detail

- write

```java
public void write​(int c)
throws
IOException
```

Writes a single character.

**Overrides:** write

in class

Writer
**Parameters:** c

- int specifying a character to be written
**Throws:** IOException

- If an I/O error occurs

- write

```java
public void write​(char[] cbuf,
int off,
int len)
throws
IOException
```

Writes a portion of an array of characters.

**Specified by:** write

in class

Writer
**Parameters:** cbuf

- Buffer of characters to be written
**Parameters:** off

- Offset from which to start reading characters
**Parameters:** len

- Number of characters to be written
**Throws:** IndexOutOfBoundsException

- If the values of the

off

and

len

parameters
cause the corresponding method of the underlying

Writer

to throw an

IndexOutOfBoundsException
**Throws:** IOException

- If an I/O error occurs

- write

```java
public void write​(
String
str,
int off,
int len)
throws
IOException
```

Writes a portion of a string.

**Overrides:** write

in class

Writer
**Parameters:** str

- String to be written
**Parameters:** off

- Offset from which to start reading characters
**Parameters:** len

- Number of characters to be written
**Throws:** IndexOutOfBoundsException

- If the values of the

off

and

len

parameters
cause the corresponding method of the underlying

Writer

to throw an

IndexOutOfBoundsException
**Throws:** IOException

- If an I/O error occurs

- flush

```java
public void flush()
throws
IOException
```

Flushes the stream.

**Specified by:** flush

in interface

Flushable
**Specified by:** flush

in class

Writer
**Throws:** IOException

- If an I/O error occurs

---

#### Method Detail

write

```java
public void write​(int c)
throws
IOException
```

Writes a single character.

**Overrides:** write

in class

Writer
**Parameters:** c

- int specifying a character to be written
**Throws:** IOException

- If an I/O error occurs

---

#### write

public void write​(int c)
throws

IOException

Writes a single character.

write

```java
public void write​(char[] cbuf,
int off,
int len)
throws
IOException
```

Writes a portion of an array of characters.

**Specified by:** write

in class

Writer
**Parameters:** cbuf

- Buffer of characters to be written
**Parameters:** off

- Offset from which to start reading characters
**Parameters:** len

- Number of characters to be written
**Throws:** IndexOutOfBoundsException

- If the values of the

off

and

len

parameters
cause the corresponding method of the underlying

Writer

to throw an

IndexOutOfBoundsException
**Throws:** IOException

- If an I/O error occurs

---

#### write

public void write​(char[] cbuf,
int off,
int len)
throws

IOException

Writes a portion of an array of characters.

write

```java
public void write​(
String
str,
int off,
int len)
throws
IOException
```

Writes a portion of a string.

**Overrides:** write

in class

Writer
**Parameters:** str

- String to be written
**Parameters:** off

- Offset from which to start reading characters
**Parameters:** len

- Number of characters to be written
**Throws:** IndexOutOfBoundsException

- If the values of the

off

and

len

parameters
cause the corresponding method of the underlying

Writer

to throw an

IndexOutOfBoundsException
**Throws:** IOException

- If an I/O error occurs

---

#### write

public void write​(

String

str,
int off,
int len)
throws

IOException

Writes a portion of a string.

flush

```java
public void flush()
throws
IOException
```

Flushes the stream.

**Specified by:** flush

in interface

Flushable
**Specified by:** flush

in class

Writer
**Throws:** IOException

- If an I/O error occurs

---

#### flush

public void flush()
throws

IOException

Flushes the stream.

---

