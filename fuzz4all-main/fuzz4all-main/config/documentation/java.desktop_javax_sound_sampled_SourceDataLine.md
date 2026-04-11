# Interface SourceDataLine

**Source:** `java.desktop\javax\sound\sampled\SourceDataLine.html`

### Class Description

```java
public interface
SourceDataLine

extends
DataLine
```

A source data line is a data line to which data may be written. It acts as a
source to its mixer. An application writes audio bytes to a source data line,
which handles the buffering of the bytes and delivers them to the mixer. The
mixer may mix the samples with those from other sources and then deliver the
mix to a target such as an output port (which may represent an audio output
device on a sound card).

Note that the naming convention for this interface reflects the relationship
between the line and its mixer. From the perspective of an application, a
source data line may act as a target for audio data.

A source data line can be obtained from a mixer by invoking the

getLine

method of

Mixer

with an appropriate

DataLine.Info

object.

The

SourceDataLine

interface provides a method for writing audio data
to the data line's buffer. Applications that play or mix audio should write
data to the source data line quickly enough to keep the buffer from
underflowing (emptying), which could cause discontinuities in the audio that
are perceived as clicks. Applications can use the

available

method defined in the

DataLine

interface to determine the amount of data currently queued in the data line's
buffer. The amount of data which can be written to the buffer without
blocking is the difference between the buffer size and the amount of queued
data. If the delivery of audio output stops due to underflow, a

STOP

event is generated. A

START

event is generated when the audio output
resumes.

**All Superinterfaces:** AutoCloseable

,

DataLine

,

Line

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### void open​(
AudioFormat
format,
int bufferSize)
throws
LineUnavailableException

Opens the line with the specified format and suggested buffer size,
causing the line to acquire any required system resources and become
operational.

The buffer size is specified in bytes, but must represent an integral
number of sample frames. Invoking this method with a requested buffer
size that does not meet this requirement may result in an

IllegalArgumentException

. The actual buffer size for the open
line may differ from the requested buffer size. The value actually set
may be queried by subsequently calling

DataLine.getBufferSize()

.

If this operation succeeds, the line is marked as open, and an

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
- format

- the desired audio format
- bufferSize

- the desired buffer size

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
- open(AudioFormat)

,

Line.open()

,

Line.close()

,

Line.isOpen()

,

LineEvent

---

#### void open​(
AudioFormat
format)
throws
LineUnavailableException

Opens the line with the specified format, causing the line to acquire any
required system resources and become operational.

The implementation chooses a buffer size, which is measured in bytes but
which encompasses an integral number of sample frames. The buffer size
that the system has chosen may be queried by subsequently calling

DataLine.getBufferSize()

.

If this operation succeeds, the line is marked as open, and an

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
- format

- the desired audio format

**Throws:**
- LineUnavailableException

- if the line cannot be opened due to
resource restrictions
- IllegalArgumentException

- if

format

is not fully specified
or invalid
- IllegalStateException

- if the line is already open
- SecurityException

- if the line cannot be opened due to security
restrictions

**See Also:**
- open(AudioFormat, int)

,

Line.open()

,

Line.close()

,

Line.isOpen()

,

LineEvent

---

#### int write​(byte[] b,
int off,
int len)

Writes audio data to the mixer via this source data line. The requested
number of bytes of data are read from the specified array, starting at
the given offset into the array, and written to the data line's buffer.
If the caller attempts to write more data than can currently be written
(see

available

), this method blocks until the
requested amount of data has been written. This applies even if the
requested amount of data to write is greater than the data line's buffer
size. However, if the data line is closed, stopped, or flushed before the
requested amount has been written, the method no longer blocks, but
returns the number of bytes written thus far.

The number of bytes that can be written without blocking can be
ascertained using the

available

method of the

DataLine

interface. (While it is guaranteed that this number of
bytes can be written without blocking, there is no guarantee that
attempts to write additional data will block.)

The number of bytes to write must represent an integral number of sample
frames, such that:

[ bytes written ] % [frame size in bytes ] == 0

The return value will always meet this requirement. A request to write a
number of bytes representing a non-integral number of sample frames
cannot be fulfilled and may result in an

