# Class ShortMessage

**Source:** `java.desktop\javax\sound\midi\ShortMessage.html`

### Class Description

```java
public class
ShortMessage

extends
MidiMessage
```

A

ShortMessage

contains a MIDI message that has at most two data
bytes following its status byte. The types of MIDI message that satisfy this
criterion are channel voice, channel mode, system common, and system
real-time--in other words, everything except system exclusive and
meta-events. The

ShortMessage

class provides methods for getting and
setting the contents of the MIDI message.

A number of

ShortMessage

methods have integer parameters by which you
specify a MIDI status or data byte. If you know the numeric value, you can
express it directly. For system common and system real-time messages, you can
often use the corresponding fields of

ShortMessage

, such as

SYSTEM_RESET

. For channel messages, the upper four bits
of the status byte are specified by a command value and the lower four bits
are specified by a MIDI channel number. To convert incoming MIDI data bytes
that are in the form of Java's signed bytes, you can use the

conversion code

given in the

MidiMessage

class description.

**All Implemented Interfaces:** Cloneable

---

### Field Details

#### public static final int MIDI_TIME_CODE

Status byte for MIDI Time Code Quarter Frame message (0xF1, or 241).

**See Also:**
- MidiMessage.getStatus()

,

Constant Field Values

---

#### public static final int SONG_POSITION_POINTER

Status byte for Song Position Pointer message (0xF2, or 242).

**See Also:**
- MidiMessage.getStatus()

,

Constant Field Values

---

#### public static final int SONG_SELECT

Status byte for MIDI Song Select message (0xF3, or 243).

**See Also:**
- MidiMessage.getStatus()

,

Constant Field Values

---

#### public static final int TUNE_REQUEST

Status byte for Tune Request message (0xF6, or 246).

**See Also:**
- MidiMessage.getStatus()

,

Constant Field Values

---

#### public static final int END_OF_EXCLUSIVE

Status byte for End of System Exclusive message (0xF7, or 247).

**See Also:**
- MidiMessage.getStatus()

,

Constant Field Values

---

#### public static final int TIMING_CLOCK

Status byte for Timing Clock message (0xF8, or 248).

**See Also:**
- MidiMessage.getStatus()

,

Constant Field Values

---

#### public static final int START

Status byte for Start message (0xFA, or 250).

**See Also:**
- MidiMessage.getStatus()

,

Constant Field Values

---

#### public static final int CONTINUE

Status byte for Continue message (0xFB, or 251).

**See Also:**
- MidiMessage.getStatus()

,

Constant Field Values

---

#### public static final int STOP

Status byte for Stop message (0xFC, or 252).

**See Also:**
- MidiMessage.getStatus()

,

Constant Field Values

---

#### public static final int ACTIVE_SENSING

Status byte for Active Sensing message (0xFE, or 254).

**See Also:**
- MidiMessage.getStatus()

,

Constant Field Values

---

#### public static final int SYSTEM_RESET

Status byte for System Reset message (0xFF, or 255).

**See Also:**
- MidiMessage.getStatus()

,

Constant Field Values

---

#### public static final int NOTE_OFF

Command value for Note Off message (0x80, or 128).

**See Also:**
- Constant Field Values

---

#### public static final int NOTE_ON

Command value for Note On message (0x90, or 144).

**See Also:**
- Constant Field Values

---

#### public static final int POLY_PRESSURE

Command value for Polyphonic Key Pressure (Aftertouch) message (0xA0, or
160).

**See Also:**
- Constant Field Values

---

#### public static final int CONTROL_CHANGE

Command value for Control Change message (0xB0, or 176).

**See Also:**
- Constant Field Values

---

#### public static final int PROGRAM_CHANGE

Command value for Program Change message (0xC0, or 192).

**See Also:**
- Constant Field Values

---

#### public static final int CHANNEL_PRESSURE

Command value for Channel Pressure (Aftertouch) message (0xD0, or 208).

**See Also:**
- Constant Field Values

---

#### public static final int PITCH_BEND

Command value for Pitch Bend message (0xE0, or 224).

**See Also:**
- Constant Field Values

---

### Constructor Details

#### public ShortMessage()

Constructs a new

ShortMessage

. The contents of the new message
are guaranteed to specify a valid MIDI message. Subsequently, you may set
the contents of the message using one of the

setMessage

methods.

**See Also:**
- setMessage(int)

---

#### public ShortMessage​(int status)
throws
InvalidMidiDataException

Constructs a new

ShortMessage

which represents a MIDI message
that takes no data bytes. The contents of the message can be changed by
using one of the

setMessage

methods.

**Parameters:**
- status

- the MIDI status byte

**Throws:**
- InvalidMidiDataException

- if

status

does not specify a
valid MIDI status byte for a message that requires no data bytes

**See Also:**
- setMessage(int)

,

setMessage(int, int, int)

,

setMessage(int, int, int, int)

,

MidiMessage.getStatus()

**Since:**
- 1.7

---

#### public ShortMessage​(int status,
int data1,
int data2)
throws
InvalidMidiDataException

Constructs a new

ShortMessage

which represents a MIDI message
that takes up to two data bytes. If the message only takes one data byte,
the second data byte is ignored. If the message does not take any data
bytes, both data bytes are ignored. The contents of the message can be
changed by using one of the

setMessage

methods.

**Parameters:**
- status

- the MIDI status byte
- data1

- the first data byte
- data2

- the second data byte

**Throws:**
- InvalidMidiDataException

- if the status byte or all data bytes
belonging to the message do not specify a valid MIDI message

**See Also:**
- setMessage(int)

,

setMessage(int, int, int)

,

setMessage(int, int, int, int)

,

MidiMessage.getStatus()

,

getData1()

,

getData2()

**Since:**
- 1.7

---

#### public ShortMessage​(int command,
int channel,
int data1,
int data2)
throws
InvalidMidiDataException

Constructs a new

ShortMessage

which represents a channel MIDI
message that takes up to two data bytes. If the message only takes one
data byte, the second data byte is ignored. If the message does not take
any data bytes, both data bytes are ignored. The contents of the message
can be changed by using one of the

setMessage

methods.

**Parameters:**
- command

- the MIDI command represented by this message
- channel

- the channel associated with the message
- data1

- the first data byte
- data2

- the second data byte

**Throws:**
- InvalidMidiDataException

- if the command value, channel value or
all data bytes belonging to the message do not specify a valid
MIDI message

**See Also:**
- setMessage(int)

,

setMessage(int, int, int)

,

setMessage(int, int, int, int)

,

getCommand()

,

getChannel()

,

getData1()

,

getData2()

**Since:**
- 1.7

---

#### protected ShortMessage​(byte[] data)

Constructs a new

ShortMessage

.

**Parameters:**
- data

