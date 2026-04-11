# Class RecordingFile

**Source:** `jdk.jfr\jdk\jfr\consumer\RecordingFile.html`

### Class Description

```java
public final class
RecordingFile

extends
Object

implements
Closeable
```

A recording file.

The following example shows how read and print all events in a recording file.

```java
try (RecordingFile recordingFile = new RecordingFile(Paths.get("recording.jfr"))) {
while (recordingFile.hasMoreEvents()) {
RecordedEvent event = recordingFile.readEvent();
System.out.println(event);
}
}
```

**All Implemented Interfaces:** Closeable

,

AutoCloseable

---

### Field Details

*No entries found.*

### Constructor Details

#### public RecordingFile​(
Path
file)
throws
IOException

Creates a recording file.

Only recording files from trusted sources should be used.

**Parameters:**
- file

- the path of the file to open, not

null

**Throws:**
- IOException

- if it's not a valid recording file, or an I/O error
occurred
- NoSuchFileException

- if the

file

can't be located
- SecurityException

- if a security manager exists and its

checkRead

method denies read access to the file.

---

### Method Details

#### public
RecordedEvent
readEvent()
throws
IOException

Reads the next event in the recording.

**Returns:**
- the next event, not

null

**Throws:**
- EOFException

- if no more events exist in the recording file
- IOException

- if an I/O error occurs.

**See Also:**
- hasMoreEvents()

---

#### public boolean hasMoreEvents()

Returns

true

if unread events exist in the recording file,

false

otherwise.

**Returns:**
- true

if unread events exist in the recording,

false

otherwise.

---

#### public
List
<
EventType
> readEventTypes()
throws
IOException

Returns a list of all event types in this recording.

**Returns:**
- a list of event types, not

null

**Throws:**
- IOException

- if an I/O error occurred while reading from the file

**See Also:**
- hasMoreEvents()

---

#### public void close()
throws
IOException

Closes this recording file and releases any system resources that are
associated with it.

**Specified by:**
- close

in interface

AutoCloseable
- close

in interface

Closeable

**Throws:**
- IOException

- if an I/O error occurred

---

#### public static
List
<
RecordedEvent
> readAllEvents​(
Path
path)
throws
IOException

Returns a list of all events in a file.

This method is intended for simple cases where it's convenient to read all
events in a single operation. It isn't intended for reading large files.

Only recording files from trusted sources should be used.

**Parameters:**
- path

- the path to the file, not

null

**Returns:**
- the events from the file as a

List

object; whether the

List

is modifiable or not is implementation dependent and
therefore not specified, not

null

**Throws:**
- IOException

- if an I/O error occurred, it's not a Flight Recorder
file or a version of a JFR file that can't be parsed
- SecurityException

- if a security manager exists and its

checkRead

method denies read access to the file.

---

### Additional Sections

#### Class RecordingFile

java.lang.Object

- jdk.jfr.consumer.RecordingFile

jdk.jfr.consumer.RecordingFile

**All Implemented Interfaces:** Closeable

,

AutoCloseable

```java
public final class
RecordingFile

extends
Object

implements
Closeable
```

A recording file.

The following example shows how read and print all events in a recording file.

```java
try (RecordingFile recordingFile = new RecordingFile(Paths.get("recording.jfr"))) {
while (recordingFile.hasMoreEvents()) {
RecordedEvent event = recordingFile.readEvent();
System.out.println(event);
}
}
```

**Since:** 9

public final class

RecordingFile

extends

Object

implements

Closeable

A recording file.

The following example shows how read and print all events in a recording file.

```java
try (RecordingFile recordingFile = new RecordingFile(Paths.get("recording.jfr"))) {
while (recordingFile.hasMoreEvents()) {
RecordedEvent event = recordingFile.readEvent();
System.out.println(event);
}
}
```

The following example shows how read and print all events in a recording file.

```java
try (RecordingFile recordingFile = new RecordingFile(Paths.get("recording.jfr"))) {
while (recordingFile.hasMoreEvents()) {
RecordedEvent event = recordingFile.readEvent();
System.out.println(event);
}
}
```

try (RecordingFile recordingFile = new RecordingFile(Paths.get("recording.jfr"))) {
while (recordingFile.hasMoreEvents()) {
RecordedEvent event = recordingFile.readEvent();
System.out.println(event);
}
}

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

RecordingFile

​(

Path

file)

Creates a recording file.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

close

()

Closes this recording file and releases any system resources that are
associated with it.

boolean

hasMoreEvents

()

Returns

true