IllegalArgumentException

.

**Parameters:**
- b

- a byte array containing data to be written to the data line
- off

- the offset from the beginning of the array, in bytes
- len

- the length, in bytes, of the valid data in the array (in
other words, the requested amount of data to write, in bytes)

**Returns:**
- the number of bytes actually written

**Throws:**
- IllegalArgumentException

- if the requested number of bytes does
not represent an integral number of sample frames, or if

len

is negative
- ArrayIndexOutOfBoundsException

- if

off

is negative, or

off+len

is greater than the length of the array

b

**See Also:**
- TargetDataLine.read(byte[], int, int)

,

DataLine.available()

---

### Additional Sections

#### Interface SourceDataLine

**All Superinterfaces:** AutoCloseable

,

DataLine

,

Line

```java
public interface
SourceDataLine

extends
DataLine
```

A source data line is a data line to which data may be written. It acts as a
source to its mixer. An application writes audio bytes to a source data line,
which handles the buffering of the bytes and delivers them to the mixer. The
mixer may mix the samples with those from other sources and then deliver the
mix to a target such as an output port (which may represent an audio output
device on a sound card).

Note that the naming convention for this interface reflects the relationship
between the line and its mixer. From the perspective of an application, a
source data line may act as a target for audio data.

A source data line can be obtained from a mixer by invoking the

getLine

method of

Mixer

with an appropriate

DataLine.Info

object.

The

SourceDataLine

interface provides a method for writing audio data
to the data line's buffer. Applications that play or mix audio should write
data to the source data line quickly enough to keep the buffer from
underflowing (emptying), which could cause discontinuities in the audio that
are perceived as clicks. Applications can use the

available

method defined in the

DataLine

interface to determine the amount of data currently queued in the data line's
buffer. The amount of data which can be written to the buffer without
blocking is the difference between the buffer size and the amount of queued
data. If the delivery of audio output stops due to underflow, a

STOP

event is generated. A

START

event is generated when the audio output
resumes.

**Since:** 1.3
**See Also:** Mixer

,

DataLine

,

TargetDataLine

public interface

SourceDataLine

extends

DataLine

A source data line is a data line to which data may be written. It acts as a
source to its mixer. An application writes audio bytes to a source data line,
which handles the buffering of the bytes and delivers them to the mixer. The
mixer may mix the samples with those from other sources and then deliver the
mix to a target such as an output port (which may represent an audio output
device on a sound card).

Note that the naming convention for this interface reflects the relationship
between the line and its mixer. From the perspective of an application, a
source data line may act as a target for audio data.

A source data line can be obtained from a mixer by invoking the

getLine

method of

Mixer

with an appropriate

DataLine.Info

object.

The

SourceDataLine

interface provides a method for writing audio data
to the data line's buffer. Applications that play or mix audio should write
data to the source data line quickly enough to keep the buffer from
underflowing (emptying), which could cause discontinuities in the audio that
are perceived as clicks. Applications can use the

available

method defined in the

DataLine

interface to determine the amount of data currently queued in the data line's
buffer. The amount of data which can be written to the buffer without
blocking is the difference between the buffer size and the amount of queued
data. If the delivery of audio output stops due to underflow, a

STOP

event is generated. A

START

event is generated when the audio output
resumes.

Note that the naming convention for this interface reflects the relationship
between the line and its mixer. From the perspective of an application, a
source data line may act as a target for audio data.

A source data line can be obtained from a mixer by invoking the

getLine

method of

Mixer

with an appropriate

DataLine.Info

object.

The

SourceDataLine

interface provides a method for writing audio data
to the data line's buffer. Applications that play or mix audio should write
data to the source data line quickly enough to keep the buffer from
underflowing (emptying), which could cause discontinuities in the audio that
are perceived as clicks. Applications can use the

available

method defined in the

DataLine

interface to determine the amount of data currently queued in the data line's
buffer. The amount of data which can be written to the buffer without
blocking is the difference between the buffer size and the amount of queued
data. If the delivery of audio output stops due to underflow, a

STOP

event is generated. A

START

event is generated when the audio output
resumes.

