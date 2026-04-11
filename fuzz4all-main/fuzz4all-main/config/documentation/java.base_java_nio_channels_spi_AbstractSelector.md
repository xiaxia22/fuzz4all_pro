# Class AbstractSelector

**Source:** `java.base\java\nio\channels\spi\AbstractSelector.html`

### Class Description

```java
public abstract class
AbstractSelector

extends
Selector
```

Base implementation class for selectors.

This class encapsulates the low-level machinery required to implement
the interruption of selection operations. A concrete selector class must
invoke the

begin

and

end

methods before and
after, respectively, invoking an I/O operation that might block
indefinitely. In order to ensure that the

end

method is always
invoked, these methods should be used within a

try

...

finally

block:

```java
try {
begin();
// Perform blocking I/O operation here
...
} finally {
end();
}
```

This class also defines methods for maintaining a selector's
cancelled-key set and for removing a key from its channel's key set, and
declares the abstract

register

method that is invoked by a
selectable channel's

register

method in order to perform the actual work of registering a channel.

**All Implemented Interfaces:** Closeable

,

AutoCloseable

---

### Field Details

*No entries found.*

### Constructor Details

#### protected AbstractSelector​(
SelectorProvider
provider)

Initializes a new instance of this class.

**Parameters:**
- provider

- The provider that created this selector

---

### Method Details

#### public final void close()
throws
IOException

Closes this selector.

If the selector has already been closed then this method returns
immediately. Otherwise it marks the selector as closed and then invokes
the

implCloseSelector

method in order to
complete the close operation.

**Specified by:**
- close

in interface

AutoCloseable
- close

in interface

Closeable
- close

in class

Selector

**Throws:**
- IOException

- If an I/O error occurs

---

#### protected abstract void implCloseSelector()
throws
IOException

Closes this selector.

This method is invoked by the

close

method in order
to perform the actual work of closing the selector. This method is only
invoked if the selector has not yet been closed, and it is never invoked
more than once.

An implementation of this method must arrange for any other thread
that is blocked in a selection operation upon this selector to return
immediately as if by invoking the

wakeup

method.

**Throws:**
- IOException

- If an I/O error occurs while closing the selector

---

#### public final
SelectorProvider
provider()

Returns the provider that created this channel.

**Specified by:**
- provider

in class

Selector

**Returns:**
- The provider that created this channel

---

#### protected final
Set
<
SelectionKey
> cancelledKeys()

Retrieves this selector's cancelled-key set.

This set should only be used while synchronized upon it.

**Returns:**
- The cancelled-key set

---

#### protected abstract
SelectionKey
register​(
AbstractSelectableChannel
ch,
int ops,

Object
att)

Registers the given channel with this selector.

This method is invoked by a channel's

register

method in order to perform
the actual work of registering the channel with this selector.

**Parameters:**
- ch

- The channel to be registered
- ops

- The initial interest set, which must be valid
- att

- The initial attachment for the resulting key

**Returns:**
- A new key representing the registration of the given channel
with this selector

---

#### protected final void deregister​(
AbstractSelectionKey
key)

Removes the given key from its channel's key set.

This method must be invoked by the selector for each channel that it
deregisters.

**Parameters:**
- key

- The selection key to be removed

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

, in order to implement interruption for
this selector.

Invoking this method arranges for the selector's

wakeup

method to be invoked if a thread's

interrupt

method is invoked while the thread is
blocked in an I/O operation upon the selector.

---

#### protected final void end()

Marks the end of an I/O operation that might block indefinitely.

This method should be invoked in tandem with the

begin

method, using a

try

...

finally

block as
shown

above

, in order to implement interruption for
this selector.

---

### Additional Sections

#### Class AbstractSelector

java.lang.Object

- java.nio.channels.Selector
- - java.nio.channels.spi.AbstractSelector

java.nio.channels.Selector

- java.nio.channels.spi.AbstractSelector

java.nio.channels.spi.AbstractSelector

**All Implemented Interfaces:** Closeable

,

AutoCloseable

