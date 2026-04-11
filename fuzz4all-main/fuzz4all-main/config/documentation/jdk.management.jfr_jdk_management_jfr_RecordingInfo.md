# Class RecordingInfo

**Source:** `jdk.management.jfr\jdk\management\jfr\RecordingInfo.html`

### Class Description

```java
public final class
RecordingInfo

extends
Object
```

Management representation of a

Recording

.

**Since:** 9
**See Also:** Recording

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### public
String
getName()

Returns the name of the recording associated with this

RecordingInfo

.

**Returns:**
- the recording name, not

null

**See Also:**
- Recording.getName()

---

#### public long getId()

Returns the unique ID for the recording associated with this

RecordingInfo

.

**Returns:**
- the recording ID

**See Also:**
- Recording.getId()

---

#### public boolean getDumpOnExit()

Returns if the recording associated with this

RecordingInfo

should be dumped to file when the JVM exits.

**Returns:**
- true

if recording should be dumped on exit,

false

otherwise

**See Also:**
- Recording.getDumpOnExit()

---

#### public long getMaxAge()

Returns how many seconds data should be kept on disk, or

0

if
data is to be kept forever.

In-memory recordings are not affected by maximum age.

**Returns:**
- how long data should be kept on disk, measured in seconds

**See Also:**
- Recording.getMaxAge()

,

Recording.setToDisk(boolean)

---

#### public long getMaxSize()

Returns the amount of data, measured in bytes, the recording associated
with this

RecordingInfo

, should be kept on disk, before it's
rotated away, or

0

if data is to be kept indefinitely.

In-memory recordings are not affected by maximum size.

**Returns:**
- the amount of data should be kept on disk, in bytes

**See Also:**
- Recording.setToDisk(boolean)

,

Recording.getMaxSize()

---

#### public
String
getState()

Returns a

String

representation of state of the recording
associated with this

RecordingInfo

.

Valid return values are

"NEW"

,

"DELAYED"

,

"STARTING"

,

"RUNNING"

,

"STOPPING"

,

"STOPPED"

and

"CLOSED"

.

**Returns:**
- the recording state, not

null

**See Also:**
- Enum.toString()

,

Recording.getState()

---

#### public long getStartTime()

Returns start time of the recording associated with this

RecordingInfo

, measured as ms since epoch, or

null

if the
recording hasn't started.

**Returns:**
- the start time of the recording, or

null

if the recording
hasn't started

**See Also:**
- Recording.getStartTime()

---

#### public long getStopTime()

Returns the actual or expected stop time of the recording associated with
this

RecordingInfo

, measured as ms since epoch, or

null

if the expected or actual stop time is not known, which can only happen
if the recording has not yet been stopped.

**Returns:**
- the stop time of recording, or

null

if recording hasn't
been stopped.

**See Also:**
- Recording.getStopTime()

---

#### public
Map
<
String
,​
String
> getSettings()

Returns the settings for the recording associated with this

RecordingInfo

.

**Returns:**
- the recording settings, not

null

**See Also:**
- Recording.getSettings()

---

#### public
String
getDestination()

Returns destination path where data, for the recording associated with
this

RecordingInfo

, should be written when the recording stops,
or

null

if the recording should not be written.

**Returns:**
- the destination, or

null

if not set

**See Also:**
- Recording.getDestination()

---

#### public
String
toString()

Returns a string description of the recording associated with this

RecordingInfo

**Overrides:**
- toString

in class

Object

**Returns:**
- description, not

null

---

#### public long getSize()

Returns the amount data recorded by recording. associated with this

RecordingInfo

.

**Returns:**
- the amount of recorded data, measured in bytes

---

#### public boolean isToDisk()

Returns

true

if the recording associated with this

RecordingInfo

should be flushed to disk, when memory buffers are
full,

false

otherwise.

**Returns:**
- true

if recording is to disk,

false

otherwise

---

#### public long getDuration()

Returns the desired duration, measured in seconds, of the recording
associated with this

RecordingInfo

, or {code 0} if no duration
has been set.

**Returns:**
- the desired duration, or {code 0} if no duration has been set

**See Also:**
- Recording.getDuration()

---

#### public static
RecordingInfo
from​(
CompositeData
cd)

