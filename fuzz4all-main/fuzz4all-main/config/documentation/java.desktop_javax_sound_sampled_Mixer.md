# Interface Mixer

**Source:** `java.desktop\javax\sound\sampled\Mixer.html`

### Class Description

```java
public interface
Mixer

extends
Line
```

A mixer is an audio device with one or more lines. It need not be designed
for mixing audio signals. A mixer that actually mixes audio has multiple
input (source) lines and at least one output (target) line. The former are
often instances of classes that implement

SourceDataLine

, and the
latter,

TargetDataLine

.

Port

objects, too, are either source
lines or target lines. A mixer can accept prerecorded, loopable sound as
input, by having some of its source lines be instances of objects that
implement the

Clip

interface.

Through methods of the

Line

interface, which

Mixer

extends, a
mixer might provide a set of controls that are global to the mixer. For
example, the mixer can have a master gain control. These global controls are
distinct from the controls belonging to each of the mixer's individual lines.

Some mixers, especially those with internal digital mixing capabilities, may
provide additional capabilities by implementing the

DataLine

interface.

A mixer can support synchronization of its lines. When one line in a
synchronized group is started or stopped, the other lines in the group
automatically start or stop simultaneously with the explicitly affected one.

**All Superinterfaces:** AutoCloseable

,

Line

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### Mixer.Info
getMixerInfo()

Obtains information about this mixer, including the product's name,
version, vendor, etc.

**Returns:**
- a mixer info object that describes this mixer

**See Also:**
- Mixer.Info

---

#### Line.Info
[] getSourceLineInfo()

Obtains information about the set of source lines supported by this
mixer. Some source lines may only be available when this mixer is open.

**Returns:**
- array of

Line.Info

objects representing source lines for
this mixer. If no source lines are supported, an array of length
0 is returned.

---

#### Line.Info
[] getTargetLineInfo()

Obtains information about the set of target lines supported by this
mixer. Some target lines may only be available when this mixer is open.

**Returns:**
- array of

Line.Info

objects representing target lines for
this mixer. If no target lines are supported, an array of length
0 is returned.

---

#### Line.Info
[] getSourceLineInfo​(
Line.Info
info)

Obtains information about source lines of a particular type supported by
the mixer. Some source lines may only be available when this mixer is
open.

**Parameters:**
- info

- a

Line.Info

object describing lines about which
information is queried

**Returns:**
- an array of

Line.Info

objects describing source lines
matching the type requested. If no matching source lines are
supported, an array of length 0 is returned.

---

#### Line.Info
[] getTargetLineInfo​(
Line.Info
info)

Obtains information about target lines of a particular type supported by
the mixer. Some target lines may only be available when this mixer is
open.

**Parameters:**
- info

- a

Line.Info

object describing lines about which
information is queried

**Returns:**
- an array of

Line.Info

objects describing target lines
matching the type requested. If no matching target lines are
supported, an array of length 0 is returned.

---

#### boolean isLineSupported​(
Line.Info
info)

Indicates whether the mixer supports a line (or lines) that match the
specified

Line.Info

object. Some lines may only be supported when
this mixer is open.

**Parameters:**
- info

- describes the line for which support is queried

**Returns:**
- true

if at least one matching line is supported,

false

otherwise

---

#### Line
getLine​(
Line.Info
info)
throws
LineUnavailableException

Obtains a line that is available for use and that matches the description
in the specified

Line.Info

object.

If a

DataLine

is requested, and

info

is an instance of

DataLine.Info

specifying at least one fully qualified audio
format, the last one will be used as the default format of the returned

DataLine

.

**Parameters:**
- info

- describes the desired line

**Returns:**
- a line that is available for use and that matches the description
in the specified

Line.Info

object

**Throws:**
- LineUnavailableException

- if a matching line is not available due
to resource restrictions
- IllegalArgumentException

- if this mixer does not support any lines
matching the description
- SecurityException

- if a matching line is not available due to
security restrictions

---

#### int getMaxLines​(
Line.Info
info)

Obtains the approximate maximum number of lines of the requested type
that can be open simultaneously on the mixer.

Certain types of mixers do not have a hard bound and may allow opening
more lines. Since certain lines are a shared resource, a mixer may not be
able to open the maximum number of lines if another process has opened
lines of this mixer.

The requested type is any line that matches the description in the
provided

Line.Info

object. For example, if the info object
represents a speaker port, and the mixer supports exactly one speaker
port, this method should return 1. If the info object represents a source
data line and the mixer supports the use of 32 source data lines
simultaneously, the return value should be 32. If there is no limit, this
function returns

AudioSystem.NOT_SPECIFIED

.

**Parameters:**
- info

- a

Line.Info

that describes the line for which the
number of supported instances is queried

