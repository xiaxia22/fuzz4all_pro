# Class AsynchronousChannelProvider

**Source:** `java.base\java\nio\channels\spi\AsynchronousChannelProvider.html`

### Class Description

```java
public abstract class
AsynchronousChannelProvider

extends
Object
```

Service-provider class for asynchronous channels.

An asynchronous channel provider is a concrete subclass of this class that
has a zero-argument constructor and implements the abstract methods specified
below. A given invocation of the Java virtual machine maintains a single
system-wide default provider instance, which is returned by the

provider

method. The first invocation of that method will locate
the default provider as specified below.

All of the methods in this class are safe for use by multiple concurrent
threads.

**Since:** 1.7

---

### Field Details

*No entries found.*

### Constructor Details

#### protected AsynchronousChannelProvider()

Initializes a new instance of this class.

**Throws:**
- SecurityException

- If a security manager has been installed and it denies

RuntimePermission

("asynchronousChannelProvider")

---

### Method Details

#### public static
AsynchronousChannelProvider
provider()

Returns the system-wide default asynchronous channel provider for this
invocation of the Java virtual machine.

The first invocation of this method locates the default provider
object as follows:

- If the system property

java.nio.channels.spi.AsynchronousChannelProvider

is defined
then it is taken to be the fully-qualified name of a concrete provider class.
The class is loaded and instantiated; if this process fails then an
unspecified error is thrown.
- If a provider class has been installed in a jar file that is
visible to the system class loader, and that jar file contains a
provider-configuration file named

java.nio.channels.spi.AsynchronousChannelProvider

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
- The system-wide default AsynchronousChannel provider

---

#### public abstract
AsynchronousChannelGroup
openAsynchronousChannelGroup​(int nThreads,

ThreadFactory
threadFactory)
throws
IOException

Constructs a new asynchronous channel group with a fixed thread pool.

**Parameters:**
- nThreads

- The number of threads in the pool
- threadFactory

- The factory to use when creating new threads

**Returns:**
- A new asynchronous channel group

**Throws:**
- IllegalArgumentException

- If

nThreads <= 0
- IOException

- If an I/O error occurs

**See Also:**
- AsynchronousChannelGroup.withFixedThreadPool(int, java.util.concurrent.ThreadFactory)

---

#### public abstract
AsynchronousChannelGroup
openAsynchronousChannelGroup​(
ExecutorService
executor,
int initialSize)
throws
IOException

Constructs a new asynchronous channel group with the given thread pool.

**Parameters:**
- executor

- The thread pool
- initialSize

- A value

>=0

or a negative value for implementation
specific default

**Returns:**
- A new asynchronous channel group

**Throws:**
- IOException

- If an I/O error occurs

**See Also:**
- AsynchronousChannelGroup.withCachedThreadPool(java.util.concurrent.ExecutorService, int)

---

#### public abstract
AsynchronousServerSocketChannel
openAsynchronousServerSocketChannel​(
AsynchronousChannelGroup
group)
throws
IOException

Opens an asynchronous server-socket channel.

**Parameters:**
- group

- The group to which the channel is bound, or

null

to
bind to the default group

**Returns:**
- The new channel

**Throws:**
- IllegalChannelGroupException

- If the provider that created the group differs from this provider
- ShutdownChannelGroupException

- The group is shutdown
- IOException

- If an I/O error occurs

---

#### public abstract
AsynchronousSocketChannel
openAsynchronousSocketChannel​(
AsynchronousChannelGroup
group)
throws
IOException

Opens an asynchronous socket channel.

**Parameters:**
- group

- The group to which the channel is bound, or

null

to
bind to the default group

**Returns:**
- The new channel

**Throws:**
- IllegalChannelGroupException

- If the provider that created the group differs from this provider
- ShutdownChannelGroupException

- The group is shutdown
- IOException

- If an I/O error occurs

---

### Additional Sections

#### Class AsynchronousChannelProvider

java.lang.Object

- java.nio.channels.spi.AsynchronousChannelProvider

