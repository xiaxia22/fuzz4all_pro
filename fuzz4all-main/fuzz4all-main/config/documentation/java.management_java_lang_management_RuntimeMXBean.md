# Interface RuntimeMXBean

**Source:** `java.management\java\lang\management\RuntimeMXBean.html`

### Class Description

```java
public interface
RuntimeMXBean

extends
PlatformManagedObject
```

The management interface for the runtime system of
the Java virtual machine.

A Java virtual machine has a single instance of the implementation
class of this interface. This instance implementing this interface is
an

MXBean

that can be obtained by calling
the

ManagementFactory.getRuntimeMXBean()

method or
from the

platform MBeanServer

method.

The

ObjectName

for uniquely identifying the MXBean for
the runtime system within an MBeanServer is:

java.lang:type=Runtime

It can be obtained by calling the

PlatformManagedObject.getObjectName()

method.

This interface defines several convenient methods for accessing
system properties about the Java virtual machine.

**All Superinterfaces:** PlatformManagedObject

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### default long getPid()

Returns the

process ID

representing
the running Java virtual machine.

**Returns:**
- the process ID representing the running Java virtual machine.

**Since:**
- 10

**Implementation Requirements:**
- The default implementation returns

process ID

of the

current process

.

---

#### String
getName()

Returns the name representing the running Java virtual machine.
The returned name string can be any arbitrary string and
a Java virtual machine implementation can choose
to embed platform-specific useful information in the
returned name string. Each running virtual machine could have
a different name.

**Returns:**
- the name representing the running Java virtual machine.

---

#### String
getVmName()

Returns the Java virtual machine implementation name.
This method is equivalent to

System.getProperty("java.vm.name")

.

**Returns:**
- the Java virtual machine implementation name.

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
getVmVendor()

Returns the Java virtual machine implementation vendor.
This method is equivalent to

System.getProperty("java.vm.vendor")

.

**Returns:**
- the Java virtual machine implementation vendor.

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
getVmVersion()

Returns the Java virtual machine implementation version.
This method is equivalent to

System.getProperty("java.vm.version")

.

**Returns:**
- the Java virtual machine implementation version.

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
getSpecName()

Returns the Java virtual machine specification name.
This method is equivalent to

System.getProperty("java.vm.specification.name")

.

**Returns:**
- the Java virtual machine specification name.

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
getSpecVendor()

Returns the Java virtual machine specification vendor.
This method is equivalent to

System.getProperty("java.vm.specification.vendor")

.

**Returns:**
- the Java virtual machine specification vendor.

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
getSpecVersion()

Returns the Java virtual machine specification version.
This method is equivalent to

System.getProperty("java.vm.specification.version")

.

**Returns:**
- the Java virtual machine specification version.

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
getManagementSpecVersion()

Returns the version of the specification for the management interface
implemented by the running Java virtual machine.

**Returns:**
- the version of the specification for the management interface
implemented by the running Java virtual machine.

---

#### String
getClassPath()

Returns the Java class path that is used by the system class loader
to search for class files.
This method is equivalent to

System.getProperty("java.class.path")

.

Multiple paths in the Java class path are separated by the
path separator character of the platform of the Java virtual machine
being monitored.

**Returns:**
- the Java class path.

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
getLibraryPath()

Returns the Java library path.
This method is equivalent to

System.getProperty("java.library.path")

.

Multiple paths in the Java library path are separated by the
path separator character of the platform of the Java virtual machine
being monitored.

**Returns:**
- the Java library path.

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

#### boolean isBootClassPathSupported()

Tests if the Java virtual machine supports the boot class path
mechanism used by the bootstrap class loader to search for class
files.

**Returns:**
- true

if the Java virtual machine supports the
class path mechanism;

false

otherwise.

---

#### String
getBootClassPath()

Returns the boot class path that is used by the bootstrap class loader
to search for class files.

Multiple paths in the boot class path are separated by the
path separator character of the platform on which the Java
virtual machine is running.

A Java virtual machine implementation may not support
the boot class path mechanism for the bootstrap class loader
to search for class files.
The

isBootClassPathSupported()

method can be used
to determine if the Java virtual machine supports this method.

**Returns:**
- the boot class path.

**Throws:**
- UnsupportedOperationException

- if the Java virtual machine does not support this operation.
- SecurityException

- if a security manager exists and the caller does not have
ManagementPermission("monitor").

---

#### List
<
String
> getInputArguments()

Returns the input arguments passed to the Java virtual machine
which does not include the arguments to the

main

method.
This method returns an empty list if there is no input argument
to the Java virtual machine.

Some Java virtual machine implementations may take input arguments
from multiple different sources: for examples, arguments passed from
the application that launches the Java virtual machine such as
the 'java' command, environment variables, configuration files, etc.

Typically, not all command-line options to the 'java' command
are passed to the Java virtual machine.
Thus, the returned input arguments may not
include all command-line options.

MBeanServer access

:

The mapped type of

List<String>

is

String[]

.

**Returns:**
- a list of

String

objects; each element
is an argument passed to the Java virtual machine.

**Throws:**
- SecurityException

