# Class InvalidMidiDataException

**Source:** `java.desktop\javax\sound\midi\InvalidMidiDataException.html`

### Class Description

```java
public class
InvalidMidiDataException

extends
Exception
```

An

InvalidMidiDataException

indicates that inappropriate MIDI data
was encountered. This often means that the data is invalid in and of itself,
from the perspective of the MIDI specification. An example would be an
undefined status byte. However, the exception might simply mean that the data
was invalid in the context it was used, or that the object to which the data
was given was unable to parse or use it. For example, a file reader might not
be able to parse a Type 2 MIDI file, even though that format is defined in
the MIDI specification.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public InvalidMidiDataException()

Constructs an

InvalidMidiDataException

with

null

for its
error detail message.

---

#### public InvalidMidiDataException​(
String
message)

Constructs an

InvalidMidiDataException

with the specified detail
message.

**Parameters:**
- message

- the string to display as an error detail message

---

### Method Details

*No entries found.*

### Additional Sections

#### Class InvalidMidiDataException

java.lang.Object

- java.lang.Throwable
- - java.lang.Exception
- - javax.sound.midi.InvalidMidiDataException

java.lang.Throwable

- java.lang.Exception
- - javax.sound.midi.InvalidMidiDataException

java.lang.Exception

- javax.sound.midi.InvalidMidiDataException

javax.sound.midi.InvalidMidiDataException

**All Implemented Interfaces:** Serializable

```java
public class
InvalidMidiDataException

extends
Exception
```

An

InvalidMidiDataException

indicates that inappropriate MIDI data
was encountered. This often means that the data is invalid in and of itself,
from the perspective of the MIDI specification. An example would be an
undefined status byte. However, the exception might simply mean that the data
was invalid in the context it was used, or that the object to which the data
was given was unable to parse or use it. For example, a file reader might not
be able to parse a Type 2 MIDI file, even though that format is defined in
the MIDI specification.

**See Also:** Serialized Form

public class

InvalidMidiDataException

extends

Exception

An

InvalidMidiDataException

indicates that inappropriate MIDI data
was encountered. This often means that the data is invalid in and of itself,
from the perspective of the MIDI specification. An example would be an
undefined status byte. However, the exception might simply mean that the data
was invalid in the context it was used, or that the object to which the data
was given was unable to parse or use it. For example, a file reader might not
be able to parse a Type 2 MIDI file, even though that format is defined in
the MIDI specification.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

InvalidMidiDataException

()

Constructs an

InvalidMidiDataException

with

null

for its
error detail message.

InvalidMidiDataException

​(

String

message)

Constructs an

InvalidMidiDataException

with the specified detail
message.

========== METHOD SUMMARY ===========

- Method Summary

- Methods declared in class java.lang.

Throwable

addSuppressed

,

fillInStackTrace

,

getCause

,

getLocalizedMessage

,

getMessage

,

getStackTrace

,

getSuppressed

,

initCause

,

printStackTrace

,

printStackTrace

,

printStackTrace

,

setStackTrace

,

toString

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

wait

,

wait

,

wait

Constructor Summary

Constructors

Constructor

Description

InvalidMidiDataException

()

Constructs an

InvalidMidiDataException

with

null

for its
error detail message.

InvalidMidiDataException

​(

String

message)

Constructs an

InvalidMidiDataException

with the specified detail
message.

---

#### Constructor Summary

Constructs an

InvalidMidiDataException

with

null

for its
error detail message.

Constructs an

InvalidMidiDataException

with the specified detail
message.

Method Summary

- Methods declared in class java.lang.

Throwable

addSuppressed

,

fillInStackTrace

,

getCause

,

getLocalizedMessage

,

getMessage

,

getStackTrace

,

getSuppressed

,

initCause

,

printStackTrace

,

printStackTrace

,

printStackTrace

,

setStackTrace

,

toString

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

wait

,

wait

,

wait

---

#### Method Summary

Methods declared in class java.lang.

Throwable

addSuppressed

,

fillInStackTrace

,

getCause

,

getLocalizedMessage

,

getMessage

,

getStackTrace

,

getSuppressed

,

initCause

,

printStackTrace

,

printStackTrace

,

printStackTrace

,

setStackTrace

,

toString

---

#### Methods declared in class java.lang. Throwable

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

wait

,

wait

,

wait

---

#### Methods declared in class java.lang. Object

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- InvalidMidiDataException

```java
public InvalidMidiDataException()
```

Constructs an

InvalidMidiDataException

with

null

for its
error detail message.

- InvalidMidiDataException

```java
public InvalidMidiDataException​(
String
message)
```

Constructs an

InvalidMidiDataException

with the specified detail
message.

**Parameters:** message

- the string to display as an error detail message

Constructor Detail

- InvalidMidiDataException

```java
public InvalidMidiDataException()
```

Constructs an

InvalidMidiDataException

with

null

for its
error detail message.

- InvalidMidiDataException

```java
public InvalidMidiDataException​(
String
message)
```

Constructs an

InvalidMidiDataException

with the specified detail
message.

**Parameters:** message

- the string to display as an error detail message

---

#### Constructor Detail

InvalidMidiDataException

```java
public InvalidMidiDataException()
```

Constructs an

InvalidMidiDataException

with

null

for its
error detail message.

---

#### InvalidMidiDataException

public InvalidMidiDataException()

Constructs an

InvalidMidiDataException

with

null

for its
error detail message.

InvalidMidiDataException

```java
public InvalidMidiDataException​(
String
message)
```

Constructs an

InvalidMidiDataException

with the specified detail
message.

**Parameters:** message

- the string to display as an error detail message

---

#### InvalidMidiDataException

public InvalidMidiDataException​(

String

message)

Constructs an

InvalidMidiDataException

with the specified detail
message.

---