Returns a

RecordingInfo

represented by the specified

CompositeData

object.

The specified

CompositeData

must have the following item names and
item types to be valid.

Supported names and types in a specified

CompositeData

object

Name

Type

id

Long

name

String

state

String

dumpOnExit

Boolean

size

Long

toDisk

Boolean

maxAge

Long

maxSize

Long

startTime

Long

stopTime

Long

destination

String

duration

Long

settings

javax.management.openmbean.CompositeData[]

whose element type
is the mapped type for

SettingDescriptorInfo

as specified in the

SettingDescriptorInfo.from(javax.management.openmbean.CompositeData)

method.

**Parameters:**
- cd

-

CompositeData

representing the

RecordingInfo

to
return

**Returns:**
- the

RecordingInfo

represented by

cd

, or

null

if

cd

is

null

**Throws:**
- IllegalArgumentException

- if

cd

does not represent a valid

RecordingInfo

---

### Additional Sections

#### Class RecordingInfo

java.lang.Object

- jdk.management.jfr.RecordingInfo

jdk.management.jfr.RecordingInfo

```java
public final class
RecordingInfo

extends
Object
```

Management representation of a

Recording

.

**Since:** 9
**See Also:** Recording

public final class

RecordingInfo

extends

Object

Management representation of a

Recording

.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

static

RecordingInfo

from

​(

CompositeData

cd)

Returns a

RecordingInfo

represented by the specified

CompositeData

object.

String

getDestination

()

Returns destination path where data, for the recording associated with
this

RecordingInfo

, should be written when the recording stops,
or

null

if the recording should not be written.

boolean

getDumpOnExit

()

Returns if the recording associated with this

RecordingInfo

should be dumped to file when the JVM exits.

long

getDuration

()

Returns the desired duration, measured in seconds, of the recording
associated with this

RecordingInfo

, or {code 0} if no duration
has been set.

long

getId

()

Returns the unique ID for the recording associated with this

RecordingInfo

.

long

getMaxAge

()

Returns how many seconds data should be kept on disk, or

0

if
data is to be kept forever.

long

getMaxSize

()

Returns the amount of data, measured in bytes, the recording associated
with this

RecordingInfo

, should be kept on disk, before it's
rotated away, or

0

if data is to be kept indefinitely.

String

getName

()

Returns the name of the recording associated with this

RecordingInfo

.

Map

<

String

,​

String

>

getSettings

()

Returns the settings for the recording associated with this

RecordingInfo

.

long

getSize

()

Returns the amount data recorded by recording. associated with this

RecordingInfo

.

long

getStartTime

()

Returns start time of the recording associated with this

RecordingInfo

, measured as ms since epoch, or

null

if the
recording hasn't started.

String

getState

()

Returns a

String

representation of state of the recording
associated with this

RecordingInfo

.

long

getStopTime

()

Returns the actual or expected stop time of the recording associated with
this

RecordingInfo

, measured as ms since epoch, or

null

if the expected or actual stop time is not known, which can only happen
if the recording has not yet been stopped.

boolean

isToDisk

()

Returns

true

if the recording associated with this

RecordingInfo

should be flushed to disk, when memory buffers are
full,

false

otherwise.

String

toString

()

Returns a string description of the recording associated with this

RecordingInfo

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

Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

static

RecordingInfo

from

​(

CompositeData

cd)

Returns a

RecordingInfo

represented by the specified

CompositeData

object.

String

getDestination

()

Returns destination path where data, for the recording associated with
this

RecordingInfo

, should be written when the recording stops,
or

null

if the recording should not be written.

boolean

getDumpOnExit

()

Returns if the recording associated with this

RecordingInfo

should be dumped to file when the JVM exits.

long

getDuration

()

Returns the desired duration, measured in seconds, of the recording
associated with this

RecordingInfo

, or {code 0} if no duration
has been set.

long

getId

()

Returns the unique ID for the recording associated with this

RecordingInfo

.

long

getMaxAge

()

Returns how many seconds data should be kept on disk, or

0

if
data is to be kept forever.

long

getMaxSize

()

Returns the amount of data, measured in bytes, the recording associated
with this

RecordingInfo

, should be kept on disk, before it's
rotated away, or

