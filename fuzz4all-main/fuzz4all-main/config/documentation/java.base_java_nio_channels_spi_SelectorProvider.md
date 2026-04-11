# Class SelectorProvider

**Source:** `java.base\java\nio\channels\spi\SelectorProvider.html`

### Class Description

```java
public abstract class
SelectorProvider

extends
Object
```

Service-provider class for selectors and selectable channels.

A selector provider is a concrete subclass of this class that has a
zero-argument constructor and implements the abstract methods specified
below. A given invocation of the Java virtual machine maintains a single
system-wide default provider instance, which is returned by the

provider

method. The first invocation of that method will locate
the default provider as specified below.

The system-wide default provider is used by the static

open

methods of the

DatagramChannel

,

Pipe

,

Selector

,

ServerSocketChannel

, and

SocketChannel

classes. It is also
used by the

System.inheritedChannel()

method. A program may make use of a provider other than the default provider
by instantiating that provider and then directly invoking the

open

methods defined in this class.

All of the methods in this class are safe for use by multiple concurrent
threads.

**Since:** 1.4

---

### Field Details

*No entries found.*

### Constructor Details

#### protected SelectorProvider()

Initializes a new instance of this class.

**Throws:**
- SecurityException

- If a security manager has been installed and it denies

RuntimePermission

("selectorProvider")

---

### Method Details

#### public static
SelectorProvider
provider()

Returns the system-wide default selector provider for this invocation of
the Java virtual machine.

The first invocation of this method locates the default provider
object as follows:

- If the system property

java.nio.channels.spi.SelectorProvider

is defined then it is
taken to be the fully-qualified name of a concrete provider class.
The class is loaded and instantiated; if this process fails then an
unspecified error is thrown.
- If a provider class has been installed in a jar file that is
visible to the system class loader, and that jar file contains a
provider-configuration file named

java.nio.channels.spi.SelectorProvider

in the resource
directory

META-INF/services

, then the first class name
specified in that file is taken. The class is loaded and
instantiated; if this process fails then an unspecified error is
thrown.
- Finally, if no provider has been specified by any of the above
means then the system-default provider class is instantiated and the
result is returned.

Subsequent invocations of this method return the provider that was
returned by the first invocation.

**Returns:**
- The system-wide default selector provider

---

#### public abstract
DatagramChannel
openDatagramChannel()
throws
IOException

Opens a datagram channel.

**Returns:**
- The new channel

**Throws:**
- IOException

- If an I/O error occurs

---

#### public abstract
DatagramChannel
openDatagramChannel​(
ProtocolFamily
family)
throws
IOException

Opens a datagram channel.

**Parameters:**
- family

- The protocol family

**Returns:**
- A new datagram channel

**Throws:**
- UnsupportedOperationException

- If the specified protocol family is not supported
- IOException

- If an I/O error occurs

**Since:**
- 1.7

---

#### public abstract
Pipe
openPipe()
throws
IOException

Opens a pipe.

**Returns:**
- The new pipe

**Throws:**
- IOException

- If an I/O error occurs

---

#### public abstract
AbstractSelector
openSelector()
throws
IOException

Opens a selector.

**Returns:**
- The new selector

**Throws:**
- IOException

- If an I/O error occurs

---

#### public abstract
ServerSocketChannel
openServerSocketChannel()
throws
IOException

Opens a server-socket channel.

**Returns:**
- The new channel

**Throws:**
- IOException

- If an I/O error occurs

---

#### public abstract
SocketChannel
openSocketChannel()
throws
IOException

Opens a socket channel.

**Returns:**
- The new channel

**Throws:**
- IOException

- If an I/O error occurs

---

#### public
Channel
inheritedChannel()
throws
IOException

Returns the channel inherited from the entity that created this
Java virtual machine.

On many operating systems a process, such as a Java virtual
machine, can be started in a manner that allows the process to
inherit a channel from the entity that created the process. The
manner in which this is done is system dependent, as are the
possible entities to which the channel may be connected. For example,
on UNIX systems, the Internet services daemon (

inetd

) is used to
start programs to service requests when a request arrives on an
associated network port. In this example, the process that is started,
inherits a channel representing a network socket.

In cases where the inherited channel represents a network socket
then the

Channel

type returned
by this method is determined as follows:

- If the inherited channel represents a stream-oriented connected
socket then a

SocketChannel

