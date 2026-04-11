# Class AbstractInterruptibleChannel

**Source:** `java.base\java\nio\channels\spi\AbstractInterruptibleChannel.html`

### Class Description

```java
public abstract class
AbstractInterruptibleChannel

extends
Object

implements
Channel
,
InterruptibleChannel
```

Base implementation class for interruptible channels.

This class encapsulates the low-level machinery required to implement
the asynchronous closing and interruption of channels. A concrete channel
class must invoke the

begin

and

end

methods
before and after, respectively, invoking an I/O operation that might block
indefinitely. In order to ensure that the

end

method is always
invoked, these methods should be used within a

try

...

finally

block:

```java
boolean completed = false;
try {
begin();
completed = ...; // Perform blocking I/O operation
return ...; // Return result
} finally {
end(completed);
}
```

The

completed

argument to the

end

method tells
whether or not the I/O operation actually completed, that is, whether it had
any effect that would be visible to the invoker. In the case of an
operation that reads bytes, for example, this argument should be

true

if, and only if, some bytes were actually transferred into the
invoker's target buffer.

A concrete channel class must also implement the

implCloseChannel

method in such a way that if it is
invoked while another thread is blocked in a native I/O operation upon the
channel then that operation will immediately return, either by throwing an
exception or by returning normally. If a thread is interrupted or the
channel upon which it is blocked is asynchronously closed then the channel's

end

method will throw the appropriate exception.

This class performs the synchronization required to implement the

Channel

specification. Implementations of the

implCloseChannel

method need not synchronize against
other threads that might be attempting to close the channel.

**All Implemented Interfaces:** Closeable

,

AutoCloseable

,

Channel

,

InterruptibleChannel

---

### Field Details

*No entries found.*

### Constructor Details

#### protected AbstractInterruptibleChannel()

Initializes a new instance of this class.

---

### Method Details

#### public final void close()
throws
IOException

Closes this channel.

If the channel has already been closed then this method returns
immediately. Otherwise it marks the channel as closed and then invokes
the

implCloseChannel

method in order to
complete the close operation.

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
- close

in interface

InterruptibleChannel

**Throws:**
- IOException

- If an I/O error occurs

---

#### protected abstract void implCloseChannel()
throws
IOException

Closes this channel.

This method is invoked by the

close

method in order
to perform the actual work of closing the channel. This method is only
invoked if the channel has not yet been closed, and it is never invoked
more than once.

An implementation of this method must arrange for any other thread
that is blocked in an I/O operation upon this channel to return
immediately, either by throwing an exception or by returning normally.

**Throws:**
- IOException

- If an I/O error occurs while closing the channel

---

#### protected final void begin()

Marks the beginning of an I/O operation that might block indefinitely.

This method should be invoked in tandem with the

end

method, using a

try

...

finally

block as
shown

above

, in order to implement asynchronous
closing and interruption for this channel.

---

#### protected final void end​(boolean completed)
throws
AsynchronousCloseException

Marks the end of an I/O operation that might block indefinitely.

This method should be invoked in tandem with the

begin

method, using a

try

...

finally

block
as shown

above

, in order to implement asynchronous
closing and interruption for this channel.

**Parameters:**
- completed

-

true

if, and only if, the I/O operation completed
successfully, that is, had some effect that would be visible to
the operation's invoker

**Throws:**
- AsynchronousCloseException

- If the channel was asynchronously closed
- ClosedByInterruptException

- If the thread blocked in the I/O operation was interrupted

---

### Additional Sections

#### Class AbstractInterruptibleChannel

java.lang.Object

- java.nio.channels.spi.AbstractInterruptibleChannel

java.nio.channels.spi.AbstractInterruptibleChannel

**All Implemented Interfaces:** Closeable

,

AutoCloseable

,

Channel

,

InterruptibleChannel

**Direct Known Subclasses:** FileChannel

,

SelectableChannel

```java
public abstract class
AbstractInterruptibleChannel

extends
Object

implements
Channel
,
InterruptibleChannel
```

Base implementation class for interruptible channels.

This class encapsulates the low-level machinery required to implement
the asynchronous closing and interruption of channels. A concrete channel
class must invoke the

begin

and

end

methods
before and after, respectively, invoking an I/O operation that might block
indefinitely. In order to ensure that the

end

method is always
invoked, these methods should be used within a

try

...

finally

block:

```java
boolean completed = false;
try {
begin();
completed = ...; // Perform blocking I/O operation
return ...; // Return result
} finally {
end(completed);
}
```

The

completed

argument to the

end

method tells
whether or not the I/O operation actually completed, that is, whether it had
any effect that would be visible to the invoker. In the case of an
operation that reads bytes, for example, this argument should be

true

