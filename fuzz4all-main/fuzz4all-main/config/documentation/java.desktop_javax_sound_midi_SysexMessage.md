# Class SysexMessage

**Source:** `java.desktop\javax\sound\midi\SysexMessage.html`

### Class Description

```java
public class
SysexMessage

extends
MidiMessage
```

A

SysexMessage

object represents a MIDI system exclusive message.

When a system exclusive message is read from a MIDI file, it always has a
defined length. Data from a system exclusive message from a MIDI file should
be stored in the data array of a

SysexMessage

as follows: the system
exclusive message status byte (0xF0 or 0xF7), all message data bytes, and
finally the end-of-exclusive flag (0xF7). The length reported by the

SysexMessage

object is therefore the length of the system exclusive
data plus two: one byte for the status byte and one for the end-of-exclusive
flag.

As dictated by the Standard MIDI Files specification, two status byte values
are legal for a

SysexMessage

read from a MIDI file:

- 0xF0: System Exclusive message (same as in MIDI wire protocol)

0xF7: Special System Exclusive message

When Java Sound is used to handle system exclusive data that is being
received using MIDI wire protocol, it should place the data in one or more

SysexMessages

. In this case, the length of the system exclusive data
is not known in advance; the end of the system exclusive data is marked by an
end-of-exclusive flag (0xF7) in the MIDI wire byte stream.

- 0xF0: System Exclusive message (same as in MIDI wire protocol)

0xF7: End of Exclusive (EOX)

The first

SysexMessage

object containing data for a particular system
exclusive message should have the status value 0xF0. If this message contains
all the system exclusive data for the message, it should end with the status
byte 0xF7 (EOX). Otherwise, additional system exclusive data should be sent
in one or more

SysexMessages

with a status value of 0xF7. The

SysexMessage

containing the last of the data for the system exclusive
message should end with the value 0xF7 (EOX) to mark the end of the system
exclusive message.

If system exclusive data from

SysexMessages

objects is being
transmitted using MIDI wire protocol, only the initial 0xF0 status byte, the
system exclusive data itself, and the final 0xF7 (EOX) byte should be
propagated; any 0xF7 status bytes used to indicate that a

SysexMessage

contains continuing system exclusive data should not be
propagated via MIDI wire protocol.

**All Implemented Interfaces:** Cloneable

---

### Field Details

#### public static final int SYSTEM_EXCLUSIVE

Status byte for System Exclusive message (0xF0, or 240).

**See Also:**
- MidiMessage.getStatus()

,

Constant Field Values

---

#### public static final int SPECIAL_SYSTEM_EXCLUSIVE

Status byte for Special System Exclusive message (0xF7, or 247), which is
used in MIDI files. It has the same value as END_OF_EXCLUSIVE, which is
used in the real-time "MIDI wire" protocol.

**See Also:**
- MidiMessage.getStatus()

,

Constant Field Values

---

### Constructor Details

#### public SysexMessage()

Constructs a new

SysexMessage

. The contents of the new message
are guaranteed to specify a valid MIDI message. Subsequently, you may set
the contents of the message using one of the

setMessage

methods.

**See Also:**
- setMessage(byte[], int)

---

#### public SysexMessage​(byte[] data,
int length)
throws
InvalidMidiDataException

Constructs a new

SysexMessage

and sets the data for the message.
The first byte of the data array must be a valid system exclusive status
byte (0xF0 or 0xF7). The contents of the message can be changed by using
one of the

setMessage

methods.

**Parameters:**
- data

- the system exclusive message data including the status byte
- length

- the length of the valid message data in the array,
including the status byte; it should be non-negative and less
than or equal to

data.length

**Throws:**
- InvalidMidiDataException

- if the parameter values do not specify a
valid MIDI meta message

**See Also:**
- setMessage(byte[], int)

,

setMessage(int, byte[], int)

,

getData()

**Since:**
- 1.7

---

#### public SysexMessage​(int status,
byte[] data,
int length)
throws
InvalidMidiDataException

