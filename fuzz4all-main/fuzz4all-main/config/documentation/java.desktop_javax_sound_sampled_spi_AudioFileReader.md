# Class AudioFileReader

**Source:** `java.desktop\javax\sound\sampled\spi\AudioFileReader.html`

### Class Description

```java
public abstract class
AudioFileReader

extends
Object
```

Provider for audio file reading services. Classes providing concrete
implementations can parse the format information from one or more types of
audio file, and can produce audio input streams from files of these types.

**Since:** 1.3

---

### Field Details

*No entries found.*

### Constructor Details

#### public AudioFileReader()

*No description found.*

---

### Method Details

#### public abstract
AudioFileFormat
getAudioFileFormat​(
InputStream
stream)
throws
UnsupportedAudioFileException
,

IOException

Obtains the audio file format of the input stream provided. The stream
must point to valid audio file data. In general, audio file readers may
need to read some data from the stream before determining whether they
support it. These parsers must be able to mark the stream, read enough
data to determine whether they support the stream, and reset the stream's
read pointer to its original position. If the input stream does not
support this, this method may fail with an

IOException

.

**Parameters:**
- stream

- the input stream from which file format information should
be extracted

**Returns:**
- an

AudioFileFormat

object describing the audio file
format

**Throws:**
- UnsupportedAudioFileException

- if the stream does not point to
valid audio file data recognized by the system
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
AudioFileFormat
getAudioFileFormat​(
URL
url)
throws
UnsupportedAudioFileException
,

IOException

Obtains the audio file format of the

URL

provided. The

URL

must point to valid audio file data.

**Parameters:**
- url

- the

URL

from which file format information should be
extracted

**Returns:**
- an

AudioFileFormat

object describing the audio file
format

**Throws:**
- UnsupportedAudioFileException

- if the

URL

does not point
to valid audio file data recognized by the system
- IOException

- if an I/O exception occurs
- NullPointerException

- if

url

is

null

---

#### public abstract
AudioFileFormat
getAudioFileFormat​(
File
file)
throws
UnsupportedAudioFileException
,

IOException

Obtains the audio file format of the

File

provided. The

File

must point to valid audio file data.

**Parameters:**
- file

- the

File

from which file format information should
be extracted

**Returns:**
- an

AudioFileFormat

object describing the audio file
format

**Throws:**
- UnsupportedAudioFileException

- if the

File

does not point
to valid audio file data recognized by the system
- IOException

- if an I/O exception occurs
- NullPointerException

- if

file

is

null

---

#### public abstract
AudioInputStream
getAudioInputStream​(
InputStream
stream)
throws
UnsupportedAudioFileException
,

IOException

Obtains an audio input stream from the input stream provided. The stream
must point to valid audio file data. In general, audio file readers may
need to read some data from the stream before determining whether they
support it. These parsers must be able to mark the stream, read enough
data to determine whether they support the stream, and reset the stream's
read pointer to its original position. If the input stream does not
support this, this method may fail with an

IOException

.

**Parameters:**
- stream

- the input stream from which the

AudioInputStream

should be constructed

**Returns:**
- an

AudioInputStream

object based on the audio file data
contained in the input stream

**Throws:**
- UnsupportedAudioFileException

- if the stream does not point to
valid audio file data recognized by the system
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
AudioInputStream
getAudioInputStream​(
URL
url)
throws
UnsupportedAudioFileException
,

IOException

Obtains an audio input stream from the

URL

provided. The

URL

must point to valid audio file data.

**Parameters:**
- url

- the

URL

for which the

AudioInputStream

should
be constructed

**Returns:**
- an

AudioInputStream

object based on the audio file data
pointed to by the

URL

**Throws:**
- UnsupportedAudioFileException

- if the

URL

does not point
to valid audio file data recognized by the system
- IOException

- if an I/O exception occurs
- NullPointerException

- if

url

is

null

---

#### public abstract
AudioInputStream
getAudioInputStream​(
File
file)
throws
UnsupportedAudioFileException
,

IOException

Obtains an audio input stream from the

File

provided. The

File

must point to valid audio file data.

**Parameters:**
- file

- the

File

for which the

AudioInputStream

should be constructed

**Returns:**
- an

AudioInputStream

object based on the audio file data
pointed to by the File

