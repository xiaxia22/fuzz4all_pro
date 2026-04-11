# Class DataLine.Info

**Source:** `java.desktop\javax\sound\sampled\DataLine.Info.html`

### Class Description

```java
public static class
DataLine.Info

extends
Line.Info
```

Besides the class information inherited from its superclass,

DataLine.Info

provides additional information specific to data
lines. This information includes:

- the audio formats supported by the data line

the minimum and maximum sizes of its internal buffer

Because a

Line.Info

knows the class of the line its describes, a

DataLine.Info

object can describe

DataLine

subinterfaces
such as

SourceDataLine

,

TargetDataLine

, and

Clip

.
You can query a mixer for lines of any of these types, passing an
appropriate instance of

DataLine.Info

as the argument to a method
such as

Mixer.getLine(Line.Info)

.

**Enclosing interface:** DataLine

---

### Field Details

*No entries found.*

### Constructor Details

#### public Info​(
Class
<?> lineClass,

AudioFormat
[] formats,
int minBufferSize,
int maxBufferSize)

Constructs a data line's info object from the specified information,
which includes a set of supported audio formats and a range for the
buffer size. This constructor is typically used by mixer
implementations when returning information about a supported line.

**Parameters:**
- lineClass

- the class of the data line described by the info
object
- formats

- set of formats supported
- minBufferSize

- minimum buffer size supported by the data line,
in bytes
- maxBufferSize

- maximum buffer size supported by the data line,
in bytes

---

#### public Info​(
Class
<?> lineClass,

AudioFormat
format,
int bufferSize)

Constructs a data line's info object from the specified information,
which includes a single audio format and a desired buffer size. This
constructor is typically used by an application to describe a desired
line.

**Parameters:**
- lineClass

- the class of the data line described by the info
object
- format

- desired format
- bufferSize

- desired buffer size, in bytes

---

#### public Info​(
Class
<?> lineClass,

AudioFormat
format)

Constructs a data line's info object from the specified information,
which includes a single audio format. This constructor is typically
used by an application to describe a desired line.

**Parameters:**
- lineClass

- the class of the data line described by the info
object
- format

- desired format

---

### Method Details

#### public
AudioFormat
[] getFormats()

Obtains a set of audio formats supported by the data line. Note that

isFormatSupported(AudioFormat)

might return

true

for
certain additional formats that are missing from the set returned by

getFormats()

. The reverse is not the case:

isFormatSupported(AudioFormat)

is guaranteed to return

true

for all formats returned by

getFormats()

.

Some fields in the

AudioFormat

instances can be set to

NOT_SPECIFIED

if that field does
not apply to the format, or if the format supports a wide range of
values for that field. For example, a multi-channel device supporting
up to 64 channels, could set the channel field in the

AudioFormat

instances returned by this method to

NOT_SPECIFIED

.

**Returns:**
- a set of supported audio formats

**See Also:**
- isFormatSupported(AudioFormat)

---

#### public boolean isFormatSupported​(
AudioFormat
format)

Indicates whether this data line supports a particular audio format.
The default implementation of this method simply returns

true

if the specified format matches any of the supported formats.

**Parameters:**
- format

- the audio format for which support is queried

**Returns:**
- true

if the format is supported, otherwise

false

**See Also:**
- getFormats()

,

AudioFormat.matches(javax.sound.sampled.AudioFormat)

---

#### public int getMinBufferSize()

Obtains the minimum buffer size supported by the data line.

**Returns:**
- minimum buffer size in bytes, or

AudioSystem.NOT_SPECIFIED

---

#### public int getMaxBufferSize()

Obtains the maximum buffer size supported by the data line.

**Returns:**
- maximum buffer size in bytes, or

AudioSystem.NOT_SPECIFIED

---

#### public boolean matches​(
Line.Info
info)

Determines whether the specified info object matches this one. To
match, the superclass match requirements must be met. In addition,
this object's minimum buffer size must be at least as large as that
of the object specified, its maximum buffer size must be at most as
large as that of the object specified, and all of its formats must
match formats supported by the object specified.

**Overrides:**
- matches

in class

Line.Info

**Parameters:**
- info

- the info object which is being compared to this one

**Returns:**
- true

if this object matches the one specified,
otherwise

false

---

#### public
String
toString()

Obtains a textual description of the data line info.

**Overrides:**
- toString

in class

Line.Info

**Returns:**
- a string description

---

### Additional Sections

#### Class DataLine.Info

java.lang.Object

- javax.sound.sampled.Line.Info
- - javax.sound.sampled.DataLine.Info