if, and only if, some bytes were actually transferred into the
invoker's target buffer.

A concrete channel class must also implement the

implCloseChannel

method in such a way that if it is
invoked while another thread is blocked in a native I/O operation upon the
channel then that operation will immediately return, either by throwing an
exception or by returning normally. If a thread is interrupted or the
channel upon which it is blocked is asynchronously closed then the channel's

end

method will throw the appropriate exception.

This class performs the synchronization required to implement the

Channel

specification. Implementations of the

implCloseChannel

method need not synchronize against
other threads that might be attempting to close the channel.

**Since:** 1.4

public abstract class

AbstractInterruptibleChannel

extends

Object

implements

Channel

,

InterruptibleChannel

Base implementation class for interruptible channels.

This class encapsulates the low-level machinery required to implement
the asynchronous closing and interruption of channels. A concrete channel
class must invoke the

begin

and

end

methods
before and after, respectively, invoking an I/O operation that might block
indefinitely. In order to ensure that the

end

method is always
invoked, these methods should be used within a

try

...

finally

block:

```java
boolean completed = false;
try {
begin();
completed = ...; // Perform blocking I/O operation
return ...; // Return result
} finally {
end(completed);
}
```

The

completed

argument to the

end

method tells
whether or not the I/O operation actually completed, that is, whether it had
any effect that would be visible to the invoker. In the case of an
operation that reads bytes, for example, this argument should be

true

if, and only if, some bytes were actually transferred into the
invoker's target buffer.

A concrete channel class must also implement the

implCloseChannel

method in such a way that if it is
invoked while another thread is blocked in a native I/O operation upon the
channel then that operation will immediately return, either by throwing an
exception or by returning normally. If a thread is interrupted or the
channel upon which it is blocked is asynchronously closed then the channel's

end

method will throw the appropriate exception.

This class performs the synchronization required to implement the

Channel

specification. Implementations of the

implCloseChannel

method need not synchronize against
other threads that might be attempting to close the channel.

This class encapsulates the low-level machinery required to implement
the asynchronous closing and interruption of channels. A concrete channel
class must invoke the

begin

and

end

methods
before and after, respectively, invoking an I/O operation that might block
indefinitely. In order to ensure that the

end

method is always
invoked, these methods should be used within a

try

...

finally

block:

```java
boolean completed = false;
try {
begin();
completed = ...; // Perform blocking I/O operation
return ...; // Return result
} finally {
end(completed);
}
```

The

completed

argument to the

end

method tells
whether or not the I/O operation actually completed, that is, whether it had
any effect that would be visible to the invoker. In the case of an
operation that reads bytes, for example, this argument should be

true

if, and only if, some bytes were actually transferred into the
invoker's target buffer.

A concrete channel class must also implement the

implCloseChannel

method in such a way that if it is
invoked while another thread is blocked in a native I/O operation upon the
channel then that operation will immediately return, either by throwing an
exception or by returning normally. If a thread is interrupted or the
channel upon which it is blocked is asynchronously closed then the channel's

end

method will throw the appropriate exception.

This class performs the synchronization required to implement the

Channel

specification. Implementations of the

implCloseChannel

method need not synchronize against
other threads that might be attempting to close the channel.

boolean completed = false;
try {
begin();
completed = ...; // Perform blocking I/O operation
return ...; // Return result
} finally {
end(completed);
}

The

completed

argument to the

end

method tells
whether or not the I/O operation actually completed, that is, whether it had
any effect that would be visible to the invoker. In the case of an
operation that reads bytes, for example, this argument should be

true

if, and only if, some bytes were actually transferred into the
invoker's target buffer.

A concrete channel class must also implement the

implCloseChannel

method in such a way that if it is
invoked while another thread is blocked in a native I/O operation upon the
channel then that operation will immediately return, either by throwing an
exception or by returning normally. If a thread is interrupted or the
channel upon which it is blocked is asynchronously closed then the channel's

end

method will throw the appropriate exception.

This class performs the synchronization required to implement the

Channel

specification. Implementations of the

implCloseChannel

method need not synchronize against
other threads that might be attempting to close the channel.

A concrete channel class must also implement the

implCloseChannel

method in such a way that if it is
invoked while another thread is blocked in a native I/O operation upon the
channel then that operation will immediately return, either by throwing an
exception or by returning normally. If a thread is interrupted or the
channel upon which it is blocked is asynchronously closed then the channel's

end

method will throw the appropriate exception.

This class performs the synchronization required to implement the

Channel

specification. Implementations of the

implCloseChannel

method need not synchronize against
other threads that might be attempting to close the channel.

This class performs the synchronization required to implement the

Channel

specification. Implementations of the

implCloseChannel

method need not synchronize against
other threads that might be attempting to close the channel.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