```java
public abstract class
AbstractSelector

extends
Selector
```

Base implementation class for selectors.

This class encapsulates the low-level machinery required to implement
the interruption of selection operations. A concrete selector class must
invoke the

begin

and

end

methods before and
after, respectively, invoking an I/O operation that might block
indefinitely. In order to ensure that the

end

method is always
invoked, these methods should be used within a

try

...

finally

block:

```java
try {
begin();
// Perform blocking I/O operation here
...
} finally {
end();
}
```

This class also defines methods for maintaining a selector's
cancelled-key set and for removing a key from its channel's key set, and
declares the abstract

register

method that is invoked by a
selectable channel's

register

method in order to perform the actual work of registering a channel.

**Since:** 1.4

public abstract class

AbstractSelector

extends

Selector

Base implementation class for selectors.

This class encapsulates the low-level machinery required to implement
the interruption of selection operations. A concrete selector class must
invoke the

begin

and

end

methods before and
after, respectively, invoking an I/O operation that might block
indefinitely. In order to ensure that the

end

method is always
invoked, these methods should be used within a

try

...

finally

block:

```java
try {
begin();
// Perform blocking I/O operation here
...
} finally {
end();
}
```

This class also defines methods for maintaining a selector's
cancelled-key set and for removing a key from its channel's key set, and
declares the abstract

register

method that is invoked by a
selectable channel's

register

method in order to perform the actual work of registering a channel.

This class encapsulates the low-level machinery required to implement
the interruption of selection operations. A concrete selector class must
invoke the

begin

and

end

methods before and
after, respectively, invoking an I/O operation that might block
indefinitely. In order to ensure that the

end

method is always
invoked, these methods should be used within a

try

...

finally

block:

```java
try {
begin();
// Perform blocking I/O operation here
...
} finally {
end();
}
```

This class also defines methods for maintaining a selector's
cancelled-key set and for removing a key from its channel's key set, and
declares the abstract

register

method that is invoked by a
selectable channel's

register

method in order to perform the actual work of registering a channel.

try {
begin();
// Perform blocking I/O operation here
...
} finally {
end();
}

This class also defines methods for maintaining a selector's
cancelled-key set and for removing a key from its channel's key set, and
declares the abstract

register

method that is invoked by a
selectable channel's

register

method in order to perform the actual work of registering a channel.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

AbstractSelector

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

protected void

begin

()

Marks the beginning of an I/O operation that might block indefinitely.

protected

Set

<

SelectionKey

>

cancelledKeys

()

Retrieves this selector's cancelled-key set.

void

close

()

Closes this selector.

protected void

deregister

​(

AbstractSelectionKey

key)

Removes the given key from its channel's key set.

protected void

end

()

Marks the end of an I/O operation that might block indefinitely.

protected abstract void

implCloseSelector

()

Closes this selector.

SelectorProvider

provider

()

Returns the provider that created this channel.

protected abstract

SelectionKey

register

​(

AbstractSelectableChannel

ch,
int ops,

Object

att)

Registers the given channel with this selector.

- Methods declared in class java.nio.channels.

Selector

isOpen

,

keys

,

open

,

select

,

select

,

select

,

select

,

selectedKeys

,

selectNow

,

selectNow

,

wakeup

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

Modifier

Constructor

Description

protected

AbstractSelector

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

protected void

begin

()

Marks the beginning of an I/O operation that might block indefinitely.

protected

Set

<

SelectionKey

>

cancelledKeys

()

Retrieves this selector's cancelled-key set.

void

close

()

Closes this selector.

protected void

deregister

​(

AbstractSelectionKey

key)

Removes the given key from its channel's key set.

protected void

end

()

Marks the end of an I/O operation that might block indefinitely.

protected abstract void

implCloseSelector

()

Closes this selector.

SelectorProvider

provider

()

Returns the provider that created this channel.

protected abstract

SelectionKey

register

​(

AbstractSelectableChannel

ch,
int ops,

Object

att)

Registers the given channel with this selector.