javax.sound.sampled.Line.Info

- javax.sound.sampled.DataLine.Info

javax.sound.sampled.DataLine.Info

**Enclosing interface:** DataLine

```java
public static class
DataLine.Info

extends
Line.Info
```

Besides the class information inherited from its superclass,

DataLine.Info

provides additional information specific to data
lines. This information includes:

- the audio formats supported by the data line

the minimum and maximum sizes of its internal buffer

Because a

Line.Info

knows the class of the line its describes, a

DataLine.Info

object can describe

DataLine

subinterfaces
such as

SourceDataLine

,

TargetDataLine

, and

Clip

.
You can query a mixer for lines of any of these types, passing an
appropriate instance of

DataLine.Info

as the argument to a method
such as

Mixer.getLine(Line.Info)

.

**Since:** 1.3
**See Also:** Line.Info

public static class

DataLine.Info

extends

Line.Info

Besides the class information inherited from its superclass,

DataLine.Info

provides additional information specific to data
lines. This information includes:

- the audio formats supported by the data line

the minimum and maximum sizes of its internal buffer

Because a

Line.Info

knows the class of the line its describes, a

DataLine.Info

object can describe

DataLine

subinterfaces
such as

SourceDataLine

,

TargetDataLine

, and

Clip

.
You can query a mixer for lines of any of these types, passing an
appropriate instance of

DataLine.Info

as the argument to a method
such as

Mixer.getLine(Line.Info)

.

the audio formats supported by the data line

the minimum and maximum sizes of its internal buffer

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

Info

​(

Class

<?> lineClass,

AudioFormat

format)

Constructs a data line's info object from the specified information,
which includes a single audio format.

Info

​(

Class

<?> lineClass,

AudioFormat

[] formats,
int minBufferSize,
int maxBufferSize)

Constructs a data line's info object from the specified information,
which includes a set of supported audio formats and a range for the
buffer size.

Info

​(

Class

<?> lineClass,

AudioFormat

format,
int bufferSize)

Constructs a data line's info object from the specified information,
which includes a single audio format and a desired buffer size.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

AudioFormat

[]

getFormats

()

Obtains a set of audio formats supported by the data line.

int

getMaxBufferSize

()

Obtains the maximum buffer size supported by the data line.

int

getMinBufferSize

()

Obtains the minimum buffer size supported by the data line.

boolean

isFormatSupported

​(

AudioFormat

format)

Indicates whether this data line supports a particular audio format.

boolean

matches

​(

Line.Info

info)

Determines whether the specified info object matches this one.

String

toString

()

Obtains a textual description of the data line info.

- Methods declared in class javax.sound.sampled.

Line.Info

getLineClass

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

Info

​(

Class

<?> lineClass,

AudioFormat

format)

Constructs a data line's info object from the specified information,
which includes a single audio format.

Info

​(

Class

<?> lineClass,

AudioFormat

[] formats,
int minBufferSize,
int maxBufferSize)

Constructs a data line's info object from the specified information,
which includes a set of supported audio formats and a range for the
buffer size.

Info

​(

Class

<?> lineClass,

AudioFormat

format,
int bufferSize)

Constructs a data line's info object from the specified information,
which includes a single audio format and a desired buffer size.

---

#### Constructor Summary

Constructs a data line's info object from the specified information,
which includes a single audio format.

Constructs a data line's info object from the specified information,
which includes a set of supported audio formats and a range for the
buffer size.

Constructs a data line's info object from the specified information,
which includes a single audio format and a desired buffer size.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

AudioFormat

[]

getFormats

()

Obtains a set of audio formats supported by the data line.

int

getMaxBufferSize

()

Obtains the maximum buffer size supported by the data line.

int

getMinBufferSize

()

Obtains the minimum buffer size supported by the data line.

boolean

isFormatSupported

​(

AudioFormat

format)

Indicates whether this data line supports a particular audio format.

boolean

matches

​(

Line.Info

info)

Determines whether the specified info object matches this one.

String

toString

()

Obtains a textual description of the data line info.

- Methods declared in class javax.sound.sampled.

Line.Info

getLineClass

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

Obtains a set of audio formats supported by the data line.

Obtains the maximum buffer size supported by the data line.

Obtains the minimum buffer size supported by the data line.

Indicates whether this data line supports a particular audio format.

Determines whether the specified info object matches this one.

Obtains a textual description of the data line info.

Methods declared in class javax.sound.sampled.

Line.Info

getLineClass

---

#### Methods declared in class javax.sound.sampled. Line.Info

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

- Info

