# Class MidiFileFormat

**Source:** `java.desktop\javax\sound\midi\MidiFileFormat.html`

### Class Description

```java
public class
MidiFileFormat

extends
Object
```

A

MidiFileFormat

object encapsulates a MIDI file's type, as well as
its length and timing information.

A

MidiFileFormat

object can include a set of properties. A property
is a pair of key and value: the key is of type

String

, the associated
property value is an arbitrary object. Properties specify additional
informational meta data (like a author, or copyright). Properties are
optional information, and file reader and file writer implementations are not
required to provide or recognize properties.

The following table lists some common properties that should be used in
implementations:

MIDI File Format Properties

Property key

Value type

Description

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

**See Also:** MidiSystem.getMidiFileFormat(java.io.File)

,

Sequencer.setSequence(java.io.InputStream stream)

---

### Field Details

#### public static final int UNKNOWN_LENGTH

Represents unknown length.

**See Also:**
- getByteLength()

,

getMicrosecondLength()

,

Constant Field Values

---

#### protected int type

The type of MIDI file.

---

#### protected float divisionType

The division type of the MIDI file.

**See Also:**
- Sequence.PPQ

,

Sequence.SMPTE_24

,

Sequence.SMPTE_25

,

Sequence.SMPTE_30DROP

,

Sequence.SMPTE_30

---

#### protected int resolution

The timing resolution of the MIDI file.

---

#### protected int byteLength

The length of the MIDI file in bytes.

---

#### protected long microsecondLength

The duration of the MIDI file in microseconds.

---

### Constructor Details

#### public MidiFileFormat​(int type,
float divisionType,
int resolution,
int bytes,
long microseconds)

Constructs a

MidiFileFormat

.

**Parameters:**
- type

- the MIDI file type (0, 1, or 2)
- divisionType

- the timing division type (PPQ or one of the SMPTE
types)
- resolution

- the timing resolution
- bytes

- the length of the MIDI file in bytes, or

UNKNOWN_LENGTH

if not known
- microseconds

- the duration of the file in microseconds, or

UNKNOWN_LENGTH

if not known

**See Also:**
- UNKNOWN_LENGTH

,

Sequence.PPQ

,

Sequence.SMPTE_24

,

Sequence.SMPTE_25

,

Sequence.SMPTE_30DROP

,

Sequence.SMPTE_30

---

#### public MidiFileFormat​(int type,
float divisionType,
int resolution,
int bytes,
long microseconds,

Map
<
String
,​
Object
> properties)

Construct a

MidiFileFormat

with a set of properties.

**Parameters:**
- type

- the MIDI file type (0, 1, or 2)
- divisionType

- the timing division type (PPQ or one of the SMPTE
types)
- resolution

- the timing resolution
- bytes

- the length of the MIDI file in bytes, or

UNKNOWN_LENGTH

if not known
- microseconds

- the duration of the file in microseconds, or

UNKNOWN_LENGTH

if not known
- properties

- a

Map<String,Object>

object with properties

**See Also:**
- UNKNOWN_LENGTH

,

Sequence.PPQ

,

Sequence.SMPTE_24

,

Sequence.SMPTE_25

,

Sequence.SMPTE_30DROP

,

Sequence.SMPTE_30

**Since:**
- 1.5

---

### Method Details

#### public int getType()

Obtains the MIDI file type.

**Returns:**
- the file's type (0, 1, or 2)

---

#### public float getDivisionType()

Obtains the timing division type for the MIDI file.

**Returns:**
- the division type (PPQ or one of the SMPTE types)

**See Also:**
- Sequence(float, int)

,

Sequence.PPQ

,

Sequence.SMPTE_24

,

Sequence.SMPTE_25

,

Sequence.SMPTE_30DROP

,

Sequence.SMPTE_30

,

Sequence.getDivisionType()

---

#### public int getResolution()

Obtains the timing resolution for the MIDI file. If the division type is
PPQ, the resolution is specified in ticks per beat. For SMTPE timing, the
resolution is specified in ticks per frame.

**Returns:**
- the number of ticks per beat (PPQ) or per frame (SMPTE)