A source data line can be obtained from a mixer by invoking the

getLine

method of

Mixer

with an appropriate

DataLine.Info

object.

The

SourceDataLine

interface provides a method for writing audio data
to the data line's buffer. Applications that play or mix audio should write
data to the source data line quickly enough to keep the buffer from
underflowing (emptying), which could cause discontinuities in the audio that
are perceived as clicks. Applications can use the

available

method defined in the

DataLine

interface to determine the amount of data currently queued in the data line's
buffer. The amount of data which can be written to the buffer without
blocking is the difference between the buffer size and the amount of queued
data. If the delivery of audio output stops due to underflow, a

STOP

event is generated. A

START

event is generated when the audio output
resumes.

The

SourceDataLine

interface provides a method for writing audio data
to the data line's buffer. Applications that play or mix audio should write
data to the source data line quickly enough to keep the buffer from
underflowing (emptying), which could cause discontinuities in the audio that
are perceived as clicks. Applications can use the

available

method defined in the

DataLine

interface to determine the amount of data currently queued in the data line's
buffer. The amount of data which can be written to the buffer without
blocking is the difference between the buffer size and the amount of queued
data. If the delivery of audio output stops due to underflow, a

STOP

event is generated. A

START

event is generated when the audio output
resumes.

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

- Nested classes/interfaces declared in interface javax.sound.sampled.

DataLine

DataLine.Info

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

open

​(

AudioFormat

format)

Opens the line with the specified format, causing the line to acquire any
required system resources and become operational.

void

open

​(

AudioFormat

format,
int bufferSize)

Opens the line with the specified format and suggested buffer size,
causing the line to acquire any required system resources and become
operational.

int

write

​(byte[] b,
int off,
int len)

Writes audio data to the mixer via this source data line.

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

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

open

​(

AudioFormat

format)

Opens the line with the specified format, causing the line to acquire any
required system resources and become operational.

void

open

​(

AudioFormat

format,
int bufferSize)

Opens the line with the specified format and suggested buffer size,
causing the line to acquire any required system resources and become
operational.

int

write

​(byte[] b,
int off,
int len)

Writes audio data to the mixer via this source data line.

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

Opens the line with the specified format, causing the line to acquire any
required system resources and become operational.

Opens the line with the specified format and suggested buffer size,
causing the line to acquire any required system resources and become
operational.

Writes audio data to the mixer via this source data line.

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

============ METHOD DETAIL ==========

- Method Detail

- open

```java
void open​(
AudioFormat
format,
int bufferSize)
throws
LineUnavailableException
```

Opens the line with the specified format and suggested buffer size,
causing the line to acquire any required system resources and become
operational.

The buffer size is specified in bytes, but must represent an integral
number of sample frames. Invoking this method with a requested buffer
size that does not meet this requirement may result in an

IllegalArgumentException

. The actual buffer size for the open
line may differ from the requested buffer size. The value actually set
may be queried by subsequently calling

DataLine.getBufferSize()

.

If this operation succeeds, the line is marked as open, and an

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

**Parameters:** format

- the desired audio format
**Parameters:** bufferSize

- the desired buffer size
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
**See Also:** open(AudioFormat)

,

Line.open()

,

Line.close()

,

Line.isOpen()

,

LineEvent

- open

```java
void open​(
AudioFormat
format)
throws
LineUnavailableException
```

Opens the line with the specified format, causing the line to acquire any
required system resources and become operational.

The implementation chooses a buffer size, which is measured in bytes but
which encompasses an integral number of sample frames. The buffer size
that the system has chosen may be queried by subsequently calling

DataLine.getBufferSize()

.

If this operation succeeds, the line is marked as open, and an

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

**Parameters:** format

- the desired audio format
**Throws:** LineUnavailableException

- if the line cannot be opened due to
resource restrictions
**Throws:** IllegalArgumentException

- if

format

is not fully specified
or invalid
**Throws:** IllegalStateException

- if the line is already open
**Throws:** SecurityException

- if the line cannot be opened due to security
restrictions
**See Also:** open(AudioFormat, int)

,

Line.open()

,

Line.close()

,

Line.isOpen()

,