```java
public Info​(
Class
<?> lineClass,

AudioFormat
[] formats,
int minBufferSize,
int maxBufferSize)
```

Constructs a data line's info object from the specified information,
which includes a set of supported audio formats and a range for the
buffer size. This constructor is typically used by mixer
implementations when returning information about a supported line.

**Parameters:** lineClass

- the class of the data line described by the info
object
**Parameters:** formats

- set of formats supported
**Parameters:** minBufferSize

- minimum buffer size supported by the data line,
in bytes
**Parameters:** maxBufferSize

- maximum buffer size supported by the data line,
in bytes

- Info

```java
public Info​(
Class
<?> lineClass,

AudioFormat
format,
int bufferSize)
```

Constructs a data line's info object from the specified information,
which includes a single audio format and a desired buffer size. This
constructor is typically used by an application to describe a desired
line.

**Parameters:** lineClass

- the class of the data line described by the info
object
**Parameters:** format

- desired format
**Parameters:** bufferSize

- desired buffer size, in bytes

- Info

```java
public Info​(
Class
<?> lineClass,

AudioFormat
format)
```

Constructs a data line's info object from the specified information,
which includes a single audio format. This constructor is typically
used by an application to describe a desired line.

**Parameters:** lineClass

- the class of the data line described by the info
object
**Parameters:** format

- desired format

============ METHOD DETAIL ==========

- Method Detail

- getFormats

```java
public
AudioFormat
[] getFormats()
```

Obtains a set of audio formats supported by the data line. Note that

isFormatSupported(AudioFormat)

might return

true

for
certain additional formats that are missing from the set returned by

getFormats()

. The reverse is not the case:

isFormatSupported(AudioFormat)

is guaranteed to return

true

for all formats returned by

getFormats()

.

Some fields in the

AudioFormat

instances can be set to

NOT_SPECIFIED

if that field does
not apply to the format, or if the format supports a wide range of
values for that field. For example, a multi-channel device supporting
up to 64 channels, could set the channel field in the

AudioFormat

instances returned by this method to

NOT_SPECIFIED

.

**Returns:** a set of supported audio formats
**See Also:** isFormatSupported(AudioFormat)

- isFormatSupported

```java
public boolean isFormatSupported​(
AudioFormat
format)
```

Indicates whether this data line supports a particular audio format.
The default implementation of this method simply returns

true

if the specified format matches any of the supported formats.

**Parameters:** format

- the audio format for which support is queried
**Returns:** true

if the format is supported, otherwise

false
**See Also:** getFormats()

,

AudioFormat.matches(javax.sound.sampled.AudioFormat)

- getMinBufferSize

```java
public int getMinBufferSize()
```

Obtains the minimum buffer size supported by the data line.

**Returns:** minimum buffer size in bytes, or

AudioSystem.NOT_SPECIFIED

- getMaxBufferSize

```java
public int getMaxBufferSize()
```

Obtains the maximum buffer size supported by the data line.

**Returns:** maximum buffer size in bytes, or

AudioSystem.NOT_SPECIFIED

- matches

```java
public boolean matches​(
Line.Info
info)
```

Determines whether the specified info object matches this one. To
match, the superclass match requirements must be met. In addition,
this object's minimum buffer size must be at least as large as that
of the object specified, its maximum buffer size must be at most as
large as that of the object specified, and all of its formats must
match formats supported by the object specified.

**Overrides:** matches

in class

Line.Info
**Parameters:** info

- the info object which is being compared to this one
**Returns:** true

if this object matches the one specified,
otherwise

false

- toString

```java
public
String
toString()
```

Obtains a textual description of the data line info.

**Overrides:** toString

in class

Line.Info
**Returns:** a string description

Constructor Detail

- Info

```java
public Info​(
Class
<?> lineClass,

AudioFormat
[] formats,
int minBufferSize,
int maxBufferSize)
```

Constructs a data line's info object from the specified information,
which includes a set of supported audio formats and a range for the
buffer size. This constructor is typically used by mixer
implementations when returning information about a supported line.

**Parameters:** lineClass

- the class of the data line described by the info
object
**Parameters:** formats

- set of formats supported
**Parameters:** minBufferSize

- minimum buffer size supported by the data line,
in bytes
**Parameters:** maxBufferSize

- maximum buffer size supported by the data line,
in bytes

- Info

```java
public Info​(
Class
<?> lineClass,

AudioFormat
format,
int bufferSize)
```

Constructs a data line's info object from the specified information,
which includes a single audio format and a desired buffer size. This
constructor is typically used by an application to describe a desired
line.

