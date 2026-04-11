# Interface OperatingSystemMXBean

**Source:** `java.management\java\lang\management\OperatingSystemMXBean.html`

### Class Description

```java
public interface
OperatingSystemMXBean

extends
PlatformManagedObject
```

The management interface for the operating system on which
the Java virtual machine is running.

A Java virtual machine has a single instance of the implementation
class of this interface. This instance implementing this interface is
an

MXBean

that can be obtained by calling
the

ManagementFactory.getOperatingSystemMXBean()

method or
from the

platform MBeanServer

method.

The

ObjectName

for uniquely identifying the MXBean for
the operating system within an MBeanServer is:

java.lang:type=OperatingSystem

It can be obtained by calling the

PlatformManagedObject.getObjectName()

method.

This interface defines several convenient methods for accessing
system properties about the operating system on which the Java
virtual machine is running.

**All Superinterfaces:** PlatformManagedObject

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### String
getName()

Returns the operating system name.
This method is equivalent to

System.getProperty("os.name")

.

**Returns:**
- the operating system name.

**Throws:**
- SecurityException

- if a security manager exists and its

checkPropertiesAccess

method doesn't allow access
to this system property.

**See Also:**
- SecurityManager.checkPropertyAccess(java.lang.String)

,

System.getProperty(java.lang.String)

---

#### String
getArch()

Returns the operating system architecture.
This method is equivalent to

System.getProperty("os.arch")

.

**Returns:**
- the operating system architecture.

**Throws:**
- SecurityException

- if a security manager exists and its

checkPropertiesAccess

method doesn't allow access
to this system property.

**See Also:**
- SecurityManager.checkPropertyAccess(java.lang.String)

,

System.getProperty(java.lang.String)

---

#### String
getVersion()

Returns the operating system version.
This method is equivalent to

System.getProperty("os.version")

.

**Returns:**
- the operating system version.

**Throws:**
- SecurityException

- if a security manager exists and its

checkPropertiesAccess

method doesn't allow access
to this system property.

**See Also:**
- SecurityManager.checkPropertyAccess(java.lang.String)

,

System.getProperty(java.lang.String)

---

#### int getAvailableProcessors()

Returns the number of processors available to the Java virtual machine.
This method is equivalent to the

Runtime.availableProcessors()

method.

This value may change during a particular invocation of
the virtual machine.

**Returns:**
- the number of processors available to the virtual
machine; never smaller than one.

---

#### double getSystemLoadAverage()

Returns the system load average for the last minute.
The system load average is the sum of the number of runnable entities
queued to the

available processors

and the number of runnable entities running on the available processors
averaged over a period of time.
The way in which the load average is calculated is operating system
specific but is typically a damped time-dependent average.

If the load average is not available, a negative value is returned.

This method is designed to provide a hint about the system load
and may be queried frequently.
The load average may be unavailable on some platform where it is
expensive to implement this method.

**Returns:**
- the system load average; or a negative value if not available.

**Since:**
- 1.6

---

### Additional Sections

#### Interface OperatingSystemMXBean

**All Superinterfaces:** PlatformManagedObject

**All Known Subinterfaces:** OperatingSystemMXBean

,

UnixOperatingSystemMXBean

```java
public interface
OperatingSystemMXBean

extends
PlatformManagedObject
```

The management interface for the operating system on which
the Java virtual machine is running.

A Java virtual machine has a single instance of the implementation
class of this interface. This instance implementing this interface is
an

MXBean

that can be obtained by calling
the

ManagementFactory.getOperatingSystemMXBean()

method or
from the

platform MBeanServer

method.

The

ObjectName

for uniquely identifying the MXBean for
the operating system within an MBeanServer is:

java.lang:type=OperatingSystem

It can be obtained by calling the

PlatformManagedObject.getObjectName()

method.

This interface defines several convenient methods for accessing
system properties about the operating system on which the Java
virtual machine is running.

**Since:** 1.5
**See Also:** ManagementFactory.getPlatformMXBeans(Class)

,

JMX Specification.

,

Ways to Access MXBeans

public interface

OperatingSystemMXBean

extends

PlatformManagedObject

The management interface for the operating system on which
the Java virtual machine is running.

A Java virtual machine has a single instance of the implementation
class of this interface. This instance implementing this interface is
an

MXBean

that can be obtained by calling
the

ManagementFactory.getOperatingSystemMXBean()

method or
from the

platform MBeanServer

method.

The

ObjectName

for uniquely identifying the MXBean for
the operating system within an MBeanServer is:

java.lang:type=OperatingSystem

It can be obtained by calling the

PlatformManagedObject.getObjectName()

method.

This interface defines several convenient methods for accessing
system properties about the operating system on which the Java
virtual machine is running.

A Java virtual machine has a single instance of the implementation
class of this interface. This instance implementing this interface is
an

