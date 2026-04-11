# Class MidiFileReader

**Source:** `java.desktop\javax\sound\midi\spi\MidiFileReader.html`

### Class Description

```java
public abstract class
MidiFileReader

extends
Object
```

A

MidiFileReader

supplies MIDI file-reading services. Classes
implementing this interface can parse the format information from one or more
types of MIDI file, and can produce a

Sequence

object from files of
these types.

**Since:** 1.3

---

### Field Details

*No entries found.*

### Constructor Details

#### public MidiFileReader()

*No description found.*

---

### Method Details

#### public abstract
MidiFileFormat
getMidiFileFormat​(
InputStream
stream)
throws
InvalidMidiDataException
,

IOException

Obtains the MIDI file format of the input stream provided. The stream
must point to valid MIDI file data. In general, MIDI file readers may
need to read some data from the stream before determining whether they
support it. These parsers must be able to mark the stream, read enough
data to determine whether they support the stream, and, if not, reset the
stream's read pointer to its original position. If the input stream does
not support this, this method may fail with an

IOException

.

**Parameters:**
- stream

- the input stream from which file format information should
be extracted

**Returns:**
- a

MidiFileFormat

object describing the MIDI file format

**Throws:**
- InvalidMidiDataException

- if the stream does not point to valid
MIDI file data recognized by the system
- IOException

- if an I/O exception occurs
- NullPointerException

- if

stream

is

null

**See Also:**
- InputStream.markSupported()

,

InputStream.mark(int)

---

#### public abstract
MidiFileFormat
getMidiFileFormat​(
URL
url)
throws
InvalidMidiDataException
,

IOException

Obtains the MIDI file format of the

URL

provided. The

URL

must point to valid MIDI file data.

**Parameters:**
- url

- the

URL

from which file format information should be
extracted

**Returns:**
- a

MidiFileFormat

object describing the MIDI file format

**Throws:**
- InvalidMidiDataException

- if the

URL

does not point to
valid MIDI file data recognized by the system
- IOException

- if an I/O exception occurs
- NullPointerException

- if

url

is

null

---

#### public abstract
MidiFileFormat
getMidiFileFormat​(
File
file)
throws
InvalidMidiDataException
,

IOException

Obtains the MIDI file format of the

File

provided. The

File

must point to valid MIDI file data.

**Parameters:**
- file

- the

File

from which file format information should
be extracted

**Returns:**
- a

MidiFileFormat

object describing the MIDI file format

**Throws:**
- InvalidMidiDataException

- if the

File

does not point to
valid MIDI file data recognized by the system
- IOException

- if an I/O exception occurs
- NullPointerException

- if

file

is

null

---

#### public abstract
Sequence
getSequence​(
InputStream
stream)
throws
InvalidMidiDataException
,

IOException

Obtains a MIDI sequence from the input stream provided. The stream must
point to valid MIDI file data. In general, MIDI file readers may need to
read some data from the stream before determining whether they support
it. These parsers must be able to mark the stream, read enough data to
determine whether they support the stream, and, if not, reset the
stream's read pointer to its original position. If the input stream does
not support this, this method may fail with an

IOException

.

**Parameters:**
- stream

- the input stream from which the

Sequence

should be
constructed

**Returns:**
- a

Sequence

object based on the MIDI file data contained
in the input stream

**Throws:**
- InvalidMidiDataException

- if the stream does not point to valid
MIDI file data recognized by the system
- IOException

- if an I/O exception occurs
- NullPointerException

- if

stream

is

null

**See Also:**
- InputStream.markSupported()

,

InputStream.mark(int)

---

#### public abstract
Sequence
getSequence​(
URL
url)
throws
InvalidMidiDataException
,

IOException

Obtains a MIDI sequence from the

URL

provided. The

URL

must point to valid MIDI file data.

**Parameters:**
- url

- the

URL

for which the

Sequence

should be
constructed

**Returns:**
- a

Sequence

object based on the MIDI file data pointed to
by the

URL

**Throws:**
- InvalidMidiDataException

- if the

URL

does not point to
valid MIDI file data recognized by the system
- IOException

- if an I/O exception occurs
- NullPointerException

- if

url

is

null

---

#### public abstract
Sequence
getSequence​(
File
file)
throws
InvalidMidiDataException
,

IOException

Obtains a MIDI sequence from the

File

provided. The

File

must point to valid MIDI file data.

**Parameters:**
- file

- the

File

from which the

Sequence

should be
constructed

**Returns:**
- a

Sequence

object based on the MIDI file data pointed to
by the

File

**Throws:**
- InvalidMidiDataException

