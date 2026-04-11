# Interface OperatingSystemMXBean

**Source:** `jdk.management\com\sun\management\OperatingSystemMXBean.html`

### Class Description

```java
public interface
OperatingSystemMXBean

extends
OperatingSystemMXBean
```

Platform-specific management interface for the operating system
on which the Java virtual machine is running.

The

OperatingSystemMXBean

object returned by

ManagementFactory.getOperatingSystemMXBean()

is an instance of the implementation class of this interface
or

UnixOperatingSystemMXBean

interface depending on
its underlying operating system.

**All Superinterfaces:** OperatingSystemMXBean

,

PlatformManagedObject

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### long getCommittedVirtualMemorySize()

Returns the amount of virtual memory that is guaranteed to
be available to the running process in bytes,
or

-1

if this operation is not supported.

**Returns:**
- the amount of virtual memory that is guaranteed to
be available to the running process in bytes,
or

-1

if this operation is not supported.

---

#### long getTotalSwapSpaceSize()

Returns the total amount of swap space in bytes.

**Returns:**
- the total amount of swap space in bytes.

---

#### long getFreeSwapSpaceSize()

Returns the amount of free swap space in bytes.

**Returns:**
- the amount of free swap space in bytes.

---

#### long getProcessCpuTime()

Returns the CPU time used by the process on which the Java
virtual machine is running in nanoseconds. The returned value
is of nanoseconds precision but not necessarily nanoseconds
accuracy. This method returns

-1

if the
the platform does not support this operation.

**Returns:**
- the CPU time used by the process in nanoseconds,
or

-1

if this operation is not supported.

---

#### long getFreePhysicalMemorySize()

Returns the amount of free physical memory in bytes.

**Returns:**
- the amount of free physical memory in bytes.

---

#### long getTotalPhysicalMemorySize()

Returns the total amount of physical memory in bytes.

**Returns:**
- the total amount of physical memory in bytes.

---

#### double getSystemCpuLoad()

Returns the "recent cpu usage" for the whole system. This value is a
double in the [0.0,1.0] interval. A value of 0.0 means that all CPUs
were idle during the recent period of time observed, while a value
of 1.0 means that all CPUs were actively running 100% of the time
during the recent period being observed. All values betweens 0.0 and
1.0 are possible depending of the activities going on in the system.
If the system recent cpu usage is not available, the method returns a
negative value.

**Returns:**
- the "recent cpu usage" for the whole system; a negative
value if not available.

**Since:**
- 1.7

---

#### double getProcessCpuLoad()

Returns the "recent cpu usage" for the Java Virtual Machine process.
This value is a double in the [0.0,1.0] interval. A value of 0.0 means
that none of the CPUs were running threads from the JVM process during
the recent period of time observed, while a value of 1.0 means that all
CPUs were actively running threads from the JVM 100% of the time
during the recent period being observed. Threads from the JVM include
the application threads as well as the JVM internal threads. All values
betweens 0.0 and 1.0 are possible depending of the activities going on
in the JVM process and the whole system. If the Java Virtual Machine
recent CPU usage is not available, the method returns a negative value.

**Returns:**
- the "recent cpu usage" for the Java Virtual Machine process;
a negative value if not available.

**Since:**
- 1.7

---

### Additional Sections

#### Interface OperatingSystemMXBean

**All Superinterfaces:** OperatingSystemMXBean

,

PlatformManagedObject

**All Known Subinterfaces:** UnixOperatingSystemMXBean

```java
public interface
OperatingSystemMXBean

extends
OperatingSystemMXBean
```

Platform-specific management interface for the operating system
on which the Java virtual machine is running.

The

OperatingSystemMXBean

object returned by

ManagementFactory.getOperatingSystemMXBean()

is an instance of the implementation class of this interface
or

UnixOperatingSystemMXBean

interface depending on
its underlying operating system.

**Since:** 1.5

public interface

OperatingSystemMXBean

extends

OperatingSystemMXBean

Platform-specific management interface for the operating system
on which the Java virtual machine is running.

The

OperatingSystemMXBean

object returned by

ManagementFactory.getOperatingSystemMXBean()

is an instance of the implementation class of this interface
or

UnixOperatingSystemMXBean

interface depending on
its underlying operating system.

The

OperatingSystemMXBean

object returned by

ManagementFactory.getOperatingSystemMXBean()

is an instance of the implementation class of this interface
or

UnixOperatingSystemMXBean

interface depending on
its underlying operating system.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

long

getCommittedVirtualMemorySize

()

Returns the amount of virtual memory that is guaranteed to
be available to the running process in bytes,
or