**Parameters:** lineClass

- the class of the data line described by the info
object
**Parameters:** format

- desired format
**Parameters:** bufferSize

- desired buffer size, in bytes

- Info

```java
public Info​(
Class
<?> lineClass,

AudioFormat
format)
```

Constructs a data line's info object from the specified information,
which includes a single audio format. This constructor is typically
used by an application to describe a desired line.

**Parameters:** lineClass

- the class of the data line described by the info
object
**Parameters:** format

- desired format

---

#### Constructor Detail

Info

```java
public Info​(
Class
<?> lineClass,

AudioFormat
[] formats,
int minBufferSize,
int maxBufferSize)
```

Constructs a data line's info object from the specified information,
which includes a set of supported audio formats and a range for the
buffer size. This constructor is typically used by mixer
implementations when returning information about a supported line.

**Parameters:** lineClass

- the class of the data line described by the info
object
**Parameters:** formats

- set of formats supported
**Parameters:** minBufferSize

- minimum buffer size supported by the data line,
in bytes
**Parameters:** maxBufferSize

- maximum buffer size supported by the data line,
in bytes

---

#### Info

public Info​(

Class

<?> lineClass,

AudioFormat

[] formats,
int minBufferSize,
int maxBufferSize)

Constructs a data line's info object from the specified information,
which includes a set of supported audio formats and a range for the
buffer size. This constructor is typically used by mixer
implementations when returning information about a supported line.

Info

```java
public Info​(
Class
<?> lineClass,

AudioFormat
format,
int bufferSize)
```

Constructs a data line's info object from the specified information,
which includes a single audio format and a desired buffer size. This
constructor is typically used by an application to describe a desired
line.

**Parameters:** lineClass

- the class of the data line described by the info
object
**Parameters:** format

- desired format
**Parameters:** bufferSize

- desired buffer size, in bytes

---

#### Info

public Info​(

Class

<?> lineClass,

AudioFormat

format,
int bufferSize)

Constructs a data line's info object from the specified information,
which includes a single audio format and a desired buffer size. This
constructor is typically used by an application to describe a desired
line.

Info

```java
public Info​(
Class
<?> lineClass,

AudioFormat
format)
```

Constructs a data line's info object from the specified information,
which includes a single audio format. This constructor is typically
used by an application to describe a desired line.

**Parameters:** lineClass

- the class of the data line described by the info
object
**Parameters:** format

- desired format

---

#### Info

public Info​(

Class

<?> lineClass,

AudioFormat

format)

Constructs a data line's info object from the specified information,
which includes a single audio format. This constructor is typically
used by an application to describe a desired line.

Method Detail

- getFormats

```java
public
AudioFormat
[] getFormats()
```

Obtains a set of audio formats supported by the data line. Note that

isFormatSupported(AudioFormat)

might return

true

for
certain additional formats that are missing from the set returned by

getFormats()

. The reverse is not the case:

isFormatSupported(AudioFormat)

is guaranteed to return

true

for all formats returned by

getFormats()

.

Some fields in the

AudioFormat

instances can be set to

NOT_SPECIFIED

if that field does
not apply to the format, or if the format supports a wide range of
values for that field. For example, a multi-channel device supporting
up to 64 channels, could set the channel field in the

AudioFormat

instances returned by this method to

NOT_SPECIFIED

.

**Returns:** a set of supported audio formats
**See Also:** isFormatSupported(AudioFormat)

- isFormatSupported

```java
public boolean isFormatSupported​(
AudioFormat
format)
```

Indicates whether this data line supports a particular audio format.
The default implementation of this method simply returns

true

if the specified format matches any of the supported formats.

**Parameters:** format

- the audio format for which support is queried
**Returns:** true

if the format is supported, otherwise

false
**See Also:** getFormats()

,

AudioFormat.matches(javax.sound.sampled.AudioFormat)

- getMinBufferSize

```java
public int getMinBufferSize()
```

Obtains the minimum buffer size supported by the data line.

**Returns:** minimum buffer size in bytes, or

AudioSystem.NOT_SPECIFIED

- getMaxBufferSize

```java
public int getMaxBufferSize()
```

Obtains the maximum buffer size supported by the data line.

**Returns:** maximum buffer size in bytes, or

AudioSystem.NOT_SPECIFIED

- matches

```java
public boolean matches​(
Line.Info
info)
```

Determines whether the specified info object matches this one. To
match, the superclass match requirements must be met. In addition,
this object's minimum buffer size must be at least as large as that
of the object specified, its maximum buffer size must be at most as
large as that of the object specified, and all of its formats must
match formats supported by the object specified.

