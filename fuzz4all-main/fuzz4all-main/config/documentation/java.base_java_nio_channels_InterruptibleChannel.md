# Interface InterruptibleChannel

**Source:** `java.base\java\nio\channels\InterruptibleChannel.html`

### Class Description

```java
public interface
InterruptibleChannel

extends
Channel
```

A channel that can be asynchronously closed and interrupted.

A channel that implements this interface is

asynchronously
closeable:

If a thread is blocked in an I/O operation on an
interruptible channel then another thread may invoke the channel's

close

method. This will cause the blocked thread to receive an

AsynchronousCloseException

.

A channel that implements this interface is also

interruptible:

If a thread is blocked in an I/O operation on an interruptible channel then
another thread may invoke the blocked thread's

interrupt

method. This will cause the channel to be closed, the blocked
thread to receive a

ClosedByInterruptException

, and the blocked
thread's interrupt status to be set.

If a thread's interrupt status is already set and it invokes a blocking
I/O operation upon a channel then the channel will be closed and the thread
will immediately receive a

ClosedByInterruptException

; its interrupt
status will remain set.

A channel supports asynchronous closing and interruption if, and only
if, it implements this interface. This can be tested at runtime, if
necessary, via the

instanceof

operator.

**All Superinterfaces:** AutoCloseable

,

Channel

,

Closeable

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### void close()
throws
IOException

Closes this channel.

Any thread currently blocked in an I/O operation upon this channel
will receive an

AsynchronousCloseException

.

This method otherwise behaves exactly as specified by the

Channel

interface.

**Specified by:**
- close

in interface

AutoCloseable
- close

in interface

Channel
- close

in interface

Closeable

**Throws:**
- IOException

- If an I/O error occurs

---

### Additional Sections

#### Interface InterruptibleChannel

**All Superinterfaces:** AutoCloseable

,

Channel

,

Closeable

**All Known Implementing Classes:** AbstractInterruptibleChannel

,

AbstractSelectableChannel

,

DatagramChannel

,

FileChannel

,

Pipe.SinkChannel

,

Pipe.SourceChannel

,

SctpChannel

,

SctpMultiChannel

,

SctpServerChannel

,

SelectableChannel

,

ServerSocketChannel

,

SocketChannel

```java
public interface
InterruptibleChannel

extends
Channel
```

A channel that can be asynchronously closed and interrupted.

A channel that implements this interface is

asynchronously
closeable:

If a thread is blocked in an I/O operation on an
interruptible channel then another thread may invoke the channel's

close

method. This will cause the blocked thread to receive an

AsynchronousCloseException

.

A channel that implements this interface is also

interruptible:

If a thread is blocked in an I/O operation on an interruptible channel then
another thread may invoke the blocked thread's

interrupt

method. This will cause the channel to be closed, the blocked
thread to receive a

ClosedByInterruptException

, and the blocked
thread's interrupt status to be set.

If a thread's interrupt status is already set and it invokes a blocking
I/O operation upon a channel then the channel will be closed and the thread
will immediately receive a

ClosedByInterruptException

; its interrupt
status will remain set.

A channel supports asynchronous closing and interruption if, and only
if, it implements this interface. This can be tested at runtime, if
necessary, via the

instanceof

operator.

**Since:** 1.4

public interface

InterruptibleChannel

extends

Channel

A channel that can be asynchronously closed and interrupted.

A channel that implements this interface is

asynchronously
closeable:

If a thread is blocked in an I/O operation on an
interruptible channel then another thread may invoke the channel's

close

method. This will cause the blocked thread to receive an

AsynchronousCloseException

.

A channel that implements this interface is also

interruptible:

If a thread is blocked in an I/O operation on an interruptible channel then
another thread may invoke the blocked thread's

interrupt

method. This will cause the channel to be closed, the blocked
thread to receive a

ClosedByInterruptException

, and the blocked
thread's interrupt status to be set.

If a thread's interrupt status is already set and it invokes a blocking
I/O operation upon a channel then the channel will be closed and the thread
will immediately receive a

ClosedByInterruptException

; its interrupt
status will remain set.

A channel supports asynchronous closing and interruption if, and only
if, it implements this interface. This can be tested at runtime, if
necessary, via the

instanceof

operator.

