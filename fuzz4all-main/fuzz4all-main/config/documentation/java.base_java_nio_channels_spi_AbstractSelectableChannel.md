# Class AbstractSelectableChannel

**Source:** `java.base\java\nio\channels\spi\AbstractSelectableChannel.html`

### Class Description

```java
public abstract class
AbstractSelectableChannel

extends
SelectableChannel
```

Base implementation class for selectable channels.

This class defines methods that handle the mechanics of channel
registration, deregistration, and closing. It maintains the current
blocking mode of this channel as well as its current set of selection keys.
It performs all of the synchronization required to implement the

SelectableChannel

specification. Implementations of the
abstract protected methods defined in this class need not synchronize
against other threads that might be engaged in the same operations.

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

#### protected AbstractSelectableChannel​(
SelectorProvider
provider)

Initializes a new instance of this class.

**Parameters:**
- provider

- The provider that created this channel

---

### Method Details

#### public final
SelectorProvider
provider()

Returns the provider that created this channel.

**Specified by:**
- provider

in class

SelectableChannel

**Returns:**
- The provider that created this channel

---

#### public final
SelectionKey
register​(
Selector
sel,
int ops,

Object
att)
throws
ClosedChannelException

Registers this channel with the given selector, returning a selection key.

This method first verifies that this channel is open and that the
given initial interest set is valid.

If this channel is already registered with the given selector then
the selection key representing that registration is returned after
setting its interest set to the given value.

Otherwise this channel has not yet been registered with the given
selector, so the

register

method of
the selector is invoked while holding the appropriate locks. The
resulting key is added to this channel's key set before being returned.

**Specified by:**
- register

in class

SelectableChannel

**Parameters:**
- sel

- The selector with which this channel is to be registered
- ops

- The interest set for the resulting key
- att

- The attachment for the resulting key; may be

null

**Returns:**
- A key representing the registration of this channel with
the given selector

**Throws:**
- ClosedSelectorException

- If the selector is closed
- IllegalBlockingModeException

- If this channel is in blocking mode
- IllegalSelectorException

- If this channel was not created by the same provider
as the given selector
- CancelledKeyException

- If this channel is currently registered with the given selector
but the corresponding key has already been cancelled
- IllegalArgumentException

- If a bit in the

ops

set does not correspond to an
operation that is supported by this channel, that is, if

set & ~validOps() != 0
- ClosedChannelException

- If this channel is closed

---

#### protected final void implCloseChannel()
throws
IOException

Closes this channel.

This method, which is specified in the

AbstractInterruptibleChannel

class and is invoked by the

close

method, in turn invokes the

implCloseSelectableChannel

method in
order to perform the actual work of closing this channel. It then
cancels all of this channel's keys.

**Specified by:**
- implCloseChannel

in class

AbstractInterruptibleChannel

**Throws:**
- IOException

- If an I/O error occurs while closing the channel

---

#### protected abstract void implCloseSelectableChannel()
throws
IOException

Closes this selectable channel.

This method is invoked by the

close

method in order to perform the actual work of closing the
channel. This method is only invoked if the channel has not yet been
closed, and it is never invoked more than once.

An implementation of this method must arrange for any other thread
that is blocked in an I/O operation upon this channel to return
immediately, either by throwing an exception or by returning normally.

**Throws:**
- IOException

- If an I/O error occurs

---

#### public final
SelectableChannel
configureBlocking​(boolean block)
throws
IOException

Adjusts this channel's blocking mode.

If the given blocking mode is different from the current blocking
mode then this method invokes the

implConfigureBlocking

method, while holding the appropriate locks, in
order to change the mode.

**Specified by:**
- configureBlocking

in class

SelectableChannel

**Parameters:**
- block

- If

true

then this channel will be placed in
blocking mode; if

false

then it will be placed
non-blocking mode

**Returns:**
- This selectable channel

**Throws:**
- ClosedChannelException

- If this channel is closed
- IOException

- If an I/O error occurs

---

#### protected abstract void implConfigureBlocking​(boolean block)
throws
IOException

Adjusts this channel's blocking mode.

