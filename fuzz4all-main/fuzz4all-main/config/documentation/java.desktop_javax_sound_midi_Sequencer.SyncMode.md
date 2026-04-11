# Class Sequencer.SyncMode

**Source:** `java.desktop\javax\sound\midi\Sequencer.SyncMode.html`

### Class Description

```java
public static class
Sequencer.SyncMode

extends
Object
```

A

SyncMode

object represents one of the ways in which a MIDI
sequencer's notion of time can be synchronized with a master or slave
device. If the sequencer is being synchronized to a master, the sequencer
revises its current time in response to messages from the master. If the
sequencer has a slave, the sequencer similarly sends messages to control
the slave's timing.

There are three predefined modes that specify possible masters for a
sequencer:

INTERNAL_CLOCK

,

MIDI_SYNC

, and

MIDI_TIME_CODE

. The latter two work if the sequencer receives
MIDI messages from another device. In these two modes, the sequencer's
time gets reset based on system real-time timing clock messages or MIDI
time code (MTC) messages, respectively. These two modes can also be used
as slave modes, in which case the sequencer sends the corresponding types
of MIDI messages to its receiver (whether or not the sequencer is also
receiving them from a master). A fourth mode,

NO_SYNC

, is used to
indicate that the sequencer should not control its receiver's timing.

**Enclosing interface:** Sequencer

---

### Field Details

#### public static final
Sequencer.SyncMode
INTERNAL_CLOCK

A master synchronization mode that makes the sequencer get its timing
information from its internal clock. This is not a legal slave sync
mode.

---

#### public static final
Sequencer.SyncMode
MIDI_SYNC

A master or slave synchronization mode that specifies the use of MIDI
clock messages. If this mode is used as the master sync mode, the
sequencer gets its timing information from system real-time MIDI
clock messages. This mode only applies as the master sync mode for
sequencers that are also MIDI receivers. If this is the slave sync
mode, the sequencer sends system real-time MIDI clock messages to its
receiver. MIDI clock messages are sent at a rate of 24 per quarter
note.

---

#### public static final
Sequencer.SyncMode
MIDI_TIME_CODE

A master or slave synchronization mode that specifies the use of MIDI
Time Code. If this mode is used as the master sync mode, the
sequencer gets its timing information from MIDI Time Code messages.
This mode only applies as the master sync mode to sequencers that are
also MIDI receivers. If this mode is used as the slave sync mode, the
sequencer sends MIDI Time Code messages to its receiver. (See the
MIDI 1.0 Detailed Specification for a description of MIDI Time Code.)

---

#### public static final
Sequencer.SyncMode
NO_SYNC

A slave synchronization mode indicating that no timing information
should be sent to the receiver. This is not a legal master sync mode.

---

### Constructor Details

#### protected SyncMode​(
String
name)

Constructs a synchronization mode.

**Parameters:**
- name

- name of the synchronization mode

---

### Method Details

#### public final boolean equals​(
Object
obj)

Indicates whether the specified object is equal to this
synchronization mode, returning

true

if the objects are the
same.

**Overrides:**
- equals

in class

Object

**Parameters:**
- obj

- the reference object with which to compare

**Returns:**
- true

if the specified object is equal to this
synchronization mode;

false

otherwise

**See Also:**
- Object.hashCode()

,

HashMap

---

#### public final int hashCode()

Returns a hash code value for this synchronization mode.

**Overrides:**
- hashCode

in class

Object

**Returns:**
- a hash code value for this synchronization mode

**See Also:**
- Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### public final
String
toString()

Provides this synchronization mode's name as the string
representation of the mode.

**Overrides:**
- toString

in class

Object

**Returns:**
- the name of this synchronization mode

---

### Additional Sections

#### Class Sequencer.SyncMode

java.lang.Object

- javax.sound.midi.Sequencer.SyncMode

javax.sound.midi.Sequencer.SyncMode

**Enclosing interface:** Sequencer

```java
public static class
Sequencer.SyncMode

extends
Object
```

A

SyncMode

object represents one of the ways in which a MIDI
sequencer's notion of time can be synchronized with a master or slave
device. If the sequencer is being synchronized to a master, the sequencer
revises its current time in response to messages from the master. If the
sequencer has a slave, the sequencer similarly sends messages to control
the slave's timing.

There are three predefined modes that specify possible masters for a
sequencer:

INTERNAL_CLOCK

,

MIDI_SYNC

, and

MIDI_TIME_CODE

. The latter two work if the sequencer receives
MIDI messages from another device. In these two modes, the sequencer's
time gets reset based on system real-time timing clock messages or MIDI
time code (MTC) messages, respectively. These two modes can also be used
as slave modes, in which case the sequencer sends the corresponding types
of MIDI messages to its receiver (whether or not the sequencer is also
receiving them from a master). A fourth mode,