java.nio.channels.spi.AsynchronousChannelProvider

```java
public abstract class
AsynchronousChannelProvider

extends
Object
```

Service-provider class for asynchronous channels.

An asynchronous channel provider is a concrete subclass of this class that
has a zero-argument constructor and implements the abstract methods specified
below. A given invocation of the Java virtual machine maintains a single
system-wide default provider instance, which is returned by the

provider

method. The first invocation of that method will locate
the default provider as specified below.

All of the methods in this class are safe for use by multiple concurrent
threads.

**Since:** 1.7

public abstract class

AsynchronousChannelProvider

extends

Object

Service-provider class for asynchronous channels.

An asynchronous channel provider is a concrete subclass of this class that
has a zero-argument constructor and implements the abstract methods specified
below. A given invocation of the Java virtual machine maintains a single
system-wide default provider instance, which is returned by the

provider

method. The first invocation of that method will locate
the default provider as specified below.

All of the methods in this class are safe for use by multiple concurrent
threads.

An asynchronous channel provider is a concrete subclass of this class that
has a zero-argument constructor and implements the abstract methods specified
below. A given invocation of the Java virtual machine maintains a single
system-wide default provider instance, which is returned by the

provider

method. The first invocation of that method will locate
the default provider as specified below.

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

AsynchronousChannelProvider

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

abstract

AsynchronousChannelGroup

openAsynchronousChannelGroup

​(int nThreads,

ThreadFactory

threadFactory)

Constructs a new asynchronous channel group with a fixed thread pool.

abstract

AsynchronousChannelGroup

openAsynchronousChannelGroup

​(

ExecutorService

executor,
int initialSize)

Constructs a new asynchronous channel group with the given thread pool.

abstract

AsynchronousServerSocketChannel

openAsynchronousServerSocketChannel

​(

AsynchronousChannelGroup

group)

Opens an asynchronous server-socket channel.

abstract

AsynchronousSocketChannel

openAsynchronousSocketChannel

​(

AsynchronousChannelGroup

group)

Opens an asynchronous socket channel.

static

AsynchronousChannelProvider

provider

()

Returns the system-wide default asynchronous channel provider for this
invocation of the Java virtual machine.

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

AsynchronousChannelProvider

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

abstract

AsynchronousChannelGroup

openAsynchronousChannelGroup

​(int nThreads,

ThreadFactory

threadFactory)

Constructs a new asynchronous channel group with a fixed thread pool.

abstract

AsynchronousChannelGroup

openAsynchronousChannelGroup

​(

ExecutorService

executor,
int initialSize)

Constructs a new asynchronous channel group with the given thread pool.

abstract

AsynchronousServerSocketChannel

openAsynchronousServerSocketChannel

​(

AsynchronousChannelGroup

group)

Opens an asynchronous server-socket channel.

abstract

AsynchronousSocketChannel

openAsynchronousSocketChannel

​(

AsynchronousChannelGroup

group)

Opens an asynchronous socket channel.

static

AsynchronousChannelProvider

provider

()

Returns the system-wide default asynchronous channel provider for this
invocation of the Java virtual machine.

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

Constructs a new asynchronous channel group with a fixed thread pool.

Constructs a new asynchronous channel group with the given thread pool.

Opens an asynchronous server-socket channel.

Opens an asynchronous socket channel.

Returns the system-wide default asynchronous channel provider for this
invocation of the Java virtual machine.

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

- AsynchronousChannelProvider

```java
protected AsynchronousChannelProvider()
```

Initializes a new instance of this class.

**Throws:** SecurityException

- If a security manager has been installed and it denies

RuntimePermission

("asynchronousChannelProvider")

============ METHOD DETAIL ==========

- Method Detail

- provider

```java
public static
AsynchronousChannelProvider
provider()
```

Returns the system-wide default asynchronous channel provider for this
invocation of the Java virtual machine.

The first invocation of this method locates the default provider
object as follows:

- If the system property

java.nio.channels.spi.AsynchronousChannelProvider