- if a security manager exists and the caller does not have
ManagementPermission("monitor").

---

#### long getUptime()

Returns the uptime of the Java virtual machine in milliseconds.

**Returns:**
- uptime of the Java virtual machine in milliseconds.

---

#### long getStartTime()

Returns the start time of the Java virtual machine in milliseconds.
This method returns the approximate time when the Java virtual
machine started.

**Returns:**
- start time of the Java virtual machine in milliseconds.

---

#### Map
<
String
,​
String
> getSystemProperties()

Returns a map of names and values of all system properties.
This method calls

System.getProperties()

to get all
system properties. Properties whose name or value is not
a

String

are omitted.

MBeanServer access

:

The mapped type of

Map<String,String>

is

TabularData

with two items in each row as follows:

Name and Type for each item

Item Name

Item Type

key

String

value

String

**Returns:**
- a map of names and values of all system properties.

**Throws:**
- SecurityException

- if a security manager exists and its

checkPropertiesAccess

method doesn't allow access
to the system properties.

---

### Additional Sections

#### Interface RuntimeMXBean

**All Superinterfaces:** PlatformManagedObject

```java
public interface
RuntimeMXBean

extends
PlatformManagedObject
```

The management interface for the runtime system of
the Java virtual machine.

A Java virtual machine has a single instance of the implementation
class of this interface. This instance implementing this interface is
an

MXBean

that can be obtained by calling
the

ManagementFactory.getRuntimeMXBean()

method or
from the

platform MBeanServer

method.

The

ObjectName

for uniquely identifying the MXBean for
the runtime system within an MBeanServer is:

java.lang:type=Runtime

It can be obtained by calling the

PlatformManagedObject.getObjectName()

method.

This interface defines several convenient methods for accessing
system properties about the Java virtual machine.

**Since:** 1.5
**See Also:** ManagementFactory.getPlatformMXBeans(Class)

,

JMX Specification.

,

Ways to Access MXBeans

public interface

RuntimeMXBean

extends

PlatformManagedObject

The management interface for the runtime system of
the Java virtual machine.

A Java virtual machine has a single instance of the implementation
class of this interface. This instance implementing this interface is
an

MXBean

that can be obtained by calling
the

ManagementFactory.getRuntimeMXBean()

method or
from the

platform MBeanServer

method.

The

ObjectName

for uniquely identifying the MXBean for
the runtime system within an MBeanServer is:

java.lang:type=Runtime

It can be obtained by calling the

PlatformManagedObject.getObjectName()

method.

This interface defines several convenient methods for accessing
system properties about the Java virtual machine.

A Java virtual machine has a single instance of the implementation
class of this interface. This instance implementing this interface is
an

MXBean

that can be obtained by calling
the

ManagementFactory.getRuntimeMXBean()

method or
from the

platform MBeanServer

method.

The

ObjectName

for uniquely identifying the MXBean for
the runtime system within an MBeanServer is:

java.lang:type=Runtime

It can be obtained by calling the

PlatformManagedObject.getObjectName()

method.

This interface defines several convenient methods for accessing
system properties about the Java virtual machine.

The

ObjectName

for uniquely identifying the MXBean for
the runtime system within an MBeanServer is:

java.lang:type=Runtime

It can be obtained by calling the

PlatformManagedObject.getObjectName()

method.

This interface defines several convenient methods for accessing
system properties about the Java virtual machine.

This interface defines several convenient methods for accessing
system properties about the Java virtual machine.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Default Methods

Modifier and Type

Method

Description

String

getBootClassPath

()

Returns the boot class path that is used by the bootstrap class loader
to search for class files.

String

getClassPath

()

Returns the Java class path that is used by the system class loader
to search for class files.

List

<

String

>

getInputArguments

()

Returns the input arguments passed to the Java virtual machine
which does not include the arguments to the

main

method.

String

getLibraryPath

()

Returns the Java library path.

String

getManagementSpecVersion

()

Returns the version of the specification for the management interface
implemented by the running Java virtual machine.

String

getName

()

Returns the name representing the running Java virtual machine.

default long

getPid

()

Returns the

process ID

representing
the running Java virtual machine.

String

getSpecName

()

Returns the Java virtual machine specification name.

String

getSpecVendor

()

Returns the Java virtual machine specification vendor.

String

getSpecVersion

()

Returns the Java virtual machine specification version.

long

getStartTime

()

Returns the start time of the Java virtual machine in milliseconds.

Map

<

String

,​

String

>

getSystemProperties

()

Returns a map of names and values of all system properties.

long

getUptime

()

Returns the uptime of the Java virtual machine in milliseconds.

String

getVmName

()

Returns the Java virtual machine implementation name.

String

getVmVendor

()

Returns the Java virtual machine implementation vendor.

String

getVmVersion

()

Returns the Java virtual machine implementation version.

boolean

isBootClassPathSupported

()

Tests if the Java virtual machine supports the boot class path
mechanism used by the bootstrap class loader to search for class
files.

- Methods declared in interface java.lang.management.

PlatformManagedObject

getObjectName

Method Summary

All Methods