This method is invoked by the

configureBlocking

method in order to perform the actual work of
changing the blocking mode. This method is only invoked if the new mode
is different from the current mode.

**Parameters:**
- block

- If

true

then this channel will be placed in
blocking mode; if

false

then it will be placed
non-blocking mode

**Throws:**
- IOException

- If an I/O error occurs

---

### Additional Sections

#### Class AbstractSelectableChannel

java.lang.Object

- java.nio.channels.spi.AbstractInterruptibleChannel
- - java.nio.channels.SelectableChannel
- - java.nio.channels.spi.AbstractSelectableChannel

java.nio.channels.spi.AbstractInterruptibleChannel

- java.nio.channels.SelectableChannel
- - java.nio.channels.spi.AbstractSelectableChannel

java.nio.channels.SelectableChannel

- java.nio.channels.spi.AbstractSelectableChannel

java.nio.channels.spi.AbstractSelectableChannel

**All Implemented Interfaces:** Closeable

,

AutoCloseable

,

Channel

,

InterruptibleChannel

**Direct Known Subclasses:** DatagramChannel

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

ServerSocketChannel

,

SocketChannel

```java
public abstract class
AbstractSelectableChannel

extends
SelectableChannel
```

Base implementation class for selectable channels.

This class defines methods that handle the mechanics of channel
registration, deregistration, and closing. It maintains the current
blocking mode of this channel as well as its current set of selection keys.
It performs all of the synchronization required to implement the

SelectableChannel

specification. Implementations of the
abstract protected methods defined in this class need not synchronize
against other threads that might be engaged in the same operations.

**Since:** 1.4

public abstract class

AbstractSelectableChannel

extends

SelectableChannel

Base implementation class for selectable channels.

This class defines methods that handle the mechanics of channel
registration, deregistration, and closing. It maintains the current
blocking mode of this channel as well as its current set of selection keys.
It performs all of the synchronization required to implement the

SelectableChannel

specification. Implementations of the
abstract protected methods defined in this class need not synchronize
against other threads that might be engaged in the same operations.

This class defines methods that handle the mechanics of channel
registration, deregistration, and closing. It maintains the current
blocking mode of this channel as well as its current set of selection keys.
It performs all of the synchronization required to implement the

SelectableChannel

specification. Implementations of the
abstract protected methods defined in this class need not synchronize
against other threads that might be engaged in the same operations.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

AbstractSelectableChannel

​(

SelectorProvider

provider)

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

SelectableChannel

configureBlocking

​(boolean block)

Adjusts this channel's blocking mode.

protected void

implCloseChannel

()

Closes this channel.

protected abstract void

implCloseSelectableChannel

()

Closes this selectable channel.

protected abstract void

implConfigureBlocking

​(boolean block)

Adjusts this channel's blocking mode.

SelectorProvider

provider

()

Returns the provider that created this channel.

SelectionKey

register

​(

Selector

sel,
int ops,

Object

att)

Registers this channel with the given selector, returning a selection key.

- Methods declared in class java.nio.channels.

SelectableChannel

blockingLock

,

isBlocking

,

isRegistered

,

keyFor

,

register

,

validOps

- Methods declared in class java.nio.channels.spi.

AbstractInterruptibleChannel

begin

,

close

,

end

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

AbstractSelectableChannel

​(

SelectorProvider

provider)

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

SelectableChannel

configureBlocking

​(boolean block)

Adjusts this channel's blocking mode.

protected void

implCloseChannel

()

Closes this channel.

protected abstract void

implCloseSelectableChannel

()

Closes this selectable channel.

protected abstract void

implConfigureBlocking

​(boolean block)

Adjusts this channel's blocking mode.

SelectorProvider

provider

()

Returns the provider that created this channel.

SelectionKey

register

​(

Selector

sel,
int ops,

Object

att)

Registers this channel with the given selector, returning a selection key.

- Methods declared in class java.nio.channels.

SelectableChannel

blockingLock

,

isBlocking

,

isRegistered

,

keyFor

,

register

,

validOps

- Methods declared in class java.nio.channels.spi.