-1

if this operation is not supported.

long

getFreePhysicalMemorySize

()

Returns the amount of free physical memory in bytes.

long

getFreeSwapSpaceSize

()

Returns the amount of free swap space in bytes.

double

getProcessCpuLoad

()

Returns the "recent cpu usage" for the Java Virtual Machine process.

long

getProcessCpuTime

()

Returns the CPU time used by the process on which the Java
virtual machine is running in nanoseconds.

double

getSystemCpuLoad

()

Returns the "recent cpu usage" for the whole system.

long

getTotalPhysicalMemorySize

()

Returns the total amount of physical memory in bytes.

long

getTotalSwapSpaceSize

()

Returns the total amount of swap space in bytes.

- Methods declared in interface java.lang.management.

OperatingSystemMXBean

getArch

,

getAvailableProcessors

,

getName

,

getSystemLoadAverage

,

getVersion

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

getCommittedVirtualMemorySize

()

Returns the amount of virtual memory that is guaranteed to
be available to the running process in bytes,
or

-1

if this operation is not supported.

long

getFreePhysicalMemorySize

()

Returns the amount of free physical memory in bytes.

long

getFreeSwapSpaceSize

()

Returns the amount of free swap space in bytes.

double

getProcessCpuLoad

()

Returns the "recent cpu usage" for the Java Virtual Machine process.

long

getProcessCpuTime

()

Returns the CPU time used by the process on which the Java
virtual machine is running in nanoseconds.

double

getSystemCpuLoad

()

Returns the "recent cpu usage" for the whole system.

long

getTotalPhysicalMemorySize

()

Returns the total amount of physical memory in bytes.

long

getTotalSwapSpaceSize

()

Returns the total amount of swap space in bytes.

- Methods declared in interface java.lang.management.

OperatingSystemMXBean

getArch

,

getAvailableProcessors

,

getName

,

getSystemLoadAverage

,

getVersion

- Methods declared in interface java.lang.management.

PlatformManagedObject

getObjectName

---

#### Method Summary

Returns the amount of virtual memory that is guaranteed to
be available to the running process in bytes,
or

-1

if this operation is not supported.

Returns the amount of free physical memory in bytes.

Returns the amount of free swap space in bytes.

Returns the "recent cpu usage" for the Java Virtual Machine process.

Returns the CPU time used by the process on which the Java
virtual machine is running in nanoseconds.

Returns the "recent cpu usage" for the whole system.

Returns the total amount of physical memory in bytes.

Returns the total amount of swap space in bytes.

Methods declared in interface java.lang.management.

OperatingSystemMXBean

getArch

,

getAvailableProcessors

,

getName

,

getSystemLoadAverage

,

getVersion

---

#### Methods declared in interface java.lang.management. OperatingSystemMXBean

Methods declared in interface java.lang.management.

PlatformManagedObject

getObjectName

---

#### Methods declared in interface java.lang.management. PlatformManagedObject

============ METHOD DETAIL ==========

- Method Detail

- getCommittedVirtualMemorySize

```java
long getCommittedVirtualMemorySize()
```

Returns the amount of virtual memory that is guaranteed to
be available to the running process in bytes,
or

-1

if this operation is not supported.

**Returns:** the amount of virtual memory that is guaranteed to
be available to the running process in bytes,
or

-1

if this operation is not supported.

- getTotalSwapSpaceSize

```java
long getTotalSwapSpaceSize()
```

Returns the total amount of swap space in bytes.

**Returns:** the total amount of swap space in bytes.

- getFreeSwapSpaceSize

```java
long getFreeSwapSpaceSize()
```

Returns the amount of free swap space in bytes.

**Returns:** the amount of free swap space in bytes.

- getProcessCpuTime

```java
long getProcessCpuTime()
```

Returns the CPU time used by the process on which the Java
virtual machine is running in nanoseconds. The returned value
is of nanoseconds precision but not necessarily nanoseconds
accuracy. This method returns

-1

if the
the platform does not support this operation.

**Returns:** the CPU time used by the process in nanoseconds,
or

-1

if this operation is not supported.

- getFreePhysicalMemorySize

```java
long getFreePhysicalMemorySize()
```

Returns the amount of free physical memory in bytes.

**Returns:** the amount of free physical memory in bytes.

- getTotalPhysicalMemorySize

```java
long getTotalPhysicalMemorySize()
```

Returns the total amount of physical memory in bytes.

**Returns:** the total amount of physical memory in bytes.

- getSystemCpuLoad

```java
double getSystemCpuLoad()
```