NO_SYNC

, is used to
indicate that the sequencer should not control its receiver's timing.

**See Also:** Sequencer.setMasterSyncMode(SyncMode)

,

Sequencer.setSlaveSyncMode(SyncMode)

public static class

Sequencer.SyncMode

extends

Object

A

SyncMode

object represents one of the ways in which a MIDI
sequencer's notion of time can be synchronized with a master or slave
device. If the sequencer is being synchronized to a master, the sequencer
revises its current time in response to messages from the master. If the
sequencer has a slave, the sequencer similarly sends messages to control
the slave's timing.

There are three predefined modes that specify possible masters for a
sequencer:

INTERNAL_CLOCK

,

MIDI_SYNC

, and

MIDI_TIME_CODE

. The latter two work if the sequencer receives
MIDI messages from another device. In these two modes, the sequencer's
time gets reset based on system real-time timing clock messages or MIDI
time code (MTC) messages, respectively. These two modes can also be used
as slave modes, in which case the sequencer sends the corresponding types
of MIDI messages to its receiver (whether or not the sequencer is also
receiving them from a master). A fourth mode,

NO_SYNC

, is used to
indicate that the sequencer should not control its receiver's timing.

There are three predefined modes that specify possible masters for a
sequencer:

INTERNAL_CLOCK

,

MIDI_SYNC

, and

MIDI_TIME_CODE

. The latter two work if the sequencer receives
MIDI messages from another device. In these two modes, the sequencer's
time gets reset based on system real-time timing clock messages or MIDI
time code (MTC) messages, respectively. These two modes can also be used
as slave modes, in which case the sequencer sends the corresponding types
of MIDI messages to its receiver (whether or not the sequencer is also
receiving them from a master). A fourth mode,

NO_SYNC

, is used to
indicate that the sequencer should not control its receiver's timing.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static

Sequencer.SyncMode

INTERNAL_CLOCK

A master synchronization mode that makes the sequencer get its timing
information from its internal clock.

static

Sequencer.SyncMode

MIDI_SYNC

A master or slave synchronization mode that specifies the use of MIDI
clock messages.

static

Sequencer.SyncMode

MIDI_TIME_CODE

A master or slave synchronization mode that specifies the use of MIDI
Time Code.

static

Sequencer.SyncMode

NO_SYNC

A slave synchronization mode indicating that no timing information
should be sent to the receiver.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

SyncMode

​(

String

name)

Constructs a synchronization mode.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

boolean

equals

​(

Object

obj)

Indicates whether the specified object is equal to this
synchronization mode, returning

true

if the objects are the
same.

int

hashCode

()

Returns a hash code value for this synchronization mode.

String

toString

()

Provides this synchronization mode's name as the string
representation of the mode.

- Methods declared in class java.lang.

Object

clone

,

finalize

,

getClass

,

notify

,

notifyAll

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

static

Sequencer.SyncMode

INTERNAL_CLOCK

A master synchronization mode that makes the sequencer get its timing
information from its internal clock.

static

Sequencer.SyncMode

MIDI_SYNC

A master or slave synchronization mode that specifies the use of MIDI
clock messages.

static

Sequencer.SyncMode

MIDI_TIME_CODE

A master or slave synchronization mode that specifies the use of MIDI
Time Code.

static

Sequencer.SyncMode

NO_SYNC

A slave synchronization mode indicating that no timing information
should be sent to the receiver.

---

#### Field Summary

A master synchronization mode that makes the sequencer get its timing
information from its internal clock.

A master or slave synchronization mode that specifies the use of MIDI
clock messages.

A master or slave synchronization mode that specifies the use of MIDI
Time Code.

A slave synchronization mode indicating that no timing information
should be sent to the receiver.

Constructor Summary

Constructors

Modifier

Constructor

Description

protected

SyncMode

​(

String

name)

Constructs a synchronization mode.

---

#### Constructor Summary

Constructs a synchronization mode.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

boolean

equals

​(

Object

obj)

Indicates whether the specified object is equal to this
synchronization mode, returning

true

if the objects are the
same.

int

hashCode

()

Returns a hash code value for this synchronization mode.

String

toString

()

Provides this synchronization mode's name as the string
representation of the mode.

- Methods declared in class java.lang.

Object

clone

,

finalize

,

getClass

,

notify

,

notifyAll

,

wait

,

wait

,

wait

---

#### Method Summary

Indicates whether the specified object is equal to this
synchronization mode, returning

true

if the objects are the
same.

Returns a hash code value for this synchronization mode.

Provides this synchronization mode's name as the string
representation of the mode.

