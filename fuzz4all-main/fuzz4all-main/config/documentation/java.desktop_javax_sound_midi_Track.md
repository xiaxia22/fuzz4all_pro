# Class Track

**Source:** `java.desktop\javax\sound\midi\Track.html`

### Class Description

```java
public class
Track

extends
Object
```

A MIDI track is an independent stream of MIDI events (time-stamped MIDI data)
that can be stored along with other tracks in a standard MIDI file. The MIDI
specification allows only 16 channels of MIDI data, but tracks are a way to
get around this limitation. A MIDI file can contain any number of tracks,
each containing its own stream of up to 16 channels of MIDI data.

A

Track

occupies a middle level in the hierarchy of data played by a

Sequencer

: sequencers play sequences, which contain tracks, which
contain MIDI events. A sequencer may provide controls that mute or solo
individual tracks.

The timing information and resolution for a track is controlled by and stored
in the sequence containing the track. A given

Track

is considered to
belong to the particular

Sequence

that maintains its timing. For this
reason, a new (empty) track is created by calling the

Sequence.createTrack()

method, rather than by directly invoking a

Track

constructor.

The

Track

class provides methods to edit the track by adding or
removing

MidiEvent

objects from it. These operations keep the event
list in the correct time order. Methods are also included to obtain the
track's size, in terms of either the number of events it contains or its
duration in ticks.

**See Also:** Sequencer.setTrackMute(int, boolean)

,

Sequencer.setTrackSolo(int, boolean)

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### public boolean add​(
MidiEvent
event)

Adds a new event to the track. However, if the event is already contained
in the track, it is not added again. The list of events is kept in time
order, meaning that this event inserted at the appropriate place in the
list, not necessarily at the end.

**Parameters:**
- event

- the event to add

**Returns:**
- true

if the event did not already exist in the track and
was added, otherwise

false

---

#### public boolean remove​(
MidiEvent
event)

Removes the specified event from the track.

**Parameters:**
- event

- the event to remove

**Returns:**
- true

if the event existed in the track and was removed,
otherwise

false

---

#### public
MidiEvent
get​(int index)
throws
ArrayIndexOutOfBoundsException

Obtains the event at the specified index.

**Parameters:**
- index

- the location of the desired event in the event vector

**Returns:**
- the event at the specified index

**Throws:**
- ArrayIndexOutOfBoundsException

- if the specified index is negative
or not less than the current size of this track

**See Also:**
- size()

---

#### public int size()

Obtains the number of events in this track.

**Returns:**
- the size of the track's event vector

---

#### public long ticks()

Obtains the length of the track, expressed in MIDI ticks. (The duration
of a tick in seconds is determined by the timing resolution of the

Sequence

containing this track, and also by the tempo of the
music as set by the sequencer.)

**Returns:**
- the duration, in ticks

**See Also:**
- Sequence(float, int)

,

Sequencer.setTempoInBPM(float)

,

Sequencer.getTickPosition()

---

### Additional Sections

#### Class Track

java.lang.Object

- javax.sound.midi.Track

javax.sound.midi.Track

```java
public class
Track

extends
Object
```

A MIDI track is an independent stream of MIDI events (time-stamped MIDI data)
that can be stored along with other tracks in a standard MIDI file. The MIDI
specification allows only 16 channels of MIDI data, but tracks are a way to
get around this limitation. A MIDI file can contain any number of tracks,
each containing its own stream of up to 16 channels of MIDI data.

A

Track

occupies a middle level in the hierarchy of data played by a

Sequencer

: sequencers play sequences, which contain tracks, which
contain MIDI events. A sequencer may provide controls that mute or solo
individual tracks.

The timing information and resolution for a track is controlled by and stored
in the sequence containing the track. A given

Track

is considered to
belong to the particular

Sequence

that maintains its timing. For this
reason, a new (empty) track is created by calling the

Sequence.createTrack()

method, rather than by directly invoking a

Track

constructor.

The

Track

class provides methods to edit the track by adding or
removing

MidiEvent

objects from it. These operations keep the event
list in the correct time order. Methods are also included to obtain the
track's size, in terms of either the number of events it contains or its
duration in ticks.

**See Also:** Sequencer.setTrackMute(int, boolean)

,

Sequencer.setTrackSolo(int, boolean)

public class

Track

extends

Object

