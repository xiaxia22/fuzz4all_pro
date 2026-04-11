# Interface TargetDataLine

**Source:** `java.desktop\javax\sound\sampled\TargetDataLine.html`

### Class Description

```java
public interface
TargetDataLine

extends
DataLine
```

A target data line is a type of

DataLine

from which audio data can be
read. The most common example is a data line that gets its data from an audio
capture device. (The device is implemented as a mixer that writes to the
target data line.)

Note that the naming convention for this interface reflects the relationship
between the line and its mixer. From the perspective of an application, a
target data line may act as a source for audio data.

The target data line can be obtained from a mixer by invoking the

getLine

method of

Mixer

with an appropriate

DataLine.Info

object.

The

TargetDataLine

interface provides a method for reading the
captured data from the target data line's buffer. Applications that record
audio should read data from the target data line quickly enough to keep the
buffer from overflowing, which could cause discontinuities in the captured
data that are perceived as clicks. Applications can use the

available

method defined in the

DataLine

interface to determine the amount of data currently queued in the data line's
buffer. If the buffer does overflow, the oldest queued data is discarded and
replaced by new data.

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

Opens the line with the specified format and requested buffer size,
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

If this operation succeeds, the line is marked as open, and an

OPEN

event is dispatched to the line's
listeners.

Invoking this method on a line that is already open is illegal and may
result in an

IllegalStateException

.

Some lines, once closed, cannot be reopened. Attempts to reopen such a
line will always result in a

LineUnavailableException

.

**Parameters:**
- format

- the desired audio format
- bufferSize

- the desired buffer size, in bytes

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

If this operation succeeds, the line is marked as open, and an

OPEN

event is dispatched to the line's
listeners.

Invoking this method on a line that is already open is illegal and may
result in an

IllegalStateException

.

Some lines, once closed, cannot be reopened. Attempts to reopen such a
line will always result in a

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

#### int read​(byte[] b,
int off,
int len)

Reads audio data from the data line's input buffer. The requested number
of bytes is read into the specified array, starting at the specified
offset into the array in bytes. This method blocks until the requested
amount of data has been read. However, if the data line is closed,
stopped, drained, or flushed before the requested amount has been read,
the method no longer blocks, but returns the number of bytes read thus
far.

The number of bytes that can be read without blocking can be ascertained
using the

available

method of the

DataLine

interface. (While it is guaranteed that this number of
bytes can be read without blocking, there is no guarantee that attempts
to read additional data will block.)

The number of bytes to be read must represent an integral number of
sample frames, such that:

[ bytes read ] % [frame size in bytes ] == 0

The return value will always meet this requirement. A request to read a
number of bytes representing a non-integral number of sample frames
cannot be fulfilled and may result in an IllegalArgumentException.

**Parameters:**
- b

- a byte array that will contain the requested input data when
this method returns
- off

- the offset from the beginning of the array, in bytes
- len

- the requested number of bytes to read

**Returns:**
- the number of bytes actually read

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
- SourceDataLine.write(byte[], int, int)

,

DataLine.available()

---

### Additional Sections

#### Interface TargetDataLine

**All Superinterfaces:** AutoCloseable

,

DataLine

,

Line

```java
public interface
TargetDataLine

extends
DataLine
```

A target data line is a type of

DataLine

from which audio data can be
read. The most common example is a data line that gets its data from an audio
capture device. (The device is implemented as a mixer that writes to the
target data line.)

Note that the naming convention for this interface reflects the relationship
between the line and its mixer. From the perspective of an application, a
target data line may act as a source for audio data.

The target data line can be obtained from a mixer by invoking the

getLine

method of

Mixer

with an appropriate

DataLine.Info

object.

The

TargetDataLine

interface provides a method for reading the
captured data from the target data line's buffer. Applications that record
audio should read data from the target data line quickly enough to keep the
buffer from overflowing, which could cause discontinuities in the captured
data that are perceived as clicks. Applications can use the

available

method defined in the

DataLine

interface to determine the amount of data currently queued in the data line's
buffer. If the buffer does overflow, the oldest queued data is discarded and
replaced by new data.

**Since:** 1.3
**See Also:** Mixer

,

DataLine

,

SourceDataLine

public interface

TargetDataLine

extends

DataLine

A target data line is a type of

DataLine

from which audio data can be
read. The most common example is a data line that gets its data from an audio
capture device. (The device is implemented as a mixer that writes to the
target data line.)