**Returns:**
- the maximum number of matching lines supported, or

AudioSystem.NOT_SPECIFIED

---

#### Line
[] getSourceLines()

Obtains the set of all source lines currently open to this mixer.

**Returns:**
- the source lines currently open to the mixer. If no source lines
are currently open to this mixer, an array of length 0 is
returned.

**Throws:**
- SecurityException

- if the matching lines are not available due to
security restrictions

---

#### Line
[] getTargetLines()

Obtains the set of all target lines currently open from this mixer.

**Returns:**
- target lines currently open from the mixer. If no target lines
are currently open from this mixer, an array of length 0 is
returned.

**Throws:**
- SecurityException

- if the matching lines are not available due to
security restrictions

---

#### void synchronize​(
Line
[] lines,
boolean maintainSync)

Synchronizes two or more lines. Any subsequent command that starts or
stops audio playback or capture for one of these lines will exert the
same effect on the other lines in the group, so that they start or stop
playing or capturing data simultaneously.

**Parameters:**
- lines

- the lines that should be synchronized
- maintainSync

-

true

if the synchronization must be
precisely maintained (i.e., the synchronization must be
sample-accurate) at all times during operation of the lines, or

false

if precise synchronization is required only during
start and stop operations

**Throws:**
- IllegalArgumentException

- if the lines cannot be synchronized.
This may occur if the lines are of different types or have
different formats for which this mixer does not support
synchronization, or if all lines specified do not belong to this
mixer.

---

#### void unsynchronize​(
Line
[] lines)

Releases synchronization for the specified lines. The array must be
identical to one for which synchronization has already been established;
otherwise an exception may be thrown. However,

null

may be
specified, in which case all currently synchronized lines that belong to
this mixer are unsynchronized.

**Parameters:**
- lines

- the synchronized lines for which synchronization should be
released, or

null

for all this mixer's synchronized lines

**Throws:**
- IllegalArgumentException

- if the lines cannot be unsynchronized.
This may occur if the argument specified does not exactly match a
set of lines for which synchronization has already been
established.

---

#### boolean isSynchronizationSupported​(
Line
[] lines,
boolean maintainSync)

Reports whether this mixer supports synchronization of the specified set
of lines.

**Parameters:**
- lines

- the set of lines for which synchronization support is
queried
- maintainSync

-

true

if the synchronization must be
precisely maintained (i.e., the synchronization must be
sample-accurate) at all times during operation of the lines, or

false

if precise synchronization is required only during
start and stop operations

**Returns:**
- true

if the lines can be synchronized,

false

otherwise

---

### Additional Sections

#### Interface Mixer

**All Superinterfaces:** AutoCloseable

,

Line

```java
public interface
Mixer

extends
Line
```

A mixer is an audio device with one or more lines. It need not be designed
for mixing audio signals. A mixer that actually mixes audio has multiple
input (source) lines and at least one output (target) line. The former are
often instances of classes that implement

SourceDataLine

, and the
latter,

TargetDataLine

.

Port

objects, too, are either source
lines or target lines. A mixer can accept prerecorded, loopable sound as
input, by having some of its source lines be instances of objects that
implement the

Clip

interface.

Through methods of the

Line

interface, which

Mixer

extends, a
mixer might provide a set of controls that are global to the mixer. For
example, the mixer can have a master gain control. These global controls are
distinct from the controls belonging to each of the mixer's individual lines.

Some mixers, especially those with internal digital mixing capabilities, may
provide additional capabilities by implementing the

DataLine

interface.

A mixer can support synchronization of its lines. When one line in a
synchronized group is started or stopped, the other lines in the group
automatically start or stop simultaneously with the explicitly affected one.

**Since:** 1.3

public interface

Mixer

extends

Line

A mixer is an audio device with one or more lines. It need not be designed
for mixing audio signals. A mixer that actually mixes audio has multiple
input (source) lines and at least one output (target) line. The former are
often instances of classes that implement

SourceDataLine

, and the
latter,

TargetDataLine

.

Port

objects, too, are either source
lines or target lines. A mixer can accept prerecorded, loopable sound as
input, by having some of its source lines be instances of objects that
implement the

Clip

interface.

Through methods of the

Line

interface, which

Mixer

extends, a
mixer might provide a set of controls that are global to the mixer. For
example, the mixer can have a master gain control. These global controls are
distinct from the controls belonging to each of the mixer's individual lines.

Some mixers, especially those with internal digital mixing capabilities, may
provide additional capabilities by implementing the

DataLine

interface.

A mixer can support synchronization of its lines. When one line in a
synchronized group is started or stopped, the other lines in the group
automatically start or stop simultaneously with the explicitly affected one.

Through methods of the

Line

interface, which

Mixer