if unread events exist in the recording file,

false

otherwise.

static

List

<

RecordedEvent

>

readAllEvents

​(

Path

path)

Returns a list of all events in a file.

RecordedEvent

readEvent

()

Reads the next event in the recording.

List

<

EventType

>

readEventTypes

()

Returns a list of all event types in this recording.

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

RecordingFile

​(

Path

file)

Creates a recording file.

---

#### Constructor Summary

Creates a recording file.

Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

close

()

Closes this recording file and releases any system resources that are
associated with it.

boolean

hasMoreEvents

()

Returns

true

if unread events exist in the recording file,

false

otherwise.

static

List

<

RecordedEvent

>

readAllEvents

​(

Path

path)

Returns a list of all events in a file.

RecordedEvent

readEvent

()

Reads the next event in the recording.

List

<

EventType

>

readEventTypes

()

Returns a list of all event types in this recording.

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

Closes this recording file and releases any system resources that are
associated with it.

Returns

true

if unread events exist in the recording file,

false

otherwise.

Returns a list of all events in a file.

Reads the next event in the recording.

Returns a list of all event types in this recording.

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

- RecordingFile

```java
public RecordingFile​(
Path
file)
throws
IOException
```

Creates a recording file.

Only recording files from trusted sources should be used.

**Parameters:** file

- the path of the file to open, not

null
**Throws:** IOException

- if it's not a valid recording file, or an I/O error
occurred
**Throws:** NoSuchFileException

- if the

file

can't be located
**Throws:** SecurityException

- if a security manager exists and its

checkRead

method denies read access to the file.

============ METHOD DETAIL ==========

- Method Detail

- readEvent

```java
public
RecordedEvent
readEvent()
throws
IOException
```

Reads the next event in the recording.

**Returns:** the next event, not

null
**Throws:** EOFException

- if no more events exist in the recording file
**Throws:** IOException

- if an I/O error occurs.
**See Also:** hasMoreEvents()

- hasMoreEvents

```java
public boolean hasMoreEvents()
```

Returns

true

if unread events exist in the recording file,

false

otherwise.

**Returns:** true

if unread events exist in the recording,

false

otherwise.

- readEventTypes

```java
public
List
<
EventType
> readEventTypes()
throws
IOException
```

Returns a list of all event types in this recording.

**Returns:** a list of event types, not

null
**Throws:** IOException

- if an I/O error occurred while reading from the file
**See Also:** hasMoreEvents()

- close

```java
public void close()
throws
IOException
```

Closes this recording file and releases any system resources that are
associated with it.

**Specified by:** close

in interface

AutoCloseable
**Specified by:** close

in interface

Closeable
**Throws:** IOException

- if an I/O error occurred

- readAllEvents

```java
public static
List
<
RecordedEvent
> readAllEvents​(
Path
path)
throws
IOException
```

Returns a list of all events in a file.

This method is intended for simple cases where it's convenient to read all
events in a single operation. It isn't intended for reading large files.

Only recording files from trusted sources should be used.

**Parameters:** path

- the path to the file, not

null
**Returns:** the events from the file as a

List

object; whether the

List

is modifiable or not is implementation dependent and
therefore not specified, not

null
**Throws:** IOException

- if an I/O error occurred, it's not a Flight Recorder
file or a version of a JFR file that can't be parsed
**Throws:** SecurityException

- if a security manager exists and its

checkRead

method denies read access to the file.

Constructor Detail

- RecordingFile

```java
public RecordingFile​(
Path
file)
throws
IOException
```

Creates a recording file.

Only recording files from trusted sources should be used.

**Parameters:** file

- the path of the file to open, not

null
**Throws:** IOException

- if it's not a valid recording file, or an I/O error
occurred
**Throws:** NoSuchFileException

- if the

file

can't be located
**Throws:** SecurityException

- if a security manager exists and its

checkRead

method denies read access to the file.

---

#### Constructor Detail

RecordingFile

```java
public RecordingFile​(
Path
file)
throws
IOException
```

Creates a recording file.

Only recording files from trusted sources should be used.

**Parameters:** file

- the path of the file to open, not

null
**Throws:** IOException

- if it's not a valid recording file, or an I/O error
occurred
**Throws:** NoSuchFileException

- if the

file

can't be located
**Throws:** SecurityException

- if a security manager exists and its

checkRead

method denies read access to the file.

---

#### RecordingFile

public RecordingFile​(

Path

file)
throws

IOException

Creates a recording file.

Only recording files from trusted sources should be used.

Only recording files from trusted sources should be used.

