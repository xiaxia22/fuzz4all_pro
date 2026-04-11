# Class MidiFileWriter

**Source:** `java.desktop\javax\sound\midi\spi\MidiFileWriter.html`

### Class Description

```java
public abstract class
MidiFileWriter

extends
Object
```

A

MidiFileWriter

supplies MIDI file-writing services. Classes that
implement this interface can write one or more types of MIDI file from a

Sequence

object.

**Since:** 1.3

---

### Field Details

*No entries found.*

### Constructor Details

#### public MidiFileWriter()

*No description found.*

---

### Method Details

#### public abstract int[] getMidiFileTypes()

Obtains the set of MIDI file types for which file writing support is
provided by this file writer.

**Returns:**
- array of file types. If no file types are supported, an array of
length 0 is returned.

---

#### public abstract int[] getMidiFileTypes​(
Sequence
sequence)

Obtains the file types that this file writer can write from the sequence
specified.

**Parameters:**
- sequence

- the sequence for which MIDI file type support is queried

**Returns:**
- array of file types. If no file types are supported, returns an
array of length 0.

**Throws:**
- NullPointerException

- if

sequence

is

null

---

#### public boolean isFileTypeSupported​(int fileType)

Indicates whether file writing support for the specified MIDI file type
is provided by this file writer.

**Parameters:**
- fileType

- the file type for which write capabilities are queried

**Returns:**
- true

if the file type is supported, otherwise

false

---

#### public boolean isFileTypeSupported​(int fileType,

Sequence
sequence)

Indicates whether a MIDI file of the file type specified can be written
from the sequence indicated.

**Parameters:**
- fileType

- the file type for which write capabilities are queried
- sequence

- the sequence for which file writing support is queried

**Returns:**
- true

if the file type is supported for this sequence,
otherwise

false

**Throws:**
- NullPointerException

- if

sequence

is

null

---

#### public abstract int write​(
Sequence
in,
int fileType,

OutputStream
out)
throws
IOException

Writes a stream of bytes representing a MIDI file of the file type
indicated to the output stream provided.

**Parameters:**
- in

- sequence containing MIDI data to be written to the file
- fileType

- type of the file to be written to the output stream
- out

- stream to which the file data should be written

**Returns:**
- the number of bytes written to the output stream

**Throws:**
- IOException

- if an I/O exception occurs
- IllegalArgumentException

- if the file type is not supported by
this file writer
- NullPointerException

- if

in

or

out

are

null

**See Also:**
- isFileTypeSupported(int, Sequence)

,

getMidiFileTypes(Sequence)

---

#### public abstract int write​(
Sequence
in,
int fileType,

File
out)
throws
IOException

Writes a stream of bytes representing a MIDI file of the file type
indicated to the external file provided.

**Parameters:**
- in

- sequence containing MIDI data to be written to the external
file
- fileType

- type of the file to be written to the external file
- out

- external file to which the file data should be written

**Returns:**
- the number of bytes written to the file

**Throws:**
- IOException

- if an I/O exception occurs
- IllegalArgumentException

- if the file type is not supported by
this file writer
- NullPointerException

- if

in

or

out

are

null

**See Also:**
- isFileTypeSupported(int, Sequence)

,

getMidiFileTypes(Sequence)

---

### Additional Sections

#### Class MidiFileWriter

java.lang.Object

- javax.sound.midi.spi.MidiFileWriter

javax.sound.midi.spi.MidiFileWriter

```java
public abstract class
MidiFileWriter

extends
Object
```

A

MidiFileWriter

supplies MIDI file-writing services. Classes that
implement this interface can write one or more types of MIDI file from a

Sequence

object.

**Since:** 1.3

public abstract class

MidiFileWriter

extends

Object

A

MidiFileWriter

supplies MIDI file-writing services. Classes that
implement this interface can write one or more types of MIDI file from a

Sequence

object.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

MidiFileWriter

()

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

abstract int[]

getMidiFileTypes

()

Obtains the set of MIDI file types for which file writing support is
provided by this file writer.

abstract int[]

getMidiFileTypes

