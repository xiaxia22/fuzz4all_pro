# Interface Channels.SelectableChannelCloser

**Source:** `jdk.net\jdk\nio\Channels.SelectableChannelCloser.html`

### Class Description

```java
public static interface
Channels.SelectableChannelCloser
```

An object used to coordinate the closing of a selectable channel created
by

readWriteSelectableChannel

.

**Enclosing class:** Channels

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### void implCloseChannel​(
SelectableChannel
sc)
throws
IOException

Closes a selectable channel.

This method is invoked by the channel's close method in order to
perform the actual work of closing the channel. This method is only
invoked if the channel has not yet been closed, and it is never
invoked more than once by the channel's close implementation.

An implementation of this method must arrange for any other
thread that is blocked in an I/O operation upon the channel to return
immediately, either by throwing an exception or by returning normally.
If the channel is

registered

with one or more

Selector

s then
the file descriptor should not be released until the

implReleaseChannel

method is invoked.

**Parameters:**
- sc

- The selectable channel

**Throws:**
- IOException

- If an I/O error occurs while closing the file descriptor

**See Also:**
- AbstractInterruptibleChannel.implCloseChannel()

---

#### void implReleaseChannel​(
SelectableChannel
sc)
throws
IOException

Release the file descriptor and any resources for a selectable
channel that closed while registered with one or more

Selector

s.

This method is for cases where a channel is closed when

registered

with one or more

Selector

s. A channel may remain registered
for some time after it is closed. This method is invoked when the
channel is eventually deregistered from the last

Selector

that it was registered with. It is invoked at most once.

**Parameters:**
- sc

- The closed selectable channel

**Throws:**
- IOException

- If an I/O error occurs

**See Also:**
- AbstractSelector.deregister(java.nio.channels.spi.AbstractSelectionKey)

**API Note:**
- This method is invoked while synchronized on the selector
and its selected-key set. Great care must be taken to avoid deadlocks
with other threads that also synchronize on these objects.

---

### Additional Sections

#### Interface Channels.SelectableChannelCloser

**Enclosing class:** Channels

```java
public static interface
Channels.SelectableChannelCloser
```

An object used to coordinate the closing of a selectable channel created
by

readWriteSelectableChannel

.

**Since:** 11

public static interface

Channels.SelectableChannelCloser

An object used to coordinate the closing of a selectable channel created
by

readWriteSelectableChannel

.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

implCloseChannel

​(

SelectableChannel

sc)

Closes a selectable channel.

void

implReleaseChannel

​(

SelectableChannel

sc)

Release the file descriptor and any resources for a selectable
channel that closed while registered with one or more

Selector

s.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

implCloseChannel

​(

SelectableChannel

sc)

Closes a selectable channel.

void

implReleaseChannel

​(

SelectableChannel

sc)

Release the file descriptor and any resources for a selectable
channel that closed while registered with one or more

Selector

s.

---

#### Method Summary

Closes a selectable channel.

Release the file descriptor and any resources for a selectable
channel that closed while registered with one or more

Selector

s.

============ METHOD DETAIL ==========

- Method Detail

- implCloseChannel

```java
void implCloseChannel​(
SelectableChannel
sc)
throws
IOException
```

Closes a selectable channel.

This method is invoked by the channel's close method in order to
perform the actual work of closing the channel. This method is only
invoked if the channel has not yet been closed, and it is never
invoked more than once by the channel's close implementation.

An implementation of this method must arrange for any other
thread that is blocked in an I/O operation upon the channel to return
immediately, either by throwing an exception or by returning normally.
If the channel is

registered

with one or more

Selector

s then
the file descriptor should not be released until the

implReleaseChannel

method is invoked.

**Parameters:** sc

- The selectable channel
**Throws:** IOException

- If an I/O error occurs while closing the file descriptor
**See Also:** AbstractInterruptibleChannel.implCloseChannel()

- implReleaseChannel

```java
void implReleaseChannel​(
SelectableChannel
sc)
throws
IOException
```

Release the file descriptor and any resources for a selectable
channel that closed while registered with one or more

Selector

s.

This method is for cases where a channel is closed when

registered

with one or more

Selector

s. A channel may remain registered
for some time after it is closed. This method is invoked when the
channel is eventually deregistered from the last

Selector

that it was registered with. It is invoked at most once.

**API Note:** This method is invoked while synchronized on the selector
and its selected-key set. Great care must be taken to avoid deadlocks
with other threads that also synchronize on these objects.
**Parameters:** sc

- The closed selectable channel
**Throws:** IOException

- If an I/O error occurs
**See Also:** AbstractSelector.deregister(java.nio.channels.spi.AbstractSelectionKey)

Method Detail

- implCloseChannel

```java
void implCloseChannel​(
SelectableChannel
sc)
throws
IOException
```

Closes a selectable channel.

This method is invoked by the channel's close method in order to
perform the actual work of closing the channel. This method is only
invoked if the channel has not yet been closed, and it is never
invoked more than once by the channel's close implementation.