AbstractInterruptibleChannel

begin

,

close

,

end

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

Adjusts this channel's blocking mode.

Closes this channel.

Closes this selectable channel.

Returns the provider that created this channel.

Registers this channel with the given selector, returning a selection key.

Methods declared in class java.nio.channels.

SelectableChannel

blockingLock

,

isBlocking

,

isRegistered

,

keyFor

,

register

,

validOps

---

#### Methods declared in class java.nio.channels. SelectableChannel

Methods declared in class java.nio.channels.spi.

AbstractInterruptibleChannel

begin

,

close

,

end

---

#### Methods declared in class java.nio.channels.spi. AbstractInterruptibleChannel

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

- AbstractSelectableChannel

```java
protected AbstractSelectableChannel​(
SelectorProvider
provider)
```

Initializes a new instance of this class.

**Parameters:** provider

- The provider that created this channel

============ METHOD DETAIL ==========

- Method Detail

- provider

```java
public final
SelectorProvider
provider()
```

Returns the provider that created this channel.

**Specified by:** provider

in class

SelectableChannel
**Returns:** The provider that created this channel

- register

```java
public final
SelectionKey
register​(
Selector
sel,
int ops,

Object
att)
throws
ClosedChannelException
```

Registers this channel with the given selector, returning a selection key.

This method first verifies that this channel is open and that the
given initial interest set is valid.

If this channel is already registered with the given selector then
the selection key representing that registration is returned after
setting its interest set to the given value.

Otherwise this channel has not yet been registered with the given
selector, so the

register

method of
the selector is invoked while holding the appropriate locks. The
resulting key is added to this channel's key set before being returned.

**Specified by:** register

in class

SelectableChannel
**Parameters:** sel

- The selector with which this channel is to be registered
**Parameters:** ops

- The interest set for the resulting key
**Parameters:** att

- The attachment for the resulting key; may be

null
**Returns:** A key representing the registration of this channel with
the given selector
**Throws:** ClosedSelectorException

- If the selector is closed
**Throws:** IllegalBlockingModeException

- If this channel is in blocking mode
**Throws:** IllegalSelectorException

- If this channel was not created by the same provider
as the given selector
**Throws:** CancelledKeyException

- If this channel is currently registered with the given selector
but the corresponding key has already been cancelled
**Throws:** IllegalArgumentException

- If a bit in the

ops

set does not correspond to an
operation that is supported by this channel, that is, if

set & ~validOps() != 0
**Throws:** ClosedChannelException

- If this channel is closed

- implCloseChannel

```java
protected final void implCloseChannel()
throws
IOException
```

Closes this channel.

This method, which is specified in the

AbstractInterruptibleChannel

class and is invoked by the

close

method, in turn invokes the

implCloseSelectableChannel

method in
order to perform the actual work of closing this channel. It then
cancels all of this channel's keys.

**Specified by:** implCloseChannel

in class

AbstractInterruptibleChannel
**Throws:** IOException

- If an I/O error occurs while closing the channel

- implCloseSelectableChannel

```java
protected abstract void implCloseSelectableChannel()
throws
IOException
```

Closes this selectable channel.

This method is invoked by the

close

method in order to perform the actual work of closing the
channel. This method is only invoked if the channel has not yet been
closed, and it is never invoked more than once.

An implementation of this method must arrange for any other thread
that is blocked in an I/O operation upon this channel to return
immediately, either by throwing an exception or by returning normally.

**Throws:** IOException

- If an I/O error occurs

- configureBlocking

```java
public final
SelectableChannel
configureBlocking​(boolean block)
throws
IOException
```

Adjusts this channel's blocking mode.

If the given blocking mode is different from the current blocking
mode then this method invokes the

implConfigureBlocking

method, while holding the appropriate locks, in
order to change the mode.

**Specified by:** configureBlocking

in class

SelectableChannel
**Parameters:** block

- If

true

then this channel will be placed in
blocking mode; if

false

then it will be placed
non-blocking mode
**Returns:** This selectable channel
**Throws:** ClosedChannelException

- If this channel is closed
**Throws:** IOException