**Throws:**
- UnsupportedAudioFileException

- if the

File

does not point
to valid audio file data recognized by the system
- IOException

- if an I/O exception occurs
- NullPointerException

- if

file

is

null

---

### Additional Sections

#### Class AudioFileReader

java.lang.Object

- javax.sound.sampled.spi.AudioFileReader

javax.sound.sampled.spi.AudioFileReader

```java
public abstract class
AudioFileReader

extends
Object
```

Provider for audio file reading services. Classes providing concrete
implementations can parse the format information from one or more types of
audio file, and can produce audio input streams from files of these types.

**Since:** 1.3

public abstract class

AudioFileReader

extends

Object

Provider for audio file reading services. Classes providing concrete
implementations can parse the format information from one or more types of
audio file, and can produce audio input streams from files of these types.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

AudioFileReader

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

AudioFileFormat

getAudioFileFormat

​(

File

file)

Obtains the audio file format of the

File

provided.

abstract

AudioFileFormat

getAudioFileFormat

​(

InputStream

stream)

Obtains the audio file format of the input stream provided.

abstract

AudioFileFormat

getAudioFileFormat

​(

URL

url)

Obtains the audio file format of the

URL

provided.

abstract

AudioInputStream

getAudioInputStream

​(

File

file)

Obtains an audio input stream from the

File

provided.

abstract

AudioInputStream

getAudioInputStream

​(

InputStream

stream)

Obtains an audio input stream from the input stream provided.

abstract

AudioInputStream

getAudioInputStream

​(

URL

url)

Obtains an audio input stream from the

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

AudioFileReader

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

AudioFileFormat

getAudioFileFormat

​(

File

file)

Obtains the audio file format of the

File

provided.

abstract

AudioFileFormat

getAudioFileFormat

​(

InputStream

stream)

Obtains the audio file format of the input stream provided.

abstract

AudioFileFormat

getAudioFileFormat

​(

URL

url)

Obtains the audio file format of the

URL

provided.

abstract

AudioInputStream

getAudioInputStream

​(

File

file)

Obtains an audio input stream from the

File

provided.

abstract

AudioInputStream

getAudioInputStream

​(

InputStream

stream)

Obtains an audio input stream from the input stream provided.

abstract

AudioInputStream

getAudioInputStream

​(

URL

url)

Obtains an audio input stream from the

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

Obtains the audio file format of the

File

provided.

Obtains the audio file format of the input stream provided.

Obtains the audio file format of the

URL

provided.

Obtains an audio input stream from the

File

provided.

Obtains an audio input stream from the input stream provided.

Obtains an audio input stream from the

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

- AudioFileReader

```java
public AudioFileReader()
```

============ METHOD DETAIL ==========

- Method Detail

- getAudioFileFormat

```java
public abstract
AudioFileFormat
getAudioFileFormat​(
InputStream
stream)
throws
UnsupportedAudioFileException
,

IOException
```

Obtains the audio file format of the input stream provided. The stream
must point to valid audio file data. In general, audio file readers may
need to read some data from the stream before determining whether they
support it. These parsers must be able to mark the stream, read enough
data to determine whether they support the stream, and reset the stream's
read pointer to its original position. If the input stream does not
support this, this method may fail with an

IOException

.

**Parameters:** stream

- the input stream from which file format information should
be extracted
**Returns:** an

AudioFileFormat

object describing the audio file
format
**Throws:** UnsupportedAudioFileException

- if the stream does not point to
valid audio file data recognized by the system
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

- getAudioFileFormat

```java
public abstract
AudioFileFormat
getAudioFileFormat​(
URL
url)
throws
UnsupportedAudioFileException
,

IOException
```

Obtains the audio file format of the

URL

provided. The

URL

must point to valid audio file data.

**Parameters:** url

- the

URL

from which file format information should be
extracted
**Returns:** an

AudioFileFormat

object describing the audio file
format
**Throws:** UnsupportedAudioFileException

- if the

URL

does not point
to valid audio file data recognized by the system
**Throws:** IOException

- if an I/O exception occurs
**Throws:** NullPointerException

- if

url

is

null

- getAudioFileFormat

```java
public abstract
AudioFileFormat
getAudioFileFormat​(
File
file)
throws
UnsupportedAudioFileException
,

IOException
```

Obtains the audio file format of the

