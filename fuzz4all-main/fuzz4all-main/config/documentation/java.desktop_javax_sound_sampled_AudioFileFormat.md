# Class AudioFileFormat

**Source:** `java.desktop\javax\sound\sampled\AudioFileFormat.html`

### Class Description

```java
public class
AudioFileFormat

extends
Object
```

An instance of the

AudioFileFormat

class describes an audio file,
including the file type, the file's length in bytes, the length in sample
frames of the audio data contained in the file, and the format of the audio
data.

The

AudioSystem

class includes methods for determining the format of
an audio file, obtaining an audio input stream from an audio file, and
writing an audio file from an audio input stream.

An

AudioFileFormat

object can include a set of properties. A property
is a pair of key and value: the key is of type

String

, the associated
property value is an arbitrary object. Properties specify additional
informational meta data (like a author, copyright, or file duration).
Properties are optional information, and file reader and file writer
implementations are not required to provide or recognize properties.

The following table lists some common properties that should be used in
implementations:

Audio File Format Properties

Property key

Value type

Description

"duration"

Long

playback duration of the file in microseconds

"author"

String

name of the author of this file

"title"

String

title of this file

"copyright"

String

copyright message

"date"

Date

date of the recording or release

"comment"

String

an arbitrary text

**Since:** 1.3
**See Also:** AudioInputStream

---

### Field Details

*No entries found.*

### Constructor Details

#### protected AudioFileFormat​(
AudioFileFormat.Type
type,
int byteLength,

AudioFormat
format,
int frameLength)

Constructs an audio file format object. This protected constructor is
intended for use by providers of file-reading services when returning
information about an audio file or about supported audio file formats.

**Parameters:**
- type

- the type of the audio file
- byteLength

- the length of the file in bytes, or

AudioSystem.NOT_SPECIFIED
- format

- the format of the audio data contained in the file
- frameLength

- the audio data length in sample frames, or

AudioSystem.NOT_SPECIFIED

**See Also:**
- getType()

---

#### public AudioFileFormat​(
AudioFileFormat.Type
type,

AudioFormat
format,
int frameLength)

Constructs an audio file format object. This public constructor may be
used by applications to describe the properties of a requested audio
file.

**Parameters:**
- type

- the type of the audio file
- format

- the format of the audio data contained in the file
- frameLength

- the audio data length in sample frames, or

AudioSystem.NOT_SPECIFIED

---

#### public AudioFileFormat​(
AudioFileFormat.Type
type,

AudioFormat
format,
int frameLength,

Map
<
String
,​
Object
> properties)

Construct an audio file format object with a set of defined properties.
This public constructor may be used by applications to describe the
properties of a requested audio file. The properties map will be copied
to prevent any changes to it.

**Parameters:**
- type

- the type of the audio file
- format

- the format of the audio data contained in the file
- frameLength

- the audio data length in sample frames, or

AudioSystem.NOT_SPECIFIED
- properties

- a

Map<String, Object>

object with properties

**Since:**
- 1.5

---

### Method Details

#### public
AudioFileFormat.Type
getType()

Obtains the audio file type, such as

WAVE

or

AU

.

**Returns:**
- the audio file type

**See Also:**
- AudioFileFormat.Type.WAVE

,

AudioFileFormat.Type.AU

,

AudioFileFormat.Type.AIFF

,

AudioFileFormat.Type.AIFC

,

AudioFileFormat.Type.SND

---

#### public int getByteLength()

Obtains the size in bytes of the entire audio file (not just its audio
data).

**Returns:**
- the audio file length in bytes

**See Also:**
- AudioSystem.NOT_SPECIFIED

---

#### public
AudioFormat
getFormat()

Obtains the format of the audio data contained in the audio file.

**Returns:**
- the audio data format

---

#### public int getFrameLength()

Obtains the length of the audio data contained in the file, expressed in
sample frames.

**Returns:**
- the number of sample frames of audio data in the file

**See Also:**
- AudioSystem.NOT_SPECIFIED

---

#### public
Map
<
String
,​
Object
> properties()

Obtain an unmodifiable map of properties. The concept of properties is
further explained in the

class description

.

**Returns:**
- a