MXBean

that can be obtained by calling
the

ManagementFactory.getOperatingSystemMXBean()

method or
from the

platform MBeanServer

method.

The

ObjectName

for uniquely identifying the MXBean for
the operating system within an MBeanServer is:

java.lang:type=OperatingSystem

It can be obtained by calling the

PlatformManagedObject.getObjectName()

method.

This interface defines several convenient methods for accessing
system properties about the operating system on which the Java
virtual machine is running.

The

ObjectName

for uniquely identifying the MXBean for
the operating system within an MBeanServer is:

java.lang:type=OperatingSystem

It can be obtained by calling the

PlatformManagedObject.getObjectName()

method.

This interface defines several convenient methods for accessing
system properties about the operating system on which the Java
virtual machine is running.

This interface defines several convenient methods for accessing
system properties about the operating system on which the Java
virtual machine is running.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

String

getArch

()

Returns the operating system architecture.

int

getAvailableProcessors

()

Returns the number of processors available to the Java virtual machine.

String

getName

()

Returns the operating system name.

double

getSystemLoadAverage

()

Returns the system load average for the last minute.

String

getVersion

()

Returns the operating system version.

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

String

getArch

()

Returns the operating system architecture.

int

getAvailableProcessors

()

Returns the number of processors available to the Java virtual machine.

String

getName

()

Returns the operating system name.

double

getSystemLoadAverage

()

Returns the system load average for the last minute.

String

getVersion

()

Returns the operating system version.

- Methods declared in interface java.lang.management.

PlatformManagedObject

getObjectName

---

#### Method Summary

Returns the operating system architecture.

Returns the number of processors available to the Java virtual machine.

Returns the operating system name.

Returns the system load average for the last minute.

Returns the operating system version.

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

Returns the operating system name.
This method is equivalent to

System.getProperty("os.name")

.

**Returns:** the operating system name.
**Throws:** SecurityException

- if a security manager exists and its

checkPropertiesAccess

method doesn't allow access
to this system property.
**See Also:** SecurityManager.checkPropertyAccess(java.lang.String)

,

System.getProperty(java.lang.String)

- getArch

```java
String
getArch()
```

Returns the operating system architecture.
This method is equivalent to

System.getProperty("os.arch")

.

**Returns:** the operating system architecture.
**Throws:** SecurityException

- if a security manager exists and its

checkPropertiesAccess

method doesn't allow access
to this system property.
**See Also:** SecurityManager.checkPropertyAccess(java.lang.String)

,

System.getProperty(java.lang.String)

- getVersion

```java
String
getVersion()
```

Returns the operating system version.
This method is equivalent to

System.getProperty("os.version")

.

**Returns:** the operating system version.
**Throws:** SecurityException

- if a security manager exists and its

checkPropertiesAccess

method doesn't allow access
to this system property.
**See Also:** SecurityManager.checkPropertyAccess(java.lang.String)

,

System.getProperty(java.lang.String)

- getAvailableProcessors

```java
int getAvailableProcessors()
```

Returns the number of processors available to the Java virtual machine.
This method is equivalent to the

Runtime.availableProcessors()

method.

This value may change during a particular invocation of
the virtual machine.

**Returns:** the number of processors available to the virtual
machine; never smaller than one.

- getSystemLoadAverage

```java
double getSystemLoadAverage()
```

Returns the system load average for the last minute.
The system load average is the sum of the number of runnable entities
queued to the

available processors

and the number of runnable entities running on the available processors
averaged over a period of time.
The way in which the load average is calculated is operating system
specific but is typically a damped time-dependent average.

If the load average is not available, a negative value is returned.

This method is designed to provide a hint about the system load
and may be queried frequently.
The load average may be unavailable on some platform where it is
expensive to implement this method.

**Returns:** the system load average; or a negative value if not available.
**Since:** 1.6

Method Detail

- getName

```java
String
getName()
```

Returns the operating system name.
This method is equivalent to

System.getProperty("os.name")

.

**Returns:** the operating system name.
**Throws:** SecurityException

- if a security manager exists and its

checkPropertiesAccess

method doesn't allow access
to this system property.
**See Also:** SecurityManager.checkPropertyAccess(java.lang.String)

,

System.getProperty(java.lang.String)

- getArch

```java
String
getArch()
```

Returns the operating system architecture.
This method is equivalent to

System.getProperty("os.arch")

.

**Returns:** the operating system architecture.
**Throws:** SecurityException

- if a security manager exists and its

checkPropertiesAccess

method doesn't allow access
to this system property.
**See Also:** SecurityManager.checkPropertyAccess(java.lang.String)

,

System.getProperty(java.lang.String)

- getVersion

```java
String
getVersion()
```

Returns the operating system version.
This method is equivalent to

