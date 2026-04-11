# Interface Transmitter

**Source:** `java.desktop\javax\sound\midi\Transmitter.html`

### Class Description

```java
public interface
Transmitter

extends
AutoCloseable
```

A

Transmitter

sends

MidiEvent

objects to one or more

Receivers

. Common MIDI transmitters include sequencers and
MIDI input ports.

**All Superinterfaces:** AutoCloseable

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### void setReceiver​(
Receiver
receiver)

Sets the receiver to which this transmitter will deliver MIDI messages.
If a receiver is currently set, it is replaced with this one.

**Parameters:**
- receiver

- the desired receiver

---

#### Receiver
getReceiver()

Obtains the current receiver to which this transmitter will deliver MIDI
messages.

**Returns:**
- the current receiver. If no receiver is currently set, returns

null

.

---

#### void close()

Indicates that the application has finished using the transmitter, and
that limited resources it requires may be released or made available.

If the creation of this

Transmitter

resulted in implicitly
opening the underlying device, the device is implicitly closed by this
method. This is true unless the device is kept open by other

Receiver

or

Transmitter

instances that opened the device
implicitly, and unless the device has been opened explicitly. If the
device this

Transmitter

is retrieved from is closed explicitly by
calling

MidiDevice.close

, the

Transmitter

is closed, too. For a detailed description of
open/close behaviour see the class description of

MidiDevice

.

**Specified by:**
- close

in interface

AutoCloseable

**See Also:**
- MidiSystem.getTransmitter()

---

### Additional Sections

#### Interface Transmitter

**All Superinterfaces:** AutoCloseable

**All Known Subinterfaces:** MidiDeviceTransmitter

```java
public interface
Transmitter

extends
AutoCloseable
```

A

Transmitter

sends

MidiEvent

objects to one or more

Receivers

. Common MIDI transmitters include sequencers and
MIDI input ports.

**See Also:** Receiver

public interface

Transmitter

extends

AutoCloseable

A

Transmitter

sends

MidiEvent

objects to one or more

Receivers

. Common MIDI transmitters include sequencers and
MIDI input ports.

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

Indicates that the application has finished using the transmitter, and
that limited resources it requires may be released or made available.

Receiver

getReceiver

()

Obtains the current receiver to which this transmitter will deliver MIDI
messages.

void

setReceiver

​(

Receiver

receiver)

Sets the receiver to which this transmitter will deliver MIDI messages.

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

Indicates that the application has finished using the transmitter, and
that limited resources it requires may be released or made available.

Receiver

getReceiver

()

Obtains the current receiver to which this transmitter will deliver MIDI
messages.

void

setReceiver

​(

Receiver

receiver)

Sets the receiver to which this transmitter will deliver MIDI messages.

---

#### Method Summary

Indicates that the application has finished using the transmitter, and
that limited resources it requires may be released or made available.

Obtains the current receiver to which this transmitter will deliver MIDI
messages.

Sets the receiver to which this transmitter will deliver MIDI messages.

============ METHOD DETAIL ==========

- Method Detail

- setReceiver

```java
void setReceiver​(
Receiver
receiver)
```

Sets the receiver to which this transmitter will deliver MIDI messages.
If a receiver is currently set, it is replaced with this one.

**Parameters:** receiver

- the desired receiver

- getReceiver

```java
Receiver
getReceiver()
```

Obtains the current receiver to which this transmitter will deliver MIDI
messages.

**Returns:** the current receiver. If no receiver is currently set, returns

null

.

- close

```java
void close()
```

Indicates that the application has finished using the transmitter, and
that limited resources it requires may be released or made available.

If the creation of this

Transmitter

resulted in implicitly
opening the underlying device, the device is implicitly closed by this
method. This is true unless the device is kept open by other

Receiver

or

Transmitter

instances that opened the device
implicitly, and unless the device has been opened explicitly. If the
device this

Transmitter

is retrieved from is closed explicitly by
calling