Constructs a new

SysexMessage

and sets the data for the message.
The contents of the message can be changed by using one of the

setMessage

methods.

**Parameters:**
- status

- the status byte for the message; it must be a valid system
exclusive status byte (0xF0 or 0xF7)
- data

- the system exclusive message data (without the status byte)
- length

- the length of the valid message data in the array; it
should be non-negative and less than or equal to

data.length

**Throws:**
- InvalidMidiDataException

- if the parameter values do not specify a
valid MIDI system exclusive message

**See Also:**
- setMessage(byte[], int)

,

setMessage(int, byte[], int)

,

getData()

**Since:**
- 1.7

---

#### protected SysexMessage​(byte[] data)

Constructs a new

SysexMessage

.

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

#### public void setMessage​(byte[] data,
int length)
throws
InvalidMidiDataException

Sets the data for the system exclusive message. The first byte of the
data array must be a valid system exclusive status byte (0xF0 or 0xF7).

**Overrides:**
- setMessage

in class

MidiMessage

**Parameters:**
- data

- the system exclusive message data
- length

- the length of the valid message data in the array,
including the status byte

**Throws:**
- InvalidMidiDataException

- if the parameter values do not specify a
valid MIDI system exclusive message

---

#### public void setMessage​(int status,
byte[] data,
int length)
throws
InvalidMidiDataException

Sets the data for the system exclusive message.

**Parameters:**
- status

- the status byte for the message (0xF0 or 0xF7)
- data

- the system exclusive message data
- length

- the length of the valid message data in the array

**Throws:**
- InvalidMidiDataException

- if the status byte is invalid for a
system exclusive message

---

#### public byte[] getData()

Obtains a copy of the data for the system exclusive message. The returned
array of bytes does not include the status byte.

**Returns:**
- array containing the system exclusive message data

---

#### public
Object
clone()

Creates a new object of the same class and with the same contents as this
object.

**Specified by:**
- clone

in class

MidiMessage

**Returns:**
- a clone of this instance

**See Also:**
- Cloneable

---

### Additional Sections

#### Class SysexMessage

java.lang.Object

- javax.sound.midi.MidiMessage
- - javax.sound.midi.SysexMessage

javax.sound.midi.MidiMessage

- javax.sound.midi.SysexMessage

javax.sound.midi.SysexMessage

**All Implemented Interfaces:** Cloneable

```java
public class
SysexMessage

extends
MidiMessage
```

A

SysexMessage

object represents a MIDI system exclusive message.

When a system exclusive message is read from a MIDI file, it always has a
defined length. Data from a system exclusive message from a MIDI file should
be stored in the data array of a

SysexMessage

as follows: the system
exclusive message status byte (0xF0 or 0xF7), all message data bytes, and
finally the end-of-exclusive flag (0xF7). The length reported by the

SysexMessage

object is therefore the length of the system exclusive
data plus two: one byte for the status byte and one for the end-of-exclusive
flag.

As dictated by the Standard MIDI Files specification, two status byte values
are legal for a

SysexMessage

read from a MIDI file:

- 0xF0: System Exclusive message (same as in MIDI wire protocol)

0xF7: Special System Exclusive message

When Java Sound is used to handle system exclusive data that is being
received using MIDI wire protocol, it should place the data in one or more

SysexMessages

. In this case, the length of the system exclusive data
is not known in advance; the end of the system exclusive data is marked by an
end-of-exclusive flag (0xF7) in the MIDI wire byte stream.

- 0xF0: System Exclusive message (same as in MIDI wire protocol)

0xF7: End of Exclusive (EOX)

The first

SysexMessage

object containing data for a particular system
exclusive message should have the status value 0xF0. If this message contains
all the system exclusive data for the message, it should end with the status
byte 0xF7 (EOX). Otherwise, additional system exclusive data should be sent
in one or more

SysexMessages

with a status value of 0xF7. The

SysexMessage

