# Interface HotSpotDiagnosticMXBean

**Source:** `jdk.management\com\sun\management\HotSpotDiagnosticMXBean.html`

### Class Description

```java
public interface
HotSpotDiagnosticMXBean

extends
PlatformManagedObject
```

Diagnostic management interface for the HotSpot Virtual Machine.

The diagnostic MBean is registered to the platform MBeanServer
as are other platform MBeans.

The

ObjectName

for uniquely identifying the diagnostic
MXBean within an MBeanServer is:

com.sun.management:type=HotSpotDiagnostic

.*
It can be obtained by calling the

PlatformManagedObject.getObjectName()

method.

All methods throw a

NullPointerException

if any input argument is

null

unless it's stated otherwise.

**All Superinterfaces:** PlatformManagedObject

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### void dumpHeap​(
String
outputFile,
boolean live)
throws
IOException

Dumps the heap to the

outputFile

file in the same
format as the hprof heap dump.

If this method is called remotely from another process,
the heap dump output is written to a file named

outputFile

on the machine where the target VM is running. If outputFile is
a relative path, it is relative to the working directory where
the target VM was started.

**Parameters:**
- outputFile

- the system-dependent filename
- live

- if

true

dump only

live

objects
i.e. objects that are reachable from others

**Throws:**
- IOException

- if the

outputFile

already exists,
cannot be created, opened, or written to.
- UnsupportedOperationException

- if this operation is not supported.
- IllegalArgumentException

- if

outputFile

does not end with ".hprof" suffix.
- NullPointerException

- if

outputFile

is

null

.
- SecurityException

- If a security manager exists and its

SecurityManager.checkWrite(java.lang.String)

method denies write access to the named file
or the caller does not have ManagmentPermission("control").

---

#### List
<
VMOption
> getDiagnosticOptions()

Returns a list of

VMOption

objects for all diagnostic options.
A diagnostic option is a

writeable

VM option that can be set dynamically mainly for troubleshooting
and diagnosis.

**Returns:**
- a list of

VMOption

objects for all diagnostic options.

---

#### VMOption
getVMOption​(
String
name)

Returns a

VMOption

object for a VM option of the given
name.

**Returns:**
- a

VMOption

object for a VM option of the given name.

**Throws:**
- NullPointerException

- if name is

null

.
- IllegalArgumentException

- if a VM option of the given name
does not exist.

---

#### void setVMOption​(
String
name,

String
value)

Sets a VM option of the given name to the specified value.
The new value will be reflected in a new

VMOption

object returned by the

getVMOption(java.lang.String)

method or
the

getDiagnosticOptions()

method. This method does
not change the value of this

VMOption

object.

**Parameters:**
- name

- Name of a VM option
- value

- New value of the VM option to be set

**Throws:**
- IllegalArgumentException

- if the VM option of the given name
does not exist.
- IllegalArgumentException

- if the new value is invalid.
- IllegalArgumentException

- if the VM option is not writable.
- NullPointerException

- if name or value is

null

.
- SecurityException

- if a security manager exists and the caller does not have
ManagementPermission("control").

---

### Additional Sections

#### Interface HotSpotDiagnosticMXBean

**All Superinterfaces:** PlatformManagedObject

```java
public interface
HotSpotDiagnosticMXBean

extends
PlatformManagedObject
```

Diagnostic management interface for the HotSpot Virtual Machine.

The diagnostic MBean is registered to the platform MBeanServer
as are other platform MBeans.

The

ObjectName

for uniquely identifying the diagnostic
MXBean within an MBeanServer is:

com.sun.management:type=HotSpotDiagnostic

.*
It can be obtained by calling the

PlatformManagedObject.getObjectName()

method.

All methods throw a

NullPointerException

if any input argument is

null

unless it's stated otherwise.

**See Also:** ManagementFactory.getPlatformMXBeans(Class)

public interface

HotSpotDiagnosticMXBean

extends

PlatformManagedObject

Diagnostic management interface for the HotSpot Virtual Machine.

The diagnostic MBean is registered to the platform MBeanServer
as are other platform MBeans.

The

ObjectName

for uniquely identifying the diagnostic
MXBean within an MBeanServer is:

com.sun.management:type=HotSpotDiagnostic

.*
It can be obtained by calling the

PlatformManagedObject.getObjectName()

method.

All methods throw a

NullPointerException

if any input argument is

null

unless it's stated otherwise.

The diagnostic MBean is registered to the platform MBeanServer
as are other platform MBeans.

The

ObjectName

for uniquely identifying the diagnostic
MXBean within an MBeanServer is:

com.sun.management:type=HotSpotDiagnostic

.*
It can be obtained by calling the

PlatformManagedObject.getObjectName()

method.

All methods throw a

NullPointerException

if any input argument is

null

unless it's stated otherwise.

The

ObjectName

for uniquely identifying the diagnostic
MXBean within an MBeanServer is:

com.sun.management:type=HotSpotDiagnostic

.*
It can be obtained by calling the

PlatformManagedObject.getObjectName()

method.

All methods throw a

NullPointerException

if any input argument is

null

unless it's stated otherwise.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

dumpHeap