- Methods declared in class java.nio.channels.

Selector

isOpen

,

keys

,

open

,

select

,

select

,

select

,

select

,

selectedKeys

,

selectNow

,

selectNow

,

wakeup

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

Marks the beginning of an I/O operation that might block indefinitely.

Retrieves this selector's cancelled-key set.

Closes this selector.

Removes the given key from its channel's key set.

Marks the end of an I/O operation that might block indefinitely.

Returns the provider that created this channel.

Registers the given channel with this selector.

Methods declared in class java.nio.channels.

Selector

isOpen

,

keys

,

open

,

select

,

select

,

select

,

select

,

selectedKeys

,

selectNow

,

selectNow

,

wakeup

---

#### Methods declared in class java.nio.channels. Selector

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

- AbstractSelector

```java
protected AbstractSelector​(
SelectorProvider
provider)
```

Initializes a new instance of this class.

**Parameters:** provider

- The provider that created this selector

============ METHOD DETAIL ==========

- Method Detail

- close

```java
public final void close()
throws
IOException
```

Closes this selector.

If the selector has already been closed then this method returns
immediately. Otherwise it marks the selector as closed and then invokes
the

implCloseSelector

method in order to
complete the close operation.

**Specified by:** close

in interface

AutoCloseable
**Specified by:** close

in interface

Closeable
**Specified by:** close

in class

Selector
**Throws:** IOException

- If an I/O error occurs

- implCloseSelector

```java
protected abstract void implCloseSelector()
throws
IOException
```

Closes this selector.

This method is invoked by the

close

method in order
to perform the actual work of closing the selector. This method is only
invoked if the selector has not yet been closed, and it is never invoked
more than once.

An implementation of this method must arrange for any other thread
that is blocked in a selection operation upon this selector to return
immediately as if by invoking the

wakeup

method.

**Throws:** IOException

- If an I/O error occurs while closing the selector

- provider

```java
public final
SelectorProvider
provider()
```

Returns the provider that created this channel.

**Specified by:** provider

in class

Selector
**Returns:** The provider that created this channel

- cancelledKeys

```java
protected final
Set
<
SelectionKey
> cancelledKeys()
```

Retrieves this selector's cancelled-key set.

This set should only be used while synchronized upon it.

**Returns:** The cancelled-key set

- register

```java
protected abstract
SelectionKey
register​(
AbstractSelectableChannel
ch,
int ops,

Object
att)
```

Registers the given channel with this selector.

This method is invoked by a channel's

register

method in order to perform
the actual work of registering the channel with this selector.

**Parameters:** ch

- The channel to be registered
**Parameters:** ops

- The initial interest set, which must be valid
**Parameters:** att

- The initial attachment for the resulting key
**Returns:** A new key representing the registration of the given channel
with this selector

- deregister

```java
protected final void deregister​(
AbstractSelectionKey
key)
```

Removes the given key from its channel's key set.

This method must be invoked by the selector for each channel that it
deregisters.

**Parameters:** key

- The selection key to be removed

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

, in order to implement interruption for
this selector.

Invoking this method arranges for the selector's

wakeup

method to be invoked if a thread's

interrupt

method is invoked while the thread is
blocked in an I/O operation upon the selector.

- end

```java
protected final void end()
```

Marks the end of an I/O operation that might block indefinitely.

This method should be invoked in tandem with the

begin

method, using a

try

...

finally

block as
shown

above

, in order to implement interruption for
this selector.

Constructor Detail

- AbstractSelector

```java
protected AbstractSelector​(
SelectorProvider
provider)
```

Initializes a new instance of this class.

**Parameters:** provider

- The provider that created this selector

---

#### Constructor Detail

AbstractSelector

```java
protected AbstractSelector​(
SelectorProvider
provider)
```

Initializes a new instance of this class.

**Parameters:** provider

- The provider that created this selector

---

#### AbstractSelector

protected AbstractSelector​(

SelectorProvider

provider)

Initializes a new instance of this class.

Method Detail

- close