Instance Methods

Abstract Methods

Default Methods

Modifier and Type

Method

Description

String

getBootClassPath

()

Returns the boot class path that is used by the bootstrap class loader
to search for class files.

String

getClassPath

()

Returns the Java class path that is used by the system class loader
to search for class files.

List

<

String

>

getInputArguments

()

Returns the input arguments passed to the Java virtual machine
which does not include the arguments to the

main

method.

String

getLibraryPath

()

Returns the Java library path.

String

getManagementSpecVersion

()

Returns the version of the specification for the management interface
implemented by the running Java virtual machine.

String

getName

()

Returns the name representing the running Java virtual machine.

default long

getPid

()

Returns the

process ID

representing
the running Java virtual machine.

String

getSpecName

()

Returns the Java virtual machine specification name.

String

getSpecVendor

()

Returns the Java virtual machine specification vendor.

String

getSpecVersion

()

Returns the Java virtual machine specification version.

long

getStartTime

()

Returns the start time of the Java virtual machine in milliseconds.

Map

<

String

,​

String

>

getSystemProperties

()

Returns a map of names and values of all system properties.

long

getUptime

()

Returns the uptime of the Java virtual machine in milliseconds.

String

getVmName

()

Returns the Java virtual machine implementation name.

String

getVmVendor

()

Returns the Java virtual machine implementation vendor.

String

getVmVersion

()

Returns the Java virtual machine implementation version.

boolean

isBootClassPathSupported

()

Tests if the Java virtual machine supports the boot class path
mechanism used by the bootstrap class loader to search for class
files.

- Methods declared in interface java.lang.management.

PlatformManagedObject

getObjectName

---

#### Method Summary

Returns the boot class path that is used by the bootstrap class loader
to search for class files.

Returns the Java class path that is used by the system class loader
to search for class files.

Returns the input arguments passed to the Java virtual machine
which does not include the arguments to the

main

method.

Returns the Java library path.

Returns the version of the specification for the management interface
implemented by the running Java virtual machine.

Returns the name representing the running Java virtual machine.

Returns the

process ID

representing
the running Java virtual machine.

Returns the Java virtual machine specification name.

Returns the Java virtual machine specification vendor.

Returns the Java virtual machine specification version.

Returns the start time of the Java virtual machine in milliseconds.

Returns a map of names and values of all system properties.

Returns the uptime of the Java virtual machine in milliseconds.

Returns the Java virtual machine implementation name.

Returns the Java virtual machine implementation vendor.

Returns the Java virtual machine implementation version.

Tests if the Java virtual machine supports the boot class path
mechanism used by the bootstrap class loader to search for class
files.

Methods declared in interface java.lang.management.

PlatformManagedObject

getObjectName

---

#### Methods declared in interface java.lang.management. PlatformManagedObject

============ METHOD DETAIL ==========

- Method Detail

- getPid

```java
default long getPid()
```

Returns the

process ID

representing
the running Java virtual machine.

**Implementation Requirements:** The default implementation returns

process ID

of the

current process

.
**Returns:** the process ID representing the running Java virtual machine.
**Since:** 10

- getName

```java
String
getName()
```

Returns the name representing the running Java virtual machine.
The returned name string can be any arbitrary string and
a Java virtual machine implementation can choose
to embed platform-specific useful information in the
returned name string. Each running virtual machine could have
a different name.

**Returns:** the name representing the running Java virtual machine.

- getVmName

```java
String
getVmName()
```

Returns the Java virtual machine implementation name.
This method is equivalent to

System.getProperty("java.vm.name")

.

**Returns:** the Java virtual machine implementation name.
**Throws:** SecurityException

- if a security manager exists and its

checkPropertiesAccess

method doesn't allow access
to this system property.
**See Also:** SecurityManager.checkPropertyAccess(java.lang.String)

,

System.getProperty(java.lang.String)

- getVmVendor

```java
String
getVmVendor()
```

Returns the Java virtual machine implementation vendor.
This method is equivalent to

System.getProperty("java.vm.vendor")

.

**Returns:** the Java virtual machine implementation vendor.
**Throws:** SecurityException

- if a security manager exists and its

checkPropertiesAccess

method doesn't allow access
to this system property.
**See Also:** SecurityManager.checkPropertyAccess(java.lang.String)

,

System.getProperty(java.lang.String)

- getVmVersion

```java
String
getVmVersion()
```

Returns the Java virtual machine implementation version.
This method is equivalent to

System.getProperty("java.vm.version")

.

**Returns:** the Java virtual machine implementation version.
**Throws:** SecurityException

- if a security manager exists and its

checkPropertiesAccess

method doesn't allow access
to this system property.
**See Also:** SecurityManager.checkPropertyAccess(java.lang.String)

,

System.getProperty(java.lang.String)

- getSpecName

```java
String
getSpecName()
```

Returns the Java virtual machine specification name.
This method is equivalent to

System.getProperty("java.vm.specification.name")

.

**Returns:** the Java virtual machine specification name.
**Throws:** SecurityException

- if a security manager exists and its

checkPropertiesAccess