LineEvent

- write

```java
int write​(byte[] b,
int off,
int len)
```

Writes audio data to the mixer via this source data line. The requested
number of bytes of data are read from the specified array, starting at
the given offset into the array, and written to the data line's buffer.
If the caller attempts to write more data than can currently be written
(see

available

), this method blocks until the
requested amount of data has been written. This applies even if the
requested amount of data to write is greater than the data line's buffer
size. However, if the data line is closed, stopped, or flushed before the
requested amount has been written, the method no longer blocks, but
returns the number of bytes written thus far.

The number of bytes that can be written without blocking can be
ascertained using the

available

method of the

DataLine

interface. (While it is guaranteed that this number of
bytes can be written without blocking, there is no guarantee that
attempts to write additional data will block.)

The number of bytes to write must represent an integral number of sample
frames, such that:

[ bytes written ] % [frame size in bytes ] == 0

The return value will always meet this requirement. A request to write a
number of bytes representing a non-integral number of sample frames
cannot be fulfilled and may result in an

IllegalArgumentException

.

**Parameters:** b

- a byte array containing data to be written to the data line
**Parameters:** off

- the offset from the beginning of the array, in bytes
**Parameters:** len

- the length, in bytes, of the valid data in the array (in
other words, the requested amount of data to write, in bytes)
**Returns:** the number of bytes actually written
**Throws:** IllegalArgumentException

- if the requested number of bytes does
not represent an integral number of sample frames, or if

len

is negative
**Throws:** ArrayIndexOutOfBoundsException

- if

off

is negative, or

off+len

is greater than the length of the array

b
**See Also:** TargetDataLine.read(byte[], int, int)

,

DataLine.available()

Method Detail

- open

```java
void open​(
AudioFormat
format,
int bufferSize)
throws
LineUnavailableException
```

Opens the line with the specified format and suggested buffer size,
causing the line to acquire any required system resources and become
operational.

The buffer size is specified in bytes, but must represent an integral
number of sample frames. Invoking this method with a requested buffer
size that does not meet this requirement may result in an

IllegalArgumentException

. The actual buffer size for the open
line may differ from the requested buffer size. The value actually set
may be queried by subsequently calling

DataLine.getBufferSize()

.

If this operation succeeds, the line is marked as open, and an

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

**Parameters:** format

- the desired audio format
**Parameters:** bufferSize

- the desired buffer size
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
**See Also:** open(AudioFormat)

,

Line.open()

,

Line.close()

,

Line.isOpen()

,

LineEvent

- open

```java
void open​(
AudioFormat
format)
throws
LineUnavailableException
```

Opens the line with the specified format, causing the line to acquire any
required system resources and become operational.

The implementation chooses a buffer size, which is measured in bytes but
which encompasses an integral number of sample frames. The buffer size
that the system has chosen may be queried by subsequently calling

DataLine.getBufferSize()

.

If this operation succeeds, the line is marked as open, and an

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

**Parameters:** format

- the desired audio format
**Throws:** LineUnavailableException

- if the line cannot be opened due to
resource restrictions
**Throws:** IllegalArgumentException

- if

format

is not fully specified
or invalid
**Throws:** IllegalStateException

- if the line is already open
**Throws:** SecurityException

- if the line cannot be opened due to security
restrictions
**See Also:** open(AudioFormat, int)

,

Line.open()

,

Line.close()

,

Line.isOpen()

,

LineEvent

- write

```java
int write​(byte[] b,
int off,
int len)
```

Writes audio data to the mixer via this source data line. The requested
number of bytes of data are read from the specified array, starting at
the given offset into the array, and written to the data line's buffer.
If the caller attempts to write more data than can currently be written
(see

available

), this method blocks until the
requested amount of data has been written. This applies even if the
requested amount of data to write is greater than the data line's buffer
size. However, if the data line is closed, stopped, or flushed before the
requested amount has been written, the method no longer blocks, but
returns the number of bytes written thus far.

The number of bytes that can be written without blocking can be
ascertained using the

available

method of the

DataLine

interface. (While it is guaranteed that this number of
bytes can be written without blocking, there is no guarantee that
attempts to write additional data will block.)

