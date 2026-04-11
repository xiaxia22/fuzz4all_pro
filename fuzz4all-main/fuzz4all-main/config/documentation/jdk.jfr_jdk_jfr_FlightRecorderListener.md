# Interface FlightRecorderListener

**Source:** `jdk.jfr\jdk\jfr\FlightRecorderListener.html`

### Class Description

```java
public interface
FlightRecorderListener
```

Callback interface to monitor Flight Recorder's life cycle.

**Since:** 9

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### default void recorderInitialized​(
FlightRecorder
recorder)

Receives notification when Flight Recorder is initialized.

This method is also be invoked when a listener is added to an already
initialized Flight Recorder.

This method allows clients to implement their own initialization mechanism
that is executed before a

FlightRecorder

instance is returned by

FlightRecorder#getFlightRecorder()

.

**Parameters:**
- recorder

- Flight Recorder instance, not

null

**See Also:**
- FlightRecorder.addListener(FlightRecorderListener)

**Implementation Requirements:**
- The default implementation of this method is empty.

**Implementation Note:**
- This method should return as soon as possible, to avoid blocking
initialization of Flight Recorder. To avoid deadlocks or unexpected
behavior, this method should not call

FlightRecorder.getFlightRecorder()

or start new recordings.

---

#### default void recordingStateChanged​(
Recording
recording)

Receives notification when the state of a recording changes.

Callback is invoked when a recording reaches the

RUNNING

,

STOPPED

and

CLOSED

state.

**Parameters:**
- recording

- the recording where the state change occurred, not

null

**See Also:**
- FlightRecorder.addListener(FlightRecorderListener)

,

RecordingState

**Implementation Requirements:**
- The default implementation of this method is empty.

**Implementation Note:**
- The implementation of this method should return as soon as possible
to avoid blocking normal operation of Flight Recorder.

---

### Additional Sections

#### Interface FlightRecorderListener

```java
public interface
FlightRecorderListener
```

Callback interface to monitor Flight Recorder's life cycle.

**Since:** 9

public interface

FlightRecorderListener

Callback interface to monitor Flight Recorder's life cycle.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Default Methods

Modifier and Type

Method

Description

default void

recorderInitialized

​(

FlightRecorder

recorder)

Receives notification when Flight Recorder is initialized.

default void

recordingStateChanged

​(

Recording

recording)

Receives notification when the state of a recording changes.

Method Summary

All Methods

Instance Methods

Default Methods

Modifier and Type

Method

Description

default void

recorderInitialized

​(

FlightRecorder

recorder)

Receives notification when Flight Recorder is initialized.

default void

recordingStateChanged

​(

Recording

recording)

Receives notification when the state of a recording changes.

---

#### Method Summary

Receives notification when Flight Recorder is initialized.

Receives notification when the state of a recording changes.

============ METHOD DETAIL ==========

- Method Detail

- recorderInitialized

```java
default void recorderInitialized​(
FlightRecorder
recorder)
```

Receives notification when Flight Recorder is initialized.

This method is also be invoked when a listener is added to an already
initialized Flight Recorder.

This method allows clients to implement their own initialization mechanism
that is executed before a

FlightRecorder

instance is returned by

FlightRecorder#getFlightRecorder()

.

**Implementation Requirements:** The default implementation of this method is empty.
**Implementation Note:** This method should return as soon as possible, to avoid blocking
initialization of Flight Recorder. To avoid deadlocks or unexpected
behavior, this method should not call

FlightRecorder.getFlightRecorder()

or start new recordings.
**Parameters:** recorder

- Flight Recorder instance, not

null
**See Also:** FlightRecorder.addListener(FlightRecorderListener)

- recordingStateChanged

```java
default void recordingStateChanged​(
Recording
recording)
```

Receives notification when the state of a recording changes.

Callback is invoked when a recording reaches the

RUNNING

,

STOPPED

and

CLOSED

state.

**Implementation Requirements:** The default implementation of this method is empty.
**Implementation Note:** The implementation of this method should return as soon as possible
to avoid blocking normal operation of Flight Recorder.
**Parameters:** recording

