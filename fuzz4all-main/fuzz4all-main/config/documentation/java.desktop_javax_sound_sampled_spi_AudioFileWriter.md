# Class AudioFileWriter

**Source:** `java.desktop\javax\sound\sampled\spi\AudioFileWriter.html`

### Class Description

```java
public abstract class
AudioFileWriter

extends
Object
```

Provider for audio file writing services. Classes providing concrete
implementations can write one or more types of audio file from an audio
stream.

**Since:** 1.3

---

### Field Details

*No entries found.*

### Constructor Details

#### public AudioFileWriter()

*No description found.*

---

### Method Details

#### public abstract
AudioFileFormat.Type
[] getAudioFileTypes()

Obtains the file types for which file writing support is provided by this
audio file writer.

**Returns:**
- array of file types. If no file types are supported, an array of
length 0 is returned.

---

#### public boolean isFileTypeSupported​(
AudioFileFormat.Type
fileType)

Indicates whether file writing support for the specified file type is
provided by this audio file writer.

**Parameters:**
- fileType

- the file type for which write capabilities are queried

**Returns:**
- true

if the file type is supported, otherwise

false

**Throws:**
- NullPointerException

- if

fileType

is

null

---

#### public abstract
AudioFileFormat.Type
[] getAudioFileTypes​(
AudioInputStream
stream)

Obtains the file types that this audio file writer can write from the
audio input stream specified.

**Parameters:**
- stream

- the audio input stream for which audio file type support
is queried

**Returns:**
- array of file types. If no file types are supported, an array of
length 0 is returned.

**Throws:**
- NullPointerException

- if

stream

is

null

---

#### public boolean isFileTypeSupported​(
AudioFileFormat.Type
fileType,

AudioInputStream
stream)

Indicates whether an audio file of the type specified can be written from
the audio input stream indicated.

**Parameters:**
- fileType

- file type for which write capabilities are queried
- stream

- for which file writing support is queried

**Returns:**
- true

if the file type is supported for this audio input
stream, otherwise

false

**Throws:**
- NullPointerException

- if

fileType

or

stream

are

null

---

#### public abstract int write​(
AudioInputStream
stream,

AudioFileFormat.Type
fileType,

OutputStream
out)
throws
IOException

Writes a stream of bytes representing an audio file of the file type
indicated to the output stream provided. Some file types require that the
length be written into the file header, and cannot be written from start
to finish unless the length is known in advance. An attempt to write such
a file type will fail with an

IOException

if the length in the
audio file format is

AudioSystem.NOT_SPECIFIED

.

**Parameters:**
- stream

- the audio input stream containing audio data to be written
to the output stream
- fileType

- file type to be written to the output stream
- out

- stream to which the file data should be written

**Returns:**
- the number of bytes written to the output stream

**Throws:**
- IOException

- if an I/O exception occurs
- IllegalArgumentException

- if the file type is not supported by the
system
- NullPointerException

- if

stream

or

fileType

or

out

are

null

**See Also:**
- isFileTypeSupported(Type, AudioInputStream)

,

getAudioFileTypes()

---

#### public abstract int write​(
AudioInputStream
stream,

AudioFileFormat.Type
fileType,

File
out)
throws
IOException

Writes a stream of bytes representing an audio file of the file format
indicated to the external file provided.

**Parameters:**
- stream

- the audio input stream containing audio data to be written
to the file
- fileType

- file type to be written to the file
- out

- external file to which the file data should be written

**Returns:**
- the number of bytes written to the file

**Throws:**
- IOException

- if an I/O exception occurs
- IllegalArgumentException

- if the file format is not supported by
the system
- NullPointerException

- if

stream

or

fileType

or

out

are

null

**See Also:**
- isFileTypeSupported(Type, AudioInputStream)

,

getAudioFileTypes()

---

### Additional Sections

#### Class AudioFileWriter

java.lang.Object

- javax.sound.sampled.spi.AudioFileWriter

javax.sound.sampled.spi.AudioFileWriter

```java
public abstract class
AudioFileWriter

extends
Object
```

Provider for audio file writing services. Classes providing concrete
implementations can write one or more types of audio file from an audio
stream.

**Since:** 1.3

public abstract class

AudioFileWriter

extends

Object

Provider for audio file writing services. Classes providing concrete
implementations can write one or more types of audio file from an audio
stream.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

AudioFileWriter

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

abstract

AudioFileFormat.Type

[]

getAudioFileTypes

()

Obtains the file types for which file writing support is provided by this
audio file writer.

abstract

AudioFileFormat.Type

[]

getAudioFileTypes

​(

AudioInputStream

stream)

Obtains the file types that this audio file writer can write from the
audio input stream specified.

boolean

isFileTypeSupported