- If an I/O error occurs

- implConfigureBlocking

```java
protected abstract void implConfigureBlocking​(boolean block)
throws
IOException
```

Adjusts this channel's blocking mode.

This method is invoked by the

configureBlocking

method in order to perform the actual work of
changing the blocking mode. This method is only invoked if the new mode
is different from the current mode.

**Parameters:** block

- If

true

then this channel will be placed in
blocking mode; if

false

then it will be placed
non-blocking mode
**Throws:** IOException

- If an I/O error occurs

Constructor Detail

- AbstractSelectableChannel

```java
protected AbstractSelectableChannel​(
SelectorProvider
provider)
```

Initializes a new instance of this class.

**Parameters:** provider

- The provider that created this channel

---

#### Constructor Detail

AbstractSelectableChannel

```java
protected AbstractSelectableChannel​(
SelectorProvider
provider)
```

Initializes a new instance of this class.

**Parameters:** provider

- The provider that created this channel

---

#### AbstractSelectableChannel

protected AbstractSelectableChannel​(

SelectorProvider

provider)

Initializes a new instance of this class.

Method Detail

- provider

```java
public final
SelectorProvider
provider()
```

Returns the provider that created this channel.

**Specified by:** provider

in class

SelectableChannel
**Returns:** The provider that created this channel

- register

```java
public final
SelectionKey
register​(
Selector
sel,
int ops,

Object
att)
throws
ClosedChannelException
```

Registers this channel with the given selector, returning a selection key.

This method first verifies that this channel is open and that the
given initial interest set is valid.

If this channel is already registered with the given selector then
the selection key representing that registration is returned after
setting its interest set to the given value.

Otherwise this channel has not yet been registered with the given
selector, so the

register

method of
the selector is invoked while holding the appropriate locks. The
resulting key is added to this channel's key set before being returned.

**Specified by:** register

in class

SelectableChannel
**Parameters:** sel

- The selector with which this channel is to be registered
**Parameters:** ops

- The interest set for the resulting key
**Parameters:** att

- The attachment for the resulting key; may be

null
**Returns:** A key representing the registration of this channel with
the given selector
**Throws:** ClosedSelectorException

- If the selector is closed
**Throws:** IllegalBlockingModeException

- If this channel is in blocking mode
**Throws:** IllegalSelectorException

- If this channel was not created by the same provider
as the given selector
**Throws:** CancelledKeyException

- If this channel is currently registered with the given selector
but the corresponding key has already been cancelled
**Throws:** IllegalArgumentException

- If a bit in the

ops

set does not correspond to an
operation that is supported by this channel, that is, if

set & ~validOps() != 0
**Throws:** ClosedChannelException

- If this channel is closed

- implCloseChannel

```java
protected final void implCloseChannel()
throws
IOException
```

Closes this channel.

This method, which is specified in the

AbstractInterruptibleChannel

class and is invoked by the

close

method, in turn invokes the

implCloseSelectableChannel

method in
order to perform the actual work of closing this channel. It then
cancels all of this channel's keys.

**Specified by:** implCloseChannel

in class

AbstractInterruptibleChannel
**Throws:** IOException

- If an I/O error occurs while closing the channel

- implCloseSelectableChannel

```java
protected abstract void implCloseSelectableChannel()
throws
IOException
```

Closes this selectable channel.

This method is invoked by the

close

method in order to perform the actual work of closing the
channel. This method is only invoked if the channel has not yet been
closed, and it is never invoked more than once.

An implementation of this method must arrange for any other thread
that is blocked in an I/O operation upon this channel to return
immediately, either by throwing an exception or by returning normally.

**Throws:** IOException

- If an I/O error occurs

- configureBlocking

```java
public final
SelectableChannel
configureBlocking​(boolean block)
throws
IOException
```

Adjusts this channel's blocking mode.

If the given blocking mode is different from the current blocking
mode then this method invokes the

implConfigureBlocking

method, while holding the appropriate locks, in
order to change the mode.

**Specified by:** configureBlocking

in class

SelectableChannel
**Parameters:** block