System.getProperty("os.version")

.

**Returns:** the operating system version.
**Throws:** SecurityException

- if a security manager exists and its

checkPropertiesAccess

method doesn't allow access
to this system property.
**See Also:** SecurityManager.checkPropertyAccess(java.lang.String)

,

System.getProperty(java.lang.String)

- getAvailableProcessors

```java
int getAvailableProcessors()
```

Returns the number of processors available to the Java virtual machine.
This method is equivalent to the

Runtime.availableProcessors()

method.

This value may change during a particular invocation of
the virtual machine.

**Returns:** the number of processors available to the virtual
machine; never smaller than one.

- getSystemLoadAverage

```java
double getSystemLoadAverage()
```

Returns the system load average for the last minute.
The system load average is the sum of the number of runnable entities
queued to the

available processors

and the number of runnable entities running on the available processors
averaged over a period of time.
The way in which the load average is calculated is operating system
specific but is typically a damped time-dependent average.

If the load average is not available, a negative value is returned.

This method is designed to provide a hint about the system load
and may be queried frequently.
The load average may be unavailable on some platform where it is
expensive to implement this method.

**Returns:** the system load average; or a negative value if not available.
**Since:** 1.6

---

#### Method Detail

getName

```java
String
getName()
```

Returns the operating system name.
This method is equivalent to

System.getProperty("os.name")

.

**Returns:** the operating system name.
**Throws:** SecurityException

- if a security manager exists and its

checkPropertiesAccess

method doesn't allow access
to this system property.
**See Also:** SecurityManager.checkPropertyAccess(java.lang.String)

,

System.getProperty(java.lang.String)

---

#### getName

String

getName()

Returns the operating system name.
This method is equivalent to

System.getProperty("os.name")

.

getArch

```java
String
getArch()
```

Returns the operating system architecture.
This method is equivalent to

System.getProperty("os.arch")

.

**Returns:** the operating system architecture.
**Throws:** SecurityException

- if a security manager exists and its

checkPropertiesAccess

method doesn't allow access
to this system property.
**See Also:** SecurityManager.checkPropertyAccess(java.lang.String)

,

System.getProperty(java.lang.String)

---

#### getArch

String

getArch()

Returns the operating system architecture.
This method is equivalent to

System.getProperty("os.arch")

.

getVersion

```java
String
getVersion()
```

Returns the operating system version.
This method is equivalent to

System.getProperty("os.version")

.

**Returns:** the operating system version.
**Throws:** SecurityException

- if a security manager exists and its

checkPropertiesAccess

method doesn't allow access
to this system property.
**See Also:** SecurityManager.checkPropertyAccess(java.lang.String)

,

System.getProperty(java.lang.String)

---

#### getVersion

String

getVersion()

Returns the operating system version.
This method is equivalent to

System.getProperty("os.version")

.

getAvailableProcessors

```java
int getAvailableProcessors()
```

Returns the number of processors available to the Java virtual machine.
This method is equivalent to the

Runtime.availableProcessors()

method.

This value may change during a particular invocation of
the virtual machine.

**Returns:** the number of processors available to the virtual
machine; never smaller than one.

---

#### getAvailableProcessors

int getAvailableProcessors()

Returns the number of processors available to the Java virtual machine.
This method is equivalent to the

Runtime.availableProcessors()

method.

This value may change during a particular invocation of
the virtual machine.

This value may change during a particular invocation of
the virtual machine.

getSystemLoadAverage

```java
double getSystemLoadAverage()
```

Returns the system load average for the last minute.
The system load average is the sum of the number of runnable entities
queued to the

available processors

and the number of runnable entities running on the available processors
averaged over a period of time.
The way in which the load average is calculated is operating system
specific but is typically a damped time-dependent average.

If the load average is not available, a negative value is returned.

This method is designed to provide a hint about the system load
and may be queried frequently.
The load average may be unavailable on some platform where it is
expensive to implement this method.

**Returns:** the system load average; or a negative value if not available.
**Since:** 1.6

---

#### getSystemLoadAverage

double getSystemLoadAverage()

Returns the system load average for the last minute.
The system load average is the sum of the number of runnable entities
queued to the

available processors

and the number of runnable entities running on the available processors
averaged over a period of time.
The way in which the load average is calculated is operating system
specific but is typically a damped time-dependent average.

If the load average is not available, a negative value is returned.

This method is designed to provide a hint about the system load
and may be queried frequently.
The load average may be unavailable on some platform where it is
expensive to implement this method.

If the load average is not available, a negative value is returned.

This method is designed to provide a hint about the system load
and may be queried frequently.
The load average may be unavailable on some platform where it is
expensive to implement this method.

This method is designed to provide a hint about the system load
and may be queried frequently.
The load average may be unavailable on some platform where it is
expensive to implement this method.

---