​(

AudioFileFormat.Type

fileType)

Indicates whether file writing support for the specified file type is
provided by this audio file writer.

boolean

isFileTypeSupported

​(

AudioFileFormat.Type

fileType,

AudioInputStream

stream)

Indicates whether an audio file of the type specified can be written from
the audio input stream indicated.

abstract int

write

​(

AudioInputStream

stream,

AudioFileFormat.Type

fileType,

File

out)

Writes a stream of bytes representing an audio file of the file format
indicated to the external file provided.

abstract int

write

​(

AudioInputStream

stream,

AudioFileFormat.Type

fileType,

OutputStream

out)

Writes a stream of bytes representing an audio file of the file type
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

AudioFileWriter

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

abstract

AudioFileFormat.Type

[]

getAudioFileTypes

()

Obtains the file types for which file writing support is provided by this
audio file writer.

abstract

AudioFileFormat.Type

[]

getAudioFileTypes

​(

AudioInputStream

stream)

Obtains the file types that this audio file writer can write from the
audio input stream specified.

boolean

isFileTypeSupported

​(

AudioFileFormat.Type

fileType)

Indicates whether file writing support for the specified file type is
provided by this audio file writer.

boolean

isFileTypeSupported

​(

AudioFileFormat.Type

fileType,

AudioInputStream

stream)

Indicates whether an audio file of the type specified can be written from
the audio input stream indicated.

abstract int

write

​(

AudioInputStream

stream,

AudioFileFormat.Type

fileType,

File

out)

Writes a stream of bytes representing an audio file of the file format
indicated to the external file provided.

abstract int

write

​(

AudioInputStream

stream,

AudioFileFormat.Type

fileType,

OutputStream

out)

Writes a stream of bytes representing an audio file of the file type
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

Obtains the file types for which file writing support is provided by this
audio file writer.

Obtains the file types that this audio file writer can write from the
audio input stream specified.

Indicates whether file writing support for the specified file type is
provided by this audio file writer.

Indicates whether an audio file of the type specified can be written from
the audio input stream indicated.

Writes a stream of bytes representing an audio file of the file format
indicated to the external file provided.

Writes a stream of bytes representing an audio file of the file type
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

- AudioFileWriter

```java
public AudioFileWriter()
```

============ METHOD DETAIL ==========

- Method Detail

- getAudioFileTypes

```java
public abstract
AudioFileFormat.Type
[] getAudioFileTypes()
```

Obtains the file types for which file writing support is provided by this
audio file writer.

**Returns:** array of file types. If no file types are supported, an array of
length 0 is returned.

- isFileTypeSupported

```java
public boolean isFileTypeSupported​(
AudioFileFormat.Type
fileType)
```

Indicates whether file writing support for the specified file type is
provided by this audio file writer.

**Parameters:** fileType

- the file type for which write capabilities are queried
**Returns:** true

if the file type is supported, otherwise

false
**Throws:** NullPointerException

- if

fileType

is

null

- getAudioFileTypes

```java
public abstract
AudioFileFormat.Type
[] getAudioFileTypes​(
AudioInputStream
stream)
```

Obtains the file types that this audio file writer can write from the
audio input stream specified.

**Parameters:** stream

- the audio input stream for which audio file type support
is queried
**Returns:** array of file types. If no file types are supported, an array of
length 0 is returned.
**Throws:** NullPointerException

- if

stream

is

null

- isFileTypeSupported

```java
public boolean isFileTypeSupported​(
AudioFileFormat.Type
fileType,

AudioInputStream
stream)
```

Indicates whether an audio file of the type specified can be written from
the audio input stream indicated.

**Parameters:** fileType

- file type for which write capabilities are queried
**Parameters:** stream

- for which file writing support is queried
**Returns:** true

if the file type is supported for this audio input
stream, otherwise

false
**Throws:** NullPointerException

- if

fileType

or

stream

are

null

- write

```java
public abstract int write​(
AudioInputStream
stream,

AudioFileFormat.Type
fileType,

OutputStream
out)
throws
IOException
```

Writes a stream of bytes representing an audio file of the file type
indicated to the output stream provided. Some file types require that the
length be written into the file header, and cannot be written from start
to finish unless the length is known in advance. An attempt to write such
a file type will fail with an

IOException

if the length in the
audio file format is

AudioSystem.NOT_SPECIFIED

.

**Parameters:** stream

- the audio input stream containing audio data to be written
to the output stream
**Parameters:** fileType

- file type to be written to the output stream
**Parameters:** out

- stream to which the file data should be written
**Returns:** the number of bytes written to the output stream
**Throws:** IOException

- if an I/O exception occurs
**Throws:** IllegalArgumentException

