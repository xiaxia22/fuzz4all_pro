# Interface ModuleReference

**Source:** `jdk.jdi\com\sun\jdi\ModuleReference.html`

### Class Description

```java
public interface
ModuleReference

extends
ObjectReference
```

A module in the target VM.

Any method on

ModuleReference

which directly or indirectly takes

ModuleReference

as a parameter may throw

VMDisconnectedException

if the target VM is disconnected and the

VMDisconnectEvent

has been or is
available to be read from the

EventQueue

.

Any method on

ModuleReference

which directly or indirectly takes

ModuleReference

as a parameter may throw

VMOutOfMemoryException

if the target VM has run out of memory.

Any method on

ModuleReference

or which directly or indirectly takes

ModuleReference

as a parameter may throw

InvalidModuleException

if the mirrored module has been unloaded.

Not all target virtual machines support this class.
Use

VirtualMachine.canGetModuleInfo()

to determine if the class is supported.

**All Superinterfaces:** Mirror

,

ObjectReference

,

Value

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### String
name()

Returns the module name.
This method returns

null

if this module is an unnamed module.

**Returns:**
- the name of this module.

---

#### ClassLoaderReference
classLoader()

Returns the

ClassLoaderReference

object for this module.

**Returns:**
- the

ClassLoaderReference

object for this module.

---

### Additional Sections

#### Interface ModuleReference

**All Superinterfaces:** Mirror

,

ObjectReference

,

Value

```java
public interface
ModuleReference

extends
ObjectReference
```

A module in the target VM.

Any method on

ModuleReference

which directly or indirectly takes

ModuleReference

as a parameter may throw

VMDisconnectedException

if the target VM is disconnected and the

VMDisconnectEvent

has been or is
available to be read from the

EventQueue

.

Any method on

ModuleReference

which directly or indirectly takes

ModuleReference

as a parameter may throw

VMOutOfMemoryException

if the target VM has run out of memory.

Any method on

ModuleReference

or which directly or indirectly takes

ModuleReference

as a parameter may throw

InvalidModuleException

if the mirrored module has been unloaded.

Not all target virtual machines support this class.
Use

VirtualMachine.canGetModuleInfo()

to determine if the class is supported.

**Since:** 9

public interface

ModuleReference

extends

ObjectReference

A module in the target VM.

Any method on

ModuleReference

which directly or indirectly takes

ModuleReference

as a parameter may throw

VMDisconnectedException

if the target VM is disconnected and the

VMDisconnectEvent

has been or is
available to be read from the

EventQueue

.

Any method on

ModuleReference

which directly or indirectly takes

ModuleReference

as a parameter may throw

VMOutOfMemoryException

if the target VM has run out of memory.

Any method on

ModuleReference

or which directly or indirectly takes

ModuleReference

as a parameter may throw

InvalidModuleException

if the mirrored module has been unloaded.

Not all target virtual machines support this class.
Use

VirtualMachine.canGetModuleInfo()

to determine if the class is supported.

Any method on

ModuleReference

which directly or indirectly takes

ModuleReference

as a parameter may throw

VMDisconnectedException

if the target VM is disconnected and the

VMDisconnectEvent

has been or is
available to be read from the

EventQueue

.

Any method on

ModuleReference

which directly or indirectly takes

ModuleReference

as a parameter may throw

VMOutOfMemoryException

if the target VM has run out of memory.

Any method on

ModuleReference

or which directly or indirectly takes

ModuleReference

as a parameter may throw

InvalidModuleException

if the mirrored module has been unloaded.

Not all target virtual machines support this class.
Use

VirtualMachine.canGetModuleInfo()

to determine if the class is supported.

Any method on

ModuleReference

which directly or indirectly takes

ModuleReference

as a parameter may throw

VMOutOfMemoryException

if the target VM has run out of memory.

Any method on

ModuleReference

or which directly or indirectly takes

ModuleReference

as a parameter may throw

InvalidModuleException

if the mirrored module has been unloaded.

Not all target virtual machines support this class.
Use

VirtualMachine.canGetModuleInfo()

to determine if the class is supported.

Any method on

ModuleReference