​(

Sequence

sequence)

Obtains the file types that this file writer can write from the sequence
specified.

boolean

isFileTypeSupported

​(int fileType)

Indicates whether file writing support for the specified MIDI file type
is provided by this file writer.

boolean

isFileTypeSupported

​(int fileType,

Sequence

sequence)

Indicates whether a MIDI file of the file type specified can be written
from the sequence indicated.

abstract int

write

​(

Sequence

in,
int fileType,

File

out)

Writes a stream of bytes representing a MIDI file of the file type
indicated to the external file provided.

abstract int

write

​(

Sequence

in,
int fileType,

OutputStream

out)

Writes a stream of bytes representing a MIDI file of the file type
indicated to the output stream provided.

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

MidiFileWriter

()

---

#### Constructor Summary

Method Summary

All Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

abstract int[]

getMidiFileTypes

()

Obtains the set of MIDI file types for which file writing support is
provided by this file writer.

abstract int[]

getMidiFileTypes

​(

Sequence

sequence)

Obtains the file types that this file writer can write from the sequence
specified.

boolean

isFileTypeSupported

​(int fileType)

Indicates whether file writing support for the specified MIDI file type
is provided by this file writer.

boolean

isFileTypeSupported

​(int fileType,

Sequence

sequence)

Indicates whether a MIDI file of the file type specified can be written
from the sequence indicated.

abstract int

write

​(

Sequence

in,
int fileType,

File

out)

Writes a stream of bytes representing a MIDI file of the file type
indicated to the external file provided.

abstract int

write

​(

Sequence

in,
int fileType,

OutputStream

out)

Writes a stream of bytes representing a MIDI file of the file type
indicated to the output stream provided.

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

Obtains the set of MIDI file types for which file writing support is
provided by this file writer.

Obtains the file types that this file writer can write from the sequence
specified.

Indicates whether file writing support for the specified MIDI file type
is provided by this file writer.

Indicates whether a MIDI file of the file type specified can be written
from the sequence indicated.

Writes a stream of bytes representing a MIDI file of the file type
indicated to the external file provided.

Writes a stream of bytes representing a MIDI file of the file type
indicated to the output stream provided.

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

- MidiFileWriter

```java
public MidiFileWriter()
```

============ METHOD DETAIL ==========

- Method Detail

- getMidiFileTypes

```java
public abstract int[] getMidiFileTypes()
```

Obtains the set of MIDI file types for which file writing support is
provided by this file writer.

**Returns:** array of file types. If no file types are supported, an array of
length 0 is returned.

- getMidiFileTypes

```java
public abstract int[] getMidiFileTypes​(
Sequence
sequence)
```

Obtains the file types that this file writer can write from the sequence
specified.

**Parameters:** sequence

- the sequence for which MIDI file type support is queried
**Returns:** array of file types. If no file types are supported, returns an
array of length 0.
**Throws:** NullPointerException

- if

sequence

is

null

- isFileTypeSupported

```java
public boolean isFileTypeSupported​(int fileType)
```

Indicates whether file writing support for the specified MIDI file type
is provided by this file writer.

**Parameters:** fileType

- the file type for which write capabilities are queried
**Returns:** true

if the file type is supported, otherwise

false

- isFileTypeSupported

```java
public boolean isFileTypeSupported​(int fileType,

Sequence
sequence)
```

Indicates whether a MIDI file of the file type specified can be written
from the sequence indicated.

**Parameters:** fileType

- the file type for which write capabilities are queried
**Parameters:** sequence

- the sequence for which file writing support is queried
**Returns:** true

if the file type is supported for this sequence,
otherwise

false
**Throws:** NullPointerException

- if

sequence

is

null

- write

```java
public abstract int write​(
Sequence
in,
int fileType,

OutputStream
out)
throws
IOException
```

Writes a stream of bytes representing a MIDI file of the file type
indicated to the output stream provided.

**Parameters:** in

- sequence containing MIDI data to be written to the file
**Parameters:** fileType

- type of the file to be written to the output stream
**Parameters:** out