Methods declared in class java.lang.

Object

clone

,

finalize

,

getClass

,

notify

,

notifyAll

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

- INTERNAL_CLOCK

```java
public static final
Sequencer.SyncMode
INTERNAL_CLOCK
```

A master synchronization mode that makes the sequencer get its timing
information from its internal clock. This is not a legal slave sync
mode.

- MIDI_SYNC

```java
public static final
Sequencer.SyncMode
MIDI_SYNC
```

A master or slave synchronization mode that specifies the use of MIDI
clock messages. If this mode is used as the master sync mode, the
sequencer gets its timing information from system real-time MIDI
clock messages. This mode only applies as the master sync mode for
sequencers that are also MIDI receivers. If this is the slave sync
mode, the sequencer sends system real-time MIDI clock messages to its
receiver. MIDI clock messages are sent at a rate of 24 per quarter
note.

- MIDI_TIME_CODE

```java
public static final
Sequencer.SyncMode
MIDI_TIME_CODE
```

A master or slave synchronization mode that specifies the use of MIDI
Time Code. If this mode is used as the master sync mode, the
sequencer gets its timing information from MIDI Time Code messages.
This mode only applies as the master sync mode to sequencers that are
also MIDI receivers. If this mode is used as the slave sync mode, the
sequencer sends MIDI Time Code messages to its receiver. (See the
MIDI 1.0 Detailed Specification for a description of MIDI Time Code.)

- NO_SYNC

```java
public static final
Sequencer.SyncMode
NO_SYNC
```

A slave synchronization mode indicating that no timing information
should be sent to the receiver. This is not a legal master sync mode.

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- SyncMode

```java
protected SyncMode​(
String
name)
```

Constructs a synchronization mode.

**Parameters:** name

- name of the synchronization mode

============ METHOD DETAIL ==========

- Method Detail

- equals

```java
public final boolean equals​(
Object
obj)
```

Indicates whether the specified object is equal to this
synchronization mode, returning

true

if the objects are the
same.

**Overrides:** equals

in class

Object
**Parameters:** obj

- the reference object with which to compare
**Returns:** true

if the specified object is equal to this
synchronization mode;

false

