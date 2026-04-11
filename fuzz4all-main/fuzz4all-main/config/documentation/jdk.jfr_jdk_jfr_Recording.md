# Class Recording

**Source:** `jdk.jfr\jdk\jfr\Recording.html`

### Class Description

```java
public final class
Recording

extends
Object

implements
Closeable
```

Provides means to configure, start, stop and dump recording data to disk.

The following example shows how configure, start, stop and dump recording data to disk.

```java
Configuration c = Configuration.getConfiguration("default");
Recording r = new Recording(c);
r.start();
System.gc();
Thread.sleep(5000);
r.stop();
r.copyTo(Files.createTempFile("my-recording", ".jfr"));
```

**All Implemented Interfaces:** Closeable

,

AutoCloseable

---

### Field Details

*No entries found.*

### Constructor Details

#### public Recording​(
Map
<
String
,​
String
> settings)

*No description found.*

---

#### public Recording()

Creates a recording without any settings.

A newly created recording is in the

RecordingState.NEW

state. To start
the recording, invoke the

start()

method.

**Throws:**
- IllegalStateException

- if Flight Recorder can't be created (for
example, if the Java Virtual Machine (JVM) lacks Flight Recorder
support, or if the file repository can't be created or accessed)
- SecurityException

- If a security manager is used and
FlightRecorderPermission "accessFlightRecorder" is not set.

---

#### public Recording​(
Configuration
configuration)

Creates a recording with settings from a configuration.

The following example shows how create a recording that uses a predefined configuration.

```java
Recording r = new Recording(Configuration.getConfiguration("default"));
```

The newly created recording is in the

RecordingState.NEW

state. To
start the recording, invoke the

start()

method.

**Parameters:**
- configuration

- configuration that contains the settings to be use, not

null

**Throws:**
- IllegalStateException

- if Flight Recorder can't be created (for
example, if the Java Virtual Machine (JVM) lacks Flight Recorder
support, or if the file repository can't be created or accessed)
- SecurityException

- if a security manager is used and
FlightRecorderPermission "accessFlightRecorder" is not set.

**See Also:**
- Configuration

---

### Method Details

#### public void start()

Starts this recording.

It's recommended that the recording options and event settings are configured
before calling this method. The benefits of doing so are a more consistent
state when analyzing the recorded data, and improved performance because the
configuration can be applied atomically.

After a successful invocation of this method, this recording is in the

RUNNING

state.

**Throws:**
- IllegalStateException

- if recording is already started or is in the

CLOSED

state

---

#### public void scheduleStart​(
Duration
delay)

Starts this recording after a delay.

After a successful invocation of this method, this recording is in the

DELAYED

state.

**Parameters:**
- delay

- the time to wait before starting this recording, not

null

**Throws:**
- IllegalStateException

- if the recording is not it the

NEW

state

---

#### public boolean stop()

Stops this recording.

When a recording is stopped it can't be restarted. If this
recording has a destination, data is written to that destination and
the recording is closed. After a recording is closed, the data is no longer
available.

After a successful invocation of this method, this recording will be
in the

STOPPED

state.

**Returns:**
- true

if recording is stopped,

false

otherwise

**Throws:**
- IllegalStateException

- if the recording is not started or is already stopped
- SecurityException

- if a security manager exists and the caller
doesn't have

FilePermission

to write to the destination
path

**See Also:**
- setDestination(Path)

---

#### public
Map
<
String
,​
String
> getSettings()

Returns settings used by this recording.

Modifying the returned

Map

will not change the settings for this recording.

If no settings are set for this recording, an empty

Map

is
returned.

**Returns:**
- recording settings, not

null

---

#### public long getSize()

Returns the current size of this recording in the disk repository,
measured in bytes.

The size is updated when recording buffers are flushed. If the recording is
not written to the disk repository the returned size is always

0

.

**Returns:**
- amount of recorded data, measured in bytes, or

0

if the
recording is not written to the disk repository

---

#### public
Instant
getStopTime()

Returns the time when this recording was stopped.

**Returns:**
- the time, or

null

if this recording is not stopped

---

#### public
Instant
getStartTime()

Returns the time when this recording was started.

**Returns:**
- the the time, or

null

if this recording is not started

---

#### public long getMaxSize()

Returns the maximum size, measured in bytes, at which data is no longer kept in the disk repository.

**Returns:**
- maximum size in bytes, or

0

if no maximum size is set

---

#### public
Duration
getMaxAge()

Returns the length of time that the data is kept in the disk repository
before it is removed.

**Returns:**
- maximum length of time, or

null

if no maximum length of time
has been set

---

#### public
String
getName()

Returns the name of this recording.

By default, the name is the same as the recording ID.

**Returns:**
- the recording name, not

null

---

#### public void setSettings​(
Map
<
String
,​
String
> settings)

Replaces all settings for this recording.

The following example shows how to set event settings for a recording.

```java
Map<String, String> settings = new HashMap<>();
settings.putAll(EventSettings.enabled("jdk.CPUSample").withPeriod(Duration.ofSeconds(2)).toMap());
settings.putAll(EventSettings.enabled(MyEvent.class).withThreshold(Duration.ofSeconds(2)).withoutStackTrace().toMap());
settings.put("jdk.ExecutionSample#period", "10 ms");
recording.setSettings(settings);
```

The following example shows how to merge settings.

```java
Map<String, String> settings = recording.getSettings();
settings.putAll(additionalSettings);
recording.setSettings(settings);
```

**Parameters:**
- settings

- the settings to set, not

null

---

#### public
RecordingState
getState()

Returns the recording state that this recording is currently in.

**Returns:**
- the recording state, not

null

**See Also:**
- RecordingState

---

#### public void close()

Releases all data that is associated with this recording.

After a successful invocation of this method, this recording is in the

CLOSED

state.

**Specified by:**
- close

in interface

AutoCloseable
- close

in interface

Closeable

---

#### public
Recording
copy​(boolean stop)

Returns a clone of this recording, with a new recording ID and name.

Clones are useful for dumping data without stopping the recording. After
a clone is created, the amount of data to copy is constrained
with the

setMaxAge(Duration)

method and the

setMaxSize(long)

method.

**Parameters:**
- stop

-

true

if the newly created copy should be stopped
immediately,

false

otherwise

**Returns:**
- the recording copy, not

null

---

#### public void dump​(
Path
destination)
throws
IOException

Writes recording data to a file.

Recording must be started, but not necessarily stopped.

**Parameters:**
- destination

- the location where recording data is written, not

null

**Throws:**
- IOException

- if the recording can't be copied to the specified
location
- SecurityException

- if a security manager exists and the caller doesn't
have

FilePermission

to write to the destination path

---

#### public boolean isToDisk()

Returns

true

if this recording uses the disk repository,

false

otherwise.

If no value is set,

true

is returned.

**Returns:**
- true

if the recording uses the disk repository,

false

otherwise

---

#### public void setMaxSize​(long maxSize)

Determines how much data is kept in the disk repository.

To control the amount of recording data that is stored on disk, the maximum
amount of data to retain can be specified. When the maximum limit is
exceeded, the Java Virtual Machine (JVM) removes the oldest chunk to make
room for a more recent chunk.

If neither maximum limit or the maximum age is set, the size of the
recording may grow indefinitely.

**Parameters:**
- maxSize

- the amount of data to retain,

0

if infinite

**Throws:**
- IllegalArgumentException

- if

maxSize

is negative
- IllegalStateException

- if the recording is in

CLOSED

state

---

#### public void setMaxAge​(
Duration
maxAge)

Determines how far back data is kept in the disk repository.

To control the amount of recording data stored on disk, the maximum length of
time to retain the data can be specified. Data stored on disk that is older
than the specified length of time is removed by the Java Virtual Machine (JVM).

If neither maximum limit or the maximum age is set, the size of the
recording may grow indefinitely.

**Parameters:**
- maxAge

- the length of time that data is kept, or

null

if infinite

**Throws:**
- IllegalArgumentException

- if

maxAge

is negative
- IllegalStateException

- if the recording is in the

CLOSED

state

---

#### public void setDestination​(
Path
destination)
throws
IOException

Sets a location where data is written on recording stop, or

null

if data is not to be dumped.

If a destination is set, this recording is automatically closed
after data is successfully copied to the destination path.

If a destination is

not

set, Flight Recorder retains the
recording data until this recording is closed. Use the

dump(Path)

method to
manually write data to a file.

**Parameters:**
- destination

- the destination path, or

null

if recording should
not be dumped at stop

**Throws:**
- IllegalStateException

- if recording is in the

STOPPED

or

CLOSED

state.
- SecurityException