**See Also:**
- getDivisionType()

,

Sequence.getResolution()

---

#### public int getByteLength()

Obtains the length of the MIDI file, expressed in 8-bit bytes.

**Returns:**
- the number of bytes in the file, or

UNKNOWN_LENGTH

if not
known

**See Also:**
- UNKNOWN_LENGTH

---

#### public long getMicrosecondLength()

Obtains the length of the MIDI file, expressed in microseconds.

**Returns:**
- the file's duration in microseconds, or

UNKNOWN_LENGTH

if
not known

**See Also:**
- Sequence.getMicrosecondLength()

,

getByteLength()

,

UNKNOWN_LENGTH

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

Map<String,Object>

object containing all properties. If
no properties are recognized, an empty map is returned.

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

### Additional Sections

#### Class MidiFileFormat

java.lang.Object

- javax.sound.midi.MidiFileFormat

javax.sound.midi.MidiFileFormat

```java
public class
MidiFileFormat

extends
Object
```

A

MidiFileFormat

object encapsulates a MIDI file's type, as well as
its length and timing information.

A

MidiFileFormat

object can include a set of properties. A property
is a pair of key and value: the key is of type

String

, the associated
property value is an arbitrary object. Properties specify additional
informational meta data (like a author, or copyright). Properties are
optional information, and file reader and file writer implementations are not
required to provide or recognize properties.

The following table lists some common properties that should be used in
implementations:

MIDI File Format Properties

Property key

Value type

Description

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

**See Also:** MidiSystem.getMidiFileFormat(java.io.File)

,

Sequencer.setSequence(java.io.InputStream stream)

public class

MidiFileFormat

extends

Object

A

MidiFileFormat

object encapsulates a MIDI file's type, as well as
its length and timing information.

A

MidiFileFormat

object can include a set of properties. A property
is a pair of key and value: the key is of type

String

, the associated
property value is an arbitrary object. Properties specify additional
informational meta data (like a author, or copyright). Properties are
optional information, and file reader and file writer implementations are not
required to provide or recognize properties.

The following table lists some common properties that should be used in
implementations:

MIDI File Format Properties

Property key

Value type

Description

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

A

MidiFileFormat

object can include a set of properties. A property
is a pair of key and value: the key is of type

String

, the associated
property value is an arbitrary object. Properties specify additional
informational meta data (like a author, or copyright). Properties are
optional information, and file reader and file writer implementations are not
required to provide or recognize properties.

The following table lists some common properties that should be used in
implementations:

MIDI File Format Properties

Property key

Value type

Description

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

MIDI File Format Properties

Property key

Value type

Description

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

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

protected int

byteLength

The length of the MIDI file in bytes.

protected float

divisionType

The division type of the MIDI file.

protected long

microsecondLength

The duration of the MIDI file in microseconds.

protected int

resolution

The timing resolution of the MIDI file.

protected int

type

The type of MIDI file.

static int

UNKNOWN_LENGTH

Represents unknown length.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

MidiFileFormat

​(int type,
float divisionType,
int resolution,
int bytes,
long microseconds)

Constructs a

MidiFileFormat

.

MidiFileFormat

​(int type,
float divisionType,
int resolution,
int bytes,
long microseconds,

Map

<

String

,​

Object

> properties)

Construct a

MidiFileFormat

with a set of properties.

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

Obtains the length of the MIDI file, expressed in 8-bit bytes.

float

getDivisionType

()

Obtains the timing division type for the MIDI file.

long

getMicrosecondLength

()

Obtains the length of the MIDI file, expressed in microseconds.

Object

getProperty

​(

String

key)

Obtain the property value specified by the key.

int

getResolution

()

Obtains the timing resolution for the MIDI file.

int

getType

()

Obtains the MIDI file type.

Map

<

String

,​

Object

>

properties

()

Obtain an unmodifiable map of properties.

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

protected int

byteLength

The length of the MIDI file in bytes.

protected float

divisionType

The division type of the MIDI file.

protected long

microsecondLength

The duration of the MIDI file in microseconds.

protected int

resolution

The timing resolution of the MIDI file.

protected int