- an array of bytes containing the complete message. The
message data may be changed using the

setMessage

method.

**See Also:**
- setMessage(int)

---

### Method Details

#### public void setMessage​(int status)
throws
InvalidMidiDataException

Sets the parameters for a MIDI message that takes no data bytes.

**Parameters:**
- status

- the MIDI status byte

**Throws:**
- InvalidMidiDataException

- if

status

does not specify a
valid MIDI status byte for a message that requires no data bytes

**See Also:**
- setMessage(int, int, int)

,

setMessage(int, int, int, int)

---

#### public void setMessage​(int status,
int data1,
int data2)
throws
InvalidMidiDataException

Sets the parameters for a MIDI message that takes one or two data bytes.
If the message takes only one data byte, the second data byte is ignored;
if the message does not take any data bytes, both data bytes are ignored.

**Parameters:**
- status

- the MIDI status byte
- data1

- the first data byte
- data2

- the second data byte

**Throws:**
- InvalidMidiDataException

- if the status byte, or all data bytes
belonging to the message, do not specify a valid MIDI message

**See Also:**
- setMessage(int, int, int, int)

,

setMessage(int)

---

#### public void setMessage​(int command,
int channel,
int data1,
int data2)
throws
InvalidMidiDataException

Sets the short message parameters for a channel message which takes up to
two data bytes. If the message only takes one data byte, the second data
byte is ignored; if the message does not take any data bytes, both data
bytes are ignored.

**Parameters:**
- command

- the MIDI command represented by this message
- channel

- the channel associated with the message
- data1

- the first data byte
- data2

- the second data byte

**Throws:**
- InvalidMidiDataException

- if the status byte or all data bytes
belonging to the message, do not specify a valid MIDI message

**See Also:**
- setMessage(int, int, int)

,

setMessage(int)

,

getCommand()

,

getChannel()

,

getData1()

,

getData2()

---

#### public int getChannel()

Obtains the MIDI channel associated with this event. This method assumes
that the event is a MIDI channel message; if not, the return value will
not be meaningful.

**Returns:**
- MIDI channel associated with the message

**See Also:**
- setMessage(int, int, int, int)

---

#### public int getCommand()

Obtains the MIDI command associated with this event. This method assumes
that the event is a MIDI channel message; if not, the return value will
not be meaningful.

**Returns:**
- the MIDI command associated with this event

**See Also:**
- setMessage(int, int, int, int)

---

#### public int getData1()

Obtains the first data byte in the message.

**Returns:**
- the value of the

data1

field

**See Also:**
- setMessage(int, int, int)

---

#### public int getData2()

Obtains the second data byte in the message.

**Returns:**
- the value of the

data2

field

**See Also:**
- setMessage(int, int, int)

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

#### protected final int getDataLength​(int status)
throws
InvalidMidiDataException

Retrieves the number of data bytes associated with a particular status
byte value.

**Parameters:**
- status

- status byte value, which must represent a short MIDI
message

**Returns:**
- data length in bytes (0, 1, or 2)

**Throws:**
- InvalidMidiDataException

- if the

status

argument does not
represent the status byte for any short message

---

### Additional Sections

#### Class ShortMessage

java.lang.Object

- javax.sound.midi.MidiMessage
- - javax.sound.midi.ShortMessage

javax.sound.midi.MidiMessage

- javax.sound.midi.ShortMessage

javax.sound.midi.ShortMessage

**All Implemented Interfaces:** Cloneable

```java
public class
ShortMessage

extends
MidiMessage
```

A

ShortMessage

contains a MIDI message that has at most two data
bytes following its status byte. The types of MIDI message that satisfy this
criterion are channel voice, channel mode, system common, and system
real-time--in other words, everything except system exclusive and
meta-events. The

ShortMessage

class provides methods for getting and
setting the contents of the MIDI message.

A number of

ShortMessage

methods have integer parameters by which you
specify a MIDI status or data byte. If you know the numeric value, you can
express it directly. For system common and system real-time messages, you can
often use the corresponding fields of

ShortMessage

, such as

SYSTEM_RESET

. For channel messages, the upper four bits
of the status byte are specified by a command value and the lower four bits
are specified by a MIDI channel number. To convert incoming MIDI data bytes
that are in the form of Java's signed bytes, you can use the

conversion code

given in the

MidiMessage

class description.

**See Also:** SysexMessage

,

MetaMessage

public class

ShortMessage

extends

MidiMessage

A

ShortMessage

contains a MIDI message that has at most two data
bytes following its status byte. The types of MIDI message that satisfy this
criterion are channel voice, channel mode, system common, and system
real-time--in other words, everything except system exclusive and
meta-events. The

ShortMessage

class provides methods for getting and
setting the contents of the MIDI message.

A number of

ShortMessage

methods have integer parameters by which you
specify a MIDI status or data byte. If you know the numeric value, you can
express it directly. For system common and system real-time messages, you can
often use the corresponding fields of

ShortMessage

, such as

SYSTEM_RESET

. For channel messages, the upper four bits
of the status byte are specified by a command value and the lower four bits
are specified by a MIDI channel number. To convert incoming MIDI data bytes
that are in the form of Java's signed bytes, you can use the

conversion code

given in the

MidiMessage

class description.

A number of

ShortMessage

methods have integer parameters by which you
specify a MIDI status or data byte. If you know the numeric value, you can
express it directly. For system common and system real-time messages, you can
often use the corresponding fields of

ShortMessage

, such as

SYSTEM_RESET

. For channel messages, the upper four bits
of the status byte are specified by a command value and the lower four bits
are specified by a MIDI channel number. To convert incoming MIDI data bytes
that are in the form of Java's signed bytes, you can use the

conversion code

given in the

MidiMessage

class description.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static int

ACTIVE_SENSING

Status byte for Active Sensing message (0xFE, or 254).

static int

CHANNEL_PRESSURE

Command value for Channel Pressure (Aftertouch) message (0xD0, or 208).

static int

CONTINUE

Status byte for Continue message (0xFB, or 251).

static int

CONTROL_CHANGE

Command value for Control Change message (0xB0, or 176).

static int

END_OF_EXCLUSIVE

Status byte for End of System Exclusive message (0xF7, or 247).

static int

MIDI_TIME_CODE

Status byte for MIDI Time Code Quarter Frame message (0xF1, or 241).

static int

NOTE_OFF

Command value for Note Off message (0x80, or 128).

static int

NOTE_ON

Command value for Note On message (0x90, or 144).

static int

PITCH_BEND

Command value for Pitch Bend message (0xE0, or 224).

static int

POLY_PRESSURE

Command value for Polyphonic Key Pressure (Aftertouch) message (0xA0, or
160).

static int

PROGRAM_CHANGE

Command value for Program Change message (0xC0, or 192).

static int