- if a security manager exists and the caller
doesn't have

FilePermission

to read, write, and delete the

destination

file
- IOException

- if the path is not writable

---

#### public
Path
getDestination()

Returns the destination file, where recording data is written when the
recording stops, or

null

if no destination is set.

**Returns:**
- the destination file, or

null

if not set.

---

#### public long getId()

Returns a unique ID for this recording.

**Returns:**
- the recording ID

---

#### public void setName​(
String
name)

Sets a human-readable name (for example,

"My Recording"

).

**Parameters:**
- name

- the recording name, not

null

**Throws:**
- IllegalStateException

- if the recording is in

CLOSED

state

---

#### public void setDumpOnExit​(boolean dumpOnExit)

Sets whether this recording is dumped to disk when the JVM exits.

**Parameters:**
- dumpOnExit

- if this recording should be dumped when the JVM exits

---

#### public boolean getDumpOnExit()

Returns whether this recording is dumped to disk when the JVM exits.

If dump on exit is not set,

false

is returned.

**Returns:**
- true

if the recording is dumped on exit,

false

otherwise.

---

#### public void setToDisk​(boolean disk)

Determines whether this recording is continuously flushed to the disk
repository or data is constrained to what is available in memory buffers.

**Parameters:**
- disk

-

true

if this recording is written to disk,

false

if in-memory

---

#### public
InputStream
getStream​(
Instant
start,

Instant
end)
throws
IOException

Creates a data stream for a specified interval.

The stream may contain some data outside the specified range.

**Parameters:**
- the

- start start time for the stream, or

null

to get data from
start time of the recording
- the

- end end time for the stream, or

null

to get data until the
present time.

**Returns:**
- an input stream, or

null

if no data is available in the
interval.

**Throws:**
- IllegalArgumentException

- if

end

happens before

start
- IOException

- if a stream can't be opened

---

#### public
Duration
getDuration()

Returns the specified duration for this recording, or

null

if no
duration is set.

The duration can be set only when the recording is in the

RecordingState.NEW

state.

**Returns:**
- the desired duration of the recording, or

null

if no duration
has been set.

---

#### public void setDuration​(
Duration
duration)

Sets a duration for how long a recording runs before it stops.

By default, a recording has no duration (

null

).

**Parameters:**
- duration

- the duration, or

null

if no duration is set

**Throws:**
- IllegalStateException

- if recording is in the

STOPPED

or

CLOSED

state

---

#### public
EventSettings
enable​(
String
name)

Enables the event with the specified name.

If multiple events have the same name (for example, the same class is loaded
in different class loaders), then all events that match the name are enabled. To
enable a specific class, use the

enable(Class)

method or a

String

representation of the event type ID.

**Parameters:**
- name

- the settings for the event, not

null

**Returns:**
- an event setting for further configuration, not

null

**See Also:**
- EventType

---

#### public
EventSettings
disable​(
String
name)

Disables event with the specified name.

If multiple events with same name (for example, the same class is loaded
in different class loaders), then all events that match the
name is disabled. To disable a specific class, use the

disable(Class)

method or a

String

representation of the event
type ID.

**Parameters:**
- name

- the settings for the event, not

null

**Returns:**
- an event setting for further configuration, not

null

---

#### public
EventSettings
enable​(
Class
<? extends
Event
> eventClass)

Enables event.

**Parameters:**
- eventClass

- the event to enable, not

null

**Returns:**
- an event setting for further configuration, not

null

**Throws:**
- IllegalArgumentException

- if

eventClass

is an abstract
class or not a subclass of

Event

---

#### public
EventSettings
disable​(
Class
<? extends
Event
> eventClass)

Disables event.

**Parameters:**
- eventClass

- the event to enable, not

null

**Returns:**
- an event setting for further configuration, not

null

**Throws:**
- IllegalArgumentException

- if

eventClass

is an abstract
class or not a subclass of

Event

---

### Additional Sections

#### Class Recording

java.lang.Object

- jdk.jfr.Recording

jdk.jfr.Recording

**All Implemented Interfaces:** Closeable

,

AutoCloseable

```java
public final class
Recording

extends
Object

implements
Closeable
```

Provides means to configure, start, stop and dump recording data to disk.

The following example shows how configure, start, stop and dump recording data to disk.

```java
Configuration c = Configuration.getConfiguration("default");
Recording r = new Recording(c);
r.start();
System.gc();
Thread.sleep(5000);
r.stop();
r.copyTo(Files.createTempFile("my-recording", ".jfr"));
```

**Since:** 9

public final class

Recording

extends

Object

implements

Closeable

Provides means to configure, start, stop and dump recording data to disk.

The following example shows how configure, start, stop and dump recording data to disk.

```java
Configuration c = Configuration.getConfiguration("default");
Recording r = new Recording(c);
r.start();
System.gc();
Thread.sleep(5000);
r.stop();
r.copyTo(Files.createTempFile("my-recording", ".jfr"));
```

The following example shows how configure, start, stop and dump recording data to disk.

```java
Configuration c = Configuration.getConfiguration("default");
Recording r = new Recording(c);
r.start();
System.gc();
Thread.sleep(5000);
r.stop();
r.copyTo(Files.createTempFile("my-recording", ".jfr"));
```

Configuration c = Configuration.getConfiguration("default");
Recording r = new Recording(c);
r.start();
System.gc();
Thread.sleep(5000);
r.stop();
r.copyTo(Files.createTempFile("my-recording", ".jfr"));

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

Recording

()

Creates a recording without any settings.

Recording

​(

Map

<

String

,​

String

> settings)

Recording

​(

Configuration

configuration)

Creates a recording with settings from a configuration.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

close

()

Releases all data that is associated with this recording.

Recording

copy

​(boolean stop)

Returns a clone of this recording, with a new recording ID and name.

EventSettings

disable

​(

Class

<? extends

Event

> eventClass)

Disables event.

EventSettings

disable

​(

String

name)

Disables event with the specified name.

void

dump

​(

Path

destination)

Writes recording data to a file.

EventSettings

enable

​(

Class

<? extends

Event

> eventClass)

Enables event.

EventSettings

enable

​(

String

name)

Enables the event with the specified name.

Path

getDestination

()

Returns the destination file, where recording data is written when the
recording stops, or

null

if no destination is set.

boolean

getDumpOnExit

()

Returns whether this recording is dumped to disk when the JVM exits.

Duration

getDuration

()

Returns the specified duration for this recording, or

null

if no
duration is set.

long

getId

()

Returns a unique ID for this recording.

Duration

getMaxAge

()

Returns the length of time that the data is kept in the disk repository
before it is removed.

long

getMaxSize

()

Returns the maximum size, measured in bytes, at which data is no longer kept in the disk repository.

String

getName

()

Returns the name of this recording.

Map

<

String

,​

String

>

getSettings

()

Returns settings used by this recording.

long

getSize

()

Returns the current size of this recording in the disk repository,
measured in bytes.

Instant

getStartTime

()

Returns the time when this recording was started.

RecordingState

getState

()

Returns the recording state that this recording is currently in.

Instant

getStopTime

()

Returns the time when this recording was stopped.

InputStream

getStream

​(

Instant

start,

Instant

end)

Creates a data stream for a specified interval.

boolean

isToDisk

()

Returns

true

if this recording uses the disk repository,

false

otherwise.

void

scheduleStart

​(

Duration

delay)

Starts this recording after a delay.

void

setDestination

​(

Path

destination)

Sets a location where data is written on recording stop, or

null

if data is not to be dumped.

void

setDumpOnExit

​(boolean dumpOnExit)

Sets whether this recording is dumped to disk when the JVM exits.

void

setDuration

​(

Duration

duration)

Sets a duration for how long a recording runs before it stops.

void

setMaxAge

​(

Duration

maxAge)

Determines how far back data is kept in the disk repository.

void

setMaxSize

​(long maxSize)

Determines how much data is kept in the disk repository.

void

setName

​(

String

name)

Sets a human-readable name (for example,

"My Recording"

).

void

setSettings

​(

Map

<

String

,​

String

> settings)

Replaces all settings for this recording.

void

setToDisk

​(boolean disk)

Determines whether this recording is continuously flushed to the disk
repository or data is constrained to what is available in memory buffers.

void

start

()

Starts this recording.

boolean

stop

()

Stops this recording.

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

toString

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

Recording

()

Creates a recording without any settings.

Recording

​(

Map

<

String

,​

String

> settings)

Recording

​(

Configuration

configuration)

Creates a recording with settings from a configuration.

---

#### Constructor Summary

Creates a recording without any settings.

Creates a recording with settings from a configuration.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

close

()