​(

String

outputFile,
boolean live)

Dumps the heap to the

outputFile

file in the same
format as the hprof heap dump.

List

<

VMOption

>

getDiagnosticOptions

()

Returns a list of

VMOption

objects for all diagnostic options.

VMOption

getVMOption

​(

String

name)

Returns a

VMOption

object for a VM option of the given
name.

void

setVMOption

​(

String

name,

String

value)

Sets a VM option of the given name to the specified value.

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

void

dumpHeap

​(

String

outputFile,
boolean live)

Dumps the heap to the

outputFile

file in the same
format as the hprof heap dump.

List

<

VMOption

>

getDiagnosticOptions

()

Returns a list of

VMOption

objects for all diagnostic options.

VMOption

getVMOption

​(

String

name)

Returns a

VMOption

object for a VM option of the given
name.

void

setVMOption

​(

String

name,

String

value)

Sets a VM option of the given name to the specified value.

- Methods declared in interface java.lang.management.

PlatformManagedObject

getObjectName

---

#### Method Summary

Dumps the heap to the

outputFile

file in the same
format as the hprof heap dump.

Returns a list of

VMOption

objects for all diagnostic options.

Returns a

VMOption

object for a VM option of the given
name.

Sets a VM option of the given name to the specified value.

Methods declared in interface java.lang.management.

PlatformManagedObject

getObjectName

---

#### Methods declared in interface java.lang.management. PlatformManagedObject

============ METHOD DETAIL ==========

- Method Detail

- dumpHeap

```java
void dumpHeap​(
String
outputFile,
boolean live)
throws
IOException
```

Dumps the heap to the

outputFile

file in the same
format as the hprof heap dump.

If this method is called remotely from another process,
the heap dump output is written to a file named

outputFile

on the machine where the target VM is running. If outputFile is
a relative path, it is relative to the working directory where
the target VM was started.

**Parameters:** outputFile

- the system-dependent filename
**Parameters:** live

- if

true

dump only

live

objects
i.e. objects that are reachable from others
**Throws:** IOException

- if the

outputFile

already exists,
cannot be created, opened, or written to.
**Throws:** UnsupportedOperationException

- if this operation is not supported.
**Throws:** IllegalArgumentException

- if

outputFile

does not end with ".hprof" suffix.
**Throws:** NullPointerException

- if

outputFile

is

null

.
**Throws:** SecurityException

- If a security manager exists and its

SecurityManager.checkWrite(java.lang.String)

method denies write access to the named file
or the caller does not have ManagmentPermission("control").

- getDiagnosticOptions

```java
List
<
VMOption
> getDiagnosticOptions()
```

Returns a list of

VMOption

objects for all diagnostic options.
A diagnostic option is a

writeable

VM option that can be set dynamically mainly for troubleshooting
and diagnosis.

**Returns:** a list of

VMOption

objects for all diagnostic options.

- getVMOption

```java
VMOption
getVMOption​(
String
name)
```

Returns a

VMOption

object for a VM option of the given
name.

**Returns:** a

VMOption

object for a VM option of the given name.
**Throws:** NullPointerException

- if name is

null

.
**Throws:** IllegalArgumentException

- if a VM option of the given name
does not exist.

- setVMOption

```java
void setVMOption​(
String
name,

String
value)
```

Sets a VM option of the given name to the specified value.
The new value will be reflected in a new

VMOption

object returned by the

getVMOption(java.lang.String)

method or
the

getDiagnosticOptions()

method. This method does
not change the value of this

VMOption

object.

**Parameters:** name

- Name of a VM option
**Parameters:** value

- New value of the VM option to be set
**Throws:** IllegalArgumentException

- if the VM option of the given name
does not exist.
**Throws:** IllegalArgumentException

- if the new value is invalid.
**Throws:** IllegalArgumentException

- if the VM option is not writable.
**Throws:** NullPointerException

- if name or value is

null

.
**Throws:** SecurityException

- if a security manager exists and the caller does not have
ManagementPermission("control").

Method Detail

- dumpHeap

```java
void dumpHeap​(
String
outputFile,
boolean live)
throws
IOException
```

Dumps the heap to the

outputFile

file in the same
format as the hprof heap dump.

If this method is called remotely from another process,
the heap dump output is written to a file named

outputFile

on the machine where the target VM is running. If outputFile is
a relative path, it is relative to the working directory where
the target VM was started.

**Parameters:** outputFile

- the system-dependent filename
**Parameters:** live

- if

true

dump only

live

objects
i.e. objects that are reachable from others
**Throws:** IOException

- if the

outputFile

already exists,
cannot be created, opened, or written to.
**Throws:** UnsupportedOperationException

- if this operation is not supported.
**Throws:** IllegalArgumentException

- if

outputFile

does not end with ".hprof" suffix.
**Throws:** NullPointerException

- if

outputFile

is

null

.
**Throws:** SecurityException

- If a security manager exists and its

SecurityManager.checkWrite(java.lang.String)

method denies write access to the named file
or the caller does not have ManagmentPermission("control").

- getDiagnosticOptions

```java
List
<
VMOption
> getDiagnosticOptions()
```

