# Interface Clip

**Source:** `java.desktop\javax\sound\sampled\Clip.html`

### Class Description

```java
public interface
Clip

extends
DataLine
```

The

Clip

interface represents a special kind of data line whose audio
data can be loaded prior to playback, instead of being streamed in real time.

Because the data is pre-loaded and has a known length, you can set a clip to
start playing at any position in its audio data. You can also create a loop,
so that when the clip is played it will cycle repeatedly. Loops are specified
with a starting and ending sample frame, along with the number of times that
the loop should be played.

Clips may be obtained from a

Mixer

that supports lines of this type.
Data is loaded into a clip when it is opened.

Playback of an audio clip may be started and stopped using the

start

and

stop

methods. These methods do not
reset the media position;

start

causes playback to continue from the
position where playback was last stopped. To restart playback from the
beginning of the clip's audio data, simply follow the invocation of

stop

with

setFramePosition(0)

, which rewinds the media to the
beginning of the clip.

**All Superinterfaces:** AutoCloseable

,

DataLine

,

Line

---

### Field Details

#### static final int LOOP_CONTINUOUSLY

A value indicating that looping should continue indefinitely rather than
complete after a specific number of loops.

**See Also:**
- loop(int)

,

Constant Field Values

---

### Constructor Details

*No entries found.*

### Method Details

#### void open​(
AudioFormat
format,
byte[] data,
int offset,
int bufferSize)
throws
LineUnavailableException

Opens the clip, meaning that it should acquire any required system
resources and become operational. The clip is opened with the format and
audio data indicated. If this operation succeeds, the line is marked as
open and an

OPEN

event is dispatched to the
line's listeners.

Invoking this method on a line which is already open is illegal and may
result in an

IllegalStateException

.

Note that some lines, once closed, cannot be reopened. Attempts to reopen
such a line will always result in a

LineUnavailableException

.

**Parameters:**
- format

- the format of the supplied audio data
- data

- a byte array containing audio data to load into the clip
- offset

- the point at which to start copying, expressed in

bytes

from the beginning of the array
- bufferSize

- the number of

bytes

of data to load into the
clip from the array

**Throws:**
- LineUnavailableException

- if the line cannot be opened due to
resource restrictions
- IllegalArgumentException

- if the buffer size does not represent an
integral number of sample frames, or if

format

is not
fully specified or invalid
- IllegalStateException

- if the line is already open
- SecurityException

- if the line cannot be opened due to security
restrictions

**See Also:**
- Line.close()

,

Line.isOpen()

,

LineListener

---

#### void open​(
AudioInputStream
stream)
throws
LineUnavailableException
,

IOException

Opens the clip with the format and audio data present in the provided
audio input stream. Opening a clip means that it should acquire any
required system resources and become operational. If this operation input
stream. If this operation succeeds, the line is marked open and an

OPEN

event is dispatched to the line's
listeners.

Invoking this method on a line which is already open is illegal and may
result in an

IllegalStateException

.

Note that some lines, once closed, cannot be reopened. Attempts to reopen
such a line will always result in a

LineUnavailableException

.

**Parameters:**
- stream

- an audio input stream from which audio data will be read
into the clip

**Throws:**
- LineUnavailableException

- if the line cannot be opened due to
resource restrictions
- IOException

- if an I/O exception occurs during reading of the
stream
- IllegalArgumentException

- if the stream's audio format is not
fully specified or invalid
- IllegalStateException

- if the line is already open
- SecurityException

- if the line cannot be opened due to security
restrictions

**See Also:**
- Line.close()

,

Line.isOpen()

,

LineListener

---

#### int getFrameLength()

Obtains the media length in sample frames.

**Returns:**
- the media length, expressed in sample frames, or

AudioSystem.NOT_SPECIFIED

if the line is not open

**See Also:**
- AudioSystem.NOT_SPECIFIED

---

#### long getMicrosecondLength()

Obtains the media duration in microseconds.

**Returns:**
- the media duration, expressed in microseconds, or

AudioSystem.NOT_SPECIFIED

if the line is not open

**See Also:**
- AudioSystem.NOT_SPECIFIED

---

#### void setFramePosition​(int frames)

Sets the media position in sample frames. The position is zero-based; the
first frame is frame number zero. When the clip begins playing the next
time, it will start by playing the frame at this position.

To obtain the current position in sample frames, use the

getFramePosition

method of

DataLine

.

**Parameters:**
- frames

- the desired new media position, expressed in sample frames

---