is
returned. The socket channel is, at least initially, in blocking
mode, bound to a socket address, and connected to a peer.
- If the inherited channel represents a stream-oriented listening
socket then a

ServerSocketChannel

is returned. The server-socket channel is, at
least initially, in blocking mode, and bound to a socket address.
- If the inherited channel is a datagram-oriented socket
then a

DatagramChannel

is
returned. The datagram channel is, at least initially, in blocking
mode, and bound to a socket address.

In addition to the network-oriented channels described, this method
may return other kinds of channels in the future.

The first invocation of this method creates the channel that is
returned. Subsequent invocations of this method return the same
channel.

**Returns:**
- The inherited channel, if any, otherwise

null

.

**Throws:**
- IOException

- If an I/O error occurs
- SecurityException

- If a security manager has been installed and it denies

RuntimePermission

("inheritedChannel")

**Since:**
- 1.5

---

### Additional Sections

#### Class SelectorProvider

java.lang.Object

- java.nio.channels.spi.SelectorProvider

java.nio.channels.spi.SelectorProvider

```java
public abstract class
SelectorProvider

extends
Object
```

Service-provider class for selectors and selectable channels.

A selector provider is a concrete subclass of this class that has a
zero-argument constructor and implements the abstract methods specified
below. A given invocation of the Java virtual machine maintains a single
system-wide default provider instance, which is returned by the

provider

method. The first invocation of that method will locate
the default provider as specified below.

The system-wide default provider is used by the static

open

methods of the

DatagramChannel

,

Pipe

,

Selector

,

ServerSocketChannel

, and

SocketChannel

classes. It is also
used by the

System.inheritedChannel()

method. A program may make use of a provider other than the default provider
by instantiating that provider and then directly invoking the

open

methods defined in this class.

All of the methods in this class are safe for use by multiple concurrent
threads.

**Since:** 1.4

public abstract class

SelectorProvider

extends

Object

Service-provider class for selectors and selectable channels.

A selector provider is a concrete subclass of this class that has a
zero-argument constructor and implements the abstract methods specified
below. A given invocation of the Java virtual machine maintains a single
system-wide default provider instance, which is returned by the

provider

method. The first invocation of that method will locate
the default provider as specified below.

The system-wide default provider is used by the static

open

methods of the

DatagramChannel

,

Pipe

,

Selector

,

ServerSocketChannel

, and

SocketChannel

classes. It is also
used by the

System.inheritedChannel()

method. A program may make use of a provider other than the default provider
by instantiating that provider and then directly invoking the

open

methods defined in this class.

All of the methods in this class are safe for use by multiple concurrent
threads.

A selector provider is a concrete subclass of this class that has a
zero-argument constructor and implements the abstract methods specified
below. A given invocation of the Java virtual machine maintains a single
system-wide default provider instance, which is returned by the

provider

method. The first invocation of that method will locate
the default provider as specified below.

The system-wide default provider is used by the static

open

methods of the

DatagramChannel

,

Pipe

,

Selector

,

ServerSocketChannel

, and

SocketChannel

classes. It is also
used by the

System.inheritedChannel()

method. A program may make use of a provider other than the default provider
by instantiating that provider and then directly invoking the

open

methods defined in this class.

All of the methods in this class are safe for use by multiple concurrent
threads.

The system-wide default provider is used by the static

open

methods of the

DatagramChannel

,

Pipe

,

Selector

,

ServerSocketChannel

, and

SocketChannel

classes. It is also
used by the

System.inheritedChannel()

method. A program may make use of a provider other than the default provider
by instantiating that provider and then directly invoking the

open

methods defined in this class.

All of the methods in this class are safe for use by multiple concurrent
threads.

All of the methods in this class are safe for use by multiple concurrent
threads.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

SelectorProvider

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

Channel

inheritedChannel

()

Returns the channel inherited from the entity that created this
Java virtual machine.

abstract

DatagramChannel

openDatagramChannel

()

Opens a datagram channel.

abstract

DatagramChannel

openDatagramChannel

​(

ProtocolFamily

family)

Opens a datagram channel.

abstract

Pipe

openPipe

()

Opens a pipe.

abstract

AbstractSelector

openSelector

()

Opens a selector.

abstract

ServerSocketChannel

openServerSocketChannel

()

Opens a server-socket channel.

abstract

SocketChannel

openSocketChannel

()

Opens a socket channel.