Map<String, Object>

object containing all properties.
If no properties are recognized, an empty map is returned.

**See Also:**
- getProperty(String)

**Since:**
- 1.5

---

#### public
Object
getProperty​(
String
key)

Obtain the property value specified by the key. The concept of properties
is further explained in the

class description

.

If the specified property is not defined for a particular file format,
this method returns

null

.

**Parameters:**
- key

- the key of the desired property

**Returns:**
- the value of the property with the specified key, or

null

if the property does not exist

**See Also:**
- properties()

**Since:**
- 1.5

---

#### public
String
toString()

Provides a string representation of the file format.

**Overrides:**
- toString

in class

Object

**Returns:**
- the file format as a string

---

### Additional Sections

#### Class AudioFileFormat

java.lang.Object

- javax.sound.sampled.AudioFileFormat

javax.sound.sampled.AudioFileFormat

```java
public class
AudioFileFormat

extends
Object
```

An instance of the

AudioFileFormat

class describes an audio file,
including the file type, the file's length in bytes, the length in sample
frames of the audio data contained in the file, and the format of the audio
data.

The

AudioSystem

class includes methods for determining the format of
an audio file, obtaining an audio input stream from an audio file, and
writing an audio file from an audio input stream.

An

AudioFileFormat

object can include a set of properties. A property
is a pair of key and value: the key is of type

String

, the associated
property value is an arbitrary object. Properties specify additional
informational meta data (like a author, copyright, or file duration).
Properties are optional information, and file reader and file writer
implementations are not required to provide or recognize properties.

The following table lists some common properties that should be used in
implementations:

Audio File Format Properties

Property key

Value type

Description

"duration"

Long

playback duration of the file in microseconds

"author"

String

name of the author of this file

"title"

String

title of this file

"copyright"

String

copyright message

"date"

Date

date of the recording or release

"comment"

String

an arbitrary text

**Since:** 1.3
**See Also:** AudioInputStream

public class

AudioFileFormat

extends

Object

An instance of the

AudioFileFormat

class describes an audio file,
including the file type, the file's length in bytes, the length in sample
frames of the audio data contained in the file, and the format of the audio
data.

The

AudioSystem

class includes methods for determining the format of
an audio file, obtaining an audio input stream from an audio file, and
writing an audio file from an audio input stream.

An

AudioFileFormat

object can include a set of properties. A property
is a pair of key and value: the key is of type

String

, the associated
property value is an arbitrary object. Properties specify additional
informational meta data (like a author, copyright, or file duration).
Properties are optional information, and file reader and file writer
implementations are not required to provide or recognize properties.

The following table lists some common properties that should be used in
implementations:

Audio File Format Properties

Property key

Value type

Description

"duration"

Long

playback duration of the file in microseconds

"author"

String

name of the author of this file

"title"

String

title of this file

"copyright"

String

copyright message

"date"

Date

date of the recording or release

"comment"

String

an arbitrary text

The

AudioSystem

class includes methods for determining the format of
an audio file, obtaining an audio input stream from an audio file, and
writing an audio file from an audio input stream.

An

AudioFileFormat

object can include a set of properties. A property
is a pair of key and value: the key is of type

String

, the associated
property value is an arbitrary object. Properties specify additional
informational meta data (like a author, copyright, or file duration).
Properties are optional information, and file reader and file writer
implementations are not required to provide or recognize properties.

The following table lists some common properties that should be used in
implementations:

Audio File Format Properties

Property key

Value type

Description

"duration"

Long

playback duration of the file in microseconds

"author"

String

name of the author of this file

"title"

String

title of this file

"copyright"

String

copyright message

"date"

Date

date of the recording or release

"comment"

String

an arbitrary text

An

AudioFileFormat

object can include a set of properties. A property
is a pair of key and value: the key is of type

String

, the associated
property value is an arbitrary object. Properties specify additional
informational meta data (like a author, copyright, or file duration).
Properties are optional information, and file reader and file writer
implementations are not required to provide or recognize properties.

The following table lists some common properties that should be used in
implementations:

Audio File Format Properties

Property key

Value type

Description

"duration"

Long

playback duration of the file in microseconds

