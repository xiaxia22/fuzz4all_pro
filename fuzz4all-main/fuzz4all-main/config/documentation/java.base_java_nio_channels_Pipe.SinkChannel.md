# Class Pipe.SinkChannel

**Source:** `java.base\java\nio\channels\Pipe.SinkChannel.html`

### Class Description

```java
public abstract static class
Pipe.SinkChannel

extends
AbstractSelectableChannel

implements
WritableByteChannel
,
GatheringByteChannel
```

A channel representing the writable end of a

Pipe

.

**All Implemented Interfaces:** Closeable

,

AutoCloseable

,

Channel

,

GatheringByteChannel

,

InterruptibleChannel

,

WritableByteChannel

---

### Field Details

*No entries found.*

### Constructor Details

#### protected SinkChannel​(
SelectorProvider
provider)

Initializes a new instance of this class.

**Parameters:**
- provider

- The selector provider

---

### Method Details

#### public final int validOps()

Returns an operation set identifying this channel's supported
operations.

Pipe-sink channels only support writing, so this method returns

SelectionKey.OP_WRITE

.

**Specified by:**
- validOps

in class

SelectableChannel

**Returns:**
- The valid-operation set

---

### Additional Sections

#### Class Pipe.SinkChannel

java.lang.Object

- java.nio.channels.spi.AbstractInterruptibleChannel
- - java.nio.channels.SelectableChannel
- - java.nio.channels.spi.AbstractSelectableChannel
- - java.nio.channels.Pipe.SinkChannel

java.nio.channels.spi.AbstractInterruptibleChannel

- java.nio.channels.SelectableChannel
- - java.nio.channels.spi.AbstractSelectableChannel
- - java.nio.channels.Pipe.SinkChannel

java.nio.channels.SelectableChannel

- java.nio.channels.spi.AbstractSelectableChannel
- - java.nio.channels.Pipe.SinkChannel

java.nio.channels.spi.AbstractSelectableChannel

- java.nio.channels.Pipe.SinkChannel

java.nio.channels.Pipe.SinkChannel

**All Implemented Interfaces:** Closeable

,

AutoCloseable

,

Channel

,

GatheringByteChannel

,

InterruptibleChannel

,

WritableByteChannel

**Enclosing class:** Pipe

```java
public abstract static class
Pipe.SinkChannel

extends
AbstractSelectableChannel

implements
WritableByteChannel
,
GatheringByteChannel
```

A channel representing the writable end of a

Pipe

.

**Since:** 1.4

public abstract static class

Pipe.SinkChannel

extends

AbstractSelectableChannel

implements

WritableByteChannel

,

GatheringByteChannel

A channel representing the writable end of a

Pipe

.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

SinkChannel

​(

SelectorProvider

provider)

Initializes a new instance of this class.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

int

validOps

()

Returns an operation set identifying this channel's supported
operations.

- Methods declared in class java.nio.channels.spi.

AbstractSelectableChannel

configureBlocking

,

implCloseChannel

,

implCloseSelectableChannel

,

implConfigureBlocking

,

provider

,

register

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

- Methods declared in interface java.nio.channels.

GatheringByteChannel

write

,

write

- Methods declared in interface java.nio.channels.

WritableByteChannel

write

Constructor Summary

Constructors

Modifier

Constructor

Description

protected

SinkChannel

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

Concrete Methods

Modifier and Type

Method

Description

int

validOps

()

Returns an operation set identifying this channel's supported
operations.

- Methods declared in class java.nio.channels.spi.

AbstractSelectableChannel

configureBlocking

,

implCloseChannel

,

implCloseSelectableChannel

,

implConfigureBlocking

,

provider

,

register

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

- Methods declared in interface java.nio.channels.

GatheringByteChannel

write

,

write

- Methods declared in interface java.nio.channels.

WritableByteChannel

write

---

#### Method Summary

Returns an operation set identifying this channel's supported
operations.

Methods declared in class java.nio.channels.spi.

AbstractSelectableChannel

configureBlocking

,

implCloseChannel

,

implCloseSelectableChannel

,

implConfigureBlocking

,

provider

,

register

---

#### Methods declared in class java.nio.channels.spi. AbstractSelectableChannel

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

Methods declared in interface java.nio.channels.

GatheringByteChannel

write

,

write

---

#### Methods declared in interface java.nio.channels. GatheringByteChannel

Methods declared in interface java.nio.channels.

WritableByteChannel

write

---

#### Methods declared in interface java.nio.channels. WritableByteChannel

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- SinkChannel

```java
protected SinkChannel​(
SelectorProvider
provider)
```

Initializes a new instance of this class.

**Parameters:** provider

- The selector provider

============ METHOD DETAIL ==========

- Method Detail

- validOps

```java
public final int validOps()
```

Returns an operation set identifying this channel's supported
operations.

Pipe-sink channels only support writing, so this method returns

SelectionKey.OP_WRITE

.

**Specified by:** validOps

in class

SelectableChannel
**Returns:** The valid-operation set

Constructor Detail

- SinkChannel

```java
protected SinkChannel​(
SelectorProvider
provider)
```

Initializes a new instance of this class.

**Parameters:** provider

- The selector provider

---

#### Constructor Detail

SinkChannel

```java
protected SinkChannel​(
SelectorProvider
provider)
```

Initializes a new instance of this class.

**Parameters:** provider

- The selector provider

---

#### SinkChannel

protected SinkChannel​(

SelectorProvider

provider)

Initializes a new instance of this class.

Method Detail

- validOps

```java
public final int validOps()
```

Returns an operation set identifying this channel's supported
operations.

Pipe-sink channels only support writing, so this method returns

SelectionKey.OP_WRITE

.

**Specified by:** validOps

in class

SelectableChannel
**Returns:** The valid-operation set

---

#### Method Detail

validOps

```java
public final int validOps()
```

Returns an operation set identifying this channel's supported
operations.

Pipe-sink channels only support writing, so this method returns

SelectionKey.OP_WRITE

.

**Specified by:** validOps

in class

SelectableChannel
**Returns:** The valid-operation set

---

#### validOps

public final int validOps()

Returns an operation set identifying this channel's supported
operations.

Pipe-sink channels only support writing, so this method returns

SelectionKey.OP_WRITE

.

Pipe-sink channels only support writing, so this method returns

SelectionKey.OP_WRITE

.

---

