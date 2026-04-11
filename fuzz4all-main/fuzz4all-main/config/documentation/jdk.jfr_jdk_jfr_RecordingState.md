# Enum RecordingState

**Source:** `jdk.jfr\jdk\jfr\RecordingState.html`

### Class Description

```java
public enum
RecordingState

extends
Enum
<
RecordingState
>
```

Indicates a state in the life cycle of a recording.

**All Implemented Interfaces:** Serializable

,

Comparable

<

RecordingState

>

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### public static
RecordingState
[] values()

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (RecordingState c : RecordingState.values())
System.out.println(c);
```

**Returns:**
- an array containing the constants of this enum type, in the order they are declared

---

#### public static
RecordingState
valueOf​(
String
name)

Returns the enum constant of this type with the specified name.
The string must match

exactly

an identifier used to declare an
enum constant in this type. (Extraneous whitespace characters are
not permitted.)

**Parameters:**
- name

- the name of the enum constant to be returned.

**Returns:**
- the enum constant with the specified name

**Throws:**
- IllegalArgumentException

- if this enum type has no constant with the specified name
- NullPointerException

- if the argument is null

---

### Additional Sections

#### Enum RecordingState

java.lang.Object

- java.lang.Enum

<

RecordingState

>
- - jdk.jfr.RecordingState

java.lang.Enum

<

RecordingState

>

- jdk.jfr.RecordingState

jdk.jfr.RecordingState

**All Implemented Interfaces:** Serializable

,

Comparable

<

RecordingState

>

```java
public enum
RecordingState