#### void setMicrosecondPosition​(long microseconds)

Sets the media position in microseconds. When the clip begins playing the
next time, it will start at this position. The level of precision is not
guaranteed. For example, an implementation might calculate the
microsecond position from the current frame position and the audio sample
frame rate. The precision in microseconds would then be limited to the
number of microseconds per sample frame.

To obtain the current position in microseconds, use the

getMicrosecondPosition

method of

DataLine

.

**Parameters:**
- microseconds

- the desired new media position, expressed in
microseconds

---

#### void setLoopPoints​(int start,
int end)

Sets the first and last sample frames that will be played in the loop.
The ending point must be greater than or equal to the starting point, and
both must fall within the size of the loaded media. A value of 0 for the
starting point means the beginning of the loaded media. Similarly, a
value of -1 for the ending point indicates the last frame of the media.

**Parameters:**
- start

- the loop's starting position, in sample frames (zero-based)
- end

- the loop's ending position, in sample frames (zero-based), or
-1 to indicate the final frame

**Throws:**
- IllegalArgumentException

- if the requested loop points cannot be
set, usually because one or both falls outside the media's
duration or because the ending point is before the starting point

---

#### void loop​(int count)

Starts looping playback from the current position. Playback will continue
to the loop's end point, then loop back to the loop start point

count

times, and finally continue playback to the end of the
clip.

If the current position when this method is invoked is greater than the
loop end point, playback simply continues to the end of the clip without
looping.

A

count

value of 0 indicates that any current looping should
cease and playback should continue to the end of the clip. The behavior
is undefined when this method is invoked with any other value during a
loop operation.

If playback is stopped during looping, the current loop status is
cleared; the behavior of subsequent loop and start requests is not
affected by an interrupted loop operation.

**Parameters:**
- count

- the number of times playback should loop back from the
loop's end position to the loop's start position, or

LOOP_CONTINUOUSLY

to indicate that looping should
continue until interrupted

---

### Additional Sections

#### Interface Clip

**All Superinterfaces:** AutoCloseable

,

DataLine

,

Line

```java
public interface
Clip

extends
DataLine
```

The

Clip

interface represents a special kind of data line whose audio
data can be loaded prior to playback, instead of being streamed in real time.

Because the data is pre-loaded and has a known length, you can set a clip to
start playing at any position in its audio data. You can also create a loop,
so that when the clip is played it will cycle repeatedly. Loops are specified
with a starting and ending sample frame, along with the number of times that
the loop should be played.

Clips may be obtained from a

Mixer

that supports lines of this type.
Data is loaded into a clip when it is opened.

Playback of an audio clip may be started and stopped using the

start

and

stop

methods. These methods do not
reset the media position;

start

causes playback to continue from the
position where playback was last stopped. To restart playback from the
beginning of the clip's audio data, simply follow the invocation of

stop

with

setFramePosition(0)

, which rewinds the media to the
beginning of the clip.

**Since:** 1.3

public interface

Clip

extends

DataLine

The

Clip

interface represents a special kind of data line whose audio
data can be loaded prior to playback, instead of being streamed in real time.

Because the data is pre-loaded and has a known length, you can set a clip to
start playing at any position in its audio data. You can also create a loop,
so that when the clip is played it will cycle repeatedly. Loops are specified
with a starting and ending sample frame, along with the number of times that
the loop should be played.

Clips may be obtained from a

Mixer

that supports lines of this type.
Data is loaded into a clip when it is opened.

Playback of an audio clip may be started and stopped using the

start

and

stop

methods. These methods do not
reset the media position;

start

causes playback to continue from the
position where playback was last stopped. To restart playback from the
beginning of the clip's audio data, simply follow the invocation of

stop

with

setFramePosition(0)

, which rewinds the media to the
beginning of the clip.

Because the data is pre-loaded and has a known length, you can set a clip to
start playing at any position in its audio data. You can also create a loop,
so that when the clip is played it will cycle repeatedly. Loops are specified
with a starting and ending sample frame, along with the number of times that
the loop should be played.

Clips may be obtained from a

Mixer

that supports lines of this type.
Data is loaded into a clip when it is opened.

Playback of an audio clip may be started and stopped using the

start

and

stop

methods. These methods do not
reset the media position;

start

causes playback to continue from the
position where playback was last stopped. To restart playback from the
beginning of the clip's audio data, simply follow the invocation of

stop

with

setFramePosition(0)

, which rewinds the media to the
beginning of the clip.