method doesn't allow access
to this system property.
**See Also:** SecurityManager.checkPropertyAccess(java.lang.String)

,

System.getProperty(java.lang.String)

- getSpecVendor

```java
String
getSpecVendor()
```

Returns the Java virtual machine specification vendor.
This method is equivalent to

System.getProperty("java.vm.specification.vendor")

.

**Returns:** the Java virtual machine specification vendor.
**Throws:** SecurityException

- if a security manager exists and its

checkPropertiesAccess

method doesn't allow access
to this system property.
**See Also:** SecurityManager.checkPropertyAccess(java.lang.String)

,

System.getProperty(java.lang.String)

- getSpecVersion

```java
String
getSpecVersion()
```

Returns the Java virtual machine specification version.
This method is equivalent to

System.getProperty("java.vm.specification.version")

.

**Returns:** the Java virtual machine specification version.
**Throws:** SecurityException

- if a security manager exists and its

checkPropertiesAccess

method doesn't allow access
to this system property.
**See Also:** SecurityManager.checkPropertyAccess(java.lang.String)

,

System.getProperty(java.lang.String)

- getManagementSpecVersion

```java
String
getManagementSpecVersion()
```

Returns the version of the specification for the management interface
implemented by the running Java virtual machine.

**Returns:** the version of the specification for the management interface
implemented by the running Java virtual machine.

- getClassPath

```java
String
getClassPath()
```

Returns the Java class path that is used by the system class loader
to search for class files.
This method is equivalent to

System.getProperty("java.class.path")

.

Multiple paths in the Java class path are separated by the
path separator character of the platform of the Java virtual machine
being monitored.

**Returns:** the Java class path.
**Throws:** SecurityException

- if a security manager exists and its

checkPropertiesAccess

method doesn't allow access
to this system property.
**See Also:** SecurityManager.checkPropertyAccess(java.lang.String)

,

System.getProperty(java.lang.String)

- getLibraryPath

```java
String
getLibraryPath()
```

Returns the Java library path.
This method is equivalent to

System.getProperty("java.library.path")

.

Multiple paths in the Java library path are separated by the
path separator character of the platform of the Java virtual machine
being monitored.

**Returns:** the Java library path.
**Throws:** SecurityException

- if a security manager exists and its

checkPropertiesAccess

method doesn't allow access
to this system property.
**See Also:** SecurityManager.checkPropertyAccess(java.lang.String)

,

System.getProperty(java.lang.String)

- isBootClassPathSupported

```java
boolean isBootClassPathSupported()
```

Tests if the Java virtual machine supports the boot class path
mechanism used by the bootstrap class loader to search for class
files.

**Returns:** true

if the Java virtual machine supports the
class path mechanism;

false

otherwise.

- getBootClassPath

```java
String
getBootClassPath()
```

Returns the boot class path that is used by the bootstrap class loader
to search for class files.

Multiple paths in the boot class path are separated by the
path separator character of the platform on which the Java
virtual machine is running.

A Java virtual machine implementation may not support
the boot class path mechanism for the bootstrap class loader
to search for class files.
The

isBootClassPathSupported()

method can be used
to determine if the Java virtual machine supports this method.

**Returns:** the boot class path.
**Throws:** UnsupportedOperationException

- if the Java virtual machine does not support this operation.
**Throws:** SecurityException

- if a security manager exists and the caller does not have
ManagementPermission("monitor").

- getInputArguments

```java
List
<
String
> getInputArguments()
```

Returns the input arguments passed to the Java virtual machine
which does not include the arguments to the

main

method.
This method returns an empty list if there is no input argument
to the Java virtual machine.

Some Java virtual machine implementations may take input arguments
from multiple different sources: for examples, arguments passed from
the application that launches the Java virtual machine such as
the 'java' command, environment variables, configuration files, etc.

Typically, not all command-line options to the 'java' command
are passed to the Java virtual machine.
Thus, the returned input arguments may not
include all command-line options.

MBeanServer access

:

The mapped type of

List<String>

is

String[]

.

**Returns:** a list of

String

objects; each element
is an argument passed to the Java virtual machine.
**Throws:** SecurityException

- if a security manager exists and the caller does not have
ManagementPermission("monitor").

- getUptime

```java
long getUptime()
```

Returns the uptime of the Java virtual machine in milliseconds.

**Returns:** uptime of the Java virtual machine in milliseconds.

- getStartTime

```java
long getStartTime()
```

Returns the start time of the Java virtual machine in milliseconds.
This method returns the approximate time when the Java virtual
machine started.

**Returns:** start time of the Java virtual machine in milliseconds.

- getSystemProperties

```java
Map
<
String
,​
String
> getSystemProperties()
```

Returns a map of names and values of all system properties.
This method calls

System.getProperties()

to get all
system properties. Properties whose name or value is not
a

String

are omitted.

MBeanServer access

:

The mapped type of

Map<String,String>

is

TabularData

with two items in each row as follows:

Name and Type for each item

Item Name

Item Type

key

String

value

String

**Returns:** a map of names and values of all system properties.
**Throws:** SecurityException

- if a security manager exists and its

checkPropertiesAccess