containing the last of the data for the system exclusive
message should end with the value 0xF7 (EOX) to mark the end of the system
exclusive message.

If system exclusive data from

SysexMessages

objects is being
transmitted using MIDI wire protocol, only the initial 0xF0 status byte, the
system exclusive data itself, and the final 0xF7 (EOX) byte should be
propagated; any 0xF7 status bytes used to indicate that a

SysexMessage

contains continuing system exclusive data should not be
propagated via MIDI wire protocol.

public class

SysexMessage

extends

MidiMessage

A

SysexMessage

object represents a MIDI system exclusive message.

When a system exclusive message is read from a MIDI file, it always has a
defined length. Data from a system exclusive message from a MIDI file should
be stored in the data array of a

SysexMessage

as follows: the system
exclusive message status byte (0xF0 or 0xF7), all message data bytes, and
finally the end-of-exclusive flag (0xF7). The length reported by the

SysexMessage

object is therefore the length of the system exclusive
data plus two: one byte for the status byte and one for the end-of-exclusive
flag.

As dictated by the Standard MIDI Files specification, two status byte values
are legal for a

SysexMessage

read from a MIDI file:

- 0xF0: System Exclusive message (same as in MIDI wire protocol)

0xF7: Special System Exclusive message

When Java Sound is used to handle system exclusive data that is being
received using MIDI wire protocol, it should place the data in one or more

SysexMessages

. In this case, the length of the system exclusive data
is not known in advance; the end of the system exclusive data is marked by an
end-of-exclusive flag (0xF7) in the MIDI wire byte stream.

- 0xF0: System Exclusive message (same as in MIDI wire protocol)

0xF7: End of Exclusive (EOX)

The first

SysexMessage

object containing data for a particular system
exclusive message should have the status value 0xF0. If this message contains
all the system exclusive data for the message, it should end with the status
byte 0xF7 (EOX). Otherwise, additional system exclusive data should be sent
in one or more

SysexMessages

with a status value of 0xF7. The

SysexMessage

containing the last of the data for the system exclusive
message should end with the value 0xF7 (EOX) to mark the end of the system
exclusive message.

If system exclusive data from

SysexMessages

objects is being
transmitted using MIDI wire protocol, only the initial 0xF0 status byte, the
system exclusive data itself, and the final 0xF7 (EOX) byte should be
propagated; any 0xF7 status bytes used to indicate that a

SysexMessage

contains continuing system exclusive data should not be
propagated via MIDI wire protocol.

When a system exclusive message is read from a MIDI file, it always has a
defined length. Data from a system exclusive message from a MIDI file should
be stored in the data array of a

SysexMessage

as follows: the system
exclusive message status byte (0xF0 or 0xF7), all message data bytes, and
finally the end-of-exclusive flag (0xF7). The length reported by the

SysexMessage

object is therefore the length of the system exclusive
data plus two: one byte for the status byte and one for the end-of-exclusive
flag.

As dictated by the Standard MIDI Files specification, two status byte values
are legal for a

SysexMessage

read from a MIDI file:

- 0xF0: System Exclusive message (same as in MIDI wire protocol)

0xF7: Special System Exclusive message

When Java Sound is used to handle system exclusive data that is being
received using MIDI wire protocol, it should place the data in one or more

SysexMessages

. In this case, the length of the system exclusive data
is not known in advance; the end of the system exclusive data is marked by an
end-of-exclusive flag (0xF7) in the MIDI wire byte stream.

- 0xF0: System Exclusive message (same as in MIDI wire protocol)

0xF7: End of Exclusive (EOX)

The first

SysexMessage

object containing data for a particular system
exclusive message should have the status value 0xF0. If this message contains
all the system exclusive data for the message, it should end with the status
byte 0xF7 (EOX). Otherwise, additional system exclusive data should be sent
in one or more

SysexMessages

with a status value of 0xF7. The

SysexMessage

containing the last of the data for the system exclusive
message should end with the value 0xF7 (EOX) to mark the end of the system
exclusive message.