SONG_POSITION_POINTER

Status byte for Song Position Pointer message (0xF2, or 242).

static int

SONG_SELECT

Status byte for MIDI Song Select message (0xF3, or 243).

static int

START

Status byte for Start message (0xFA, or 250).

static int

STOP

Status byte for Stop message (0xFC, or 252).

static int

SYSTEM_RESET

Status byte for System Reset message (0xFF, or 255).

static int

TIMING_CLOCK

Status byte for Timing Clock message (0xF8, or 248).

static int

TUNE_REQUEST

Status byte for Tune Request message (0xF6, or 246).

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

ShortMessage

()

Constructs a new

ShortMessage

.

protected

ShortMessage

​(byte[] data)

Constructs a new

ShortMessage

.

ShortMessage

​(int status)

Constructs a new

ShortMessage

which represents a MIDI message
that takes no data bytes.

ShortMessage

​(int status,
int data1,
int data2)

Constructs a new

ShortMessage

which represents a MIDI message
that takes up to two data bytes.

ShortMessage

​(int command,
int channel,
int data1,
int data2)

Constructs a new

ShortMessage

which represents a channel MIDI
message that takes up to two data bytes.

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

int

getChannel

()

Obtains the MIDI channel associated with this event.

int

getCommand

()

Obtains the MIDI command associated with this event.

int

getData1

()

Obtains the first data byte in the message.

int

getData2

()

Obtains the second data byte in the message.

protected int

getDataLength

​(int status)

Retrieves the number of data bytes associated with a particular status
byte value.

void

setMessage

​(int status)

Sets the parameters for a MIDI message that takes no data bytes.

void

setMessage

​(int status,
int data1,
int data2)

Sets the parameters for a MIDI message that takes one or two data bytes.

void

setMessage

​(int command,
int channel,
int data1,
int data2)

Sets the short message parameters for a channel message which takes up to
two data bytes.

- Methods declared in class javax.sound.midi.

MidiMessage

getLength

,

getMessage

,

getStatus

,

setMessage

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

ACTIVE_SENSING

Status byte for Active Sensing message (0xFE, or 254).

static int

CHANNEL_PRESSURE

Command value for Channel Pressure (Aftertouch) message (0xD0, or 208).

static int

CONTINUE

Status byte for Continue message (0xFB, or 251).

static int

CONTROL_CHANGE

Command value for Control Change message (0xB0, or 176).

static int

END_OF_EXCLUSIVE

Status byte for End of System Exclusive message (0xF7, or 247).

static int

MIDI_TIME_CODE

Status byte for MIDI Time Code Quarter Frame message (0xF1, or 241).

static int

NOTE_OFF

Command value for Note Off message (0x80, or 128).

static int

NOTE_ON

Command value for Note On message (0x90, or 144).

static int

PITCH_BEND

Command value for Pitch Bend message (0xE0, or 224).

static int

POLY_PRESSURE

Command value for Polyphonic Key Pressure (Aftertouch) message (0xA0, or
160).

static int

PROGRAM_CHANGE

Command value for Program Change message (0xC0, or 192).

static int

SONG_POSITION_POINTER

Status byte for Song Position Pointer message (0xF2, or 242).

static int

SONG_SELECT

Status byte for MIDI Song Select message (0xF3, or 243).

static int

START

Status byte for Start message (0xFA, or 250).

static int

STOP

Status byte for Stop message (0xFC, or 252).

static int

SYSTEM_RESET

Status byte for System Reset message (0xFF, or 255).

static int

TIMING_CLOCK

Status byte for Timing Clock message (0xF8, or 248).

static int

TUNE_REQUEST

Status byte for Tune Request message (0xF6, or 246).

- Fields declared in class javax.sound.midi.

MidiMessage

data

,

length

---

#### Field Summary

Status byte for Active Sensing message (0xFE, or 254).

Command value for Channel Pressure (Aftertouch) message (0xD0, or 208).

Status byte for Continue message (0xFB, or 251).

Command value for Control Change message (0xB0, or 176).

Status byte for End of System Exclusive message (0xF7, or 247).

Status byte for MIDI Time Code Quarter Frame message (0xF1, or 241).

Command value for Note Off message (0x80, or 128).

Command value for Note On message (0x90, or 144).

Command value for Pitch Bend message (0xE0, or 224).

Command value for Polyphonic Key Pressure (Aftertouch) message (0xA0, or
160).

Command value for Program Change message (0xC0, or 192).

Status byte for Song Position Pointer message (0xF2, or 242).

Status byte for MIDI Song Select message (0xF3, or 243).

Status byte for Start message (0xFA, or 250).

Status byte for Stop message (0xFC, or 252).

Status byte for System Reset message (0xFF, or 255).

Status byte for Timing Clock message (0xF8, or 248).

Status byte for Tune Request message (0xF6, or 246).

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

ShortMessage

()

Constructs a new

ShortMessage

.

protected

ShortMessage

​(byte[] data)

Constructs a new

ShortMessage

.

ShortMessage

​(int status)

Constructs a new

ShortMessage

which represents a MIDI message
that takes no data bytes.

ShortMessage

​(int status,
int data1,
int data2)

Constructs a new

ShortMessage

which represents a MIDI message
that takes up to two data bytes.

ShortMessage

​(int command,
int channel,
int data1,
int data2)

Constructs a new

ShortMessage

which represents a channel MIDI
message that takes up to two data bytes.

---

#### Constructor Summary

Constructs a new

ShortMessage

.

Constructs a new

ShortMessage

which represents a MIDI message
that takes no data bytes.

Constructs a new

ShortMessage

which represents a MIDI message
that takes up to two data bytes.

Constructs a new

ShortMessage

which represents a channel MIDI
message that takes up to two data bytes.

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

int

getChannel

()

Obtains the MIDI channel associated with this event.

int

getCommand

()

Obtains the MIDI command associated with this event.

int

getData1

()

Obtains the first data byte in the message.

int

getData2

()

Obtains the second data byte in the message.

protected int

getDataLength

​(int status)

Retrieves the number of data bytes associated with a particular status
byte value.

void

setMessage

​(int status)

Sets the parameters for a MIDI message that takes no data bytes.

void

setMessage

​(int status,
int data1,
int data2)

Sets the parameters for a MIDI message that takes one or two data bytes.

void

setMessage

​(int command,
int channel,
int data1,
int data2)

Sets the short message parameters for a channel message which takes up to
two data bytes.

- Methods declared in class javax.sound.midi.

MidiMessage

getLength

,

getMessage

,

getStatus

,

setMessage

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

Obtains the MIDI channel associated with this event.

Obtains the MIDI command associated with this event.

Obtains the first data byte in the message.

Obtains the second data byte in the message.

Retrieves the number of data bytes associated with a particular status
byte value.