- stream to which the file data should be written
**Returns:** the number of bytes written to the output stream
**Throws:** IOException

- if an I/O exception occurs
**Throws:** IllegalArgumentException

- if the file type is not supported by
this file writer
**Throws:** NullPointerException

- if

in

or

out

are

null
**See Also:** isFileTypeSupported(int, Sequence)

,

getMidiFileTypes(Sequence)

- write

```java
public abstract int write​(
Sequence
in,
int fileType,

File
out)
throws
IOException
```

Writes a stream of bytes representing a MIDI file of the file type
indicated to the external file provided.

**Parameters:** in

- sequence containing MIDI data to be written to the external
file
**Parameters:** fileType

- type of the file to be written to the external file
**Parameters:** out

- external file to which the file data should be written
**Returns:** the number of bytes written to the file
**Throws:** IOException

- if an I/O exception occurs
**Throws:** IllegalArgumentException

- if the file type is not supported by
this file writer
**Throws:** NullPointerException

- if

in

or

out

are

null
**See Also:** isFileTypeSupported(int, Sequence)

,

getMidiFileTypes(Sequence)

Constructor Detail

- MidiFileWriter

```java
public MidiFileWriter()
```

---

#### Constructor Detail

MidiFileWriter

```java
public MidiFileWriter()
```

---

#### MidiFileWriter

public MidiFileWriter()

Method Detail

- getMidiFileTypes

```java
public abstract int[] getMidiFileTypes()
```

Obtains the set of MIDI file types for which file writing support is
provided by this file writer.

**Returns:** array of file types. If no file types are supported, an array of
length 0 is returned.

- getMidiFileTypes

```java
public abstract int[] getMidiFileTypes​(
Sequence
sequence)
```

Obtains the file types that this file writer can write from the sequence
specified.

**Parameters:** sequence

- the sequence for which MIDI file type support is queried
**Returns:** array of file types. If no file types are supported, returns an
array of length 0.
**Throws:** NullPointerException

- if

sequence

is

null

- isFileTypeSupported

```java
public boolean isFileTypeSupported​(int fileType)
```

Indicates whether file writing support for the specified MIDI file type
is provided by this file writer.

**Parameters:** fileType

- the file type for which write capabilities are queried
**Returns:** true

if the file type is supported, otherwise

false

- isFileTypeSupported

```java
public boolean isFileTypeSupported​(int fileType,

Sequence
sequence)
```

Indicates whether a MIDI file of the file type specified can be written
from the sequence indicated.

**Parameters:** fileType

- the file type for which write capabilities are queried
**Parameters:** sequence

- the sequence for which file writing support is queried
**Returns:** true

if the file type is supported for this sequence,
otherwise

false
**Throws:** NullPointerException

- if

sequence

is

null

- write

```java
public abstract int write​(
Sequence
in,
int fileType,

OutputStream
out)
throws
IOException
```

Writes a stream of bytes representing a MIDI file of the file type
indicated to the output stream provided.

**Parameters:** in

- sequence containing MIDI data to be written to the file
**Parameters:** fileType

- type of the file to be written to the output stream
**Parameters:** out

- stream to which the file data should be written
**Returns:** the number of bytes written to the output stream
**Throws:** IOException

- if an I/O exception occurs
**Throws:** IllegalArgumentException

- if the file type is not supported by
this file writer
**Throws:** NullPointerException

- if

in

or

out

are

null
**See Also:** isFileTypeSupported(int, Sequence)

,

getMidiFileTypes(Sequence)

- write

```java
public abstract int write​(
Sequence
in,
int fileType,

File
out)
throws
IOException
```

Writes a stream of bytes representing a MIDI file of the file type
indicated to the external file provided.

**Parameters:** in

- sequence containing MIDI data to be written to the external
file
**Parameters:** fileType

- type of the file to be written to the external file
**Parameters:** out

- external file to which the file data should be written
**Returns:** the number of bytes written to the file
**Throws:** IOException

- if an I/O exception occurs
**Throws:** IllegalArgumentException

- if the file type is not supported by
this file writer
**Throws:** NullPointerException

- if

in

or