0

if data is to be kept indefinitely.

String

getName

()

Returns the name of the recording associated with this

RecordingInfo

.

Map

<

String

,​

String

>

getSettings

()

Returns the settings for the recording associated with this

RecordingInfo

.

long

getSize

()

Returns the amount data recorded by recording. associated with this

RecordingInfo

.

long

getStartTime

()

Returns start time of the recording associated with this

RecordingInfo

, measured as ms since epoch, or

null

if the
recording hasn't started.

String

getState

()

Returns a

String

representation of state of the recording
associated with this

RecordingInfo

.

long

getStopTime

()

Returns the actual or expected stop time of the recording associated with
this

RecordingInfo

, measured as ms since epoch, or

null

if the expected or actual stop time is not known, which can only happen
if the recording has not yet been stopped.

boolean

isToDisk

()

Returns

true

if the recording associated with this

RecordingInfo

should be flushed to disk, when memory buffers are
full,

false

otherwise.

String

toString

()

Returns a string description of the recording associated with this

RecordingInfo

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

Returns a

RecordingInfo

represented by the specified

CompositeData

object.

Returns destination path where data, for the recording associated with
this

RecordingInfo

, should be written when the recording stops,
or

null

if the recording should not be written.

Returns if the recording associated with this

RecordingInfo

should be dumped to file when the JVM exits.

Returns the desired duration, measured in seconds, of the recording
associated with this

RecordingInfo

, or {code 0} if no duration
has been set.

Returns the unique ID for the recording associated with this

RecordingInfo

.

Returns how many seconds data should be kept on disk, or

0

if
data is to be kept forever.

Returns the amount of data, measured in bytes, the recording associated
with this

RecordingInfo

, should be kept on disk, before it's
rotated away, or

0

if data is to be kept indefinitely.

Returns the name of the recording associated with this

RecordingInfo

.

Returns the settings for the recording associated with this

RecordingInfo

.

Returns the amount data recorded by recording. associated with this

RecordingInfo

.

Returns start time of the recording associated with this

RecordingInfo

, measured as ms since epoch, or

null

if the
recording hasn't started.

Returns a

String

representation of state of the recording
associated with this

RecordingInfo

.

Returns the actual or expected stop time of the recording associated with
this

RecordingInfo

, measured as ms since epoch, or

null

if the expected or actual stop time is not known, which can only happen
if the recording has not yet been stopped.

Returns

true

if the recording associated with this

RecordingInfo

should be flushed to disk, when memory buffers are
full,

false

otherwise.

Returns a string description of the recording associated with this

RecordingInfo

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

============ METHOD DETAIL ==========

- Method Detail

- getName

```java
public
String
getName()
```

Returns the name of the recording associated with this

RecordingInfo

.

**Returns:** the recording name, not

null
**See Also:** Recording.getName()

- getId

```java
public long getId()
```

Returns the unique ID for the recording associated with this

RecordingInfo

.

**Returns:** the recording ID
**See Also:** Recording.getId()

- getDumpOnExit

```java
public boolean getDumpOnExit()
```

Returns if the recording associated with this

RecordingInfo

should be dumped to file when the JVM exits.

**Returns:** true

if recording should be dumped on exit,

false

otherwise
**See Also:** Recording.getDumpOnExit()

- getMaxAge

```java
public long getMaxAge()
```

Returns how many seconds data should be kept on disk, or

0

if
data is to be kept forever.

In-memory recordings are not affected by maximum age.

**Returns:** how long data should be kept on disk, measured in seconds
**See Also:** Recording.getMaxAge()

,

Recording.setToDisk(boolean)

- getMaxSize

```java
public long getMaxSize()
```

Returns the amount of data, measured in bytes, the recording associated
with this

RecordingInfo

, should be kept on disk, before it's
rotated away, or

0

if data is to be kept indefinitely.

In-memory recordings are not affected by maximum size.

**Returns:** the amount of data should be kept on disk, in bytes
**See Also:** Recording.setToDisk(boolean)

,

Recording.getMaxSize()

- getState

```java
public
String
getState()
```

Returns a

String

representation of state of the recording
associated with this

RecordingInfo

.

Valid return values are

"NEW"

,

"DELAYED"

,