Sets the parameters for a MIDI message that takes no data bytes.

Sets the parameters for a MIDI message that takes one or two data bytes.

Sets the short message parameters for a channel message which takes up to
two data bytes.

Methods declared in class javax.sound.midi.

MidiMessage

getLength

,

getMessage

,

getStatus

,

setMessage

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

- MIDI_TIME_CODE

```java
public static final int MIDI_TIME_CODE
```

Status byte for MIDI Time Code Quarter Frame message (0xF1, or 241).

**See Also:** MidiMessage.getStatus()

,

Constant Field Values

- SONG_POSITION_POINTER

```java
public static final int SONG_POSITION_POINTER
```

Status byte for Song Position Pointer message (0xF2, or 242).

**See Also:** MidiMessage.getStatus()

,

Constant Field Values

- SONG_SELECT

```java
public static final int SONG_SELECT
```

Status byte for MIDI Song Select message (0xF3, or 243).

**See Also:** MidiMessage.getStatus()

,

Constant Field Values

- TUNE_REQUEST

```java
public static final int TUNE_REQUEST
```

Status byte for Tune Request message (0xF6, or 246).

**See Also:** MidiMessage.getStatus()

,

Constant Field Values

- END_OF_EXCLUSIVE

```java
public static final int END_OF_EXCLUSIVE
```

Status byte for End of System Exclusive message (0xF7, or 247).

**See Also:** MidiMessage.getStatus()

,

Constant Field Values

- TIMING_CLOCK

```java
public static final int TIMING_CLOCK
```

Status byte for Timing Clock message (0xF8, or 248).

**See Also:** MidiMessage.getStatus()

,

Constant Field Values

- START

```java
public static final int START
```

Status byte for Start message (0xFA, or 250).

**See Also:** MidiMessage.getStatus()

,

Constant Field Values

- CONTINUE

```java
public static final int CONTINUE
```

Status byte for Continue message (0xFB, or 251).

**See Also:** MidiMessage.getStatus()

,

Constant Field Values

- STOP

```java
public static final int STOP
```

Status byte for Stop message (0xFC, or 252).

**See Also:** MidiMessage.getStatus()

,

Constant Field Values

- ACTIVE_SENSING

```java
public static final int ACTIVE_SENSING
```

Status byte for Active Sensing message (0xFE, or 254).

**See Also:** MidiMessage.getStatus()

,

Constant Field Values

- SYSTEM_RESET

```java
public static final int SYSTEM_RESET
```

Status byte for System Reset message (0xFF, or 255).

**See Also:** MidiMessage.getStatus()

,

Constant Field Values

- NOTE_OFF

```java
public static final int NOTE_OFF
```

Command value for Note Off message (0x80, or 128).

**See Also:** Constant Field Values

- NOTE_ON

```java
public static final int NOTE_ON
```

Command value for Note On message (0x90, or 144).

**See Also:** Constant Field Values

- POLY_PRESSURE

```java
public static final int POLY_PRESSURE
```

Command value for Polyphonic Key Pressure (Aftertouch) message (0xA0, or
160).

**See Also:** Constant Field Values

- CONTROL_CHANGE

```java
public static final int CONTROL_CHANGE
```

Command value for Control Change message (0xB0, or 176).

**See Also:** Constant Field Values

- PROGRAM_CHANGE

```java
public static final int PROGRAM_CHANGE
```

Command value for Program Change message (0xC0, or 192).

**See Also:** Constant Field Values

- CHANNEL_PRESSURE

```java
public static final int CHANNEL_PRESSURE
```

Command value for Channel Pressure (Aftertouch) message (0xD0, or 208).

**See Also:** Constant Field Values

- PITCH_BEND

```java
public static final int PITCH_BEND
```

Command value for Pitch Bend message (0xE0, or 224).

**See Also:** Constant Field Values

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- ShortMessage

```java
public ShortMessage()
```

Constructs a new

ShortMessage

. The contents of the new message
are guaranteed to specify a valid MIDI message. Subsequently, you may set
the contents of the message using one of the

setMessage

methods.

**See Also:** setMessage(int)

- ShortMessage

```java
public ShortMessage​(int status)
throws
InvalidMidiDataException
```

Constructs a new

ShortMessage

which represents a MIDI message
that takes no data bytes. The contents of the message can be changed by
using one of the

setMessage

methods.

**Parameters:** status

- the MIDI status byte
**Throws:** InvalidMidiDataException

- if

status

does not specify a
valid MIDI status byte for a message that requires no data bytes
**Since:** 1.7
**See Also:** setMessage(int)

,

setMessage(int, int, int)

,

setMessage(int, int, int, int)

,

MidiMessage.getStatus()

- ShortMessage

```java
public ShortMessage​(int status,
int data1,
int data2)
throws
InvalidMidiDataException
```

Constructs a new

ShortMessage

which represents a MIDI message
that takes up to two data bytes. If the message only takes one data byte,
the second data byte is ignored. If the message does not take any data
bytes, both data bytes are ignored. The contents of the message can be
changed by using one of the

setMessage

methods.

**Parameters:** status

- the MIDI status byte
**Parameters:** data1

- the first data byte
**Parameters:** data2

- the second data byte
**Throws:** InvalidMidiDataException

- if the status byte or all data bytes
belonging to the message do not specify a valid MIDI message
**Since:** 1.7
**See Also:** setMessage(int)

,

setMessage(int, int, int)

,

setMessage(int, int, int, int)

,

MidiMessage.getStatus()

,

getData1()

,

getData2()

- ShortMessage

```java
public ShortMessage​(int command,
int channel,
int data1,
int data2)
throws
InvalidMidiDataException
```

Constructs a new

ShortMessage

which represents a channel MIDI
message that takes up to two data bytes. If the message only takes one
data byte, the second data byte is ignored. If the message does not take
any data bytes, both data bytes are ignored. The contents of the message
can be changed by using one of the

setMessage

methods.

**Parameters:** command

- the MIDI command represented by this message
**Parameters:** channel

- the channel associated with the message
**Parameters:** data1

- the first data byte
**Parameters:** data2

- the second data byte
**Throws:** InvalidMidiDataException

- if the command value, channel value or
all data bytes belonging to the message do not specify a valid
MIDI message
**Since:** 1.7
**See Also:** setMessage(int)

,

setMessage(int, int, int)

,

setMessage(int, int, int, int)

,

getCommand()

,

getChannel()

,

getData1()

,

getData2()

- ShortMessage

```java
protected ShortMessage​(byte[] data)
```

Constructs a new

ShortMessage

.

**Parameters:** data

- an array of bytes containing the complete message. The
message data may be changed using the

setMessage

method.
**See Also:** setMessage(int)

============ METHOD DETAIL ==========

- Method Detail

- setMessage

