# Interface PathSearchingVirtualMachine

**Source:** `jdk.jdi\com\sun\jdi\PathSearchingVirtualMachine.html`

### Class Description

```java
public interface
PathSearchingVirtualMachine

extends
VirtualMachine
```

A virtual machine which searches for classes through paths

**All Superinterfaces:** Mirror

,

VirtualMachine

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### List
<
String
> classPath()

Get the class path for this virtual machine.

**Returns:**
- List

of components of the classpath,
each represented by a

String

.

---

#### List
<
String
> bootClassPath()

Get the boot class path for this virtual machine.

**Returns:**
- List

of components of the boot class path,
each represented by a

String

.

---

#### String
baseDirectory()

Get the base directory used for path searching. Relative directories
in the class path and boot class path can be resolved through
this directory name.

**Returns:**
- the base directory.

---

### Additional Sections

#### Interface PathSearchingVirtualMachine

**All Superinterfaces:** Mirror

,

VirtualMachine

```java
public interface
PathSearchingVirtualMachine

extends
VirtualMachine
```

A virtual machine which searches for classes through paths

**Since:** 1.3

public interface

PathSearchingVirtualMachine

extends

VirtualMachine

A virtual machine which searches for classes through paths

=========== FIELD SUMMARY ===========

- Field Summary

- Fields declared in interface com.sun.jdi.

VirtualMachine

TRACE_ALL

,

TRACE_EVENTS

,

TRACE_NONE

,

TRACE_OBJREFS

,

TRACE_RECEIVES

,

TRACE_REFTYPES

,

TRACE_SENDS

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

String

baseDirectory

()

Get the base directory used for path searching.

List

<

String

>

bootClassPath

()

Get the boot class path for this virtual machine.

List

<

String

>

classPath

()

Get the class path for this virtual machine.

- Methods declared in interface com.sun.jdi.

Mirror

toString

,

virtualMachine

- Methods declared in interface com.sun.jdi.

VirtualMachine

allClasses

,

allModules

,

allThreads

,

canAddMethod

,

canBeModified

,

canForceEarlyReturn

,

canGetBytecodes

,

canGetClassFileVersion

,

canGetConstantPool

,

canGetCurrentContendedMonitor

,

canGetInstanceInfo

,

canGetMethodReturnValues

,

canGetModuleInfo

,

canGetMonitorFrameInfo

,

canGetMonitorInfo

,

canGetOwnedMonitorInfo

,

canGetSourceDebugExtension

,

canGetSyntheticAttribute

,

canPopFrames

,

canRedefineClasses

,

canRequestMonitorEvents

,

canRequestVMDeathEvent

,

canUnrestrictedlyRedefineClasses

,

canUseInstanceFilters

,

canUseSourceNameFilters

,

canWatchFieldAccess

,

canWatchFieldModification

,

classesByName

,

description

,

dispose

,

eventQueue

,

eventRequestManager

,

exit

,

getDefaultStratum

,

instanceCounts

,

mirrorOf

,

mirrorOf

,

mirrorOf

,

mirrorOf

,

mirrorOf

,

mirrorOf

,

mirrorOf

,

mirrorOf

,

mirrorOf

,

mirrorOfVoid

,

name

,

process

,

redefineClasses

,

resume

,

setDebugTraceMode

,

setDefaultStratum

,

suspend

,

topLevelThreadGroups

,

version

Field Summary

- Fields declared in interface com.sun.jdi.

VirtualMachine

TRACE_ALL

,

TRACE_EVENTS

,

TRACE_NONE

,

TRACE_OBJREFS

,

TRACE_RECEIVES

,

TRACE_REFTYPES

,

TRACE_SENDS

---

#### Field Summary

Fields declared in interface com.sun.jdi.

VirtualMachine

TRACE_ALL

,

TRACE_EVENTS

,

TRACE_NONE

,

TRACE_OBJREFS

,

TRACE_RECEIVES

,

TRACE_REFTYPES

,

TRACE_SENDS

---

#### Fields declared in interface com.sun.jdi. VirtualMachine

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

String

baseDirectory

()

Get the base directory used for path searching.

List

<

String

>

bootClassPath

()

Get the boot class path for this virtual machine.

List

<

String

>

classPath

()

Get the class path for this virtual machine.

- Methods declared in interface com.sun.jdi.

Mirror

toString

,

virtualMachine

- Methods declared in interface com.sun.jdi.

VirtualMachine

allClasses

,

allModules

,

allThreads

,

canAddMethod

,

canBeModified

,

canForceEarlyReturn

,

canGetBytecodes

,

canGetClassFileVersion

,

canGetConstantPool

,

canGetCurrentContendedMonitor

,

canGetInstanceInfo

,

canGetMethodReturnValues

,

canGetModuleInfo

,

canGetMonitorFrameInfo

,

canGetMonitorInfo