"author"

String

name of the author of this file

"title"

String

title of this file

"copyright"

String

copyright message

"date"

Date

date of the recording or release

"comment"

String

an arbitrary text

The following table lists some common properties that should be used in
implementations:

Audio File Format Properties

Property key

Value type

Description

"duration"

Long

playback duration of the file in microseconds

"author"

String

name of the author of this file

"title"

String

title of this file

"copyright"

String

copyright message

"date"

Date

date of the recording or release

"comment"

String

an arbitrary text

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

static class

AudioFileFormat.Type

An instance of the

Type

class represents one of the standard
types of audio file.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

AudioFileFormat

​(

AudioFileFormat.Type

type,
int byteLength,

AudioFormat

format,
int frameLength)

Constructs an audio file format object.

AudioFileFormat

​(

AudioFileFormat.Type

type,

AudioFormat

format,
int frameLength)

Constructs an audio file format object.

AudioFileFormat

​(

AudioFileFormat.Type

type,

AudioFormat

format,
int frameLength,

Map

<

String

,​

Object

> properties)

Construct an audio file format object with a set of defined properties.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

int

getByteLength

()

Obtains the size in bytes of the entire audio file (not just its audio
data).

AudioFormat

getFormat

()

Obtains the format of the audio data contained in the audio file.

int

getFrameLength

()

Obtains the length of the audio data contained in the file, expressed in
sample frames.

Object

getProperty

​(

String

key)

Obtain the property value specified by the key.

AudioFileFormat.Type

getType

()

Obtains the audio file type, such as

WAVE

or

AU

.

Map

<

String

,​

Object

>

properties

()

Obtain an unmodifiable map of properties.

String

toString

()

Provides a string representation of the file format.

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

Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

static class

AudioFileFormat.Type

An instance of the

Type

class represents one of the standard
types of audio file.

---

#### Nested Class Summary

An instance of the

Type

class represents one of the standard
types of audio file.

Constructor Summary

Constructors

Modifier

Constructor

Description

protected

AudioFileFormat

​(

AudioFileFormat.Type

type,
int byteLength,

AudioFormat

format,
int frameLength)

Constructs an audio file format object.

AudioFileFormat

​(

AudioFileFormat.Type

type,

AudioFormat

format,
int frameLength)

Constructs an audio file format object.

AudioFileFormat

​(

AudioFileFormat.Type

type,

AudioFormat

format,
int frameLength,

Map

<

String

,​

Object

> properties)

Construct an audio file format object with a set of defined properties.

---

#### Constructor Summary

Constructs an audio file format object.

Construct an audio file format object with a set of defined properties.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

int

getByteLength

()

Obtains the size in bytes of the entire audio file (not just its audio
data).

AudioFormat

getFormat

()

Obtains the format of the audio data contained in the audio file.

int

getFrameLength

()

Obtains the length of the audio data contained in the file, expressed in
sample frames.

Object

getProperty

​(

String

key)

Obtain the property value specified by the key.

AudioFileFormat.Type

getType

()

Obtains the audio file type, such as

WAVE

or

AU

.

Map

<

String

,​

Object

>

properties

()

Obtain an unmodifiable map of properties.

String

toString

()

Provides a string representation of the file format.

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

Obtains the size in bytes of the entire audio file (not just its audio
data).

Obtains the format of the audio data contained in the audio file.

Obtains the length of the audio data contained in the file, expressed in
sample frames.

Obtain the property value specified by the key.

Obtains the audio file type, such as

WAVE

or

AU

.

Obtain an unmodifiable map of properties.

Provides a string representation of the file format.

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

- AudioFileFormat

```java
protected AudioFileFormat​(
AudioFileFormat.Type
type,
int byteLength,

AudioFormat
format,
int frameLength)
```

Constructs an audio file format object. This protected constructor is
intended for use by providers of file-reading services when returning
information about an audio file or about supported audio file formats.

**Parameters:** type

- the type of the audio file
**Parameters:** byteLength

- the length of the file in bytes, or

AudioSystem.NOT_SPECIFIED
**Parameters:** format

- the format of the audio data contained in the file
**Parameters:** frameLength

