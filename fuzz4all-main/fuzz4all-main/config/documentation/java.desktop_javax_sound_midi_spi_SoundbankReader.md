# Class SoundbankReader

**Source:** `java.desktop\javax\sound\midi\spi\SoundbankReader.html`

### Class Description

```java
public abstract class
SoundbankReader

extends
Object
```

A

SoundbankReader

supplies soundbank file-reading services. Concrete
subclasses of

SoundbankReader

parse a given soundbank file, producing
a

Soundbank

object that can be loaded into a

Synthesizer

.

**Since:** 1.3

---

### Field Details

*No entries found.*

### Constructor Details

#### public SoundbankReader()

*No description found.*

---

### Method Details

#### public abstract
Soundbank
getSoundbank​(
URL
url)
throws
InvalidMidiDataException
,

IOException

Obtains a soundbank object from the

URL

provided.

**Parameters:**
- url

-

URL

representing the soundbank

**Returns:**
- soundbank object

**Throws:**
- InvalidMidiDataException

- if the

URL

does not point to
valid MIDI soundbank data recognized by this soundbank reader
- IOException

- if an I/O error occurs
- NullPointerException

- if

url

is

null

---

#### public abstract
Soundbank
getSoundbank​(
InputStream
stream)
throws
InvalidMidiDataException
,

IOException

Obtains a soundbank object from the

InputStream

provided.

**Parameters:**
- stream

-

InputStream

representing the soundbank

**Returns:**
- soundbank object

**Throws:**
- InvalidMidiDataException

- if the stream does not point to valid
MIDI soundbank data recognized by this soundbank reader
- IOException

- if an I/O error occurs
- NullPointerException

- if

stream

is

null

---

#### public abstract
Soundbank
getSoundbank​(
File
file)
throws
InvalidMidiDataException
,

IOException

Obtains a soundbank object from the

File

provided.

**Parameters:**
- file

- the

File

representing the soundbank

**Returns:**
- soundbank object

**Throws:**
- InvalidMidiDataException

- if the file does not point to valid MIDI
soundbank data recognized by this soundbank reader
- IOException

- if an I/O error occurs
- NullPointerException

- if

file

is

null

---

### Additional Sections

#### Class SoundbankReader

java.lang.Object

- javax.sound.midi.spi.SoundbankReader

javax.sound.midi.spi.SoundbankReader

```java
public abstract class
SoundbankReader

extends
Object
```

A

SoundbankReader

supplies soundbank file-reading services. Concrete
subclasses of

SoundbankReader

parse a given soundbank file, producing
a

Soundbank

object that can be loaded into a

Synthesizer

.

**Since:** 1.3

public abstract class

SoundbankReader

extends

Object

A

SoundbankReader

supplies soundbank file-reading services. Concrete
subclasses of

SoundbankReader

parse a given soundbank file, producing
a

Soundbank

object that can be loaded into a

Synthesizer

.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

SoundbankReader

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

Soundbank

getSoundbank

​(

File

file)

Obtains a soundbank object from the

File

provided.

abstract

Soundbank

getSoundbank

​(

InputStream

stream)

Obtains a soundbank object from the

InputStream

provided.

abstract

Soundbank

getSoundbank

​(

URL

url)

Obtains a soundbank object from the

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

SoundbankReader

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

Soundbank

getSoundbank

​(

File

file)

Obtains a soundbank object from the

File

provided.

abstract

Soundbank

getSoundbank

​(

InputStream

stream)

Obtains a soundbank object from the

InputStream

provided.

abstract

Soundbank

getSoundbank

​(

URL

url)

Obtains a soundbank object from the

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

Obtains a soundbank object from the

File

provided.

Obtains a soundbank object from the

InputStream

provided.

Obtains a soundbank object from the

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

- SoundbankReader

```java
public SoundbankReader()
```

============ METHOD DETAIL ==========

- Method Detail

- getSoundbank

```java
public abstract
Soundbank
getSoundbank​(
URL
url)
throws
InvalidMidiDataException
,

IOException
```

Obtains a soundbank object from the

URL

provided.

**Parameters:** url

-

URL

representing the soundbank
**Returns:** soundbank object
**Throws:** InvalidMidiDataException

- if the

URL

does not point to
valid MIDI soundbank data recognized by this soundbank reader
**Throws:** IOException

- if an I/O error occurs
**Throws:** NullPointerException

- if

url

is

null

- getSoundbank

```java
public abstract
Soundbank
getSoundbank​(
InputStream
stream)
throws
InvalidMidiDataException
,

IOException
```

Obtains a soundbank object from the

InputStream

provided.

**Parameters:** stream

-

InputStream

representing the soundbank
**Returns:** soundbank object
**Throws:** InvalidMidiDataException