```java
public final void close()
throws
IOException
```

Closes this selector.

If the selector has already been closed then this method returns
immediately. Otherwise it marks the selector as closed and then invokes
the

implCloseSelector

method in order to
complete the close operation.

**Specified by:** close

in interface

AutoCloseable
**Specified by:** close

in interface

Closeable
**Specified by:** close

in class

Selector
**Throws:** IOException

- If an I/O error occurs

- implCloseSelector

```java
protected abstract void implCloseSelector()
throws
IOException
```

Closes this selector.

This method is invoked by the

close

method in order
to perform the actual work of closing the selector. This method is only
invoked if the selector has not yet been closed, and it is never invoked
more than once.

An implementation of this method must arrange for any other thread
that is blocked in a selection operation upon this selector to return
immediately as if by invoking the

wakeup

method.

**Throws:** IOException

- If an I/O error occurs while closing the selector

- provider

```java
public final
SelectorProvider
provider()
```

Returns the provider that created this channel.

**Specified by:** provider

in class

Selector
**Returns:** The provider that created this channel

- cancelledKeys

```java
protected final
Set
<
SelectionKey
> cancelledKeys()
```

Retrieves this selector's cancelled-key set.

This set should only be used while synchronized upon it.

**Returns:** The cancelled-key set

- register

```java
protected abstract
SelectionKey
register​(
AbstractSelectableChannel
ch,
int ops,

Object
att)
```

Registers the given channel with this selector.

This method is invoked by a channel's

register

method in order to perform
the actual work of registering the channel with this selector.

**Parameters:** ch

- The channel to be registered
**Parameters:** ops

- The initial interest set, which must be valid
**Parameters:** att

- The initial attachment for the resulting key
**Returns:** A new key representing the registration of the given channel
with this selector

- deregister

```java
protected final void deregister​(
AbstractSelectionKey
key)
```

Removes the given key from its channel's key set.

This method must be invoked by the selector for each channel that it
deregisters.

**Parameters:** key

- The selection key to be removed

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

, in order to implement interruption for
this selector.

Invoking this method arranges for the selector's

wakeup

method to be invoked if a thread's

interrupt

method is invoked while the thread is
blocked in an I/O operation upon the selector.

- end

```java
protected final void end()
```

Marks the end of an I/O operation that might block indefinitely.

This method should be invoked in tandem with the

begin

method, using a

try

...

finally

block as
shown

above

, in order to implement interruption for
this selector.

---

#### Method Detail

close

```java
public final void close()
throws
IOException
```

Closes this selector.

If the selector has already been closed then this method returns
immediately. Otherwise it marks the selector as closed and then invokes
the

implCloseSelector

method in order to
complete the close operation.

**Specified by:** close

in interface

AutoCloseable
**Specified by:** close

in interface

Closeable
**Specified by:** close

in class

Selector
**Throws:** IOException

- If an I/O error occurs

---

#### close

public final void close()
throws

IOException

Closes this selector.

If the selector has already been closed then this method returns
immediately. Otherwise it marks the selector as closed and then invokes
the

implCloseSelector

method in order to
complete the close operation.

If the selector has already been closed then this method returns
immediately. Otherwise it marks the selector as closed and then invokes
the

implCloseSelector

method in order to
complete the close operation.

implCloseSelector

```java
protected abstract void implCloseSelector()
throws
IOException
```

Closes this selector.

This method is invoked by the

close

method in order
to perform the actual work of closing the selector. This method is only
invoked if the selector has not yet been closed, and it is never invoked
more than once.

An implementation of this method must arrange for any other thread
that is blocked in a selection operation upon this selector to return
immediately as if by invoking the

wakeup

method.

**Throws:** IOException

- If an I/O error occurs while closing the selector

---

#### implCloseSelector

protected abstract void implCloseSelector()
throws

IOException

Closes this selector.

This method is invoked by the

close

method in order
to perform the actual work of closing the selector. This method is only
invoked if the selector has not yet been closed, and it is never invoked
more than once.

