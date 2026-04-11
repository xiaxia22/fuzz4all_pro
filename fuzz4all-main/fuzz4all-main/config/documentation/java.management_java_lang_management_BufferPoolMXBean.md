# Interface BufferPoolMXBean

**Source:** `java.management\java\lang\management\BufferPoolMXBean.html`

### Class Description

```java
public interface
BufferPoolMXBean

extends
PlatformManagedObject
```

The management interface for a buffer pool, for example a pool of

direct

or

mapped

buffers.

A class implementing this interface is an

MXBean

. A Java
virtual machine has one or more implementations of this interface. The

getPlatformMXBeans

method can be used to obtain the list of

BufferPoolMXBean

objects
representing the management interfaces for pools of buffers as follows:

```java
List<BufferPoolMXBean> pools = ManagementFactory.getPlatformMXBeans(BufferPoolMXBean.class);
```

The management interfaces are also registered with the platform

MBeanServer

. The

ObjectName

that uniquely identifies the
management interface within the

MBeanServer

takes the form:

```java
java.nio:type=BufferPool,name=
pool name
```

where

pool name

is the

name

of the buffer pool.

**All Superinterfaces:** PlatformManagedObject

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### String
getName()

Returns the name representing this buffer pool.

**Returns:**
- The name of this buffer pool.

---

#### long getCount()

Returns an estimate of the number of buffers in the pool.

**Returns:**
- An estimate of the number of buffers in this pool

---

#### long getTotalCapacity()

Returns an estimate of the total capacity of the buffers in this pool.
A buffer's capacity is the number of elements it contains and the value
returned by this method is an estimate of the total capacity of buffers
in the pool in bytes.

**Returns:**
- An estimate of the total capacity of the buffers in this pool
in bytes

---

#### long getMemoryUsed()

Returns an estimate of the memory that the Java virtual machine is using
for this buffer pool. The value returned by this method may differ
from the estimate of the total

capacity

of
the buffers in this pool. This difference is explained by alignment,
memory allocator, and other implementation specific reasons.

**Returns:**
- An estimate of the memory that the Java virtual machine is using
for this buffer pool in bytes, or

-1L

if an estimate of
the memory usage is not available

---

### Additional Sections

#### Interface BufferPoolMXBean

**All Superinterfaces:** PlatformManagedObject

```java
public interface
BufferPoolMXBean

extends
PlatformManagedObject
```

The management interface for a buffer pool, for example a pool of

direct

or

mapped

buffers.

A class implementing this interface is an

MXBean

. A Java
virtual machine has one or more implementations of this interface. The

getPlatformMXBeans

method can be used to obtain the list of

BufferPoolMXBean

objects
representing the management interfaces for pools of buffers as follows:

```java
List<BufferPoolMXBean> pools = ManagementFactory.getPlatformMXBeans(BufferPoolMXBean.class);
```

The management interfaces are also registered with the platform

MBeanServer

. The

ObjectName

that uniquely identifies the
management interface within the

MBeanServer

takes the form:

```java
java.nio:type=BufferPool,name=
pool name
```

where

pool name

is the

name

of the buffer pool.

**Since:** 1.7

public interface

BufferPoolMXBean

extends

PlatformManagedObject

The management interface for a buffer pool, for example a pool of

direct

or

mapped

buffers.

A class implementing this interface is an

MXBean

. A Java
virtual machine has one or more implementations of this interface. The

getPlatformMXBeans

method can be used to obtain the list of

BufferPoolMXBean

objects
representing the management interfaces for pools of buffers as follows:

```java
List<BufferPoolMXBean> pools = ManagementFactory.getPlatformMXBeans(BufferPoolMXBean.class);
```

The management interfaces are also registered with the platform

MBeanServer

. The

ObjectName

that uniquely identifies the
management interface within the

MBeanServer

takes the form:

```java
java.nio:type=BufferPool,name=
pool name
```

where

pool name

is the

name

of the buffer pool.

A class implementing this interface is an

MXBean

. A Java
virtual machine has one or more implementations of this interface. The

getPlatformMXBeans

method can be used to obtain the list of

BufferPoolMXBean

objects
representing the management interfaces for pools of buffers as follows:

```java
List<BufferPoolMXBean> pools = ManagementFactory.getPlatformMXBeans(BufferPoolMXBean.class);
```

The management interfaces are also registered with the platform

MBeanServer

. The

ObjectName

that uniquely identifies the
management interface within the

MBeanServer

takes the form:

```java
java.nio:type=BufferPool,name=
pool name
```

where

pool name

is the

name

of the buffer pool.

List<BufferPoolMXBean> pools = ManagementFactory.getPlatformMXBeans(BufferPoolMXBean.class);

The management interfaces are also registered with the platform

MBeanServer

. The

ObjectName

that uniquely identifies the
management interface within the

MBeanServer

takes the form:

```java
java.nio:type=BufferPool,name=
pool name
```

where

pool name

is the

name

of the buffer pool.

java.nio:type=BufferPool,name=

pool name

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

long

getCount

()

Returns an estimate of the number of buffers in the pool.

long

getMemoryUsed