Note that the naming convention for this interface reflects the relationship
between the line and its mixer. From the perspective of an application, a
target data line may act as a source for audio data.

The target data line can be obtained from a mixer by invoking the

getLine

method of

Mixer

with an appropriate

DataLine.Info

object.

The

TargetDataLine

interface provides a method for reading the
captured data from the target data line's buffer. Applications that record
audio should read data from the target data line quickly enough to keep the
buffer from overflowing, which could cause discontinuities in the captured
data that are perceived as clicks. Applications can use the

available

method defined in the

DataLine

interface to determine the amount of data currently queued in the data line's
buffer. If the buffer does overflow, the oldest queued data is discarded and
replaced by new data.

Note that the naming convention for this interface reflects the relationship
between the line and its mixer. From the perspective of an application, a
target data line may act as a source for audio data.

The target data line can be obtained from a mixer by invoking the

getLine

method of

Mixer

with an appropriate

DataLine.Info

object.

The

TargetDataLine

interface provides a method for reading the
captured data from the target data line's buffer. Applications that record
audio should read data from the target data line quickly enough to keep the
buffer from overflowing, which could cause discontinuities in the captured
data that are perceived as clicks. Applications can use the

available

method defined in the

DataLine

interface to determine the amount of data currently queued in the data line's
buffer. If the buffer does overflow, the oldest queued data is discarded and
replaced by new data.

The target data line can be obtained from a mixer by invoking the

getLine

method of

Mixer

with an appropriate

DataLine.Info

object.

The

TargetDataLine

interface provides a method for reading the
captured data from the target data line's buffer. Applications that record
audio should read data from the target data line quickly enough to keep the
buffer from overflowing, which could cause discontinuities in the captured
data that are perceived as clicks. Applications can use the

available

method defined in the

DataLine

interface to determine the amount of data currently queued in the data line's
buffer. If the buffer does overflow, the oldest queued data is discarded and
replaced by new data.

The

TargetDataLine

interface provides a method for reading the
captured data from the target data line's buffer. Applications that record
audio should read data from the target data line quickly enough to keep the
buffer from overflowing, which could cause discontinuities in the captured
data that are perceived as clicks. Applications can use the

available

method defined in the

DataLine

interface to determine the amount of data currently queued in the data line's
buffer. If the buffer does overflow, the oldest queued data is discarded and
replaced by new data.

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

Opens the line with the specified format and requested buffer size,
causing the line to acquire any required system resources and become
operational.

int

read

​(byte[] b,
int off,
int len)

Reads audio data from the data line's input buffer.

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

Opens the line with the specified format and requested buffer size,
causing the line to acquire any required system resources and become
operational.

int

read

​(byte[] b,
int off,
int len)

Reads audio data from the data line's input buffer.

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

Opens the line with the specified format and requested buffer size,
causing the line to acquire any required system resources and become
operational.

Reads audio data from the data line's input buffer.

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

Opens the line with the specified format and requested buffer size,
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

If this operation succeeds, the line is marked as open, and an

OPEN

event is dispatched to the line's
listeners.

Invoking this method on a line that is already open is illegal and may
result in an

IllegalStateException

.

Some lines, once closed, cannot be reopened. Attempts to reopen such a
line will always result in a

LineUnavailableException

.

**Parameters:** format

- the desired audio format
**Parameters:** bufferSize

- the desired buffer size, in bytes
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

If this operation succeeds, the line is marked as open, and an

OPEN

event is dispatched to the line's
listeners.

Invoking this method on a line that is already open is illegal and may
result in an

IllegalStateException

.

Some lines, once closed, cannot be reopened. Attempts to reopen such a
line will always result in a

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

- read

```java
int read​(byte[] b,
int off,
int len)
```

Reads audio data from the data line's input buffer. The requested number
of bytes is read into the specified array, starting at the specified
offset into the array in bytes. This method blocks until the requested
amount of data has been read. However, if the data line is closed,
stopped, drained, or flushed before the requested amount has been read,
the method no longer blocks, but returns the number of bytes read thus
far.

The number of bytes that can be read without blocking can be ascertained
using the

available

method of the

DataLine

interface. (While it is guaranteed that this number of
bytes can be read without blocking, there is no guarantee that attempts
to read additional data will block.)

The number of bytes to be read must represent an integral number of
sample frames, such that:

[ bytes read ] % [frame size in bytes ] == 0

The return value will always meet this requirement. A request to read a
number of bytes representing a non-integral number of sample frames
cannot be fulfilled and may result in an IllegalArgumentException.