File

provided. The

File

must point to valid audio file data.

**Parameters:** file

- the

File

from which file format information should
be extracted
**Returns:** an

AudioFileFormat

object describing the audio file
format
**Throws:** UnsupportedAudioFileException

- if the

File

does not point
to valid audio file data recognized by the system
**Throws:** IOException

- if an I/O exception occurs
**Throws:** NullPointerException

- if

file

is

null

- getAudioInputStream

```java
public abstract
AudioInputStream
getAudioInputStream​(
InputStream
stream)
throws
UnsupportedAudioFileException
,

IOException
```

Obtains an audio input stream from the input stream provided. The stream
must point to valid audio file data. In general, audio file readers may
need to read some data from the stream before determining whether they
support it. These parsers must be able to mark the stream, read enough
data to determine whether they support the stream, and reset the stream's
read pointer to its original position. If the input stream does not
support this, this method may fail with an

IOException

.

**Parameters:** stream

- the input stream from which the

AudioInputStream

should be constructed
**Returns:** an

AudioInputStream

object based on the audio file data
contained in the input stream
**Throws:** UnsupportedAudioFileException

- if the stream does not point to
valid audio file data recognized by the system
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

- getAudioInputStream

```java
public abstract
AudioInputStream
getAudioInputStream​(
URL
url)
throws
UnsupportedAudioFileException
,

IOException
```

Obtains an audio input stream from the

URL

provided. The

URL

must point to valid audio file data.

**Parameters:** url

- the

URL

for which the

AudioInputStream

should
be constructed
**Returns:** an

AudioInputStream

object based on the audio file data
pointed to by the

URL
**Throws:** UnsupportedAudioFileException

- if the

URL

does not point
to valid audio file data recognized by the system
**Throws:** IOException

- if an I/O exception occurs
**Throws:** NullPointerException

- if

url

is

null

- getAudioInputStream

```java
public abstract
AudioInputStream
getAudioInputStream​(
File
file)
throws
UnsupportedAudioFileException
,

IOException
```

Obtains an audio input stream from the

File

provided. The

File

must point to valid audio file data.

**Parameters:** file

- the

File

for which the

AudioInputStream

should be constructed
**Returns:** an

AudioInputStream

object based on the audio file data
pointed to by the File
**Throws:** UnsupportedAudioFileException

- if the

File

does not point
to valid audio file data recognized by the system
**Throws:** IOException

- if an I/O exception occurs
**Throws:** NullPointerException

- if

file

is

null

Constructor Detail

- AudioFileReader

```java
public AudioFileReader()
```

---

#### Constructor Detail

AudioFileReader

```java
public AudioFileReader()
```

---

#### AudioFileReader

public AudioFileReader()

Method Detail

- getAudioFileFormat

```java
public abstract
AudioFileFormat
getAudioFileFormat​(
InputStream
stream)
throws
UnsupportedAudioFileException
,

IOException
```

Obtains the audio file format of the input stream provided. The stream
must point to valid audio file data. In general, audio file readers may
need to read some data from the stream before determining whether they
support it. These parsers must be able to mark the stream, read enough
data to determine whether they support the stream, and reset the stream's
read pointer to its original position. If the input stream does not
support this, this method may fail with an

IOException

.

**Parameters:** stream

- the input stream from which file format information should
be extracted
**Returns:** an

AudioFileFormat

object describing the audio file
format
**Throws:** UnsupportedAudioFileException

- if the stream does not point to
valid audio file data recognized by the system
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

- getAudioFileFormat

```java
public abstract
AudioFileFormat
getAudioFileFormat​(
URL
url)
throws
UnsupportedAudioFileException
,

IOException
```

Obtains the audio file format of the

URL

provided. The

URL

must point to valid audio file data.

**Parameters:** url

- the

URL

from which file format information should be
extracted
**Returns:** an

AudioFileFormat

object describing the audio file
format
**Throws:** UnsupportedAudioFileException

- if the

URL

does not point
to valid audio file data recognized by the system
**Throws:** IOException

- if an I/O exception occurs
**Throws:** NullPointerException

- if

url

is

null

- getAudioFileFormat

```java
public abstract
AudioFileFormat
getAudioFileFormat​(
File
file)
throws
UnsupportedAudioFileException
,

IOException
```

Obtains the audio file format of the