MidiDevice.close

, the

Transmitter

is closed, too. For a detailed description of
open/close behaviour see the class description of

MidiDevice

.

**Specified by:** close

in interface

AutoCloseable
**See Also:** MidiSystem.getTransmitter()

Method Detail

- setReceiver

```java
void setReceiver​(
Receiver
receiver)
```

Sets the receiver to which this transmitter will deliver MIDI messages.
If a receiver is currently set, it is replaced with this one.

**Parameters:** receiver

- the desired receiver

- getReceiver

```java
Receiver
getReceiver()
```

Obtains the current receiver to which this transmitter will deliver MIDI
messages.

**Returns:** the current receiver. If no receiver is currently set, returns

null

.

- close

```java
void close()
```

Indicates that the application has finished using the transmitter, and
that limited resources it requires may be released or made available.

If the creation of this

Transmitter

resulted in implicitly
opening the underlying device, the device is implicitly closed by this
method. This is true unless the device is kept open by other

Receiver

or

Transmitter

instances that opened the device
implicitly, and unless the device has been opened explicitly. If the
device this

Transmitter

is retrieved from is closed explicitly by
calling

MidiDevice.close

, the

Transmitter

is closed, too. For a detailed description of
open/close behaviour see the class description of

MidiDevice

.

**Specified by:** close

in interface

AutoCloseable
**See Also:** MidiSystem.getTransmitter()

---

#### Method Detail

setReceiver

```java
void setReceiver​(
Receiver
receiver)
```

Sets the receiver to which this transmitter will deliver MIDI messages.
If a receiver is currently set, it is replaced with this one.

**Parameters:** receiver

- the desired receiver

---

#### setReceiver

void setReceiver​(

Receiver

receiver)

Sets the receiver to which this transmitter will deliver MIDI messages.
If a receiver is currently set, it is replaced with this one.

getReceiver

```java
Receiver
getReceiver()
```

Obtains the current receiver to which this transmitter will deliver MIDI
messages.

**Returns:** the current receiver. If no receiver is currently set, returns

null

.

---

#### getReceiver

Receiver

getReceiver()

Obtains the current receiver to which this transmitter will deliver MIDI
messages.

close

```java
void close()
```

Indicates that the application has finished using the transmitter, and
that limited resources it requires may be released or made available.

If the creation of this

Transmitter

resulted in implicitly
opening the underlying device, the device is implicitly closed by this
method. This is true unless the device is kept open by other

Receiver

or

Transmitter

instances that opened the device
implicitly, and unless the device has been opened explicitly. If the
device this

Transmitter

is retrieved from is closed explicitly by
calling

MidiDevice.close

, the

Transmitter

is closed, too. For a detailed description of
open/close behaviour see the class description of

MidiDevice

.

**Specified by:** close

in interface

AutoCloseable
**See Also:** MidiSystem.getTransmitter()

---

#### close

void close()

Indicates that the application has finished using the transmitter, and
that limited resources it requires may be released or made available.

If the creation of this

Transmitter

resulted in implicitly
opening the underlying device, the device is implicitly closed by this
method. This is true unless the device is kept open by other

Receiver

or

Transmitter

instances that opened the device
implicitly, and unless the device has been opened explicitly. If the
device this

Transmitter

is retrieved from is closed explicitly by
calling

MidiDevice.close

, the

Transmitter

is closed, too. For a detailed description of
open/close behaviour see the class description of

MidiDevice

.

If the creation of this

Transmitter

resulted in implicitly
opening the underlying device, the device is implicitly closed by this
method. This is true unless the device is kept open by other

Receiver

or

Transmitter

instances that opened the device
implicitly, and unless the device has been opened explicitly. If the
device this

Transmitter

is retrieved from is closed explicitly by
calling

MidiDevice.close

, the

Transmitter

is closed, too. For a detailed description of
open/close behaviour see the class description of

MidiDevice

.

---