A channel that implements this interface is

asynchronously
closeable:

If a thread is blocked in an I/O operation on an
interruptible channel then another thread may invoke the channel's

close

method. This will cause the blocked thread to receive an

AsynchronousCloseException

.

A channel that implements this interface is also

interruptible:

If a thread is blocked in an I/O operation on an interruptible channel then
another thread may invoke the blocked thread's

interrupt

method. This will cause the channel to be closed, the blocked
thread to receive a

ClosedByInterruptException

, and the blocked
thread's interrupt status to be set.

If a thread's interrupt status is already set and it invokes a blocking
I/O operation upon a channel then the channel will be closed and the thread
will immediately receive a

ClosedByInterruptException

; its interrupt
status will remain set.

A channel supports asynchronous closing and interruption if, and only
if, it implements this interface. This can be tested at runtime, if
necessary, via the

instanceof

operator.

A channel that implements this interface is also

interruptible:

If a thread is blocked in an I/O operation on an interruptible channel then
another thread may invoke the blocked thread's

interrupt

method. This will cause the channel to be closed, the blocked
thread to receive a

ClosedByInterruptException

, and the blocked
thread's interrupt status to be set.

If a thread's interrupt status is already set and it invokes a blocking
I/O operation upon a channel then the channel will be closed and the thread
will immediately receive a

ClosedByInterruptException

; its interrupt
status will remain set.

A channel supports asynchronous closing and interruption if, and only
if, it implements this interface. This can be tested at runtime, if
necessary, via the

instanceof

operator.

If a thread's interrupt status is already set and it invokes a blocking
I/O operation upon a channel then the channel will be closed and the thread
will immediately receive a

ClosedByInterruptException

; its interrupt
status will remain set.

A channel supports asynchronous closing and interruption if, and only
if, it implements this interface. This can be tested at runtime, if
necessary, via the

instanceof

operator.

A channel supports asynchronous closing and interruption if, and only
if, it implements this interface. This can be tested at runtime, if
necessary, via the

instanceof

operator.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

close

()

Closes this channel.

- Methods declared in interface java.nio.channels.

Channel

isOpen

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

close

()

Closes this channel.

- Methods declared in interface java.nio.channels.

Channel

isOpen

---

#### Method Summary

Closes this channel.

Methods declared in interface java.nio.channels.

Channel

isOpen

---

#### Methods declared in interface java.nio.channels. Channel

============ METHOD DETAIL ==========

- Method Detail

- close

```java
void close()
throws
IOException
```

Closes this channel.

Any thread currently blocked in an I/O operation upon this channel
will receive an

AsynchronousCloseException

.

This method otherwise behaves exactly as specified by the

Channel

interface.

**Specified by:** close

in interface

AutoCloseable
**Specified by:** close

in interface

Channel
**Specified by:** close

in interface

Closeable
**Throws:** IOException

- If an I/O error occurs

Method Detail

- close

```java
void close()
throws
IOException
```

Closes this channel.

Any thread currently blocked in an I/O operation upon this channel
will receive an

AsynchronousCloseException

.

This method otherwise behaves exactly as specified by the

Channel

interface.

**Specified by:** close

in interface

AutoCloseable
**Specified by:** close

in interface

Channel
**Specified by:** close

in interface

Closeable
**Throws:** IOException

- If an I/O error occurs

---

#### Method Detail

close

```java
void close()
throws
IOException
```

Closes this channel.

Any thread currently blocked in an I/O operation upon this channel
will receive an

AsynchronousCloseException

.

This method otherwise behaves exactly as specified by the

Channel

interface.

**Specified by:** close

in interface

AutoCloseable
**Specified by:** close

in interface

Channel
**Specified by:** close

in interface

Closeable
**Throws:** IOException

- If an I/O error occurs

---

#### close

void close()
throws

IOException

Closes this channel.

Any thread currently blocked in an I/O operation upon this channel
will receive an

AsynchronousCloseException

.

This method otherwise behaves exactly as specified by the

Channel

interface.

Any thread currently blocked in an I/O operation upon this channel
will receive an

AsynchronousCloseException

.

This method otherwise behaves exactly as specified by the

Channel

interface.

This method otherwise behaves exactly as specified by the

Channel

interface.

---