```java
public void setMessage​(int status)
throws
InvalidMidiDataException
```

Sets the parameters for a MIDI message that takes no data bytes.

**Parameters:** status

- the MIDI status byte
**Throws:** InvalidMidiDataException

- if

status

does not specify a
valid MIDI status byte for a message that requires no data bytes
**See Also:** setMessage(int, int, int)

,

setMessage(int, int, int, int)

- setMessage

```java
public void setMessage​(int status,
int data1,
int data2)
throws
InvalidMidiDataException
```

Sets the parameters for a MIDI message that takes one or two data bytes.
If the message takes only one data byte, the second data byte is ignored;
if the message does not take any data bytes, both data bytes are ignored.

**Parameters:** status

- the MIDI status byte
**Parameters:** data1

- the first data byte
**Parameters:** data2

- the second data byte
**Throws:** InvalidMidiDataException

- if the status byte, or all data bytes
belonging to the message, do not specify a valid MIDI message
**See Also:** setMessage(int, int, int, int)

,

setMessage(int)

- setMessage

```java
public void setMessage​(int command,
int channel,
int data1,
int data2)
throws
InvalidMidiDataException
```

Sets the short message parameters for a channel message which takes up to
two data bytes. If the message only takes one data byte, the second data
byte is ignored; if the message does not take any data bytes, both data
bytes are ignored.

**Parameters:** command

- the MIDI command represented by this message
**Parameters:** channel

- the channel associated with the message
**Parameters:** data1

- the first data byte
**Parameters:** data2

- the second data byte
**Throws:** InvalidMidiDataException

- if the status byte or all data bytes
belonging to the message, do not specify a valid MIDI message
**See Also:** setMessage(int, int, int)

,

setMessage(int)

,

getCommand()

,

getChannel()

,

getData1()

,

getData2()

- getChannel

```java
public int getChannel()
```

Obtains the MIDI channel associated with this event. This method assumes
that the event is a MIDI channel message; if not, the return value will
not be meaningful.

**Returns:** MIDI channel associated with the message
**See Also:** setMessage(int, int, int, int)

- getCommand

```java
public int getCommand()
```

Obtains the MIDI command associated with this event. This method assumes
that the event is a MIDI channel message; if not, the return value will
not be meaningful.

**Returns:** the MIDI command associated with this event
**See Also:** setMessage(int, int, int, int)

- getData1

```java
public int getData1()
```

Obtains the first data byte in the message.

**Returns:** the value of the

data1

field
**See Also:** setMessage(int, int, int)

- getData2

```java
public int getData2()
```

Obtains the second data byte in the message.

**Returns:** the value of the

data2

field
**See Also:** setMessage(int, int, int)

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

- getDataLength

```java
protected final int getDataLength​(int status)
throws
InvalidMidiDataException
```

Retrieves the number of data bytes associated with a particular status
byte value.

**Parameters:** status

- status byte value, which must represent a short MIDI
message
**Returns:** data length in bytes (0, 1, or 2)
**Throws:** InvalidMidiDataException

- if the

status

argument does not
represent the status byte for any short message

Field Detail

- MIDI_TIME_CODE

```java
public static final int MIDI_TIME_CODE
```

Status byte for MIDI Time Code Quarter Frame message (0xF1, or 241).

**See Also:** MidiMessage.getStatus()

,

Constant Field Values

- SONG_POSITION_POINTER

```java
public static final int SONG_POSITION_POINTER
```

Status byte for Song Position Pointer message (0xF2, or 242).

**See Also:** MidiMessage.getStatus()

,

Constant Field Values

- SONG_SELECT

```java
public static final int SONG_SELECT
```

Status byte for MIDI Song Select message (0xF3, or 243).

**See Also:** MidiMessage.getStatus()

,

Constant Field Values

- TUNE_REQUEST

```java
public static final int TUNE_REQUEST
```

Status byte for Tune Request message (0xF6, or 246).

**See Also:** MidiMessage.getStatus()

,

Constant Field Values

- END_OF_EXCLUSIVE

```java
public static final int END_OF_EXCLUSIVE
```

Status byte for End of System Exclusive message (0xF7, or 247).

**See Also:** MidiMessage.getStatus()

,

Constant Field Values

- TIMING_CLOCK

```java
public static final int TIMING_CLOCK
```

Status byte for Timing Clock message (0xF8, or 248).

**See Also:** MidiMessage.getStatus()

,

Constant Field Values

- START

```java
public static final int START
```

Status byte for Start message (0xFA, or 250).

**See Also:** MidiMessage.getStatus()

,

Constant Field Values

- CONTINUE

```java
public static final int CONTINUE
```

Status byte for Continue message (0xFB, or 251).

**See Also:** MidiMessage.getStatus()

,

Constant Field Values

- STOP

```java
public static final int STOP
```

Status byte for Stop message (0xFC, or 252).

**See Also:** MidiMessage.getStatus()

,

Constant Field Values

- ACTIVE_SENSING

```java
public static final int ACTIVE_SENSING
```

Status byte for Active Sensing message (0xFE, or 254).

**See Also:** MidiMessage.getStatus()

,

Constant Field Values

- SYSTEM_RESET

```java
public static final int SYSTEM_RESET
```

Status byte for System Reset message (0xFF, or 255).

**See Also:** MidiMessage.getStatus()

,

Constant Field Values

- NOTE_OFF

```java
public static final int NOTE_OFF
```

Command value for Note Off message (0x80, or 128).

**See Also:** Constant Field Values

- NOTE_ON

```java
public static final int NOTE_ON
```

Command value for Note On message (0x90, or 144).

**See Also:** Constant Field Values

- POLY_PRESSURE

```java
public static final int POLY_PRESSURE
```

Command value for Polyphonic Key Pressure (Aftertouch) message (0xA0, or
160).

**See Also:** Constant Field Values

- CONTROL_CHANGE

```java
public static final int CONTROL_CHANGE
```

Command value for Control Change message (0xB0, or 176).

**See Also:** Constant Field Values

- PROGRAM_CHANGE

```java
public static final int PROGRAM_CHANGE
```

Command value for Program Change message (0xC0, or 192).

**See Also:** Constant Field Values

- CHANNEL_PRESSURE

```java
public static final int CHANNEL_PRESSURE
```

Command value for Channel Pressure (Aftertouch) message (0xD0, or 208).

**See Also:** Constant Field Values

- PITCH_BEND

```java
public static final int PITCH_BEND
```

Command value for Pitch Bend message (0xE0, or 224).

**See Also:** Constant Field Values

---

#### Field Detail

MIDI_TIME_CODE

```java
public static final int MIDI_TIME_CODE
```

Status byte for MIDI Time Code Quarter Frame message (0xF1, or 241).

**See Also:** MidiMessage.getStatus()