Releases all data that is associated with this recording.

Recording

copy

​(boolean stop)

Returns a clone of this recording, with a new recording ID and name.

EventSettings

disable

​(

Class

<? extends

Event

> eventClass)

Disables event.

EventSettings

disable

​(

String

name)

Disables event with the specified name.

void

dump

​(

Path

destination)

Writes recording data to a file.

EventSettings

enable

​(

Class

<? extends

Event

> eventClass)

Enables event.

EventSettings

enable

​(

String

name)

Enables the event with the specified name.

Path

getDestination

()

Returns the destination file, where recording data is written when the
recording stops, or

null

if no destination is set.

boolean

getDumpOnExit

()

Returns whether this recording is dumped to disk when the JVM exits.

Duration

getDuration

()

Returns the specified duration for this recording, or

null

if no
duration is set.

long

getId

()

Returns a unique ID for this recording.

Duration

getMaxAge

()

Returns the length of time that the data is kept in the disk repository
before it is removed.

long

getMaxSize

()

Returns the maximum size, measured in bytes, at which data is no longer kept in the disk repository.

String

getName

()

Returns the name of this recording.

Map

<

String

,​

String

>

getSettings

()

Returns settings used by this recording.

long

getSize

()

Returns the current size of this recording in the disk repository,
measured in bytes.

Instant

getStartTime

()

Returns the time when this recording was started.

RecordingState

getState

()

Returns the recording state that this recording is currently in.

Instant

getStopTime

()

Returns the time when this recording was stopped.

InputStream

getStream

​(

Instant

start,

Instant

end)

Creates a data stream for a specified interval.

boolean

isToDisk

()

Returns

true

if this recording uses the disk repository,

false

otherwise.

void

scheduleStart

​(

Duration

delay)

Starts this recording after a delay.

void

setDestination

​(

Path

destination)

Sets a location where data is written on recording stop, or

null

if data is not to be dumped.

void

setDumpOnExit

​(boolean dumpOnExit)

Sets whether this recording is dumped to disk when the JVM exits.

void

setDuration

​(

Duration

duration)

Sets a duration for how long a recording runs before it stops.

void

setMaxAge

​(

Duration

maxAge)

Determines how far back data is kept in the disk repository.

void

setMaxSize

​(long maxSize)

Determines how much data is kept in the disk repository.

void

setName

​(

String

name)

Sets a human-readable name (for example,

"My Recording"

).

void

setSettings

​(

Map

<

String

,​

String

> settings)

Replaces all settings for this recording.

void

setToDisk

​(boolean disk)

Determines whether this recording is continuously flushed to the disk
repository or data is constrained to what is available in memory buffers.

void

start

()

Starts this recording.

boolean

stop

()

Stops this recording.

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

toString

,

wait

,

wait

,

wait

---

#### Method Summary

Releases all data that is associated with this recording.

Returns a clone of this recording, with a new recording ID and name.

Disables event.

Disables event with the specified name.

Writes recording data to a file.

Enables event.

Enables the event with the specified name.

Returns the destination file, where recording data is written when the
recording stops, or

null

if no destination is set.

Returns whether this recording is dumped to disk when the JVM exits.

Returns the specified duration for this recording, or

null

if no
duration is set.

Returns a unique ID for this recording.

Returns the length of time that the data is kept in the disk repository
before it is removed.

Returns the maximum size, measured in bytes, at which data is no longer kept in the disk repository.

Returns the name of this recording.

Returns settings used by this recording.

Returns the current size of this recording in the disk repository,
measured in bytes.

Returns the time when this recording was started.

Returns the recording state that this recording is currently in.

Returns the time when this recording was stopped.

Creates a data stream for a specified interval.

Returns

true

if this recording uses the disk repository,

false

otherwise.

Starts this recording after a delay.

Sets a location where data is written on recording stop, or

null

if data is not to be dumped.

Sets whether this recording is dumped to disk when the JVM exits.

Sets a duration for how long a recording runs before it stops.

Determines how far back data is kept in the disk repository.

Determines how much data is kept in the disk repository.

Sets a human-readable name (for example,

"My Recording"

).

Replaces all settings for this recording.

Determines whether this recording is continuously flushed to the disk
repository or data is constrained to what is available in memory buffers.

Starts this recording.

Stops this recording.

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

toString

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

- Recording

```java
public Recording​(
Map
<
String
,​
String
> settings)
```

- Recording

```java
public Recording()
```

Creates a recording without any settings.

A newly created recording is in the

RecordingState.NEW

state. To start
the recording, invoke the

start()

method.

**Throws:** IllegalStateException

- if Flight Recorder can't be created (for
example, if the Java Virtual Machine (JVM) lacks Flight Recorder
support, or if the file repository can't be created or accessed)
**Throws:** SecurityException

- If a security manager is used and
FlightRecorderPermission "accessFlightRecorder" is not set.

- Recording

```java
public Recording​(
Configuration
configuration)
```

Creates a recording with settings from a configuration.

The following example shows how create a recording that uses a predefined configuration.

```java
Recording r = new Recording(Configuration.getConfiguration("default"));
```

The newly created recording is in the

RecordingState.NEW

state. To
start the recording, invoke the

start()

method.

**Parameters:** configuration

- configuration that contains the settings to be use, not

null
**Throws:** IllegalStateException

- if Flight Recorder can't be created (for
example, if the Java Virtual Machine (JVM) lacks Flight Recorder
support, or if the file repository can't be created or accessed)
**Throws:** SecurityException

- if a security manager is used and
FlightRecorderPermission "accessFlightRecorder" is not set.
**See Also:** Configuration

============ METHOD DETAIL ==========

- Method Detail

- start

```java
public void start()
```

Starts this recording.

It's recommended that the recording options and event settings are configured
before calling this method. The benefits of doing so are a more consistent
state when analyzing the recorded data, and improved performance because the
configuration can be applied atomically.

After a successful invocation of this method, this recording is in the

RUNNING

state.

**Throws:** IllegalStateException

- if recording is already started or is in the

CLOSED

state

- scheduleStart

```java
public void scheduleStart​(
Duration
delay)
```

Starts this recording after a delay.

After a successful invocation of this method, this recording is in the

DELAYED

state.

**Parameters:** delay

- the time to wait before starting this recording, not

null
**Throws:** IllegalStateException

- if the recording is not it the

NEW

state

- stop

```java
public boolean stop()
```

Stops this recording.

When a recording is stopped it can't be restarted. If this
recording has a destination, data is written to that destination and
the recording is closed. After a recording is closed, the data is no longer
available.

After a successful invocation of this method, this recording will be
in the

STOPPED

state.

**Returns:** true

if recording is stopped,

false

otherwise
**Throws:** IllegalStateException

- if the recording is not started or is already stopped
**Throws:** SecurityException

- if a security manager exists and the caller
doesn't have

FilePermission

to write to the destination
path
**See Also:** setDestination(Path)

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

Returns settings used by this recording.

Modifying the returned

Map

will not change the settings for this recording.

If no settings are set for this recording, an empty

Map

is
returned.

**Returns:** recording settings, not

null

- getSize

```java
public long getSize()
```

Returns the current size of this recording in the disk repository,
measured in bytes.

The size is updated when recording buffers are flushed. If the recording is
not written to the disk repository the returned size is always

0

.

**Returns:** amount of recorded data, measured in bytes, or

0

if the
recording is not written to the disk repository

- getStopTime

```java
public
Instant
getStopTime()
```

Returns the time when this recording was stopped.

**Returns:** the time, or

null

if this recording is not stopped

- getStartTime

```java
public
Instant
getStartTime()
```

Returns the time when this recording was started.

**Returns:** the the time, or

null

if this recording is not started

- getMaxSize

```java
public long getMaxSize()
```

Returns the maximum size, measured in bytes, at which data is no longer kept in the disk repository.

**Returns:** maximum size in bytes, or

0

if no maximum size is set

- getMaxAge

```java
public
Duration
getMaxAge()
```

Returns the length of time that the data is kept in the disk repository
before it is removed.

**Returns:** maximum length of time, or

null

if no maximum length of time
has been set

- getName

```java
public
String
getName()
```

Returns the name of this recording.

By default, the name is the same as the recording ID.

**Returns:** the recording name, not

null

- setSettings

```java
public void setSettings​(
Map
<
String
,​
String
> settings)
```

Replaces all settings for this recording.

The following example shows how to set event settings for a recording.