static

SelectorProvider

provider

()

Returns the system-wide default selector provider for this invocation of
the Java virtual machine.

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

SelectorProvider

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

Channel

inheritedChannel

()

Returns the channel inherited from the entity that created this
Java virtual machine.

abstract

DatagramChannel

openDatagramChannel

()

Opens a datagram channel.

abstract

DatagramChannel

openDatagramChannel

​(

ProtocolFamily

family)

Opens a datagram channel.

abstract

Pipe

openPipe

()

Opens a pipe.

abstract

AbstractSelector

openSelector

()

Opens a selector.

abstract

ServerSocketChannel

openServerSocketChannel

()

Opens a server-socket channel.

abstract

SocketChannel

openSocketChannel

()

Opens a socket channel.

static

SelectorProvider

provider

()

Returns the system-wide default selector provider for this invocation of
the Java virtual machine.

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

Returns the channel inherited from the entity that created this
Java virtual machine.

Opens a datagram channel.

Opens a pipe.

Opens a selector.

Opens a server-socket channel.

Opens a socket channel.

Returns the system-wide default selector provider for this invocation of
the Java virtual machine.

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

- SelectorProvider

```java
protected SelectorProvider()
```

Initializes a new instance of this class.

**Throws:** SecurityException

- If a security manager has been installed and it denies

RuntimePermission

("selectorProvider")

============ METHOD DETAIL ==========

- Method Detail

- provider

```java
public static
SelectorProvider
provider()
```

Returns the system-wide default selector provider for this invocation of
the Java virtual machine.

The first invocation of this method locates the default provider
object as follows:

- If the system property

java.nio.channels.spi.SelectorProvider

is defined then it is
taken to be the fully-qualified name of a concrete provider class.
The class is loaded and instantiated; if this process fails then an
unspecified error is thrown.
- If a provider class has been installed in a jar file that is
visible to the system class loader, and that jar file contains a
provider-configuration file named

java.nio.channels.spi.SelectorProvider

in the resource
directory

META-INF/services

, then the first class name
specified in that file is taken. The class is loaded and
instantiated; if this process fails then an unspecified error is
thrown.
- Finally, if no provider has been specified by any of the above
means then the system-default provider class is instantiated and the
result is returned.

Subsequent invocations of this method return the provider that was
returned by the first invocation.

**Returns:** The system-wide default selector provider

- openDatagramChannel

```java
public abstract
DatagramChannel
openDatagramChannel()
throws
IOException
```

Opens a datagram channel.

**Returns:** The new channel
**Throws:** IOException

- If an I/O error occurs

- openDatagramChannel

```java
public abstract
DatagramChannel
openDatagramChannel​(
ProtocolFamily
family)
throws
IOException
```

Opens a datagram channel.

**Parameters:** family

- The protocol family
**Returns:** A new datagram channel
**Throws:** UnsupportedOperationException

- If the specified protocol family is not supported
**Throws:** IOException

- If an I/O error occurs
**Since:** 1.7

- openPipe

```java
public abstract
Pipe
openPipe()
throws
IOException
```

Opens a pipe.

**Returns:** The new pipe
**Throws:** IOException

- If an I/O error occurs

- openSelector

```java
public abstract
AbstractSelector
openSelector()
throws
IOException
```

Opens a selector.

**Returns:** The new selector
**Throws:** IOException

- If an I/O error occurs

- openServerSocketChannel

```java
public abstract
ServerSocketChannel
openServerSocketChannel()
throws
IOException
```

Opens a server-socket channel.

**Returns:** The new channel
**Throws:** IOException

- If an I/O error occurs

- openSocketChannel

```java
public abstract
SocketChannel
openSocketChannel()
throws
IOException
```

Opens a socket channel.

**Returns:** The new channel
**Throws:** IOException

- If an I/O error occurs

- inheritedChannel

```java
public
Channel
inheritedChannel()
throws
IOException
```

Returns the channel inherited from the entity that created this
Java virtual machine.

On many operating systems a process, such as a Java virtual
machine, can be started in a manner that allows the process to
inherit a channel from the entity that created the process. The
manner in which this is done is system dependent, as are the
possible entities to which the channel may be connected. For example,
on UNIX systems, the Internet services daemon (

inetd

) is used to
start programs to service requests when a request arrives on an
associated network port. In this example, the process that is started,
inherits a channel representing a network socket.