Clips may be obtained from a

Mixer

that supports lines of this type.
Data is loaded into a clip when it is opened.

Playback of an audio clip may be started and stopped using the

start

and

stop

methods. These methods do not
reset the media position;

start

causes playback to continue from the
position where playback was last stopped. To restart playback from the
beginning of the clip's audio data, simply follow the invocation of

stop

with

setFramePosition(0)

, which rewinds the media to the
beginning of the clip.

Playback of an audio clip may be started and stopped using the

start

and

stop

methods. These methods do not
reset the media position;

start

causes playback to continue from the
position where playback was last stopped. To restart playback from the
beginning of the clip's audio data, simply follow the invocation of

stop

with

setFramePosition(0)

, which rewinds the media to the
beginning of the clip.

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

- Nested classes/interfaces declared in interface javax.sound.sampled.

DataLine

DataLine.Info

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static int

LOOP_CONTINUOUSLY

A value indicating that looping should continue indefinitely rather than
complete after a specific number of loops.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

int

getFrameLength

()

Obtains the media length in sample frames.

long

getMicrosecondLength

()

Obtains the media duration in microseconds.

void

loop

​(int count)

Starts looping playback from the current position.

void

open

​(

AudioFormat

format,
byte[] data,
int offset,
int bufferSize)

Opens the clip, meaning that it should acquire any required system
resources and become operational.

void

open

​(

AudioInputStream

stream)

Opens the clip with the format and audio data present in the provided
audio input stream.

void

setFramePosition

​(int frames)

Sets the media position in sample frames.

void

setLoopPoints

​(int start,
int end)

Sets the first and last sample frames that will be played in the loop.

void

setMicrosecondPosition

​(long microseconds)

Sets the media position in microseconds.

- Methods declared in interface javax.sound.sampled.

DataLine

available

,

drain

,

flush

,

getBufferSize

,

getFormat

,

getFramePosition

,

getLevel

,

getLongFramePosition

,

getMicrosecondPosition

,

isActive

,

isRunning

,

start

,

stop

- Methods declared in interface javax.sound.sampled.

Line

addLineListener

,

close

,

getControl

,

getControls

,

getLineInfo

,

isControlSupported

,

isOpen

,

open

,

removeLineListener

Nested Class Summary

- Nested classes/interfaces declared in interface javax.sound.sampled.

DataLine

DataLine.Info

---

#### Nested Class Summary

Nested classes/interfaces declared in interface javax.sound.sampled.

DataLine

DataLine.Info

---

#### Nested classes/interfaces declared in interface javax.sound.sampled. DataLine

Field Summary

Fields

Modifier and Type

Field

Description

static int

LOOP_CONTINUOUSLY

A value indicating that looping should continue indefinitely rather than
complete after a specific number of loops.

---

#### Field Summary

A value indicating that looping should continue indefinitely rather than
complete after a specific number of loops.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

int

getFrameLength

()

Obtains the media length in sample frames.

long

getMicrosecondLength

()

Obtains the media duration in microseconds.

void

loop

​(int count)

Starts looping playback from the current position.

void

open

​(

AudioFormat

format,
byte[] data,
int offset,
int bufferSize)

Opens the clip, meaning that it should acquire any required system
resources and become operational.

void

open

​(

AudioInputStream

stream)

Opens the clip with the format and audio data present in the provided
audio input stream.

void

setFramePosition

​(int frames)

Sets the media position in sample frames.

void

setLoopPoints

​(int start,
int end)

Sets the first and last sample frames that will be played in the loop.

void

setMicrosecondPosition

​(long microseconds)

Sets the media position in microseconds.

- Methods declared in interface javax.sound.sampled.

DataLine

available

,

drain

,

flush

,

getBufferSize

,

getFormat

,

getFramePosition

,

getLevel

,

getLongFramePosition

,

getMicrosecondPosition

,

isActive

,

isRunning

,

start

,

stop

- Methods declared in interface javax.sound.sampled.

Line

addLineListener

,

close

,

getControl

,

getControls

,

getLineInfo

,

isControlSupported

,

isOpen

,

open

,

removeLineListener

---

#### Method Summary

Obtains the media length in sample frames.

Obtains the media duration in microseconds.

Starts looping playback from the current position.

Opens the clip, meaning that it should acquire any required system
resources and become operational.

Opens the clip with the format and audio data present in the provided
audio input stream.

Sets the media position in sample frames.

Sets the first and last sample frames that will be played in the loop.

Sets the media position in microseconds.