```java
Map<String, String> settings = new HashMap<>();
settings.putAll(EventSettings.enabled("jdk.CPUSample").withPeriod(Duration.ofSeconds(2)).toMap());
settings.putAll(EventSettings.enabled(MyEvent.class).withThreshold(Duration.ofSeconds(2)).withoutStackTrace().toMap());
settings.put("jdk.ExecutionSample#period", "10 ms");
recording.setSettings(settings);
```

The following example shows how to merge settings.

```java
Map<String, String> settings = recording.getSettings();
settings.putAll(additionalSettings);
recording.setSettings(settings);
```

**Parameters:** settings

- the settings to set, not

null

- getState

```java
public
RecordingState
getState()
```

Returns the recording state that this recording is currently in.

**Returns:** the recording state, not

null
**See Also:** RecordingState

- close

```java
public void close()
```

Releases all data that is associated with this recording.

After a successful invocation of this method, this recording is in the

CLOSED

state.

**Specified by:** close

in interface

AutoCloseable
**Specified by:** close

in interface

Closeable

- copy

```java
public
Recording
copy​(boolean stop)
```

Returns a clone of this recording, with a new recording ID and name.

Clones are useful for dumping data without stopping the recording. After
a clone is created, the amount of data to copy is constrained
with the

setMaxAge(Duration)

method and the

setMaxSize(long)

method.

**Parameters:** stop

-

true

if the newly created copy should be stopped
immediately,

false

otherwise
**Returns:** the recording copy, not

null

- dump

```java
public void dump​(
Path
destination)
throws
IOException
```

Writes recording data to a file.

Recording must be started, but not necessarily stopped.

**Parameters:** destination

- the location where recording data is written, not

null
**Throws:** IOException

- if the recording can't be copied to the specified
location
**Throws:** SecurityException

- if a security manager exists and the caller doesn't
have

FilePermission

to write to the destination path

- isToDisk

```java
public boolean isToDisk()
```

Returns

true

if this recording uses the disk repository,

false

otherwise.

If no value is set,

true

is returned.

**Returns:** true

if the recording uses the disk repository,

false

otherwise

- setMaxSize

```java
public void setMaxSize​(long maxSize)
```

Determines how much data is kept in the disk repository.

To control the amount of recording data that is stored on disk, the maximum
amount of data to retain can be specified. When the maximum limit is
exceeded, the Java Virtual Machine (JVM) removes the oldest chunk to make
room for a more recent chunk.

If neither maximum limit or the maximum age is set, the size of the
recording may grow indefinitely.

**Parameters:** maxSize

- the amount of data to retain,

0

if infinite
**Throws:** IllegalArgumentException

- if

maxSize

is negative
**Throws:** IllegalStateException

- if the recording is in

CLOSED

state

- setMaxAge

```java
public void setMaxAge​(
Duration
maxAge)
```

Determines how far back data is kept in the disk repository.

To control the amount of recording data stored on disk, the maximum length of
time to retain the data can be specified. Data stored on disk that is older
than the specified length of time is removed by the Java Virtual Machine (JVM).

If neither maximum limit or the maximum age is set, the size of the
recording may grow indefinitely.

**Parameters:** maxAge

- the length of time that data is kept, or

null

if infinite
**Throws:** IllegalArgumentException

- if

maxAge

is negative
**Throws:** IllegalStateException

- if the recording is in the

CLOSED

state

- setDestination

```java
public void setDestination​(
Path
destination)
throws
IOException
```

Sets a location where data is written on recording stop, or

null

if data is not to be dumped.

If a destination is set, this recording is automatically closed
after data is successfully copied to the destination path.

If a destination is

not

set, Flight Recorder retains the
recording data until this recording is closed. Use the

dump(Path)

method to
manually write data to a file.

**Parameters:** destination

- the destination path, or

null

if recording should
not be dumped at stop
**Throws:** IllegalStateException

- if recording is in the

STOPPED

or

CLOSED

state.
**Throws:** SecurityException

- if a security manager exists and the caller
doesn't have

FilePermission

to read, write, and delete the

destination

file
**Throws:** IOException

- if the path is not writable

- getDestination

```java
public
Path
getDestination()
```

Returns the destination file, where recording data is written when the
recording stops, or

null

if no destination is set.

**Returns:** the destination file, or

null

if not set.

- getId

```java
public long getId()
```

Returns a unique ID for this recording.

**Returns:** the recording ID

- setName

```java
public void setName​(
String
name)
```

Sets a human-readable name (for example,

"My Recording"

).

**Parameters:** name

- the recording name, not

null
**Throws:** IllegalStateException

- if the recording is in

CLOSED

state

- setDumpOnExit

```java
public void setDumpOnExit​(boolean dumpOnExit)
```

Sets whether this recording is dumped to disk when the JVM exits.

**Parameters:** dumpOnExit

- if this recording should be dumped when the JVM exits

- getDumpOnExit

```java
public boolean getDumpOnExit()
```

Returns whether this recording is dumped to disk when the JVM exits.

If dump on exit is not set,

false

is returned.

**Returns:** true

if the recording is dumped on exit,

false

otherwise.

- setToDisk

```java
public void setToDisk​(boolean disk)
```

Determines whether this recording is continuously flushed to the disk
repository or data is constrained to what is available in memory buffers.

**Parameters:** disk

-

true

if this recording is written to disk,

false

if in-memory

- getStream

```java
public
InputStream
getStream​(
Instant
start,

Instant
end)
throws
IOException
```

Creates a data stream for a specified interval.

The stream may contain some data outside the specified range.

**Parameters:** the

- start start time for the stream, or

null

to get data from
start time of the recording
**Parameters:** the

- end end time for the stream, or

null

to get data until the
present time.
**Returns:** an input stream, or

null

if no data is available in the
interval.
**Throws:** IllegalArgumentException

- if

end

happens before

start
**Throws:** IOException

- if a stream can't be opened

- getDuration

```java
public
Duration
getDuration()
```

Returns the specified duration for this recording, or

null

if no
duration is set.

The duration can be set only when the recording is in the

RecordingState.NEW

state.

**Returns:** the desired duration of the recording, or

null

if no duration
has been set.

- setDuration

```java
public void setDuration​(
Duration
duration)
```

Sets a duration for how long a recording runs before it stops.

By default, a recording has no duration (

null

).

**Parameters:** duration

- the duration, or

null

if no duration is set
**Throws:** IllegalStateException

- if recording is in the

STOPPED

or

CLOSED

state

- enable

```java
public
EventSettings
enable​(
String
name)
```

Enables the event with the specified name.

If multiple events have the same name (for example, the same class is loaded
in different class loaders), then all events that match the name are enabled. To
enable a specific class, use the

enable(Class)

method or a

String

representation of the event type ID.

**Parameters:** name

- the settings for the event, not

null
**Returns:** an event setting for further configuration, not

null
**See Also:** EventType

- disable

```java
public
EventSettings
disable​(
String
name)
```

Disables event with the specified name.

If multiple events with same name (for example, the same class is loaded
in different class loaders), then all events that match the
name is disabled. To disable a specific class, use the

disable(Class)

method or a

String

representation of the event
type ID.

**Parameters:** name

- the settings for the event, not

null
**Returns:** an event setting for further configuration, not

null

- enable

```java
public
EventSettings
enable​(
Class
<? extends
Event
> eventClass)
```

Enables event.

**Parameters:** eventClass

- the event to enable, not

null
**Returns:** an event setting for further configuration, not

null
**Throws:** IllegalArgumentException

- if

eventClass

is an abstract
class or not a subclass of

Event

- disable

```java
public
EventSettings
disable​(
Class
<? extends
Event
> eventClass)
```

Disables event.

**Parameters:** eventClass

- the event to enable, not

null
**Returns:** an event setting for further configuration, not

null
**Throws:** IllegalArgumentException

- if

eventClass

is an abstract
class or not a subclass of

Event

Constructor Detail

- Recording

```java
public Recording​(
Map
<
String
,​
String
> settings)
```

- Recording

```java
public Recording()
```

Creates a recording without any settings.

A newly created recording is in the

RecordingState.NEW

state. To start
the recording, invoke the

start()

method.

**Throws:** IllegalStateException

- if Flight Recorder can't be created (for
example, if the Java Virtual Machine (JVM) lacks Flight Recorder
support, or if the file repository can't be created or accessed)
**Throws:** SecurityException

- If a security manager is used and
FlightRecorderPermission "accessFlightRecorder" is not set.

- Recording

```java
public Recording​(
Configuration
configuration)
```

Creates a recording with settings from a configuration.

The following example shows how create a recording that uses a predefined configuration.

```java
Recording r = new Recording(Configuration.getConfiguration("default"));
```

The newly created recording is in the

RecordingState.NEW

state. To
start the recording, invoke the

start()

method.

**Parameters:** configuration