Returns the "recent cpu usage" for the whole system. This value is a
double in the [0.0,1.0] interval. A value of 0.0 means that all CPUs
were idle during the recent period of time observed, while a value
of 1.0 means that all CPUs were actively running 100% of the time
during the recent period being observed. All values betweens 0.0 and
1.0 are possible depending of the activities going on in the system.
If the system recent cpu usage is not available, the method returns a
negative value.

**Returns:** the "recent cpu usage" for the whole system; a negative
value if not available.
**Since:** 1.7

- getProcessCpuLoad

```java
double getProcessCpuLoad()
```

Returns the "recent cpu usage" for the Java Virtual Machine process.
This value is a double in the [0.0,1.0] interval. A value of 0.0 means
that none of the CPUs were running threads from the JVM process during
the recent period of time observed, while a value of 1.0 means that all
CPUs were actively running threads from the JVM 100% of the time
during the recent period being observed. Threads from the JVM include
the application threads as well as the JVM internal threads. All values
betweens 0.0 and 1.0 are possible depending of the activities going on
in the JVM process and the whole system. If the Java Virtual Machine
recent CPU usage is not available, the method returns a negative value.

**Returns:** the "recent cpu usage" for the Java Virtual Machine process;
a negative value if not available.
**Since:** 1.7

Method Detail

- getCommittedVirtualMemorySize

```java
long getCommittedVirtualMemorySize()
```

Returns the amount of virtual memory that is guaranteed to
be available to the running process in bytes,
or

-1

if this operation is not supported.

**Returns:** the amount of virtual memory that is guaranteed to
be available to the running process in bytes,
or

-1

if this operation is not supported.

- getTotalSwapSpaceSize

```java
long getTotalSwapSpaceSize()
```

Returns the total amount of swap space in bytes.

**Returns:** the total amount of swap space in bytes.

- getFreeSwapSpaceSize

```java
long getFreeSwapSpaceSize()
```

Returns the amount of free swap space in bytes.

**Returns:** the amount of free swap space in bytes.

- getProcessCpuTime

```java
long getProcessCpuTime()
```

Returns the CPU time used by the process on which the Java
virtual machine is running in nanoseconds. The returned value
is of nanoseconds precision but not necessarily nanoseconds
accuracy. This method returns

-1

if the
the platform does not support this operation.

**Returns:** the CPU time used by the process in nanoseconds,
or

-1

if this operation is not supported.

- getFreePhysicalMemorySize

```java
long getFreePhysicalMemorySize()
```

Returns the amount of free physical memory in bytes.

**Returns:** the amount of free physical memory in bytes.

- getTotalPhysicalMemorySize

```java
long getTotalPhysicalMemorySize()
```

Returns the total amount of physical memory in bytes.

**Returns:** the total amount of physical memory in bytes.

- getSystemCpuLoad

```java
double getSystemCpuLoad()
```

Returns the "recent cpu usage" for the whole system. This value is a
double in the [0.0,1.0] interval. A value of 0.0 means that all CPUs
were idle during the recent period of time observed, while a value
of 1.0 means that all CPUs were actively running 100% of the time
during the recent period being observed. All values betweens 0.0 and
1.0 are possible depending of the activities going on in the system.
If the system recent cpu usage is not available, the method returns a
negative value.

**Returns:** the "recent cpu usage" for the whole system; a negative
value if not available.
**Since:** 1.7

- getProcessCpuLoad

```java
double getProcessCpuLoad()
```

Returns the "recent cpu usage" for the Java Virtual Machine process.
This value is a double in the [0.0,1.0] interval. A value of 0.0 means
that none of the CPUs were running threads from the JVM process during
the recent period of time observed, while a value of 1.0 means that all
CPUs were actively running threads from the JVM 100% of the time
during the recent period being observed. Threads from the JVM include
the application threads as well as the JVM internal threads. All values
betweens 0.0 and 1.0 are possible depending of the activities going on
in the JVM process and the whole system. If the Java Virtual Machine
recent CPU usage is not available, the method returns a negative value.

**Returns:** the "recent cpu usage" for the Java Virtual Machine process;
a negative value if not available.
**Since:** 1.7

---

#### Method Detail

getCommittedVirtualMemorySize

```java
long getCommittedVirtualMemorySize()
```

Returns the amount of virtual memory that is guaranteed to
be available to the running process in bytes,
or

-1

if this operation is not supported.

**Returns:** the amount of virtual memory that is guaranteed to
be available to the running process in bytes,
or

-1

if this operation is not supported.

---

#### getCommittedVirtualMemorySize

