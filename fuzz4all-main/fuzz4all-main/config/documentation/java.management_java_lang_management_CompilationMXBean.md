# Interface CompilationMXBean

**Source:** `java.management\java\lang\management\CompilationMXBean.html`

### Class Description

```java
public interface
CompilationMXBean

extends
PlatformManagedObject
```

The management interface for the compilation system of
the Java virtual machine.

A Java virtual machine has a single instance of the implementation
class of this interface. This instance implementing this interface is
an

MXBean

that can be obtained by calling
the

ManagementFactory.getCompilationMXBean()

method or
from the

platform MBeanServer

method.

The

ObjectName

for uniquely identifying the MXBean for
the compilation system within an MBeanServer is:

java.lang:type=Compilation

It can be obtained by calling the

PlatformManagedObject.getObjectName()

method.

**All Superinterfaces:** PlatformManagedObject

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### String
getName()

Returns the name of the Just-in-time (JIT) compiler.

**Returns:**
- the name of the JIT compiler.

---

#### boolean isCompilationTimeMonitoringSupported()

Tests if the Java virtual machine supports the monitoring of
compilation time.

**Returns:**
- true

if the monitoring of compilation time is
supported;

false

otherwise.

---

#### long getTotalCompilationTime()

Returns the approximate accumulated elapsed time (in milliseconds)
spent in compilation.
If multiple threads are used for compilation, this value is
summation of the approximate time that each thread spent in compilation.

This method is optionally supported by the platform.
A Java virtual machine implementation may not support the compilation
time monitoring. The

isCompilationTimeMonitoringSupported()

method can be used to determine if the Java virtual machine
supports this operation.

This value does not indicate the level of performance of
the Java virtual machine and is not intended for performance comparisons
of different virtual machine implementations.
The implementations may have different definitions and different
measurements of the compilation time.

**Returns:**
- Compilation time in milliseconds

**Throws:**
- UnsupportedOperationException

- if the Java
virtual machine does not support
this operation.

---

### Additional Sections

#### Interface CompilationMXBean

**All Superinterfaces:** PlatformManagedObject

```java
public interface
CompilationMXBean

extends
PlatformManagedObject
```

The management interface for the compilation system of
the Java virtual machine.

A Java virtual machine has a single instance of the implementation
class of this interface. This instance implementing this interface is
an

MXBean

that can be obtained by calling
the

ManagementFactory.getCompilationMXBean()

method or
from the

platform MBeanServer

method.

The

ObjectName

for uniquely identifying the MXBean for
the compilation system within an MBeanServer is:

java.lang:type=Compilation

It can be obtained by calling the

PlatformManagedObject.getObjectName()

method.

**Since:** 1.5
**See Also:** ManagementFactory.getPlatformMXBeans(Class)

,

JMX Specification.

,

Ways to Access MXBeans

public interface

CompilationMXBean

extends

PlatformManagedObject

The management interface for the compilation system of
the Java virtual machine.

A Java virtual machine has a single instance of the implementation
class of this interface. This instance implementing this interface is
an

MXBean

that can be obtained by calling
the

ManagementFactory.getCompilationMXBean()

method or
from the

platform MBeanServer

method.

The

ObjectName

for uniquely identifying the MXBean for
the compilation system within an MBeanServer is:

java.lang:type=Compilation

It can be obtained by calling the

PlatformManagedObject.getObjectName()

method.

A Java virtual machine has a single instance of the implementation
class of this interface. This instance implementing this interface is
an

MXBean

that can be obtained by calling
the

ManagementFactory.getCompilationMXBean()

method or
from the

platform MBeanServer

method.

The

ObjectName

for uniquely identifying the MXBean for
the compilation system within an MBeanServer is:

java.lang:type=Compilation

It can be obtained by calling the

PlatformManagedObject.getObjectName()

method.

The

ObjectName

for uniquely identifying the MXBean for
the compilation system within an MBeanServer is:

java.lang:type=Compilation

It can be obtained by calling the

PlatformManagedObject.getObjectName()

method.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

String

getName

()

Returns the name of the Just-in-time (JIT) compiler.

long

getTotalCompilationTime

()

Returns the approximate accumulated elapsed time (in milliseconds)
spent in compilation.

boolean

isCompilationTimeMonitoringSupported

()

Tests if the Java virtual machine supports the monitoring of
compilation time.

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

getName

()

Returns the name of the Just-in-time (JIT) compiler.

long

getTotalCompilationTime

()

Returns the approximate accumulated elapsed time (in milliseconds)
spent in compilation.

boolean

isCompilationTimeMonitoringSupported

()

Tests if the Java virtual machine supports the monitoring of
compilation time.

- Methods declared in interface java.lang.management.

PlatformManagedObject

getObjectName

---

#### Method Summary

Returns the name of the Just-in-time (JIT) compiler.

Returns the approximate accumulated elapsed time (in milliseconds)
spent in compilation.

Tests if the Java virtual machine supports the monitoring of
compilation time.

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