- configuration that contains the settings to be use, not

null
**Throws:** IllegalStateException

- if Flight Recorder can't be created (for
example, if the Java Virtual Machine (JVM) lacks Flight Recorder
support, or if the file repository can't be created or accessed)
**Throws:** SecurityException

- if a security manager is used and
FlightRecorderPermission "accessFlightRecorder" is not set.
**See Also:** Configuration

---

#### Constructor Detail

Recording

```java
public Recording​(
Map
<
String
,​
String
> settings)
```

---

#### Recording

public Recording​(

Map

<

String

,​

String

> settings)

Recording

```java
public Recording()
```

Creates a recording without any settings.

A newly created recording is in the

RecordingState.NEW

state. To start
the recording, invoke the

start()

method.

**Throws:** IllegalStateException

- if Flight Recorder can't be created (for
example, if the Java Virtual Machine (JVM) lacks Flight Recorder
support, or if the file repository can't be created or accessed)
**Throws:** SecurityException

- If a security manager is used and
FlightRecorderPermission "accessFlightRecorder" is not set.

---

#### Recording

public Recording()

Creates a recording without any settings.

A newly created recording is in the

RecordingState.NEW

state. To start
the recording, invoke the

start()

method.

A newly created recording is in the

RecordingState.NEW

state. To start
the recording, invoke the

start()

method.

Recording

```java
public Recording​(
Configuration
configuration)
```

Creates a recording with settings from a configuration.

The following example shows how create a recording that uses a predefined configuration.

```java
Recording r = new Recording(Configuration.getConfiguration("default"));
```

The newly created recording is in the

RecordingState.NEW

state. To
start the recording, invoke the

start()

method.

**Parameters:** configuration

- configuration that contains the settings to be use, not

null
**Throws:** IllegalStateException

- if Flight Recorder can't be created (for
example, if the Java Virtual Machine (JVM) lacks Flight Recorder
support, or if the file repository can't be created or accessed)
**Throws:** SecurityException

- if a security manager is used and
FlightRecorderPermission "accessFlightRecorder" is not set.
**See Also:** Configuration

---

#### Recording

public Recording​(

Configuration

configuration)

Creates a recording with settings from a configuration.

The following example shows how create a recording that uses a predefined configuration.

```java
Recording r = new Recording(Configuration.getConfiguration("default"));
```

The newly created recording is in the

RecordingState.NEW

state. To
start the recording, invoke the

start()

method.

The following example shows how create a recording that uses a predefined configuration.

```java
Recording r = new Recording(Configuration.getConfiguration("default"));
```

The newly created recording is in the

RecordingState.NEW

state. To
start the recording, invoke the

start()

method.

Recording r = new Recording(Configuration.getConfiguration("default"));

Method Detail

- start

```java
public void start()
```

Starts this recording.

It's recommended that the recording options and event settings are configured
before calling this method. The benefits of doing so are a more consistent
state when analyzing the recorded data, and improved performance because the
configuration can be applied atomically.

After a successful invocation of this method, this recording is in the

RUNNING

state.

**Throws:** IllegalStateException

- if recording is already started or is in the

CLOSED

state

- scheduleStart

```java
public void scheduleStart​(
Duration
delay)
```

Starts this recording after a delay.

After a successful invocation of this method, this recording is in the

DELAYED

state.

**Parameters:** delay

- the time to wait before starting this recording, not

null
**Throws:** IllegalStateException

- if the recording is not it the

NEW

state

- stop

```java
public boolean stop()
```

Stops this recording.

When a recording is stopped it can't be restarted. If this
recording has a destination, data is written to that destination and
the recording is closed. After a recording is closed, the data is no longer
available.

After a successful invocation of this method, this recording will be
in the

STOPPED

state.

**Returns:** true

if recording is stopped,

false

otherwise
**Throws:** IllegalStateException

- if the recording is not started or is already stopped
**Throws:** SecurityException

- if a security manager exists and the caller
doesn't have

FilePermission

to write to the destination
path
**See Also:** setDestination(Path)

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

Returns settings used by this recording.

Modifying the returned

Map

will not change the settings for this recording.

If no settings are set for this recording, an empty

Map

is
returned.

**Returns:** recording settings, not

null

- getSize

```java
public long getSize()
```

Returns the current size of this recording in the disk repository,
measured in bytes.

The size is updated when recording buffers are flushed. If the recording is
not written to the disk repository the returned size is always

0

.

**Returns:** amount of recorded data, measured in bytes, or

0

if the
recording is not written to the disk repository

- getStopTime

```java
public
Instant
getStopTime()
```

Returns the time when this recording was stopped.

**Returns:** the time, or

null

if this recording is not stopped

- getStartTime

```java
public
Instant
getStartTime()
```

Returns the time when this recording was started.

**Returns:** the the time, or

null

if this recording is not started

- getMaxSize

```java
public long getMaxSize()
```

Returns the maximum size, measured in bytes, at which data is no longer kept in the disk repository.

**Returns:** maximum size in bytes, or

0

if no maximum size is set

- getMaxAge

```java
public
Duration
getMaxAge()
```

Returns the length of time that the data is kept in the disk repository
before it is removed.

**Returns:** maximum length of time, or

null

if no maximum length of time
has been set

- getName

```java
public
String
getName()
```

Returns the name of this recording.

By default, the name is the same as the recording ID.

**Returns:** the recording name, not

null

- setSettings

```java
public void setSettings​(
Map
<
String
,​
String
> settings)
```

Replaces all settings for this recording.

The following example shows how to set event settings for a recording.

```java
Map<String, String> settings = new HashMap<>();
settings.putAll(EventSettings.enabled("jdk.CPUSample").withPeriod(Duration.ofSeconds(2)).toMap());
settings.putAll(EventSettings.enabled(MyEvent.class).withThreshold(Duration.ofSeconds(2)).withoutStackTrace().toMap());
settings.put("jdk.ExecutionSample#period", "10 ms");
recording.setSettings(settings);
```

The following example shows how to merge settings.

```java
Map<String, String> settings = recording.getSettings();
settings.putAll(additionalSettings);
recording.setSettings(settings);
```

**Parameters:** settings

- the settings to set, not

null

- getState

```java
public
RecordingState
getState()
```

Returns the recording state that this recording is currently in.

**Returns:** the recording state, not

null
**See Also:** RecordingState

- close

```java
public void close()
```

Releases all data that is associated with this recording.

After a successful invocation of this method, this recording is in the

CLOSED

state.

**Specified by:** close

in interface

AutoCloseable
**Specified by:** close

in interface

Closeable

- copy

```java
public
Recording
copy​(boolean stop)
```

Returns a clone of this recording, with a new recording ID and name.

Clones are useful for dumping data without stopping the recording. After
a clone is created, the amount of data to copy is constrained
with the

setMaxAge(Duration)

method and the

setMaxSize(long)

method.

**Parameters:** stop

-

true

if the newly created copy should be stopped
immediately,

false

otherwise
**Returns:** the recording copy, not

null

- dump

```java
public void dump​(
Path
destination)
throws
IOException
```

Writes recording data to a file.

Recording must be started, but not necessarily stopped.

**Parameters:** destination

- the location where recording data is written, not

null
**Throws:** IOException

- if the recording can't be copied to the specified
location
**Throws:** SecurityException

- if a security manager exists and the caller doesn't
have

FilePermission

to write to the destination path

- isToDisk

```java
public boolean isToDisk()
```

Returns

true

if this recording uses the disk repository,

false

otherwise.

If no value is set,

true

is returned.

**Returns:** true

if the recording uses the disk repository,

false

otherwise

- setMaxSize

```java
public void setMaxSize​(long maxSize)
```

Determines how much data is kept in the disk repository.

To control the amount of recording data that is stored on disk, the maximum
amount of data to retain can be specified. When the maximum limit is
exceeded, the Java Virtual Machine (JVM) removes the oldest chunk to make
room for a more recent chunk.

If neither maximum limit or the maximum age is set, the size of the
recording may grow indefinitely.

**Parameters:** maxSize

- the amount of data to retain,

0

if infinite
**Throws:** IllegalArgumentException

- if

maxSize

is negative
**Throws:** IllegalStateException

- if the recording is in

CLOSED

state

- setMaxAge

```java
public void setMaxAge​(
Duration
maxAge)
```

Determines how far back data is kept in the disk repository.

To control the amount of recording data stored on disk, the maximum length of
time to retain the data can be specified. Data stored on disk that is older
than the specified length of time is removed by the Java Virtual Machine (JVM).

If neither maximum limit or the maximum age is set, the size of the
recording may grow indefinitely.

**Parameters:** maxAge