The number of bytes to write must represent an integral number of sample
frames, such that:

[ bytes written ] % [frame size in bytes ] == 0

The return value will always meet this requirement. A request to write a
number of bytes representing a non-integral number of sample frames
cannot be fulfilled and may result in an

IllegalArgumentException

.

**Parameters:** b

- a byte array containing data to be written to the data line
**Parameters:** off

- the offset from the beginning of the array, in bytes
**Parameters:** len

- the length, in bytes, of the valid data in the array (in
other words, the requested amount of data to write, in bytes)
**Returns:** the number of bytes actually written
**Throws:** IllegalArgumentException

- if the requested number of bytes does
not represent an integral number of sample frames, or if

len

is negative
**Throws:** ArrayIndexOutOfBoundsException

- if

off

is negative, or

off+len

is greater than the length of the array

b
**See Also:** TargetDataLine.read(byte[], int, int)

,

DataLine.available()

---

#### Method Detail

open

```java
void open​(
AudioFormat
format,
int bufferSize)
throws
LineUnavailableException
```

Opens the line with the specified format and suggested buffer size,
causing the line to acquire any required system resources and become
operational.

The buffer size is specified in bytes, but must represent an integral
number of sample frames. Invoking this method with a requested buffer
size that does not meet this requirement may result in an

IllegalArgumentException

. The actual buffer size for the open
line may differ from the requested buffer size. The value actually set
may be queried by subsequently calling

DataLine.getBufferSize()

.

If this operation succeeds, the line is marked as open, and an

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

**Parameters:** format

- the desired audio format
**Parameters:** bufferSize

- the desired buffer size
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
**See Also:** open(AudioFormat)

,

Line.open()

,

Line.close()

,

Line.isOpen()

,

LineEvent

---

#### open

void open​(

AudioFormat

format,
int bufferSize)
throws

LineUnavailableException

Opens the line with the specified format and suggested buffer size,
causing the line to acquire any required system resources and become
operational.

The buffer size is specified in bytes, but must represent an integral
number of sample frames. Invoking this method with a requested buffer
size that does not meet this requirement may result in an

IllegalArgumentException

. The actual buffer size for the open
line may differ from the requested buffer size. The value actually set
may be queried by subsequently calling

DataLine.getBufferSize()

.

If this operation succeeds, the line is marked as open, and an

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

The buffer size is specified in bytes, but must represent an integral
number of sample frames. Invoking this method with a requested buffer
size that does not meet this requirement may result in an

IllegalArgumentException

. The actual buffer size for the open
line may differ from the requested buffer size. The value actually set
may be queried by subsequently calling

DataLine.getBufferSize()

.

If this operation succeeds, the line is marked as open, and an

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

If this operation succeeds, the line is marked as open, and an

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

open

```java
void open​(
AudioFormat
format)
throws
LineUnavailableException
```

Opens the line with the specified format, causing the line to acquire any
required system resources and become operational.

The implementation chooses a buffer size, which is measured in bytes but
which encompasses an integral number of sample frames. The buffer size
that the system has chosen may be queried by subsequently calling

DataLine.getBufferSize()

.

If this operation succeeds, the line is marked as open, and an

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

**Parameters:** format

- the desired audio format
**Throws:** LineUnavailableException

- if the line cannot be opened due to
resource restrictions
**Throws:** IllegalArgumentException

- if

format

is not fully specified
or invalid
**Throws:** IllegalStateException

- if the line is already open
**Throws:** SecurityException

- if the line cannot be opened due to security
restrictions
**See Also:** open(AudioFormat, int)

,

Line.open()

,

Line.close()

,

Line.isOpen()

,

LineEvent

---

#### open

void open​(

AudioFormat

format)
throws

LineUnavailableException

Opens the line with the specified format, causing the line to acquire any
required system resources and become operational.

The implementation chooses a buffer size, which is measured in bytes but
which encompasses an integral number of sample frames. The buffer size
that the system has chosen may be queried by subsequently calling

DataLine.getBufferSize()

.

If this operation succeeds, the line is marked as open, and an

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

