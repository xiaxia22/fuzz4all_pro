# Interface GarbageCollectorMXBean

**Source:** `jdk.management\com\sun\management\GarbageCollectorMXBean.html`

### Class Description

```java
public interface
GarbageCollectorMXBean

extends
GarbageCollectorMXBean
```

Platform-specific management interface for a garbage collector
which performs collections in cycles.

This platform extension is only available to the garbage
collection implementation that supports this extension.

**All Superinterfaces:** GarbageCollectorMXBean

,

MemoryManagerMXBean

,

PlatformManagedObject

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### GcInfo
getLastGcInfo()

Returns the GC information about the most recent GC.
This method returns a

GcInfo

.
If no GC information is available,

null

is returned.
The collector-specific attributes, if any, can be obtained
via the

CompositeData

interface.

MBeanServer access:

The mapped type of

GcInfo

is

CompositeData

with attributes specified in

GcInfo

.

**Returns:**
- a

GcInfo

object representing
the most GC information; or

null

if no GC
information available.

---

### Additional Sections

#### Interface GarbageCollectorMXBean

**All Superinterfaces:** GarbageCollectorMXBean

,

MemoryManagerMXBean

,

PlatformManagedObject

```java
public interface
GarbageCollectorMXBean

extends
GarbageCollectorMXBean
```

Platform-specific management interface for a garbage collector
which performs collections in cycles.

This platform extension is only available to the garbage
collection implementation that supports this extension.

**Since:** 1.5

public interface

GarbageCollectorMXBean

extends

GarbageCollectorMXBean

Platform-specific management interface for a garbage collector
which performs collections in cycles.

This platform extension is only available to the garbage
collection implementation that supports this extension.

This platform extension is only available to the garbage
collection implementation that supports this extension.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

GcInfo

getLastGcInfo

()

Returns the GC information about the most recent GC.

- Methods declared in interface java.lang.management.

GarbageCollectorMXBean

getCollectionCount

,

getCollectionTime

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

GcInfo

getLastGcInfo

()

Returns the GC information about the most recent GC.

- Methods declared in interface java.lang.management.

GarbageCollectorMXBean

getCollectionCount

,

getCollectionTime

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

Returns the GC information about the most recent GC.

Methods declared in interface java.lang.management.

GarbageCollectorMXBean

getCollectionCount

,

getCollectionTime

---

#### Methods declared in interface java.lang.management. GarbageCollectorMXBean

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

- getLastGcInfo

```java
GcInfo
getLastGcInfo()
```

Returns the GC information about the most recent GC.
This method returns a

GcInfo

.
If no GC information is available,

null

is returned.
The collector-specific attributes, if any, can be obtained
via the

CompositeData

interface.

MBeanServer access:

The mapped type of

GcInfo

is

CompositeData

with attributes specified in

GcInfo

.

**Returns:** a

GcInfo

object representing
the most GC information; or

null

if no GC
information available.

Method Detail

- getLastGcInfo

```java
GcInfo
getLastGcInfo()
```

Returns the GC information about the most recent GC.
This method returns a

GcInfo

.
If no GC information is available,

null

is returned.
The collector-specific attributes, if any, can be obtained
via the

CompositeData

interface.

MBeanServer access:

The mapped type of

GcInfo

is

CompositeData

with attributes specified in

GcInfo

.

**Returns:** a

GcInfo

object representing
the most GC information; or

null

if no GC
information available.

---

#### Method Detail

getLastGcInfo

```java
GcInfo
getLastGcInfo()
```

Returns the GC information about the most recent GC.
This method returns a

GcInfo

.
If no GC information is available,

null

is returned.
The collector-specific attributes, if any, can be obtained
via the

CompositeData

interface.

MBeanServer access:

The mapped type of

GcInfo

is

CompositeData

with attributes specified in

GcInfo

.

**Returns:** a

GcInfo

object representing
the most GC information; or

null

if no GC
information available.

---

#### getLastGcInfo

GcInfo

getLastGcInfo()

Returns the GC information about the most recent GC.
This method returns a

GcInfo

.
If no GC information is available,

null

is returned.
The collector-specific attributes, if any, can be obtained
via the

CompositeData

interface.

MBeanServer access:

The mapped type of

GcInfo

is

CompositeData

with attributes specified in

GcInfo

.

MBeanServer access:

The mapped type of

GcInfo

is

CompositeData

with attributes specified in

GcInfo

.

---