- the length of time that data is kept, or

null

if infinite
**Throws:** IllegalArgumentException

- if

maxAge

is negative
**Throws:** IllegalStateException

- if the recording is in the

CLOSED

state

- setDestination

```java
public void setDestination​(
Path
destination)
throws
IOException
```

Sets a location where data is written on recording stop, or

null

if data is not to be dumped.

If a destination is set, this recording is automatically closed
after data is successfully copied to the destination path.

If a destination is

not

set, Flight Recorder retains the
recording data until this recording is closed. Use the

dump(Path)

method to
manually write data to a file.

**Parameters:** destination

- the destination path, or

null

if recording should
not be dumped at stop
**Throws:** IllegalStateException

- if recording is in the

STOPPED

or

CLOSED

state.
**Throws:** SecurityException

- if a security manager exists and the caller
doesn't have

FilePermission

to read, write, and delete the

destination

file
**Throws:** IOException

- if the path is not writable

- getDestination

```java
public
Path
getDestination()
```

Returns the destination file, where recording data is written when the
recording stops, or

null

if no destination is set.

**Returns:** the destination file, or

null

if not set.

- getId

```java
public long getId()
```

Returns a unique ID for this recording.

**Returns:** the recording ID

- setName

```java
public void setName​(
String
name)
```

Sets a human-readable name (for example,

"My Recording"

).

**Parameters:** name

- the recording name, not

null
**Throws:** IllegalStateException

- if the recording is in

CLOSED

state

- setDumpOnExit

```java
public void setDumpOnExit​(boolean dumpOnExit)
```

Sets whether this recording is dumped to disk when the JVM exits.

**Parameters:** dumpOnExit

- if this recording should be dumped when the JVM exits

- getDumpOnExit

```java
public boolean getDumpOnExit()
```

Returns whether this recording is dumped to disk when the JVM exits.

If dump on exit is not set,

false

is returned.

**Returns:** true

if the recording is dumped on exit,

false

otherwise.

- setToDisk

```java
public void setToDisk​(boolean disk)
```

Determines whether this recording is continuously flushed to the disk
repository or data is constrained to what is available in memory buffers.

**Parameters:** disk

-

true

if this recording is written to disk,

false

if in-memory

- getStream

```java
public
InputStream
getStream​(
Instant
start,

Instant
end)
throws
IOException
```

Creates a data stream for a specified interval.

The stream may contain some data outside the specified range.

**Parameters:** the

- start start time for the stream, or

null

to get data from
start time of the recording
**Parameters:** the

- end end time for the stream, or

null

to get data until the
present time.
**Returns:** an input stream, or

null

if no data is available in the
interval.
**Throws:** IllegalArgumentException

- if

end

happens before

start
**Throws:** IOException

- if a stream can't be opened

- getDuration

```java
public
Duration
getDuration()
```

Returns the specified duration for this recording, or

null

if no
duration is set.

The duration can be set only when the recording is in the

RecordingState.NEW

state.

**Returns:** the desired duration of the recording, or

null

if no duration
has been set.

- setDuration

```java
public void setDuration​(
Duration
duration)
```

Sets a duration for how long a recording runs before it stops.

By default, a recording has no duration (

null

).

**Parameters:** duration

- the duration, or

null

if no duration is set
**Throws:** IllegalStateException

- if recording is in the

STOPPED

or

CLOSED

state

- enable

```java
public
EventSettings
enable​(
String
name)
```

Enables the event with the specified name.

If multiple events have the same name (for example, the same class is loaded
in different class loaders), then all events that match the name are enabled. To
enable a specific class, use the

enable(Class)

method or a

String

representation of the event type ID.

**Parameters:** name

- the settings for the event, not

null
**Returns:** an event setting for further configuration, not

null
**See Also:** EventType

- disable

```java
public
EventSettings
disable​(
String
name)
```

Disables event with the specified name.

If multiple events with same name (for example, the same class is loaded
in different class loaders), then all events that match the
name is disabled. To disable a specific class, use the

disable(Class)

method or a

String

representation of the event
type ID.

**Parameters:** name

- the settings for the event, not

null
**Returns:** an event setting for further configuration, not

null

- enable

```java
public
EventSettings
enable​(
Class
<? extends
Event
> eventClass)
```

Enables event.

**Parameters:** eventClass

- the event to enable, not

null
**Returns:** an event setting for further configuration, not

null
**Throws:** IllegalArgumentException

- if

eventClass

is an abstract
class or not a subclass of

Event

- disable

```java
public
EventSettings
disable​(
Class
<? extends
Event
> eventClass)
```

Disables event.

**Parameters:** eventClass

- the event to enable, not

null
**Returns:** an event setting for further configuration, not

null
**Throws:** IllegalArgumentException

- if

eventClass

is an abstract
class or not a subclass of

Event

---

#### Method Detail

start

```java
public void start()
```

Starts this recording.

It's recommended that the recording options and event settings are configured
before calling this method. The benefits of doing so are a more consistent
state when analyzing the recorded data, and improved performance because the
configuration can be applied atomically.

After a successful invocation of this method, this recording is in the

RUNNING

state.

**Throws:** IllegalStateException

- if recording is already started or is in the

CLOSED

state

---

#### start

public void start()

Starts this recording.

It's recommended that the recording options and event settings are configured
before calling this method. The benefits of doing so are a more consistent
state when analyzing the recorded data, and improved performance because the
configuration can be applied atomically.

After a successful invocation of this method, this recording is in the

RUNNING

state.

It's recommended that the recording options and event settings are configured
before calling this method. The benefits of doing so are a more consistent
state when analyzing the recorded data, and improved performance because the
configuration can be applied atomically.

After a successful invocation of this method, this recording is in the

RUNNING

state.

After a successful invocation of this method, this recording is in the

RUNNING

state.

scheduleStart

```java
public void scheduleStart​(
Duration
delay)
```

Starts this recording after a delay.

After a successful invocation of this method, this recording is in the

DELAYED

state.

**Parameters:** delay

- the time to wait before starting this recording, not

null
**Throws:** IllegalStateException

- if the recording is not it the

NEW

state

---

#### scheduleStart

public void scheduleStart​(

Duration

delay)

Starts this recording after a delay.

After a successful invocation of this method, this recording is in the

DELAYED

state.

After a successful invocation of this method, this recording is in the

DELAYED

state.

stop

```java
public boolean stop()
```

Stops this recording.

When a recording is stopped it can't be restarted. If this
recording has a destination, data is written to that destination and
the recording is closed. After a recording is closed, the data is no longer
available.

After a successful invocation of this method, this recording will be
in the

STOPPED

state.

**Returns:** true

if recording is stopped,

false

otherwise
**Throws:** IllegalStateException

- if the recording is not started or is already stopped
**Throws:** SecurityException

- if a security manager exists and the caller
doesn't have

FilePermission

to write to the destination
path
**See Also:** setDestination(Path)

---

#### stop

public boolean stop()

Stops this recording.

When a recording is stopped it can't be restarted. If this
recording has a destination, data is written to that destination and
the recording is closed. After a recording is closed, the data is no longer
available.

After a successful invocation of this method, this recording will be
in the

STOPPED

state.

When a recording is stopped it can't be restarted. If this
recording has a destination, data is written to that destination and
the recording is closed. After a recording is closed, the data is no longer
available.

After a successful invocation of this method, this recording will be
in the

STOPPED

state.

After a successful invocation of this method, this recording will be
in the

STOPPED

state.

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

Returns settings used by this recording.

Modifying the returned

Map

will not change the settings for this recording.

If no settings are set for this recording, an empty

Map

is
returned.

**Returns:** recording settings, not

null

---

#### getSettings

public

Map

<

String

,​

String

> getSettings()

Returns settings used by this recording.

Modifying the returned

Map

will not change the settings for this recording.

If no settings are set for this recording, an empty

Map

is
returned.

Modifying the returned

Map

will not change the settings for this recording.

If no settings are set for this recording, an empty

Map

is
returned.

If no settings are set for this recording, an empty

Map

is
returned.

getSize

```java
public long getSize()
```

Returns the current size of this recording in the disk repository,
measured in bytes.

The size is updated when recording buffers are flushed. If the recording is
not written to the disk repository the returned size is always

0

.

**Returns:** amount of recorded data, measured in bytes, or

0

if the
recording is not written to the disk repository

---

#### getSize

public long getSize()

Returns the current size of this recording in the disk repository,
measured in bytes.

The size is updated when recording buffers are flushed. If the recording is
not written to the disk repository the returned size is always

0

.

The size is updated when recording buffers are flushed. If the recording is
not written to the disk repository the returned size is always