- if the stream does not point to valid
MIDI soundbank data recognized by this soundbank reader
**Throws:** IOException

- if an I/O error occurs
**Throws:** NullPointerException

- if

stream

is

null

- getSoundbank

```java
public abstract
Soundbank
getSoundbank​(
File
file)
throws
InvalidMidiDataException
,

IOException
```

Obtains a soundbank object from the

File

provided.

**Parameters:** file

- the

File

representing the soundbank
**Returns:** soundbank object
**Throws:** InvalidMidiDataException

- if the file does not point to valid MIDI
soundbank data recognized by this soundbank reader
**Throws:** IOException

- if an I/O error occurs
**Throws:** NullPointerException

- if

file

is

null

Constructor Detail

- SoundbankReader

```java
public SoundbankReader()
```

---

#### Constructor Detail

SoundbankReader

```java
public SoundbankReader()
```

---

#### SoundbankReader

public SoundbankReader()

Method Detail

- getSoundbank

```java
public abstract
Soundbank
getSoundbank​(
URL
url)
throws
InvalidMidiDataException
,

IOException
```

Obtains a soundbank object from the

URL

provided.

**Parameters:** url

-

URL

representing the soundbank
**Returns:** soundbank object
**Throws:** InvalidMidiDataException

- if the

URL

does not point to
valid MIDI soundbank data recognized by this soundbank reader
**Throws:** IOException

- if an I/O error occurs
**Throws:** NullPointerException

- if

url

is

null

- getSoundbank

```java
public abstract
Soundbank
getSoundbank​(
InputStream
stream)
throws
InvalidMidiDataException
,

IOException
```

Obtains a soundbank object from the

InputStream

provided.

**Parameters:** stream

-

InputStream

representing the soundbank
**Returns:** soundbank object
**Throws:** InvalidMidiDataException

- if the stream does not point to valid
MIDI soundbank data recognized by this soundbank reader
**Throws:** IOException

- if an I/O error occurs
**Throws:** NullPointerException

- if

stream

is

null

- getSoundbank

```java
public abstract
Soundbank
getSoundbank​(
File
file)
throws
InvalidMidiDataException
,

IOException
```

Obtains a soundbank object from the

File

provided.

**Parameters:** file

- the

File

representing the soundbank
**Returns:** soundbank object
**Throws:** InvalidMidiDataException

- if the file does not point to valid MIDI
soundbank data recognized by this soundbank reader
**Throws:** IOException

- if an I/O error occurs
**Throws:** NullPointerException

- if

file

is

null

---

#### Method Detail

getSoundbank

```java
public abstract
Soundbank
getSoundbank​(
URL
url)
throws
InvalidMidiDataException
,

IOException
```

Obtains a soundbank object from the

URL

provided.

**Parameters:** url

-

URL

representing the soundbank
**Returns:** soundbank object
**Throws:** InvalidMidiDataException

- if the

URL

does not point to
valid MIDI soundbank data recognized by this soundbank reader
**Throws:** IOException

- if an I/O error occurs
**Throws:** NullPointerException

- if

url

is

null

---

#### getSoundbank

public abstract

Soundbank

getSoundbank​(

URL

url)
throws

InvalidMidiDataException

,

IOException

Obtains a soundbank object from the

URL

provided.

getSoundbank

```java
public abstract
Soundbank
getSoundbank​(
InputStream
stream)
throws
InvalidMidiDataException
,

IOException
```

Obtains a soundbank object from the

InputStream

provided.

**Parameters:** stream

-

InputStream

representing the soundbank
**Returns:** soundbank object
**Throws:** InvalidMidiDataException

- if the stream does not point to valid
MIDI soundbank data recognized by this soundbank reader
**Throws:** IOException

- if an I/O error occurs
**Throws:** NullPointerException

- if

stream

is

null

---

#### getSoundbank

public abstract

Soundbank

getSoundbank​(

InputStream

stream)
throws

InvalidMidiDataException

,

IOException

Obtains a soundbank object from the

InputStream

provided.

getSoundbank

```java
public abstract
Soundbank
getSoundbank​(
File
file)
throws
InvalidMidiDataException
,

IOException
```

Obtains a soundbank object from the

File

provided.

**Parameters:** file

- the

File

representing the soundbank
**Returns:** soundbank object
**Throws:** InvalidMidiDataException

- if the file does not point to valid MIDI
soundbank data recognized by this soundbank reader
**Throws:** IOException

- if an I/O error occurs
**Throws:** NullPointerException

- if

file

is

null

---

#### getSoundbank

public abstract

Soundbank

getSoundbank​(

File

file)
throws

InvalidMidiDataException

,

IOException

Obtains a soundbank object from the

File

provided.

---