Methods declared in interface javax.sound.sampled.

DataLine

available

,

drain

,

flush

,

getBufferSize

,

getFormat

,

getFramePosition

,

getLevel

,

getLongFramePosition

,

getMicrosecondPosition

,

isActive

,

isRunning

,

start

,

stop

---

#### Methods declared in interface javax.sound.sampled. DataLine

Methods declared in interface javax.sound.sampled.

Line

addLineListener

,

close

,

getControl

,

getControls

,

getLineInfo

,

isControlSupported

,

isOpen

,

open

,

removeLineListener

---

#### Methods declared in interface javax.sound.sampled. Line

============ FIELD DETAIL ===========

- Field Detail

- LOOP_CONTINUOUSLY

```java
static final int LOOP_CONTINUOUSLY
```

A value indicating that looping should continue indefinitely rather than
complete after a specific number of loops.

**See Also:** loop(int)

,

Constant Field Values

============ METHOD DETAIL ==========

- Method Detail

- open

```java
void open​(
AudioFormat
format,
byte[] data,
int offset,
int bufferSize)
throws
LineUnavailableException
```

Opens the clip, meaning that it should acquire any required system
resources and become operational. The clip is opened with the format and
audio data indicated. If this operation succeeds, the line is marked as
open and an

OPEN

event is dispatched to the
line's listeners.

Invoking this method on a line which is already open is illegal and may
result in an

IllegalStateException

.

Note that some lines, once closed, cannot be reopened. Attempts to reopen
such a line will always result in a

LineUnavailableException

.

**Parameters:** format

- the format of the supplied audio data
**Parameters:** data

- a byte array containing audio data to load into the clip
**Parameters:** offset

- the point at which to start copying, expressed in

bytes

from the beginning of the array
**Parameters:** bufferSize

- the number of

bytes

of data to load into the
clip from the array
**Throws:** LineUnavailableException

- if the line cannot be opened due to
resource restrictions
**Throws:** IllegalArgumentException

- if the buffer size does not represent an
integral number of sample frames, or if

format

is not
fully specified or invalid
**Throws:** IllegalStateException

- if the line is already open
**Throws:** SecurityException

- if the line cannot be opened due to security
restrictions
**See Also:** Line.close()

,

Line.isOpen()

,

LineListener

- open

```java
void open​(
AudioInputStream
stream)
throws
LineUnavailableException
,

IOException
```

Opens the clip with the format and audio data present in the provided
audio input stream. Opening a clip means that it should acquire any
required system resources and become operational. If this operation input
stream. If this operation succeeds, the line is marked open and an

OPEN

event is dispatched to the line's
listeners.

Invoking this method on a line which is already open is illegal and may
result in an

IllegalStateException

.

Note that some lines, once closed, cannot be reopened. Attempts to reopen
such a line will always result in a

LineUnavailableException

.

**Parameters:** stream

- an audio input stream from which audio data will be read
into the clip
**Throws:** LineUnavailableException

- if the line cannot be opened due to
resource restrictions
**Throws:** IOException

- if an I/O exception occurs during reading of the
stream
**Throws:** IllegalArgumentException

- if the stream's audio format is not
fully specified or invalid
**Throws:** IllegalStateException

- if the line is already open
**Throws:** SecurityException

- if the line cannot be opened due to security
restrictions
**See Also:** Line.close()

,

Line.isOpen()

,

LineListener

- getFrameLength

```java
int getFrameLength()
```

Obtains the media length in sample frames.

**Returns:** the media length, expressed in sample frames, or

AudioSystem.NOT_SPECIFIED

if the line is not open
**See Also:** AudioSystem.NOT_SPECIFIED

- getMicrosecondLength

```java
long getMicrosecondLength()
```

Obtains the media duration in microseconds.

**Returns:** the media duration, expressed in microseconds, or

AudioSystem.NOT_SPECIFIED

if the line is not open
**See Also:** AudioSystem.NOT_SPECIFIED

- setFramePosition

```java
void setFramePosition​(int frames)
```

Sets the media position in sample frames. The position is zero-based; the
first frame is frame number zero. When the clip begins playing the next
time, it will start by playing the frame at this position.

To obtain the current position in sample frames, use the

getFramePosition

method of

DataLine

.

**Parameters:** frames

- the desired new media position, expressed in sample frames

- setMicrosecondPosition

```java
void setMicrosecondPosition​(long microseconds)
```

