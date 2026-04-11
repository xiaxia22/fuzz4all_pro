# Class MidiMessage

**Source:** `java.desktop\javax\sound\midi\MidiMessage.html`

### Class Description

```java
public abstract class
MidiMessage

extends
Object

implements
Cloneable
```

MidiMessage

is the base class for MIDI messages. They include not
only the standard MIDI messages that a synthesizer can respond to, but also
"meta-events" that can be used by sequencer programs. There are meta-events
for such information as lyrics, copyrights, tempo indications, time and key
signatures, markers, etc. For more information, see the Standard MIDI Files
1.0 specification, which is part of the Complete MIDI 1.0 Detailed
Specification published by the MIDI Manufacturer's Association
(

http://www.midi.org

).

The base

MidiMessage

class provides access to three types of
information about a MIDI message:

- The messages's status byte

The total length of the message in bytes (the status byte plus any data
bytes)

A byte array containing the complete message

MidiMessage

includes methods to get, but not set, these values.
Setting them is a subclass responsibility.

The MIDI standard expresses MIDI data in bytes.
However, because Java™ uses signed bytes, the Java Sound API uses
integers instead of bytes when expressing MIDI data. For example, the

getStatus()

method of

MidiMessage

returns MIDI status bytes
as integers. If you are processing MIDI data that originated outside Java
Sound and now is encoded as signed bytes, the bytes can be converted to
integers using this conversion:

int i = (int)(byte & 0xFF)

If you simply need to pass a known MIDI byte value as a method parameter, it
can be expressed directly as an integer, using (for example) decimal or
hexadecimal notation. For instance, to pass the "active sensing" status byte
as the first argument to

ShortMessage

's

setMessage(int)

method, you can express
it as 254 or 0xFE.

**All Implemented Interfaces:** Cloneable

---

### Field Details

#### protected byte[] data

The MIDI message data. The first byte is the status byte for the message;
subsequent bytes up to the length of the message are data bytes for this
message.

**See Also:**
- getLength()

---

#### protected int length

The number of bytes in the MIDI message, including the status byte and
any data bytes.

**See Also:**
- getLength()

---

### Constructor Details

#### protected MidiMessage​(byte[] data)

Constructs a new

MidiMessage

. This protected constructor is
called by concrete subclasses, which should ensure that the data array
specifies a complete, valid MIDI message.

**Parameters:**
- data

- an array of bytes containing the complete message. The
message data may be changed using the

setMessage

method.

**See Also:**
- setMessage(byte[], int)

---

### Method Details

#### protected void setMessage​(byte[] data,
int length)
throws
InvalidMidiDataException

Sets the data for the MIDI message. This protected method is called by
concrete subclasses, which should ensure that the data array specifies a
complete, valid MIDI message.

**Parameters:**
- data

- the data bytes in the MIDI message
- length

- the number of bytes in the data byte array

**Throws:**
- InvalidMidiDataException

- if the parameter values do not specify a
valid MIDI meta message

---

#### public byte[] getMessage()

Obtains the MIDI message data. The first byte of the returned byte array
is the status byte of the message. Any subsequent bytes up to the length
of the message are data bytes. The byte array may have a length which is
greater than that of the actual message; the total length of the message
in bytes is reported by the

getLength()

method.

**Returns:**
- the byte array containing the complete

MidiMessage

data

---

#### public int getStatus()

Obtains the status byte for the MIDI message. The status "byte" is
represented as an integer; see the

discussion

in the

MidiMessage

class description.

**Returns:**
- the integer representation of this event's status byte

---

#### public int getLength()

Obtains the total length of the MIDI message in bytes. A MIDI message
consists of one status byte and zero or more data bytes. The return value
ranges from 1 for system real-time messages, to 2 or 3 for channel
messages, to any value for meta and system exclusive messages.

**Returns:**
- the length of the message in bytes

---

#### public abstract
Object
clone()

Creates a new object of the same class and with the same contents as this
object.

**Overrides:**
- clone

in class

Object

**Returns:**
- a clone of this instance

**See Also:**
- Cloneable

---

### Additional Sections