0

.

getStopTime

```java
public
Instant
getStopTime()
```

Returns the time when this recording was stopped.

**Returns:** the time, or

null

if this recording is not stopped

---

#### getStopTime

public

Instant

getStopTime()

Returns the time when this recording was stopped.

getStartTime

```java
public
Instant
getStartTime()
```

Returns the time when this recording was started.

**Returns:** the the time, or

null

if this recording is not started

---

#### getStartTime

public

Instant

getStartTime()

Returns the time when this recording was started.

getMaxSize

```java
public long getMaxSize()
```

Returns the maximum size, measured in bytes, at which data is no longer kept in the disk repository.

**Returns:** maximum size in bytes, or

0

if no maximum size is set

---

#### getMaxSize

public long getMaxSize()

Returns the maximum size, measured in bytes, at which data is no longer kept in the disk repository.

getMaxAge

```java
public
Duration
getMaxAge()
```

Returns the length of time that the data is kept in the disk repository
before it is removed.

**Returns:** maximum length of time, or

null

if no maximum length of time
has been set

---

#### getMaxAge

public

Duration

getMaxAge()

Returns the length of time that the data is kept in the disk repository
before it is removed.

getName

```java
public
String
getName()
```

Returns the name of this recording.

By default, the name is the same as the recording ID.

**Returns:** the recording name, not

null

---

#### getName

public

String

getName()

Returns the name of this recording.

By default, the name is the same as the recording ID.

By default, the name is the same as the recording ID.

setSettings

```java
public void setSettings​(
Map
<
String
,​
String
> settings)
```

Replaces all settings for this recording.

The following example shows how to set event settings for a recording.

```java
Map<String, String> settings = new HashMap<>();
settings.putAll(EventSettings.enabled("jdk.CPUSample").withPeriod(Duration.ofSeconds(2)).toMap());
settings.putAll(EventSettings.enabled(MyEvent.class).withThreshold(Duration.ofSeconds(2)).withoutStackTrace().toMap());
settings.put("jdk.ExecutionSample#period", "10 ms");
recording.setSettings(settings);
```

The following example shows how to merge settings.

```java
Map<String, String> settings = recording.getSettings();
settings.putAll(additionalSettings);
recording.setSettings(settings);
```

**Parameters:** settings

- the settings to set, not

null

---

#### setSettings

public void setSettings​(

Map

<

String

,​

String

> settings)

Replaces all settings for this recording.

The following example shows how to set event settings for a recording.

```java
Map<String, String> settings = new HashMap<>();
settings.putAll(EventSettings.enabled("jdk.CPUSample").withPeriod(Duration.ofSeconds(2)).toMap());
settings.putAll(EventSettings.enabled(MyEvent.class).withThreshold(Duration.ofSeconds(2)).withoutStackTrace().toMap());
settings.put("jdk.ExecutionSample#period", "10 ms");
recording.setSettings(settings);
```

The following example shows how to merge settings.

```java
Map<String, String> settings = recording.getSettings();
settings.putAll(additionalSettings);
recording.setSettings(settings);
```

The following example shows how to set event settings for a recording.

```java
Map<String, String> settings = new HashMap<>();
settings.putAll(EventSettings.enabled("jdk.CPUSample").withPeriod(Duration.ofSeconds(2)).toMap());
settings.putAll(EventSettings.enabled(MyEvent.class).withThreshold(Duration.ofSeconds(2)).withoutStackTrace().toMap());
settings.put("jdk.ExecutionSample#period", "10 ms");
recording.setSettings(settings);
```

The following example shows how to merge settings.

```java
Map<String, String> settings = recording.getSettings();
settings.putAll(additionalSettings);
recording.setSettings(settings);
```

Map<String, String> settings = new HashMap<>();
settings.putAll(EventSettings.enabled("jdk.CPUSample").withPeriod(Duration.ofSeconds(2)).toMap());
settings.putAll(EventSettings.enabled(MyEvent.class).withThreshold(Duration.ofSeconds(2)).withoutStackTrace().toMap());
settings.put("jdk.ExecutionSample#period", "10 ms");
recording.setSettings(settings);

Map<String, String> settings = recording.getSettings();
settings.putAll(additionalSettings);
recording.setSettings(settings);

getState

```java
public
RecordingState
getState()
```

Returns the recording state that this recording is currently in.

**Returns:** the recording state, not

null
**See Also:** RecordingState

---

#### getState

public

RecordingState

getState()

Returns the recording state that this recording is currently in.

close

```java
public void close()
```

Releases all data that is associated with this recording.

After a successful invocation of this method, this recording is in the

CLOSED

state.

**Specified by:** close

in interface

AutoCloseable
**Specified by:** close

in interface

Closeable

---

#### close

public void close()

Releases all data that is associated with this recording.

After a successful invocation of this method, this recording is in the

CLOSED

state.

After a successful invocation of this method, this recording is in the

CLOSED

state.

copy

```java
public
Recording
copy​(boolean stop)
```

Returns a clone of this recording, with a new recording ID and name.

Clones are useful for dumping data without stopping the recording. After
a clone is created, the amount of data to copy is constrained
with the

setMaxAge(Duration)

method and the

setMaxSize(long)

method.

**Parameters:** stop

-

true

if the newly created copy should be stopped
immediately,

false

otherwise
**Returns:** the recording copy, not

null

---

#### copy

public

Recording

copy​(boolean stop)

Returns a clone of this recording, with a new recording ID and name.

Clones are useful for dumping data without stopping the recording. After
a clone is created, the amount of data to copy is constrained
with the

setMaxAge(Duration)

method and the

setMaxSize(long)

method.

dump

```java
public void dump​(
Path
destination)
throws
IOException
```

Writes recording data to a file.

Recording must be started, but not necessarily stopped.

**Parameters:** destination

- the location where recording data is written, not

null
**Throws:** IOException

- if the recording can't be copied to the specified
location
**Throws:** SecurityException

- if a security manager exists and the caller doesn't
have

FilePermission

to write to the destination path

---

#### dump

public void dump​(

Path

destination)
throws

IOException

Writes recording data to a file.

Recording must be started, but not necessarily stopped.

Recording must be started, but not necessarily stopped.

isToDisk

```java
public boolean isToDisk()
```

Returns

true

if this recording uses the disk repository,

false

otherwise.

If no value is set,

true

is returned.

**Returns:** true

if the recording uses the disk repository,

false

otherwise

---

#### isToDisk

public boolean isToDisk()

Returns

true

if this recording uses the disk repository,

false

otherwise.

If no value is set,

true

is returned.

If no value is set,

true

is returned.

setMaxSize

```java
public void setMaxSize​(long maxSize)
```

Determines how much data is kept in the disk repository.

To control the amount of recording data that is stored on disk, the maximum
amount of data to retain can be specified. When the maximum limit is
exceeded, the Java Virtual Machine (JVM) removes the oldest chunk to make
room for a more recent chunk.

If neither maximum limit or the maximum age is set, the size of the
recording may grow indefinitely.

**Parameters:** maxSize

- the amount of data to retain,

0

if infinite
**Throws:** IllegalArgumentException

- if

maxSize

is negative
**Throws:** IllegalStateException

- if the recording is in

CLOSED

state

---

#### setMaxSize

public void setMaxSize​(long maxSize)

Determines how much data is kept in the disk repository.

To control the amount of recording data that is stored on disk, the maximum
amount of data to retain can be specified. When the maximum limit is
exceeded, the Java Virtual Machine (JVM) removes the oldest chunk to make
room for a more recent chunk.

If neither maximum limit or the maximum age is set, the size of the
recording may grow indefinitely.

To control the amount of recording data that is stored on disk, the maximum
amount of data to retain can be specified. When the maximum limit is
exceeded, the Java Virtual Machine (JVM) removes the oldest chunk to make
room for a more recent chunk.

If neither maximum limit or the maximum age is set, the size of the
recording may grow indefinitely.

If neither maximum limit or the maximum age is set, the size of the
recording may grow indefinitely.

setMaxAge

```java
public void setMaxAge​(
Duration
maxAge)
```

Determines how far back data is kept in the disk repository.

To control the amount of recording data stored on disk, the maximum length of
time to retain the data can be specified. Data stored on disk that is older
than the specified length of time is removed by the Java Virtual Machine (JVM).

If neither maximum limit or the maximum age is set, the size of the
recording may grow indefinitely.

**Parameters:** maxAge

- the length of time that data is kept, or

null

if infinite
**Throws:** IllegalArgumentException

- if

maxAge

is negative
**Throws:** IllegalStateException

- if the recording is in the

CLOSED

state

---