Returns the name of the Just-in-time (JIT) compiler.

**Returns:** the name of the JIT compiler.

- isCompilationTimeMonitoringSupported

```java
boolean isCompilationTimeMonitoringSupported()
```

Tests if the Java virtual machine supports the monitoring of
compilation time.

**Returns:** true

if the monitoring of compilation time is
supported;

false

otherwise.

- getTotalCompilationTime

```java
long getTotalCompilationTime()
```

Returns the approximate accumulated elapsed time (in milliseconds)
spent in compilation.
If multiple threads are used for compilation, this value is
summation of the approximate time that each thread spent in compilation.

This method is optionally supported by the platform.
A Java virtual machine implementation may not support the compilation
time monitoring. The

isCompilationTimeMonitoringSupported()

method can be used to determine if the Java virtual machine
supports this operation.

This value does not indicate the level of performance of
the Java virtual machine and is not intended for performance comparisons
of different virtual machine implementations.
The implementations may have different definitions and different
measurements of the compilation time.

**Returns:** Compilation time in milliseconds
**Throws:** UnsupportedOperationException

- if the Java
virtual machine does not support
this operation.

Method Detail

- getName

```java
String
getName()
```

Returns the name of the Just-in-time (JIT) compiler.

**Returns:** the name of the JIT compiler.

- isCompilationTimeMonitoringSupported

```java
boolean isCompilationTimeMonitoringSupported()
```

Tests if the Java virtual machine supports the monitoring of
compilation time.

**Returns:** true

if the monitoring of compilation time is
supported;

false

otherwise.

- getTotalCompilationTime

```java
long getTotalCompilationTime()
```

Returns the approximate accumulated elapsed time (in milliseconds)
spent in compilation.
If multiple threads are used for compilation, this value is
summation of the approximate time that each thread spent in compilation.

This method is optionally supported by the platform.
A Java virtual machine implementation may not support the compilation
time monitoring. The

isCompilationTimeMonitoringSupported()

method can be used to determine if the Java virtual machine
supports this operation.

This value does not indicate the level of performance of
the Java virtual machine and is not intended for performance comparisons
of different virtual machine implementations.
The implementations may have different definitions and different
measurements of the compilation time.

**Returns:** Compilation time in milliseconds
**Throws:** UnsupportedOperationException

- if the Java
virtual machine does not support
this operation.

---

#### Method Detail

getName

```java
String
getName()
```

Returns the name of the Just-in-time (JIT) compiler.

**Returns:** the name of the JIT compiler.

---

#### getName

String

getName()

Returns the name of the Just-in-time (JIT) compiler.

isCompilationTimeMonitoringSupported

```java
boolean isCompilationTimeMonitoringSupported()
```

Tests if the Java virtual machine supports the monitoring of
compilation time.

**Returns:** true

if the monitoring of compilation time is
supported;

false

otherwise.

---

#### isCompilationTimeMonitoringSupported

boolean isCompilationTimeMonitoringSupported()

Tests if the Java virtual machine supports the monitoring of
compilation time.

getTotalCompilationTime

```java
long getTotalCompilationTime()
```

Returns the approximate accumulated elapsed time (in milliseconds)
spent in compilation.
If multiple threads are used for compilation, this value is
summation of the approximate time that each thread spent in compilation.

This method is optionally supported by the platform.
A Java virtual machine implementation may not support the compilation
time monitoring. The

isCompilationTimeMonitoringSupported()

method can be used to determine if the Java virtual machine
supports this operation.

This value does not indicate the level of performance of
the Java virtual machine and is not intended for performance comparisons
of different virtual machine implementations.
The implementations may have different definitions and different
measurements of the compilation time.

**Returns:** Compilation time in milliseconds
**Throws:** UnsupportedOperationException

- if the Java
virtual machine does not support
this operation.

---

#### getTotalCompilationTime

long getTotalCompilationTime()

Returns the approximate accumulated elapsed time (in milliseconds)
spent in compilation.
If multiple threads are used for compilation, this value is
summation of the approximate time that each thread spent in compilation.

This method is optionally supported by the platform.
A Java virtual machine implementation may not support the compilation
time monitoring. The

isCompilationTimeMonitoringSupported()

method can be used to determine if the Java virtual machine
supports this operation.

This value does not indicate the level of performance of
the Java virtual machine and is not intended for performance comparisons
of different virtual machine implementations.
The implementations may have different definitions and different
measurements of the compilation time.

This method is optionally supported by the platform.
A Java virtual machine implementation may not support the compilation
time monitoring. The

isCompilationTimeMonitoringSupported()

method can be used to determine if the Java virtual machine
supports this operation.

This value does not indicate the level of performance of
the Java virtual machine and is not intended for performance comparisons
of different virtual machine implementations.
The implementations may have different definitions and different
measurements of the compilation time.

This value does not indicate the level of performance of
the Java virtual machine and is not intended for performance comparisons
of different virtual machine implementations.
The implementations may have different definitions and different
measurements of the compilation time.

---