is defined
then it is taken to be the fully-qualified name of a concrete provider class.
The class is loaded and instantiated; if this process fails then an
unspecified error is thrown.
- If a provider class has been installed in a jar file that is
visible to the system class loader, and that jar file contains a
provider-configuration file named

java.nio.channels.spi.AsynchronousChannelProvider

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

**Returns:** The system-wide default AsynchronousChannel provider

- openAsynchronousChannelGroup

```java
public abstract
AsynchronousChannelGroup
openAsynchronousChannelGroup​(int nThreads,

ThreadFactory
threadFactory)
throws
IOException
```

Constructs a new asynchronous channel group with a fixed thread pool.

**Parameters:** nThreads

- The number of threads in the pool
**Parameters:** threadFactory

- The factory to use when creating new threads
**Returns:** A new asynchronous channel group
**Throws:** IllegalArgumentException

- If

nThreads <= 0
**Throws:** IOException

- If an I/O error occurs
**See Also:** AsynchronousChannelGroup.withFixedThreadPool(int, java.util.concurrent.ThreadFactory)

- openAsynchronousChannelGroup

```java
public abstract
AsynchronousChannelGroup
openAsynchronousChannelGroup​(
ExecutorService
executor,
int initialSize)
throws
IOException
```

Constructs a new asynchronous channel group with the given thread pool.

**Parameters:** executor

- The thread pool
**Parameters:** initialSize

- A value

>=0

or a negative value for implementation
specific default
**Returns:** A new asynchronous channel group
**Throws:** IOException

- If an I/O error occurs
**See Also:** AsynchronousChannelGroup.withCachedThreadPool(java.util.concurrent.ExecutorService, int)

- openAsynchronousServerSocketChannel

```java
public abstract
AsynchronousServerSocketChannel
openAsynchronousServerSocketChannel​(
AsynchronousChannelGroup
group)
throws
IOException
```

Opens an asynchronous server-socket channel.

**Parameters:** group

- The group to which the channel is bound, or

null

to
bind to the default group
**Returns:** The new channel
**Throws:** IllegalChannelGroupException

- If the provider that created the group differs from this provider
**Throws:** ShutdownChannelGroupException

- The group is shutdown
**Throws:** IOException

- If an I/O error occurs

- openAsynchronousSocketChannel

```java
public abstract
AsynchronousSocketChannel
openAsynchronousSocketChannel​(
AsynchronousChannelGroup
group)
throws
IOException
```

Opens an asynchronous socket channel.

**Parameters:** group

- The group to which the channel is bound, or

null

to
bind to the default group
**Returns:** The new channel
**Throws:** IllegalChannelGroupException

- If the provider that created the group differs from this provider
**Throws:** ShutdownChannelGroupException

- The group is shutdown
**Throws:** IOException

- If an I/O error occurs

Constructor Detail

- AsynchronousChannelProvider

```java
protected AsynchronousChannelProvider()
```

Initializes a new instance of this class.

**Throws:** SecurityException

- If a security manager has been installed and it denies

RuntimePermission

("asynchronousChannelProvider")

---

#### Constructor Detail

AsynchronousChannelProvider

```java
protected AsynchronousChannelProvider()
```

Initializes a new instance of this class.

**Throws:** SecurityException

- If a security manager has been installed and it denies

RuntimePermission

("asynchronousChannelProvider")

---

#### AsynchronousChannelProvider

protected AsynchronousChannelProvider()

Initializes a new instance of this class.

Method Detail

- provider

```java
public static
AsynchronousChannelProvider
provider()
```

Returns the system-wide default asynchronous channel provider for this
invocation of the Java virtual machine.

The first invocation of this method locates the default provider
object as follows:

- If the system property

java.nio.channels.spi.AsynchronousChannelProvider

is defined
then it is taken to be the fully-qualified name of a concrete provider class.
The class is loaded and instantiated; if this process fails then an
unspecified error is thrown.
- If a provider class has been installed in a jar file that is
visible to the system class loader, and that jar file contains a
provider-configuration file named