extends, a
mixer might provide a set of controls that are global to the mixer. For
example, the mixer can have a master gain control. These global controls are
distinct from the controls belonging to each of the mixer's individual lines.

Some mixers, especially those with internal digital mixing capabilities, may
provide additional capabilities by implementing the

DataLine

interface.

A mixer can support synchronization of its lines. When one line in a
synchronized group is started or stopped, the other lines in the group
automatically start or stop simultaneously with the explicitly affected one.

Some mixers, especially those with internal digital mixing capabilities, may
provide additional capabilities by implementing the

DataLine

interface.

A mixer can support synchronization of its lines. When one line in a
synchronized group is started or stopped, the other lines in the group
automatically start or stop simultaneously with the explicitly affected one.

A mixer can support synchronization of its lines. When one line in a
synchronized group is started or stopped, the other lines in the group
automatically start or stop simultaneously with the explicitly affected one.

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

Nested Classes

Modifier and Type

Interface

Description

static class

Mixer.Info

The

Mixer.Info

class represents information about an audio mixer,
including the product's name, version, and vendor, along with a textual
description.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

Line

getLine

​(

Line.Info

info)

Obtains a line that is available for use and that matches the description
in the specified

Line.Info

object.

int

getMaxLines

​(

Line.Info

info)

Obtains the approximate maximum number of lines of the requested type
that can be open simultaneously on the mixer.

Mixer.Info

getMixerInfo

()

Obtains information about this mixer, including the product's name,
version, vendor, etc.

Line.Info

[]

getSourceLineInfo

()

Obtains information about the set of source lines supported by this
mixer.

Line.Info

[]

getSourceLineInfo

​(

Line.Info

info)

Obtains information about source lines of a particular type supported by
the mixer.

Line

[]

getSourceLines

()

Obtains the set of all source lines currently open to this mixer.

Line.Info

[]

getTargetLineInfo

()

Obtains information about the set of target lines supported by this
mixer.

Line.Info

[]

getTargetLineInfo

​(

Line.Info

info)

Obtains information about target lines of a particular type supported by
the mixer.

Line

[]

getTargetLines

()

Obtains the set of all target lines currently open from this mixer.

boolean

isLineSupported

​(

Line.Info

info)

Indicates whether the mixer supports a line (or lines) that match the
specified

Line.Info

object.

boolean

isSynchronizationSupported

​(

Line

[] lines,
boolean maintainSync)

Reports whether this mixer supports synchronization of the specified set
of lines.

void

synchronize

​(

Line

[] lines,
boolean maintainSync)

Synchronizes two or more lines.

void

unsynchronize

​(

Line

[] lines)

Releases synchronization for the specified lines.

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

Mixer.Info

The

Mixer.Info

class represents information about an audio mixer,
including the product's name, version, and vendor, along with a textual
description.

---

#### Nested Class Summary

The

Mixer.Info

class represents information about an audio mixer,
including the product's name, version, and vendor, along with a textual
description.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

Line

getLine

​(

Line.Info

info)

Obtains a line that is available for use and that matches the description
in the specified

Line.Info

object.

int

getMaxLines

​(

Line.Info

info)

Obtains the approximate maximum number of lines of the requested type
that can be open simultaneously on the mixer.

Mixer.Info

getMixerInfo

()

Obtains information about this mixer, including the product's name,
version, vendor, etc.

Line.Info

[]

getSourceLineInfo

()

Obtains information about the set of source lines supported by this
mixer.

Line.Info

[]

getSourceLineInfo

​(

Line.Info

info)

Obtains information about source lines of a particular type supported by
the mixer.

Line

[]

getSourceLines

()

Obtains the set of all source lines currently open to this mixer.

Line.Info

[]

getTargetLineInfo

()

Obtains information about the set of target lines supported by this
mixer.

Line.Info

[]

getTargetLineInfo

​(

Line.Info

info)

Obtains information about target lines of a particular type supported by
the mixer.

Line

[]

getTargetLines

()

Obtains the set of all target lines currently open from this mixer.

boolean

isLineSupported

​(

Line.Info

info)

Indicates whether the mixer supports a line (or lines) that match the
specified

Line.Info

object.

boolean

isSynchronizationSupported

​(

Line

[] lines,
boolean maintainSync)

Reports whether this mixer supports synchronization of the specified set
of lines.

void

synchronize

​(

Line

[] lines,
boolean maintainSync)

Synchronizes two or more lines.

void

unsynchronize

​(

Line

[] lines)

Releases synchronization for the specified lines.

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

Obtains a line that is available for use and that matches the description
in the specified

Line.Info

object.

Obtains the approximate maximum number of lines of the requested type
that can be open simultaneously on the mixer.

Obtains information about this mixer, including the product's name,
version, vendor, etc.