Returns a list of

VMOption

objects for all diagnostic options.
A diagnostic option is a

writeable

VM option that can be set dynamically mainly for troubleshooting
and diagnosis.

**Returns:** a list of

VMOption

objects for all diagnostic options.

- getVMOption

```java
VMOption
getVMOption​(
String
name)
```

Returns a

VMOption

object for a VM option of the given
name.

**Returns:** a

VMOption

object for a VM option of the given name.
**Throws:** NullPointerException

- if name is

null

.
**Throws:** IllegalArgumentException

- if a VM option of the given name
does not exist.

- setVMOption

```java
void setVMOption​(
String
name,

String
value)
```

Sets a VM option of the given name to the specified value.
The new value will be reflected in a new

VMOption

object returned by the

getVMOption(java.lang.String)

method or
the

getDiagnosticOptions()

method. This method does
not change the value of this

VMOption

object.

**Parameters:** name

- Name of a VM option
**Parameters:** value

- New value of the VM option to be set
**Throws:** IllegalArgumentException

- if the VM option of the given name
does not exist.
**Throws:** IllegalArgumentException

- if the new value is invalid.
**Throws:** IllegalArgumentException

- if the VM option is not writable.
**Throws:** NullPointerException

- if name or value is

null

.
**Throws:** SecurityException

- if a security manager exists and the caller does not have
ManagementPermission("control").

---

#### Method Detail

dumpHeap

```java
void dumpHeap​(
String
outputFile,
boolean live)
throws
IOException
```

Dumps the heap to the

outputFile

file in the same
format as the hprof heap dump.

If this method is called remotely from another process,
the heap dump output is written to a file named

outputFile

on the machine where the target VM is running. If outputFile is
a relative path, it is relative to the working directory where
the target VM was started.

**Parameters:** outputFile

- the system-dependent filename
**Parameters:** live

- if

true

dump only

live

objects
i.e. objects that are reachable from others
**Throws:** IOException

- if the

outputFile

already exists,
cannot be created, opened, or written to.
**Throws:** UnsupportedOperationException

- if this operation is not supported.
**Throws:** IllegalArgumentException

- if

outputFile

does not end with ".hprof" suffix.
**Throws:** NullPointerException

- if

outputFile

is

null

.
**Throws:** SecurityException

- If a security manager exists and its

SecurityManager.checkWrite(java.lang.String)

method denies write access to the named file
or the caller does not have ManagmentPermission("control").

---

#### dumpHeap

void dumpHeap​(

String

outputFile,
boolean live)
throws

IOException

Dumps the heap to the

outputFile

file in the same
format as the hprof heap dump.

If this method is called remotely from another process,
the heap dump output is written to a file named

outputFile

on the machine where the target VM is running. If outputFile is
a relative path, it is relative to the working directory where
the target VM was started.

If this method is called remotely from another process,
the heap dump output is written to a file named

outputFile

on the machine where the target VM is running. If outputFile is
a relative path, it is relative to the working directory where
the target VM was started.

getDiagnosticOptions

```java
List
<
VMOption
> getDiagnosticOptions()
```

Returns a list of

VMOption

objects for all diagnostic options.
A diagnostic option is a

writeable

VM option that can be set dynamically mainly for troubleshooting
and diagnosis.

**Returns:** a list of

VMOption

objects for all diagnostic options.

---

#### getDiagnosticOptions

List

<

VMOption

> getDiagnosticOptions()

Returns a list of

VMOption

objects for all diagnostic options.
A diagnostic option is a

writeable

VM option that can be set dynamically mainly for troubleshooting
and diagnosis.

getVMOption

```java
VMOption
getVMOption​(
String
name)
```

Returns a

VMOption

object for a VM option of the given
name.

**Returns:** a

VMOption

object for a VM option of the given name.
**Throws:** NullPointerException

- if name is

null

.
**Throws:** IllegalArgumentException

- if a VM option of the given name
does not exist.

---

#### getVMOption

VMOption

getVMOption​(

String

name)

Returns a

VMOption

object for a VM option of the given
name.

setVMOption

```java
void setVMOption​(
String
name,

String
value)
```

Sets a VM option of the given name to the specified value.
The new value will be reflected in a new

VMOption

object returned by the

getVMOption(java.lang.String)

method or
the

getDiagnosticOptions()

method. This method does
not change the value of this

VMOption

object.

**Parameters:** name

- Name of a VM option
**Parameters:** value

- New value of the VM option to be set
**Throws:** IllegalArgumentException

- if the VM option of the given name
does not exist.
**Throws:** IllegalArgumentException

- if the new value is invalid.
**Throws:** IllegalArgumentException

- if the VM option is not writable.
**Throws:** NullPointerException

- if name or value is

null

.
**Throws:** SecurityException

- if a security manager exists and the caller does not have
ManagementPermission("control").

---

#### setVMOption

void setVMOption​(

String

name,

String

value)

Sets a VM option of the given name to the specified value.
The new value will be reflected in a new

VMOption

object returned by the

getVMOption(java.lang.String)

method or
the

getDiagnosticOptions()

method. This method does
not change the value of this

VMOption

object.

---