java.nio.channels.spi.AsynchronousChannelProvider

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

**Returns:** The system-wide default AsynchronousChannel provider

- openAsynchronousChannelGroup

```java
public abstract
AsynchronousChannelGroup
openAsynchronousChannelGroup​(int nThreads,

ThreadFactory
threadFactory)
throws
IOException
```

Constructs a new asynchronous channel group with a fixed thread pool.

**Parameters:** nThreads

- The number of threads in the pool
**Parameters:** threadFactory

- The factory to use when creating new threads
**Returns:** A new asynchronous channel group
**Throws:** IllegalArgumentException

- If

nThreads <= 0
**Throws:** IOException

- If an I/O error occurs
**See Also:** AsynchronousChannelGroup.withFixedThreadPool(int, java.util.concurrent.ThreadFactory)

- openAsynchronousChannelGroup

```java
public abstract
AsynchronousChannelGroup
openAsynchronousChannelGroup​(
ExecutorService
executor,
int initialSize)
throws
IOException
```

Constructs a new asynchronous channel group with the given thread pool.

**Parameters:** executor

- The thread pool
**Parameters:** initialSize

- A value

>=0

or a negative value for implementation
specific default
**Returns:** A new asynchronous channel group
**Throws:** IOException

- If an I/O error occurs
**See Also:** AsynchronousChannelGroup.withCachedThreadPool(java.util.concurrent.ExecutorService, int)

- openAsynchronousServerSocketChannel

```java
public abstract
AsynchronousServerSocketChannel
openAsynchronousServerSocketChannel​(
AsynchronousChannelGroup
group)
throws
IOException
```

Opens an asynchronous server-socket channel.

**Parameters:** group

- The group to which the channel is bound, or

null

to
bind to the default group
**Returns:** The new channel
**Throws:** IllegalChannelGroupException

- If the provider that created the group differs from this provider
**Throws:** ShutdownChannelGroupException

- The group is shutdown
**Throws:** IOException

- If an I/O error occurs

- openAsynchronousSocketChannel

```java
public abstract
AsynchronousSocketChannel
openAsynchronousSocketChannel​(
AsynchronousChannelGroup
group)
throws
IOException
```

Opens an asynchronous socket channel.

**Parameters:** group

- The group to which the channel is bound, or

null

to
bind to the default group
**Returns:** The new channel
**Throws:** IllegalChannelGroupException

- If the provider that created the group differs from this provider
**Throws:** ShutdownChannelGroupException

- The group is shutdown
**Throws:** IOException

- If an I/O error occurs

---

#### Method Detail

provider

```java
public static
AsynchronousChannelProvider
provider()
```

Returns the system-wide default asynchronous channel provider for this
invocation of the Java virtual machine.

The first invocation of this method locates the default provider
object as follows:

- If the system property

java.nio.channels.spi.AsynchronousChannelProvider

is defined
then it is taken to be the fully-qualified name of a concrete provider class.
The class is loaded and instantiated; if this process fails then an
unspecified error is thrown.
- If a provider class has been installed in a jar file that is
visible to the system class loader, and that jar file contains a
provider-configuration file named

java.nio.channels.spi.AsynchronousChannelProvider

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

**Returns:** The system-wide default AsynchronousChannel provider

---

#### provider

public static

AsynchronousChannelProvider

provider()

Returns the system-wide default asynchronous channel provider for this
invocation of the Java virtual machine.

The first invocation of this method locates the default provider
object as follows:

- If the system property

java.nio.channels.spi.AsynchronousChannelProvider

is defined
then it is taken to be the fully-qualified name of a concrete provider class.
The class is loaded and instantiated; if this process fails then an
unspecified error is thrown.
- If a provider class has been installed in a jar file that is
visible to the system class loader, and that jar file contains a
provider-configuration file named

java.nio.channels.spi.AsynchronousChannelProvider

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

java.nio.channels.spi.AsynchronousChannelProvider

is defined
then it is taken to be the fully-qualified name of a concrete provider class.
The class is loaded and instantiated; if this process fails then an
unspecified error is thrown.