#### Class MidiMessage

java.lang.Object

- javax.sound.midi.MidiMessage

javax.sound.midi.MidiMessage

**All Implemented Interfaces:** Cloneable

**Direct Known Subclasses:** MetaMessage

,

ShortMessage

,

SysexMessage

```java
public abstract class
MidiMessage

extends
Object

implements
Cloneable
```

MidiMessage

is the base class for MIDI messages. They include not
only the standard MIDI messages that a synthesizer can respond to, but also
"meta-events" that can be used by sequencer programs. There are meta-events
for such information as lyrics, copyrights, tempo indications, time and key
signatures, markers, etc. For more information, see the Standard MIDI Files
1.0 specification, which is part of the Complete MIDI 1.0 Detailed
Specification published by the MIDI Manufacturer's Association
(

http://www.midi.org

).

The base

MidiMessage

class provides access to three types of
information about a MIDI message:

- The messages's status byte

The total length of the message in bytes (the status byte plus any data
bytes)

A byte array containing the complete message

MidiMessage

includes methods to get, but not set, these values.
Setting them is a subclass responsibility.

The MIDI standard expresses MIDI data in bytes.
However, because Java™ uses signed bytes, the Java Sound API uses
integers instead of bytes when expressing MIDI data. For example, the

getStatus()

method of

MidiMessage

returns MIDI status bytes
as integers. If you are processing MIDI data that originated outside Java
Sound and now is encoded as signed bytes, the bytes can be converted to
integers using this conversion:

int i = (int)(byte & 0xFF)

If you simply need to pass a known MIDI byte value as a method parameter, it
can be expressed directly as an integer, using (for example) decimal or
hexadecimal notation. For instance, to pass the "active sensing" status byte
as the first argument to

ShortMessage

's

setMessage(int)

method, you can express
it as 254 or 0xFE.

**See Also:** Track

,

Sequence

,

Receiver

public abstract class

MidiMessage

extends

Object

implements

Cloneable

MidiMessage

is the base class for MIDI messages. They include not
only the standard MIDI messages that a synthesizer can respond to, but also
"meta-events" that can be used by sequencer programs. There are meta-events
for such information as lyrics, copyrights, tempo indications, time and key
signatures, markers, etc. For more information, see the Standard MIDI Files
1.0 specification, which is part of the Complete MIDI 1.0 Detailed
Specification published by the MIDI Manufacturer's Association
(

http://www.midi.org

).

The base

MidiMessage

class provides access to three types of
information about a MIDI message:

- The messages's status byte

The total length of the message in bytes (the status byte plus any data
bytes)

A byte array containing the complete message

MidiMessage

includes methods to get, but not set, these values.
Setting them is a subclass responsibility.

The MIDI standard expresses MIDI data in bytes.
However, because Java™ uses signed bytes, the Java Sound API uses
integers instead of bytes when expressing MIDI data. For example, the

getStatus()

method of

MidiMessage

returns MIDI status bytes
as integers. If you are processing MIDI data that originated outside Java
Sound and now is encoded as signed bytes, the bytes can be converted to
integers using this conversion:

int i = (int)(byte & 0xFF)

If you simply need to pass a known MIDI byte value as a method parameter, it
can be expressed directly as an integer, using (for example) decimal or
hexadecimal notation. For instance, to pass the "active sensing" status byte
as the first argument to

ShortMessage

's

setMessage(int)

method, you can express
it as 254 or 0xFE.

The base

MidiMessage

class provides access to three types of
information about a MIDI message:

- The messages's status byte

The total length of the message in bytes (the status byte plus any data
bytes)

A byte array containing the complete message

MidiMessage

includes methods to get, but not set, these values.
Setting them is a subclass responsibility.

The MIDI standard expresses MIDI data in bytes.
However, because Java™ uses signed bytes, the Java Sound API uses
integers instead of bytes when expressing MIDI data. For example, the

getStatus()

method of

MidiMessage

returns MIDI status bytes
as integers. If you are processing MIDI data that originated outside Java
Sound and now is encoded as signed bytes, the bytes can be converted to
integers using this conversion:

int i = (int)(byte & 0xFF)

If you simply need to pass a known MIDI byte value as a method parameter, it
can be expressed directly as an integer, using (for example) decimal or
hexadecimal notation. For instance, to pass the "active sensing" status byte
as the first argument to

ShortMessage

's

setMessage(int)

method, you can express
it as 254 or 0xFE.

The messages's status byte

The total length of the message in bytes (the status byte plus any data
bytes)

A byte array containing the complete message

The MIDI standard expresses MIDI data in bytes.
However, because Java™ uses signed bytes, the Java Sound API uses
integers instead of bytes when expressing MIDI data. For example, the

getStatus()

method of

MidiMessage

returns MIDI status bytes
as integers. If you are processing MIDI data that originated outside Java
Sound and now is encoded as signed bytes, the bytes can be converted to
integers using this conversion:

int i = (int)(byte & 0xFF)

If you simply need to pass a known MIDI byte value as a method parameter, it
can be expressed directly as an integer, using (for example) decimal or
hexadecimal notation. For instance, to pass the "active sensing" status byte
as the first argument to

ShortMessage

's

setMessage(int)

method, you can express
it as 254 or 0xFE.

int i = (int)(byte & 0xFF)

If you simply need to pass a known MIDI byte value as a method parameter, it
can be expressed directly as an integer, using (for example) decimal or
hexadecimal notation. For instance, to pass the "active sensing" status byte
as the first argument to

ShortMessage

's

setMessage(int)

method, you can express
it as 254 or 0xFE.

If you simply need to pass a known MIDI byte value as a method parameter, it
can be expressed directly as an integer, using (for example) decimal or
hexadecimal notation. For instance, to pass the "active sensing" status byte
as the first argument to

ShortMessage

's

setMessage(int)

method, you can express
it as 254 or 0xFE.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

protected byte[]

data

The MIDI message data.

protected int

length

The number of bytes in the MIDI message, including the status byte and
any data bytes.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

MidiMessage

​(byte[] data)

Constructs a new

MidiMessage

.

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

Object

clone

()

Creates a new object of the same class and with the same contents as this
object.

int

getLength

()

Obtains the total length of the MIDI message in bytes.

byte[]

getMessage

()

Obtains the MIDI message data.

int

getStatus

()

Obtains the status byte for the MIDI message.

protected void

setMessage

​(byte[] data,
int length)

Sets the data for the MIDI message.

- Methods declared in class java.lang.

Object

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

protected byte[]

data

The MIDI message data.

protected int

length

The number of bytes in the MIDI message, including the status byte and
any data bytes.

---

#### Field Summary

The MIDI message data.

The number of bytes in the MIDI message, including the status byte and
any data bytes.

Constructor Summary

Constructors

Modifier

Constructor

Description

protected

MidiMessage

​(byte[] data)

Constructs a new

MidiMessage

.

---

#### Constructor Summary

Constructs a new

MidiMessage

.

Method Summary

All Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

abstract

Object

clone

()

Creates a new object of the same class and with the same contents as this
object.

int

getLength

()

Obtains the total length of the MIDI message in bytes.

byte[]

getMessage

()

Obtains the MIDI message data.

int

getStatus

()

Obtains the status byte for the MIDI message.

protected void

setMessage

​(byte[] data,
int length)

Sets the data for the MIDI message.

- Methods declared in class java.lang.

Object

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

Creates a new object of the same class and with the same contents as this
object.

Obtains the total length of the MIDI message in bytes.

Obtains the MIDI message data.

Obtains the status byte for the MIDI message.

Sets the data for the MIDI message.

Methods declared in class java.lang.

Object

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

- data

```java
protected byte[] data
```

The MIDI message data. The first byte is the status byte for the message;
subsequent bytes up to the length of the message are data bytes for this
message.

**See Also:** getLength()

- length

```java
protected int length
```

The number of bytes in the MIDI message, including the status byte and
any data bytes.

**See Also:** getLength()

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- MidiMessage

```java
protected MidiMessage​(byte[] data)
```

Constructs a new

MidiMessage

