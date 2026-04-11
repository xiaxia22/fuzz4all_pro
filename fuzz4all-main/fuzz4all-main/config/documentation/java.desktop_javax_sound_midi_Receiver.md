# Interface Receiver

**Source:** `java.desktop\javax\sound\midi\Receiver.html`

### Class Description

```java
public interface
Receiver

extends
AutoCloseable
```

A

Receiver

receives

MidiEvent

objects and typically does
something useful in response, such as interpreting them to generate sound or
raw MIDI output. Common MIDI receivers include synthesizers and MIDI Out
ports.

**All Superinterfaces:** AutoCloseable

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### void send​(
MidiMessage
message,
long timeStamp)

Sends a MIDI message and time-stamp to this receiver. If time-stamping is
not supported by this receiver, the time-stamp value should be -1.

**Parameters:**
- message

- the MIDI message to send
- timeStamp

- the time-stamp for the message, in microseconds

**Throws:**
- IllegalStateException

- if the receiver is closed

---

#### void close()

Indicates that the application has finished using the receiver, and that
limited resources it requires may be released or made available.

If the creation of this

Receiver

resulted in implicitly opening
the underlying device, the device is implicitly closed by this method.
This is true unless the device is kept open by other

Receiver

or

Transmitter

instances that opened the device implicitly, and
unless the device has been opened explicitly. If the device this

Receiver

is retrieved from is closed explicitly by calling

MidiDevice.close

, the

Receiver

is
closed, too. For a detailed description of open/close behaviour see the
class description of

MidiDevice

.

**Specified by:**
- close

in interface

AutoCloseable

**See Also:**
- MidiSystem.getReceiver()

---

### Additional Sections

#### Interface Receiver

**All Superinterfaces:** AutoCloseable

**All Known Subinterfaces:** MidiDeviceReceiver

```java
public interface
Receiver

extends
AutoCloseable
```

A

Receiver

receives

MidiEvent

objects and typically does
something useful in response, such as interpreting them to generate sound or
raw MIDI output. Common MIDI receivers include synthesizers and MIDI Out
ports.

**See Also:** MidiDevice

,

Synthesizer

,

Transmitter

public interface

Receiver

extends

AutoCloseable

A

Receiver

receives

MidiEvent

objects and typically does
something useful in response, such as interpreting them to generate sound or
raw MIDI output. Common MIDI receivers include synthesizers and MIDI Out
ports.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

close

()

Indicates that the application has finished using the receiver, and that
limited resources it requires may be released or made available.

void

send

​(

MidiMessage

message,
long timeStamp)

Sends a MIDI message and time-stamp to this receiver.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

close

()

Indicates that the application has finished using the receiver, and that
limited resources it requires may be released or made available.

void

send

​(

MidiMessage

message,
long timeStamp)

Sends a MIDI message and time-stamp to this receiver.

---

#### Method Summary

Indicates that the application has finished using the receiver, and that
limited resources it requires may be released or made available.

Sends a MIDI message and time-stamp to this receiver.

============ METHOD DETAIL ==========

- Method Detail

- send

```java
void send​(
MidiMessage
message,
long timeStamp)
```

Sends a MIDI message and time-stamp to this receiver. If time-stamping is
not supported by this receiver, the time-stamp value should be -1.

**Parameters:** message

- the MIDI message to send
**Parameters:** timeStamp

- the time-stamp for the message, in microseconds
**Throws:** IllegalStateException

- if the receiver is closed

- close

```java
void close()
```

Indicates that the application has finished using the receiver, and that
limited resources it requires may be released or made available.

If the creation of this

Receiver

resulted in implicitly opening
the underlying device, the device is implicitly closed by this method.
This is true unless the device is kept open by other

Receiver

or

Transmitter

instances that opened the device implicitly, and
unless the device has been opened explicitly. If the device this

Receiver

is retrieved from is closed explicitly by calling

MidiDevice.close

, the

Receiver

is
closed, too. For a detailed description of open/close behaviour see the
class description of

MidiDevice

.

**Specified by:** close

in interface

AutoCloseable
**See Also:** MidiSystem.getReceiver()

Method Detail

- send

```java
void send​(
MidiMessage
message,
long timeStamp)
```

Sends a MIDI message and time-stamp to this receiver. If time-stamping is
not supported by this receiver, the time-stamp value should be -1.

**Parameters:** message

- the MIDI message to send
**Parameters:** timeStamp

- the time-stamp for the message, in microseconds
**Throws:** IllegalStateException

- if the receiver is closed

- close

```java
void close()
```

Indicates that the application has finished using the receiver, and that
limited resources it requires may be released or made available.

If the creation of this

Receiver

resulted in implicitly opening
the underlying device, the device is implicitly closed by this method.
This is true unless the device is kept open by other

Receiver

or

Transmitter

instances that opened the device implicitly, and
unless the device has been opened explicitly. If the device this

Receiver

is retrieved from is closed explicitly by calling

MidiDevice.close

, the

Receiver

is
closed, too. For a detailed description of open/close behaviour see the
class description of

MidiDevice

.

**Specified by:** close

in interface

AutoCloseable
**See Also:** MidiSystem.getReceiver()

---

#### Method Detail

send

```java
void send​(
MidiMessage
message,
long timeStamp)
```

Sends a MIDI message and time-stamp to this receiver. If time-stamping is
not supported by this receiver, the time-stamp value should be -1.

**Parameters:** message

- the MIDI message to send
**Parameters:** timeStamp

- the time-stamp for the message, in microseconds
**Throws:** IllegalStateException

- if the receiver is closed

---

#### send

void send​(

MidiMessage

message,
long timeStamp)

Sends a MIDI message and time-stamp to this receiver. If time-stamping is
not supported by this receiver, the time-stamp value should be -1.

close

```java
void close()
```

Indicates that the application has finished using the receiver, and that
limited resources it requires may be released or made available.

If the creation of this

Receiver

resulted in implicitly opening
the underlying device, the device is implicitly closed by this method.
This is true unless the device is kept open by other

Receiver

or

Transmitter

instances that opened the device implicitly, and
unless the device has been opened explicitly. If the device this

Receiver

is retrieved from is closed explicitly by calling

MidiDevice.close

, the

Receiver

is
closed, too. For a detailed description of open/close behaviour see the
class description of

MidiDevice

.

**Specified by:** close

in interface

AutoCloseable
**See Also:** MidiSystem.getReceiver()

---

#### close

void close()

Indicates that the application has finished using the receiver, and that
limited resources it requires may be released or made available.

If the creation of this

Receiver

resulted in implicitly opening
the underlying device, the device is implicitly closed by this method.
This is true unless the device is kept open by other

Receiver

or

Transmitter

instances that opened the device implicitly, and
unless the device has been opened explicitly. If the device this

Receiver

is retrieved from is closed explicitly by calling

MidiDevice.close

, the

Receiver

is
closed, too. For a detailed description of open/close behaviour see the
class description of

MidiDevice

.

If the creation of this

Receiver

resulted in implicitly opening
the underlying device, the device is implicitly closed by this method.
This is true unless the device is kept open by other

Receiver

or

Transmitter

instances that opened the device implicitly, and
unless the device has been opened explicitly. If the device this

Receiver

is retrieved from is closed explicitly by calling

MidiDevice.close

, the

Receiver

is
closed, too. For a detailed description of open/close behaviour see the
class description of

MidiDevice

.

---