Sets the media position in microseconds. When the clip begins playing the
next time, it will start at this position. The level of precision is not
guaranteed. For example, an implementation might calculate the
microsecond position from the current frame position and the audio sample
frame rate. The precision in microseconds would then be limited to the
number of microseconds per sample frame.

To obtain the current position in microseconds, use the

getMicrosecondPosition

method of

DataLine

.

**Parameters:** microseconds

- the desired new media position, expressed in
microseconds

- setLoopPoints

```java
void setLoopPoints​(int start,
int end)
```

Sets the first and last sample frames that will be played in the loop.
The ending point must be greater than or equal to the starting point, and
both must fall within the size of the loaded media. A value of 0 for the
starting point means the beginning of the loaded media. Similarly, a
value of -1 for the ending point indicates the last frame of the media.

**Parameters:** start

- the loop's starting position, in sample frames (zero-based)
**Parameters:** end

- the loop's ending position, in sample frames (zero-based), or
-1 to indicate the final frame
**Throws:** IllegalArgumentException

- if the requested loop points cannot be
set, usually because one or both falls outside the media's
duration or because the ending point is before the starting point

- loop

```java
void loop​(int count)
```

Starts looping playback from the current position. Playback will continue
to the loop's end point, then loop back to the loop start point

count

times, and finally continue playback to the end of the
clip.

If the current position when this method is invoked is greater than the
loop end point, playback simply continues to the end of the clip without
looping.

A

count

value of 0 indicates that any current looping should
cease and playback should continue to the end of the clip. The behavior
is undefined when this method is invoked with any other value during a
loop operation.

If playback is stopped during looping, the current loop status is
cleared; the behavior of subsequent loop and start requests is not
affected by an interrupted loop operation.

**Parameters:** count

- the number of times playback should loop back from the
loop's end position to the loop's start position, or

LOOP_CONTINUOUSLY

to indicate that looping should
continue until interrupted

Field Detail

- LOOP_CONTINUOUSLY

```java
static final int LOOP_CONTINUOUSLY
```

A value indicating that looping should continue indefinitely rather than
complete after a specific number of loops.

**See Also:** loop(int)

,

Constant Field Values

---

#### Field Detail

LOOP_CONTINUOUSLY

```java
static final int LOOP_CONTINUOUSLY
```

A value indicating that looping should continue indefinitely rather than
complete after a specific number of loops.

**See Also:** loop(int)

,

Constant Field Values

---

#### LOOP_CONTINUOUSLY

static final int LOOP_CONTINUOUSLY

A value indicating that looping should continue indefinitely rather than
complete after a specific number of loops.

Method Detail

- open

```java
void open​(
AudioFormat
format,
byte[] data,
int offset,
int bufferSize)
throws
LineUnavailableException
```

Opens the clip, meaning that it should acquire any required system
resources and become operational. The clip is opened with the format and
audio data indicated. If this operation succeeds, the line is marked as
open and an

OPEN

event is dispatched to the
line's listeners.

Invoking this method on a line which is already open is illegal and may
result in an

IllegalStateException

.

Note that some lines, once closed, cannot be reopened. Attempts to reopen
such a line will always result in a

LineUnavailableException

.

**Parameters:** format

- the format of the supplied audio data
**Parameters:** data

- a byte array containing audio data to load into the clip
**Parameters:** offset

- the point at which to start copying, expressed in

bytes

from the beginning of the array
**Parameters:** bufferSize

- the number of

bytes

of data to load into the
clip from the array
**Throws:** LineUnavailableException

- if the line cannot be opened due to
resource restrictions
**Throws:** IllegalArgumentException

- if the buffer size does not represent an
integral number of sample frames, or if

format

is not
fully specified or invalid
**Throws:** IllegalStateException

- if the line is already open
**Throws:** SecurityException

- if the line cannot be opened due to security
restrictions
**See Also:** Line.close()

,

Line.isOpen()

,

LineListener

- open

```java
void open​(
AudioInputStream
stream)
throws
LineUnavailableException
,

IOException
```

Opens the clip with the format and audio data present in the provided
audio input stream. Opening a clip means that it should acquire any
required system resources and become operational. If this operation input
stream. If this operation succeeds, the line is marked open and an

OPEN

event is dispatched to the line's
listeners.

Invoking this method on a line which is already open is illegal and may
result in an

IllegalStateException

.

Note that some lines, once closed, cannot be reopened. Attempts to reopen
such a line will always result in a

LineUnavailableException

.

**Parameters:** stream