method doesn't allow access
to the system properties.

Method Detail

- getPid

```java
default long getPid()
```

Returns the

process ID

representing
the running Java virtual machine.

**Implementation Requirements:** The default implementation returns

process ID

of the

current process

.
**Returns:** the process ID representing the running Java virtual machine.
**Since:** 10

- getName

```java
String
getName()
```

Returns the name representing the running Java virtual machine.
The returned name string can be any arbitrary string and
a Java virtual machine implementation can choose
to embed platform-specific useful information in the
returned name string. Each running virtual machine could have
a different name.

**Returns:** the name representing the running Java virtual machine.

- getVmName

```java
String
getVmName()
```

Returns the Java virtual machine implementation name.
This method is equivalent to

System.getProperty("java.vm.name")

.

**Returns:** the Java virtual machine implementation name.
**Throws:** SecurityException

- if a security manager exists and its

checkPropertiesAccess

method doesn't allow access
to this system property.
**See Also:** SecurityManager.checkPropertyAccess(java.lang.String)

,

System.getProperty(java.lang.String)

- getVmVendor

```java
String
getVmVendor()
```

Returns the Java virtual machine implementation vendor.
This method is equivalent to

System.getProperty("java.vm.vendor")

.

**Returns:** the Java virtual machine implementation vendor.
**Throws:** SecurityException

- if a security manager exists and its

checkPropertiesAccess

method doesn't allow access
to this system property.
**See Also:** SecurityManager.checkPropertyAccess(java.lang.String)

,

System.getProperty(java.lang.String)

- getVmVersion

```java
String
getVmVersion()
```

Returns the Java virtual machine implementation version.
This method is equivalent to

System.getProperty("java.vm.version")

.

**Returns:** the Java virtual machine implementation version.
**Throws:** SecurityException

- if a security manager exists and its

checkPropertiesAccess

method doesn't allow access
to this system property.
**See Also:** SecurityManager.checkPropertyAccess(java.lang.String)

,

System.getProperty(java.lang.String)

- getSpecName

```java
String
getSpecName()
```

Returns the Java virtual machine specification name.
This method is equivalent to

System.getProperty("java.vm.specification.name")

.

**Returns:** the Java virtual machine specification name.
**Throws:** SecurityException

- if a security manager exists and its

checkPropertiesAccess

method doesn't allow access
to this system property.
**See Also:** SecurityManager.checkPropertyAccess(java.lang.String)

,

System.getProperty(java.lang.String)

- getSpecVendor

```java
String
getSpecVendor()
```

Returns the Java virtual machine specification vendor.
This method is equivalent to

System.getProperty("java.vm.specification.vendor")

.

**Returns:** the Java virtual machine specification vendor.
**Throws:** SecurityException

- if a security manager exists and its

checkPropertiesAccess

method doesn't allow access
to this system property.
**See Also:** SecurityManager.checkPropertyAccess(java.lang.String)

,

System.getProperty(java.lang.String)

- getSpecVersion

```java
String
getSpecVersion()
```

Returns the Java virtual machine specification version.
This method is equivalent to

System.getProperty("java.vm.specification.version")

.

**Returns:** the Java virtual machine specification version.
**Throws:** SecurityException

- if a security manager exists and its

checkPropertiesAccess

method doesn't allow access
to this system property.
**See Also:** SecurityManager.checkPropertyAccess(java.lang.String)

,

System.getProperty(java.lang.String)

- getManagementSpecVersion

```java
String
getManagementSpecVersion()
```

Returns the version of the specification for the management interface
implemented by the running Java virtual machine.

**Returns:** the version of the specification for the management interface
implemented by the running Java virtual machine.

- getClassPath

```java
String
getClassPath()
```

Returns the Java class path that is used by the system class loader
to search for class files.
This method is equivalent to

System.getProperty("java.class.path")

.

Multiple paths in the Java class path are separated by the
path separator character of the platform of the Java virtual machine
being monitored.

**Returns:** the Java class path.
**Throws:** SecurityException

- if a security manager exists and its

checkPropertiesAccess

method doesn't allow access
to this system property.
**See Also:** SecurityManager.checkPropertyAccess(java.lang.String)

,

System.getProperty(java.lang.String)

- getLibraryPath

```java
String
getLibraryPath()
```

Returns the Java library path.
This method is equivalent to

System.getProperty("java.library.path")

.

Multiple paths in the Java library path are separated by the
path separator character of the platform of the Java virtual machine
being monitored.

**Returns:** the Java library path.
**Throws:** SecurityException

- if a security manager exists and its

checkPropertiesAccess

method doesn't allow access
to this system property.
**See Also:** SecurityManager.checkPropertyAccess(java.lang.String)

,

System.getProperty(java.lang.String)

- isBootClassPathSupported

```java
boolean isBootClassPathSupported()
```

Tests if the Java virtual machine supports the boot class path
mechanism used by the bootstrap class loader to search for class
files.

**Returns:** true

if the Java virtual machine supports the
class path mechanism;

false

otherwise.

- getBootClassPath

```java
String
getBootClassPath()
```