If a provider class has been installed in a jar file that is
visible to the system class loader, and that jar file contains a
provider-configuration file named

java.nio.channels.spi.AsynchronousChannelProvider

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

java.nio.channels.spi.AsynchronousChannelProvider

is defined
then it is taken to be the fully-qualified name of a concrete provider class.
The class is loaded and instantiated; if this process fails then an
unspecified error is thrown.

If a provider class has been installed in a jar file that is
visible to the system class loader, and that jar file contains a
provider-configuration file named

java.nio.channels.spi.AsynchronousChannelProvider

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

openAsynchronousChannelGroup

```java
public abstract
AsynchronousChannelGroup
openAsynchronousChannelGroup​(int nThreads,

ThreadFactory
threadFactory)
throws
IOException
```

Constructs a new asynchronous channel group with a fixed thread pool.

**Parameters:** nThreads

- The number of threads in the pool
**Parameters:** threadFactory

- The factory to use when creating new threads
**Returns:** A new asynchronous channel group
**Throws:** IllegalArgumentException

- If

nThreads <= 0
**Throws:** IOException

- If an I/O error occurs
**See Also:** AsynchronousChannelGroup.withFixedThreadPool(int, java.util.concurrent.ThreadFactory)

---

#### openAsynchronousChannelGroup

public abstract

AsynchronousChannelGroup

openAsynchronousChannelGroup​(int nThreads,

ThreadFactory

threadFactory)
throws

IOException

Constructs a new asynchronous channel group with a fixed thread pool.

openAsynchronousChannelGroup

```java
public abstract
AsynchronousChannelGroup
openAsynchronousChannelGroup​(
ExecutorService
executor,
int initialSize)
throws
IOException
```

Constructs a new asynchronous channel group with the given thread pool.

**Parameters:** executor

- The thread pool
**Parameters:** initialSize

- A value

>=0

or a negative value for implementation
specific default
**Returns:** A new asynchronous channel group
**Throws:** IOException

- If an I/O error occurs
**See Also:** AsynchronousChannelGroup.withCachedThreadPool(java.util.concurrent.ExecutorService, int)

---

#### openAsynchronousChannelGroup

public abstract

AsynchronousChannelGroup

openAsynchronousChannelGroup​(

ExecutorService

executor,
int initialSize)
throws

IOException

Constructs a new asynchronous channel group with the given thread pool.

openAsynchronousServerSocketChannel

```java
public abstract
AsynchronousServerSocketChannel
openAsynchronousServerSocketChannel​(
AsynchronousChannelGroup
group)
throws
IOException
```

Opens an asynchronous server-socket channel.

**Parameters:** group

- The group to which the channel is bound, or

null

to
bind to the default group
**Returns:** The new channel
**Throws:** IllegalChannelGroupException

- If the provider that created the group differs from this provider
**Throws:** ShutdownChannelGroupException

- The group is shutdown
**Throws:** IOException

- If an I/O error occurs

---

#### openAsynchronousServerSocketChannel

public abstract

AsynchronousServerSocketChannel

openAsynchronousServerSocketChannel​(

AsynchronousChannelGroup

group)
throws

IOException

Opens an asynchronous server-socket channel.

openAsynchronousSocketChannel

```java
public abstract
AsynchronousSocketChannel
openAsynchronousSocketChannel​(
AsynchronousChannelGroup
group)
throws
IOException
```

Opens an asynchronous socket channel.

**Parameters:** group

- The group to which the channel is bound, or

null

to
bind to the default group
**Returns:** The new channel
**Throws:** IllegalChannelGroupException

- If the provider that created the group differs from this provider
**Throws:** ShutdownChannelGroupException

- The group is shutdown
**Throws:** IOException

- If an I/O error occurs

---

#### openAsynchronousSocketChannel

public abstract

AsynchronousSocketChannel

openAsynchronousSocketChannel​(

AsynchronousChannelGroup

group)
throws

IOException

Opens an asynchronous socket channel.

---