- an audio input stream from which audio data will be read
into the clip
**Throws:** LineUnavailableException

- if the line cannot be opened due to
resource restrictions
**Throws:** IOException

- if an I/O exception occurs during reading of the
stream
**Throws:** IllegalArgumentException

- if the stream's audio format is not
fully specified or invalid
**Throws:** IllegalStateException

- if the line is already open
**Throws:** SecurityException

- if the line cannot be opened due to security
restrictions
**See Also:** Line.close()

,

Line.isOpen()

,

LineListener

- getFrameLength

```java
int getFrameLength()
```

Obtains the media length in sample frames.

**Returns:** the media length, expressed in sample frames, or

AudioSystem.NOT_SPECIFIED

if the line is not open
**See Also:** AudioSystem.NOT_SPECIFIED

- getMicrosecondLength

```java
long getMicrosecondLength()
```

Obtains the media duration in microseconds.

**Returns:** the media duration, expressed in microseconds, or

AudioSystem.NOT_SPECIFIED

if the line is not open
**See Also:** AudioSystem.NOT_SPECIFIED

- setFramePosition

```java
void setFramePosition​(int frames)
```

Sets the media position in sample frames. The position is zero-based; the
first frame is frame number zero. When the clip begins playing the next
time, it will start by playing the frame at this position.

To obtain the current position in sample frames, use the

getFramePosition

method of

DataLine

.

**Parameters:** frames

- the desired new media position, expressed in sample frames

- setMicrosecondPosition

```java
void setMicrosecondPosition​(long microseconds)
```

Sets the media position in microseconds. When the clip begins playing the
next time, it will start at this position. The level of precision is not
guaranteed. For example, an implementation might calculate the
microsecond position from the current frame position and the audio sample
frame rate. The precision in microseconds would then be limited to the
number of microseconds per sample frame.

To obtain the current position in microseconds, use the

getMicrosecondPosition

method of

DataLine

.

**Parameters:** microseconds

- the desired new media position, expressed in
microseconds

- setLoopPoints

```java
void setLoopPoints​(int start,
int end)
```

Sets the first and last sample frames that will be played in the loop.
The ending point must be greater than or equal to the starting point, and
both must fall within the size of the loaded media. A value of 0 for the
starting point means the beginning of the loaded media. Similarly, a
value of -1 for the ending point indicates the last frame of the media.

**Parameters:** start

- the loop's starting position, in sample frames (zero-based)
**Parameters:** end

- the loop's ending position, in sample frames (zero-based), or
-1 to indicate the final frame
**Throws:** IllegalArgumentException

- if the requested loop points cannot be
set, usually because one or both falls outside the media's
duration or because the ending point is before the starting point

- loop

```java
void loop​(int count)
```

Starts looping playback from the current position. Playback will continue
to the loop's end point, then loop back to the loop start point

count

times, and finally continue playback to the end of the
clip.

If the current position when this method is invoked is greater than the
loop end point, playback simply continues to the end of the clip without
looping.

A

count

value of 0 indicates that any current looping should
cease and playback should continue to the end of the clip. The behavior
is undefined when this method is invoked with any other value during a
loop operation.

If playback is stopped during looping, the current loop status is
cleared; the behavior of subsequent loop and start requests is not
affected by an interrupted loop operation.

**Parameters:** count

- the number of times playback should loop back from the
loop's end position to the loop's start position, or

LOOP_CONTINUOUSLY

to indicate that looping should
continue until interrupted

---

#### Method Detail

open

```java
void open​(
AudioFormat
format,
byte[] data,
int offset,
int bufferSize)
throws
LineUnavailableException
```

Opens the clip, meaning that it should acquire any required system
resources and become operational. The clip is opened with the format and
audio data indicated. If this operation succeeds, the line is marked as
open and an

OPEN

event is dispatched to the
line's listeners.

Invoking this method on a line which is already open is illegal and may
result in an

IllegalStateException

.

Note that some lines, once closed, cannot be reopened. Attempts to reopen
such a line will always result in a

LineUnavailableException

.

**Parameters:** format

- the format of the supplied audio data
**Parameters:** data

- a byte array containing audio data to load into the clip
**Parameters:** offset

- the point at which to start copying, expressed in

bytes

from the beginning of the array
**Parameters:** bufferSize

- the number of

bytes

of data to load into the
clip from the array
**Throws:** LineUnavailableException

- if the line cannot be opened due to
resource restrictions
**Throws:** IllegalArgumentException

- if the buffer size does not represent an
integral number of sample frames, or if

