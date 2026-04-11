# Interface ClassLoadingMXBean

**Source:** `java.management\java\lang\management\ClassLoadingMXBean.html`

### Class Description

```java
public interface
ClassLoadingMXBean

extends
PlatformManagedObject
```

The management interface for the class loading system of
the Java virtual machine.

A Java virtual machine has a single instance of the implementation
class of this interface. This instance implementing this interface is
an

MXBean

that can be obtained by calling
the

ManagementFactory.getClassLoadingMXBean()

method or
from the

platform MBeanServer

.

The

ObjectName

for uniquely identifying the MXBean for
the class loading system within an

MBeanServer

is:

java.lang:type=ClassLoading

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

#### long getTotalLoadedClassCount()

Returns the total number of classes that have been loaded since
the Java virtual machine has started execution.

**Returns:**
- the total number of classes loaded.

---

#### int getLoadedClassCount()

Returns the number of classes that are currently loaded in the
Java virtual machine.

**Returns:**
- the number of currently loaded classes.

---

#### long getUnloadedClassCount()

Returns the total number of classes unloaded since the Java virtual machine
has started execution.

**Returns:**
- the total number of unloaded classes.

---

#### boolean isVerbose()

Tests if the verbose output for the class loading system is enabled.

**Returns:**
- true

if the verbose output for the class loading
system is enabled;

false

otherwise.

---

#### void setVerbose​(boolean value)

Enables or disables the verbose output for the class loading
system. The verbose output information and the output stream
to which the verbose information is emitted are implementation
dependent. Typically, a Java virtual machine implementation
prints a message each time a class file is loaded.

This method can be called by multiple threads concurrently.
Each invocation of this method enables or disables the verbose
output globally.

**Parameters:**
- value

-

true

to enable the verbose output;

false

to disable.

**Throws:**
- SecurityException

- if a security manager
exists and the caller does not have
ManagementPermission("control").

---

### Additional Sections

#### Interface ClassLoadingMXBean

**All Superinterfaces:** PlatformManagedObject

```java
public interface
ClassLoadingMXBean

extends
PlatformManagedObject
```

The management interface for the class loading system of
the Java virtual machine.

A Java virtual machine has a single instance of the implementation
class of this interface. This instance implementing this interface is
an

MXBean

that can be obtained by calling
the

ManagementFactory.getClassLoadingMXBean()

method or
from the

platform MBeanServer

.

The

ObjectName

for uniquely identifying the MXBean for
the class loading system within an

MBeanServer

is:

java.lang:type=ClassLoading

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

ClassLoadingMXBean

extends

PlatformManagedObject

The management interface for the class loading system of
the Java virtual machine.

A Java virtual machine has a single instance of the implementation
class of this interface. This instance implementing this interface is
an

MXBean

that can be obtained by calling
the

ManagementFactory.getClassLoadingMXBean()

method or
from the

platform MBeanServer

.

The

ObjectName

for uniquely identifying the MXBean for
the class loading system within an

MBeanServer

is:

java.lang:type=ClassLoading

It can be obtained by calling the

PlatformManagedObject.getObjectName()

method.

A Java virtual machine has a single instance of the implementation
class of this interface. This instance implementing this interface is
an

MXBean

that can be obtained by calling
the

ManagementFactory.getClassLoadingMXBean()

method or
from the

platform MBeanServer

.

The

ObjectName

for uniquely identifying the MXBean for
the class loading system within an

MBeanServer

is:

java.lang:type=ClassLoading

It can be obtained by calling the

PlatformManagedObject.getObjectName()

method.

The

ObjectName

for uniquely identifying the MXBean for
the class loading system within an

MBeanServer

is:

java.lang:type=ClassLoading

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

int

getLoadedClassCount

()

Returns the number of classes that are currently loaded in the
Java virtual machine.

long

getTotalLoadedClassCount

()

Returns the total number of classes that have been loaded since
the Java virtual machine has started execution.

long

getUnloadedClassCount

()

Returns the total number of classes unloaded since the Java virtual machine
has started execution.

boolean

isVerbose

()

Tests if the verbose output for the class loading system is enabled.

void

setVerbose

​(boolean value)

Enables or disables the verbose output for the class loading
system.

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

int

getLoadedClassCount

()

Returns the number of classes that are currently loaded in the
Java virtual machine.

long

getTotalLoadedClassCount

()

Returns the total number of classes that have been loaded since
the Java virtual machine has started execution.

long

getUnloadedClassCount

()

Returns the total number of classes unloaded since the Java virtual machine
has started execution.

boolean

isVerbose

()

Tests if the verbose output for the class loading system is enabled.

void

setVerbose

​(boolean value)

Enables or disables the verbose output for the class loading
system.

- Methods declared in interface java.lang.management.

PlatformManagedObject

getObjectName

---

#### Method Summary

Returns the number of classes that are currently loaded in the
Java virtual machine.

Returns the total number of classes that have been loaded since
the Java virtual machine has started execution.

Returns the total number of classes unloaded since the Java virtual machine
has started execution.

Tests if the verbose output for the class loading system is enabled.

Enables or disables the verbose output for the class loading
system.

Methods declared in interface java.lang.management.