long getCommittedVirtualMemorySize()

Returns the amount of virtual memory that is guaranteed to
be available to the running process in bytes,
or

-1

if this operation is not supported.

getTotalSwapSpaceSize

```java
long getTotalSwapSpaceSize()
```

Returns the total amount of swap space in bytes.

**Returns:** the total amount of swap space in bytes.

---

#### getTotalSwapSpaceSize

long getTotalSwapSpaceSize()

Returns the total amount of swap space in bytes.

getFreeSwapSpaceSize

```java
long getFreeSwapSpaceSize()
```

Returns the amount of free swap space in bytes.

**Returns:** the amount of free swap space in bytes.

---

#### getFreeSwapSpaceSize

long getFreeSwapSpaceSize()

Returns the amount of free swap space in bytes.

getProcessCpuTime

```java
long getProcessCpuTime()
```

Returns the CPU time used by the process on which the Java
virtual machine is running in nanoseconds. The returned value
is of nanoseconds precision but not necessarily nanoseconds
accuracy. This method returns

-1

if the
the platform does not support this operation.

**Returns:** the CPU time used by the process in nanoseconds,
or

-1

if this operation is not supported.

---

#### getProcessCpuTime

long getProcessCpuTime()

Returns the CPU time used by the process on which the Java
virtual machine is running in nanoseconds. The returned value
is of nanoseconds precision but not necessarily nanoseconds
accuracy. This method returns

-1

if the
the platform does not support this operation.

getFreePhysicalMemorySize

```java
long getFreePhysicalMemorySize()
```

Returns the amount of free physical memory in bytes.

**Returns:** the amount of free physical memory in bytes.

---

#### getFreePhysicalMemorySize

long getFreePhysicalMemorySize()

Returns the amount of free physical memory in bytes.

getTotalPhysicalMemorySize

```java
long getTotalPhysicalMemorySize()
```

Returns the total amount of physical memory in bytes.

**Returns:** the total amount of physical memory in bytes.

---

#### getTotalPhysicalMemorySize

long getTotalPhysicalMemorySize()

Returns the total amount of physical memory in bytes.

getSystemCpuLoad

```java
double getSystemCpuLoad()
```

Returns the "recent cpu usage" for the whole system. This value is a
double in the [0.0,1.0] interval. A value of 0.0 means that all CPUs
were idle during the recent period of time observed, while a value
of 1.0 means that all CPUs were actively running 100% of the time
during the recent period being observed. All values betweens 0.0 and
1.0 are possible depending of the activities going on in the system.
If the system recent cpu usage is not available, the method returns a
negative value.

**Returns:** the "recent cpu usage" for the whole system; a negative
value if not available.
**Since:** 1.7

---

#### getSystemCpuLoad

double getSystemCpuLoad()

Returns the "recent cpu usage" for the whole system. This value is a
double in the [0.0,1.0] interval. A value of 0.0 means that all CPUs
were idle during the recent period of time observed, while a value
of 1.0 means that all CPUs were actively running 100% of the time
during the recent period being observed. All values betweens 0.0 and
1.0 are possible depending of the activities going on in the system.
If the system recent cpu usage is not available, the method returns a
negative value.

getProcessCpuLoad

```java
double getProcessCpuLoad()
```

Returns the "recent cpu usage" for the Java Virtual Machine process.
This value is a double in the [0.0,1.0] interval. A value of 0.0 means
that none of the CPUs were running threads from the JVM process during
the recent period of time observed, while a value of 1.0 means that all
CPUs were actively running threads from the JVM 100% of the time
during the recent period being observed. Threads from the JVM include
the application threads as well as the JVM internal threads. All values
betweens 0.0 and 1.0 are possible depending of the activities going on
in the JVM process and the whole system. If the Java Virtual Machine
recent CPU usage is not available, the method returns a negative value.

**Returns:** the "recent cpu usage" for the Java Virtual Machine process;
a negative value if not available.
**Since:** 1.7

---

#### getProcessCpuLoad

double getProcessCpuLoad()

Returns the "recent cpu usage" for the Java Virtual Machine process.
This value is a double in the [0.0,1.0] interval. A value of 0.0 means
that none of the CPUs were running threads from the JVM process during
the recent period of time observed, while a value of 1.0 means that all
CPUs were actively running threads from the JVM 100% of the time
during the recent period being observed. Threads from the JVM include
the application threads as well as the JVM internal threads. All values
betweens 0.0 and 1.0 are possible depending of the activities going on
in the JVM process and the whole system. If the Java Virtual Machine
recent CPU usage is not available, the method returns a negative value.

---