format

is not
fully specified or invalid
**Throws:** IllegalStateException

- if the line is already open
**Throws:** SecurityException

- if the line cannot be opened due to security
restrictions
**See Also:** Line.close()

,

Line.isOpen()

,

LineListener

---

#### open

void open​(

AudioFormat

format,
byte[] data,
int offset,
int bufferSize)
throws

LineUnavailableException

Opens the clip, meaning that it should acquire any required system
resources and become operational. The clip is opened with the format and
audio data indicated. If this operation succeeds, the line is marked as
open and an

OPEN

event is dispatched to the
line's listeners.

Invoking this method on a line which is already open is illegal and may
result in an

IllegalStateException

.

Note that some lines, once closed, cannot be reopened. Attempts to reopen
such a line will always result in a

LineUnavailableException

.

Invoking this method on a line which is already open is illegal and may
result in an

IllegalStateException

.

Note that some lines, once closed, cannot be reopened. Attempts to reopen
such a line will always result in a

LineUnavailableException

.

Note that some lines, once closed, cannot be reopened. Attempts to reopen
such a line will always result in a

LineUnavailableException

.

open

```java
void open​(
AudioInputStream
stream)
throws
LineUnavailableException
,

IOException
```

Opens the clip with the format and audio data present in the provided
audio input stream. Opening a clip means that it should acquire any
required system resources and become operational. If this operation input
stream. If this operation succeeds, the line is marked open and an

OPEN

event is dispatched to the line's
listeners.

Invoking this method on a line which is already open is illegal and may
result in an

IllegalStateException

.

Note that some lines, once closed, cannot be reopened. Attempts to reopen
such a line will always result in a

LineUnavailableException

.

**Parameters:** stream

- an audio input stream from which audio data will be read
into the clip
**Throws:** LineUnavailableException

- if the line cannot be opened due to
resource restrictions
**Throws:** IOException

- if an I/O exception occurs during reading of the
stream
**Throws:** IllegalArgumentException

- if the stream's audio format is not
fully specified or invalid
**Throws:** IllegalStateException

- if the line is already open
**Throws:** SecurityException

- if the line cannot be opened due to security
restrictions
**See Also:** Line.close()

,

Line.isOpen()

,

LineListener

---

#### open

void open​(

AudioInputStream

stream)
throws

LineUnavailableException

,

IOException

Opens the clip with the format and audio data present in the provided
audio input stream. Opening a clip means that it should acquire any
required system resources and become operational. If this operation input
stream. If this operation succeeds, the line is marked open and an

OPEN

event is dispatched to the line's
listeners.

Invoking this method on a line which is already open is illegal and may
result in an

IllegalStateException

.

Note that some lines, once closed, cannot be reopened. Attempts to reopen
such a line will always result in a

LineUnavailableException

.

Invoking this method on a line which is already open is illegal and may
result in an

IllegalStateException

.

Note that some lines, once closed, cannot be reopened. Attempts to reopen
such a line will always result in a

LineUnavailableException

.

Note that some lines, once closed, cannot be reopened. Attempts to reopen
such a line will always result in a

LineUnavailableException

.

getFrameLength

```java
int getFrameLength()
```

Obtains the media length in sample frames.

**Returns:** the media length, expressed in sample frames, or

AudioSystem.NOT_SPECIFIED

if the line is not open
**See Also:** AudioSystem.NOT_SPECIFIED

---

#### getFrameLength

int getFrameLength()

Obtains the media length in sample frames.

getMicrosecondLength

```java
long getMicrosecondLength()
```

Obtains the media duration in microseconds.

**Returns:** the media duration, expressed in microseconds, or

AudioSystem.NOT_SPECIFIED

if the line is not open
**See Also:** AudioSystem.NOT_SPECIFIED

---

#### getMicrosecondLength

long getMicrosecondLength()

Obtains the media duration in microseconds.

setFramePosition

```java
void setFramePosition​(int frames)
```

Sets the media position in sample frames. The position is zero-based; the
first frame is frame number zero. When the clip begins playing the next
time, it will start by playing the frame at this position.

To obtain the current position in sample frames, use the

getFramePosition

method of

DataLine

.

**Parameters:** frames

- the desired new media position, expressed in sample frames

---

#### setFramePosition

void setFramePosition​(int frames)

Sets the media position in sample frames. The position is zero-based; the
first frame is frame number zero. When the clip begins playing the next
time, it will start by playing the frame at this position.