out

are

null
**See Also:** isFileTypeSupported(int, Sequence)

,

getMidiFileTypes(Sequence)

---

#### Method Detail

getMidiFileTypes

```java
public abstract int[] getMidiFileTypes()
```

Obtains the set of MIDI file types for which file writing support is
provided by this file writer.

**Returns:** array of file types. If no file types are supported, an array of
length 0 is returned.

---

#### getMidiFileTypes

public abstract int[] getMidiFileTypes()

Obtains the set of MIDI file types for which file writing support is
provided by this file writer.

getMidiFileTypes

```java
public abstract int[] getMidiFileTypes​(
Sequence
sequence)
```

Obtains the file types that this file writer can write from the sequence
specified.

**Parameters:** sequence

- the sequence for which MIDI file type support is queried
**Returns:** array of file types. If no file types are supported, returns an
array of length 0.
**Throws:** NullPointerException

- if

sequence

is

null

---

#### getMidiFileTypes

public abstract int[] getMidiFileTypes​(

Sequence

sequence)

Obtains the file types that this file writer can write from the sequence
specified.

isFileTypeSupported

```java
public boolean isFileTypeSupported​(int fileType)
```

Indicates whether file writing support for the specified MIDI file type
is provided by this file writer.

**Parameters:** fileType

- the file type for which write capabilities are queried
**Returns:** true

if the file type is supported, otherwise

false

---

#### isFileTypeSupported

public boolean isFileTypeSupported​(int fileType)

Indicates whether file writing support for the specified MIDI file type
is provided by this file writer.

isFileTypeSupported

```java
public boolean isFileTypeSupported​(int fileType,

Sequence
sequence)
```

Indicates whether a MIDI file of the file type specified can be written
from the sequence indicated.

**Parameters:** fileType

- the file type for which write capabilities are queried
**Parameters:** sequence

- the sequence for which file writing support is queried
**Returns:** true

if the file type is supported for this sequence,
otherwise

false
**Throws:** NullPointerException

- if

sequence

is

null

---

#### isFileTypeSupported

public boolean isFileTypeSupported​(int fileType,

Sequence

sequence)

Indicates whether a MIDI file of the file type specified can be written
from the sequence indicated.

write

```java
public abstract int write​(
Sequence
in,
int fileType,

OutputStream
out)
throws
IOException
```

Writes a stream of bytes representing a MIDI file of the file type
indicated to the output stream provided.

**Parameters:** in

- sequence containing MIDI data to be written to the file
**Parameters:** fileType

- type of the file to be written to the output stream
**Parameters:** out

- stream to which the file data should be written
**Returns:** the number of bytes written to the output stream
**Throws:** IOException

- if an I/O exception occurs
**Throws:** IllegalArgumentException

- if the file type is not supported by
this file writer
**Throws:** NullPointerException

- if

in

or

out

are

null
**See Also:** isFileTypeSupported(int, Sequence)

,

getMidiFileTypes(Sequence)

---

#### write

public abstract int write​(

Sequence

in,
int fileType,

OutputStream

out)
throws

IOException

Writes a stream of bytes representing a MIDI file of the file type
indicated to the output stream provided.

write

```java
public abstract int write​(
Sequence
in,
int fileType,

File
out)
throws
IOException
```

Writes a stream of bytes representing a MIDI file of the file type
indicated to the external file provided.

**Parameters:** in

- sequence containing MIDI data to be written to the external
file
**Parameters:** fileType

- type of the file to be written to the external file
**Parameters:** out

- external file to which the file data should be written
**Returns:** the number of bytes written to the file
**Throws:** IOException

- if an I/O exception occurs
**Throws:** IllegalArgumentException

- if the file type is not supported by
this file writer
**Throws:** NullPointerException

- if

in

or

out

are

null
**See Also:** isFileTypeSupported(int, Sequence)

,

getMidiFileTypes(Sequence)

---

#### write

public abstract int write​(

Sequence

in,
int fileType,

File

out)
throws

IOException

Writes a stream of bytes representing a MIDI file of the file type
indicated to the external file provided.

---