In cases where the inherited channel represents a network socket
then the

Channel

type returned
by this method is determined as follows:

- If the inherited channel represents a stream-oriented connected
socket then a

SocketChannel

is
returned. The socket channel is, at least initially, in blocking
mode, bound to a socket address, and connected to a peer.
- If the inherited channel represents a stream-oriented listening
socket then a

ServerSocketChannel

is returned. The server-socket channel is, at
least initially, in blocking mode, and bound to a socket address.
- If the inherited channel is a datagram-oriented socket
then a

DatagramChannel

is
returned. The datagram channel is, at least initially, in blocking
mode, and bound to a socket address.

In addition to the network-oriented channels described, this method
may return other kinds of channels in the future.

The first invocation of this method creates the channel that is
returned. Subsequent invocations of this method return the same
channel.

**Returns:** The inherited channel, if any, otherwise

null

.
**Throws:** IOException

- If an I/O error occurs
**Throws:** SecurityException

- If a security manager has been installed and it denies

RuntimePermission

("inheritedChannel")
**Since:** 1.5

Constructor Detail

- SelectorProvider

```java
protected SelectorProvider()
```

Initializes a new instance of this class.

**Throws:** SecurityException

- If a security manager has been installed and it denies

RuntimePermission

("selectorProvider")

---

#### Constructor Detail

SelectorProvider

```java
protected SelectorProvider()
```

Initializes a new instance of this class.

**Throws:** SecurityException

- If a security manager has been installed and it denies

RuntimePermission

("selectorProvider")

---

#### SelectorProvider

protected SelectorProvider()

Initializes a new instance of this class.

Method Detail

- provider

```java
public static
SelectorProvider
provider()
```

Returns the system-wide default selector provider for this invocation of
the Java virtual machine.

The first invocation of this method locates the default provider
object as follows:

- If the system property

java.nio.channels.spi.SelectorProvider

is defined then it is
taken to be the fully-qualified name of a concrete provider class.
The class is loaded and instantiated; if this process fails then an
unspecified error is thrown.
- If a provider class has been installed in a jar file that is
visible to the system class loader, and that jar file contains a
provider-configuration file named

java.nio.channels.spi.SelectorProvider

in the resource
directory

META-INF/services

, then the first class name
specified in that file is taken. The class is loaded and
instantiated; if this process fails then an unspecified error is
thrown.
- Finally, if no provider has been specified by any of the above
means then the system-default provider class is instantiated and the
result is returned.

Subsequent invocations of this method return the provider that was
returned by the first invocation.

**Returns:** The system-wide default selector provider

- openDatagramChannel

```java
public abstract
DatagramChannel
openDatagramChannel()
throws
IOException
```

Opens a datagram channel.

**Returns:** The new channel
**Throws:** IOException

- If an I/O error occurs

- openDatagramChannel

```java
public abstract
DatagramChannel
openDatagramChannel​(
ProtocolFamily
family)
throws
IOException
```

Opens a datagram channel.

**Parameters:** family

- The protocol family
**Returns:** A new datagram channel
**Throws:** UnsupportedOperationException

- If the specified protocol family is not supported
**Throws:** IOException

- If an I/O error occurs
**Since:** 1.7

- openPipe

```java
public abstract
Pipe
openPipe()
throws
IOException
```

Opens a pipe.

**Returns:** The new pipe
**Throws:** IOException

- If an I/O error occurs

- openSelector

```java
public abstract
AbstractSelector
openSelector()
throws
IOException
```

Opens a selector.

**Returns:** The new selector
**Throws:** IOException

- If an I/O error occurs

- openServerSocketChannel

```java
public abstract
ServerSocketChannel
openServerSocketChannel()
throws
IOException
```

Opens a server-socket channel.

**Returns:** The new channel
**Throws:** IOException

- If an I/O error occurs

- openSocketChannel

```java
public abstract
SocketChannel
openSocketChannel()
throws
IOException
```

Opens a socket channel.

**Returns:** The new channel
**Throws:** IOException

- If an I/O error occurs

- inheritedChannel

```java
public
Channel
inheritedChannel()
throws
IOException
```

Returns the channel inherited from the entity that created this
Java virtual machine.