A MIDI track is an independent stream of MIDI events (time-stamped MIDI data)
that can be stored along with other tracks in a standard MIDI file. The MIDI
specification allows only 16 channels of MIDI data, but tracks are a way to
get around this limitation. A MIDI file can contain any number of tracks,
each containing its own stream of up to 16 channels of MIDI data.

A

Track

occupies a middle level in the hierarchy of data played by a

Sequencer

: sequencers play sequences, which contain tracks, which
contain MIDI events. A sequencer may provide controls that mute or solo
individual tracks.

The timing information and resolution for a track is controlled by and stored
in the sequence containing the track. A given

Track

is considered to
belong to the particular

Sequence

that maintains its timing. For this
reason, a new (empty) track is created by calling the

Sequence.createTrack()

method, rather than by directly invoking a

Track

constructor.

The

Track

class provides methods to edit the track by adding or
removing

MidiEvent

objects from it. These operations keep the event
list in the correct time order. Methods are also included to obtain the
track's size, in terms of either the number of events it contains or its
duration in ticks.

A

Track

occupies a middle level in the hierarchy of data played by a

Sequencer

: sequencers play sequences, which contain tracks, which
contain MIDI events. A sequencer may provide controls that mute or solo
individual tracks.

The timing information and resolution for a track is controlled by and stored
in the sequence containing the track. A given

Track

is considered to
belong to the particular

Sequence

that maintains its timing. For this
reason, a new (empty) track is created by calling the

Sequence.createTrack()

method, rather than by directly invoking a

Track

constructor.

The

Track

class provides methods to edit the track by adding or
removing

MidiEvent

objects from it. These operations keep the event
list in the correct time order. Methods are also included to obtain the
track's size, in terms of either the number of events it contains or its
duration in ticks.

The timing information and resolution for a track is controlled by and stored
in the sequence containing the track. A given

Track

is considered to
belong to the particular

Sequence

that maintains its timing. For this
reason, a new (empty) track is created by calling the

Sequence.createTrack()

method, rather than by directly invoking a

Track

constructor.

The

Track

class provides methods to edit the track by adding or
removing

MidiEvent

objects from it. These operations keep the event
list in the correct time order. Methods are also included to obtain the
track's size, in terms of either the number of events it contains or its
duration in ticks.

The

Track

class provides methods to edit the track by adding or
removing

MidiEvent

objects from it. These operations keep the event
list in the correct time order. Methods are also included to obtain the
track's size, in terms of either the number of events it contains or its
duration in ticks.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

boolean

add

​(

MidiEvent

event)

Adds a new event to the track.

MidiEvent

get

​(int index)

Obtains the event at the specified index.

boolean

remove

​(

MidiEvent

event)

Removes the specified event from the track.

int

size

()

Obtains the number of events in this track.

long

ticks

()

Obtains the length of the track, expressed in MIDI ticks.

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

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

boolean

add

​(

MidiEvent

event)

Adds a new event to the track.

MidiEvent

get

​(int index)

Obtains the event at the specified index.

boolean

remove

​(

MidiEvent

event)

Removes the specified event from the track.

int

size

()

Obtains the number of events in this track.

long

ticks

()

Obtains the length of the track, expressed in MIDI ticks.

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

Adds a new event to the track.

Obtains the event at the specified index.

Removes the specified event from the track.

Obtains the number of events in this track.

Obtains the length of the track, expressed in MIDI ticks.

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

============ METHOD DETAIL ==========

- Method Detail

- add

```java
public boolean add​(
MidiEvent
event)
```

Adds a new event to the track. However, if the event is already contained
in the track, it is not added again. The list of events is kept in time
order, meaning that this event inserted at the appropriate place in the
list, not necessarily at the end.

**Parameters:** event

- the event to add
**Returns:** true

if the event did not already exist in the track and
was added, otherwise

false

- remove

```java
public boolean remove​(
MidiEvent
event)
```

Removes the specified event from the track.

**Parameters:** event

- the event to remove
**Returns:** true

if the event existed in the track and was removed,
otherwise

false

- get

```java
public
MidiEvent
get​(int index)
throws
ArrayIndexOutOfBoundsException
```

Obtains the event at the specified index.

**Parameters:** index

- the location of the desired event in the event vector
**Returns:** the event at the specified index
**Throws:** ArrayIndexOutOfBoundsException

