# Interface Readable

**Source:** `java.base\java\lang\Readable.html`

### Class Description

```java
public interface
Readable
```

A

Readable

is a source of characters. Characters from
a

Readable

are made available to callers of the read
method via a

CharBuffer

.

**All Known Implementing Classes:** BufferedReader

,

CharArrayReader

,

CharBuffer

,

FileReader

,

FilterReader

,

InputStreamReader

,

LineNumberReader

,

PipedReader

,

PushbackReader

,

Reader

,

StringReader

,

URLReader

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### int read​(
CharBuffer
cb)
throws
IOException

Attempts to read characters into the specified character buffer.
The buffer is used as a repository of characters as-is: the only
changes made are the results of a put operation. No flipping or
rewinding of the buffer is performed.

**Parameters:**
- cb

- the buffer to read characters into

**Returns:**
- The number of

char

values added to the buffer,
or -1 if this source of characters is at its end

**Throws:**
- IOException

- if an I/O error occurs
- NullPointerException

- if cb is null
- ReadOnlyBufferException

- if cb is a read only buffer

---

### Additional Sections

#### Interface Readable

**All Known Implementing Classes:** BufferedReader

,

CharArrayReader

,

CharBuffer

,

FileReader

,

FilterReader

,

InputStreamReader

,

LineNumberReader

,

PipedReader

,

PushbackReader

,

Reader

,

StringReader

,

URLReader

```java
public interface
Readable
```

A

Readable

is a source of characters. Characters from
a

Readable

are made available to callers of the read
method via a

CharBuffer

.

**Since:** 1.5

public interface

Readable

A

Readable

is a source of characters. Characters from
a

Readable

are made available to callers of the read
method via a

CharBuffer

.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

int

read

​(

CharBuffer

cb)

Attempts to read characters into the specified character buffer.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

int

read

​(

CharBuffer

cb)

Attempts to read characters into the specified character buffer.

---

#### Method Summary

Attempts to read characters into the specified character buffer.

============ METHOD DETAIL ==========

- Method Detail

- read

```java
int read​(
CharBuffer
cb)
throws
IOException
```

Attempts to read characters into the specified character buffer.
The buffer is used as a repository of characters as-is: the only
changes made are the results of a put operation. No flipping or
rewinding of the buffer is performed.

**Parameters:** cb

- the buffer to read characters into
**Returns:** The number of

char

values added to the buffer,
or -1 if this source of characters is at its end
**Throws:** IOException

- if an I/O error occurs
**Throws:** NullPointerException

- if cb is null
**Throws:** ReadOnlyBufferException

- if cb is a read only buffer

Method Detail

- read

```java
int read​(
CharBuffer
cb)
throws
IOException
```

Attempts to read characters into the specified character buffer.
The buffer is used as a repository of characters as-is: the only
changes made are the results of a put operation. No flipping or
rewinding of the buffer is performed.

**Parameters:** cb

- the buffer to read characters into
**Returns:** The number of

char

values added to the buffer,
or -1 if this source of characters is at its end
**Throws:** IOException

- if an I/O error occurs
**Throws:** NullPointerException

- if cb is null
**Throws:** ReadOnlyBufferException

- if cb is a read only buffer

---

#### Method Detail

read

```java
int read​(
CharBuffer
cb)
throws
IOException
```

Attempts to read characters into the specified character buffer.
The buffer is used as a repository of characters as-is: the only
changes made are the results of a put operation. No flipping or
rewinding of the buffer is performed.

**Parameters:** cb

- the buffer to read characters into
**Returns:** The number of

char

values added to the buffer,
or -1 if this source of characters is at its end
**Throws:** IOException

- if an I/O error occurs
**Throws:** NullPointerException

- if cb is null
**Throws:** ReadOnlyBufferException

- if cb is a read only buffer

---

#### read

int read​(

CharBuffer

cb)
throws

IOException

Attempts to read characters into the specified character buffer.
The buffer is used as a repository of characters as-is: the only
changes made are the results of a put operation. No flipping or
rewinding of the buffer is performed.

---