The implementation chooses a buffer size, which is measured in bytes but
which encompasses an integral number of sample frames. The buffer size
that the system has chosen may be queried by subsequently calling

DataLine.getBufferSize()

.

If this operation succeeds, the line is marked as open, and an

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

If this operation succeeds, the line is marked as open, and an

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

write

```java
int write​(byte[] b,
int off,
int len)
```

Writes audio data to the mixer via this source data line. The requested
number of bytes of data are read from the specified array, starting at
the given offset into the array, and written to the data line's buffer.
If the caller attempts to write more data than can currently be written
(see

available

), this method blocks until the
requested amount of data has been written. This applies even if the
requested amount of data to write is greater than the data line's buffer
size. However, if the data line is closed, stopped, or flushed before the
requested amount has been written, the method no longer blocks, but
returns the number of bytes written thus far.

The number of bytes that can be written without blocking can be
ascertained using the

available

method of the

DataLine

interface. (While it is guaranteed that this number of
bytes can be written without blocking, there is no guarantee that
attempts to write additional data will block.)

The number of bytes to write must represent an integral number of sample
frames, such that:

[ bytes written ] % [frame size in bytes ] == 0

The return value will always meet this requirement. A request to write a
number of bytes representing a non-integral number of sample frames
cannot be fulfilled and may result in an

IllegalArgumentException

.

**Parameters:** b

- a byte array containing data to be written to the data line
**Parameters:** off

- the offset from the beginning of the array, in bytes
**Parameters:** len

- the length, in bytes, of the valid data in the array (in
other words, the requested amount of data to write, in bytes)
**Returns:** the number of bytes actually written
**Throws:** IllegalArgumentException

- if the requested number of bytes does
not represent an integral number of sample frames, or if

len

is negative
**Throws:** ArrayIndexOutOfBoundsException

- if

off

is negative, or

off+len

is greater than the length of the array

b
**See Also:** TargetDataLine.read(byte[], int, int)

,

DataLine.available()

---

#### write

int write​(byte[] b,
int off,
int len)

Writes audio data to the mixer via this source data line. The requested
number of bytes of data are read from the specified array, starting at
the given offset into the array, and written to the data line's buffer.
If the caller attempts to write more data than can currently be written
(see

available

), this method blocks until the
requested amount of data has been written. This applies even if the
requested amount of data to write is greater than the data line's buffer
size. However, if the data line is closed, stopped, or flushed before the
requested amount has been written, the method no longer blocks, but
returns the number of bytes written thus far.

The number of bytes that can be written without blocking can be
ascertained using the

available

method of the

DataLine

interface. (While it is guaranteed that this number of
bytes can be written without blocking, there is no guarantee that
attempts to write additional data will block.)

The number of bytes to write must represent an integral number of sample
frames, such that:

[ bytes written ] % [frame size in bytes ] == 0

The return value will always meet this requirement. A request to write a
number of bytes representing a non-integral number of sample frames
cannot be fulfilled and may result in an

IllegalArgumentException

.

The number of bytes that can be written without blocking can be
ascertained using the

available

method of the

DataLine

interface. (While it is guaranteed that this number of
bytes can be written without blocking, there is no guarantee that
attempts to write additional data will block.)

The number of bytes to write must represent an integral number of sample
frames, such that:

[ bytes written ] % [frame size in bytes ] == 0

The return value will always meet this requirement. A request to write a
number of bytes representing a non-integral number of sample frames
cannot be fulfilled and may result in an

IllegalArgumentException

.

The number of bytes to write must represent an integral number of sample
frames, such that:

[ bytes written ] % [frame size in bytes ] == 0

The return value will always meet this requirement. A request to write a
number of bytes representing a non-integral number of sample frames
cannot be fulfilled and may result in an

IllegalArgumentException

.

[ bytes written ] % [frame size in bytes ] == 0

The return value will always meet this requirement. A request to write a
number of bytes representing a non-integral number of sample frames
cannot be fulfilled and may result in an

IllegalArgumentException

.

The return value will always meet this requirement. A request to write a
number of bytes representing a non-integral number of sample frames
cannot be fulfilled and may result in an

IllegalArgumentException

.

---