AbstractInterruptibleChannel

()

Initializes a new instance of this class.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

protected void

begin

()

Marks the beginning of an I/O operation that might block indefinitely.

void

close

()

Closes this channel.

protected void

end

​(boolean completed)

Marks the end of an I/O operation that might block indefinitely.

protected abstract void

implCloseChannel

()

Closes this channel.

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

- Methods declared in interface java.nio.channels.

Channel

isOpen

Constructor Summary

Constructors

Modifier

Constructor

Description

protected

AbstractInterruptibleChannel

()

Initializes a new instance of this class.

---

#### Constructor Summary

Initializes a new instance of this class.

Method Summary

All Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

protected void

begin

()

Marks the beginning of an I/O operation that might block indefinitely.

void

close

()

Closes this channel.

protected void

end

​(boolean completed)

Marks the end of an I/O operation that might block indefinitely.

protected abstract void

implCloseChannel

()

Closes this channel.

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

- Methods declared in interface java.nio.channels.

Channel

isOpen

---

#### Method Summary

Marks the beginning of an I/O operation that might block indefinitely.

Closes this channel.

Marks the end of an I/O operation that might block indefinitely.

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

Methods declared in interface java.nio.channels.

Channel

isOpen

---

#### Methods declared in interface java.nio.channels. Channel

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- AbstractInterruptibleChannel

```java
protected AbstractInterruptibleChannel()
```

Initializes a new instance of this class.

============ METHOD DETAIL ==========

- Method Detail

- close

```java
public final void close()
throws
IOException
```

Closes this channel.

If the channel has already been closed then this method returns
immediately. Otherwise it marks the channel as closed and then invokes
the

implCloseChannel

method in order to
complete the close operation.

**Specified by:** close

in interface

AutoCloseable
**Specified by:** close

in interface

Channel
**Specified by:** close

in interface

Closeable
**Specified by:** close

in interface

InterruptibleChannel
**Throws:** IOException

- If an I/O error occurs

- implCloseChannel

```java
protected abstract void implCloseChannel()
throws
IOException
```

Closes this channel.

This method is invoked by the

close

method in order
to perform the actual work of closing the channel. This method is only
invoked if the channel has not yet been closed, and it is never invoked
more than once.

An implementation of this method must arrange for any other thread
that is blocked in an I/O operation upon this channel to return
immediately, either by throwing an exception or by returning normally.

**Throws:** IOException

- If an I/O error occurs while closing the channel

- begin

```java
protected final void begin()
```

Marks the beginning of an I/O operation that might block indefinitely.

This method should be invoked in tandem with the

end

method, using a

try

...

finally

block as
shown

above

, in order to implement asynchronous
closing and interruption for this channel.

- end

```java
protected final void end​(boolean completed)
throws
AsynchronousCloseException
```

Marks the end of an I/O operation that might block indefinitely.

This method should be invoked in tandem with the

begin

method, using a

try

...

finally

block
as shown

above

, in order to implement asynchronous
closing and interruption for this channel.

**Parameters:** completed

-

true

if, and only if, the I/O operation completed
successfully, that is, had some effect that would be visible to
the operation's invoker
**Throws:** AsynchronousCloseException

- If the channel was asynchronously closed
**Throws:** ClosedByInterruptException

- If the thread blocked in the I/O operation was interrupted

Constructor Detail

- AbstractInterruptibleChannel

```java
protected AbstractInterruptibleChannel()
```

Initializes a new instance of this class.

---

#### Constructor Detail

AbstractInterruptibleChannel

```java
protected AbstractInterruptibleChannel()
```

Initializes a new instance of this class.

---

#### AbstractInterruptibleChannel

protected AbstractInterruptibleChannel()

Initializes a new instance of this class.

Method Detail

- close

```java
public final void close()
throws
IOException
```

Closes this channel.

If the channel has already been closed then this method returns
immediately. Otherwise it marks the channel as closed and then invokes
the

implCloseChannel

method in order to
complete the close operation.

**Specified by:** close

in interface

AutoCloseable
**Specified by:** close

in interface

Channel
**Specified by:** close

in interface

Closeable
**Specified by:** close

in interface

InterruptibleChannel
**Throws:** IOException

- If an I/O error occurs

- implCloseChannel

```java
protected abstract void implCloseChannel()
throws
IOException
```

Closes this channel.

This method is invoked by the

close

method in order
to perform the actual work of closing the channel. This method is only
invoked if the channel has not yet been closed, and it is never invoked
more than once.

An implementation of this method must arrange for any other thread
that is blocked in an I/O operation upon this channel to return
immediately, either by throwing an exception or by returning normally.

**Throws:** IOException

- If an I/O error occurs while closing the channel

- begin

```java
protected final void begin()
```