An implementation of this method must arrange for any other thread
that is blocked in a selection operation upon this selector to return
immediately as if by invoking the

wakeup

method.

This method is invoked by the

close

method in order
to perform the actual work of closing the selector. This method is only
invoked if the selector has not yet been closed, and it is never invoked
more than once.

An implementation of this method must arrange for any other thread
that is blocked in a selection operation upon this selector to return
immediately as if by invoking the

wakeup

method.

An implementation of this method must arrange for any other thread
that is blocked in a selection operation upon this selector to return
immediately as if by invoking the

wakeup

method.

provider

```java
public final
SelectorProvider
provider()
```

Returns the provider that created this channel.

**Specified by:** provider

in class

Selector
**Returns:** The provider that created this channel

---

#### provider

public final

SelectorProvider

provider()

Returns the provider that created this channel.

cancelledKeys

```java
protected final
Set
<
SelectionKey
> cancelledKeys()
```

Retrieves this selector's cancelled-key set.

This set should only be used while synchronized upon it.

**Returns:** The cancelled-key set

---

#### cancelledKeys

protected final

Set

<

SelectionKey

> cancelledKeys()

Retrieves this selector's cancelled-key set.

This set should only be used while synchronized upon it.

This set should only be used while synchronized upon it.

register

```java
protected abstract
SelectionKey
register​(
AbstractSelectableChannel
ch,
int ops,

Object
att)
```

Registers the given channel with this selector.

This method is invoked by a channel's

register

method in order to perform
the actual work of registering the channel with this selector.

**Parameters:** ch

- The channel to be registered
**Parameters:** ops

- The initial interest set, which must be valid
**Parameters:** att

- The initial attachment for the resulting key
**Returns:** A new key representing the registration of the given channel
with this selector

---

#### register

protected abstract

SelectionKey

register​(

AbstractSelectableChannel

ch,
int ops,

Object

att)

Registers the given channel with this selector.

This method is invoked by a channel's

register

method in order to perform
the actual work of registering the channel with this selector.

This method is invoked by a channel's

register

method in order to perform
the actual work of registering the channel with this selector.

deregister

```java
protected final void deregister​(
AbstractSelectionKey
key)
```

Removes the given key from its channel's key set.

This method must be invoked by the selector for each channel that it
deregisters.

**Parameters:** key

- The selection key to be removed

---

#### deregister

protected final void deregister​(

AbstractSelectionKey

key)

Removes the given key from its channel's key set.

This method must be invoked by the selector for each channel that it
deregisters.

This method must be invoked by the selector for each channel that it
deregisters.

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

, in order to implement interruption for
this selector.

Invoking this method arranges for the selector's

wakeup

method to be invoked if a thread's

interrupt

method is invoked while the thread is
blocked in an I/O operation upon the selector.

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

, in order to implement interruption for
this selector.

Invoking this method arranges for the selector's

wakeup

method to be invoked if a thread's

interrupt

method is invoked while the thread is
blocked in an I/O operation upon the selector.

This method should be invoked in tandem with the

end

method, using a

try

...

finally

block as
shown

above

, in order to implement interruption for
this selector.

Invoking this method arranges for the selector's

wakeup

method to be invoked if a thread's

interrupt

method is invoked while the thread is
blocked in an I/O operation upon the selector.

Invoking this method arranges for the selector's

wakeup

method to be invoked if a thread's

interrupt

method is invoked while the thread is
blocked in an I/O operation upon the selector.

end

```java
protected final void end()
```

Marks the end of an I/O operation that might block indefinitely.

This method should be invoked in tandem with the

begin

method, using a

try

...

finally

block as
shown

above

, in order to implement interruption for
this selector.

---

#### end

protected final void end()

Marks the end of an I/O operation that might block indefinitely.

This method should be invoked in tandem with the

begin

method, using a

try

...

finally

block as
shown

above

, in order to implement interruption for
this selector.

This method should be invoked in tandem with the

begin

method, using a

try

...

finally

block as
shown

above

, in order to implement interruption for
this selector.

---