- if the file type is not supported by the
system
**Throws:** NullPointerException

- if

stream

or

fileType

or

out

are

null
**See Also:** isFileTypeSupported(Type, AudioInputStream)

,

getAudioFileTypes()

- write

```java
public abstract int write​(
AudioInputStream
stream,

AudioFileFormat.Type
fileType,

File
out)
throws
IOException
```

Writes a stream of bytes representing an audio file of the file format
indicated to the external file provided.

**Parameters:** stream

- the audio input stream containing audio data to be written
to the file
**Parameters:** fileType

- file type to be written to the file
**Parameters:** out

- external file to which the file data should be written
**Returns:** the number of bytes written to the file
**Throws:** IOException

- if an I/O exception occurs
**Throws:** IllegalArgumentException

- if the file format is not supported by
the system
**Throws:** NullPointerException

- if

stream

or

fileType

or

out

are

null
**See Also:** isFileTypeSupported(Type, AudioInputStream)

,

getAudioFileTypes()

Constructor Detail

- AudioFileWriter

```java
public AudioFileWriter()
```

---

#### Constructor Detail

AudioFileWriter

```java
public AudioFileWriter()
```

---

#### AudioFileWriter

public AudioFileWriter()

Method Detail

- getAudioFileTypes

```java
public abstract
AudioFileFormat.Type
[] getAudioFileTypes()
```

Obtains the file types for which file writing support is provided by this
audio file writer.

**Returns:** array of file types. If no file types are supported, an array of
length 0 is returned.

- isFileTypeSupported

```java
public boolean isFileTypeSupported​(
AudioFileFormat.Type
fileType)
```

Indicates whether file writing support for the specified file type is
provided by this audio file writer.

**Parameters:** fileType

- the file type for which write capabilities are queried
**Returns:** true

if the file type is supported, otherwise

false
**Throws:** NullPointerException

- if

fileType

is

null

- getAudioFileTypes

```java
public abstract
AudioFileFormat.Type
[] getAudioFileTypes​(
AudioInputStream
stream)
```

Obtains the file types that this audio file writer can write from the
audio input stream specified.

**Parameters:** stream

- the audio input stream for which audio file type support
is queried
**Returns:** array of file types. If no file types are supported, an array of
length 0 is returned.
**Throws:** NullPointerException

- if

stream

is

null

- isFileTypeSupported

```java
public boolean isFileTypeSupported​(
AudioFileFormat.Type
fileType,

AudioInputStream
stream)
```

Indicates whether an audio file of the type specified can be written from
the audio input stream indicated.

**Parameters:** fileType

- file type for which write capabilities are queried
**Parameters:** stream

- for which file writing support is queried
**Returns:** true

if the file type is supported for this audio input
stream, otherwise

false
**Throws:** NullPointerException

- if

fileType

or

stream

are

null

- write

```java
public abstract int write​(
AudioInputStream
stream,

AudioFileFormat.Type
fileType,

OutputStream
out)
throws
IOException
```

Writes a stream of bytes representing an audio file of the file type
indicated to the output stream provided. Some file types require that the
length be written into the file header, and cannot be written from start
to finish unless the length is known in advance. An attempt to write such
a file type will fail with an

IOException

if the length in the
audio file format is

AudioSystem.NOT_SPECIFIED

.

**Parameters:** stream

- the audio input stream containing audio data to be written
to the output stream
**Parameters:** fileType

- file type to be written to the output stream
**Parameters:** out

- stream to which the file data should be written
**Returns:** the number of bytes written to the output stream
**Throws:** IOException

- if an I/O exception occurs
**Throws:** IllegalArgumentException

- if the file type is not supported by the
system
**Throws:** NullPointerException

- if

stream

or

fileType

or

out

are

null
**See Also:** isFileTypeSupported(Type, AudioInputStream)

,

getAudioFileTypes()

- write

```java
public abstract int write​(
AudioInputStream
stream,

AudioFileFormat.Type
fileType,

File
out)
throws
IOException
```

Writes a stream of bytes representing an audio file of the file format
indicated to the external file provided.

**Parameters:** stream

- the audio input stream containing audio data to be written
to the file
**Parameters:** fileType

- file type to be written to the file
**Parameters:** out

- external file to which the file data should be written
**Returns:** the number of bytes written to the file
**Throws:** IOException

- if an I/O exception occurs
**Throws:** IllegalArgumentException

- if the file format is not supported by
the system
**Throws:** NullPointerException

- if

stream

or

fileType

or

out

are

null
**See Also:** isFileTypeSupported(Type, AudioInputStream)

,

getAudioFileTypes()

---

#### Method Detail

getAudioFileTypes

```java
public abstract
AudioFileFormat.Type
[] getAudioFileTypes()
```