- the audio data length in sample frames, or

AudioSystem.NOT_SPECIFIED
**See Also:** getType()

- AudioFileFormat

```java
public AudioFileFormat​(
AudioFileFormat.Type
type,

AudioFormat
format,
int frameLength)
```

Constructs an audio file format object. This public constructor may be
used by applications to describe the properties of a requested audio
file.

**Parameters:** type

- the type of the audio file
**Parameters:** format

- the format of the audio data contained in the file
**Parameters:** frameLength

- the audio data length in sample frames, or

AudioSystem.NOT_SPECIFIED

- AudioFileFormat

```java
public AudioFileFormat​(
AudioFileFormat.Type
type,

AudioFormat
format,
int frameLength,

Map
<
String
,​
Object
> properties)
```

Construct an audio file format object with a set of defined properties.
This public constructor may be used by applications to describe the
properties of a requested audio file. The properties map will be copied
to prevent any changes to it.

**Parameters:** type

- the type of the audio file
**Parameters:** format

- the format of the audio data contained in the file
**Parameters:** frameLength

- the audio data length in sample frames, or

AudioSystem.NOT_SPECIFIED
**Parameters:** properties

- a

Map<String, Object>

object with properties
**Since:** 1.5

============ METHOD DETAIL ==========

- Method Detail

- getType

```java
public
AudioFileFormat.Type
getType()
```

Obtains the audio file type, such as

WAVE

or

AU

.

**Returns:** the audio file type
**See Also:** AudioFileFormat.Type.WAVE

,

AudioFileFormat.Type.AU

,

AudioFileFormat.Type.AIFF

,

AudioFileFormat.Type.AIFC

,

AudioFileFormat.Type.SND

- getByteLength

```java
public int getByteLength()
```

Obtains the size in bytes of the entire audio file (not just its audio
data).

**Returns:** the audio file length in bytes
**See Also:** AudioSystem.NOT_SPECIFIED

- getFormat

```java
public
AudioFormat
getFormat()
```

Obtains the format of the audio data contained in the audio file.

**Returns:** the audio data format

- getFrameLength

```java
public int getFrameLength()
```

Obtains the length of the audio data contained in the file, expressed in
sample frames.

**Returns:** the number of sample frames of audio data in the file
**See Also:** AudioSystem.NOT_SPECIFIED

- properties

```java
public
Map
<
String
,​
Object
> properties()
```

Obtain an unmodifiable map of properties. The concept of properties is
further explained in the

class description

.

**Returns:** a

Map<String, Object>

object containing all properties.
If no properties are recognized, an empty map is returned.
**Since:** 1.5
**See Also:** getProperty(String)

- getProperty

```java
public
Object
getProperty​(
String
key)
```

Obtain the property value specified by the key. The concept of properties
is further explained in the

class description

.

If the specified property is not defined for a particular file format,
this method returns

null

.

**Parameters:** key

- the key of the desired property
**Returns:** the value of the property with the specified key, or

null

if the property does not exist
**Since:** 1.5
**See Also:** properties()

- toString

```java
public
String
toString()
```

Provides a string representation of the file format.

**Overrides:** toString

in class

Object
**Returns:** the file format as a string

Constructor Detail

- AudioFileFormat

```java
protected AudioFileFormat​(
AudioFileFormat.Type
type,
int byteLength,

AudioFormat
format,
int frameLength)
```

Constructs an audio file format object. This protected constructor is
intended for use by providers of file-reading services when returning
information about an audio file or about supported audio file formats.

**Parameters:** type

- the type of the audio file
**Parameters:** byteLength

- the length of the file in bytes, or

AudioSystem.NOT_SPECIFIED
**Parameters:** format

- the format of the audio data contained in the file
**Parameters:** frameLength

- the audio data length in sample frames, or

AudioSystem.NOT_SPECIFIED
**See Also:** getType()

- AudioFileFormat

```java
public AudioFileFormat​(
AudioFileFormat.Type
type,

AudioFormat
format,
int frameLength)
```

Constructs an audio file format object. This public constructor may be
used by applications to describe the properties of a requested audio
file.

**Parameters:** type

- the type of the audio file
**Parameters:** format

