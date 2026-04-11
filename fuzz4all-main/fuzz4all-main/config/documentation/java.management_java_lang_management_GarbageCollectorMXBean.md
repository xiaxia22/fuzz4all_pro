# Interface GarbageCollectorMXBean

**Source:** `java.management\java\lang\management\GarbageCollectorMXBean.html`

### Class Description

```java
public interface
GarbageCollectorMXBean

extends
MemoryManagerMXBean
```

The management interface for the garbage collection of
the Java virtual machine. Garbage collection is the process
that the Java virtual machine uses to find and reclaim unreachable
objects to free up memory space. A garbage collector is one type of

memory manager

.

A Java virtual machine may have one or more instances of
the implementation class of this interface.
An instance implementing this interface is
an

MXBean

that can be obtained by calling
the

ManagementFactory.getGarbageCollectorMXBeans()

method or
from the

platform MBeanServer

method.

The

ObjectName

for uniquely identifying the MXBean for
a garbage collector within an MBeanServer is:

java.lang:type=GarbageCollector

,name=

collector's name

It can be obtained by calling the

PlatformManagedObject.getObjectName()

method.

A platform usually includes additional platform-dependent information
specific to a garbage collection algorithm for monitoring.

**All Superinterfaces:** MemoryManagerMXBean

,

PlatformManagedObject

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### long getCollectionCount()

Returns the total number of collections that have occurred.
This method returns

-1

if the collection count is undefined for
this collector.

**Returns:**
- the total number of collections that have occurred.

---

#### long getCollectionTime()

Returns the approximate accumulated collection elapsed time
in milliseconds. This method returns

-1

if the collection
elapsed time is undefined for this collector.

The Java virtual machine implementation may use a high resolution
timer to measure the elapsed time. This method may return the
same value even if the collection count has been incremented
if the collection elapsed time is very short.

**Returns:**
- the approximate accumulated collection elapsed time
in milliseconds.

---

### Additional Sections

#### Interface GarbageCollectorMXBean

**All Superinterfaces:** MemoryManagerMXBean

,

PlatformManagedObject

**All Known Subinterfaces:** GarbageCollectorMXBean

```java
public interface
GarbageCollectorMXBean

extends
MemoryManagerMXBean
```

The management interface for the garbage collection of
the Java virtual machine. Garbage collection is the process
that the Java virtual machine uses to find and reclaim unreachable
objects to free up memory space. A garbage collector is one type of

memory manager

.

A Java virtual machine may have one or more instances of
the implementation class of this interface.
An instance implementing this interface is
an

MXBean

that can be obtained by calling
the

ManagementFactory.getGarbageCollectorMXBeans()

method or
from the

platform MBeanServer

method.

The

ObjectName

for uniquely identifying the MXBean for
a garbage collector within an MBeanServer is:

java.lang:type=GarbageCollector

,name=

collector's name

It can be obtained by calling the

PlatformManagedObject.getObjectName()

method.

A platform usually includes additional platform-dependent information
specific to a garbage collection algorithm for monitoring.

**Since:** 1.5
**See Also:** ManagementFactory.getPlatformMXBeans(Class)

,

MemoryMXBean

,

JMX Specification.

,

Ways to Access MXBeans

public interface

GarbageCollectorMXBean

extends

MemoryManagerMXBean

The management interface for the garbage collection of
the Java virtual machine. Garbage collection is the process
that the Java virtual machine uses to find and reclaim unreachable
objects to free up memory space. A garbage collector is one type of

memory manager

.

A Java virtual machine may have one or more instances of
the implementation class of this interface.
An instance implementing this interface is
an

MXBean

that can be obtained by calling
the

ManagementFactory.getGarbageCollectorMXBeans()

method or
from the

platform MBeanServer

method.

The

ObjectName

for uniquely identifying the MXBean for
a garbage collector within an MBeanServer is:

java.lang:type=GarbageCollector

,name=

collector's name

It can be obtained by calling the

PlatformManagedObject.getObjectName()

method.

A platform usually includes additional platform-dependent information
specific to a garbage collection algorithm for monitoring.

A Java virtual machine may have one or more instances of
the implementation class of this interface.
An instance implementing this interface is
an

MXBean

that can be obtained by calling
the

ManagementFactory.getGarbageCollectorMXBeans()

method or
from the

platform MBeanServer

method.

The

ObjectName

for uniquely identifying the MXBean for
a garbage collector within an MBeanServer is:

java.lang:type=GarbageCollector

,name=

collector's name

It can be obtained by calling the

PlatformManagedObject.getObjectName()

method.

A platform usually includes additional platform-dependent information
specific to a garbage collection algorithm for monitoring.

The

ObjectName

for uniquely identifying the MXBean for
a garbage collector within an MBeanServer is:

java.lang:type=GarbageCollector

,name=

collector's name

It can be obtained by calling the

PlatformManagedObject.getObjectName()

method.

A platform usually includes additional platform-dependent information
specific to a garbage collection algorithm for monitoring.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

long

getCollectionCount

()

Returns the total number of collections that have occurred.

long

getCollectionTime

()

Returns the approximate accumulated collection elapsed time
in milliseconds.

- Methods declared in interface java.lang.management.

MemoryManagerMXBean

getMemoryPoolNames

,

getName

,

isValid

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

getCollectionCount

()

Returns the total number of collections that have occurred.

long

getCollectionTime

()

Returns the approximate accumulated collection elapsed time
in milliseconds.

- Methods declared in interface java.lang.management.

MemoryManagerMXBean

getMemoryPoolNames

,

getName

,

isValid

- Methods declared in interface java.lang.management.

PlatformManagedObject

getObjectName

---

#### Method Summary

Returns the total number of collections that have occurred.

Returns the approximate accumulated collection elapsed time
in milliseconds.

Methods declared in interface java.lang.management.

MemoryManagerMXBean

getMemoryPoolNames

,

getName

,

isValid

---

#### Methods declared in interface java.lang.management. MemoryManagerMXBean

Methods declared in interface java.lang.management.

PlatformManagedObject

getObjectName

---

#### Methods declared in interface java.lang.management. PlatformManagedObject

============ METHOD DETAIL ==========

- Method Detail

- getCollectionCount

```java
long getCollectionCount()
```

Returns the total number of collections that have occurred.
This method returns

-1

if the collection count is undefined for
this collector.

**Returns:** the total number of collections that have occurred.

- getCollectionTime

```java
long getCollectionTime()
```

Returns the approximate accumulated collection elapsed time
in milliseconds. This method returns

-1

if the collection
elapsed time is undefined for this collector.

The Java virtual machine implementation may use a high resolution
timer to measure the elapsed time. This method may return the
same value even if the collection count has been incremented
if the collection elapsed time is very short.

**Returns:** the approximate accumulated collection elapsed time
in milliseconds.

Method Detail

- getCollectionCount

```java
long getCollectionCount()
```

Returns the total number of collections that have occurred.
This method returns

-1

if the collection count is undefined for
this collector.

**Returns:** the total number of collections that have occurred.

- getCollectionTime

```java
long getCollectionTime()
```

Returns the approximate accumulated collection elapsed time
in milliseconds. This method returns

-1

if the collection
elapsed time is undefined for this collector.

The Java virtual machine implementation may use a high resolution
timer to measure the elapsed time. This method may return the
same value even if the collection count has been incremented
if the collection elapsed time is very short.

**Returns:** the approximate accumulated collection elapsed time
in milliseconds.

---

#### Method Detail

getCollectionCount

```java
long getCollectionCount()
```

Returns the total number of collections that have occurred.
This method returns

-1

if the collection count is undefined for
this collector.

**Returns:** the total number of collections that have occurred.

---

#### getCollectionCount

long getCollectionCount()

Returns the total number of collections that have occurred.
This method returns

-1

if the collection count is undefined for
this collector.

getCollectionTime

```java
long getCollectionTime()
```

Returns the approximate accumulated collection elapsed time
in milliseconds. This method returns

-1

if the collection
elapsed time is undefined for this collector.

The Java virtual machine implementation may use a high resolution
timer to measure the elapsed time. This method may return the
same value even if the collection count has been incremented
if the collection elapsed time is very short.

**Returns:** the approximate accumulated collection elapsed time
in milliseconds.

---

#### getCollectionTime

long getCollectionTime()

Returns the approximate accumulated collection elapsed time
in milliseconds. This method returns

-1

if the collection
elapsed time is undefined for this collector.

The Java virtual machine implementation may use a high resolution
timer to measure the elapsed time. This method may return the
same value even if the collection count has been incremented
if the collection elapsed time is very short.

The Java virtual machine implementation may use a high resolution
timer to measure the elapsed time. This method may return the
same value even if the collection count has been incremented
if the collection elapsed time is very short.

---