If system exclusive data from

SysexMessages

objects is being
transmitted using MIDI wire protocol, only the initial 0xF0 status byte, the
system exclusive data itself, and the final 0xF7 (EOX) byte should be
propagated; any 0xF7 status bytes used to indicate that a

SysexMessage

contains continuing system exclusive data should not be
propagated via MIDI wire protocol.

As dictated by the Standard MIDI Files specification, two status byte values
are legal for a

SysexMessage

read from a MIDI file:

- 0xF0: System Exclusive message (same as in MIDI wire protocol)

0xF7: Special System Exclusive message

When Java Sound is used to handle system exclusive data that is being
received using MIDI wire protocol, it should place the data in one or more

SysexMessages

. In this case, the length of the system exclusive data
is not known in advance; the end of the system exclusive data is marked by an
end-of-exclusive flag (0xF7) in the MIDI wire byte stream.

- 0xF0: System Exclusive message (same as in MIDI wire protocol)

0xF7: End of Exclusive (EOX)

The first

SysexMessage

object containing data for a particular system
exclusive message should have the status value 0xF0. If this message contains
all the system exclusive data for the message, it should end with the status
byte 0xF7 (EOX). Otherwise, additional system exclusive data should be sent
in one or more

SysexMessages

with a status value of 0xF7. The

SysexMessage

containing the last of the data for the system exclusive
message should end with the value 0xF7 (EOX) to mark the end of the system
exclusive message.

If system exclusive data from

SysexMessages

objects is being
transmitted using MIDI wire protocol, only the initial 0xF0 status byte, the
system exclusive data itself, and the final 0xF7 (EOX) byte should be
propagated; any 0xF7 status bytes used to indicate that a

SysexMessage

contains continuing system exclusive data should not be
propagated via MIDI wire protocol.

0xF0: System Exclusive message (same as in MIDI wire protocol)

0xF7: Special System Exclusive message

0xF0: System Exclusive message (same as in MIDI wire protocol)

0xF7: End of Exclusive (EOX)

If system exclusive data from

SysexMessages

objects is being
transmitted using MIDI wire protocol, only the initial 0xF0 status byte, the
system exclusive data itself, and the final 0xF7 (EOX) byte should be
propagated; any 0xF7 status bytes used to indicate that a

SysexMessage

contains continuing system exclusive data should not be
propagated via MIDI wire protocol.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static int

SPECIAL_SYSTEM_EXCLUSIVE

Status byte for Special System Exclusive message (0xF7, or 247), which is
used in MIDI files.

static int

SYSTEM_EXCLUSIVE

Status byte for System Exclusive message (0xF0, or 240).

- Fields declared in class javax.sound.midi.

MidiMessage

data

,

length

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

SysexMessage

()

Constructs a new

SysexMessage

.

protected

SysexMessage

​(byte[] data)

Constructs a new

SysexMessage

.

SysexMessage

​(byte[] data,
int length)

Constructs a new

SysexMessage

and sets the data for the message.

SysexMessage

​(int status,
byte[] data,
int length)

Constructs a new

SysexMessage

and sets the data for the message.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Object

clone

()

Creates a new object of the same class and with the same contents as this
object.

byte[]

getData

()

Obtains a copy of the data for the system exclusive message.

void

setMessage

​(byte[] data,
int length)

Sets the data for the system exclusive message.

void

setMessage

​(int status,
byte[] data,
int length)

Sets the data for the system exclusive message.

- Methods declared in class javax.sound.midi.

MidiMessage

getLength

,

getMessage

,

getStatus

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

static int

SPECIAL_SYSTEM_EXCLUSIVE

Status byte for Special System Exclusive message (0xF7, or 247), which is
used in MIDI files.

static int

SYSTEM_EXCLUSIVE

Status byte for System Exclusive message (0xF0, or 240).

- Fields declared in class javax.sound.midi.

MidiMessage

data

,

length

---

#### Field Summary