Returns the boot class path that is used by the bootstrap class loader
to search for class files.

Multiple paths in the boot class path are separated by the
path separator character of the platform on which the Java
virtual machine is running.

A Java virtual machine implementation may not support
the boot class path mechanism for the bootstrap class loader
to search for class files.
The

isBootClassPathSupported()

method can be used
to determine if the Java virtual machine supports this method.

**Returns:** the boot class path.
**Throws:** UnsupportedOperationException

- if the Java virtual machine does not support this operation.
**Throws:** SecurityException

- if a security manager exists and the caller does not have
ManagementPermission("monitor").

- getInputArguments

```java
List
<
String
> getInputArguments()
```

Returns the input arguments passed to the Java virtual machine
which does not include the arguments to the

main

method.
This method returns an empty list if there is no input argument
to the Java virtual machine.

Some Java virtual machine implementations may take input arguments
from multiple different sources: for examples, arguments passed from
the application that launches the Java virtual machine such as
the 'java' command, environment variables, configuration files, etc.

Typically, not all command-line options to the 'java' command
are passed to the Java virtual machine.
Thus, the returned input arguments may not
include all command-line options.

MBeanServer access

:

The mapped type of

List<String>

is

String[]

.

**Returns:** a list of

String

objects; each element
is an argument passed to the Java virtual machine.
**Throws:** SecurityException

- if a security manager exists and the caller does not have
ManagementPermission("monitor").

- getUptime

```java
long getUptime()
```

Returns the uptime of the Java virtual machine in milliseconds.

**Returns:** uptime of the Java virtual machine in milliseconds.

- getStartTime

```java
long getStartTime()
```

Returns the start time of the Java virtual machine in milliseconds.
This method returns the approximate time when the Java virtual
machine started.

**Returns:** start time of the Java virtual machine in milliseconds.

- getSystemProperties

```java
Map
<
String
,​
String
> getSystemProperties()
```

Returns a map of names and values of all system properties.
This method calls

System.getProperties()

to get all
system properties. Properties whose name or value is not
a

String

are omitted.

MBeanServer access

:

The mapped type of

Map<String,String>

is

TabularData

with two items in each row as follows:

Name and Type for each item

Item Name

Item Type

key

String

value

String

**Returns:** a map of names and values of all system properties.
**Throws:** SecurityException

- if a security manager exists and its

checkPropertiesAccess

method doesn't allow access
to the system properties.

---

#### Method Detail

getPid

```java
default long getPid()
```

Returns the

process ID

representing
the running Java virtual machine.

**Implementation Requirements:** The default implementation returns

process ID

of the

current process

.
**Returns:** the process ID representing the running Java virtual machine.
**Since:** 10

---

#### getPid

default long getPid()

Returns the

process ID

representing
the running Java virtual machine.

getName

```java
String
getName()
```

Returns the name representing the running Java virtual machine.
The returned name string can be any arbitrary string and
a Java virtual machine implementation can choose
to embed platform-specific useful information in the
returned name string. Each running virtual machine could have
a different name.

**Returns:** the name representing the running Java virtual machine.

---

#### getName

String

getName()

Returns the name representing the running Java virtual machine.
The returned name string can be any arbitrary string and
a Java virtual machine implementation can choose
to embed platform-specific useful information in the
returned name string. Each running virtual machine could have
a different name.

getVmName

```java
String
getVmName()
```

Returns the Java virtual machine implementation name.
This method is equivalent to

System.getProperty("java.vm.name")

.

**Returns:** the Java virtual machine implementation name.
**Throws:** SecurityException

- if a security manager exists and its

checkPropertiesAccess

method doesn't allow access
to this system property.
**See Also:** SecurityManager.checkPropertyAccess(java.lang.String)

,

System.getProperty(java.lang.String)

---

#### getVmName

String

getVmName()

Returns the Java virtual machine implementation name.
This method is equivalent to

System.getProperty("java.vm.name")

.

getVmVendor

```java
String
getVmVendor()
```

Returns the Java virtual machine implementation vendor.
This method is equivalent to

System.getProperty("java.vm.vendor")

.

**Returns:** the Java virtual machine implementation vendor.
**Throws:** SecurityException

- if a security manager exists and its

checkPropertiesAccess

method doesn't allow access
to this system property.
**See Also:** SecurityManager.checkPropertyAccess(java.lang.String)

,

System.getProperty(java.lang.String)

---

#### getVmVendor

String

getVmVendor()

Returns the Java virtual machine implementation vendor.
This method is equivalent to

System.getProperty("java.vm.vendor")

.

getVmVersion

```java
String
getVmVersion()
```

Returns the Java virtual machine implementation version.
This method is equivalent to

System.getProperty("java.vm.version")

.

**Returns:** the Java virtual machine implementation version.
**Throws:** SecurityException

- if a security manager exists and its

checkPropertiesAccess

method doesn't allow access
to this system property.
**See Also:** SecurityManager.checkPropertyAccess(java.lang.String)

,

System.getProperty(java.lang.String)

---

#### getVmVersion

String

getVmVersion()

Returns the Java virtual machine implementation version.
This method is equivalent to