- if the

File

does not point to
valid MIDI file data recognized by the system
- IOException

- if an I/O exception occurs
- NullPointerException

- if

file

is

null

---

### Additional Sections

#### Class MidiFileReader

java.lang.Object

- javax.sound.midi.spi.MidiFileReader

javax.sound.midi.spi.MidiFileReader

```java
public abstract class
MidiFileReader

extends
Object
```

A

MidiFileReader

supplies MIDI file-reading services. Classes
implementing this interface can parse the format information from one or more
types of MIDI file, and can produce a

Sequence

object from files of
these types.

**Since:** 1.3

public abstract class

MidiFileReader

extends

Object

A

MidiFileReader

supplies MIDI file-reading services. Classes
implementing this interface can parse the format information from one or more
types of MIDI file, and can produce a

Sequence

object from files of
these types.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

MidiFileReader

()

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

abstract

MidiFileFormat

getMidiFileFormat

​(

File

file)

Obtains the MIDI file format of the

File

provided.

abstract

MidiFileFormat

getMidiFileFormat

​(

InputStream

stream)

Obtains the MIDI file format of the input stream provided.

abstract

MidiFileFormat

getMidiFileFormat

​(

URL

url)

Obtains the MIDI file format of the

URL

provided.

abstract

Sequence

getSequence

​(

File

file)

Obtains a MIDI sequence from the

File

provided.

abstract

Sequence

getSequence

​(

InputStream

stream)

Obtains a MIDI sequence from the input stream provided.

abstract

Sequence

getSequence

​(

URL

url)

Obtains a MIDI sequence from the

URL

provided.

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

MidiFileReader

()

---

#### Constructor Summary

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

abstract

MidiFileFormat

getMidiFileFormat

​(

File

file)

Obtains the MIDI file format of the

File

provided.

abstract

MidiFileFormat

getMidiFileFormat

​(

InputStream

stream)

Obtains the MIDI file format of the input stream provided.

abstract

MidiFileFormat

getMidiFileFormat

​(

URL

url)

Obtains the MIDI file format of the

URL

provided.

abstract

Sequence

getSequence

​(

File

file)

Obtains a MIDI sequence from the

File

provided.

abstract

Sequence

getSequence

​(

InputStream

stream)

Obtains a MIDI sequence from the input stream provided.

abstract

Sequence

getSequence

​(

URL

url)

Obtains a MIDI sequence from the

URL

provided.

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

Obtains the MIDI file format of the

File

provided.

Obtains the MIDI file format of the input stream provided.

Obtains the MIDI file format of the

URL

provided.

Obtains a MIDI sequence from the

File

provided.

Obtains a MIDI sequence from the input stream provided.

Obtains a MIDI sequence from the

URL

provided.

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

- MidiFileReader

```java
public MidiFileReader()
```

============ METHOD DETAIL ==========

- Method Detail

- getMidiFileFormat

```java
public abstract
MidiFileFormat
getMidiFileFormat​(
InputStream
stream)
throws
InvalidMidiDataException
,

IOException
```

Obtains the MIDI file format of the input stream provided. The stream
must point to valid MIDI file data. In general, MIDI file readers may
need to read some data from the stream before determining whether they
support it. These parsers must be able to mark the stream, read enough
data to determine whether they support the stream, and, if not, reset the
stream's read pointer to its original position. If the input stream does
not support this, this method may fail with an

IOException

.

**Parameters:** stream

- the input stream from which file format information should
be extracted
**Returns:** a

MidiFileFormat

object describing the MIDI file format
**Throws:** InvalidMidiDataException

- if the stream does not point to valid
MIDI file data recognized by the system
**Throws:** IOException

- if an I/O exception occurs
**Throws:** NullPointerException

- if

stream

is

null
**See Also:** InputStream.markSupported()

,

InputStream.mark(int)

- getMidiFileFormat

```java
public abstract
MidiFileFormat
getMidiFileFormat​(
URL
url)
throws
InvalidMidiDataException
,

IOException
```

Obtains the MIDI file format of the

URL

provided. The

URL

must point to valid MIDI file data.

**Parameters:** url

- the

URL

from which file format information should be
extracted
**Returns:** a

MidiFileFormat

object describing the MIDI file format
**Throws:** InvalidMidiDataException

- if the

URL

does not point to
valid MIDI file data recognized by the system
**Throws:** IOException

- if an I/O exception occurs
**Throws:** NullPointerException

- if

url

is

null

- getMidiFileFormat

```java
public abstract
MidiFileFormat
getMidiFileFormat​(
File
file)
throws
InvalidMidiDataException
,

IOException
```