**Parameters:** b

- a byte array that will contain the requested input data when
this method returns
**Parameters:** off

- the offset from the beginning of the array, in bytes
**Parameters:** len

- the requested number of bytes to read
**Returns:** the number of bytes actually read
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
**See Also:** SourceDataLine.write(byte[], int, int)

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

Opens the line with the specified format and requested buffer size,
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

If this operation succeeds, the line is marked as open, and an

OPEN

event is dispatched to the line's
listeners.

Invoking this method on a line that is already open is illegal and may
result in an

IllegalStateException

.

Some lines, once closed, cannot be reopened. Attempts to reopen such a
line will always result in a

LineUnavailableException

.

**Parameters:** format

- the desired audio format
**Parameters:** bufferSize

- the desired buffer size, in bytes
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

If this operation succeeds, the line is marked as open, and an

OPEN

event is dispatched to the line's
listeners.

Invoking this method on a line that is already open is illegal and may
result in an

IllegalStateException

.

Some lines, once closed, cannot be reopened. Attempts to reopen such a
line will always result in a

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

- read

```java
int read​(byte[] b,
int off,
int len)
```

Reads audio data from the data line's input buffer. The requested number
of bytes is read into the specified array, starting at the specified
offset into the array in bytes. This method blocks until the requested
amount of data has been read. However, if the data line is closed,
stopped, drained, or flushed before the requested amount has been read,
the method no longer blocks, but returns the number of bytes read thus
far.

The number of bytes that can be read without blocking can be ascertained
using the

available

method of the

DataLine

interface. (While it is guaranteed that this number of
bytes can be read without blocking, there is no guarantee that attempts
to read additional data will block.)

The number of bytes to be read must represent an integral number of
sample frames, such that:

[ bytes read ] % [frame size in bytes ] == 0

The return value will always meet this requirement. A request to read a
number of bytes representing a non-integral number of sample frames
cannot be fulfilled and may result in an IllegalArgumentException.

**Parameters:** b

- a byte array that will contain the requested input data when
this method returns
**Parameters:** off

- the offset from the beginning of the array, in bytes
**Parameters:** len

- the requested number of bytes to read
**Returns:** the number of bytes actually read
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
**See Also:** SourceDataLine.write(byte[], int, int)

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

Opens the line with the specified format and requested buffer size,
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

If this operation succeeds, the line is marked as open, and an

OPEN

event is dispatched to the line's
listeners.

Invoking this method on a line that is already open is illegal and may
result in an

IllegalStateException

.

Some lines, once closed, cannot be reopened. Attempts to reopen such a
line will always result in a

LineUnavailableException

.

**Parameters:** format

- the desired audio format
**Parameters:** bufferSize

- the desired buffer size, in bytes
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

Opens the line with the specified format and requested buffer size,
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

If this operation succeeds, the line is marked as open, and an

OPEN

event is dispatched to the line's
listeners.

Invoking this method on a line that is already open is illegal and may
result in an

IllegalStateException

.

Some lines, once closed, cannot be reopened. Attempts to reopen such a
line will always result in a

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

If this operation succeeds, the line is marked as open, and an

OPEN

event is dispatched to the line's
listeners.

Invoking this method on a line that is already open is illegal and may
result in an

IllegalStateException

.

Some lines, once closed, cannot be reopened. Attempts to reopen such a
line will always result in a

LineUnavailableException

.

If this operation succeeds, the line is marked as open, and an

OPEN

event is dispatched to the line's
listeners.

Invoking this method on a line that is already open is illegal and may
result in an

IllegalStateException

.

Some lines, once closed, cannot be reopened. Attempts to reopen such a
line will always result in a

LineUnavailableException

.

Invoking this method on a line that is already open is illegal and may
result in an

IllegalStateException

.

Some lines, once closed, cannot be reopened. Attempts to reopen such a
line will always result in a

LineUnavailableException

.

Some lines, once closed, cannot be reopened. Attempts to reopen such a
line will always result in a

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

If this operation succeeds, the line is marked as open, and an

OPEN

event is dispatched to the line's
listeners.

Invoking this method on a line that is already open is illegal and may
result in an

IllegalStateException

.

Some lines, once closed, cannot be reopened. Attempts to reopen such a
line will always result in a

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

If this operation succeeds, the line is marked as open, and an

OPEN

event is dispatched to the line's
listeners.

Invoking this method on a line that is already open is illegal and may
result in an

IllegalStateException

.