"STARTING"

,

"RUNNING"

,

"STOPPING"

,

"STOPPED"

and

"CLOSED"

.

**Returns:** the recording state, not

null
**See Also:** Enum.toString()

,

Recording.getState()

- getStartTime

```java
public long getStartTime()
```

Returns start time of the recording associated with this

RecordingInfo

, measured as ms since epoch, or

null

if the
recording hasn't started.

**Returns:** the start time of the recording, or

null

if the recording
hasn't started
**See Also:** Recording.getStartTime()

- getStopTime

```java
public long getStopTime()
```

Returns the actual or expected stop time of the recording associated with
this

RecordingInfo

, measured as ms since epoch, or

null

if the expected or actual stop time is not known, which can only happen
if the recording has not yet been stopped.

**Returns:** the stop time of recording, or

null

if recording hasn't
been stopped.
**See Also:** Recording.getStopTime()

- getSettings

```java
public
Map
<
String
,​
String
> getSettings()
```

Returns the settings for the recording associated with this

RecordingInfo

.

**Returns:** the recording settings, not

null
**See Also:** Recording.getSettings()

- getDestination

```java
public
String
getDestination()
```

Returns destination path where data, for the recording associated with
this

RecordingInfo

, should be written when the recording stops,
or

null

if the recording should not be written.

**Returns:** the destination, or

null

if not set
**See Also:** Recording.getDestination()

- toString

```java
public
String
toString()
```

Returns a string description of the recording associated with this

RecordingInfo

**Overrides:** toString

in class

Object
**Returns:** description, not

null

- getSize

```java
public long getSize()
```

Returns the amount data recorded by recording. associated with this

RecordingInfo

.

**Returns:** the amount of recorded data, measured in bytes

- isToDisk

```java
public boolean isToDisk()
```

Returns

true

if the recording associated with this

RecordingInfo

should be flushed to disk, when memory buffers are
full,

false

otherwise.

**Returns:** true

if recording is to disk,

false

otherwise

- getDuration

```java
public long getDuration()
```

Returns the desired duration, measured in seconds, of the recording
associated with this

RecordingInfo

, or {code 0} if no duration
has been set.

**Returns:** the desired duration, or {code 0} if no duration has been set
**See Also:** Recording.getDuration()

- from

```java
public static
RecordingInfo
from​(
CompositeData
cd)
```

Returns a

RecordingInfo

represented by the specified

CompositeData

object.

The specified

CompositeData

must have the following item names and
item types to be valid.

Supported names and types in a specified

CompositeData

object

Name

Type

id

Long

name

String

state

String

dumpOnExit

Boolean

size

Long

toDisk

Boolean

maxAge

Long

maxSize

Long

startTime

Long

stopTime

Long

destination

String

duration

Long

settings

javax.management.openmbean.CompositeData[]

whose element type
is the mapped type for

SettingDescriptorInfo

as specified in the

SettingDescriptorInfo.from(javax.management.openmbean.CompositeData)

method.

**Parameters:** cd

-

CompositeData

representing the

RecordingInfo

to
return
**Returns:** the

RecordingInfo

represented by

cd

, or

null

if

cd

is

null
**Throws:** IllegalArgumentException

- if

cd

does not represent a valid

RecordingInfo

Method Detail

- getName

```java
public
String
getName()
```

Returns the name of the recording associated with this

RecordingInfo

.

**Returns:** the recording name, not

null
**See Also:** Recording.getName()

- getId

```java
public long getId()
```

Returns the unique ID for the recording associated with this

RecordingInfo

.

**Returns:** the recording ID
**See Also:** Recording.getId()

- getDumpOnExit

```java
public boolean getDumpOnExit()
```

Returns if the recording associated with this

RecordingInfo

should be dumped to file when the JVM exits.

**Returns:** true

if recording should be dumped on exit,

false

otherwise
**See Also:** Recording.getDumpOnExit()

- getMaxAge

```java
public long getMaxAge()
```

Returns how many seconds data should be kept on disk, or

0

if
data is to be kept forever.

In-memory recordings are not affected by maximum age.

**Returns:** how long data should be kept on disk, measured in seconds
**See Also:** Recording.getMaxAge()

,

Recording.setToDisk(boolean)