otherwise
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
public final int hashCode()
```

Returns a hash code value for this synchronization mode.

**Overrides:** hashCode

in class

Object
**Returns:** a hash code value for this synchronization mode
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

- toString

```java
public final
String
toString()
```

Provides this synchronization mode's name as the string
representation of the mode.

**Overrides:** toString

in class

Object
**Returns:** the name of this synchronization mode

Field Detail

- INTERNAL_CLOCK

```java
public static final
Sequencer.SyncMode
INTERNAL_CLOCK
```

A master synchronization mode that makes the sequencer get its timing
information from its internal clock. This is not a legal slave sync
mode.

- MIDI_SYNC

```java
public static final
Sequencer.SyncMode
MIDI_SYNC
```

A master or slave synchronization mode that specifies the use of MIDI
clock messages. If this mode is used as the master sync mode, the
sequencer gets its timing information from system real-time MIDI
clock messages. This mode only applies as the master sync mode for
sequencers that are also MIDI receivers. If this is the slave sync
mode, the sequencer sends system real-time MIDI clock messages to its
receiver. MIDI clock messages are sent at a rate of 24 per quarter
note.

- MIDI_TIME_CODE

```java
public static final
Sequencer.SyncMode
MIDI_TIME_CODE
```

A master or slave synchronization mode that specifies the use of MIDI
Time Code. If this mode is used as the master sync mode, the
sequencer gets its timing information from MIDI Time Code messages.
This mode only applies as the master sync mode to sequencers that are
also MIDI receivers. If this mode is used as the slave sync mode, the
sequencer sends MIDI Time Code messages to its receiver. (See the
MIDI 1.0 Detailed Specification for a description of MIDI Time Code.)

- NO_SYNC

```java
public static final
Sequencer.SyncMode
NO_SYNC
```

A slave synchronization mode indicating that no timing information
should be sent to the receiver. This is not a legal master sync mode.

---

#### Field Detail

INTERNAL_CLOCK

```java
public static final
Sequencer.SyncMode
INTERNAL_CLOCK
```

A master synchronization mode that makes the sequencer get its timing
information from its internal clock. This is not a legal slave sync
mode.

---

#### INTERNAL_CLOCK

public static final

Sequencer.SyncMode

INTERNAL_CLOCK

A master synchronization mode that makes the sequencer get its timing
information from its internal clock. This is not a legal slave sync
mode.

MIDI_SYNC

```java
public static final
Sequencer.SyncMode
MIDI_SYNC
```

A master or slave synchronization mode that specifies the use of MIDI
clock messages. If this mode is used as the master sync mode, the
sequencer gets its timing information from system real-time MIDI
clock messages. This mode only applies as the master sync mode for
sequencers that are also MIDI receivers. If this is the slave sync
mode, the sequencer sends system real-time MIDI clock messages to its
receiver. MIDI clock messages are sent at a rate of 24 per quarter
note.

---

#### MIDI_SYNC

public static final

Sequencer.SyncMode

MIDI_SYNC

A master or slave synchronization mode that specifies the use of MIDI
clock messages. If this mode is used as the master sync mode, the
sequencer gets its timing information from system real-time MIDI
clock messages. This mode only applies as the master sync mode for
sequencers that are also MIDI receivers. If this is the slave sync
mode, the sequencer sends system real-time MIDI clock messages to its
receiver. MIDI clock messages are sent at a rate of 24 per quarter
note.

MIDI_TIME_CODE

```java
public static final
Sequencer.SyncMode
MIDI_TIME_CODE
```

A master or slave synchronization mode that specifies the use of MIDI
Time Code. If this mode is used as the master sync mode, the
sequencer gets its timing information from MIDI Time Code messages.
This mode only applies as the master sync mode to sequencers that are
also MIDI receivers. If this mode is used as the slave sync mode, the
sequencer sends MIDI Time Code messages to its receiver. (See the
MIDI 1.0 Detailed Specification for a description of MIDI Time Code.)

---

#### MIDI_TIME_CODE

public static final

Sequencer.SyncMode

MIDI_TIME_CODE

A master or slave synchronization mode that specifies the use of MIDI
Time Code. If this mode is used as the master sync mode, the
sequencer gets its timing information from MIDI Time Code messages.
This mode only applies as the master sync mode to sequencers that are
also MIDI receivers. If this mode is used as the slave sync mode, the
sequencer sends MIDI Time Code messages to its receiver. (See the
MIDI 1.0 Detailed Specification for a description of MIDI Time Code.)

NO_SYNC

```java
public static final
Sequencer.SyncMode
NO_SYNC
```

A slave synchronization mode indicating that no timing information
should be sent to the receiver. This is not a legal master sync mode.

---

#### NO_SYNC

public static final

Sequencer.SyncMode

NO_SYNC

A slave synchronization mode indicating that no timing information
should be sent to the receiver. This is not a legal master sync mode.

Constructor Detail

- SyncMode

```java
protected SyncMode​(
String
name)
```

Constructs a synchronization mode.

**Parameters:** name

- name of the synchronization mode

---

#### Constructor Detail

SyncMode

```java
protected SyncMode​(
String
name)
```

Constructs a synchronization mode.

**Parameters:** name

- name of the synchronization mode

---

#### SyncMode

protected SyncMode​(

String

name)

Constructs a synchronization mode.

Method Detail

- equals

```java
public final boolean equals​(
Object
obj)
```

Indicates whether the specified object is equal to this
synchronization mode, returning

true

if the objects are the
same.

**Overrides:** equals

in class

Object
**Parameters:** obj

- the reference object with which to compare
**Returns:** true

if the specified object is equal to this
synchronization mode;

false

otherwise
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
public final int hashCode()
```

Returns a hash code value for this synchronization mode.

**Overrides:** hashCode

in class

Object
**Returns:** a hash code value for this synchronization mode
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

- toString

```java
public final
String
toString()
```

Provides this synchronization mode's name as the string
representation of the mode.

**Overrides:** toString

in class

Object
**Returns:** the name of this synchronization mode

---

#### Method Detail

equals

```java
public final boolean equals​(
Object
obj)
```

Indicates whether the specified object is equal to this
synchronization mode, returning

true

if the objects are the
same.

**Overrides:** equals

in class

Object
**Parameters:** obj

- the reference object with which to compare
**Returns:** true

if the specified object is equal to this
synchronization mode;

false

otherwise
**See Also:** Object.hashCode()

,

HashMap

---

#### equals

public final boolean equals​(

Object

obj)

Indicates whether the specified object is equal to this
synchronization mode, returning

true

if the objects are the
same.

hashCode

```java
public final int hashCode()
```

Returns a hash code value for this synchronization mode.

**Overrides:** hashCode

in class

Object
**Returns:** a hash code value for this synchronization mode
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### hashCode

public final int hashCode()

Returns a hash code value for this synchronization mode.

toString

```java
public final
String
toString()
```

Provides this synchronization mode's name as the string
representation of the mode.

**Overrides:** toString

in class

Object
**Returns:** the name of this synchronization mode

---

#### toString

public final

String

toString()

Provides this synchronization mode's name as the string
representation of the mode.

---