System.getProperty("java.vm.version")

.

getSpecName

```java
String
getSpecName()
```

Returns the Java virtual machine specification name.
This method is equivalent to

System.getProperty("java.vm.specification.name")

.

**Returns:** the Java virtual machine specification name.
**Throws:** SecurityException

- if a security manager exists and its

checkPropertiesAccess

method doesn't allow access
to this system property.
**See Also:** SecurityManager.checkPropertyAccess(java.lang.String)

,

System.getProperty(java.lang.String)

---

#### getSpecName

String

getSpecName()

Returns the Java virtual machine specification name.
This method is equivalent to

System.getProperty("java.vm.specification.name")

.

getSpecVendor

```java
String
getSpecVendor()
```

Returns the Java virtual machine specification vendor.
This method is equivalent to

System.getProperty("java.vm.specification.vendor")

.

**Returns:** the Java virtual machine specification vendor.
**Throws:** SecurityException

- if a security manager exists and its

checkPropertiesAccess

method doesn't allow access
to this system property.
**See Also:** SecurityManager.checkPropertyAccess(java.lang.String)

,

System.getProperty(java.lang.String)

---

#### getSpecVendor

String

getSpecVendor()

Returns the Java virtual machine specification vendor.
This method is equivalent to

System.getProperty("java.vm.specification.vendor")

.

getSpecVersion

```java
String
getSpecVersion()
```

Returns the Java virtual machine specification version.
This method is equivalent to

System.getProperty("java.vm.specification.version")

.

**Returns:** the Java virtual machine specification version.
**Throws:** SecurityException

- if a security manager exists and its

checkPropertiesAccess

method doesn't allow access
to this system property.
**See Also:** SecurityManager.checkPropertyAccess(java.lang.String)

,

System.getProperty(java.lang.String)

---

#### getSpecVersion

String

getSpecVersion()

Returns the Java virtual machine specification version.
This method is equivalent to

System.getProperty("java.vm.specification.version")

.

getManagementSpecVersion

```java
String
getManagementSpecVersion()
```

Returns the version of the specification for the management interface
implemented by the running Java virtual machine.

**Returns:** the version of the specification for the management interface
implemented by the running Java virtual machine.

---

#### getManagementSpecVersion

String

getManagementSpecVersion()

Returns the version of the specification for the management interface
implemented by the running Java virtual machine.

getClassPath

```java
String
getClassPath()
```

Returns the Java class path that is used by the system class loader
to search for class files.
This method is equivalent to

System.getProperty("java.class.path")

.

Multiple paths in the Java class path are separated by the
path separator character of the platform of the Java virtual machine
being monitored.

**Returns:** the Java class path.
**Throws:** SecurityException

- if a security manager exists and its

checkPropertiesAccess

method doesn't allow access
to this system property.
**See Also:** SecurityManager.checkPropertyAccess(java.lang.String)

,

System.getProperty(java.lang.String)

---

#### getClassPath

String

getClassPath()

Returns the Java class path that is used by the system class loader
to search for class files.
This method is equivalent to

System.getProperty("java.class.path")

.

Multiple paths in the Java class path are separated by the
path separator character of the platform of the Java virtual machine
being monitored.

Multiple paths in the Java class path are separated by the
path separator character of the platform of the Java virtual machine
being monitored.

getLibraryPath

```java
String
getLibraryPath()
```

Returns the Java library path.
This method is equivalent to

System.getProperty("java.library.path")

.

Multiple paths in the Java library path are separated by the
path separator character of the platform of the Java virtual machine
being monitored.

**Returns:** the Java library path.
**Throws:** SecurityException

- if a security manager exists and its

checkPropertiesAccess

method doesn't allow access
to this system property.
**See Also:** SecurityManager.checkPropertyAccess(java.lang.String)

,

System.getProperty(java.lang.String)

---

#### getLibraryPath

String

getLibraryPath()

Returns the Java library path.
This method is equivalent to

System.getProperty("java.library.path")

.

Multiple paths in the Java library path are separated by the
path separator character of the platform of the Java virtual machine
being monitored.

Multiple paths in the Java library path are separated by the
path separator character of the platform of the Java virtual machine
being monitored.

isBootClassPathSupported

```java
boolean isBootClassPathSupported()
```

Tests if the Java virtual machine supports the boot class path
mechanism used by the bootstrap class loader to search for class
files.

**Returns:** true

if the Java virtual machine supports the
class path mechanism;

false

otherwise.

---

#### isBootClassPathSupported

boolean isBootClassPathSupported()

Tests if the Java virtual machine supports the boot class path
mechanism used by the bootstrap class loader to search for class
files.

getBootClassPath

```java
String
getBootClassPath()
```

Returns the boot class path that is used by the bootstrap class loader
to search for class files.

Multiple paths in the boot class path are separated by the
path separator character of the platform on which the Java
virtual machine is running.

A Java virtual machine implementation may not support
the boot class path mechanism for the bootstrap class loader
to search for class files.
The

isBootClassPathSupported()

method can be used
to determine if the Java virtual machine supports this method.