or which directly or indirectly takes

ModuleReference

as a parameter may throw

InvalidModuleException

if the mirrored module has been unloaded.

Not all target virtual machines support this class.
Use

VirtualMachine.canGetModuleInfo()

to determine if the class is supported.

=========== FIELD SUMMARY ===========

- Field Summary

- Fields declared in interface com.sun.jdi.

ObjectReference

INVOKE_NONVIRTUAL

,

INVOKE_SINGLE_THREADED

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

ClassLoaderReference

classLoader

()

Returns the

ClassLoaderReference

object for this module.

String

name

()

Returns the module name.

- Methods declared in interface com.sun.jdi.

Mirror

toString

,

virtualMachine

- Methods declared in interface com.sun.jdi.

ObjectReference

disableCollection

,

enableCollection

,

entryCount

,

equals

,

getValue

,

getValues

,

hashCode

,

invokeMethod

,

isCollected

,

owningThread

,

referenceType

,

referringObjects

,

setValue

,

uniqueID

,

waitingThreads

- Methods declared in interface com.sun.jdi.

Value

type

Field Summary

- Fields declared in interface com.sun.jdi.

ObjectReference

INVOKE_NONVIRTUAL

,

INVOKE_SINGLE_THREADED

---

#### Field Summary

Fields declared in interface com.sun.jdi.

ObjectReference

INVOKE_NONVIRTUAL

,

INVOKE_SINGLE_THREADED

---

#### Fields declared in interface com.sun.jdi. ObjectReference

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

ClassLoaderReference

classLoader

()

Returns the

ClassLoaderReference

object for this module.

String

name

()

Returns the module name.

- Methods declared in interface com.sun.jdi.

Mirror

toString

,

virtualMachine

- Methods declared in interface com.sun.jdi.

ObjectReference

disableCollection

,

enableCollection

,

entryCount

,

equals

,

getValue

,

getValues

,

hashCode

,

invokeMethod

,

isCollected

,

owningThread

,

referenceType

,

referringObjects

,

setValue

,

uniqueID

,

waitingThreads

- Methods declared in interface com.sun.jdi.

Value

type

---

#### Method Summary

Returns the

ClassLoaderReference

object for this module.

Returns the module name.

Methods declared in interface com.sun.jdi.

Mirror

toString

,

virtualMachine

---

#### Methods declared in interface com.sun.jdi. Mirror

Methods declared in interface com.sun.jdi.

ObjectReference

disableCollection

,

enableCollection

,

entryCount

,

equals

,

getValue

,

getValues

,

hashCode

,

invokeMethod

,

isCollected

,

owningThread

,

referenceType

,

referringObjects

,

setValue

,

uniqueID

,

waitingThreads

---

#### Methods declared in interface com.sun.jdi. ObjectReference

Methods declared in interface com.sun.jdi.

Value

type

---

#### Methods declared in interface com.sun.jdi. Value

============ METHOD DETAIL ==========

- Method Detail

- name

```java
String
name()
```

Returns the module name.
This method returns

null

if this module is an unnamed module.

**Returns:** the name of this module.

- classLoader

```java
ClassLoaderReference
classLoader()
```

Returns the

ClassLoaderReference

object for this module.

**Returns:** the

ClassLoaderReference

object for this module.

Method Detail

- name

```java
String
name()
```

Returns the module name.
This method returns

null

if this module is an unnamed module.

**Returns:** the name of this module.

- classLoader

```java
ClassLoaderReference
classLoader()
```

Returns the

ClassLoaderReference

object for this module.

**Returns:** the

ClassLoaderReference

object for this module.

---

#### Method Detail

name

```java
String
name()
```

Returns the module name.
This method returns

null

if this module is an unnamed module.

**Returns:** the name of this module.

---

#### name

String

name()

Returns the module name.
This method returns

null

if this module is an unnamed module.

classLoader

```java
ClassLoaderReference
classLoader()
```

Returns the

ClassLoaderReference

object for this module.

**Returns:** the

ClassLoaderReference

object for this module.

---

#### classLoader

ClassLoaderReference

classLoader()

Returns the

ClassLoaderReference

object for this module.

---