To obtain the current position in sample frames, use the

getFramePosition

method of

DataLine

.

To obtain the current position in sample frames, use the

getFramePosition

method of

DataLine

.

setMicrosecondPosition

```java
void setMicrosecondPosition​(long microseconds)
```

Sets the media position in microseconds. When the clip begins playing the
next time, it will start at this position. The level of precision is not
guaranteed. For example, an implementation might calculate the
microsecond position from the current frame position and the audio sample
frame rate. The precision in microseconds would then be limited to the
number of microseconds per sample frame.

To obtain the current position in microseconds, use the

getMicrosecondPosition

method of

DataLine

.

**Parameters:** microseconds

- the desired new media position, expressed in
microseconds

---

#### setMicrosecondPosition

void setMicrosecondPosition​(long microseconds)

Sets the media position in microseconds. When the clip begins playing the
next time, it will start at this position. The level of precision is not
guaranteed. For example, an implementation might calculate the
microsecond position from the current frame position and the audio sample
frame rate. The precision in microseconds would then be limited to the
number of microseconds per sample frame.

To obtain the current position in microseconds, use the

getMicrosecondPosition

method of

DataLine

.

To obtain the current position in microseconds, use the

getMicrosecondPosition

method of

DataLine

.

setLoopPoints

```java
void setLoopPoints​(int start,
int end)
```

Sets the first and last sample frames that will be played in the loop.
The ending point must be greater than or equal to the starting point, and
both must fall within the size of the loaded media. A value of 0 for the
starting point means the beginning of the loaded media. Similarly, a
value of -1 for the ending point indicates the last frame of the media.

**Parameters:** start

- the loop's starting position, in sample frames (zero-based)
**Parameters:** end

- the loop's ending position, in sample frames (zero-based), or
-1 to indicate the final frame
**Throws:** IllegalArgumentException

- if the requested loop points cannot be
set, usually because one or both falls outside the media's
duration or because the ending point is before the starting point

---

#### setLoopPoints

void setLoopPoints​(int start,
int end)

Sets the first and last sample frames that will be played in the loop.
The ending point must be greater than or equal to the starting point, and
both must fall within the size of the loaded media. A value of 0 for the
starting point means the beginning of the loaded media. Similarly, a
value of -1 for the ending point indicates the last frame of the media.

loop

```java
void loop​(int count)
```

Starts looping playback from the current position. Playback will continue
to the loop's end point, then loop back to the loop start point

count

times, and finally continue playback to the end of the
clip.

If the current position when this method is invoked is greater than the
loop end point, playback simply continues to the end of the clip without
looping.

A

count

value of 0 indicates that any current looping should
cease and playback should continue to the end of the clip. The behavior
is undefined when this method is invoked with any other value during a
loop operation.

If playback is stopped during looping, the current loop status is
cleared; the behavior of subsequent loop and start requests is not
affected by an interrupted loop operation.

**Parameters:** count

- the number of times playback should loop back from the
loop's end position to the loop's start position, or

LOOP_CONTINUOUSLY

to indicate that looping should
continue until interrupted

---

#### loop

void loop​(int count)

Starts looping playback from the current position. Playback will continue
to the loop's end point, then loop back to the loop start point

count

times, and finally continue playback to the end of the
clip.

If the current position when this method is invoked is greater than the
loop end point, playback simply continues to the end of the clip without
looping.

A

count

value of 0 indicates that any current looping should
cease and playback should continue to the end of the clip. The behavior
is undefined when this method is invoked with any other value during a
loop operation.

If playback is stopped during looping, the current loop status is
cleared; the behavior of subsequent loop and start requests is not
affected by an interrupted loop operation.

If the current position when this method is invoked is greater than the
loop end point, playback simply continues to the end of the clip without
looping.

A

count

value of 0 indicates that any current looping should
cease and playback should continue to the end of the clip. The behavior
is undefined when this method is invoked with any other value during a
loop operation.

If playback is stopped during looping, the current loop status is
cleared; the behavior of subsequent loop and start requests is not
affected by an interrupted loop operation.

A

count

value of 0 indicates that any current looping should
cease and playback should continue to the end of the clip. The behavior
is undefined when this method is invoked with any other value during a
loop operation.

If playback is stopped during looping, the current loop status is
cleared; the behavior of subsequent loop and start requests is not
affected by an interrupted loop operation.

If playback is stopped during looping, the current loop status is
cleared; the behavior of subsequent loop and start requests is not
affected by an interrupted loop operation.

---

