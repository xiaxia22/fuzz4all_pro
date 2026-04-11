# Interface UnixOperatingSystemMXBean

**Source:** `jdk.management\com\sun\management\UnixOperatingSystemMXBean.html`

### Class Description

```java
public interface
UnixOperatingSystemMXBean

extends
OperatingSystemMXBean
```

Platform-specific management interface for the Unix
operating system on which the Java virtual machine is running.

**All Superinterfaces:** OperatingSystemMXBean

,

OperatingSystemMXBean

,

PlatformManagedObject

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### long getOpenFileDescriptorCount()

Returns the number of open file descriptors.

**Returns:**
- the number of open file descriptors.

---

#### long getMaxFileDescriptorCount()

Returns the maximum number of file descriptors.

**Returns:**
- the maximum number of file descriptors.

---

### Additional Sections

#### Interface UnixOperatingSystemMXBean

**All Superinterfaces:** OperatingSystemMXBean

,

OperatingSystemMXBean

,

PlatformManagedObject

```java
public interface
UnixOperatingSystemMXBean

extends
OperatingSystemMXBean
```

Platform-specific management interface for the Unix
operating system on which the Java virtual machine is running.

**Since:** 1.5

public interface

UnixOperatingSystemMXBean

extends

OperatingSystemMXBean

Platform-specific management interface for the Unix
operating system on which the Java virtual machine is running.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

long

getMaxFileDescriptorCount

()

Returns the maximum number of file descriptors.

long

getOpenFileDescriptorCount

()

Returns the number of open file descriptors.

- Methods declared in interface com.sun.management.

OperatingSystemMXBean

getCommittedVirtualMemorySize

,

getFreePhysicalMemorySize

,

getFreeSwapSpaceSize

,

getProcessCpuLoad

,

getProcessCpuTime

,

getSystemCpuLoad

,

getTotalPhysicalMemorySize

,

getTotalSwapSpaceSize

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

getMaxFileDescriptorCount

()

Returns the maximum number of file descriptors.

long

getOpenFileDescriptorCount

()

Returns the number of open file descriptors.

- Methods declared in interface com.sun.management.

OperatingSystemMXBean

getCommittedVirtualMemorySize

,

getFreePhysicalMemorySize

,

getFreeSwapSpaceSize

,

getProcessCpuLoad

,

getProcessCpuTime

,

getSystemCpuLoad

,

getTotalPhysicalMemorySize

,

getTotalSwapSpaceSize

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

Returns the maximum number of file descriptors.

Returns the number of open file descriptors.

Methods declared in interface com.sun.management.

OperatingSystemMXBean

getCommittedVirtualMemorySize

,

getFreePhysicalMemorySize

,

getFreeSwapSpaceSize

,

getProcessCpuLoad

,

getProcessCpuTime

,

getSystemCpuLoad

,

getTotalPhysicalMemorySize

,

getTotalSwapSpaceSize

---

#### Methods declared in interface com.sun.management. OperatingSystemMXBean

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

- getOpenFileDescriptorCount

```java
long getOpenFileDescriptorCount()
```

Returns the number of open file descriptors.

**Returns:** the number of open file descriptors.

- getMaxFileDescriptorCount

```java
long getMaxFileDescriptorCount()
```

Returns the maximum number of file descriptors.

**Returns:** the maximum number of file descriptors.

Method Detail

- getOpenFileDescriptorCount

```java
long getOpenFileDescriptorCount()
```

Returns the number of open file descriptors.

**Returns:** the number of open file descriptors.

- getMaxFileDescriptorCount

```java
long getMaxFileDescriptorCount()
```

Returns the maximum number of file descriptors.

**Returns:** the maximum number of file descriptors.

---

#### Method Detail

getOpenFileDescriptorCount

```java
long getOpenFileDescriptorCount()
```

Returns the number of open file descriptors.

**Returns:** the number of open file descriptors.

---

#### getOpenFileDescriptorCount

long getOpenFileDescriptorCount()

Returns the number of open file descriptors.

getMaxFileDescriptorCount

```java
long getMaxFileDescriptorCount()
```

Returns the maximum number of file descriptors.

**Returns:** the maximum number of file descriptors.

---

#### getMaxFileDescriptorCount

long getMaxFileDescriptorCount()

Returns the maximum number of file descriptors.

---