- If

true

then this channel will be placed in
blocking mode; if

false

then it will be placed
non-blocking mode
**Returns:** This selectable channel
**Throws:** ClosedChannelException

- If this channel is closed
**Throws:** IOException

- If an I/O error occurs

- implConfigureBlocking

```java
protected abstract void implConfigureBlocking​(boolean block)
throws
IOException
```

Adjusts this channel's blocking mode.

This method is invoked by the

configureBlocking

method in order to perform the actual work of
changing the blocking mode. This method is only invoked if the new mode
is different from the current mode.

**Parameters:** block

- If

true

then this channel will be placed in
blocking mode; if

false

then it will be placed
non-blocking mode
**Throws:** IOException

- If an I/O error occurs

---

#### Method Detail

provider

```java
public final
SelectorProvider
provider()
```

Returns the provider that created this channel.

**Specified by:** provider

in class

SelectableChannel
**Returns:** The provider that created this channel

---

#### provider

public final

SelectorProvider

provider()

Returns the provider that created this channel.

register

```java
public final
SelectionKey
register​(
Selector
sel,
int ops,

Object
att)
throws
ClosedChannelException
```

Registers this channel with the given selector, returning a selection key.

This method first verifies that this channel is open and that the
given initial interest set is valid.

If this channel is already registered with the given selector then
the selection key representing that registration is returned after
setting its interest set to the given value.

Otherwise this channel has not yet been registered with the given
selector, so the

register

method of
the selector is invoked while holding the appropriate locks. The
resulting key is added to this channel's key set before being returned.

**Specified by:** register

in class

SelectableChannel
**Parameters:** sel

- The selector with which this channel is to be registered
**Parameters:** ops

- The interest set for the resulting key
**Parameters:** att

- The attachment for the resulting key; may be

null
**Returns:** A key representing the registration of this channel with
the given selector
**Throws:** ClosedSelectorException

- If the selector is closed
**Throws:** IllegalBlockingModeException

- If this channel is in blocking mode
**Throws:** IllegalSelectorException

- If this channel was not created by the same provider
as the given selector
**Throws:** CancelledKeyException

- If this channel is currently registered with the given selector
but the corresponding key has already been cancelled
**Throws:** IllegalArgumentException

- If a bit in the

ops

set does not correspond to an
operation that is supported by this channel, that is, if

set & ~validOps() != 0
**Throws:** ClosedChannelException

- If this channel is closed

---

#### register

public final

SelectionKey

register​(

Selector

sel,
int ops,

Object

att)
throws

ClosedChannelException

Registers this channel with the given selector, returning a selection key.

This method first verifies that this channel is open and that the
given initial interest set is valid.

If this channel is already registered with the given selector then
the selection key representing that registration is returned after
setting its interest set to the given value.

Otherwise this channel has not yet been registered with the given
selector, so the

register

method of
the selector is invoked while holding the appropriate locks. The
resulting key is added to this channel's key set before being returned.

This method first verifies that this channel is open and that the
given initial interest set is valid.

If this channel is already registered with the given selector then
the selection key representing that registration is returned after
setting its interest set to the given value.

Otherwise this channel has not yet been registered with the given
selector, so the

register

method of
the selector is invoked while holding the appropriate locks. The
resulting key is added to this channel's key set before being returned.

If this channel is already registered with the given selector then
the selection key representing that registration is returned after
setting its interest set to the given value.

Otherwise this channel has not yet been registered with the given
selector, so the

register

method of
the selector is invoked while holding the appropriate locks. The
resulting key is added to this channel's key set before being returned.

Otherwise this channel has not yet been registered with the given
selector, so the

register

method of
the selector is invoked while holding the appropriate locks. The
resulting key is added to this channel's key set before being returned.

implCloseChannel

```java
protected final void implCloseChannel()
throws
IOException
```

Closes this channel.

This method, which is specified in the

AbstractInterruptibleChannel

class and is invoked by the

close

method, in turn invokes the

implCloseSelectableChannel

method in
order to perform the actual work of closing this channel. It then
cancels all of this channel's keys.