PlatformManagedObject

getObjectName

---

#### Methods declared in interface java.lang.management. PlatformManagedObject

============ METHOD DETAIL ==========

- Method Detail

- getTotalLoadedClassCount

```java
long getTotalLoadedClassCount()
```

Returns the total number of classes that have been loaded since
the Java virtual machine has started execution.

**Returns:** the total number of classes loaded.

- getLoadedClassCount

```java
int getLoadedClassCount()
```

Returns the number of classes that are currently loaded in the
Java virtual machine.

**Returns:** the number of currently loaded classes.

- getUnloadedClassCount

```java
long getUnloadedClassCount()
```

Returns the total number of classes unloaded since the Java virtual machine
has started execution.

**Returns:** the total number of unloaded classes.

- isVerbose

```java
boolean isVerbose()
```

Tests if the verbose output for the class loading system is enabled.

**Returns:** true

if the verbose output for the class loading
system is enabled;

false

otherwise.

- setVerbose

```java
void setVerbose​(boolean value)
```

Enables or disables the verbose output for the class loading
system. The verbose output information and the output stream
to which the verbose information is emitted are implementation
dependent. Typically, a Java virtual machine implementation
prints a message each time a class file is loaded.

This method can be called by multiple threads concurrently.
Each invocation of this method enables or disables the verbose
output globally.

**Parameters:** value

-

true

to enable the verbose output;

false

to disable.
**Throws:** SecurityException

- if a security manager
exists and the caller does not have
ManagementPermission("control").

Method Detail

- getTotalLoadedClassCount

```java
long getTotalLoadedClassCount()
```

Returns the total number of classes that have been loaded since
the Java virtual machine has started execution.

**Returns:** the total number of classes loaded.

- getLoadedClassCount

```java
int getLoadedClassCount()
```

Returns the number of classes that are currently loaded in the
Java virtual machine.

**Returns:** the number of currently loaded classes.

- getUnloadedClassCount

```java
long getUnloadedClassCount()
```

Returns the total number of classes unloaded since the Java virtual machine
has started execution.

**Returns:** the total number of unloaded classes.

- isVerbose

```java
boolean isVerbose()
```

Tests if the verbose output for the class loading system is enabled.

**Returns:** true

if the verbose output for the class loading
system is enabled;

false

otherwise.

- setVerbose

```java
void setVerbose​(boolean value)
```

Enables or disables the verbose output for the class loading
system. The verbose output information and the output stream
to which the verbose information is emitted are implementation
dependent. Typically, a Java virtual machine implementation
prints a message each time a class file is loaded.

This method can be called by multiple threads concurrently.
Each invocation of this method enables or disables the verbose
output globally.

**Parameters:** value

-

true

to enable the verbose output;

false

to disable.
**Throws:** SecurityException

- if a security manager
exists and the caller does not have
ManagementPermission("control").

---

#### Method Detail

getTotalLoadedClassCount

```java
long getTotalLoadedClassCount()
```

Returns the total number of classes that have been loaded since
the Java virtual machine has started execution.

**Returns:** the total number of classes loaded.

---

#### getTotalLoadedClassCount

long getTotalLoadedClassCount()

Returns the total number of classes that have been loaded since
the Java virtual machine has started execution.

getLoadedClassCount

```java
int getLoadedClassCount()
```

Returns the number of classes that are currently loaded in the
Java virtual machine.

**Returns:** the number of currently loaded classes.

---

#### getLoadedClassCount

int getLoadedClassCount()

Returns the number of classes that are currently loaded in the
Java virtual machine.

getUnloadedClassCount

```java
long getUnloadedClassCount()
```

Returns the total number of classes unloaded since the Java virtual machine
has started execution.

**Returns:** the total number of unloaded classes.

---

#### getUnloadedClassCount

long getUnloadedClassCount()

Returns the total number of classes unloaded since the Java virtual machine
has started execution.

isVerbose

```java
boolean isVerbose()
```

Tests if the verbose output for the class loading system is enabled.

**Returns:** true

if the verbose output for the class loading
system is enabled;

false

otherwise.

---

#### isVerbose

boolean isVerbose()

Tests if the verbose output for the class loading system is enabled.

setVerbose

```java
void setVerbose​(boolean value)
```

Enables or disables the verbose output for the class loading
system. The verbose output information and the output stream
to which the verbose information is emitted are implementation
dependent. Typically, a Java virtual machine implementation
prints a message each time a class file is loaded.

This method can be called by multiple threads concurrently.
Each invocation of this method enables or disables the verbose
output globally.

**Parameters:** value

-

true

to enable the verbose output;

false

to disable.
**Throws:** SecurityException

- if a security manager
exists and the caller does not have
ManagementPermission("control").

---

#### setVerbose

void setVerbose​(boolean value)

Enables or disables the verbose output for the class loading
system. The verbose output information and the output stream
to which the verbose information is emitted are implementation
dependent. Typically, a Java virtual machine implementation
prints a message each time a class file is loaded.

This method can be called by multiple threads concurrently.
Each invocation of this method enables or disables the verbose
output globally.

This method can be called by multiple threads concurrently.
Each invocation of this method enables or disables the verbose
output globally.

---