- getMaxSize

```java
public long getMaxSize()
```

Returns the amount of data, measured in bytes, the recording associated
with this

RecordingInfo

, should be kept on disk, before it's
rotated away, or

0

if data is to be kept indefinitely.

In-memory recordings are not affected by maximum size.

**Returns:** the amount of data should be kept on disk, in bytes
**See Also:** Recording.setToDisk(boolean)

,

Recording.getMaxSize()

- getState

```java
public
String
getState()
```

Returns a

String

representation of state of the recording
associated with this

RecordingInfo

.

Valid return values are

"NEW"

,

"DELAYED"

,

"STARTING"

,

"RUNNING"

,

"STOPPING"

,

"STOPPED"

and

"CLOSED"

.

**Returns:** the recording state, not

null
**See Also:** Enum.toString()

,

Recording.getState()

- getStartTime

```java
public long getStartTime()
```

Returns start time of the recording associated with this

RecordingInfo

, measured as ms since epoch, or

null

if the
recording hasn't started.

**Returns:** the start time of the recording, or

null

if the recording
hasn't started
**See Also:** Recording.getStartTime()

- getStopTime

```java
public long getStopTime()
```

Returns the actual or expected stop time of the recording associated with
this

RecordingInfo

, measured as ms since epoch, or

null

if the expected or actual stop time is not known, which can only happen
if the recording has not yet been stopped.

**Returns:** the stop time of recording, or

null

if recording hasn't
been stopped.
**See Also:** Recording.getStopTime()

- getSettings

```java
public
Map
<
String
,​
String
> getSettings()
```

Returns the settings for the recording associated with this

RecordingInfo

.

**Returns:** the recording settings, not

null
**See Also:** Recording.getSettings()

- getDestination

```java
public
String
getDestination()
```

Returns destination path where data, for the recording associated with
this

RecordingInfo

, should be written when the recording stops,
or

null

if the recording should not be written.

**Returns:** the destination, or

null

if not set
**See Also:** Recording.getDestination()

- toString

```java
public
String
toString()
```

Returns a string description of the recording associated with this

RecordingInfo

**Overrides:** toString

in class

Object
**Returns:** description, not

null

- getSize

```java
public long getSize()
```

Returns the amount data recorded by recording. associated with this

RecordingInfo

.

**Returns:** the amount of recorded data, measured in bytes

- isToDisk

```java
public boolean isToDisk()
```

Returns

true

if the recording associated with this

RecordingInfo

should be flushed to disk, when memory buffers are
full,

false

otherwise.

**Returns:** true

if recording is to disk,

false

otherwise

- getDuration

```java
public long getDuration()
```

Returns the desired duration, measured in seconds, of the recording
associated with this

RecordingInfo

, or {code 0} if no duration
has been set.

**Returns:** the desired duration, or {code 0} if no duration has been set
**See Also:** Recording.getDuration()

- from

```java
public static
RecordingInfo
from​(
CompositeData
cd)
```

Returns a

RecordingInfo

represented by the specified

CompositeData

object.

The specified

CompositeData

must have the following item names and
item types to be valid.

Supported names and types in a specified

CompositeData

object

Name

Type

id

Long

name

String

state

String

dumpOnExit

Boolean

size

Long

toDisk

Boolean

maxAge

Long

maxSize

Long

startTime

Long

stopTime

Long

destination

String

duration

Long

settings

javax.management.openmbean.CompositeData[]

whose element type
is the mapped type for

SettingDescriptorInfo

as specified in the

SettingDescriptorInfo.from(javax.management.openmbean.CompositeData)

method.

**Parameters:** cd

-

CompositeData

representing the

RecordingInfo

to
return
**Returns:** the

RecordingInfo

represented by

cd

, or

null

if

cd

is

null
**Throws:** IllegalArgumentException

- if

cd

does not represent a valid

RecordingInfo

---

#### Method Detail

getName

```java
public
String
getName()
```

Returns the name of the recording associated with this

RecordingInfo

.

**Returns:** the recording name, not

null
**See Also:** Recording.getName()

---

#### getName

public

String

getName()

Returns the name of the recording associated with this

RecordingInfo

.

getId

```java
public long getId()
```

