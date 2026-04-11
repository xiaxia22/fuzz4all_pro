# Class MidiEvent

**Source:** `java.desktop\javax\sound\midi\MidiEvent.html`

### Class Description

```java
public class
MidiEvent

extends
Object
```

MIDI events contain a MIDI message and a corresponding time-stamp expressed
in ticks, and can represent the MIDI event information stored in a MIDI file
or a

Sequence

object. The duration of a tick is specified by the
timing information contained in the MIDI file or

Sequence

object.

In Java Sound,

MidiEvent

objects are typically contained in a

Track

, and

Tracks

are likewise contained in a

Sequence

.

---

### Field Details

*No entries found.*

### Constructor Details

#### public MidiEvent​(
MidiMessage
message,
long tick)

Constructs a new

MidiEvent

.

**Parameters:**
- message

- the MIDI message contained in the event
- tick

- the time-stamp for the event, in MIDI ticks

---

### Method Details

#### public
MidiMessage
getMessage()

Obtains the MIDI message contained in the event.

**Returns:**
- the MIDI message

---

#### public void setTick​(long tick)

Sets the time-stamp for the event, in MIDI ticks.

**Parameters:**
- tick

- the new time-stamp, in MIDI ticks

---

#### public long getTick()

Obtains the time-stamp for the event, in MIDI ticks.

**Returns:**
- the time-stamp for the event, in MIDI ticks

---

### Additional Sections

#### Class MidiEvent

java.lang.Object

- javax.sound.midi.MidiEvent

javax.sound.midi.MidiEvent

```java
public class
MidiEvent

extends
Object
```

MIDI events contain a MIDI message and a corresponding time-stamp expressed
in ticks, and can represent the MIDI event information stored in a MIDI file
or a

Sequence

object. The duration of a tick is specified by the
timing information contained in the MIDI file or

Sequence

object.

In Java Sound,

MidiEvent

objects are typically contained in a

Track

, and

Tracks

are likewise contained in a

Sequence

.

public class

MidiEvent

extends

Object

MIDI events contain a MIDI message and a corresponding time-stamp expressed
in ticks, and can represent the MIDI event information stored in a MIDI file
or a

Sequence

object. The duration of a tick is specified by the
timing information contained in the MIDI file or

Sequence

object.

In Java Sound,

MidiEvent

objects are typically contained in a

Track

, and

Tracks

are likewise contained in a

Sequence

.

In Java Sound,

MidiEvent

objects are typically contained in a

Track

, and

Tracks

are likewise contained in a

Sequence

.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

MidiEvent

​(

MidiMessage

message,
long tick)

Constructs a new

MidiEvent

.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

MidiMessage

getMessage

()

Obtains the MIDI message contained in the event.

long

getTick

()

Obtains the time-stamp for the event, in MIDI ticks.

void

setTick

​(long tick)

Sets the time-stamp for the event, in MIDI ticks.

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

MidiEvent

​(

MidiMessage

message,
long tick)

Constructs a new

MidiEvent

.

---

#### Constructor Summary

Constructs a new

MidiEvent

.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

MidiMessage

getMessage

()

Obtains the MIDI message contained in the event.

long

getTick

()

Obtains the time-stamp for the event, in MIDI ticks.

void

setTick

​(long tick)

Sets the time-stamp for the event, in MIDI ticks.

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

Obtains the MIDI message contained in the event.

Obtains the time-stamp for the event, in MIDI ticks.

Sets the time-stamp for the event, in MIDI ticks.

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

- MidiEvent

```java
public MidiEvent​(
MidiMessage
message,
long tick)
```

Constructs a new

MidiEvent

.

**Parameters:** message

- the MIDI message contained in the event
**Parameters:** tick

- the time-stamp for the event, in MIDI ticks

============ METHOD DETAIL ==========

- Method Detail

- getMessage

```java
public
MidiMessage
getMessage()
```

Obtains the MIDI message contained in the event.

**Returns:** the MIDI message

- setTick

```java
public void setTick​(long tick)
```

Sets the time-stamp for the event, in MIDI ticks.

**Parameters:** tick

- the new time-stamp, in MIDI ticks

- getTick

```java
public long getTick()
```

Obtains the time-stamp for the event, in MIDI ticks.

**Returns:** the time-stamp for the event, in MIDI ticks

Constructor Detail

- MidiEvent

```java
public MidiEvent​(
MidiMessage
message,
long tick)
```

Constructs a new

MidiEvent

.

**Parameters:** message

- the MIDI message contained in the event
**Parameters:** tick

- the time-stamp for the event, in MIDI ticks

---

#### Constructor Detail

MidiEvent

```java
public MidiEvent​(
MidiMessage
message,
long tick)
```

Constructs a new

MidiEvent

.

**Parameters:** message

- the MIDI message contained in the event
**Parameters:** tick

- the time-stamp for the event, in MIDI ticks

---

#### MidiEvent

public MidiEvent​(

MidiMessage

message,
long tick)

Constructs a new

MidiEvent

.

Method Detail

- getMessage

```java
public
MidiMessage
getMessage()
```

Obtains the MIDI message contained in the event.

**Returns:** the MIDI message

- setTick

```java
public void setTick​(long tick)
```

Sets the time-stamp for the event, in MIDI ticks.

**Parameters:** tick

- the new time-stamp, in MIDI ticks

- getTick

```java
public long getTick()
```

Obtains the time-stamp for the event, in MIDI ticks.

**Returns:** the time-stamp for the event, in MIDI ticks

---

#### Method Detail

getMessage

```java
public
MidiMessage
getMessage()
```

Obtains the MIDI message contained in the event.

**Returns:** the MIDI message

---

#### getMessage

public

MidiMessage

getMessage()

Obtains the MIDI message contained in the event.

setTick

```java
public void setTick​(long tick)
```

Sets the time-stamp for the event, in MIDI ticks.

**Parameters:** tick

- the new time-stamp, in MIDI ticks

---

#### setTick

public void setTick​(long tick)

Sets the time-stamp for the event, in MIDI ticks.

getTick

```java
public long getTick()
```

Obtains the time-stamp for the event, in MIDI ticks.

**Returns:** the time-stamp for the event, in MIDI ticks

---

#### getTick

public long getTick()

Obtains the time-stamp for the event, in MIDI ticks.

---

