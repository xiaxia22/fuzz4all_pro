# Interface Port

**Source:** `java.desktop\javax\sound\sampled\Port.html`

### Class Description

```java
public interface
Port

extends
Line
```

Ports are simple lines for input or output of audio to or from audio devices.
Common examples of ports that act as source lines (mixer inputs) include the
microphone, line input, and CD-ROM drive. Ports that act as target lines
(mixer outputs) include the speaker, headphone, and line output. You can
access port using a

Port.Info

object.

**All Superinterfaces:** AutoCloseable

,

Line

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### Port.Info

static class The Port.Info class extends Line.Info with additional
information specific to ports, including the port's name and whether it
is a source or a target for its mixer.

---

### Additional Sections

#### Interface Port

**All Superinterfaces:** AutoCloseable

,

Line

```java
public interface
Port

extends
Line
```

Ports are simple lines for input or output of audio to or from audio devices.
Common examples of ports that act as source lines (mixer inputs) include the
microphone, line input, and CD-ROM drive. Ports that act as target lines
(mixer outputs) include the speaker, headphone, and line output. You can
access port using a

Port.Info

object.

**Since:** 1.3

public interface

Port

extends

Line

Ports are simple lines for input or output of audio to or from audio devices.
Common examples of ports that act as source lines (mixer inputs) include the
microphone, line input, and CD-ROM drive. Ports that act as target lines
(mixer outputs) include the speaker, headphone, and line output. You can
access port using a

Port.Info

object.

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

Nested Classes

Modifier and Type

Interface

Description

static class

Port.Info

The

Port.Info

class extends

Line.Info

with additional
information specific to ports, including the port's name and whether it
is a source or a target for its mixer.

========== METHOD SUMMARY ===========

- Method Summary

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

Nested Classes

Modifier and Type

Interface

Description

static class

Port.Info

The

Port.Info

class extends

Line.Info

with additional
information specific to ports, including the port's name and whether it
is a source or a target for its mixer.

---

#### Nested Class Summary

The

Port.Info

class extends

Line.Info

with additional
information specific to ports, including the port's name and whether it
is a source or a target for its mixer.

Method Summary

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