#### setMaxAge

public void setMaxAge​(

Duration

maxAge)

Determines how far back data is kept in the disk repository.

To control the amount of recording data stored on disk, the maximum length of
time to retain the data can be specified. Data stored on disk that is older
than the specified length of time is removed by the Java Virtual Machine (JVM).

If neither maximum limit or the maximum age is set, the size of the
recording may grow indefinitely.

To control the amount of recording data stored on disk, the maximum length of
time to retain the data can be specified. Data stored on disk that is older
than the specified length of time is removed by the Java Virtual Machine (JVM).

If neither maximum limit or the maximum age is set, the size of the
recording may grow indefinitely.

If neither maximum limit or the maximum age is set, the size of the
recording may grow indefinitely.

setDestination

```java
public void setDestination​(
Path
destination)
throws
IOException
```

Sets a location where data is written on recording stop, or

null

if data is not to be dumped.

If a destination is set, this recording is automatically closed
after data is successfully copied to the destination path.

If a destination is

not

set, Flight Recorder retains the
recording data until this recording is closed. Use the

dump(Path)

method to
manually write data to a file.

**Parameters:** destination

- the destination path, or

null

if recording should
not be dumped at stop
**Throws:** IllegalStateException

- if recording is in the

STOPPED

or

CLOSED

state.
**Throws:** SecurityException

- if a security manager exists and the caller
doesn't have

FilePermission

to read, write, and delete the

destination

file
**Throws:** IOException

- if the path is not writable

---

#### setDestination

public void setDestination​(

Path

destination)
throws

IOException

Sets a location where data is written on recording stop, or

null

if data is not to be dumped.

If a destination is set, this recording is automatically closed
after data is successfully copied to the destination path.

If a destination is

not

set, Flight Recorder retains the
recording data until this recording is closed. Use the

dump(Path)

method to
manually write data to a file.

If a destination is set, this recording is automatically closed
after data is successfully copied to the destination path.

If a destination is

not

set, Flight Recorder retains the
recording data until this recording is closed. Use the

dump(Path)

method to
manually write data to a file.

If a destination is

not

set, Flight Recorder retains the
recording data until this recording is closed. Use the

dump(Path)

method to
manually write data to a file.

getDestination

```java
public
Path
getDestination()
```

Returns the destination file, where recording data is written when the
recording stops, or

null

if no destination is set.

**Returns:** the destination file, or

null

if not set.

---

#### getDestination

public

Path

getDestination()

Returns the destination file, where recording data is written when the
recording stops, or

null

if no destination is set.

getId

```java
public long getId()
```

Returns a unique ID for this recording.

**Returns:** the recording ID

---

#### getId

public long getId()

Returns a unique ID for this recording.

setName

```java
public void setName​(
String
name)
```

Sets a human-readable name (for example,

"My Recording"

).

**Parameters:** name

- the recording name, not

null
**Throws:** IllegalStateException

- if the recording is in

CLOSED

state

---

#### setName

public void setName​(

String

name)

Sets a human-readable name (for example,

"My Recording"

).

setDumpOnExit

```java
public void setDumpOnExit​(boolean dumpOnExit)
```

Sets whether this recording is dumped to disk when the JVM exits.

**Parameters:** dumpOnExit

- if this recording should be dumped when the JVM exits

---

#### setDumpOnExit

public void setDumpOnExit​(boolean dumpOnExit)

Sets whether this recording is dumped to disk when the JVM exits.

getDumpOnExit

```java
public boolean getDumpOnExit()
```

Returns whether this recording is dumped to disk when the JVM exits.

If dump on exit is not set,

false

is returned.

**Returns:** true

if the recording is dumped on exit,

false

otherwise.

---

#### getDumpOnExit

public boolean getDumpOnExit()

Returns whether this recording is dumped to disk when the JVM exits.

If dump on exit is not set,

false

is returned.

If dump on exit is not set,

false

is returned.

setToDisk

```java
public void setToDisk​(boolean disk)
```

Determines whether this recording is continuously flushed to the disk
repository or data is constrained to what is available in memory buffers.

**Parameters:** disk

-

true

if this recording is written to disk,

false

if in-memory

---

#### setToDisk

public void setToDisk​(boolean disk)

Determines whether this recording is continuously flushed to the disk
repository or data is constrained to what is available in memory buffers.

getStream

```java
public
InputStream
getStream​(
Instant
start,

Instant
end)
throws
IOException
```

Creates a data stream for a specified interval.

The stream may contain some data outside the specified range.

**Parameters:** the

- start start time for the stream, or

null

to get data from
start time of the recording
**Parameters:** the

- end end time for the stream, or

null

to get data until the
present time.
**Returns:** an input stream, or

null

if no data is available in the
interval.
**Throws:** IllegalArgumentException

- if

end

happens before

start
**Throws:** IOException

- if a stream can't be opened

---

#### getStream

public

InputStream

getStream​(

Instant

start,

Instant

end)
throws

IOException

Creates a data stream for a specified interval.

The stream may contain some data outside the specified range.

The stream may contain some data outside the specified range.

getDuration

```java
public
Duration
getDuration()
```

Returns the specified duration for this recording, or

null

if no
duration is set.

The duration can be set only when the recording is in the

RecordingState.NEW

state.

**Returns:** the desired duration of the recording, or

null

if no duration
has been set.

---

#### getDuration

public

Duration

getDuration()

Returns the specified duration for this recording, or

null

if no
duration is set.

The duration can be set only when the recording is in the

RecordingState.NEW

state.

The duration can be set only when the recording is in the

RecordingState.NEW

state.

setDuration

```java
public void setDuration​(
Duration
duration)
```

Sets a duration for how long a recording runs before it stops.

By default, a recording has no duration (

null

).

**Parameters:** duration

- the duration, or

null

if no duration is set
**Throws:** IllegalStateException

- if recording is in the

STOPPED

or

CLOSED

state

---

#### setDuration

public void setDuration​(

Duration

duration)

Sets a duration for how long a recording runs before it stops.

By default, a recording has no duration (

null

).

By default, a recording has no duration (

null

).

enable

```java
public
EventSettings
enable​(
String
name)
```

Enables the event with the specified name.

If multiple events have the same name (for example, the same class is loaded
in different class loaders), then all events that match the name are enabled. To
enable a specific class, use the

enable(Class)

method or a

String

representation of the event type ID.

**Parameters:** name

- the settings for the event, not

null
**Returns:** an event setting for further configuration, not

null
**See Also:** EventType

---

#### enable

public

EventSettings

enable​(

String

name)

Enables the event with the specified name.

If multiple events have the same name (for example, the same class is loaded
in different class loaders), then all events that match the name are enabled. To
enable a specific class, use the

enable(Class)

method or a

String

representation of the event type ID.

If multiple events have the same name (for example, the same class is loaded
in different class loaders), then all events that match the name are enabled. To
enable a specific class, use the

enable(Class)

method or a

String

representation of the event type ID.

disable

```java
public
EventSettings
disable​(
String
name)
```

Disables event with the specified name.

If multiple events with same name (for example, the same class is loaded
in different class loaders), then all events that match the
name is disabled. To disable a specific class, use the

disable(Class)

method or a

String

representation of the event
type ID.

**Parameters:** name

- the settings for the event, not

null
**Returns:** an event setting for further configuration, not

null

---

#### disable

public

EventSettings

disable​(

String

name)

Disables event with the specified name.

If multiple events with same name (for example, the same class is loaded
in different class loaders), then all events that match the
name is disabled. To disable a specific class, use the

disable(Class)

method or a

String

representation of the event
type ID.

If multiple events with same name (for example, the same class is loaded
in different class loaders), then all events that match the
name is disabled. To disable a specific class, use the

disable(Class)

method or a

String

representation of the event
type ID.

enable

```java
public
EventSettings
enable​(
Class
<? extends
Event
> eventClass)
```

Enables event.

**Parameters:** eventClass

- the event to enable, not

null
**Returns:** an event setting for further configuration, not

null
**Throws:** IllegalArgumentException

- if

eventClass

is an abstract
class or not a subclass of

Event

---

#### enable

public

EventSettings

enable​(

Class

<? extends

Event

> eventClass)

Enables event.

disable

```java
public
EventSettings
disable​(
Class
<? extends
Event
> eventClass)
```

Disables event.

**Parameters:** eventClass

- the event to enable, not

null
**Returns:** an event setting for further configuration, not

null
**Throws:** IllegalArgumentException

- if

eventClass

is an abstract
class or not a subclass of

Event

---

#### disable

public

EventSettings

disable​(

Class

<? extends

Event

> eventClass)

Disables event.

---