- the format of the audio data contained in the file
**Parameters:** frameLength

- the audio data length in sample frames, or

AudioSystem.NOT_SPECIFIED

- AudioFileFormat

```java
public AudioFileFormat​(
AudioFileFormat.Type
type,

AudioFormat
format,
int frameLength,

Map
<
String
,​
Object
> properties)
```

Construct an audio file format object with a set of defined properties.
This public constructor may be used by applications to describe the
properties of a requested audio file. The properties map will be copied
to prevent any changes to it.

**Parameters:** type

- the type of the audio file
**Parameters:** format

- the format of the audio data contained in the file
**Parameters:** frameLength

- the audio data length in sample frames, or

AudioSystem.NOT_SPECIFIED
**Parameters:** properties

- a

Map<String, Object>

object with properties
**Since:** 1.5

---

#### Constructor Detail

AudioFileFormat

```java
protected AudioFileFormat​(
AudioFileFormat.Type
type,
int byteLength,

AudioFormat
format,
int frameLength)
```

Constructs an audio file format object. This protected constructor is
intended for use by providers of file-reading services when returning
information about an audio file or about supported audio file formats.

**Parameters:** type

- the type of the audio file
**Parameters:** byteLength

- the length of the file in bytes, or

AudioSystem.NOT_SPECIFIED
**Parameters:** format

- the format of the audio data contained in the file
**Parameters:** frameLength

- the audio data length in sample frames, or

AudioSystem.NOT_SPECIFIED
**See Also:** getType()

---

#### AudioFileFormat

protected AudioFileFormat​(

AudioFileFormat.Type

type,
int byteLength,

AudioFormat

format,
int frameLength)

Constructs an audio file format object. This protected constructor is
intended for use by providers of file-reading services when returning
information about an audio file or about supported audio file formats.

AudioFileFormat

```java
public AudioFileFormat​(
AudioFileFormat.Type
type,

AudioFormat
format,
int frameLength)
```

Constructs an audio file format object. This public constructor may be
used by applications to describe the properties of a requested audio
file.

**Parameters:** type

- the type of the audio file
**Parameters:** format

- the format of the audio data contained in the file
**Parameters:** frameLength

- the audio data length in sample frames, or

AudioSystem.NOT_SPECIFIED

---

#### AudioFileFormat

public AudioFileFormat​(

AudioFileFormat.Type

type,

AudioFormat

format,
int frameLength)

Constructs an audio file format object. This public constructor may be
used by applications to describe the properties of a requested audio
file.

AudioFileFormat

```java
public AudioFileFormat​(
AudioFileFormat.Type
type,

AudioFormat
format,
int frameLength,

Map
<
String
,​
Object
> properties)
```

Construct an audio file format object with a set of defined properties.
This public constructor may be used by applications to describe the
properties of a requested audio file. The properties map will be copied
to prevent any changes to it.

**Parameters:** type

- the type of the audio file
**Parameters:** format

- the format of the audio data contained in the file
**Parameters:** frameLength

- the audio data length in sample frames, or

AudioSystem.NOT_SPECIFIED
**Parameters:** properties

- a

Map<String, Object>

object with properties
**Since:** 1.5

---

#### AudioFileFormat

public AudioFileFormat​(

AudioFileFormat.Type

type,

AudioFormat

format,
int frameLength,

Map

<

String

,​

Object

> properties)

Construct an audio file format object with a set of defined properties.
This public constructor may be used by applications to describe the
properties of a requested audio file. The properties map will be copied
to prevent any changes to it.

Method Detail

- getType

```java
public
AudioFileFormat.Type
getType()
```

Obtains the audio file type, such as

WAVE

or

AU

.

**Returns:** the audio file type
**See Also:** AudioFileFormat.Type.WAVE

,

AudioFileFormat.Type.AU

,

AudioFileFormat.Type.AIFF

,

AudioFileFormat.Type.AIFC

,

AudioFileFormat.Type.SND

- getByteLength

```java
public int getByteLength()
```

Obtains the size in bytes of the entire audio file (not just its audio
data).

**Returns:** the audio file length in bytes
**See Also:** AudioSystem.NOT_SPECIFIED