,

Constant Field Values

---

#### MIDI_TIME_CODE

public static final int MIDI_TIME_CODE

Status byte for MIDI Time Code Quarter Frame message (0xF1, or 241).

SONG_POSITION_POINTER

```java
public static final int SONG_POSITION_POINTER
```

Status byte for Song Position Pointer message (0xF2, or 242).

**See Also:** MidiMessage.getStatus()

,

Constant Field Values

---

#### SONG_POSITION_POINTER

public static final int SONG_POSITION_POINTER

Status byte for Song Position Pointer message (0xF2, or 242).

SONG_SELECT

```java
public static final int SONG_SELECT
```

Status byte for MIDI Song Select message (0xF3, or 243).

**See Also:** MidiMessage.getStatus()

,

Constant Field Values

---

#### SONG_SELECT

public static final int SONG_SELECT

Status byte for MIDI Song Select message (0xF3, or 243).

TUNE_REQUEST

```java
public static final int TUNE_REQUEST
```

Status byte for Tune Request message (0xF6, or 246).

**See Also:** MidiMessage.getStatus()

,

Constant Field Values

---

#### TUNE_REQUEST

public static final int TUNE_REQUEST

Status byte for Tune Request message (0xF6, or 246).

END_OF_EXCLUSIVE

```java
public static final int END_OF_EXCLUSIVE
```

Status byte for End of System Exclusive message (0xF7, or 247).

**See Also:** MidiMessage.getStatus()

,

Constant Field Values

---

#### END_OF_EXCLUSIVE

public static final int END_OF_EXCLUSIVE

Status byte for End of System Exclusive message (0xF7, or 247).

TIMING_CLOCK

```java
public static final int TIMING_CLOCK
```

Status byte for Timing Clock message (0xF8, or 248).

**See Also:** MidiMessage.getStatus()

,

Constant Field Values

---

#### TIMING_CLOCK

public static final int TIMING_CLOCK

Status byte for Timing Clock message (0xF8, or 248).

START

```java
public static final int START
```

Status byte for Start message (0xFA, or 250).

**See Also:** MidiMessage.getStatus()

,

Constant Field Values

---

#### START

public static final int START

Status byte for Start message (0xFA, or 250).

CONTINUE

```java
public static final int CONTINUE
```

Status byte for Continue message (0xFB, or 251).

**See Also:** MidiMessage.getStatus()

,

Constant Field Values

---

#### CONTINUE

public static final int CONTINUE

Status byte for Continue message (0xFB, or 251).

STOP

```java
public static final int STOP
```

Status byte for Stop message (0xFC, or 252).

**See Also:** MidiMessage.getStatus()

,

Constant Field Values

---

#### STOP

public static final int STOP

Status byte for Stop message (0xFC, or 252).

ACTIVE_SENSING

```java
public static final int ACTIVE_SENSING
```

Status byte for Active Sensing message (0xFE, or 254).

**See Also:** MidiMessage.getStatus()

,

Constant Field Values

---

#### ACTIVE_SENSING

public static final int ACTIVE_SENSING

Status byte for Active Sensing message (0xFE, or 254).

SYSTEM_RESET

```java
public static final int SYSTEM_RESET
```

Status byte for System Reset message (0xFF, or 255).

**See Also:** MidiMessage.getStatus()

,

Constant Field Values

---

#### SYSTEM_RESET

public static final int SYSTEM_RESET

Status byte for System Reset message (0xFF, or 255).

NOTE_OFF

```java
public static final int NOTE_OFF
```

Command value for Note Off message (0x80, or 128).

**See Also:** Constant Field Values

---

#### NOTE_OFF

public static final int NOTE_OFF

Command value for Note Off message (0x80, or 128).

NOTE_ON

```java
public static final int NOTE_ON
```

Command value for Note On message (0x90, or 144).

**See Also:** Constant Field Values

---

#### NOTE_ON

public static final int NOTE_ON

Command value for Note On message (0x90, or 144).

POLY_PRESSURE

```java
public static final int POLY_PRESSURE
```

Command value for Polyphonic Key Pressure (Aftertouch) message (0xA0, or
160).

**See Also:** Constant Field Values

---

#### POLY_PRESSURE

public static final int POLY_PRESSURE

Command value for Polyphonic Key Pressure (Aftertouch) message (0xA0, or
160).

CONTROL_CHANGE

```java
public static final int CONTROL_CHANGE
```

Command value for Control Change message (0xB0, or 176).

**See Also:** Constant Field Values

---

#### CONTROL_CHANGE

public static final int CONTROL_CHANGE

Command value for Control Change message (0xB0, or 176).

PROGRAM_CHANGE

```java
public static final int PROGRAM_CHANGE
```

Command value for Program Change message (0xC0, or 192).

**See Also:** Constant Field Values

---

#### PROGRAM_CHANGE

public static final int PROGRAM_CHANGE

Command value for Program Change message (0xC0, or 192).

CHANNEL_PRESSURE

```java
public static final int CHANNEL_PRESSURE
```

Command value for Channel Pressure (Aftertouch) message (0xD0, or 208).

**See Also:** Constant Field Values

---

#### CHANNEL_PRESSURE

public static final int CHANNEL_PRESSURE

Command value for Channel Pressure (Aftertouch) message (0xD0, or 208).

PITCH_BEND

```java
public static final int PITCH_BEND
```

Command value for Pitch Bend message (0xE0, or 224).

**See Also:** Constant Field Values

---

#### PITCH_BEND

public static final int PITCH_BEND

Command value for Pitch Bend message (0xE0, or 224).

Constructor Detail

- ShortMessage

```java
public ShortMessage()
```

Constructs a new

ShortMessage

. The contents of the new message
are guaranteed to specify a valid MIDI message. Subsequently, you may set
the contents of the message using one of the

setMessage

methods.

**See Also:** setMessage(int)

- ShortMessage

```java
public ShortMessage​(int status)
throws
InvalidMidiDataException
```

Constructs a new

ShortMessage

which represents a MIDI message
that takes no data bytes. The contents of the message can be changed by
using one of the

setMessage

methods.

**Parameters:** status

- the MIDI status byte
**Throws:** InvalidMidiDataException

- if

status

does not specify a
valid MIDI status byte for a message that requires no data bytes
**Since:** 1.7
**See Also:** setMessage(int)

,

setMessage(int, int, int)

,

setMessage(int, int, int, int)

,

MidiMessage.getStatus()

- ShortMessage

```java
public ShortMessage​(int status,
int data1,
int data2)
throws
InvalidMidiDataException
```

Constructs a new

ShortMessage

which represents a MIDI message
that takes up to two data bytes. If the message only takes one data byte,
the second data byte is ignored. If the message does not take any data
bytes, both data bytes are ignored. The contents of the message can be
changed by using one of the