. This protected constructor is
called by concrete subclasses, which should ensure that the data array
specifies a complete, valid MIDI message.

**Parameters:** data

- an array of bytes containing the complete message. The
message data may be changed using the

setMessage

method.
**See Also:** setMessage(byte[], int)

============ METHOD DETAIL ==========

- Method Detail

- setMessage

```java
protected void setMessage​(byte[] data,
int length)
throws
InvalidMidiDataException
```

Sets the data for the MIDI message. This protected method is called by
concrete subclasses, which should ensure that the data array specifies a
complete, valid MIDI message.

**Parameters:** data

- the data bytes in the MIDI message
**Parameters:** length

- the number of bytes in the data byte array
**Throws:** InvalidMidiDataException

- if the parameter values do not specify a
valid MIDI meta message

- getMessage

```java
public byte[] getMessage()
```

Obtains the MIDI message data. The first byte of the returned byte array
is the status byte of the message. Any subsequent bytes up to the length
of the message are data bytes. The byte array may have a length which is
greater than that of the actual message; the total length of the message
in bytes is reported by the

getLength()

method.

**Returns:** the byte array containing the complete

MidiMessage

data

- getStatus

```java
public int getStatus()
```

Obtains the status byte for the MIDI message. The status "byte" is
represented as an integer; see the

discussion

in the

MidiMessage

class description.

**Returns:** the integer representation of this event's status byte

- getLength

```java
public int getLength()
```

Obtains the total length of the MIDI message in bytes. A MIDI message
consists of one status byte and zero or more data bytes. The return value
ranges from 1 for system real-time messages, to 2 or 3 for channel
messages, to any value for meta and system exclusive messages.

**Returns:** the length of the message in bytes

- clone

```java
public abstract
Object
clone()
```

Creates a new object of the same class and with the same contents as this
object.

**Overrides:** clone

in class

Object
**Returns:** a clone of this instance
**See Also:** Cloneable

Field Detail

- data

```java
protected byte[] data
```

The MIDI message data. The first byte is the status byte for the message;
subsequent bytes up to the length of the message are data bytes for this
message.

**See Also:** getLength()

- length

```java
protected int length
```

The number of bytes in the MIDI message, including the status byte and
any data bytes.

**See Also:** getLength()

---

#### Field Detail

data

```java
protected byte[] data
```

The MIDI message data. The first byte is the status byte for the message;
subsequent bytes up to the length of the message are data bytes for this
message.

**See Also:** getLength()

---

#### data

protected byte[] data

The MIDI message data. The first byte is the status byte for the message;
subsequent bytes up to the length of the message are data bytes for this
message.

length

```java
protected int length
```

The number of bytes in the MIDI message, including the status byte and
any data bytes.

**See Also:** getLength()

---

#### length

protected int length

The number of bytes in the MIDI message, including the status byte and
any data bytes.

Constructor Detail

- MidiMessage

```java
protected MidiMessage​(byte[] data)
```

Constructs a new

MidiMessage

. This protected constructor is
called by concrete subclasses, which should ensure that the data array
specifies a complete, valid MIDI message.

**Parameters:** data

- an array of bytes containing the complete message. The
message data may be changed using the

setMessage

method.
**See Also:** setMessage(byte[], int)

---

#### Constructor Detail

MidiMessage

```java
protected MidiMessage​(byte[] data)
```

Constructs a new

MidiMessage

. This protected constructor is
called by concrete subclasses, which should ensure that the data array
specifies a complete, valid MIDI message.

**Parameters:** data

- an array of bytes containing the complete message. The
message data may be changed using the

setMessage

method.
**See Also:** setMessage(byte[], int)

---

#### MidiMessage

protected MidiMessage​(byte[] data)

Constructs a new

MidiMessage

. This protected constructor is
called by concrete subclasses, which should ensure that the data array
specifies a complete, valid MIDI message.

Method Detail

- setMessage

```java
protected void setMessage​(byte[] data,
int length)
throws
InvalidMidiDataException
```

Sets the data for the MIDI message. This protected method is called by
concrete subclasses, which should ensure that the data array specifies a
complete, valid MIDI message.