Obtains the MIDI file format of the

File

provided. The

File

must point to valid MIDI file data.

**Parameters:** file

- the

File

from which file format information should
be extracted
**Returns:** a

MidiFileFormat

object describing the MIDI file format
**Throws:** InvalidMidiDataException

- if the

File

does not point to
valid MIDI file data recognized by the system
**Throws:** IOException

- if an I/O exception occurs
**Throws:** NullPointerException

- if

file

is

null

- getSequence

```java
public abstract
Sequence
getSequence​(
InputStream
stream)
throws
InvalidMidiDataException
,

IOException
```

Obtains a MIDI sequence from the input stream provided. The stream must
point to valid MIDI file data. In general, MIDI file readers may need to
read some data from the stream before determining whether they support
it. These parsers must be able to mark the stream, read enough data to
determine whether they support the stream, and, if not, reset the
stream's read pointer to its original position. If the input stream does
not support this, this method may fail with an

IOException

.

**Parameters:** stream

- the input stream from which the

Sequence

should be
constructed
**Returns:** a

Sequence

object based on the MIDI file data contained
in the input stream
**Throws:** InvalidMidiDataException

- if the stream does not point to valid
MIDI file data recognized by the system
**Throws:** IOException

- if an I/O exception occurs
**Throws:** NullPointerException

- if

stream

is

null
**See Also:** InputStream.markSupported()

,

InputStream.mark(int)

- getSequence

```java
public abstract
Sequence
getSequence​(
URL
url)
throws
InvalidMidiDataException
,

IOException
```

Obtains a MIDI sequence from the

URL

provided. The

URL

must point to valid MIDI file data.

**Parameters:** url

- the

URL

for which the

Sequence

should be
constructed
**Returns:** a

Sequence

object based on the MIDI file data pointed to
by the

URL
**Throws:** InvalidMidiDataException

- if the

URL

does not point to
valid MIDI file data recognized by the system
**Throws:** IOException

- if an I/O exception occurs
**Throws:** NullPointerException

- if

url

is

null

- getSequence

```java
public abstract
Sequence
getSequence​(
File
file)
throws
InvalidMidiDataException
,

IOException
```

Obtains a MIDI sequence from the

File

provided. The

File

must point to valid MIDI file data.

**Parameters:** file

- the

File

from which the

Sequence

should be
constructed
**Returns:** a

Sequence

object based on the MIDI file data pointed to
by the

File
**Throws:** InvalidMidiDataException

- if the

File

does not point to
valid MIDI file data recognized by the system
**Throws:** IOException

- if an I/O exception occurs
**Throws:** NullPointerException

- if

file

is

null

Constructor Detail

- MidiFileReader

```java
public MidiFileReader()
```

---

#### Constructor Detail

MidiFileReader

```java
public MidiFileReader()
```

---

#### MidiFileReader

public MidiFileReader()

Method Detail

- getMidiFileFormat

```java
public abstract
MidiFileFormat
getMidiFileFormat​(
InputStream
stream)
throws
InvalidMidiDataException
,

IOException
```

Obtains the MIDI file format of the input stream provided. The stream
must point to valid MIDI file data. In general, MIDI file readers may
need to read some data from the stream before determining whether they
support it. These parsers must be able to mark the stream, read enough
data to determine whether they support the stream, and, if not, reset the
stream's read pointer to its original position. If the input stream does
not support this, this method may fail with an

IOException

.

**Parameters:** stream

- the input stream from which file format information should
be extracted
**Returns:** a

MidiFileFormat

object describing the MIDI file format
**Throws:** InvalidMidiDataException

- if the stream does not point to valid
MIDI file data recognized by the system
**Throws:** IOException

- if an I/O exception occurs
**Throws:** NullPointerException

- if

stream

is

null
**See Also:** InputStream.markSupported()

,

InputStream.mark(int)

- getMidiFileFormat

```java
public abstract
MidiFileFormat
getMidiFileFormat​(
URL
url)
throws
InvalidMidiDataException
,

IOException
```

Obtains the MIDI file format of the

URL

provided. The

URL

must point to valid MIDI file data.

**Parameters:** url

- the

URL

from which file format information should be
extracted
**Returns:** a

MidiFileFormat

object describing the MIDI file format
**Throws:** InvalidMidiDataException

- if the

URL

does not point to
valid MIDI file data recognized by the system
**Throws:** IOException

- if an I/O exception occurs
**Throws:** NullPointerException

- if

url

is

null

- getMidiFileFormat