setMessage

methods.

**Parameters:** status

- the MIDI status byte
**Parameters:** data1

- the first data byte
**Parameters:** data2

- the second data byte
**Throws:** InvalidMidiDataException

- if the status byte or all data bytes
belonging to the message do not specify a valid MIDI message
**Since:** 1.7
**See Also:** setMessage(int)

,

setMessage(int, int, int)

,

setMessage(int, int, int, int)

,

MidiMessage.getStatus()

,

getData1()

,

getData2()

- ShortMessage

```java
public ShortMessage​(int command,
int channel,
int data1,
int data2)
throws
InvalidMidiDataException
```

Constructs a new

ShortMessage

which represents a channel MIDI
message that takes up to two data bytes. If the message only takes one
data byte, the second data byte is ignored. If the message does not take
any data bytes, both data bytes are ignored. The contents of the message
can be changed by using one of the

setMessage

methods.

**Parameters:** command

- the MIDI command represented by this message
**Parameters:** channel

- the channel associated with the message
**Parameters:** data1

- the first data byte
**Parameters:** data2

- the second data byte
**Throws:** InvalidMidiDataException

- if the command value, channel value or
all data bytes belonging to the message do not specify a valid
MIDI message
**Since:** 1.7
**See Also:** setMessage(int)

,

setMessage(int, int, int)

,

setMessage(int, int, int, int)

,

getCommand()

,

getChannel()

,

getData1()

,

getData2()

- ShortMessage

```java
protected ShortMessage​(byte[] data)
```

Constructs a new

ShortMessage

.

**Parameters:** data

- an array of bytes containing the complete message. The
message data may be changed using the

setMessage

method.
**See Also:** setMessage(int)

---

#### Constructor Detail

ShortMessage

```java
public ShortMessage()
```

Constructs a new

ShortMessage

. The contents of the new message
are guaranteed to specify a valid MIDI message. Subsequently, you may set
the contents of the message using one of the

setMessage

methods.

**See Also:** setMessage(int)

---

#### ShortMessage

public ShortMessage()

Constructs a new

ShortMessage

. The contents of the new message
are guaranteed to specify a valid MIDI message. Subsequently, you may set
the contents of the message using one of the

setMessage

methods.

ShortMessage

```java
public ShortMessage​(int status)
throws
InvalidMidiDataException
```

Constructs a new

ShortMessage

which represents a MIDI message
that takes no data bytes. The contents of the message can be changed by
using one of the

setMessage

methods.

**Parameters:** status

- the MIDI status byte
**Throws:** InvalidMidiDataException

- if

status

does not specify a
valid MIDI status byte for a message that requires no data bytes
**Since:** 1.7
**See Also:** setMessage(int)

,

setMessage(int, int, int)

,

setMessage(int, int, int, int)

,

MidiMessage.getStatus()

---

#### ShortMessage

public ShortMessage​(int status)
throws

InvalidMidiDataException

Constructs a new

ShortMessage

which represents a MIDI message
that takes no data bytes. The contents of the message can be changed by
using one of the

setMessage

methods.

ShortMessage

```java
public ShortMessage​(int status,
int data1,
int data2)
throws
InvalidMidiDataException
```

Constructs a new

ShortMessage

which represents a MIDI message
that takes up to two data bytes. If the message only takes one data byte,
the second data byte is ignored. If the message does not take any data
bytes, both data bytes are ignored. The contents of the message can be
changed by using one of the

setMessage

methods.

**Parameters:** status

- the MIDI status byte
**Parameters:** data1

- the first data byte
**Parameters:** data2

- the second data byte
**Throws:** InvalidMidiDataException

- if the status byte or all data bytes
belonging to the message do not specify a valid MIDI message
**Since:** 1.7
**See Also:** setMessage(int)

,

setMessage(int, int, int)

,

setMessage(int, int, int, int)

,

MidiMessage.getStatus()

,

getData1()

,

getData2()

---

#### ShortMessage

public ShortMessage​(int status,
int data1,
int data2)
throws

InvalidMidiDataException

Constructs a new

ShortMessage

which represents a MIDI message
that takes up to two data bytes. If the message only takes one data byte,
the second data byte is ignored. If the message does not take any data
bytes, both data bytes are ignored. The contents of the message can be
changed by using one of the

setMessage

methods.

ShortMessage

```java
public ShortMessage​(int command,
int channel,
int data1,
int data2)
throws
InvalidMidiDataException
```

Constructs a new

ShortMessage

which represents a channel MIDI
message that takes up to two data bytes. If the message only takes one
data byte, the second data byte is ignored. If the message does not take
any data bytes, both data bytes are ignored. The contents of the message
can be changed by using one of the

setMessage

methods.

**Parameters:** command

- the MIDI command represented by this message
**Parameters:** channel

- the channel associated with the message
**Parameters:** data1

- the first data byte
**Parameters:** data2

- the second data byte
**Throws:** InvalidMidiDataException

- if the command value, channel value or
all data bytes belonging to the message do not specify a valid
MIDI message
**Since:** 1.7
**See Also:** setMessage(int)

,

setMessage(int, int, int)

,

setMessage(int, int, int, int)

,

getCommand()

,

getChannel()

,

getData1()

,

getData2()

---

#### ShortMessage

public ShortMessage​(int command,
int channel,
int data1,
int data2)
throws

InvalidMidiDataException

Constructs a new

ShortMessage

which represents a channel MIDI
message that takes up to two data bytes. If the message only takes one
data byte, the second data byte is ignored. If the message does not take
any data bytes, both data bytes are ignored. The contents of the message
can be changed by using one of the

setMessage

methods.

ShortMessage

```java
protected ShortMessage​(byte[] data)
```

Constructs a new

ShortMessage

.

**Parameters:** data

- an array of bytes containing the complete message. The
message data may be changed using the

setMessage

method.
**See Also:** setMessage(int)

---

#### ShortMessage

protected ShortMessage​(byte[] data)

Constructs a new

ShortMessage

.

Method Detail

- setMessage

```java
public void setMessage​(int status)
throws
InvalidMidiDataException
```

Sets the parameters for a MIDI message that takes no data bytes.

**Parameters:** status

- the MIDI status byte
**Throws:** InvalidMidiDataException

- if

status

does not specify a
valid MIDI status byte for a message that requires no data bytes
**See Also:** setMessage(int, int, int)

,

setMessage(int, int, int, int)

- setMessage

```java
public void setMessage​(int status,
int data1,
int data2)
throws
InvalidMidiDataException
```

Sets the parameters for a MIDI message that takes one or two data bytes.
If the message takes only one data byte, the second data byte is ignored;
if the message does not take any data bytes, both data bytes are ignored.

**Parameters:** status

- the MIDI status byte
**Parameters:** data1