On many operating systems a process, such as a Java virtual
machine, can be started in a manner that allows the process to
inherit a channel from the entity that created the process. The
manner in which this is done is system dependent, as are the
possible entities to which the channel may be connected. For example,
on UNIX systems, the Internet services daemon (

inetd

) is used to
start programs to service requests when a request arrives on an
associated network port. In this example, the process that is started,
inherits a channel representing a network socket.

In cases where the inherited channel represents a network socket
then the

Channel

type returned
by this method is determined as follows:

- If the inherited channel represents a stream-oriented connected
socket then a

SocketChannel

is
returned. The socket channel is, at least initially, in blocking
mode, bound to a socket address, and connected to a peer.
- If the inherited channel represents a stream-oriented listening
socket then a

ServerSocketChannel

is returned. The server-socket channel is, at
least initially, in blocking mode, and bound to a socket address.
- If the inherited channel is a datagram-oriented socket
then a

DatagramChannel

is
returned. The datagram channel is, at least initially, in blocking
mode, and bound to a socket address.

In addition to the network-oriented channels described, this method
may return other kinds of channels in the future.

The first invocation of this method creates the channel that is
returned. Subsequent invocations of this method return the same
channel.

**Returns:** The inherited channel, if any, otherwise

null

.
**Throws:** IOException

- If an I/O error occurs
**Throws:** SecurityException

- If a security manager has been installed and it denies

RuntimePermission

("inheritedChannel")
**Since:** 1.5

---

#### Method Detail

provider

```java
public static
SelectorProvider
provider()
```

Returns the system-wide default selector provider for this invocation of
the Java virtual machine.

The first invocation of this method locates the default provider
object as follows:

- If the system property

java.nio.channels.spi.SelectorProvider

is defined then it is
taken to be the fully-qualified name of a concrete provider class.
The class is loaded and instantiated; if this process fails then an
unspecified error is thrown.
- If a provider class has been installed in a jar file that is
visible to the system class loader, and that jar file contains a
provider-configuration file named

java.nio.channels.spi.SelectorProvider

in the resource
directory

META-INF/services

, then the first class name
specified in that file is taken. The class is loaded and
instantiated; if this process fails then an unspecified error is
thrown.
- Finally, if no provider has been specified by any of the above
means then the system-default provider class is instantiated and the
result is returned.

Subsequent invocations of this method return the provider that was
returned by the first invocation.

**Returns:** The system-wide default selector provider

---

#### provider

public static

SelectorProvider

provider()

Returns the system-wide default selector provider for this invocation of
the Java virtual machine.

The first invocation of this method locates the default provider
object as follows:

- If the system property

java.nio.channels.spi.SelectorProvider

is defined then it is
taken to be the fully-qualified name of a concrete provider class.
The class is loaded and instantiated; if this process fails then an
unspecified error is thrown.
- If a provider class has been installed in a jar file that is
visible to the system class loader, and that jar file contains a
provider-configuration file named

java.nio.channels.spi.SelectorProvider

in the resource
directory

META-INF/services

, then the first class name
specified in that file is taken. The class is loaded and
instantiated; if this process fails then an unspecified error is
thrown.
- Finally, if no provider has been specified by any of the above
means then the system-default provider class is instantiated and the
result is returned.

Subsequent invocations of this method return the provider that was
returned by the first invocation.

The first invocation of this method locates the default provider
object as follows:

If the system property

java.nio.channels.spi.SelectorProvider

is defined then it is
taken to be the fully-qualified name of a concrete provider class.
The class is loaded and instantiated; if this process fails then an
unspecified error is thrown.

If a provider class has been installed in a jar file that is
visible to the system class loader, and that jar file contains a
provider-configuration file named

java.nio.channels.spi.SelectorProvider

in the resource
directory

META-INF/services

, then the first class name
specified in that file is taken. The class is loaded and
instantiated; if this process fails then an unspecified error is
thrown.

Finally, if no provider has been specified by any of the above
means then the system-default provider class is instantiated and the
result is returned.

If the system property

java.nio.channels.spi.SelectorProvider

is defined then it is
taken to be the fully-qualified name of a concrete provider class.
The class is loaded and instantiated; if this process fails then an
unspecified error is thrown.

If a provider class has been installed in a jar file that is
visible to the system class loader, and that jar file contains a
provider-configuration file named

java.nio.channels.spi.SelectorProvider

in the resource
directory

META-INF/services

, then the first class name
specified in that file is taken. The class is loaded and
instantiated; if this process fails then an unspecified error is
thrown.