()

Returns an estimate of the memory that the Java virtual machine is using
for this buffer pool.

String

getName

()

Returns the name representing this buffer pool.

long

getTotalCapacity

()

Returns an estimate of the total capacity of the buffers in this pool.

- Methods declared in interface java.lang.management.

PlatformManagedObject

getObjectName

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

long

getCount

()

Returns an estimate of the number of buffers in the pool.

long

getMemoryUsed

()

Returns an estimate of the memory that the Java virtual machine is using
for this buffer pool.

String

getName

()

Returns the name representing this buffer pool.

long

getTotalCapacity

()

Returns an estimate of the total capacity of the buffers in this pool.

- Methods declared in interface java.lang.management.

PlatformManagedObject

getObjectName

---

#### Method Summary

Returns an estimate of the number of buffers in the pool.

Returns an estimate of the memory that the Java virtual machine is using
for this buffer pool.

Returns the name representing this buffer pool.

Returns an estimate of the total capacity of the buffers in this pool.

Methods declared in interface java.lang.management.

PlatformManagedObject

getObjectName

---

#### Methods declared in interface java.lang.management. PlatformManagedObject

============ METHOD DETAIL ==========

- Method Detail

- getName

```java
String
getName()
```

Returns the name representing this buffer pool.

**Returns:** The name of this buffer pool.

- getCount

```java
long getCount()
```

Returns an estimate of the number of buffers in the pool.

**Returns:** An estimate of the number of buffers in this pool

- getTotalCapacity

```java
long getTotalCapacity()
```

Returns an estimate of the total capacity of the buffers in this pool.
A buffer's capacity is the number of elements it contains and the value
returned by this method is an estimate of the total capacity of buffers
in the pool in bytes.

**Returns:** An estimate of the total capacity of the buffers in this pool
in bytes

- getMemoryUsed

```java
long getMemoryUsed()
```

Returns an estimate of the memory that the Java virtual machine is using
for this buffer pool. The value returned by this method may differ
from the estimate of the total

capacity

of
the buffers in this pool. This difference is explained by alignment,
memory allocator, and other implementation specific reasons.

**Returns:** An estimate of the memory that the Java virtual machine is using
for this buffer pool in bytes, or

-1L

if an estimate of
the memory usage is not available

Method Detail

- getName

```java
String
getName()
```

Returns the name representing this buffer pool.

**Returns:** The name of this buffer pool.

- getCount

```java
long getCount()
```

Returns an estimate of the number of buffers in the pool.

**Returns:** An estimate of the number of buffers in this pool

- getTotalCapacity

```java
long getTotalCapacity()
```

Returns an estimate of the total capacity of the buffers in this pool.
A buffer's capacity is the number of elements it contains and the value
returned by this method is an estimate of the total capacity of buffers
in the pool in bytes.

**Returns:** An estimate of the total capacity of the buffers in this pool
in bytes

- getMemoryUsed

```java
long getMemoryUsed()
```

Returns an estimate of the memory that the Java virtual machine is using
for this buffer pool. The value returned by this method may differ
from the estimate of the total

capacity

of
the buffers in this pool. This difference is explained by alignment,
memory allocator, and other implementation specific reasons.

**Returns:** An estimate of the memory that the Java virtual machine is using
for this buffer pool in bytes, or

-1L

if an estimate of
the memory usage is not available

---

#### Method Detail

getName

```java
String
getName()
```

Returns the name representing this buffer pool.

**Returns:** The name of this buffer pool.

---

#### getName

String

getName()

Returns the name representing this buffer pool.

getCount

```java
long getCount()
```

Returns an estimate of the number of buffers in the pool.

**Returns:** An estimate of the number of buffers in this pool

---

#### getCount

long getCount()

Returns an estimate of the number of buffers in the pool.

getTotalCapacity

```java
long getTotalCapacity()
```

Returns an estimate of the total capacity of the buffers in this pool.
A buffer's capacity is the number of elements it contains and the value
returned by this method is an estimate of the total capacity of buffers
in the pool in bytes.

**Returns:** An estimate of the total capacity of the buffers in this pool
in bytes

---

#### getTotalCapacity

long getTotalCapacity()

Returns an estimate of the total capacity of the buffers in this pool.
A buffer's capacity is the number of elements it contains and the value
returned by this method is an estimate of the total capacity of buffers
in the pool in bytes.

getMemoryUsed

```java
long getMemoryUsed()
```

Returns an estimate of the memory that the Java virtual machine is using
for this buffer pool. The value returned by this method may differ
from the estimate of the total

capacity

of
the buffers in this pool. This difference is explained by alignment,
memory allocator, and other implementation specific reasons.

**Returns:** An estimate of the memory that the Java virtual machine is using
for this buffer pool in bytes, or

-1L

if an estimate of
the memory usage is not available

---

#### getMemoryUsed

long getMemoryUsed()

Returns an estimate of the memory that the Java virtual machine is using
for this buffer pool. The value returned by this method may differ
from the estimate of the total

capacity

of
the buffers in this pool. This difference is explained by alignment,
memory allocator, and other implementation specific reasons.

---