An implementation of this method must arrange for any other
thread that is blocked in an I/O operation upon the channel to return
immediately, either by throwing an exception or by returning normally.
If the channel is

registered

with one or more

Selector

s then
the file descriptor should not be released until the

implReleaseChannel

method is invoked.

**Parameters:** sc

- The selectable channel
**Throws:** IOException

- If an I/O error occurs while closing the file descriptor
**See Also:** AbstractInterruptibleChannel.implCloseChannel()

- implReleaseChannel

```java
void implReleaseChannel​(
SelectableChannel
sc)
throws
IOException
```

Release the file descriptor and any resources for a selectable
channel that closed while registered with one or more

Selector

s.

This method is for cases where a channel is closed when

registered

with one or more

Selector

s. A channel may remain registered
for some time after it is closed. This method is invoked when the
channel is eventually deregistered from the last

Selector

that it was registered with. It is invoked at most once.

**API Note:** This method is invoked while synchronized on the selector
and its selected-key set. Great care must be taken to avoid deadlocks
with other threads that also synchronize on these objects.
**Parameters:** sc

- The closed selectable channel
**Throws:** IOException

- If an I/O error occurs
**See Also:** AbstractSelector.deregister(java.nio.channels.spi.AbstractSelectionKey)

---

#### Method Detail

implCloseChannel

```java
void implCloseChannel​(
SelectableChannel
sc)
throws
IOException
```

Closes a selectable channel.

This method is invoked by the channel's close method in order to
perform the actual work of closing the channel. This method is only
invoked if the channel has not yet been closed, and it is never
invoked more than once by the channel's close implementation.

An implementation of this method must arrange for any other
thread that is blocked in an I/O operation upon the channel to return
immediately, either by throwing an exception or by returning normally.
If the channel is

registered

with one or more

Selector

s then
the file descriptor should not be released until the

implReleaseChannel

method is invoked.

**Parameters:** sc

- The selectable channel
**Throws:** IOException

- If an I/O error occurs while closing the file descriptor
**See Also:** AbstractInterruptibleChannel.implCloseChannel()

---

#### implCloseChannel

void implCloseChannel​(

SelectableChannel

sc)
throws

IOException

Closes a selectable channel.

This method is invoked by the channel's close method in order to
perform the actual work of closing the channel. This method is only
invoked if the channel has not yet been closed, and it is never
invoked more than once by the channel's close implementation.

An implementation of this method must arrange for any other
thread that is blocked in an I/O operation upon the channel to return
immediately, either by throwing an exception or by returning normally.
If the channel is

registered

with one or more

Selector

s then
the file descriptor should not be released until the

implReleaseChannel

method is invoked.

This method is invoked by the channel's close method in order to
perform the actual work of closing the channel. This method is only
invoked if the channel has not yet been closed, and it is never
invoked more than once by the channel's close implementation.

An implementation of this method must arrange for any other
thread that is blocked in an I/O operation upon the channel to return
immediately, either by throwing an exception or by returning normally.
If the channel is

registered

with one or more

Selector

s then
the file descriptor should not be released until the

implReleaseChannel

method is invoked.

An implementation of this method must arrange for any other
thread that is blocked in an I/O operation upon the channel to return
immediately, either by throwing an exception or by returning normally.
If the channel is

registered

with one or more

Selector

s then
the file descriptor should not be released until the

implReleaseChannel

method is invoked.

implReleaseChannel

```java
void implReleaseChannel​(
SelectableChannel
sc)
throws
IOException
```

Release the file descriptor and any resources for a selectable
channel that closed while registered with one or more

Selector

s.

This method is for cases where a channel is closed when

registered

with one or more

Selector

s. A channel may remain registered
for some time after it is closed. This method is invoked when the
channel is eventually deregistered from the last

Selector

that it was registered with. It is invoked at most once.

**API Note:** This method is invoked while synchronized on the selector
and its selected-key set. Great care must be taken to avoid deadlocks
with other threads that also synchronize on these objects.
**Parameters:** sc

- The closed selectable channel
**Throws:** IOException

- If an I/O error occurs
**See Also:** AbstractSelector.deregister(java.nio.channels.spi.AbstractSelectionKey)

---

#### implReleaseChannel

void implReleaseChannel​(

SelectableChannel

sc)
throws

IOException

Release the file descriptor and any resources for a selectable
channel that closed while registered with one or more

Selector

s.

This method is for cases where a channel is closed when

registered

with one or more

Selector

s. A channel may remain registered
for some time after it is closed. This method is invoked when the
channel is eventually deregistered from the last

Selector

that it was registered with. It is invoked at most once.

This method is for cases where a channel is closed when

registered

with one or more

Selector

s. A channel may remain registered
for some time after it is closed. This method is invoked when the
channel is eventually deregistered from the last

Selector

that it was registered with. It is invoked at most once.

---