Marks the beginning of an I/O operation that might block indefinitely.

This method should be invoked in tandem with the

end

method, using a

try

...

finally

block as
shown

above

, in order to implement asynchronous
closing and interruption for this channel.

- end

```java
protected final void end​(boolean completed)
throws
AsynchronousCloseException
```

Marks the end of an I/O operation that might block indefinitely.

This method should be invoked in tandem with the

begin

method, using a

try

...

finally

block
as shown

above

, in order to implement asynchronous
closing and interruption for this channel.

**Parameters:** completed

-

true

if, and only if, the I/O operation completed
successfully, that is, had some effect that would be visible to
the operation's invoker
**Throws:** AsynchronousCloseException

- If the channel was asynchronously closed
**Throws:** ClosedByInterruptException

- If the thread blocked in the I/O operation was interrupted

---

#### Method Detail

close

```java
public final void close()
throws
IOException
```

Closes this channel.

If the channel has already been closed then this method returns
immediately. Otherwise it marks the channel as closed and then invokes
the

implCloseChannel

method in order to
complete the close operation.

**Specified by:** close

in interface

AutoCloseable
**Specified by:** close

in interface

Channel
**Specified by:** close

in interface

Closeable
**Specified by:** close

in interface

InterruptibleChannel
**Throws:** IOException

- If an I/O error occurs

---

#### close

public final void close()
throws

IOException

Closes this channel.

If the channel has already been closed then this method returns
immediately. Otherwise it marks the channel as closed and then invokes
the

implCloseChannel

method in order to
complete the close operation.

If the channel has already been closed then this method returns
immediately. Otherwise it marks the channel as closed and then invokes
the

implCloseChannel

method in order to
complete the close operation.

implCloseChannel

```java
protected abstract void implCloseChannel()
throws
IOException
```

Closes this channel.

This method is invoked by the

close

method in order
to perform the actual work of closing the channel. This method is only
invoked if the channel has not yet been closed, and it is never invoked
more than once.

An implementation of this method must arrange for any other thread
that is blocked in an I/O operation upon this channel to return
immediately, either by throwing an exception or by returning normally.

**Throws:** IOException

- If an I/O error occurs while closing the channel

---

#### implCloseChannel

protected abstract void implCloseChannel()
throws

IOException

Closes this channel.

This method is invoked by the

close

method in order
to perform the actual work of closing the channel. This method is only
invoked if the channel has not yet been closed, and it is never invoked
more than once.

An implementation of this method must arrange for any other thread
that is blocked in an I/O operation upon this channel to return
immediately, either by throwing an exception or by returning normally.

This method is invoked by the

close

method in order
to perform the actual work of closing the channel. This method is only
invoked if the channel has not yet been closed, and it is never invoked
more than once.

An implementation of this method must arrange for any other thread
that is blocked in an I/O operation upon this channel to return
immediately, either by throwing an exception or by returning normally.

An implementation of this method must arrange for any other thread
that is blocked in an I/O operation upon this channel to return
immediately, either by throwing an exception or by returning normally.

begin

```java
protected final void begin()
```

Marks the beginning of an I/O operation that might block indefinitely.

This method should be invoked in tandem with the

end

method, using a

try

...

finally

block as
shown

above

, in order to implement asynchronous
closing and interruption for this channel.

---

#### begin

protected final void begin()

Marks the beginning of an I/O operation that might block indefinitely.

This method should be invoked in tandem with the

end

method, using a

try

...

finally

block as
shown

above

, in order to implement asynchronous
closing and interruption for this channel.

This method should be invoked in tandem with the

end

method, using a

try

...

finally

block as
shown

above

, in order to implement asynchronous
closing and interruption for this channel.

end

```java
protected final void end​(boolean completed)
throws
AsynchronousCloseException
```

Marks the end of an I/O operation that might block indefinitely.

This method should be invoked in tandem with the

begin

method, using a

try

...

finally

block
as shown

above

, in order to implement asynchronous
closing and interruption for this channel.

**Parameters:** completed

-

true

if, and only if, the I/O operation completed
successfully, that is, had some effect that would be visible to
the operation's invoker
**Throws:** AsynchronousCloseException

- If the channel was asynchronously closed
**Throws:** ClosedByInterruptException

- If the thread blocked in the I/O operation was interrupted

---

#### end

protected final void end​(boolean completed)
throws

AsynchronousCloseException

Marks the end of an I/O operation that might block indefinitely.

This method should be invoked in tandem with the

begin

method, using a

try

...

finally

block
as shown

above

, in order to implement asynchronous
closing and interruption for this channel.

This method should be invoked in tandem with the

begin

method, using a

try

...

finally

block
as shown

above

, in order to implement asynchronous
closing and interruption for this channel.

---