Returns the unique ID for the recording associated with this

RecordingInfo

.

**Returns:** the recording ID
**See Also:** Recording.getId()

---

#### getId

public long getId()

Returns the unique ID for the recording associated with this

RecordingInfo

.

getDumpOnExit

```java
public boolean getDumpOnExit()
```

Returns if the recording associated with this

RecordingInfo

should be dumped to file when the JVM exits.

**Returns:** true

if recording should be dumped on exit,

false

otherwise
**See Also:** Recording.getDumpOnExit()

---

#### getDumpOnExit

public boolean getDumpOnExit()

Returns if the recording associated with this

RecordingInfo

should be dumped to file when the JVM exits.

getMaxAge

```java
public long getMaxAge()
```

Returns how many seconds data should be kept on disk, or

0

if
data is to be kept forever.

In-memory recordings are not affected by maximum age.

**Returns:** how long data should be kept on disk, measured in seconds
**See Also:** Recording.getMaxAge()

,

Recording.setToDisk(boolean)

---

#### getMaxAge

public long getMaxAge()

Returns how many seconds data should be kept on disk, or

0

if
data is to be kept forever.

In-memory recordings are not affected by maximum age.

In-memory recordings are not affected by maximum age.

getMaxSize

```java
public long getMaxSize()
```

Returns the amount of data, measured in bytes, the recording associated
with this

RecordingInfo

, should be kept on disk, before it's
rotated away, or

0

if data is to be kept indefinitely.

In-memory recordings are not affected by maximum size.

**Returns:** the amount of data should be kept on disk, in bytes
**See Also:** Recording.setToDisk(boolean)

,

Recording.getMaxSize()

---

#### getMaxSize

public long getMaxSize()

Returns the amount of data, measured in bytes, the recording associated
with this

RecordingInfo

, should be kept on disk, before it's
rotated away, or

0

if data is to be kept indefinitely.

In-memory recordings are not affected by maximum size.

In-memory recordings are not affected by maximum size.

getState

```java
public
String
getState()
```

Returns a

String

representation of state of the recording
associated with this

RecordingInfo

.

Valid return values are

"NEW"

,

"DELAYED"

,

"STARTING"

,

"RUNNING"

,

"STOPPING"

,

"STOPPED"

and

"CLOSED"

.

**Returns:** the recording state, not

null
**See Also:** Enum.toString()

,

Recording.getState()

---

#### getState

public

String

getState()

Returns a

String

representation of state of the recording
associated with this

RecordingInfo

.

Valid return values are

"NEW"

,

"DELAYED"

,

"STARTING"

,

"RUNNING"

,

"STOPPING"

,

"STOPPED"

and

"CLOSED"

.

Valid return values are

"NEW"

,

"DELAYED"

,

"STARTING"

,

"RUNNING"

,

"STOPPING"

,

"STOPPED"

and

"CLOSED"

.

getStartTime

```java
public long getStartTime()
```

Returns start time of the recording associated with this

RecordingInfo

, measured as ms since epoch, or

null

if the
recording hasn't started.

**Returns:** the start time of the recording, or

null

if the recording
hasn't started
**See Also:** Recording.getStartTime()

---

#### getStartTime

public long getStartTime()

Returns start time of the recording associated with this

RecordingInfo

, measured as ms since epoch, or

null

if the
recording hasn't started.

getStopTime

```java
public long getStopTime()
```

Returns the actual or expected stop time of the recording associated with
this

RecordingInfo

, measured as ms since epoch, or

null

if the expected or actual stop time is not known, which can only happen
if the recording has not yet been stopped.

**Returns:** the stop time of recording, or

null

if recording hasn't
been stopped.
**See Also:** Recording.getStopTime()

---

#### getStopTime

public long getStopTime()

Returns the actual or expected stop time of the recording associated with
this

RecordingInfo

, measured as ms since epoch, or

null

if the expected or actual stop time is not known, which can only happen
if the recording has not yet been stopped.

getSettings

```java
public
Map
<
String
,​
String
> getSettings()
```

Returns the settings for the recording associated with this

RecordingInfo

.

**Returns:** the recording settings, not

null
**See Also:** Recording.getSettings()

---

#### getSettings

public

Map

<

String