Obtains information about the set of source lines supported by this
mixer.

Obtains information about source lines of a particular type supported by
the mixer.

Obtains the set of all source lines currently open to this mixer.

Obtains information about the set of target lines supported by this
mixer.

Obtains information about target lines of a particular type supported by
the mixer.

Obtains the set of all target lines currently open from this mixer.

Indicates whether the mixer supports a line (or lines) that match the
specified

Line.Info

object.

Reports whether this mixer supports synchronization of the specified set
of lines.

Synchronizes two or more lines.

Releases synchronization for the specified lines.

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

- getMixerInfo

```java
Mixer.Info
getMixerInfo()
```

Obtains information about this mixer, including the product's name,
version, vendor, etc.

**Returns:** a mixer info object that describes this mixer
**See Also:** Mixer.Info

- getSourceLineInfo

```java
Line.Info
[] getSourceLineInfo()
```

Obtains information about the set of source lines supported by this
mixer. Some source lines may only be available when this mixer is open.

**Returns:** array of

Line.Info

objects representing source lines for
this mixer. If no source lines are supported, an array of length
0 is returned.

- getTargetLineInfo

```java
Line.Info
[] getTargetLineInfo()
```

Obtains information about the set of target lines supported by this
mixer. Some target lines may only be available when this mixer is open.

**Returns:** array of

Line.Info

objects representing target lines for
this mixer. If no target lines are supported, an array of length
0 is returned.

- getSourceLineInfo

```java
Line.Info
[] getSourceLineInfo​(
Line.Info
info)
```

Obtains information about source lines of a particular type supported by
the mixer. Some source lines may only be available when this mixer is
open.

**Parameters:** info

- a

Line.Info

object describing lines about which
information is queried
**Returns:** an array of

Line.Info

objects describing source lines
matching the type requested. If no matching source lines are
supported, an array of length 0 is returned.

- getTargetLineInfo

```java
Line.Info
[] getTargetLineInfo​(
Line.Info
info)
```

Obtains information about target lines of a particular type supported by
the mixer. Some target lines may only be available when this mixer is
open.

**Parameters:** info

- a

Line.Info

object describing lines about which
information is queried
**Returns:** an array of

Line.Info

objects describing target lines
matching the type requested. If no matching target lines are
supported, an array of length 0 is returned.

- isLineSupported

```java
boolean isLineSupported​(
Line.Info
info)
```

Indicates whether the mixer supports a line (or lines) that match the
specified

Line.Info

object. Some lines may only be supported when
this mixer is open.

**Parameters:** info

- describes the line for which support is queried
**Returns:** true

if at least one matching line is supported,

false

otherwise

- getLine

```java
Line
getLine​(
Line.Info
info)
throws
LineUnavailableException
```

Obtains a line that is available for use and that matches the description
in the specified

Line.Info

object.

If a

DataLine

is requested, and

info

is an instance of

DataLine.Info

specifying at least one fully qualified audio
format, the last one will be used as the default format of the returned

DataLine

.

**Parameters:** info

- describes the desired line
**Returns:** a line that is available for use and that matches the description
in the specified

Line.Info

object
**Throws:** LineUnavailableException

- if a matching line is not available due
to resource restrictions
**Throws:** IllegalArgumentException

- if this mixer does not support any lines
matching the description
**Throws:** SecurityException

- if a matching line is not available due to
security restrictions

- getMaxLines

```java
int getMaxLines​(
Line.Info
info)
```

Obtains the approximate maximum number of lines of the requested type
that can be open simultaneously on the mixer.

Certain types of mixers do not have a hard bound and may allow opening
more lines. Since certain lines are a shared resource, a mixer may not be
able to open the maximum number of lines if another process has opened
lines of this mixer.

The requested type is any line that matches the description in the
provided

Line.Info

object. For example, if the info object
represents a speaker port, and the mixer supports exactly one speaker
port, this method should return 1. If the info object represents a source
data line and the mixer supports the use of 32 source data lines
simultaneously, the return value should be 32. If there is no limit, this
function returns

AudioSystem.NOT_SPECIFIED

.

**Parameters:** info

- a

Line.Info

that describes the line for which the
number of supported instances is queried
**Returns:** the maximum number of matching lines supported, or

AudioSystem.NOT_SPECIFIED

- getSourceLines

```java
Line
[] getSourceLines()
```

Obtains the set of all source lines currently open to this mixer.

**Returns:** the source lines currently open to the mixer. If no source lines
are currently open to this mixer, an array of length 0 is
returned.
**Throws:** SecurityException

- if the matching lines are not available due to
security restrictions

- getTargetLines

```java
Line
[] getTargetLines()
```

Obtains the set of all target lines currently open from this mixer.

