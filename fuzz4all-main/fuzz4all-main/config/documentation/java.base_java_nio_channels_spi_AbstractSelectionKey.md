# Class AbstractSelectionKey

**Source:** `java.base\java\nio\channels\spi\AbstractSelectionKey.html`

### Class Description

```java
public abstract class
AbstractSelectionKey

extends
SelectionKey
```

Base implementation class for selection keys.

This class tracks the validity of the key and implements cancellation.

**Since:** 1.4

---

### Field Details

*No entries found.*

### Constructor Details

#### protected AbstractSelectionKey()

Initializes a new instance of this class.

---

### Method Details

#### public final void cancel()

Cancels this key.

If this key has not yet been cancelled then it is added to its
selector's cancelled-key set while synchronized on that set.

**Specified by:**
- cancel

in class

SelectionKey

---

### Additional Sections

#### Class AbstractSelectionKey

java.lang.Object

- java.nio.channels.SelectionKey
- - java.nio.channels.spi.AbstractSelectionKey

java.nio.channels.SelectionKey

- java.nio.channels.spi.AbstractSelectionKey

java.nio.channels.spi.AbstractSelectionKey

```java
public abstract class
AbstractSelectionKey

extends
SelectionKey
```

Base implementation class for selection keys.

This class tracks the validity of the key and implements cancellation.

**Since:** 1.4

public abstract class

AbstractSelectionKey

extends

SelectionKey

Base implementation class for selection keys.

This class tracks the validity of the key and implements cancellation.

This class tracks the validity of the key and implements cancellation.

=========== FIELD SUMMARY ===========

- Field Summary

- Fields declared in class java.nio.channels.

SelectionKey

OP_ACCEPT

,

OP_CONNECT

,

OP_READ

,

OP_WRITE

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

AbstractSelectionKey

()

Initializes a new instance of this class.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

cancel

()

Cancels this key.

- Methods declared in class java.nio.channels.

SelectionKey

attach

,

attachment

,

channel

,

interestOps

,

interestOps

,

interestOpsAnd

,

interestOpsOr

,

isAcceptable

,

isConnectable

,

isReadable

,

isValid

,

isWritable

,

readyOps

,

selector

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

Field Summary

- Fields declared in class java.nio.channels.

SelectionKey

OP_ACCEPT

,

OP_CONNECT

,

OP_READ

,

OP_WRITE

---

#### Field Summary

Fields declared in class java.nio.channels.

SelectionKey

OP_ACCEPT

,

OP_CONNECT

,

OP_READ

,

OP_WRITE

---

#### Fields declared in class java.nio.channels. SelectionKey

Constructor Summary

Constructors

Modifier

Constructor

Description

protected

AbstractSelectionKey

()

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

void

cancel

()

Cancels this key.

- Methods declared in class java.nio.channels.

SelectionKey

attach

,

attachment

,

channel

,

interestOps

,

interestOps

,

interestOpsAnd

,

interestOpsOr

,

isAcceptable

,

isConnectable

,

isReadable

,

isValid

,

isWritable

,

readyOps

,

selector

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

Cancels this key.

Methods declared in class java.nio.channels.

SelectionKey

attach

,

attachment

,

channel

,

interestOps

,

interestOps

,

interestOpsAnd

,

interestOpsOr

,

isAcceptable

,

isConnectable

,

isReadable

,

isValid

,

isWritable

,

readyOps

,

selector

---

#### Methods declared in class java.nio.channels. SelectionKey

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

- AbstractSelectionKey

```java
protected AbstractSelectionKey()
```

Initializes a new instance of this class.

============ METHOD DETAIL ==========

- Method Detail

- cancel

```java
public final void cancel()
```

Cancels this key.

If this key has not yet been cancelled then it is added to its
selector's cancelled-key set while synchronized on that set.

**Specified by:** cancel

in class

SelectionKey

Constructor Detail

- AbstractSelectionKey

```java
protected AbstractSelectionKey()
```

Initializes a new instance of this class.

---

#### Constructor Detail

AbstractSelectionKey

```java
protected AbstractSelectionKey()
```

Initializes a new instance of this class.

---

#### AbstractSelectionKey

protected AbstractSelectionKey()

Initializes a new instance of this class.

Method Detail

- cancel

```java
public final void cancel()
```

Cancels this key.

If this key has not yet been cancelled then it is added to its
selector's cancelled-key set while synchronized on that set.

**Specified by:** cancel

in class

SelectionKey

---

#### Method Detail

cancel

```java
public final void cancel()
```

Cancels this key.

If this key has not yet been cancelled then it is added to its
selector's cancelled-key set while synchronized on that set.

**Specified by:** cancel

in class

SelectionKey

---

#### cancel

public final void cancel()

Cancels this key.

If this key has not yet been cancelled then it is added to its
selector's cancelled-key set while synchronized on that set.

If this key has not yet been cancelled then it is added to its
selector's cancelled-key set while synchronized on that set.

---