,

canGetOwnedMonitorInfo

,

canGetSourceDebugExtension

,

canGetSyntheticAttribute

,

canPopFrames

,

canRedefineClasses

,

canRequestMonitorEvents

,

canRequestVMDeathEvent

,

canUnrestrictedlyRedefineClasses

,

canUseInstanceFilters

,

canUseSourceNameFilters

,

canWatchFieldAccess

,

canWatchFieldModification

,

classesByName

,

description

,

dispose

,

eventQueue

,

eventRequestManager

,

exit

,

getDefaultStratum

,

instanceCounts

,

mirrorOf

,

mirrorOf

,

mirrorOf

,

mirrorOf

,

mirrorOf

,

mirrorOf

,

mirrorOf

,

mirrorOf

,

mirrorOf

,

mirrorOfVoid

,

name

,

process

,

redefineClasses

,

resume

,

setDebugTraceMode

,

setDefaultStratum

,

suspend

,

topLevelThreadGroups

,

version

---

#### Method Summary

Get the base directory used for path searching.

Get the boot class path for this virtual machine.

Get the class path for this virtual machine.

Methods declared in interface com.sun.jdi.

Mirror

toString

,

virtualMachine

---

#### Methods declared in interface com.sun.jdi. Mirror

Methods declared in interface com.sun.jdi.

VirtualMachine

allClasses

,

allModules

,

allThreads

,

canAddMethod

,

canBeModified

,

canForceEarlyReturn

,

canGetBytecodes

,

canGetClassFileVersion

,

canGetConstantPool

,

canGetCurrentContendedMonitor

,

canGetInstanceInfo

,

canGetMethodReturnValues

,

canGetModuleInfo

,

canGetMonitorFrameInfo

,

canGetMonitorInfo

,

canGetOwnedMonitorInfo

,

canGetSourceDebugExtension

,

canGetSyntheticAttribute

,

canPopFrames

,

canRedefineClasses

,

canRequestMonitorEvents

,

canRequestVMDeathEvent

,

canUnrestrictedlyRedefineClasses

,

canUseInstanceFilters

,

canUseSourceNameFilters

,

canWatchFieldAccess

,

canWatchFieldModification

,

classesByName

,

description

,

dispose

,

eventQueue

,

eventRequestManager

,

exit

,

getDefaultStratum

,

instanceCounts

,

mirrorOf

,

mirrorOf

,

mirrorOf

,

mirrorOf

,

mirrorOf

,

mirrorOf

,

mirrorOf

,

mirrorOf

,

mirrorOf

,

mirrorOfVoid

,

name

,

process

,

redefineClasses

,

resume

,

setDebugTraceMode

,

setDefaultStratum

,

suspend

,

topLevelThreadGroups

,

version

---

#### Methods declared in interface com.sun.jdi. VirtualMachine

============ METHOD DETAIL ==========

- Method Detail

- classPath

```java
List
<
String
> classPath()
```

Get the class path for this virtual machine.

**Returns:** List

of components of the classpath,
each represented by a

String

.

- bootClassPath

```java
List
<
String
> bootClassPath()
```

Get the boot class path for this virtual machine.

**Returns:** List

of components of the boot class path,
each represented by a

String

.

- baseDirectory

```java
String
baseDirectory()
```

Get the base directory used for path searching. Relative directories
in the class path and boot class path can be resolved through
this directory name.

**Returns:** the base directory.

Method Detail

- classPath

```java
List
<
String
> classPath()
```

Get the class path for this virtual machine.

**Returns:** List

of components of the classpath,
each represented by a

String

.

- bootClassPath

```java
List
<
String
> bootClassPath()
```

Get the boot class path for this virtual machine.

**Returns:** List

of components of the boot class path,
each represented by a

String

.

- baseDirectory

```java
String
baseDirectory()
```

Get the base directory used for path searching. Relative directories
in the class path and boot class path can be resolved through
this directory name.

**Returns:** the base directory.

---

#### Method Detail

classPath

```java
List
<
String
> classPath()
```

Get the class path for this virtual machine.

**Returns:** List

of components of the classpath,
each represented by a

String

.

---

#### classPath

List

<

String

> classPath()

Get the class path for this virtual machine.

bootClassPath

```java
List
<
String
> bootClassPath()
```

Get the boot class path for this virtual machine.

**Returns:** List

of components of the boot class path,
each represented by a

String

.

---

#### bootClassPath

List

<

String

> bootClassPath()

Get the boot class path for this virtual machine.

baseDirectory

```java
String
baseDirectory()
```

Get the base directory used for path searching. Relative directories
in the class path and boot class path can be resolved through
this directory name.

**Returns:** the base directory.

---

#### baseDirectory

String

baseDirectory()

Get the base directory used for path searching. Relative directories
in the class path and boot class path can be resolved through
this directory name.

---