- the recording where the state change occurred, not

null
**See Also:** FlightRecorder.addListener(FlightRecorderListener)

,

RecordingState

Method Detail

- recorderInitialized

```java
default void recorderInitialized​(
FlightRecorder
recorder)
```

Receives notification when Flight Recorder is initialized.

This method is also be invoked when a listener is added to an already
initialized Flight Recorder.

This method allows clients to implement their own initialization mechanism
that is executed before a

FlightRecorder

instance is returned by

FlightRecorder#getFlightRecorder()

.

**Implementation Requirements:** The default implementation of this method is empty.
**Implementation Note:** This method should return as soon as possible, to avoid blocking
initialization of Flight Recorder. To avoid deadlocks or unexpected
behavior, this method should not call

FlightRecorder.getFlightRecorder()

or start new recordings.
**Parameters:** recorder

- Flight Recorder instance, not

null
**See Also:** FlightRecorder.addListener(FlightRecorderListener)

- recordingStateChanged

```java
default void recordingStateChanged​(
Recording
recording)
```

Receives notification when the state of a recording changes.

Callback is invoked when a recording reaches the

RUNNING

,

STOPPED

and

CLOSED

state.

**Implementation Requirements:** The default implementation of this method is empty.
**Implementation Note:** The implementation of this method should return as soon as possible
to avoid blocking normal operation of Flight Recorder.
**Parameters:** recording

- the recording where the state change occurred, not

null
**See Also:** FlightRecorder.addListener(FlightRecorderListener)

,

RecordingState

---

#### Method Detail

recorderInitialized

```java
default void recorderInitialized​(
FlightRecorder
recorder)
```

Receives notification when Flight Recorder is initialized.

This method is also be invoked when a listener is added to an already
initialized Flight Recorder.

This method allows clients to implement their own initialization mechanism
that is executed before a

FlightRecorder

instance is returned by

FlightRecorder#getFlightRecorder()

.

**Implementation Requirements:** The default implementation of this method is empty.
**Implementation Note:** This method should return as soon as possible, to avoid blocking
initialization of Flight Recorder. To avoid deadlocks or unexpected
behavior, this method should not call

FlightRecorder.getFlightRecorder()

or start new recordings.
**Parameters:** recorder

- Flight Recorder instance, not

null
**See Also:** FlightRecorder.addListener(FlightRecorderListener)

---

#### recorderInitialized

default void recorderInitialized​(

FlightRecorder

recorder)

Receives notification when Flight Recorder is initialized.

This method is also be invoked when a listener is added to an already
initialized Flight Recorder.

This method allows clients to implement their own initialization mechanism
that is executed before a

FlightRecorder

instance is returned by

FlightRecorder#getFlightRecorder()

.

This method is also be invoked when a listener is added to an already
initialized Flight Recorder.

This method allows clients to implement their own initialization mechanism
that is executed before a

FlightRecorder

instance is returned by

FlightRecorder#getFlightRecorder()

.

This method allows clients to implement their own initialization mechanism
that is executed before a

FlightRecorder

instance is returned by

FlightRecorder#getFlightRecorder()

.

recordingStateChanged

```java
default void recordingStateChanged​(
Recording
recording)
```

Receives notification when the state of a recording changes.

Callback is invoked when a recording reaches the

RUNNING

,

STOPPED

and

CLOSED

state.

**Implementation Requirements:** The default implementation of this method is empty.
**Implementation Note:** The implementation of this method should return as soon as possible
to avoid blocking normal operation of Flight Recorder.
**Parameters:** recording

- the recording where the state change occurred, not

null
**See Also:** FlightRecorder.addListener(FlightRecorderListener)

,

RecordingState

---

#### recordingStateChanged

default void recordingStateChanged​(

Recording

recording)

Receives notification when the state of a recording changes.

Callback is invoked when a recording reaches the

RUNNING

,

STOPPED

and

CLOSED

state.

Callback is invoked when a recording reaches the

RUNNING

,

STOPPED

and

CLOSED

state.

---