Obtains the file types for which file writing support is provided by this
audio file writer.

**Returns:** array of file types. If no file types are supported, an array of
length 0 is returned.

---

#### getAudioFileTypes

public abstract

AudioFileFormat.Type

[] getAudioFileTypes()

Obtains the file types for which file writing support is provided by this
audio file writer.

isFileTypeSupported

```java
public boolean isFileTypeSupported​(
AudioFileFormat.Type
fileType)
```

Indicates whether file writing support for the specified file type is
provided by this audio file writer.

**Parameters:** fileType

- the file type for which write capabilities are queried
**Returns:** true

if the file type is supported, otherwise

false
**Throws:** NullPointerException

- if

fileType

is

null

---

#### isFileTypeSupported

public boolean isFileTypeSupported​(

AudioFileFormat.Type

fileType)

Indicates whether file writing support for the specified file type is
provided by this audio file writer.

getAudioFileTypes

```java
public abstract
AudioFileFormat.Type
[] getAudioFileTypes​(
AudioInputStream
stream)
```

Obtains the file types that this audio file writer can write from the
audio input stream specified.

**Parameters:** stream

- the audio input stream for which audio file type support
is queried
**Returns:** array of file types. If no file types are supported, an array of
length 0 is returned.
**Throws:** NullPointerException

- if

stream

is

null

---

#### getAudioFileTypes

public abstract

AudioFileFormat.Type

[] getAudioFileTypes​(

AudioInputStream

stream)

Obtains the file types that this audio file writer can write from the
audio input stream specified.

isFileTypeSupported

```java
public boolean isFileTypeSupported​(
AudioFileFormat.Type
fileType,

AudioInputStream
stream)
```

Indicates whether an audio file of the type specified can be written from
the audio input stream indicated.

**Parameters:** fileType

- file type for which write capabilities are queried
**Parameters:** stream

- for which file writing support is queried
**Returns:** true

if the file type is supported for this audio input
stream, otherwise

false
**Throws:** NullPointerException

- if

fileType

or

stream

are

null

---

#### isFileTypeSupported

public boolean isFileTypeSupported​(

AudioFileFormat.Type

fileType,

AudioInputStream

stream)

Indicates whether an audio file of the type specified can be written from
the audio input stream indicated.

write

```java
public abstract int write​(
AudioInputStream
stream,

AudioFileFormat.Type
fileType,

OutputStream
out)
throws
IOException
```

Writes a stream of bytes representing an audio file of the file type
indicated to the output stream provided. Some file types require that the
length be written into the file header, and cannot be written from start
to finish unless the length is known in advance. An attempt to write such
a file type will fail with an

IOException

if the length in the
audio file format is

AudioSystem.NOT_SPECIFIED

.

**Parameters:** stream

- the audio input stream containing audio data to be written
to the output stream
**Parameters:** fileType

- file type to be written to the output stream
**Parameters:** out

- stream to which the file data should be written
**Returns:** the number of bytes written to the output stream
**Throws:** IOException

- if an I/O exception occurs
**Throws:** IllegalArgumentException

- if the file type is not supported by the
system
**Throws:** NullPointerException

- if

stream

or

fileType

or

out

are

null
**See Also:** isFileTypeSupported(Type, AudioInputStream)

,

getAudioFileTypes()

---

#### write

public abstract int write​(

AudioInputStream

stream,

AudioFileFormat.Type

fileType,

OutputStream

out)
throws

IOException

Writes a stream of bytes representing an audio file of the file type
indicated to the output stream provided. Some file types require that the
length be written into the file header, and cannot be written from start
to finish unless the length is known in advance. An attempt to write such
a file type will fail with an

IOException

if the length in the
audio file format is

AudioSystem.NOT_SPECIFIED

.

write

```java
public abstract int write​(
AudioInputStream
stream,

AudioFileFormat.Type
fileType,

File
out)
throws
IOException
```

Writes a stream of bytes representing an audio file of the file format
indicated to the external file provided.

**Parameters:** stream

- the audio input stream containing audio data to be written
to the file
**Parameters:** fileType

- file type to be written to the file
**Parameters:** out

- external file to which the file data should be written
**Returns:** the number of bytes written to the file
**Throws:** IOException

- if an I/O exception occurs
**Throws:** IllegalArgumentException

- if the file format is not supported by
the system
**Throws:** NullPointerException

- if

stream

or

fileType

or

out

are

null
**See Also:** isFileTypeSupported(Type, AudioInputStream)

,

getAudioFileTypes()

---

#### write

public abstract int write​(

AudioInputStream

stream,

AudioFileFormat.Type

fileType,

File

out)
throws

IOException

Writes a stream of bytes representing an audio file of the file format
indicated to the external file provided.

---