```java
public abstract
MidiFileFormat
getMidiFileFormat​(
File
file)
throws
InvalidMidiDataException
,

IOException
```

Obtains the MIDI file format of the

File

provided. The

File

must point to valid MIDI file data.

**Parameters:** file

- the

File

from which file format information should
be extracted
**Returns:** a

MidiFileFormat

object describing the MIDI file format
**Throws:** InvalidMidiDataException

- if the

File

does not point to
valid MIDI file data recognized by the system
**Throws:** IOException

- if an I/O exception occurs
**Throws:** NullPointerException

- if

file

is

null

- getSequence

```java
public abstract
Sequence
getSequence​(
InputStream
stream)
throws
InvalidMidiDataException
,

IOException
```

Obtains a MIDI sequence from the input stream provided. The stream must
point to valid MIDI file data. In general, MIDI file readers may need to
read some data from the stream before determining whether they support
it. These parsers must be able to mark the stream, read enough data to
determine whether they support the stream, and, if not, reset the
stream's read pointer to its original position. If the input stream does
not support this, this method may fail with an

IOException

.

**Parameters:** stream

- the input stream from which the

Sequence

should be
constructed
**Returns:** a

Sequence

object based on the MIDI file data contained
in the input stream
**Throws:** InvalidMidiDataException

- if the stream does not point to valid
MIDI file data recognized by the system
**Throws:** IOException

- if an I/O exception occurs
**Throws:** NullPointerException

- if

stream

is

null
**See Also:** InputStream.markSupported()

,

InputStream.mark(int)

- getSequence

```java
public abstract
Sequence
getSequence​(
URL
url)
throws
InvalidMidiDataException
,

IOException
```

Obtains a MIDI sequence from the

URL

provided. The

URL

must point to valid MIDI file data.

**Parameters:** url

- the

URL

for which the

Sequence

should be
constructed
**Returns:** a

Sequence

object based on the MIDI file data pointed to
by the

URL
**Throws:** InvalidMidiDataException

- if the

URL

does not point to
valid MIDI file data recognized by the system
**Throws:** IOException

- if an I/O exception occurs
**Throws:** NullPointerException

- if

url

is

null

- getSequence

```java
public abstract
Sequence
getSequence​(
File
file)
throws
InvalidMidiDataException
,

IOException
```

Obtains a MIDI sequence from the

File

provided. The

File

must point to valid MIDI file data.

**Parameters:** file

- the

File

from which the

Sequence

should be
constructed
**Returns:** a

Sequence

object based on the MIDI file data pointed to
by the

File
**Throws:** InvalidMidiDataException

- if the

File

does not point to
valid MIDI file data recognized by the system
**Throws:** IOException

- if an I/O exception occurs
**Throws:** NullPointerException

- if

file

is

null

---

#### Method Detail

getMidiFileFormat

```java
public abstract
MidiFileFormat
getMidiFileFormat​(
InputStream
stream)
throws
InvalidMidiDataException
,

IOException
```

Obtains the MIDI file format of the input stream provided. The stream
must point to valid MIDI file data. In general, MIDI file readers may
need to read some data from the stream before determining whether they
support it. These parsers must be able to mark the stream, read enough
data to determine whether they support the stream, and, if not, reset the
stream's read pointer to its original position. If the input stream does
not support this, this method may fail with an

IOException

.

**Parameters:** stream

- the input stream from which file format information should
be extracted
**Returns:** a

MidiFileFormat

object describing the MIDI file format
**Throws:** InvalidMidiDataException

- if the stream does not point to valid
MIDI file data recognized by the system
**Throws:** IOException

- if an I/O exception occurs
**Throws:** NullPointerException

- if

stream

is

null
**See Also:** InputStream.markSupported()

,

InputStream.mark(int)

---

#### getMidiFileFormat

public abstract

MidiFileFormat

getMidiFileFormat​(

InputStream

stream)
throws

InvalidMidiDataException

,

IOException

Obtains the MIDI file format of the input stream provided. The stream
must point to valid MIDI file data. In general, MIDI file readers may
need to read some data from the stream before determining whether they
support it. These parsers must be able to mark the stream, read enough
data to determine whether they support the stream, and, if not, reset the
stream's read pointer to its original position. If the input stream does
not support this, this method may fail with an

IOException

.

getMidiFileFormat

```java
public abstract
MidiFileFormat
getMidiFileFormat​(
URL
url)
throws
InvalidMidiDataException
,

IOException
```

Obtains the MIDI file format of the

URL

provided. The

URL

must point to valid MIDI file data.

**Parameters:** url

- the

URL