**Parameters:** data

- the data bytes in the MIDI message
**Parameters:** length

- the number of bytes in the data byte array
**Throws:** InvalidMidiDataException

- if the parameter values do not specify a
valid MIDI meta message

- getMessage

```java
public byte[] getMessage()
```

Obtains the MIDI message data. The first byte of the returned byte array
is the status byte of the message. Any subsequent bytes up to the length
of the message are data bytes. The byte array may have a length which is
greater than that of the actual message; the total length of the message
in bytes is reported by the

getLength()

method.

**Returns:** the byte array containing the complete

MidiMessage

data

- getStatus

```java
public int getStatus()
```

Obtains the status byte for the MIDI message. The status "byte" is
represented as an integer; see the

discussion

in the

MidiMessage

class description.

**Returns:** the integer representation of this event's status byte

- getLength

```java
public int getLength()
```

Obtains the total length of the MIDI message in bytes. A MIDI message
consists of one status byte and zero or more data bytes. The return value
ranges from 1 for system real-time messages, to 2 or 3 for channel
messages, to any value for meta and system exclusive messages.

**Returns:** the length of the message in bytes

- clone

```java
public abstract
Object
clone()
```

Creates a new object of the same class and with the same contents as this
object.

**Overrides:** clone

in class

Object
**Returns:** a clone of this instance
**See Also:** Cloneable

---

#### Method Detail

setMessage

```java
protected void setMessage​(byte[] data,
int length)
throws
InvalidMidiDataException
```

Sets the data for the MIDI message. This protected method is called by
concrete subclasses, which should ensure that the data array specifies a
complete, valid MIDI message.

**Parameters:** data

- the data bytes in the MIDI message
**Parameters:** length

- the number of bytes in the data byte array
**Throws:** InvalidMidiDataException

- if the parameter values do not specify a
valid MIDI meta message

---

#### setMessage

protected void setMessage​(byte[] data,
int length)
throws

InvalidMidiDataException

Sets the data for the MIDI message. This protected method is called by
concrete subclasses, which should ensure that the data array specifies a
complete, valid MIDI message.

getMessage

```java
public byte[] getMessage()
```

Obtains the MIDI message data. The first byte of the returned byte array
is the status byte of the message. Any subsequent bytes up to the length
of the message are data bytes. The byte array may have a length which is
greater than that of the actual message; the total length of the message
in bytes is reported by the

getLength()

method.

**Returns:** the byte array containing the complete

MidiMessage

data

---

#### getMessage

public byte[] getMessage()

Obtains the MIDI message data. The first byte of the returned byte array
is the status byte of the message. Any subsequent bytes up to the length
of the message are data bytes. The byte array may have a length which is
greater than that of the actual message; the total length of the message
in bytes is reported by the

getLength()

method.

getStatus

```java
public int getStatus()
```

Obtains the status byte for the MIDI message. The status "byte" is
represented as an integer; see the

discussion

in the

MidiMessage

class description.

**Returns:** the integer representation of this event's status byte

---

#### getStatus

public int getStatus()

Obtains the status byte for the MIDI message. The status "byte" is
represented as an integer; see the

discussion

in the

MidiMessage

class description.

getLength

```java
public int getLength()
```

Obtains the total length of the MIDI message in bytes. A MIDI message
consists of one status byte and zero or more data bytes. The return value
ranges from 1 for system real-time messages, to 2 or 3 for channel
messages, to any value for meta and system exclusive messages.

**Returns:** the length of the message in bytes

---

#### getLength

public int getLength()

Obtains the total length of the MIDI message in bytes. A MIDI message
consists of one status byte and zero or more data bytes. The return value
ranges from 1 for system real-time messages, to 2 or 3 for channel
messages, to any value for meta and system exclusive messages.

clone

```java
public abstract
Object
clone()
```

Creates a new object of the same class and with the same contents as this
object.

**Overrides:** clone

in class

Object
**Returns:** a clone of this instance
**See Also:** Cloneable

---

#### clone

public abstract

Object

clone()

Creates a new object of the same class and with the same contents as this
object.

---