**Overrides:** matches

in class

Line.Info
**Parameters:** info

- the info object which is being compared to this one
**Returns:** true

if this object matches the one specified,
otherwise

false

- toString

```java
public
String
toString()
```

Obtains a textual description of the data line info.

**Overrides:** toString

in class

Line.Info
**Returns:** a string description

---

#### Method Detail

getFormats

```java
public
AudioFormat
[] getFormats()
```

Obtains a set of audio formats supported by the data line. Note that

isFormatSupported(AudioFormat)

might return

true

for
certain additional formats that are missing from the set returned by

getFormats()

. The reverse is not the case:

isFormatSupported(AudioFormat)

is guaranteed to return

true

for all formats returned by

getFormats()

.

Some fields in the

AudioFormat

instances can be set to

NOT_SPECIFIED

if that field does
not apply to the format, or if the format supports a wide range of
values for that field. For example, a multi-channel device supporting
up to 64 channels, could set the channel field in the

AudioFormat

instances returned by this method to

NOT_SPECIFIED

.

**Returns:** a set of supported audio formats
**See Also:** isFormatSupported(AudioFormat)

---

#### getFormats

public

AudioFormat

[] getFormats()

Obtains a set of audio formats supported by the data line. Note that

isFormatSupported(AudioFormat)

might return

true

for
certain additional formats that are missing from the set returned by

getFormats()

. The reverse is not the case:

isFormatSupported(AudioFormat)

is guaranteed to return

true

for all formats returned by

getFormats()

.

Some fields in the

AudioFormat

instances can be set to

NOT_SPECIFIED

if that field does
not apply to the format, or if the format supports a wide range of
values for that field. For example, a multi-channel device supporting
up to 64 channels, could set the channel field in the

AudioFormat

instances returned by this method to

NOT_SPECIFIED

.

Some fields in the

AudioFormat

instances can be set to

NOT_SPECIFIED

if that field does
not apply to the format, or if the format supports a wide range of
values for that field. For example, a multi-channel device supporting
up to 64 channels, could set the channel field in the

AudioFormat

instances returned by this method to

NOT_SPECIFIED

.

isFormatSupported

```java
public boolean isFormatSupported​(
AudioFormat
format)
```

Indicates whether this data line supports a particular audio format.
The default implementation of this method simply returns

true

if the specified format matches any of the supported formats.

**Parameters:** format

- the audio format for which support is queried
**Returns:** true

if the format is supported, otherwise

false
**See Also:** getFormats()

,

AudioFormat.matches(javax.sound.sampled.AudioFormat)

---

#### isFormatSupported

public boolean isFormatSupported​(

AudioFormat

format)

Indicates whether this data line supports a particular audio format.
The default implementation of this method simply returns

true

if the specified format matches any of the supported formats.

getMinBufferSize

```java
public int getMinBufferSize()
```

Obtains the minimum buffer size supported by the data line.

**Returns:** minimum buffer size in bytes, or

AudioSystem.NOT_SPECIFIED

---

#### getMinBufferSize

public int getMinBufferSize()

Obtains the minimum buffer size supported by the data line.

getMaxBufferSize

```java
public int getMaxBufferSize()
```

Obtains the maximum buffer size supported by the data line.

**Returns:** maximum buffer size in bytes, or

AudioSystem.NOT_SPECIFIED

---

#### getMaxBufferSize

public int getMaxBufferSize()

Obtains the maximum buffer size supported by the data line.

matches

```java
public boolean matches​(
Line.Info
info)
```

Determines whether the specified info object matches this one. To
match, the superclass match requirements must be met. In addition,
this object's minimum buffer size must be at least as large as that
of the object specified, its maximum buffer size must be at most as
large as that of the object specified, and all of its formats must
match formats supported by the object specified.

**Overrides:** matches

in class

Line.Info
**Parameters:** info

- the info object which is being compared to this one
**Returns:** true

if this object matches the one specified,
otherwise

false

---

#### matches

public boolean matches​(

Line.Info

info)

Determines whether the specified info object matches this one. To
match, the superclass match requirements must be met. In addition,
this object's minimum buffer size must be at least as large as that
of the object specified, its maximum buffer size must be at most as
large as that of the object specified, and all of its formats must
match formats supported by the object specified.

toString

```java
public
String
toString()
```

Obtains a textual description of the data line info.

**Overrides:** toString

in class

Line.Info
**Returns:** a string description

---

#### toString

public

String

toString()

Obtains a textual description of the data line info.

---