Some lines, once closed, cannot be reopened. Attempts to reopen such a
line will always result in a

LineUnavailableException

.

The implementation chooses a buffer size, which is measured in bytes but
which encompasses an integral number of sample frames. The buffer size
that the system has chosen may be queried by subsequently calling

DataLine.getBufferSize()

If this operation succeeds, the line is marked as open, and an

OPEN

event is dispatched to the line's
listeners.

Invoking this method on a line that is already open is illegal and may
result in an

IllegalStateException

.

Some lines, once closed, cannot be reopened. Attempts to reopen such a
line will always result in a

LineUnavailableException

.

If this operation succeeds, the line is marked as open, and an

OPEN

event is dispatched to the line's
listeners.

Invoking this method on a line that is already open is illegal and may
result in an

IllegalStateException

.

Some lines, once closed, cannot be reopened. Attempts to reopen such a
line will always result in a

LineUnavailableException

.

Invoking this method on a line that is already open is illegal and may
result in an

IllegalStateException

.

Some lines, once closed, cannot be reopened. Attempts to reopen such a
line will always result in a

LineUnavailableException

.

Some lines, once closed, cannot be reopened. Attempts to reopen such a
line will always result in a

LineUnavailableException

.

read

```java
int read​(byte[] b,
int off,
int len)
```

Reads audio data from the data line's input buffer. The requested number
of bytes is read into the specified array, starting at the specified
offset into the array in bytes. This method blocks until the requested
amount of data has been read. However, if the data line is closed,
stopped, drained, or flushed before the requested amount has been read,
the method no longer blocks, but returns the number of bytes read thus
far.

The number of bytes that can be read without blocking can be ascertained
using the

available

method of the

DataLine

interface. (While it is guaranteed that this number of
bytes can be read without blocking, there is no guarantee that attempts
to read additional data will block.)

The number of bytes to be read must represent an integral number of
sample frames, such that:

[ bytes read ] % [frame size in bytes ] == 0

The return value will always meet this requirement. A request to read a
number of bytes representing a non-integral number of sample frames
cannot be fulfilled and may result in an IllegalArgumentException.

**Parameters:** b

- a byte array that will contain the requested input data when
this method returns
**Parameters:** off

- the offset from the beginning of the array, in bytes
**Parameters:** len

- the requested number of bytes to read
**Returns:** the number of bytes actually read
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
**See Also:** SourceDataLine.write(byte[], int, int)

,

DataLine.available()

---

#### read

int read​(byte[] b,
int off,
int len)

Reads audio data from the data line's input buffer. The requested number
of bytes is read into the specified array, starting at the specified
offset into the array in bytes. This method blocks until the requested
amount of data has been read. However, if the data line is closed,
stopped, drained, or flushed before the requested amount has been read,
the method no longer blocks, but returns the number of bytes read thus
far.

The number of bytes that can be read without blocking can be ascertained
using the

available

method of the

DataLine

interface. (While it is guaranteed that this number of
bytes can be read without blocking, there is no guarantee that attempts
to read additional data will block.)

The number of bytes to be read must represent an integral number of
sample frames, such that:

[ bytes read ] % [frame size in bytes ] == 0

The return value will always meet this requirement. A request to read a
number of bytes representing a non-integral number of sample frames
cannot be fulfilled and may result in an IllegalArgumentException.

The number of bytes that can be read without blocking can be ascertained
using the

available

method of the

DataLine

interface. (While it is guaranteed that this number of
bytes can be read without blocking, there is no guarantee that attempts
to read additional data will block.)

The number of bytes to be read must represent an integral number of
sample frames, such that:

[ bytes read ] % [frame size in bytes ] == 0

The return value will always meet this requirement. A request to read a
number of bytes representing a non-integral number of sample frames
cannot be fulfilled and may result in an IllegalArgumentException.

The number of bytes to be read must represent an integral number of
sample frames, such that:

[ bytes read ] % [frame size in bytes ] == 0

The return value will always meet this requirement. A request to read a
number of bytes representing a non-integral number of sample frames
cannot be fulfilled and may result in an IllegalArgumentException.

[ bytes read ] % [frame size in bytes ] == 0

The return value will always meet this requirement. A request to read a
number of bytes representing a non-integral number of sample frames
cannot be fulfilled and may result in an IllegalArgumentException.

The return value will always meet this requirement. A request to read a
number of bytes representing a non-integral number of sample frames
cannot be fulfilled and may result in an IllegalArgumentException.

---