Finally, if no provider has been specified by any of the above
means then the system-default provider class is instantiated and the
result is returned.

Subsequent invocations of this method return the provider that was
returned by the first invocation.

openDatagramChannel

```java
public abstract
DatagramChannel
openDatagramChannel()
throws
IOException
```

Opens a datagram channel.

**Returns:** The new channel
**Throws:** IOException

- If an I/O error occurs

---

#### openDatagramChannel

public abstract

DatagramChannel

openDatagramChannel()
throws

IOException

Opens a datagram channel.

openDatagramChannel

```java
public abstract
DatagramChannel
openDatagramChannel​(
ProtocolFamily
family)
throws
IOException
```

Opens a datagram channel.

**Parameters:** family

- The protocol family
**Returns:** A new datagram channel
**Throws:** UnsupportedOperationException

- If the specified protocol family is not supported
**Throws:** IOException

- If an I/O error occurs
**Since:** 1.7

---

#### openDatagramChannel

public abstract

DatagramChannel

openDatagramChannel​(

ProtocolFamily

family)
throws

IOException

Opens a datagram channel.

openPipe

```java
public abstract
Pipe
openPipe()
throws
IOException
```

Opens a pipe.

**Returns:** The new pipe
**Throws:** IOException

- If an I/O error occurs

---

#### openPipe

public abstract

Pipe

openPipe()
throws

IOException

Opens a pipe.

openSelector

```java
public abstract
AbstractSelector
openSelector()
throws
IOException
```

Opens a selector.

**Returns:** The new selector
**Throws:** IOException

- If an I/O error occurs

---

#### openSelector

public abstract

AbstractSelector

openSelector()
throws

IOException

Opens a selector.

openServerSocketChannel

```java
public abstract
ServerSocketChannel
openServerSocketChannel()
throws
IOException
```

Opens a server-socket channel.

**Returns:** The new channel
**Throws:** IOException

- If an I/O error occurs

---

#### openServerSocketChannel

public abstract

ServerSocketChannel

openServerSocketChannel()
throws

IOException

Opens a server-socket channel.

openSocketChannel

```java
public abstract
SocketChannel
openSocketChannel()
throws
IOException
```

Opens a socket channel.

**Returns:** The new channel
**Throws:** IOException

- If an I/O error occurs

---

#### openSocketChannel

public abstract

SocketChannel

openSocketChannel()
throws

IOException

Opens a socket channel.

inheritedChannel

```java
public
Channel
inheritedChannel()
throws
IOException
```

Returns the channel inherited from the entity that created this
Java virtual machine.

On many operating systems a process, such as a Java virtual
machine, can be started in a manner that allows the process to
inherit a channel from the entity that created the process. The
manner in which this is done is system dependent, as are the
possible entities to which the channel may be connected. For example,
on UNIX systems, the Internet services daemon (

inetd

) is used to
start programs to service requests when a request arrives on an
associated network port. In this example, the process that is started,
inherits a channel representing a network socket.

In cases where the inherited channel represents a network socket
then the

Channel

type returned
by this method is determined as follows:

- If the inherited channel represents a stream-oriented connected
socket then a

SocketChannel

is
returned. The socket channel is, at least initially, in blocking
mode, bound to a socket address, and connected to a peer.
- If the inherited channel represents a stream-oriented listening
socket then a

ServerSocketChannel

is returned. The server-socket channel is, at
least initially, in blocking mode, and bound to a socket address.
- If the inherited channel is a datagram-oriented socket
then a

DatagramChannel

is
returned. The datagram channel is, at least initially, in blocking
mode, and bound to a socket address.

In addition to the network-oriented channels described, this method
may return other kinds of channels in the future.

The first invocation of this method creates the channel that is
returned. Subsequent invocations of this method return the same
channel.

**Returns:** The inherited channel, if any, otherwise

null

.
**Throws:** IOException

- If an I/O error occurs
**Throws:** SecurityException

- If a security manager has been installed and it denies

RuntimePermission

("inheritedChannel")
**Since:** 1.5

---

#### inheritedChannel

public

Channel

inheritedChannel()
throws

IOException

Returns the channel inherited from the entity that created this
Java virtual machine.