extends
Enum
<
RecordingState
>
```

Indicates a state in the life cycle of a recording.

**Since:** 9

public enum

RecordingState

extends

Enum

<

RecordingState

>

Indicates a state in the life cycle of a recording.

=========== ENUM CONSTANT SUMMARY ===========

- Enum Constant Summary

Enum Constants

Enum Constant

Description

CLOSED

The recording is closed and all resources that are associated with the
recording are released.

DELAYED

The recording is scheduled to start with a start time in the future.

NEW

The initial state when a

Recording

is created.

RUNNING

The recording is recording data and an invocation of the

Recording.stop()

method will transition the recording to the

STOPPED

state.

STOPPED

The recording is stopped and is holding recorded data that can be dumped to
disk.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

RecordingState

valueOf

​(

String

name)

Returns the enum constant of this type with the specified name.

static

RecordingState

[]

values

()

Returns an array containing the constants of this enum type, in
the order they are declared.

- Methods declared in class java.lang.

Enum

clone

,

compareTo

,

equals

,

finalize

,

getDeclaringClass

,

hashCode

,

name

,

ordinal

,

toString

,

valueOf

- Methods declared in class java.lang.

Object

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

Enum Constant Summary

Enum Constants

Enum Constant

Description

CLOSED

The recording is closed and all resources that are associated with the
recording are released.

DELAYED

The recording is scheduled to start with a start time in the future.

NEW

The initial state when a

Recording

is created.

RUNNING

The recording is recording data and an invocation of the

Recording.stop()

method will transition the recording to the

STOPPED

state.

STOPPED

The recording is stopped and is holding recorded data that can be dumped to
disk.

---

#### Enum Constant Summary

The recording is closed and all resources that are associated with the
recording are released.

The recording is scheduled to start with a start time in the future.

The initial state when a

Recording

is created.

The recording is recording data and an invocation of the

Recording.stop()

method will transition the recording to the

STOPPED

state.

The recording is stopped and is holding recorded data that can be dumped to
disk.

Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

RecordingState

valueOf

​(

String

name)

Returns the enum constant of this type with the specified name.

static

RecordingState

[]

values

()

Returns an array containing the constants of this enum type, in
the order they are declared.

- Methods declared in class java.lang.

Enum

clone

,

compareTo

,

equals

,

finalize

,

getDeclaringClass

,

hashCode

,

name

,

ordinal

,

toString

,

valueOf

- Methods declared in class java.lang.

Object

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

Returns the enum constant of this type with the specified name.

Returns an array containing the constants of this enum type, in
the order they are declared.

Methods declared in class java.lang.

Enum

clone

,

compareTo

,

equals

,

finalize

,

getDeclaringClass

,

hashCode

,

name

,

ordinal

,

toString

,

valueOf

---

#### Methods declared in class java.lang. Enum

Methods declared in class java.lang.

Object

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

============ ENUM CONSTANT DETAIL ===========

- Enum Constant Detail

- NEW

```java
public static final
RecordingState
NEW
```

The initial state when a

Recording

is created.

- DELAYED

```java
public static final
RecordingState
DELAYED
```

The recording is scheduled to start with a start time in the future.

An invocation of the

Recording.start()

method will transition the
recording to the

RUNNING

state.

- RUNNING

```java
public static final
RecordingState
RUNNING
```

The recording is recording data and an invocation of the

Recording.stop()

method will transition the recording to the

STOPPED

state.

- STOPPED

```java
public static final
RecordingState
STOPPED
```

The recording is stopped and is holding recorded data that can be dumped to
disk.

An invocation of the

Recording.close()

method will release the
data and transition the recording to the

CLOSED

state.

- CLOSED

```java
public static final
RecordingState
CLOSED
```

The recording is closed and all resources that are associated with the
recording are released.

Nothing that can be done with a recording from this point, and it's
no longer retrievable from the

FlightRrecorder.getRecordings()

method.

============ METHOD DETAIL ==========

- Method Detail

- values

```java
public static
RecordingState
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (RecordingState c : RecordingState.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

- valueOf

```java
public static
RecordingState
valueOf​(
String
name)
```

Returns the enum constant of this type with the specified name.
The string must match

exactly

an identifier used to declare an
enum constant in this type. (Extraneous whitespace characters are
not permitted.)

**Parameters:** name

- the name of the enum constant to be returned.
**Returns:** the enum constant with the specified name
**Throws:** IllegalArgumentException

- if this enum type has no constant with the specified name
**Throws:** NullPointerException

- if the argument is null

Enum Constant Detail

- NEW

```java
public static final
RecordingState
NEW
```

The initial state when a

Recording

is created.

- DELAYED

```java
public static final
RecordingState
DELAYED
```

The recording is scheduled to start with a start time in the future.

An invocation of the

Recording.start()

method will transition the
recording to the

RUNNING

state.

- RUNNING

```java
public static final
RecordingState
RUNNING
```

The recording is recording data and an invocation of the

Recording.stop()

method will transition the recording to the

STOPPED

state.

- STOPPED

```java
public static final
RecordingState
STOPPED
```

The recording is stopped and is holding recorded data that can be dumped to
disk.

An invocation of the

Recording.close()

method will release the
data and transition the recording to the

CLOSED

state.

- CLOSED

```java
public static final
RecordingState
CLOSED
```

The recording is closed and all resources that are associated with the
recording are released.

Nothing that can be done with a recording from this point, and it's
no longer retrievable from the

FlightRrecorder.getRecordings()

method.

---

#### Enum Constant Detail

NEW

```java
public static final
RecordingState
NEW
```

The initial state when a

Recording

is created.

---

#### NEW

public static final

RecordingState

NEW

The initial state when a

Recording

is created.

DELAYED

```java
public static final
RecordingState
DELAYED
```

The recording is scheduled to start with a start time in the future.

An invocation of the

Recording.start()

method will transition the
recording to the

RUNNING

state.

---

#### DELAYED

public static final

RecordingState

DELAYED

The recording is scheduled to start with a start time in the future.

An invocation of the

Recording.start()

method will transition the
recording to the

RUNNING

state.

An invocation of the

Recording.start()

method will transition the
recording to the

RUNNING

state.

RUNNING

```java
public static final
RecordingState
RUNNING
```

The recording is recording data and an invocation of the

Recording.stop()

method will transition the recording to the

STOPPED

state.

---

#### RUNNING

public static final

RecordingState

RUNNING

The recording is recording data and an invocation of the

Recording.stop()

method will transition the recording to the

STOPPED

state.

STOPPED

```java
public static final
RecordingState
STOPPED
```

The recording is stopped and is holding recorded data that can be dumped to
disk.

An invocation of the

Recording.close()

method will release the
data and transition the recording to the

CLOSED

state.

---

#### STOPPED

public static final

RecordingState

STOPPED

The recording is stopped and is holding recorded data that can be dumped to
disk.

An invocation of the

Recording.close()

method will release the
data and transition the recording to the

CLOSED

state.

An invocation of the

Recording.close()

method will release the
data and transition the recording to the

CLOSED

state.

CLOSED

```java
public static final
RecordingState
CLOSED
```

The recording is closed and all resources that are associated with the
recording are released.

Nothing that can be done with a recording from this point, and it's
no longer retrievable from the

FlightRrecorder.getRecordings()

method.

---

#### CLOSED

public static final

RecordingState

CLOSED

The recording is closed and all resources that are associated with the
recording are released.

Nothing that can be done with a recording from this point, and it's
no longer retrievable from the

FlightRrecorder.getRecordings()

method.

Nothing that can be done with a recording from this point, and it's
no longer retrievable from the

FlightRrecorder.getRecordings()

method.

Method Detail

- values

```java
public static
RecordingState
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (RecordingState c : RecordingState.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

- valueOf

```java
public static
RecordingState
valueOf​(
String
name)
```

Returns the enum constant of this type with the specified name.
The string must match

exactly

an identifier used to declare an
enum constant in this type. (Extraneous whitespace characters are
not permitted.)

**Parameters:** name

- the name of the enum constant to be returned.
**Returns:** the enum constant with the specified name
**Throws:** IllegalArgumentException

- if this enum type has no constant with the specified name
**Throws:** NullPointerException

- if the argument is null

---

#### Method Detail

values

```java
public static
RecordingState
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (RecordingState c : RecordingState.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

---

#### values

public static

RecordingState

[] values()

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (RecordingState c : RecordingState.values())
System.out.println(c);
```

for (RecordingState c : RecordingState.values())
System.out.println(c);

valueOf

```java
public static
RecordingState
valueOf​(
String
name)
```

Returns the enum constant of this type with the specified name.
The string must match

exactly

an identifier used to declare an
enum constant in this type. (Extraneous whitespace characters are
not permitted.)

**Parameters:** name

- the name of the enum constant to be returned.
**Returns:** the enum constant with the specified name
**Throws:** IllegalArgumentException

- if this enum type has no constant with the specified name
**Throws:** NullPointerException

- if the argument is null

---

#### valueOf

public static

RecordingState

valueOf​(

String

name)

Returns the enum constant of this type with the specified name.
The string must match

exactly

an identifier used to declare an
enum constant in this type. (Extraneous whitespace characters are
not permitted.)

---