,​

String

> getSettings()

Returns the settings for the recording associated with this

RecordingInfo

.

getDestination

```java
public
String
getDestination()
```

Returns destination path where data, for the recording associated with
this

RecordingInfo

, should be written when the recording stops,
or

null

if the recording should not be written.

**Returns:** the destination, or

null

if not set
**See Also:** Recording.getDestination()

---

#### getDestination

public

String

getDestination()

Returns destination path where data, for the recording associated with
this

RecordingInfo

, should be written when the recording stops,
or

null

if the recording should not be written.

toString

```java
public
String
toString()
```

Returns a string description of the recording associated with this

RecordingInfo

**Overrides:** toString

in class

Object
**Returns:** description, not

null

---

#### toString

public

String

toString()

Returns a string description of the recording associated with this

RecordingInfo

getSize

```java
public long getSize()
```

Returns the amount data recorded by recording. associated with this

RecordingInfo

.

**Returns:** the amount of recorded data, measured in bytes

---

#### getSize

public long getSize()

Returns the amount data recorded by recording. associated with this

RecordingInfo

.

isToDisk

```java
public boolean isToDisk()
```

Returns

true

if the recording associated with this

RecordingInfo

should be flushed to disk, when memory buffers are
full,

false

otherwise.

**Returns:** true

if recording is to disk,

false

otherwise

---

#### isToDisk

public boolean isToDisk()

Returns

true

if the recording associated with this

RecordingInfo

should be flushed to disk, when memory buffers are
full,

false

otherwise.

getDuration

```java
public long getDuration()
```

Returns the desired duration, measured in seconds, of the recording
associated with this

RecordingInfo

, or {code 0} if no duration
has been set.

**Returns:** the desired duration, or {code 0} if no duration has been set
**See Also:** Recording.getDuration()

---

#### getDuration

public long getDuration()

Returns the desired duration, measured in seconds, of the recording
associated with this

RecordingInfo

, or {code 0} if no duration
has been set.

from

```java
public static
RecordingInfo
from​(
CompositeData
cd)
```

Returns a

RecordingInfo

represented by the specified

CompositeData

object.

The specified

CompositeData

must have the following item names and
item types to be valid.

Supported names and types in a specified

CompositeData

object

Name

Type

id

Long

name

String

state

String

dumpOnExit

Boolean

size

Long

toDisk

Boolean

maxAge

Long

maxSize

Long

startTime

Long

stopTime

Long

destination

String

duration

Long

settings

javax.management.openmbean.CompositeData[]

whose element type
is the mapped type for

SettingDescriptorInfo

as specified in the

SettingDescriptorInfo.from(javax.management.openmbean.CompositeData)

method.

**Parameters:** cd

-

CompositeData

representing the

RecordingInfo

to
return
**Returns:** the

RecordingInfo

represented by

cd

, or

null

if

cd

is

null
**Throws:** IllegalArgumentException

- if

cd

does not represent a valid

RecordingInfo

---

#### from

public static

RecordingInfo

from​(

CompositeData

cd)

Returns a

RecordingInfo

represented by the specified

CompositeData

object.

The specified

CompositeData

must have the following item names and
item types to be valid.

Supported names and types in a specified

CompositeData

object

Name

Type

id

Long

name

String

state

String

dumpOnExit

Boolean

size

Long

toDisk

Boolean

maxAge

Long

maxSize

Long

startTime

Long

stopTime

Long

destination

String

duration

Long

settings

javax.management.openmbean.CompositeData[]

whose element type
is the mapped type for

SettingDescriptorInfo

as specified in the

SettingDescriptorInfo.from(javax.management.openmbean.CompositeData)

method.

The specified

CompositeData

must have the following item names and
item types to be valid.

Supported names and types in a specified

CompositeData

object

Name

Type

id

Long

name

String

state

String

dumpOnExit

Boolean

size

Long

toDisk

Boolean

maxAge

Long

maxSize

Long

startTime

Long

stopTime

Long

destination

String

duration

Long

settings

javax.management.openmbean.CompositeData[]

whose element type
is the mapped type for

SettingDescriptorInfo

as specified in the

SettingDescriptorInfo.from(javax.management.openmbean.CompositeData)

method.

---