File

provided. The

File

must point to valid audio file data.

**Parameters:** file

- the

File

from which file format information should
be extracted
**Returns:** an

AudioFileFormat

object describing the audio file
format
**Throws:** UnsupportedAudioFileException

- if the

File

does not point
to valid audio file data recognized by the system
**Throws:** IOException

- if an I/O exception occurs
**Throws:** NullPointerException

- if

file

is

null

- getAudioInputStream

```java
public abstract
AudioInputStream
getAudioInputStream​(
InputStream
stream)
throws
UnsupportedAudioFileException
,

IOException
```

Obtains an audio input stream from the input stream provided. The stream
must point to valid audio file data. In general, audio file readers may
need to read some data from the stream before determining whether they
support it. These parsers must be able to mark the stream, read enough
data to determine whether they support the stream, and reset the stream's
read pointer to its original position. If the input stream does not
support this, this method may fail with an

IOException

.

**Parameters:** stream

- the input stream from which the

AudioInputStream

should be constructed
**Returns:** an

AudioInputStream

object based on the audio file data
contained in the input stream
**Throws:** UnsupportedAudioFileException

- if the stream does not point to
valid audio file data recognized by the system
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

- getAudioInputStream

```java
public abstract
AudioInputStream
getAudioInputStream​(
URL
url)
throws
UnsupportedAudioFileException
,

IOException
```

Obtains an audio input stream from the

URL

provided. The

URL

must point to valid audio file data.

**Parameters:** url

- the

URL

for which the

AudioInputStream

should
be constructed
**Returns:** an

AudioInputStream

object based on the audio file data
pointed to by the

URL
**Throws:** UnsupportedAudioFileException

- if the

URL

does not point
to valid audio file data recognized by the system
**Throws:** IOException

- if an I/O exception occurs
**Throws:** NullPointerException

- if

url

is

null

- getAudioInputStream

```java
public abstract
AudioInputStream
getAudioInputStream​(
File
file)
throws
UnsupportedAudioFileException
,

IOException
```

Obtains an audio input stream from the

File

provided. The

File

must point to valid audio file data.

**Parameters:** file

- the

File

for which the

AudioInputStream

should be constructed
**Returns:** an

AudioInputStream

object based on the audio file data
pointed to by the File
**Throws:** UnsupportedAudioFileException

- if the

File

does not point
to valid audio file data recognized by the system
**Throws:** IOException

- if an I/O exception occurs
**Throws:** NullPointerException

- if

file

is

null

---

#### Method Detail

getAudioFileFormat

```java
public abstract
AudioFileFormat
getAudioFileFormat​(
InputStream
stream)
throws
UnsupportedAudioFileException
,

IOException
```

Obtains the audio file format of the input stream provided. The stream
must point to valid audio file data. In general, audio file readers may
need to read some data from the stream before determining whether they
support it. These parsers must be able to mark the stream, read enough
data to determine whether they support the stream, and reset the stream's
read pointer to its original position. If the input stream does not
support this, this method may fail with an

IOException

.

**Parameters:** stream

- the input stream from which file format information should
be extracted
**Returns:** an

AudioFileFormat

object describing the audio file
format
**Throws:** UnsupportedAudioFileException

- if the stream does not point to
valid audio file data recognized by the system
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

#### getAudioFileFormat

public abstract

AudioFileFormat

getAudioFileFormat​(

InputStream

stream)
throws

UnsupportedAudioFileException

,

IOException

Obtains the audio file format of the input stream provided. The stream
must point to valid audio file data. In general, audio file readers may
need to read some data from the stream before determining whether they
support it. These parsers must be able to mark the stream, read enough
data to determine whether they support the stream, and reset the stream's
read pointer to its original position. If the input stream does not
support this, this method may fail with an

IOException

.

getAudioFileFormat

```java
public abstract
AudioFileFormat
getAudioFileFormat​(
URL
url)
throws
UnsupportedAudioFileException
,

IOException
```

Obtains the audio file format of the

URL

provided. The

URL

must point to valid audio file data.

**Parameters:** url

- the

URL

from which file format information should be
extracted
**Returns:** an

AudioFileFormat

object describing the audio file
format
**Throws:** UnsupportedAudioFileException

- if the

URL

does not point
to valid audio file data recognized by the system
**Throws:** IOException