Status byte for Special System Exclusive message (0xF7, or 247), which is
used in MIDI files.

Status byte for System Exclusive message (0xF0, or 240).

Fields declared in class javax.sound.midi.

MidiMessage

data

,

length

---

#### Fields declared in class javax.sound.midi. MidiMessage

Constructor Summary

Constructors

Modifier

Constructor

Description

SysexMessage

()

Constructs a new

SysexMessage

.

protected

SysexMessage

​(byte[] data)

Constructs a new

SysexMessage

.

SysexMessage

​(byte[] data,
int length)

Constructs a new

SysexMessage

and sets the data for the message.

SysexMessage

​(int status,
byte[] data,
int length)

Constructs a new

SysexMessage

and sets the data for the message.

---

#### Constructor Summary

Constructs a new

SysexMessage

.

Constructs a new

SysexMessage

and sets the data for the message.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Object

clone

()

Creates a new object of the same class and with the same contents as this
object.

byte[]

getData

()

Obtains a copy of the data for the system exclusive message.

void

setMessage

​(byte[] data,
int length)

Sets the data for the system exclusive message.

void

setMessage

​(int status,
byte[] data,
int length)

Sets the data for the system exclusive message.

- Methods declared in class javax.sound.midi.

MidiMessage

getLength

,

getMessage

,

getStatus

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

Obtains a copy of the data for the system exclusive message.

Sets the data for the system exclusive message.

Methods declared in class javax.sound.midi.

MidiMessage

getLength

,

getMessage

,

getStatus

---

#### Methods declared in class javax.sound.midi. MidiMessage

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

- SYSTEM_EXCLUSIVE

```java
public static final int SYSTEM_EXCLUSIVE
```

Status byte for System Exclusive message (0xF0, or 240).

**See Also:** MidiMessage.getStatus()

,

Constant Field Values

- SPECIAL_SYSTEM_EXCLUSIVE

```java
public static final int SPECIAL_SYSTEM_EXCLUSIVE
```

Status byte for Special System Exclusive message (0xF7, or 247), which is
used in MIDI files. It has the same value as END_OF_EXCLUSIVE, which is
used in the real-time "MIDI wire" protocol.

**See Also:** MidiMessage.getStatus()

,

Constant Field Values

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- SysexMessage

```java
public SysexMessage()
```

Constructs a new

SysexMessage

. The contents of the new message
are guaranteed to specify a valid MIDI message. Subsequently, you may set
the contents of the message using one of the

setMessage

methods.

**See Also:** setMessage(byte[], int)

- SysexMessage

```java
public SysexMessage​(byte[] data,
int length)
throws
InvalidMidiDataException
```

Constructs a new

SysexMessage

and sets the data for the message.
The first byte of the data array must be a valid system exclusive status
byte (0xF0 or 0xF7). The contents of the message can be changed by using
one of the

setMessage

methods.

**Parameters:** data

- the system exclusive message data including the status byte
**Parameters:** length

- the length of the valid message data in the array,
including the status byte; it should be non-negative and less
than or equal to

data.length
**Throws:** InvalidMidiDataException

- if the parameter values do not specify a
valid MIDI meta message
**Since:** 1.7
**See Also:** setMessage(byte[], int)

,

setMessage(int, byte[], int)

,

getData()

- SysexMessage

```java
public SysexMessage​(int status,
byte[] data,
int length)
throws
InvalidMidiDataException
```

Constructs a new

SysexMessage

and sets the data for the message.
The contents of the message can be changed by using one of the

setMessage

methods.

**Parameters:** status

- the status byte for the message; it must be a valid system
exclusive status byte (0xF0 or 0xF7)
**Parameters:** data

- the system exclusive message data (without the status byte)
**Parameters:** length

- the length of the valid message data in the array; it
should be non-negative and less than or equal to

data.length
**Throws:** InvalidMidiDataException

- if the parameter values do not specify a
valid MIDI system exclusive message
**Since:** 1.7
**See Also:** setMessage(byte[], int)

