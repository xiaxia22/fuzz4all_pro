# Interface PlatformManagedObject

**Source:** `java.management\java\lang\management\PlatformManagedObject.html`

### Class Description

```java
public interface
PlatformManagedObject
```

A platform managed object is a

JMX MXBean

for monitoring and managing a component in the Java platform.
Each platform managed object has a unique

object name

for the

platform MBeanServer

access.
All platform MXBeans will implement this interface.

Note:
The platform MXBean interfaces (i.e. all subinterfaces
of

PlatformManagedObject

) are implemented
by the Java platform only. New methods may be added in these interfaces
in future Java SE releases.
In addition, this

PlatformManagedObject

interface is only
intended for the management interfaces for the platform to extend but
not for applications.

**All Known Subinterfaces:** BufferPoolMXBean

,

ClassLoadingMXBean

,

CompilationMXBean

,

FlightRecorderMXBean

,

GarbageCollectorMXBean

,

GarbageCollectorMXBean

,

HotSpotDiagnosticMXBean

,

MemoryManagerMXBean

,

MemoryMXBean

,

MemoryPoolMXBean

,

OperatingSystemMXBean

,

OperatingSystemMXBean

,

PlatformLoggingMXBean

,

RuntimeMXBean

,

ThreadMXBean

,

ThreadMXBean

,

UnixOperatingSystemMXBean

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### ObjectName
getObjectName()

Returns an

ObjectName

instance representing
the object name of this platform managed object.

**Returns:**
- an

ObjectName

instance representing
the object name of this platform managed object.

---

### Additional Sections

#### Interface PlatformManagedObject

**All Known Subinterfaces:** BufferPoolMXBean

,

ClassLoadingMXBean

,

CompilationMXBean

,

FlightRecorderMXBean

,

GarbageCollectorMXBean

,

GarbageCollectorMXBean

,

HotSpotDiagnosticMXBean

,

MemoryManagerMXBean

,

MemoryMXBean

,

MemoryPoolMXBean

,

OperatingSystemMXBean

,

OperatingSystemMXBean

,

PlatformLoggingMXBean

,

RuntimeMXBean

,

ThreadMXBean

,

ThreadMXBean

,

UnixOperatingSystemMXBean

```java
public interface
PlatformManagedObject
```

A platform managed object is a

JMX MXBean

for monitoring and managing a component in the Java platform.
Each platform managed object has a unique

object name

for the

platform MBeanServer

access.
All platform MXBeans will implement this interface.

Note:
The platform MXBean interfaces (i.e. all subinterfaces
of

PlatformManagedObject

) are implemented
by the Java platform only. New methods may be added in these interfaces
in future Java SE releases.
In addition, this

PlatformManagedObject

interface is only
intended for the management interfaces for the platform to extend but
not for applications.

**Since:** 1.7
**See Also:** ManagementFactory

public interface

PlatformManagedObject

A platform managed object is a

JMX MXBean

for monitoring and managing a component in the Java platform.
Each platform managed object has a unique

object name

for the

platform MBeanServer

access.
All platform MXBeans will implement this interface.

Note:
The platform MXBean interfaces (i.e. all subinterfaces
of

PlatformManagedObject

) are implemented
by the Java platform only. New methods may be added in these interfaces
in future Java SE releases.
In addition, this

PlatformManagedObject

interface is only
intended for the management interfaces for the platform to extend but
not for applications.

Note:
The platform MXBean interfaces (i.e. all subinterfaces
of

PlatformManagedObject

) are implemented
by the Java platform only. New methods may be added in these interfaces
in future Java SE releases.
In addition, this

PlatformManagedObject

interface is only
intended for the management interfaces for the platform to extend but
not for applications.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

ObjectName

getObjectName

()

Returns an

ObjectName

instance representing
the object name of this platform managed object.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

ObjectName

getObjectName

()

Returns an

ObjectName

instance representing
the object name of this platform managed object.

---

#### Method Summary

Returns an

ObjectName

instance representing
the object name of this platform managed object.

============ METHOD DETAIL ==========

- Method Detail

- getObjectName

```java
ObjectName
getObjectName()
```

Returns an

ObjectName

instance representing
the object name of this platform managed object.

**Returns:** an

ObjectName

instance representing
the object name of this platform managed object.

Method Detail

- getObjectName

```java
ObjectName
getObjectName()
```

Returns an

ObjectName

instance representing
the object name of this platform managed object.

**Returns:** an

ObjectName

instance representing
the object name of this platform managed object.

---

#### Method Detail

getObjectName

```java
ObjectName
getObjectName()
```

Returns an

ObjectName

instance representing
the object name of this platform managed object.

**Returns:** an

ObjectName

instance representing
the object name of this platform managed object.

---

#### getObjectName

ObjectName

getObjectName()

Returns an

ObjectName

instance representing
the object name of this platform managed object.

---