from which file format information should be
extracted
**Returns:** a

MidiFileFormat

object describing the MIDI file format
**Throws:** InvalidMidiDataException

- if the

URL

does not point to
valid MIDI file data recognized by the system
**Throws:** IOException

- if an I/O exception occurs
**Throws:** NullPointerException

- if

url

is

null

---

#### getMidiFileFormat

public abstract

MidiFileFormat

getMidiFileFormat​(

URL

url)
throws

InvalidMidiDataException

,

IOException

Obtains the MIDI file format of the

URL

provided. The

URL

must point to valid MIDI file data.

getMidiFileFormat

```java
public abstract
MidiFileFormat
getMidiFileFormat​(
File
file)
throws
InvalidMidiDataException
,

IOException
```

Obtains the MIDI file format of the

File

provided. The

File

must point to valid MIDI file data.

**Parameters:** file

- the

File

from which file format information should
be extracted
**Returns:** a

MidiFileFormat

object describing the MIDI file format
**Throws:** InvalidMidiDataException

- if the

File

does not point to
valid MIDI file data recognized by the system
**Throws:** IOException

- if an I/O exception occurs
**Throws:** NullPointerException

- if

file

is

null

---

#### getMidiFileFormat

public abstract

MidiFileFormat

getMidiFileFormat​(

File

file)
throws

InvalidMidiDataException

,

IOException

Obtains the MIDI file format of the

File

provided. The

File

must point to valid MIDI file data.

getSequence

```java
public abstract
Sequence
getSequence​(
InputStream
stream)
throws
InvalidMidiDataException
,

IOException
```

Obtains a MIDI sequence from the input stream provided. The stream must
point to valid MIDI file data. In general, MIDI file readers may need to
read some data from the stream before determining whether they support
it. These parsers must be able to mark the stream, read enough data to
determine whether they support the stream, and, if not, reset the
stream's read pointer to its original position. If the input stream does
not support this, this method may fail with an

IOException

.

**Parameters:** stream

- the input stream from which the

Sequence

should be
constructed
**Returns:** a

Sequence

object based on the MIDI file data contained
in the input stream
**Throws:** InvalidMidiDataException

- if the stream does not point to valid
MIDI file data recognized by the system
**Throws:** IOException

- if an I/O exception occurs
**Throws:** NullPointerException

- if

stream

is

null
**See Also:** InputStream.markSupported()

,

InputStream.mark(int)

---

#### getSequence

public abstract

Sequence

getSequence​(

InputStream

stream)
throws

InvalidMidiDataException

,

IOException

Obtains a MIDI sequence from the input stream provided. The stream must
point to valid MIDI file data. In general, MIDI file readers may need to
read some data from the stream before determining whether they support
it. These parsers must be able to mark the stream, read enough data to
determine whether they support the stream, and, if not, reset the
stream's read pointer to its original position. If the input stream does
not support this, this method may fail with an

IOException

.

getSequence

```java
public abstract
Sequence
getSequence​(
URL
url)
throws
InvalidMidiDataException
,

IOException
```

Obtains a MIDI sequence from the

URL

provided. The

URL

must point to valid MIDI file data.

**Parameters:** url

- the

URL

for which the

Sequence

should be
constructed
**Returns:** a

Sequence

object based on the MIDI file data pointed to
by the

URL
**Throws:** InvalidMidiDataException

- if the

URL

does not point to
valid MIDI file data recognized by the system
**Throws:** IOException

- if an I/O exception occurs
**Throws:** NullPointerException

- if

url

is

null

---

#### getSequence

public abstract

Sequence

getSequence​(

URL

url)
throws

InvalidMidiDataException

,

IOException

Obtains a MIDI sequence from the

URL

provided. The

URL

must point to valid MIDI file data.

getSequence

```java
public abstract
Sequence
getSequence​(
File
file)
throws
InvalidMidiDataException
,

IOException
```

Obtains a MIDI sequence from the

File

provided. The

File

must point to valid MIDI file data.

**Parameters:** file

- the

File

from which the

Sequence

should be
constructed
**Returns:** a

Sequence

object based on the MIDI file data pointed to
by the

File
**Throws:** InvalidMidiDataException

- if the

File

does not point to
valid MIDI file data recognized by the system
**Throws:** IOException

- if an I/O exception occurs
**Throws:** NullPointerException

- if

file

is

null

---

#### getSequence

public abstract

Sequence

getSequence​(

File

file)
throws

InvalidMidiDataException

,

IOException

Obtains a MIDI sequence from the

File

provided. The

File

must point to valid MIDI file data.

---