**Returns:** target lines currently open from the mixer. If no target lines
are currently open from this mixer, an array of length 0 is
returned.
**Throws:** SecurityException

- if the matching lines are not available due to
security restrictions

- synchronize

```java
void synchronize​(
Line
[] lines,
boolean maintainSync)
```

Synchronizes two or more lines. Any subsequent command that starts or
stops audio playback or capture for one of these lines will exert the
same effect on the other lines in the group, so that they start or stop
playing or capturing data simultaneously.

**Parameters:** lines

- the lines that should be synchronized
**Parameters:** maintainSync

-

true

if the synchronization must be
precisely maintained (i.e., the synchronization must be
sample-accurate) at all times during operation of the lines, or

false

if precise synchronization is required only during
start and stop operations
**Throws:** IllegalArgumentException

- if the lines cannot be synchronized.
This may occur if the lines are of different types or have
different formats for which this mixer does not support
synchronization, or if all lines specified do not belong to this
mixer.

- unsynchronize

```java
void unsynchronize​(
Line
[] lines)
```

Releases synchronization for the specified lines. The array must be
identical to one for which synchronization has already been established;
otherwise an exception may be thrown. However,

null

may be
specified, in which case all currently synchronized lines that belong to
this mixer are unsynchronized.

**Parameters:** lines

- the synchronized lines for which synchronization should be
released, or

null

for all this mixer's synchronized lines
**Throws:** IllegalArgumentException

- if the lines cannot be unsynchronized.
This may occur if the argument specified does not exactly match a
set of lines for which synchronization has already been
established.

- isSynchronizationSupported

```java
boolean isSynchronizationSupported​(
Line
[] lines,
boolean maintainSync)
```

Reports whether this mixer supports synchronization of the specified set
of lines.

**Parameters:** lines

- the set of lines for which synchronization support is
queried
**Parameters:** maintainSync

-

true

if the synchronization must be
precisely maintained (i.e., the synchronization must be
sample-accurate) at all times during operation of the lines, or

false

if precise synchronization is required only during
start and stop operations
**Returns:** true

if the lines can be synchronized,

false

otherwise

Method Detail

- getMixerInfo

```java
Mixer.Info
getMixerInfo()
```

Obtains information about this mixer, including the product's name,
version, vendor, etc.

**Returns:** a mixer info object that describes this mixer
**See Also:** Mixer.Info

- getSourceLineInfo

```java
Line.Info
[] getSourceLineInfo()
```

Obtains information about the set of source lines supported by this
mixer. Some source lines may only be available when this mixer is open.

**Returns:** array of

Line.Info

objects representing source lines for
this mixer. If no source lines are supported, an array of length
0 is returned.

- getTargetLineInfo

```java
Line.Info
[] getTargetLineInfo()
```

Obtains information about the set of target lines supported by this
mixer. Some target lines may only be available when this mixer is open.

**Returns:** array of

Line.Info

objects representing target lines for
this mixer. If no target lines are supported, an array of length
0 is returned.

- getSourceLineInfo

```java
Line.Info
[] getSourceLineInfo​(
Line.Info
info)
```

Obtains information about source lines of a particular type supported by
the mixer. Some source lines may only be available when this mixer is
open.

**Parameters:** info

- a

Line.Info

object describing lines about which
information is queried
**Returns:** an array of

Line.Info

objects describing source lines
matching the type requested. If no matching source lines are
supported, an array of length 0 is returned.

- getTargetLineInfo

```java
Line.Info
[] getTargetLineInfo​(
Line.Info
info)
```

Obtains information about target lines of a particular type supported by
the mixer. Some target lines may only be available when this mixer is
open.

**Parameters:** info

- a

Line.Info

object describing lines about which
information is queried
**Returns:** an array of

Line.Info

objects describing target lines
matching the type requested. If no matching target lines are
supported, an array of length 0 is returned.

- isLineSupported

```java
boolean isLineSupported​(
Line.Info
info)
```

Indicates whether the mixer supports a line (or lines) that match the
specified

Line.Info

object. Some lines may only be supported when
this mixer is open.

**Parameters:** info

- describes the line for which support is queried
**Returns:** true

if at least one matching line is supported,

false

otherwise

- getLine

```java
Line
getLine​(
Line.Info
info)
throws
LineUnavailableException
```

Obtains a line that is available for use and that matches the description
in the specified

Line.Info

object.

If a

DataLine

is requested, and

info

is an instance of

DataLine.Info

specifying at least one fully qualified audio
format, the last one will be used as the default format of the returned

DataLine

.

**Parameters:** info

- describes the desired line
**Returns:** a line that is available for use and that matches the description
in the specified

Line.Info

object
**Throws:** LineUnavailableException