type

The type of MIDI file.

static int

UNKNOWN_LENGTH

Represents unknown length.

---

#### Field Summary

The length of the MIDI file in bytes.

The division type of the MIDI file.

The duration of the MIDI file in microseconds.

The timing resolution of the MIDI file.

The type of MIDI file.

Represents unknown length.

Constructor Summary

Constructors

Constructor

Description

MidiFileFormat

​(int type,
float divisionType,
int resolution,
int bytes,
long microseconds)

Constructs a

MidiFileFormat

.

MidiFileFormat

​(int type,
float divisionType,
int resolution,
int bytes,
long microseconds,

Map

<

String

,​

Object

> properties)

Construct a

MidiFileFormat

with a set of properties.

---

#### Constructor Summary

Constructs a

MidiFileFormat

.

Construct a

MidiFileFormat

with a set of properties.

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

Obtains the length of the MIDI file, expressed in 8-bit bytes.

float

getDivisionType

()

Obtains the timing division type for the MIDI file.

long

getMicrosecondLength

()

Obtains the length of the MIDI file, expressed in microseconds.

Object

getProperty

​(

String

key)

Obtain the property value specified by the key.

int

getResolution

()

Obtains the timing resolution for the MIDI file.

int

getType

()

Obtains the MIDI file type.

Map

<

String

,​

Object

>

properties

()

Obtain an unmodifiable map of properties.

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

Obtains the length of the MIDI file, expressed in 8-bit bytes.

Obtains the timing division type for the MIDI file.

Obtains the length of the MIDI file, expressed in microseconds.

Obtain the property value specified by the key.

Obtains the timing resolution for the MIDI file.

Obtains the MIDI file type.

Obtain an unmodifiable map of properties.

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

- UNKNOWN_LENGTH

```java
public static final int UNKNOWN_LENGTH
```

Represents unknown length.

**See Also:** getByteLength()

,

getMicrosecondLength()

,

Constant Field Values

- type

```java
protected int type
```

The type of MIDI file.

- divisionType

```java
protected float divisionType
```

The division type of the MIDI file.

**See Also:** Sequence.PPQ

,

Sequence.SMPTE_24

,

Sequence.SMPTE_25

,

Sequence.SMPTE_30DROP

,

Sequence.SMPTE_30

- resolution

```java
protected int resolution
```

The timing resolution of the MIDI file.

- byteLength

```java
protected int byteLength
```

The length of the MIDI file in bytes.

- microsecondLength

```java
protected long microsecondLength
```

The duration of the MIDI file in microseconds.

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- MidiFileFormat

```java
public MidiFileFormat​(int type,
float divisionType,
int resolution,
int bytes,
long microseconds)
```

Constructs a

MidiFileFormat

.

**Parameters:** type

- the MIDI file type (0, 1, or 2)
**Parameters:** divisionType

- the timing division type (PPQ or one of the SMPTE
types)
**Parameters:** resolution

- the timing resolution
**Parameters:** bytes

- the length of the MIDI file in bytes, or

UNKNOWN_LENGTH

if not known
**Parameters:** microseconds

- the duration of the file in microseconds, or

UNKNOWN_LENGTH

if not known
**See Also:** UNKNOWN_LENGTH

,

Sequence.PPQ

,

Sequence.SMPTE_24

,

Sequence.SMPTE_25

,

Sequence.SMPTE_30DROP

,

Sequence.SMPTE_30

- MidiFileFormat

```java
public MidiFileFormat​(int type,
float divisionType,
int resolution,
int bytes,
long microseconds,

Map
<
String
,​
Object
> properties)
```

Construct a

MidiFileFormat

with a set of properties.

**Parameters:** type

- the MIDI file type (0, 1, or 2)
**Parameters:** divisionType

- the timing division type (PPQ or one of the SMPTE
types)
**Parameters:** resolution

- the timing resolution
**Parameters:** bytes

- the length of the MIDI file in bytes, or

UNKNOWN_LENGTH

if not known
**Parameters:** microseconds

- the duration of the file in microseconds, or

UNKNOWN_LENGTH

if not known
**Parameters:** properties