- if an I/O exception occurs
**Throws:** NullPointerException

- if

url

is

null

---

#### getAudioFileFormat

public abstract

AudioFileFormat

getAudioFileFormat​(

URL

url)
throws

UnsupportedAudioFileException

,

IOException

Obtains the audio file format of the

URL

provided. The

URL

must point to valid audio file data.

getAudioFileFormat

```java
public abstract
AudioFileFormat
getAudioFileFormat​(
File
file)
throws
UnsupportedAudioFileException
,

IOException
```

Obtains the audio file format of the

File

provided. The

File

must point to valid audio file data.

**Parameters:** file

- the

File

from which file format information should
be extracted
**Returns:** an

AudioFileFormat

object describing the audio file
format
**Throws:** UnsupportedAudioFileException

- if the

File

does not point
to valid audio file data recognized by the system
**Throws:** IOException

- if an I/O exception occurs
**Throws:** NullPointerException

- if

file

is

null

---

#### getAudioFileFormat

public abstract

AudioFileFormat

getAudioFileFormat​(

File

file)
throws

UnsupportedAudioFileException

,

IOException

Obtains the audio file format of the

File

provided. The

File

must point to valid audio file data.

getAudioInputStream

```java
public abstract
AudioInputStream
getAudioInputStream​(
InputStream
stream)
throws
UnsupportedAudioFileException
,

IOException
```

Obtains an audio input stream from the input stream provided. The stream
must point to valid audio file data. In general, audio file readers may
need to read some data from the stream before determining whether they
support it. These parsers must be able to mark the stream, read enough
data to determine whether they support the stream, and reset the stream's
read pointer to its original position. If the input stream does not
support this, this method may fail with an

IOException

.

**Parameters:** stream

- the input stream from which the

AudioInputStream

should be constructed
**Returns:** an

AudioInputStream

object based on the audio file data
contained in the input stream
**Throws:** UnsupportedAudioFileException

- if the stream does not point to
valid audio file data recognized by the system
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

#### getAudioInputStream

public abstract

AudioInputStream

getAudioInputStream​(

InputStream

stream)
throws

UnsupportedAudioFileException

,

IOException

Obtains an audio input stream from the input stream provided. The stream
must point to valid audio file data. In general, audio file readers may
need to read some data from the stream before determining whether they
support it. These parsers must be able to mark the stream, read enough
data to determine whether they support the stream, and reset the stream's
read pointer to its original position. If the input stream does not
support this, this method may fail with an

IOException

.

getAudioInputStream

```java
public abstract
AudioInputStream
getAudioInputStream​(
URL
url)
throws
UnsupportedAudioFileException
,

IOException
```

Obtains an audio input stream from the

URL

provided. The

URL

must point to valid audio file data.

**Parameters:** url

- the

URL

for which the

AudioInputStream

should
be constructed
**Returns:** an

AudioInputStream

object based on the audio file data
pointed to by the

URL
**Throws:** UnsupportedAudioFileException

- if the

URL

does not point
to valid audio file data recognized by the system
**Throws:** IOException

- if an I/O exception occurs
**Throws:** NullPointerException

- if

url

is

null

---

#### getAudioInputStream

public abstract

AudioInputStream

getAudioInputStream​(

URL

url)
throws

UnsupportedAudioFileException

,

IOException

Obtains an audio input stream from the

URL

provided. The

URL

must point to valid audio file data.

getAudioInputStream

```java
public abstract
AudioInputStream
getAudioInputStream​(
File
file)
throws
UnsupportedAudioFileException
,

IOException
```

Obtains an audio input stream from the

File

provided. The

File

must point to valid audio file data.

**Parameters:** file

- the

File

for which the

AudioInputStream

should be constructed
**Returns:** an

AudioInputStream

object based on the audio file data
pointed to by the File
**Throws:** UnsupportedAudioFileException

- if the

File

does not point
to valid audio file data recognized by the system
**Throws:** IOException

- if an I/O exception occurs
**Throws:** NullPointerException

- if

file

is

null

---

#### getAudioInputStream

public abstract

AudioInputStream

getAudioInputStream​(

File

file)
throws

UnsupportedAudioFileException

,

IOException

Obtains an audio input stream from the

File

provided. The

File

must point to valid audio file data.

---