- if a matching line is not available due
to resource restrictions
**Throws:** IllegalArgumentException

- if this mixer does not support any lines
matching the description
**Throws:** SecurityException

- if a matching line is not available due to
security restrictions

- getMaxLines

```java
int getMaxLines​(
Line.Info
info)
```

Obtains the approximate maximum number of lines of the requested type
that can be open simultaneously on the mixer.

Certain types of mixers do not have a hard bound and may allow opening
more lines. Since certain lines are a shared resource, a mixer may not be
able to open the maximum number of lines if another process has opened
lines of this mixer.

The requested type is any line that matches the description in the
provided

Line.Info

object. For example, if the info object
represents a speaker port, and the mixer supports exactly one speaker
port, this method should return 1. If the info object represents a source
data line and the mixer supports the use of 32 source data lines
simultaneously, the return value should be 32. If there is no limit, this
function returns

AudioSystem.NOT_SPECIFIED

.

**Parameters:** info

- a

Line.Info

that describes the line for which the
number of supported instances is queried
**Returns:** the maximum number of matching lines supported, or

AudioSystem.NOT_SPECIFIED

- getSourceLines

```java
Line
[] getSourceLines()
```

Obtains the set of all source lines currently open to this mixer.

**Returns:** the source lines currently open to the mixer. If no source lines
are currently open to this mixer, an array of length 0 is
returned.
**Throws:** SecurityException

- if the matching lines are not available due to
security restrictions

- getTargetLines

```java
Line
[] getTargetLines()
```

Obtains the set of all target lines currently open from this mixer.

**Returns:** target lines currently open from the mixer. If no target lines
are currently open from this mixer, an array of length 0 is
returned.
**Throws:** SecurityException

- if the matching lines are not available due to
security restrictions

- synchronize

```java
void synchronize​(
Line
[] lines,
boolean maintainSync)
```

Synchronizes two or more lines. Any subsequent command that starts or
stops audio playback or capture for one of these lines will exert the
same effect on the other lines in the group, so that they start or stop
playing or capturing data simultaneously.

**Parameters:** lines

- the lines that should be synchronized
**Parameters:** maintainSync

-

true

if the synchronization must be
precisely maintained (i.e., the synchronization must be
sample-accurate) at all times during operation of the lines, or

false

if precise synchronization is required only during
start and stop operations
**Throws:** IllegalArgumentException

- if the lines cannot be synchronized.
This may occur if the lines are of different types or have
different formats for which this mixer does not support
synchronization, or if all lines specified do not belong to this
mixer.

- unsynchronize

```java
void unsynchronize​(
Line
[] lines)
```

Releases synchronization for the specified lines. The array must be
identical to one for which synchronization has already been established;
otherwise an exception may be thrown. However,

null

may be
specified, in which case all currently synchronized lines that belong to
this mixer are unsynchronized.

**Parameters:** lines

- the synchronized lines for which synchronization should be
released, or

null

for all this mixer's synchronized lines
**Throws:** IllegalArgumentException

- if the lines cannot be unsynchronized.
This may occur if the argument specified does not exactly match a
set of lines for which synchronization has already been
established.

- isSynchronizationSupported

```java
boolean isSynchronizationSupported​(
Line
[] lines,
boolean maintainSync)
```

Reports whether this mixer supports synchronization of the specified set
of lines.

**Parameters:** lines

- the set of lines for which synchronization support is
queried
**Parameters:** maintainSync

-

true

if the synchronization must be
precisely maintained (i.e., the synchronization must be
sample-accurate) at all times during operation of the lines, or

false

if precise synchronization is required only during
start and stop operations
**Returns:** true

if the lines can be synchronized,

false

otherwise

---

#### Method Detail

getMixerInfo

```java
Mixer.Info
getMixerInfo()
```

Obtains information about this mixer, including the product's name,
version, vendor, etc.

**Returns:** a mixer info object that describes this mixer
**See Also:** Mixer.Info

---

#### getMixerInfo

Mixer.Info

getMixerInfo()

Obtains information about this mixer, including the product's name,
version, vendor, etc.

getSourceLineInfo

```java
Line.Info
[] getSourceLineInfo()
```

Obtains information about the set of source lines supported by this
mixer. Some source lines may only be available when this mixer is open.

**Returns:** array of

Line.Info

objects representing source lines for
this mixer. If no source lines are supported, an array of length
0 is returned.

---

#### getSourceLineInfo

Line.Info

[] getSourceLineInfo()

Obtains information about the set of source lines supported by this
mixer. Some source lines may only be available when this mixer is open.

getTargetLineInfo

```java
Line.Info
[] getTargetLineInfo()
```

Obtains information about the set of target lines supported by this
mixer. Some target lines may only be available when this mixer is open.