On many operating systems a process, such as a Java virtual
machine, can be started in a manner that allows the process to
inherit a channel from the entity that created the process. The
manner in which this is done is system dependent, as are the
possible entities to which the channel may be connected. For example,
on UNIX systems, the Internet services daemon (

inetd

) is used to
start programs to service requests when a request arrives on an
associated network port. In this example, the process that is started,
inherits a channel representing a network socket.

In cases where the inherited channel represents a network socket
then the

Channel

type returned
by this method is determined as follows:

- If the inherited channel represents a stream-oriented connected
socket then a

SocketChannel

is
returned. The socket channel is, at least initially, in blocking
mode, bound to a socket address, and connected to a peer.
- If the inherited channel represents a stream-oriented listening
socket then a

ServerSocketChannel

is returned. The server-socket channel is, at
least initially, in blocking mode, and bound to a socket address.
- If the inherited channel is a datagram-oriented socket
then a

DatagramChannel

is
returned. The datagram channel is, at least initially, in blocking
mode, and bound to a socket address.

In addition to the network-oriented channels described, this method
may return other kinds of channels in the future.

The first invocation of this method creates the channel that is
returned. Subsequent invocations of this method return the same
channel.

On many operating systems a process, such as a Java virtual
machine, can be started in a manner that allows the process to
inherit a channel from the entity that created the process. The
manner in which this is done is system dependent, as are the
possible entities to which the channel may be connected. For example,
on UNIX systems, the Internet services daemon (

inetd

) is used to
start programs to service requests when a request arrives on an
associated network port. In this example, the process that is started,
inherits a channel representing a network socket.

In cases where the inherited channel represents a network socket
then the

Channel

type returned
by this method is determined as follows:

- If the inherited channel represents a stream-oriented connected
socket then a

SocketChannel

is
returned. The socket channel is, at least initially, in blocking
mode, bound to a socket address, and connected to a peer.
- If the inherited channel represents a stream-oriented listening
socket then a

ServerSocketChannel

is returned. The server-socket channel is, at
least initially, in blocking mode, and bound to a socket address.
- If the inherited channel is a datagram-oriented socket
then a

DatagramChannel

is
returned. The datagram channel is, at least initially, in blocking
mode, and bound to a socket address.

In addition to the network-oriented channels described, this method
may return other kinds of channels in the future.

The first invocation of this method creates the channel that is
returned. Subsequent invocations of this method return the same
channel.

In cases where the inherited channel represents a network socket
then the

Channel

type returned
by this method is determined as follows:

- If the inherited channel represents a stream-oriented connected
socket then a

SocketChannel

is
returned. The socket channel is, at least initially, in blocking
mode, bound to a socket address, and connected to a peer.
- If the inherited channel represents a stream-oriented listening
socket then a

ServerSocketChannel

is returned. The server-socket channel is, at
least initially, in blocking mode, and bound to a socket address.
- If the inherited channel is a datagram-oriented socket
then a

DatagramChannel

is
returned. The datagram channel is, at least initially, in blocking
mode, and bound to a socket address.

In addition to the network-oriented channels described, this method
may return other kinds of channels in the future.

The first invocation of this method creates the channel that is
returned. Subsequent invocations of this method return the same
channel.

If the inherited channel represents a stream-oriented connected
socket then a

SocketChannel

is
returned. The socket channel is, at least initially, in blocking
mode, bound to a socket address, and connected to a peer.

If the inherited channel represents a stream-oriented listening
socket then a

ServerSocketChannel

is returned. The server-socket channel is, at
least initially, in blocking mode, and bound to a socket address.

If the inherited channel is a datagram-oriented socket
then a

DatagramChannel

is
returned. The datagram channel is, at least initially, in blocking
mode, and bound to a socket address.

If the inherited channel represents a stream-oriented connected
socket then a

SocketChannel

is
returned. The socket channel is, at least initially, in blocking
mode, bound to a socket address, and connected to a peer.

If the inherited channel represents a stream-oriented listening
socket then a

ServerSocketChannel

is returned. The server-socket channel is, at
least initially, in blocking mode, and bound to a socket address.

If the inherited channel is a datagram-oriented socket
then a

DatagramChannel

is
returned. The datagram channel is, at least initially, in blocking
mode, and bound to a socket address.

In addition to the network-oriented channels described, this method
may return other kinds of channels in the future.

The first invocation of this method creates the channel that is
returned. Subsequent invocations of this method return the same
channel.

The first invocation of this method creates the channel that is
returned. Subsequent invocations of this method return the same
channel.

---