- a

Map<String,Object>

object with properties
**Since:** 1.5
**See Also:** UNKNOWN_LENGTH

,

Sequence.PPQ

,

Sequence.SMPTE_24

,

Sequence.SMPTE_25

,

Sequence.SMPTE_30DROP

,

Sequence.SMPTE_30

============ METHOD DETAIL ==========

- Method Detail

- getType

```java
public int getType()
```

Obtains the MIDI file type.

**Returns:** the file's type (0, 1, or 2)

- getDivisionType

```java
public float getDivisionType()
```

Obtains the timing division type for the MIDI file.

**Returns:** the division type (PPQ or one of the SMPTE types)
**See Also:** Sequence(float, int)

,

Sequence.PPQ

,

Sequence.SMPTE_24

,

Sequence.SMPTE_25

,

Sequence.SMPTE_30DROP

,

Sequence.SMPTE_30

,

Sequence.getDivisionType()

- getResolution

```java
public int getResolution()
```

Obtains the timing resolution for the MIDI file. If the division type is
PPQ, the resolution is specified in ticks per beat. For SMTPE timing, the
resolution is specified in ticks per frame.

**Returns:** the number of ticks per beat (PPQ) or per frame (SMPTE)
**See Also:** getDivisionType()

,

Sequence.getResolution()

- getByteLength

```java
public int getByteLength()
```

Obtains the length of the MIDI file, expressed in 8-bit bytes.

**Returns:** the number of bytes in the file, or

UNKNOWN_LENGTH

if not
known
**See Also:** UNKNOWN_LENGTH

- getMicrosecondLength

```java
public long getMicrosecondLength()
```

Obtains the length of the MIDI file, expressed in microseconds.

**Returns:** the file's duration in microseconds, or

UNKNOWN_LENGTH

if
not known
**See Also:** Sequence.getMicrosecondLength()

,

getByteLength()

,

UNKNOWN_LENGTH

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

Map<String,Object>

object containing all properties. If
no properties are recognized, an empty map is returned.
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

Field Detail

- UNKNOWN_LENGTH

```java
public static final int UNKNOWN_LENGTH
```

Represents unknown length.

**See Also:** getByteLength()

,

getMicrosecondLength()

,

Constant Field Values

- type

```java
protected int type
```

The type of MIDI file.

- divisionType

```java
protected float divisionType
```

The division type of the MIDI file.

**See Also:** Sequence.PPQ

,

Sequence.SMPTE_24

,

Sequence.SMPTE_25

,

Sequence.SMPTE_30DROP

,

Sequence.SMPTE_30

- resolution

```java
protected int resolution
```

The timing resolution of the MIDI file.

- byteLength

```java
protected int byteLength
```

The length of the MIDI file in bytes.

- microsecondLength

```java
protected long microsecondLength
```

The duration of the MIDI file in microseconds.

---

#### Field Detail

UNKNOWN_LENGTH

```java
public static final int UNKNOWN_LENGTH
```

Represents unknown length.

**See Also:** getByteLength()

,

getMicrosecondLength()

,

Constant Field Values

---

#### UNKNOWN_LENGTH

public static final int UNKNOWN_LENGTH

Represents unknown length.

type

```java
protected int type
```

The type of MIDI file.

---

#### type

protected int type

The type of MIDI file.

divisionType

```java
protected float divisionType
```

The division type of the MIDI file.

**See Also:** Sequence.PPQ

,

Sequence.SMPTE_24

,

Sequence.SMPTE_25

,

Sequence.SMPTE_30DROP

,

Sequence.SMPTE_30

---

#### divisionType

protected float divisionType

The division type of the MIDI file.

resolution

```java
protected int resolution
```

The timing resolution of the MIDI file.

---

#### resolution

protected int resolution

The timing resolution of the MIDI file.

byteLength

```java
protected int byteLength
```

The length of the MIDI file in bytes.

---

#### byteLength

protected int byteLength

The length of the MIDI file in bytes.

microsecondLength

```java
protected long microsecondLength
```

The duration of the MIDI file in microseconds.

---

#### microsecondLength

protected long microsecondLength