**Returns:** array of

Line.Info

objects representing target lines for
this mixer. If no target lines are supported, an array of length
0 is returned.

---

#### getTargetLineInfo

Line.Info

[] getTargetLineInfo()

Obtains information about the set of target lines supported by this
mixer. Some target lines may only be available when this mixer is open.

getSourceLineInfo

```java
Line.Info
[] getSourceLineInfo​(
Line.Info
info)
```

Obtains information about source lines of a particular type supported by
the mixer. Some source lines may only be available when this mixer is
open.

**Parameters:** info

- a

Line.Info

object describing lines about which
information is queried
**Returns:** an array of

Line.Info

objects describing source lines
matching the type requested. If no matching source lines are
supported, an array of length 0 is returned.

---

#### getSourceLineInfo

Line.Info

[] getSourceLineInfo​(

Line.Info

info)

Obtains information about source lines of a particular type supported by
the mixer. Some source lines may only be available when this mixer is
open.

getTargetLineInfo

```java
Line.Info
[] getTargetLineInfo​(
Line.Info
info)
```

Obtains information about target lines of a particular type supported by
the mixer. Some target lines may only be available when this mixer is
open.

**Parameters:** info

- a

Line.Info

object describing lines about which
information is queried
**Returns:** an array of

Line.Info

objects describing target lines
matching the type requested. If no matching target lines are
supported, an array of length 0 is returned.

---

#### getTargetLineInfo

Line.Info

[] getTargetLineInfo​(

Line.Info

info)

Obtains information about target lines of a particular type supported by
the mixer. Some target lines may only be available when this mixer is
open.

isLineSupported

```java
boolean isLineSupported​(
Line.Info
info)
```

Indicates whether the mixer supports a line (or lines) that match the
specified

Line.Info

object. Some lines may only be supported when
this mixer is open.

**Parameters:** info

- describes the line for which support is queried
**Returns:** true

if at least one matching line is supported,

false

otherwise

---

#### isLineSupported

boolean isLineSupported​(

Line.Info

info)

Indicates whether the mixer supports a line (or lines) that match the
specified

Line.Info

object. Some lines may only be supported when
this mixer is open.

getLine

```java
Line
getLine​(
Line.Info
info)
throws
LineUnavailableException
```

Obtains a line that is available for use and that matches the description
in the specified

Line.Info

object.

If a

DataLine

is requested, and

info

is an instance of

DataLine.Info

specifying at least one fully qualified audio
format, the last one will be used as the default format of the returned

DataLine

.

**Parameters:** info

- describes the desired line
**Returns:** a line that is available for use and that matches the description
in the specified

Line.Info

object
**Throws:** LineUnavailableException

- if a matching line is not available due
to resource restrictions
**Throws:** IllegalArgumentException

- if this mixer does not support any lines
matching the description
**Throws:** SecurityException

- if a matching line is not available due to
security restrictions

---

#### getLine

Line

getLine​(

Line.Info

info)
throws

LineUnavailableException

Obtains a line that is available for use and that matches the description
in the specified

Line.Info

object.

If a

DataLine

is requested, and

info

is an instance of

DataLine.Info

specifying at least one fully qualified audio
format, the last one will be used as the default format of the returned

DataLine

.

If a

DataLine

is requested, and

info

is an instance of

DataLine.Info

specifying at least one fully qualified audio
format, the last one will be used as the default format of the returned

DataLine

.

getMaxLines

```java
int getMaxLines​(
Line.Info
info)
```

Obtains the approximate maximum number of lines of the requested type
that can be open simultaneously on the mixer.

Certain types of mixers do not have a hard bound and may allow opening
more lines. Since certain lines are a shared resource, a mixer may not be
able to open the maximum number of lines if another process has opened
lines of this mixer.

The requested type is any line that matches the description in the
provided

Line.Info

object. For example, if the info object
represents a speaker port, and the mixer supports exactly one speaker
port, this method should return 1. If the info object represents a source
data line and the mixer supports the use of 32 source data lines
simultaneously, the return value should be 32. If there is no limit, this
function returns

AudioSystem.NOT_SPECIFIED

.

**Parameters:** info

- a

Line.Info

that describes the line for which the
number of supported instances is queried
**Returns:** the maximum number of matching lines supported, or

AudioSystem.NOT_SPECIFIED

---

#### getMaxLines

int getMaxLines​(

Line.Info

info)

Obtains the approximate maximum number of lines of the requested type
that can be open simultaneously on the mixer.

Certain types of mixers do not have a hard bound and may allow opening
more lines. Since certain lines are a shared resource, a mixer may not be
able to open the maximum number of lines if another process has opened
lines of this mixer.

The requested type is any line that matches the description in the
provided

Line.Info