- if the specified index is negative
or not less than the current size of this track
**See Also:** size()

- size

```java
public int size()
```

Obtains the number of events in this track.

**Returns:** the size of the track's event vector

- ticks

```java
public long ticks()
```

Obtains the length of the track, expressed in MIDI ticks. (The duration
of a tick in seconds is determined by the timing resolution of the

Sequence

containing this track, and also by the tempo of the
music as set by the sequencer.)

**Returns:** the duration, in ticks
**See Also:** Sequence(float, int)

,

Sequencer.setTempoInBPM(float)

,

Sequencer.getTickPosition()

Method Detail

- add

```java
public boolean add​(
MidiEvent
event)
```

Adds a new event to the track. However, if the event is already contained
in the track, it is not added again. The list of events is kept in time
order, meaning that this event inserted at the appropriate place in the
list, not necessarily at the end.

**Parameters:** event

- the event to add
**Returns:** true

if the event did not already exist in the track and
was added, otherwise

false

- remove

```java
public boolean remove​(
MidiEvent
event)
```

Removes the specified event from the track.

**Parameters:** event

- the event to remove
**Returns:** true

if the event existed in the track and was removed,
otherwise

false

- get

```java
public
MidiEvent
get​(int index)
throws
ArrayIndexOutOfBoundsException
```

Obtains the event at the specified index.

**Parameters:** index

- the location of the desired event in the event vector
**Returns:** the event at the specified index
**Throws:** ArrayIndexOutOfBoundsException

- if the specified index is negative
or not less than the current size of this track
**See Also:** size()

- size

```java
public int size()
```

Obtains the number of events in this track.

**Returns:** the size of the track's event vector

- ticks

```java
public long ticks()
```

Obtains the length of the track, expressed in MIDI ticks. (The duration
of a tick in seconds is determined by the timing resolution of the

Sequence

containing this track, and also by the tempo of the
music as set by the sequencer.)

**Returns:** the duration, in ticks
**See Also:** Sequence(float, int)

,

Sequencer.setTempoInBPM(float)

,

Sequencer.getTickPosition()

---

#### Method Detail

add

```java
public boolean add​(
MidiEvent
event)
```

Adds a new event to the track. However, if the event is already contained
in the track, it is not added again. The list of events is kept in time
order, meaning that this event inserted at the appropriate place in the
list, not necessarily at the end.

**Parameters:** event

- the event to add
**Returns:** true

if the event did not already exist in the track and
was added, otherwise

false

---

#### add

public boolean add​(

MidiEvent

event)

Adds a new event to the track. However, if the event is already contained
in the track, it is not added again. The list of events is kept in time
order, meaning that this event inserted at the appropriate place in the
list, not necessarily at the end.

remove

```java
public boolean remove​(
MidiEvent
event)
```

Removes the specified event from the track.

**Parameters:** event

- the event to remove
**Returns:** true

if the event existed in the track and was removed,
otherwise

false

---

#### remove

public boolean remove​(

MidiEvent

event)

Removes the specified event from the track.

get

```java
public
MidiEvent
get​(int index)
throws
ArrayIndexOutOfBoundsException
```

Obtains the event at the specified index.

**Parameters:** index

- the location of the desired event in the event vector
**Returns:** the event at the specified index
**Throws:** ArrayIndexOutOfBoundsException

- if the specified index is negative
or not less than the current size of this track
**See Also:** size()

---

#### get

public

MidiEvent

get​(int index)
throws

ArrayIndexOutOfBoundsException

Obtains the event at the specified index.

size

```java
public int size()
```

Obtains the number of events in this track.

**Returns:** the size of the track's event vector

---

#### size

public int size()

Obtains the number of events in this track.

ticks

```java
public long ticks()
```

Obtains the length of the track, expressed in MIDI ticks. (The duration
of a tick in seconds is determined by the timing resolution of the

Sequence

containing this track, and also by the tempo of the
music as set by the sequencer.)

**Returns:** the duration, in ticks
**See Also:** Sequence(float, int)

,

Sequencer.setTempoInBPM(float)

,

Sequencer.getTickPosition()

---

#### ticks

public long ticks()

Obtains the length of the track, expressed in MIDI ticks. (The duration
of a tick in seconds is determined by the timing resolution of the

Sequence

containing this track, and also by the tempo of the
music as set by the sequencer.)

---

