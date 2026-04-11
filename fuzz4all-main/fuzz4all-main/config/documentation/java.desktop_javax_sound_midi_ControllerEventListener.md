# Interface ControllerEventListener

**Source:** `java.desktop\javax\sound\midi\ControllerEventListener.html`

### Class Description

```java
public interface
ControllerEventListener

extends
EventListener
```

The

ControllerEventListener

interface should be implemented by
classes whose instances need to be notified when a

Sequencer

has
processed a requested type of MIDI control-change event. To register a

ControllerEventListener

object to receive such notifications, invoke
the

addControllerEventListener

method of

Sequencer

, specifying the types
of MIDI controllers about which you are interested in getting control-change
notifications.

**All Superinterfaces:** EventListener

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### void controlChange​(
ShortMessage
event)

Invoked when a

Sequencer

has encountered and processed a
control-change event of interest to this listener. The event passed in is
a

ShortMessage

whose first data byte indicates the controller
number and whose second data byte is the value to which the controller
was set.

**Parameters:**
- event

- the control-change event that the sequencer encountered in
the sequence it is processing

**See Also:**
- Sequencer.addControllerEventListener(ControllerEventListener, int[])

,

MidiChannel.controlChange(int, int)

,

ShortMessage.getData1()

,

ShortMessage.getData2()

---

### Additional Sections

#### Interface ControllerEventListener

**All Superinterfaces:** EventListener

```java
public interface
ControllerEventListener

extends
EventListener
```

The

ControllerEventListener

interface should be implemented by
classes whose instances need to be notified when a

Sequencer

has
processed a requested type of MIDI control-change event. To register a

ControllerEventListener

object to receive such notifications, invoke
the

addControllerEventListener

method of

Sequencer

, specifying the types
of MIDI controllers about which you are interested in getting control-change
notifications.

**See Also:** MidiChannel.controlChange(int, int)

public interface

ControllerEventListener

extends

EventListener

The

ControllerEventListener

interface should be implemented by
classes whose instances need to be notified when a

Sequencer

has
processed a requested type of MIDI control-change event. To register a

ControllerEventListener

object to receive such notifications, invoke
the

addControllerEventListener

method of

Sequencer

, specifying the types
of MIDI controllers about which you are interested in getting control-change
notifications.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

controlChange

​(

ShortMessage

event)

Invoked when a

Sequencer

has encountered and processed a
control-change event of interest to this listener.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

controlChange

​(

ShortMessage

event)

Invoked when a

Sequencer

has encountered and processed a
control-change event of interest to this listener.

---

#### Method Summary

Invoked when a

Sequencer

has encountered and processed a
control-change event of interest to this listener.

============ METHOD DETAIL ==========

- Method Detail

- controlChange

```java
void controlChange​(
ShortMessage
event)
```

Invoked when a

Sequencer

has encountered and processed a
control-change event of interest to this listener. The event passed in is
a

ShortMessage

whose first data byte indicates the controller
number and whose second data byte is the value to which the controller
was set.

**Parameters:** event

- the control-change event that the sequencer encountered in
the sequence it is processing
**See Also:** Sequencer.addControllerEventListener(ControllerEventListener, int[])

,

MidiChannel.controlChange(int, int)

,

ShortMessage.getData1()

,

ShortMessage.getData2()

Method Detail

- controlChange

```java
void controlChange​(
ShortMessage
event)
```

Invoked when a

Sequencer

has encountered and processed a
control-change event of interest to this listener. The event passed in is
a

ShortMessage

whose first data byte indicates the controller
number and whose second data byte is the value to which the controller
was set.

**Parameters:** event

- the control-change event that the sequencer encountered in
the sequence it is processing
**See Also:** Sequencer.addControllerEventListener(ControllerEventListener, int[])

,

MidiChannel.controlChange(int, int)

,

ShortMessage.getData1()

,

ShortMessage.getData2()

---

#### Method Detail

controlChange

```java
void controlChange​(
ShortMessage
event)
```

Invoked when a

Sequencer

has encountered and processed a
control-change event of interest to this listener. The event passed in is
a

ShortMessage

whose first data byte indicates the controller
number and whose second data byte is the value to which the controller
was set.

**Parameters:** event

- the control-change event that the sequencer encountered in
the sequence it is processing
**See Also:** Sequencer.addControllerEventListener(ControllerEventListener, int[])

,

MidiChannel.controlChange(int, int)

,

ShortMessage.getData1()

,

ShortMessage.getData2()

---

#### controlChange

void controlChange​(

ShortMessage

event)

Invoked when a

Sequencer

has encountered and processed a
control-change event of interest to this listener. The event passed in is
a

ShortMessage

whose first data byte indicates the controller
number and whose second data byte is the value to which the controller
was set.

---