- getFormat

```java
public
AudioFormat
getFormat()
```

Obtains the format of the audio data contained in the audio file.

**Returns:** the audio data format

- getFrameLength

```java
public int getFrameLength()
```

Obtains the length of the audio data contained in the file, expressed in
sample frames.

**Returns:** the number of sample frames of audio data in the file
**See Also:** AudioSystem.NOT_SPECIFIED

- properties

```java
public
Map
<
String
,​
Object
> properties()
```

Obtain an unmodifiable map of properties. The concept of properties is
further explained in the

class description

.

**Returns:** a

Map<String, Object>

object containing all properties.
If no properties are recognized, an empty map is returned.
**Since:** 1.5
**See Also:** getProperty(String)

- getProperty

```java
public
Object
getProperty​(
String
key)
```

Obtain the property value specified by the key. The concept of properties
is further explained in the

class description

.

If the specified property is not defined for a particular file format,
this method returns

null

.

**Parameters:** key

- the key of the desired property
**Returns:** the value of the property with the specified key, or

null

if the property does not exist
**Since:** 1.5
**See Also:** properties()

- toString

```java
public
String
toString()
```

Provides a string representation of the file format.

**Overrides:** toString

in class

Object
**Returns:** the file format as a string

---

#### Method Detail

getType

```java
public
AudioFileFormat.Type
getType()
```

Obtains the audio file type, such as

WAVE

or

AU

.

**Returns:** the audio file type
**See Also:** AudioFileFormat.Type.WAVE

,

AudioFileFormat.Type.AU

,

AudioFileFormat.Type.AIFF

,

AudioFileFormat.Type.AIFC

,

AudioFileFormat.Type.SND

---

#### getType

public

AudioFileFormat.Type

getType()

Obtains the audio file type, such as

WAVE

or

AU

.

getByteLength

```java
public int getByteLength()
```

Obtains the size in bytes of the entire audio file (not just its audio
data).

**Returns:** the audio file length in bytes
**See Also:** AudioSystem.NOT_SPECIFIED

---

#### getByteLength

public int getByteLength()

Obtains the size in bytes of the entire audio file (not just its audio
data).

getFormat

```java
public
AudioFormat
getFormat()
```

Obtains the format of the audio data contained in the audio file.

**Returns:** the audio data format

---

#### getFormat

public

AudioFormat

getFormat()

Obtains the format of the audio data contained in the audio file.

getFrameLength

```java
public int getFrameLength()
```

Obtains the length of the audio data contained in the file, expressed in
sample frames.

**Returns:** the number of sample frames of audio data in the file
**See Also:** AudioSystem.NOT_SPECIFIED

---

#### getFrameLength

public int getFrameLength()

Obtains the length of the audio data contained in the file, expressed in
sample frames.

properties

```java
public
Map
<
String
,​
Object
> properties()
```

Obtain an unmodifiable map of properties. The concept of properties is
further explained in the

class description

.

**Returns:** a

Map<String, Object>

object containing all properties.
If no properties are recognized, an empty map is returned.
**Since:** 1.5
**See Also:** getProperty(String)

---

#### properties

public

Map

<

String

,​

Object

> properties()

Obtain an unmodifiable map of properties. The concept of properties is
further explained in the

class description

.

getProperty

```java
public
Object
getProperty​(
String
key)
```

Obtain the property value specified by the key. The concept of properties
is further explained in the

class description

.

If the specified property is not defined for a particular file format,
this method returns

null

.

**Parameters:** key

- the key of the desired property
**Returns:** the value of the property with the specified key, or

null

if the property does not exist
**Since:** 1.5
**See Also:** properties()

---

#### getProperty

public

Object

getProperty​(

String

key)

Obtain the property value specified by the key. The concept of properties
is further explained in the

class description

.

If the specified property is not defined for a particular file format,
this method returns

null

.

If the specified property is not defined for a particular file format,
this method returns

null

.

toString

```java
public
String
toString()
```

Provides a string representation of the file format.

**Overrides:** toString

in class

Object
**Returns:** the file format as a string

---

#### toString

public

String

toString()

Provides a string representation of the file format.

---