**Returns:** the boot class path.
**Throws:** UnsupportedOperationException

- if the Java virtual machine does not support this operation.
**Throws:** SecurityException

- if a security manager exists and the caller does not have
ManagementPermission("monitor").

---

#### getBootClassPath

String

getBootClassPath()

Returns the boot class path that is used by the bootstrap class loader
to search for class files.

Multiple paths in the boot class path are separated by the
path separator character of the platform on which the Java
virtual machine is running.

A Java virtual machine implementation may not support
the boot class path mechanism for the bootstrap class loader
to search for class files.
The

isBootClassPathSupported()

method can be used
to determine if the Java virtual machine supports this method.

Multiple paths in the boot class path are separated by the
path separator character of the platform on which the Java
virtual machine is running.

A Java virtual machine implementation may not support
the boot class path mechanism for the bootstrap class loader
to search for class files.
The

isBootClassPathSupported()

method can be used
to determine if the Java virtual machine supports this method.

A Java virtual machine implementation may not support
the boot class path mechanism for the bootstrap class loader
to search for class files.
The

isBootClassPathSupported()

method can be used
to determine if the Java virtual machine supports this method.

getInputArguments

```java
List
<
String
> getInputArguments()
```

Returns the input arguments passed to the Java virtual machine
which does not include the arguments to the

main

method.
This method returns an empty list if there is no input argument
to the Java virtual machine.

Some Java virtual machine implementations may take input arguments
from multiple different sources: for examples, arguments passed from
the application that launches the Java virtual machine such as
the 'java' command, environment variables, configuration files, etc.

Typically, not all command-line options to the 'java' command
are passed to the Java virtual machine.
Thus, the returned input arguments may not
include all command-line options.

MBeanServer access

:

The mapped type of

List<String>

is

String[]

.

**Returns:** a list of

String

objects; each element
is an argument passed to the Java virtual machine.
**Throws:** SecurityException

- if a security manager exists and the caller does not have
ManagementPermission("monitor").

---

#### getInputArguments

List

<

String

> getInputArguments()

Returns the input arguments passed to the Java virtual machine
which does not include the arguments to the

main

method.
This method returns an empty list if there is no input argument
to the Java virtual machine.

Some Java virtual machine implementations may take input arguments
from multiple different sources: for examples, arguments passed from
the application that launches the Java virtual machine such as
the 'java' command, environment variables, configuration files, etc.

Typically, not all command-line options to the 'java' command
are passed to the Java virtual machine.
Thus, the returned input arguments may not
include all command-line options.

MBeanServer access

:

The mapped type of

List<String>

is

String[]

.

Some Java virtual machine implementations may take input arguments
from multiple different sources: for examples, arguments passed from
the application that launches the Java virtual machine such as
the 'java' command, environment variables, configuration files, etc.

Typically, not all command-line options to the 'java' command
are passed to the Java virtual machine.
Thus, the returned input arguments may not
include all command-line options.

MBeanServer access

:

The mapped type of

List<String>

is

String[]

.

Typically, not all command-line options to the 'java' command
are passed to the Java virtual machine.
Thus, the returned input arguments may not
include all command-line options.

MBeanServer access

:

The mapped type of

List<String>

is

String[]

.

MBeanServer access

:

The mapped type of

List<String>

is

String[]

.

getUptime

```java
long getUptime()
```

Returns the uptime of the Java virtual machine in milliseconds.

**Returns:** uptime of the Java virtual machine in milliseconds.

---

#### getUptime

long getUptime()

Returns the uptime of the Java virtual machine in milliseconds.

getStartTime

```java
long getStartTime()
```

Returns the start time of the Java virtual machine in milliseconds.
This method returns the approximate time when the Java virtual
machine started.

**Returns:** start time of the Java virtual machine in milliseconds.

---

#### getStartTime

long getStartTime()

Returns the start time of the Java virtual machine in milliseconds.
This method returns the approximate time when the Java virtual
machine started.

getSystemProperties

```java
Map
<
String
,​
String
> getSystemProperties()
```

Returns a map of names and values of all system properties.
This method calls

System.getProperties()

to get all
system properties. Properties whose name or value is not
a

String

are omitted.

MBeanServer access

:

The mapped type of

Map<String,String>

is

TabularData

with two items in each row as follows:

Name and Type for each item

Item Name

Item Type

key

String

value

String

**Returns:** a map of names and values of all system properties.
**Throws:** SecurityException

- if a security manager exists and its

checkPropertiesAccess

method doesn't allow access
to the system properties.

---

#### getSystemProperties

Map

<

String

,​

String

> getSystemProperties()

Returns a map of names and values of all system properties.
This method calls

System.getProperties()

to get all
system properties. Properties whose name or value is not
a

String

are omitted.

MBeanServer access

:

The mapped type of

Map<String,String>

is

TabularData

with two items in each row as follows:

Name and Type for each item

Item Name

Item Type

key

String

value

String

MBeanServer access

:

The mapped type of

Map<String,String>

is

TabularData

with two items in each row as follows:

Name and Type for each item

Item Name

Item Type

key

String

value

String

---