object. For example, if the info object
represents a speaker port, and the mixer supports exactly one speaker
port, this method should return 1. If the info object represents a source
data line and the mixer supports the use of 32 source data lines
simultaneously, the return value should be 32. If there is no limit, this
function returns

AudioSystem.NOT_SPECIFIED

.

Certain types of mixers do not have a hard bound and may allow opening
more lines. Since certain lines are a shared resource, a mixer may not be
able to open the maximum number of lines if another process has opened
lines of this mixer.

The requested type is any line that matches the description in the
provided

Line.Info

object. For example, if the info object
represents a speaker port, and the mixer supports exactly one speaker
port, this method should return 1. If the info object represents a source
data line and the mixer supports the use of 32 source data lines
simultaneously, the return value should be 32. If there is no limit, this
function returns

AudioSystem.NOT_SPECIFIED

.

The requested type is any line that matches the description in the
provided

Line.Info

object. For example, if the info object
represents a speaker port, and the mixer supports exactly one speaker
port, this method should return 1. If the info object represents a source
data line and the mixer supports the use of 32 source data lines
simultaneously, the return value should be 32. If there is no limit, this
function returns

AudioSystem.NOT_SPECIFIED

.

getSourceLines

```java
Line
[] getSourceLines()
```

Obtains the set of all source lines currently open to this mixer.

**Returns:** the source lines currently open to the mixer. If no source lines
are currently open to this mixer, an array of length 0 is
returned.
**Throws:** SecurityException

- if the matching lines are not available due to
security restrictions

---

#### getSourceLines

Line

[] getSourceLines()

Obtains the set of all source lines currently open to this mixer.

getTargetLines

```java
Line
[] getTargetLines()
```

Obtains the set of all target lines currently open from this mixer.

**Returns:** target lines currently open from the mixer. If no target lines
are currently open from this mixer, an array of length 0 is
returned.
**Throws:** SecurityException

- if the matching lines are not available due to
security restrictions

---

#### getTargetLines

Line

[] getTargetLines()

Obtains the set of all target lines currently open from this mixer.

synchronize

```java
void synchronize​(
Line
[] lines,
boolean maintainSync)
```

Synchronizes two or more lines. Any subsequent command that starts or
stops audio playback or capture for one of these lines will exert the
same effect on the other lines in the group, so that they start or stop
playing or capturing data simultaneously.

**Parameters:** lines

- the lines that should be synchronized
**Parameters:** maintainSync

-

true

if the synchronization must be
precisely maintained (i.e., the synchronization must be
sample-accurate) at all times during operation of the lines, or

false

if precise synchronization is required only during
start and stop operations
**Throws:** IllegalArgumentException

- if the lines cannot be synchronized.
This may occur if the lines are of different types or have
different formats for which this mixer does not support
synchronization, or if all lines specified do not belong to this
mixer.

---

#### synchronize

void synchronize​(

Line

[] lines,
boolean maintainSync)

Synchronizes two or more lines. Any subsequent command that starts or
stops audio playback or capture for one of these lines will exert the
same effect on the other lines in the group, so that they start or stop
playing or capturing data simultaneously.

unsynchronize

```java
void unsynchronize​(
Line
[] lines)
```

Releases synchronization for the specified lines. The array must be
identical to one for which synchronization has already been established;
otherwise an exception may be thrown. However,

null

may be
specified, in which case all currently synchronized lines that belong to
this mixer are unsynchronized.

**Parameters:** lines

- the synchronized lines for which synchronization should be
released, or

null

for all this mixer's synchronized lines
**Throws:** IllegalArgumentException

- if the lines cannot be unsynchronized.
This may occur if the argument specified does not exactly match a
set of lines for which synchronization has already been
established.

---

#### unsynchronize

void unsynchronize​(

Line

[] lines)

Releases synchronization for the specified lines. The array must be
identical to one for which synchronization has already been established;
otherwise an exception may be thrown. However,

null

may be
specified, in which case all currently synchronized lines that belong to
this mixer are unsynchronized.

isSynchronizationSupported

```java
boolean isSynchronizationSupported​(
Line
[] lines,
boolean maintainSync)
```

Reports whether this mixer supports synchronization of the specified set
of lines.

**Parameters:** lines

- the set of lines for which synchronization support is
queried
**Parameters:** maintainSync

-

true

if the synchronization must be
precisely maintained (i.e., the synchronization must be
sample-accurate) at all times during operation of the lines, or

false

if precise synchronization is required only during
start and stop operations
**Returns:** true

if the lines can be synchronized,

false

otherwise

---

#### isSynchronizationSupported

boolean isSynchronizationSupported​(

Line

[] lines,
boolean maintainSync)

Reports whether this mixer supports synchronization of the specified set
of lines.

---

