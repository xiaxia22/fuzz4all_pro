# Class Pipe

**Source:** `java.base\java\nio\channels\Pipe.html`

### Class Description

```java
public abstract class
Pipe

extends
Object
```

A pair of channels that implements a unidirectional pipe.

A pipe consists of a pair of channels: A writable

sink

channel and a readable

source

channel. Once some bytes are written to the sink channel they can be read
from the source channel in exactly the order in which they were written.

Whether or not a thread writing bytes to a pipe will block until another
thread reads those bytes, or some previously-written bytes, from the pipe is
system-dependent and therefore unspecified. Many pipe implementations will
buffer up to a certain number of bytes between the sink and source channels,
but such buffering should not be assumed.

**Since:** 1.4

---

### Field Details

*No entries found.*

### Constructor Details

#### protected Pipe()

Initializes a new instance of this class.

---

### Method Details

#### public abstract
Pipe.SourceChannel
source()

Returns this pipe's source channel.

**Returns:**
- This pipe's source channel

---

#### public abstract
Pipe.SinkChannel
sink()

Returns this pipe's sink channel.

**Returns:**
- This pipe's sink channel

---

#### public static
Pipe
open()
throws
IOException

Opens a pipe.

The new pipe is created by invoking the

openPipe

method of the
system-wide default

SelectorProvider

object.

**Returns:**
- A new pipe

**Throws:**
- IOException

- If an I/O error occurs

---

### Additional Sections

#### Class Pipe

java.lang.Object

- java.nio.channels.Pipe

java.nio.channels.Pipe

```java
public abstract class
Pipe

extends
Object
```

A pair of channels that implements a unidirectional pipe.

A pipe consists of a pair of channels: A writable

sink

channel and a readable

source

channel. Once some bytes are written to the sink channel they can be read
from the source channel in exactly the order in which they were written.

Whether or not a thread writing bytes to a pipe will block until another
thread reads those bytes, or some previously-written bytes, from the pipe is
system-dependent and therefore unspecified. Many pipe implementations will
buffer up to a certain number of bytes between the sink and source channels,
but such buffering should not be assumed.

**Since:** 1.4

public abstract class

Pipe

extends

Object

A pair of channels that implements a unidirectional pipe.

A pipe consists of a pair of channels: A writable

sink

channel and a readable

source

channel. Once some bytes are written to the sink channel they can be read
from the source channel in exactly the order in which they were written.

Whether or not a thread writing bytes to a pipe will block until another
thread reads those bytes, or some previously-written bytes, from the pipe is
system-dependent and therefore unspecified. Many pipe implementations will
buffer up to a certain number of bytes between the sink and source channels,
but such buffering should not be assumed.

A pipe consists of a pair of channels: A writable

sink

channel and a readable

source

channel. Once some bytes are written to the sink channel they can be read
from the source channel in exactly the order in which they were written.

Whether or not a thread writing bytes to a pipe will block until another
thread reads those bytes, or some previously-written bytes, from the pipe is
system-dependent and therefore unspecified. Many pipe implementations will
buffer up to a certain number of bytes between the sink and source channels,
but such buffering should not be assumed.

Whether or not a thread writing bytes to a pipe will block until another
thread reads those bytes, or some previously-written bytes, from the pipe is
system-dependent and therefore unspecified. Many pipe implementations will
buffer up to a certain number of bytes between the sink and source channels,
but such buffering should not be assumed.

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

static class

Pipe.SinkChannel

A channel representing the writable end of a

Pipe

.

static class

Pipe.SourceChannel

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

Pipe

()

Initializes a new instance of this class.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

static

Pipe

open

()

Opens a pipe.

abstract

Pipe.SinkChannel

sink

()

Returns this pipe's sink channel.

abstract

Pipe.SourceChannel

source

()

Returns this pipe's source channel.

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

Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

static class

Pipe.SinkChannel

A channel representing the writable end of a

Pipe

.

static class

Pipe.SourceChannel

A channel representing the readable end of a

Pipe

.

---

#### Nested Class Summary

A channel representing the writable end of a

Pipe

.

A channel representing the readable end of a

Pipe

.

Constructor Summary

Constructors

Modifier

Constructor

Description

protected

Pipe

()

Initializes a new instance of this class.

---

#### Constructor Summary

Initializes a new instance of this class.

Method Summary

All Methods

Static Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

static

Pipe

open

()

Opens a pipe.

abstract

Pipe.SinkChannel

sink

()

Returns this pipe's sink channel.

abstract

Pipe.SourceChannel

source

()

Returns this pipe's source channel.

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

Opens a pipe.

Returns this pipe's sink channel.

Returns this pipe's source channel.

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

- Pipe

```java
protected Pipe()
```

Initializes a new instance of this class.

============ METHOD DETAIL ==========

- Method Detail

- source

```java
public abstract
Pipe.SourceChannel
source()
```

Returns this pipe's source channel.

**Returns:** This pipe's source channel

- sink

```java
public abstract
Pipe.SinkChannel
sink()
```

Returns this pipe's sink channel.

**Returns:** This pipe's sink channel

- open

```java
public static
Pipe
open()
throws
IOException
```

Opens a pipe.

The new pipe is created by invoking the

openPipe

method of the
system-wide default

SelectorProvider

object.

**Returns:** A new pipe
**Throws:** IOException

- If an I/O error occurs

Constructor Detail

- Pipe

```java
protected Pipe()
```

Initializes a new instance of this class.

---

#### Constructor Detail

Pipe

```java
protected Pipe()
```

Initializes a new instance of this class.

---

#### Pipe

protected Pipe()

Initializes a new instance of this class.

Method Detail

- source

```java
public abstract
Pipe.SourceChannel
source()
```

Returns this pipe's source channel.

**Returns:** This pipe's source channel

- sink

```java
public abstract
Pipe.SinkChannel
sink()
```

Returns this pipe's sink channel.

**Returns:** This pipe's sink channel

- open

```java
public static
Pipe
open()
throws
IOException
```

Opens a pipe.

The new pipe is created by invoking the

openPipe

method of the
system-wide default

SelectorProvider

object.

**Returns:** A new pipe
**Throws:** IOException

- If an I/O error occurs

---

#### Method Detail

source

```java
public abstract
Pipe.SourceChannel
source()
```

Returns this pipe's source channel.

**Returns:** This pipe's source channel

---

#### source

public abstract

Pipe.SourceChannel

source()

Returns this pipe's source channel.

sink

```java
public abstract
Pipe.SinkChannel
sink()
```

Returns this pipe's sink channel.

**Returns:** This pipe's sink channel

---

#### sink

public abstract

Pipe.SinkChannel

sink()

Returns this pipe's sink channel.

open

```java
public static
Pipe
open()
throws
IOException
```

Opens a pipe.

The new pipe is created by invoking the

openPipe

method of the
system-wide default

SelectorProvider

object.

**Returns:** A new pipe
**Throws:** IOException

- If an I/O error occurs

---

#### open

public static

Pipe

open()
throws

IOException

Opens a pipe.

The new pipe is created by invoking the

openPipe

method of the
system-wide default

SelectorProvider

object.

The new pipe is created by invoking the

openPipe

method of the
system-wide default

SelectorProvider

object.

---

