# Class Pipe.SourceChannel

**Source:** `java.base\java\nio\channels\Pipe.SourceChannel.html`

### Class Description

```java
public abstract static class
Pipe.SourceChannel

extends
AbstractSelectableChannel

implements
ReadableByteChannel
,
ScatteringByteChannel
```

A channel representing the readable end of a

Pipe

.

**All Implemented Interfaces:** Closeable

,

AutoCloseable

,

Channel

,

InterruptibleChannel

,

ReadableByteChannel

,

ScatteringByteChannel

---

### Field Details

*No entries found.*

### Constructor Details

#### protected SourceChannel​(
SelectorProvider
provider)

Constructs a new instance of this class.

**Parameters:**
- provider

- The selector provider

---

### Method Details

#### public final int validOps()

Returns an operation set identifying this channel's supported
operations.

Pipe-source channels only support reading, so this method
returns

SelectionKey.OP_READ

.

**Specified by:**
- validOps

in class

SelectableChannel

**Returns:**
- The valid-operation set

---

### Additional Sections

#### Class Pipe.SourceChannel

java.lang.Object

- java.nio.channels.spi.AbstractInterruptibleChannel
- - java.nio.channels.SelectableChannel
- - java.nio.channels.spi.AbstractSelectableChannel
- - java.nio.channels.Pipe.SourceChannel

java.nio.channels.spi.AbstractInterruptibleChannel

- java.nio.channels.SelectableChannel
- - java.nio.channels.spi.AbstractSelectableChannel
- - java.nio.channels.Pipe.SourceChannel

java.nio.channels.SelectableChannel

- java.nio.channels.spi.AbstractSelectableChannel
- - java.nio.channels.Pipe.SourceChannel

java.nio.channels.spi.AbstractSelectableChannel

- java.nio.channels.Pipe.SourceChannel

java.nio.channels.Pipe.SourceChannel

**All Implemented Interfaces:** Closeable

,

AutoCloseable

,

Channel

,

InterruptibleChannel

,

ReadableByteChannel

,

ScatteringByteChannel

**Enclosing class:** Pipe

```java
public abstract static class
Pipe.SourceChannel

extends
AbstractSelectableChannel

implements
ReadableByteChannel
,
ScatteringByteChannel
```

A channel representing the readable end of a

Pipe

.

**Since:** 1.4

public abstract static class

Pipe.SourceChannel

extends

AbstractSelectableChannel

implements

ReadableByteChannel

,

ScatteringByteChannel

A channel representing the readable end of a

Pipe

.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

SourceChannel

​(

SelectorProvider

provider)

Constructs a new instance of this class.

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

ReadableByteChannel

read

- Methods declared in interface java.nio.channels.

ScatteringByteChannel

read

,

read

Constructor Summary

Constructors

Modifier

Constructor

Description

protected

SourceChannel

​(

SelectorProvider

provider)

Constructs a new instance of this class.

---

#### Constructor Summary

Constructs a new instance of this class.

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

ReadableByteChannel

read

- Methods declared in interface java.nio.channels.

ScatteringByteChannel

read

,

read

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

ReadableByteChannel

read

---

#### Methods declared in interface java.nio.channels. ReadableByteChannel

Methods declared in interface java.nio.channels.

ScatteringByteChannel

read

,

read

---

#### Methods declared in interface java.nio.channels. ScatteringByteChannel

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- SourceChannel

```java
protected SourceChannel​(
SelectorProvider
provider)
```

Constructs a new instance of this class.

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

Pipe-source channels only support reading, so this method
returns

SelectionKey.OP_READ

.

**Specified by:** validOps

in class

SelectableChannel
**Returns:** The valid-operation set

Constructor Detail

- SourceChannel

```java
protected SourceChannel​(
SelectorProvider
provider)
```

Constructs a new instance of this class.

**Parameters:** provider

- The selector provider

---

#### Constructor Detail

SourceChannel

```java
protected SourceChannel​(
SelectorProvider
provider)
```

Constructs a new instance of this class.

**Parameters:** provider

- The selector provider

---

#### SourceChannel

protected SourceChannel​(

SelectorProvider

provider)

Constructs a new instance of this class.

Method Detail

- validOps

```java
public final int validOps()
```

Returns an operation set identifying this channel's supported
operations.

Pipe-source channels only support reading, so this method
returns

SelectionKey.OP_READ

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

Pipe-source channels only support reading, so this method
returns

SelectionKey.OP_READ

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

Pipe-source channels only support reading, so this method
returns

SelectionKey.OP_READ

.

Pipe-source channels only support reading, so this method
returns

SelectionKey.OP_READ

.

---