The duration of the MIDI file in microseconds.

Constructor Detail

- MidiFileFormat

```java
public MidiFileFormat​(int type,
float divisionType,
int resolution,
int bytes,
long microseconds)
```

Constructs a

MidiFileFormat

.

**Parameters:** type

- the MIDI file type (0, 1, or 2)
**Parameters:** divisionType

- the timing division type (PPQ or one of the SMPTE
types)
**Parameters:** resolution

- the timing resolution
**Parameters:** bytes

- the length of the MIDI file in bytes, or

UNKNOWN_LENGTH

if not known
**Parameters:** microseconds

- the duration of the file in microseconds, or

UNKNOWN_LENGTH

if not known
**See Also:** UNKNOWN_LENGTH

,

Sequence.PPQ

,

Sequence.SMPTE_24

,

Sequence.SMPTE_25

,

Sequence.SMPTE_30DROP

,

Sequence.SMPTE_30

- MidiFileFormat

```java
public MidiFileFormat​(int type,
float divisionType,
int resolution,
int bytes,
long microseconds,

Map
<
String
,​
Object
> properties)
```

Construct a

MidiFileFormat

with a set of properties.

**Parameters:** type

- the MIDI file type (0, 1, or 2)
**Parameters:** divisionType

- the timing division type (PPQ or one of the SMPTE
types)
**Parameters:** resolution

- the timing resolution
**Parameters:** bytes

- the length of the MIDI file in bytes, or

UNKNOWN_LENGTH

if not known
**Parameters:** microseconds

- the duration of the file in microseconds, or

UNKNOWN_LENGTH

if not known
**Parameters:** properties

- a

Map<String,Object>

object with properties
**Since:** 1.5
**See Also:** UNKNOWN_LENGTH

,

Sequence.PPQ

,

Sequence.SMPTE_24

,

Sequence.SMPTE_25

,

Sequence.SMPTE_30DROP

,

Sequence.SMPTE_30

---

#### Constructor Detail

MidiFileFormat

```java
public MidiFileFormat​(int type,
float divisionType,
int resolution,
int bytes,
long microseconds)
```

Constructs a

MidiFileFormat

.

**Parameters:** type

- the MIDI file type (0, 1, or 2)
**Parameters:** divisionType

- the timing division type (PPQ or one of the SMPTE
types)
**Parameters:** resolution

- the timing resolution
**Parameters:** bytes

- the length of the MIDI file in bytes, or

UNKNOWN_LENGTH

if not known
**Parameters:** microseconds

- the duration of the file in microseconds, or

UNKNOWN_LENGTH

if not known
**See Also:** UNKNOWN_LENGTH

,

Sequence.PPQ

,

Sequence.SMPTE_24

,

Sequence.SMPTE_25

,

Sequence.SMPTE_30DROP

,

Sequence.SMPTE_30

---

#### MidiFileFormat

public MidiFileFormat​(int type,
float divisionType,
int resolution,
int bytes,
long microseconds)

Constructs a

MidiFileFormat

.

MidiFileFormat

```java
public MidiFileFormat​(int type,
float divisionType,
int resolution,
int bytes,
long microseconds,

Map
<
String
,​
Object
> properties)
```

Construct a

MidiFileFormat

with a set of properties.

**Parameters:** type

- the MIDI file type (0, 1, or 2)
**Parameters:** divisionType

- the timing division type (PPQ or one of the SMPTE
types)
**Parameters:** resolution

- the timing resolution
**Parameters:** bytes

- the length of the MIDI file in bytes, or

UNKNOWN_LENGTH

if not known
**Parameters:** microseconds

- the duration of the file in microseconds, or

UNKNOWN_LENGTH

if not known
**Parameters:** properties

- a

Map<String,Object>

object with properties
**Since:** 1.5
**See Also:** UNKNOWN_LENGTH

,

Sequence.PPQ

,

Sequence.SMPTE_24

,

Sequence.SMPTE_25

,

Sequence.SMPTE_30DROP

,

Sequence.SMPTE_30

---

#### MidiFileFormat