Method Detail

- readEvent

```java
public
RecordedEvent
readEvent()
throws
IOException
```

Reads the next event in the recording.

**Returns:** the next event, not

null
**Throws:** EOFException

- if no more events exist in the recording file
**Throws:** IOException

- if an I/O error occurs.
**See Also:** hasMoreEvents()

- hasMoreEvents

```java
public boolean hasMoreEvents()
```

Returns

true

if unread events exist in the recording file,

false

otherwise.

**Returns:** true

if unread events exist in the recording,

false

otherwise.

- readEventTypes

```java
public
List
<
EventType
> readEventTypes()
throws
IOException
```

Returns a list of all event types in this recording.

**Returns:** a list of event types, not

null
**Throws:** IOException

- if an I/O error occurred while reading from the file
**See Also:** hasMoreEvents()

- close

```java
public void close()
throws
IOException
```

Closes this recording file and releases any system resources that are
associated with it.

**Specified by:** close

in interface

AutoCloseable
**Specified by:** close

in interface

Closeable
**Throws:** IOException

- if an I/O error occurred

- readAllEvents

```java
public static
List
<
RecordedEvent
> readAllEvents​(
Path
path)
throws
IOException
```

Returns a list of all events in a file.

This method is intended for simple cases where it's convenient to read all
events in a single operation. It isn't intended for reading large files.

Only recording files from trusted sources should be used.

**Parameters:** path

- the path to the file, not

null
**Returns:** the events from the file as a

List

object; whether the

List

is modifiable or not is implementation dependent and
therefore not specified, not

null
**Throws:** IOException

- if an I/O error occurred, it's not a Flight Recorder
file or a version of a JFR file that can't be parsed
**Throws:** SecurityException

- if a security manager exists and its

checkRead

method denies read access to the file.

---

#### Method Detail

readEvent

```java
public
RecordedEvent
readEvent()
throws
IOException
```

Reads the next event in the recording.

**Returns:** the next event, not

null
**Throws:** EOFException

- if no more events exist in the recording file
**Throws:** IOException

- if an I/O error occurs.
**See Also:** hasMoreEvents()

---

#### readEvent

public

RecordedEvent

readEvent()
throws

IOException

Reads the next event in the recording.

hasMoreEvents

```java
public boolean hasMoreEvents()
```

Returns

true

if unread events exist in the recording file,

false

otherwise.

**Returns:** true

if unread events exist in the recording,

false

otherwise.

---

#### hasMoreEvents

public boolean hasMoreEvents()

Returns

true

if unread events exist in the recording file,

false

otherwise.

readEventTypes

```java
public
List
<
EventType
> readEventTypes()
throws
IOException
```

Returns a list of all event types in this recording.

**Returns:** a list of event types, not

null
**Throws:** IOException

- if an I/O error occurred while reading from the file
**See Also:** hasMoreEvents()

---

#### readEventTypes

public

List

<

EventType

> readEventTypes()
throws

IOException

Returns a list of all event types in this recording.

close

```java
public void close()
throws
IOException
```

Closes this recording file and releases any system resources that are
associated with it.

**Specified by:** close

in interface

AutoCloseable
**Specified by:** close

in interface

Closeable
**Throws:** IOException

- if an I/O error occurred

---

#### close

public void close()
throws

IOException

Closes this recording file and releases any system resources that are
associated with it.

readAllEvents

```java
public static
List
<
RecordedEvent
> readAllEvents​(
Path
path)
throws
IOException
```

Returns a list of all events in a file.

This method is intended for simple cases where it's convenient to read all
events in a single operation. It isn't intended for reading large files.

Only recording files from trusted sources should be used.

**Parameters:** path

- the path to the file, not

null
**Returns:** the events from the file as a

List

object; whether the

List

is modifiable or not is implementation dependent and
therefore not specified, not

null
**Throws:** IOException

- if an I/O error occurred, it's not a Flight Recorder
file or a version of a JFR file that can't be parsed
**Throws:** SecurityException

- if a security manager exists and its

checkRead

method denies read access to the file.

---

#### readAllEvents

public static

List

<

RecordedEvent

> readAllEvents​(

Path

path)
throws

IOException

Returns a list of all events in a file.

This method is intended for simple cases where it's convenient to read all
events in a single operation. It isn't intended for reading large files.

Only recording files from trusted sources should be used.

This method is intended for simple cases where it's convenient to read all
events in a single operation. It isn't intended for reading large files.

Only recording files from trusted sources should be used.

Only recording files from trusted sources should be used.

---