- the first data byte
**Parameters:** data2

- the second data byte
**Throws:** InvalidMidiDataException

- if the status byte, or all data bytes
belonging to the message, do not specify a valid MIDI message
**See Also:** setMessage(int, int, int, int)

,

setMessage(int)

- setMessage

```java
public void setMessage​(int command,
int channel,
int data1,
int data2)
throws
InvalidMidiDataException
```

Sets the short message parameters for a channel message which takes up to
two data bytes. If the message only takes one data byte, the second data
byte is ignored; if the message does not take any data bytes, both data
bytes are ignored.

**Parameters:** command

- the MIDI command represented by this message
**Parameters:** channel

- the channel associated with the message
**Parameters:** data1

- the first data byte
**Parameters:** data2

- the second data byte
**Throws:** InvalidMidiDataException

- if the status byte or all data bytes
belonging to the message, do not specify a valid MIDI message
**See Also:** setMessage(int, int, int)

,

setMessage(int)

,

getCommand()

,

getChannel()

,

getData1()

,

getData2()

- getChannel

```java
public int getChannel()
```

Obtains the MIDI channel associated with this event. This method assumes
that the event is a MIDI channel message; if not, the return value will
not be meaningful.

**Returns:** MIDI channel associated with the message
**See Also:** setMessage(int, int, int, int)

- getCommand

```java
public int getCommand()
```

Obtains the MIDI command associated with this event. This method assumes
that the event is a MIDI channel message; if not, the return value will
not be meaningful.

**Returns:** the MIDI command associated with this event
**See Also:** setMessage(int, int, int, int)

- getData1

```java
public int getData1()
```

Obtains the first data byte in the message.

**Returns:** the value of the

data1

field
**See Also:** setMessage(int, int, int)

- getData2

```java
public int getData2()
```

Obtains the second data byte in the message.

**Returns:** the value of the

data2

field
**See Also:** setMessage(int, int, int)

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

- getDataLength

```java
protected final int getDataLength​(int status)
throws
InvalidMidiDataException
```

Retrieves the number of data bytes associated with a particular status
byte value.

**Parameters:** status

- status byte value, which must represent a short MIDI
message
**Returns:** data length in bytes (0, 1, or 2)
**Throws:** InvalidMidiDataException

- if the

status

argument does not
represent the status byte for any short message

---

#### Method Detail

setMessage

```java
public void setMessage​(int status)
throws
InvalidMidiDataException
```

Sets the parameters for a MIDI message that takes no data bytes.

**Parameters:** status

- the MIDI status byte
**Throws:** InvalidMidiDataException

- if

status

does not specify a
valid MIDI status byte for a message that requires no data bytes
**See Also:** setMessage(int, int, int)

,

setMessage(int, int, int, int)

---

#### setMessage

public void setMessage​(int status)
throws

InvalidMidiDataException

Sets the parameters for a MIDI message that takes no data bytes.

setMessage

```java
public void setMessage​(int status,
int data1,
int data2)
throws
InvalidMidiDataException
```

Sets the parameters for a MIDI message that takes one or two data bytes.
If the message takes only one data byte, the second data byte is ignored;
if the message does not take any data bytes, both data bytes are ignored.

**Parameters:** status

- the MIDI status byte
**Parameters:** data1

- the first data byte
**Parameters:** data2

- the second data byte
**Throws:** InvalidMidiDataException

- if the status byte, or all data bytes
belonging to the message, do not specify a valid MIDI message
**See Also:** setMessage(int, int, int, int)

,

setMessage(int)

---

#### setMessage

public void setMessage​(int status,
int data1,
int data2)
throws

InvalidMidiDataException

Sets the parameters for a MIDI message that takes one or two data bytes.
If the message takes only one data byte, the second data byte is ignored;
if the message does not take any data bytes, both data bytes are ignored.

setMessage

```java
public void setMessage​(int command,
int channel,
int data1,
int data2)
throws
InvalidMidiDataException
```

Sets the short message parameters for a channel message which takes up to
two data bytes. If the message only takes one data byte, the second data
byte is ignored; if the message does not take any data bytes, both data
bytes are ignored.

**Parameters:** command

- the MIDI command represented by this message
**Parameters:** channel

- the channel associated with the message
**Parameters:** data1

- the first data byte
**Parameters:** data2

- the second data byte
**Throws:** InvalidMidiDataException

- if the status byte or all data bytes
belonging to the message, do not specify a valid MIDI message
**See Also:** setMessage(int, int, int)

,

setMessage(int)

,

getCommand()

,

getChannel()

,

getData1()

,

getData2()

---

#### setMessage

public void setMessage​(int command,
int channel,
int data1,
int data2)
throws

InvalidMidiDataException

Sets the short message parameters for a channel message which takes up to
two data bytes. If the message only takes one data byte, the second data
byte is ignored; if the message does not take any data bytes, both data
bytes are ignored.

getChannel

```java
public int getChannel()
```

Obtains the MIDI channel associated with this event. This method assumes
that the event is a MIDI channel message; if not, the return value will
not be meaningful.

**Returns:** MIDI channel associated with the message
**See Also:** setMessage(int, int, int, int)

---

#### getChannel

public int getChannel()

Obtains the MIDI channel associated with this event. This method assumes
that the event is a MIDI channel message; if not, the return value will
not be meaningful.

getCommand

```java
public int getCommand()
```

Obtains the MIDI command associated with this event. This method assumes
that the event is a MIDI channel message; if not, the return value will
not be meaningful.

**Returns:** the MIDI command associated with this event
**See Also:** setMessage(int, int, int, int)

---

#### getCommand

public int getCommand()

Obtains the MIDI command associated with this event. This method assumes
that the event is a MIDI channel message; if not, the return value will
not be meaningful.

getData1

```java
public int getData1()
```

Obtains the first data byte in the message.

**Returns:** the value of the

data1

field
**See Also:** setMessage(int, int, int)

---

#### getData1

public int getData1()

Obtains the first data byte in the message.

getData2

```java
public int getData2()
```

Obtains the second data byte in the message.

**Returns:** the value of the

data2

field
**See Also:** setMessage(int, int, int)

---

#### getData2

public int getData2()

Obtains the second data byte in the message.

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

getDataLength

```java
protected final int getDataLength​(int status)
throws
InvalidMidiDataException
```

Retrieves the number of data bytes associated with a particular status
byte value.

**Parameters:** status

- status byte value, which must represent a short MIDI
message
**Returns:** data length in bytes (0, 1, or 2)
**Throws:** InvalidMidiDataException

- if the

status

argument does not
represent the status byte for any short message

---

#### getDataLength

protected final int getDataLength​(int status)
throws

InvalidMidiDataException

Retrieves the number of data bytes associated with a particular status
byte value.

---