public MidiFileFormat​(int type,
float divisionType,
int resolution,
int bytes,
long microseconds,

Map

<

String

,​

Object

> properties)

Construct a

MidiFileFormat

with a set of properties.

Method Detail

- getType

```java
public int getType()
```

Obtains the MIDI file type.

**Returns:** the file's type (0, 1, or 2)

- getDivisionType

```java
public float getDivisionType()
```

Obtains the timing division type for the MIDI file.

**Returns:** the division type (PPQ or one of the SMPTE types)
**See Also:** Sequence(float, int)

,

Sequence.PPQ

,

Sequence.SMPTE_24

,

Sequence.SMPTE_25

,

Sequence.SMPTE_30DROP

,

Sequence.SMPTE_30

,

Sequence.getDivisionType()

- getResolution

```java
public int getResolution()
```

Obtains the timing resolution for the MIDI file. If the division type is
PPQ, the resolution is specified in ticks per beat. For SMTPE timing, the
resolution is specified in ticks per frame.

**Returns:** the number of ticks per beat (PPQ) or per frame (SMPTE)
**See Also:** getDivisionType()

,

Sequence.getResolution()

- getByteLength

```java
public int getByteLength()
```

Obtains the length of the MIDI file, expressed in 8-bit bytes.

**Returns:** the number of bytes in the file, or

UNKNOWN_LENGTH

if not
known
**See Also:** UNKNOWN_LENGTH

- getMicrosecondLength

```java
public long getMicrosecondLength()
```

Obtains the length of the MIDI file, expressed in microseconds.

**Returns:** the file's duration in microseconds, or

UNKNOWN_LENGTH

if
not known
**See Also:** Sequence.getMicrosecondLength()

,

getByteLength()

,

UNKNOWN_LENGTH

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

Map<String,Object>

object containing all properties. If
no properties are recognized, an empty map is returned.
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

---

#### Method Detail

getType

```java
public int getType()
```

Obtains the MIDI file type.

**Returns:** the file's type (0, 1, or 2)

---

#### getType

public int getType()

Obtains the MIDI file type.

getDivisionType

```java
public float getDivisionType()
```

Obtains the timing division type for the MIDI file.

**Returns:** the division type (PPQ or one of the SMPTE types)
**See Also:** Sequence(float, int)

,

Sequence.PPQ

,

Sequence.SMPTE_24

,

Sequence.SMPTE_25

,

Sequence.SMPTE_30DROP

,

Sequence.SMPTE_30

,

Sequence.getDivisionType()

---

#### getDivisionType

public float getDivisionType()

Obtains the timing division type for the MIDI file.

getResolution

```java
public int getResolution()
```

Obtains the timing resolution for the MIDI file. If the division type is
PPQ, the resolution is specified in ticks per beat. For SMTPE timing, the
resolution is specified in ticks per frame.

**Returns:** the number of ticks per beat (PPQ) or per frame (SMPTE)
**See Also:** getDivisionType()

,

Sequence.getResolution()

---

#### getResolution

public int getResolution()

Obtains the timing resolution for the MIDI file. If the division type is
PPQ, the resolution is specified in ticks per beat. For SMTPE timing, the
resolution is specified in ticks per frame.

getByteLength

```java
public int getByteLength()
```

Obtains the length of the MIDI file, expressed in 8-bit bytes.

**Returns:** the number of bytes in the file, or

UNKNOWN_LENGTH

if not
known
**See Also:** UNKNOWN_LENGTH

---

#### getByteLength

public int getByteLength()

Obtains the length of the MIDI file, expressed in 8-bit bytes.

getMicrosecondLength

```java
public long getMicrosecondLength()
```

Obtains the length of the MIDI file, expressed in microseconds.

**Returns:** the file's duration in microseconds, or

UNKNOWN_LENGTH

if
not known
**See Also:** Sequence.getMicrosecondLength()

,

getByteLength()

,

UNKNOWN_LENGTH

---

#### getMicrosecondLength

public long getMicrosecondLength()

Obtains the length of the MIDI file, expressed in microseconds.

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

Map<String,Object>

object containing all properties. If
no properties are recognized, an empty map is returned.
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

---