,

setMessage(int, byte[], int)

,

getData()

- SysexMessage

```java
protected SysexMessage​(byte[] data)
```

Constructs a new

SysexMessage

.

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
public void setMessage​(byte[] data,
int length)
throws
InvalidMidiDataException
```

Sets the data for the system exclusive message. The first byte of the
data array must be a valid system exclusive status byte (0xF0 or 0xF7).

**Overrides:** setMessage

in class

MidiMessage
**Parameters:** data

- the system exclusive message data
**Parameters:** length

- the length of the valid message data in the array,
including the status byte
**Throws:** InvalidMidiDataException

- if the parameter values do not specify a
valid MIDI system exclusive message

- setMessage

```java
public void setMessage​(int status,
byte[] data,
int length)
throws
InvalidMidiDataException
```

Sets the data for the system exclusive message.

**Parameters:** status

- the status byte for the message (0xF0 or 0xF7)
**Parameters:** data

- the system exclusive message data
**Parameters:** length

- the length of the valid message data in the array
**Throws:** InvalidMidiDataException

- if the status byte is invalid for a
system exclusive message

- getData

```java
public byte[] getData()
```

Obtains a copy of the data for the system exclusive message. The returned
array of bytes does not include the status byte.

**Returns:** array containing the system exclusive message data

- clone

```java
public
Object
clone()
```

Creates a new object of the same class and with the same contents as this
object.

**Specified by:** clone

in class

MidiMessage
**Returns:** a clone of this instance
**See Also:** Cloneable

Field Detail

- SYSTEM_EXCLUSIVE

```java
public static final int SYSTEM_EXCLUSIVE
```

Status byte for System Exclusive message (0xF0, or 240).

**See Also:** MidiMessage.getStatus()

,

Constant Field Values

- SPECIAL_SYSTEM_EXCLUSIVE

```java
public static final int SPECIAL_SYSTEM_EXCLUSIVE
```

Status byte for Special System Exclusive message (0xF7, or 247), which is
used in MIDI files. It has the same value as END_OF_EXCLUSIVE, which is
used in the real-time "MIDI wire" protocol.

**See Also:** MidiMessage.getStatus()

,

Constant Field Values

---

#### Field Detail

SYSTEM_EXCLUSIVE

```java
public static final int SYSTEM_EXCLUSIVE
```

Status byte for System Exclusive message (0xF0, or 240).

**See Also:** MidiMessage.getStatus()

,

Constant Field Values

---

#### SYSTEM_EXCLUSIVE

public static final int SYSTEM_EXCLUSIVE

Status byte for System Exclusive message (0xF0, or 240).

SPECIAL_SYSTEM_EXCLUSIVE

```java
public static final int SPECIAL_SYSTEM_EXCLUSIVE
```

Status byte for Special System Exclusive message (0xF7, or 247), which is
used in MIDI files. It has the same value as END_OF_EXCLUSIVE, which is
used in the real-time "MIDI wire" protocol.

**See Also:** MidiMessage.getStatus()

,

Constant Field Values

---

#### SPECIAL_SYSTEM_EXCLUSIVE

public static final int SPECIAL_SYSTEM_EXCLUSIVE

Status byte for Special System Exclusive message (0xF7, or 247), which is
used in MIDI files. It has the same value as END_OF_EXCLUSIVE, which is
used in the real-time "MIDI wire" protocol.

Constructor Detail

- SysexMessage

```java
public SysexMessage()
```

Constructs a new

SysexMessage

. The contents of the new message
are guaranteed to specify a valid MIDI message. Subsequently, you may set
the contents of the message using one of the

setMessage

methods.

**See Also:** setMessage(byte[], int)

- SysexMessage

```java
public SysexMessage​(byte[] data,
int length)
throws
InvalidMidiDataException
```

Constructs a new

SysexMessage

and sets the data for the message.
The first byte of the data array must be a valid system exclusive status
byte (0xF0 or 0xF7). The contents of the message can be changed by using
one of the

setMessage

methods.

**Parameters:** data

- the system exclusive message data including the status byte
**Parameters:** length

- the length of the valid message data in the array,
including the status byte; it should be non-negative and less
than or equal to

data.length
**Throws:** InvalidMidiDataException

- if the parameter values do not specify a
valid MIDI meta message
**Since:** 1.7
**See Also:** setMessage(byte[], int)

,

setMessage(int, byte[], int)

,

getData()

- SysexMessage

```java
public SysexMessage​(int status,
byte[] data,
int length)
throws
InvalidMidiDataException
```

Constructs a new

SysexMessage

and sets the data for the message.
The contents of the message can be changed by using one of the

setMessage

methods.

**Parameters:** status

- the status byte for the message; it must be a valid system
exclusive status byte (0xF0 or 0xF7)
**Parameters:** data

- the system exclusive message data (without the status byte)
**Parameters:** length

- the length of the valid message data in the array; it
should be non-negative and less than or equal to

data.length
**Throws:** InvalidMidiDataException

- if the parameter values do not specify a
valid MIDI system exclusive message
**Since:** 1.7
**See Also:** setMessage(byte[], int)

,

setMessage(int, byte[], int)

,

getData()

- SysexMessage

```java
protected SysexMessage​(byte[] data)
```

Constructs a new

SysexMessage

.

**Parameters:** data

- an array of bytes containing the complete message. The
message data may be changed using the

setMessage

method.
**See Also:** setMessage(byte[], int)

---

#### Constructor Detail

SysexMessage

```java
public SysexMessage()
```

Constructs a new

SysexMessage

. The contents of the new message
are guaranteed to specify a valid MIDI message. Subsequently, you may set
the contents of the message using one of the

setMessage

methods.

**See Also:** setMessage(byte[], int)

---

#### SysexMessage

public SysexMessage()

Constructs a new

SysexMessage

. The contents of the new message
are guaranteed to specify a valid MIDI message. Subsequently, you may set
the contents of the message using one of the

setMessage

methods.

SysexMessage

```java
public SysexMessage​(byte[] data,
int length)
throws
InvalidMidiDataException
```

Constructs a new

SysexMessage

and sets the data for the message.
The first byte of the data array must be a valid system exclusive status
byte (0xF0 or 0xF7). The contents of the message can be changed by using
one of the

setMessage

methods.

**Parameters:** data

- the system exclusive message data including the status byte
**Parameters:** length

- the length of the valid message data in the array,
including the status byte; it should be non-negative and less
than or equal to

data.length
**Throws:** InvalidMidiDataException

- if the parameter values do not specify a
valid MIDI meta message
**Since:** 1.7
**See Also:** setMessage(byte[], int)

,

setMessage(int, byte[], int)

,

getData()

---

#### SysexMessage

public SysexMessage​(byte[] data,
int length)
throws

InvalidMidiDataException

Constructs a new

SysexMessage

and sets the data for the message.
The first byte of the data array must be a valid system exclusive status
byte (0xF0 or 0xF7). The contents of the message can be changed by using
one of the

setMessage

methods.

SysexMessage

```java
public SysexMessage​(int status,
byte[] data,
int length)
throws
InvalidMidiDataException
```

Constructs a new

SysexMessage

and sets the data for the message.
The contents of the message can be changed by using one of the

setMessage

methods.

**Parameters:** status

- the status byte for the message; it must be a valid system
exclusive status byte (0xF0 or 0xF7)
**Parameters:** data

- the system exclusive message data (without the status byte)
**Parameters:** length

- the length of the valid message data in the array; it
should be non-negative and less than or equal to

data.length
**Throws:** InvalidMidiDataException

- if the parameter values do not specify a
valid MIDI system exclusive message
**Since:** 1.7
**See Also:** setMessage(byte[], int)

,

setMessage(int, byte[], int)

,

getData()

---

#### SysexMessage

public SysexMessage​(int status,
byte[] data,
int length)
throws

InvalidMidiDataException

Constructs a new

SysexMessage

and sets the data for the message.
The contents of the message can be changed by using one of the

setMessage

methods.

SysexMessage

```java
protected SysexMessage​(byte[] data)
```

Constructs a new

SysexMessage

.

**Parameters:** data

- an array of bytes containing the complete message. The
message data may be changed using the

setMessage

method.
**See Also:** setMessage(byte[], int)

---

#### SysexMessage

protected SysexMessage​(byte[] data)

Constructs a new

SysexMessage

.

Method Detail

- setMessage

```java
public void setMessage​(byte[] data,
int length)
throws
InvalidMidiDataException
```

Sets the data for the system exclusive message. The first byte of the
data array must be a valid system exclusive status byte (0xF0 or 0xF7).

**Overrides:** setMessage

in class

MidiMessage
**Parameters:** data

- the system exclusive message data
**Parameters:** length

- the length of the valid message data in the array,
including the status byte
**Throws:** InvalidMidiDataException

- if the parameter values do not specify a
valid MIDI system exclusive message

- setMessage

```java
public void setMessage​(int status,
byte[] data,
int length)
throws
InvalidMidiDataException
```

Sets the data for the system exclusive message.

**Parameters:** status

- the status byte for the message (0xF0 or 0xF7)
**Parameters:** data

- the system exclusive message data
**Parameters:** length

- the length of the valid message data in the array
**Throws:** InvalidMidiDataException

- if the status byte is invalid for a
system exclusive message

- getData

```java
public byte[] getData()
```

Obtains a copy of the data for the system exclusive message. The returned
array of bytes does not include the status byte.

**Returns:** array containing the system exclusive message data

- clone

```java
public
Object
clone()
```

Creates a new object of the same class and with the same contents as this
object.

**Specified by:** clone

in class

MidiMessage
**Returns:** a clone of this instance
**See Also:** Cloneable

---

#### Method Detail

setMessage

```java
public void setMessage​(byte[] data,
int length)
throws
InvalidMidiDataException
```

Sets the data for the system exclusive message. The first byte of the
data array must be a valid system exclusive status byte (0xF0 or 0xF7).

**Overrides:** setMessage

in class

MidiMessage
**Parameters:** data

- the system exclusive message data
**Parameters:** length

- the length of the valid message data in the array,
including the status byte
**Throws:** InvalidMidiDataException

- if the parameter values do not specify a
valid MIDI system exclusive message

---

#### setMessage

public void setMessage​(byte[] data,
int length)
throws

InvalidMidiDataException

Sets the data for the system exclusive message. The first byte of the
data array must be a valid system exclusive status byte (0xF0 or 0xF7).

setMessage

```java
public void setMessage​(int status,
byte[] data,
int length)
throws
InvalidMidiDataException
```

Sets the data for the system exclusive message.

**Parameters:** status

- the status byte for the message (0xF0 or 0xF7)
**Parameters:** data

- the system exclusive message data
**Parameters:** length

- the length of the valid message data in the array
**Throws:** InvalidMidiDataException

- if the status byte is invalid for a
system exclusive message

---

#### setMessage

public void setMessage​(int status,
byte[] data,
int length)
throws

InvalidMidiDataException

Sets the data for the system exclusive message.

getData

```java
public byte[] getData()
```

Obtains a copy of the data for the system exclusive message. The returned
array of bytes does not include the status byte.

**Returns:** array containing the system exclusive message data

---

#### getData

public byte[] getData()

Obtains a copy of the data for the system exclusive message. The returned
array of bytes does not include the status byte.

clone

```java
public
Object
clone()
```

Creates a new object of the same class and with the same contents as this
object.

**Specified by:** clone

in class

MidiMessage
**Returns:** a clone of this instance
**See Also:** Cloneable

---

#### clone

public

Object

clone()

Creates a new object of the same class and with the same contents as this
object.

---