**Specified by:** implCloseChannel

in class

AbstractInterruptibleChannel
**Throws:** IOException

- If an I/O error occurs while closing the channel

---

#### implCloseChannel

protected final void implCloseChannel()
throws

IOException

Closes this channel.

This method, which is specified in the

AbstractInterruptibleChannel

class and is invoked by the

close

method, in turn invokes the

implCloseSelectableChannel

method in
order to perform the actual work of closing this channel. It then
cancels all of this channel's keys.

This method, which is specified in the

AbstractInterruptibleChannel

class and is invoked by the

close

method, in turn invokes the

implCloseSelectableChannel

method in
order to perform the actual work of closing this channel. It then
cancels all of this channel's keys.

implCloseSelectableChannel

```java
protected abstract void implCloseSelectableChannel()
throws
IOException
```

Closes this selectable channel.

This method is invoked by the

close

method in order to perform the actual work of closing the
channel. This method is only invoked if the channel has not yet been
closed, and it is never invoked more than once.

An implementation of this method must arrange for any other thread
that is blocked in an I/O operation upon this channel to return
immediately, either by throwing an exception or by returning normally.

**Throws:** IOException

- If an I/O error occurs

---

#### implCloseSelectableChannel

protected abstract void implCloseSelectableChannel()
throws

IOException

Closes this selectable channel.

This method is invoked by the

close

method in order to perform the actual work of closing the
channel. This method is only invoked if the channel has not yet been
closed, and it is never invoked more than once.

An implementation of this method must arrange for any other thread
that is blocked in an I/O operation upon this channel to return
immediately, either by throwing an exception or by returning normally.

This method is invoked by the

close

method in order to perform the actual work of closing the
channel. This method is only invoked if the channel has not yet been
closed, and it is never invoked more than once.

An implementation of this method must arrange for any other thread
that is blocked in an I/O operation upon this channel to return
immediately, either by throwing an exception or by returning normally.

An implementation of this method must arrange for any other thread
that is blocked in an I/O operation upon this channel to return
immediately, either by throwing an exception or by returning normally.

configureBlocking

```java
public final
SelectableChannel
configureBlocking​(boolean block)
throws
IOException
```

Adjusts this channel's blocking mode.

If the given blocking mode is different from the current blocking
mode then this method invokes the

implConfigureBlocking

method, while holding the appropriate locks, in
order to change the mode.

**Specified by:** configureBlocking

in class

SelectableChannel
**Parameters:** block

- If

true

then this channel will be placed in
blocking mode; if

false

then it will be placed
non-blocking mode
**Returns:** This selectable channel
**Throws:** ClosedChannelException

- If this channel is closed
**Throws:** IOException

- If an I/O error occurs

---

#### configureBlocking

public final

SelectableChannel

configureBlocking​(boolean block)
throws

IOException

Adjusts this channel's blocking mode.

If the given blocking mode is different from the current blocking
mode then this method invokes the

implConfigureBlocking

method, while holding the appropriate locks, in
order to change the mode.

If the given blocking mode is different from the current blocking
mode then this method invokes the

implConfigureBlocking

method, while holding the appropriate locks, in
order to change the mode.

implConfigureBlocking

```java
protected abstract void implConfigureBlocking​(boolean block)
throws
IOException
```

Adjusts this channel's blocking mode.

This method is invoked by the

configureBlocking

method in order to perform the actual work of
changing the blocking mode. This method is only invoked if the new mode
is different from the current mode.

**Parameters:** block

- If

true

then this channel will be placed in
blocking mode; if

false

then it will be placed
non-blocking mode
**Throws:** IOException

- If an I/O error occurs

---

#### implConfigureBlocking

protected abstract void implConfigureBlocking​(boolean block)
throws

IOException

Adjusts this channel's blocking mode.

This method is invoked by the

configureBlocking

method in order to perform the actual work of
changing the blocking mode. This method is only invoked if the new mode
is different from the current mode.

This method is invoked by the

configureBlocking

method in order to perform the actual work of
changing the blocking mode. This method is only invoked if the new mode
is different from the current mode.

---

