# Interface MemoryManagerMXBean

**Source:** `java.management\java\lang\management\MemoryManagerMXBean.html`

### Class Description

```java
public interface
MemoryManagerMXBean

extends
PlatformManagedObject
```

The management interface for a memory manager.
A memory manager manages one or more memory pools of the
Java virtual machine.

A Java virtual machine has one or more memory managers.
An instance implementing this interface is
an

MXBean

that can be obtained by calling
the

ManagementFactory.getMemoryManagerMXBeans()

method or
from the

platform MBeanServer

method.

The

ObjectName

for uniquely identifying the MXBean for
a memory manager within an MBeanServer is:

java.lang:type=MemoryManager

,name=

manager's name

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

Returns the name representing this memory manager.

**Returns:**
- the name of this memory manager.

---

#### boolean isValid()

Tests if this memory manager is valid in the Java virtual
machine. A memory manager becomes invalid once the Java virtual
machine removes it from the memory system.

**Returns:**
- true

if the memory manager is valid in the
Java virtual machine;

false

otherwise.

---

#### String
[] getMemoryPoolNames()

Returns the name of memory pools that this memory manager manages.

**Returns:**
- an array of

String

objects, each is
the name of a memory pool that this memory manager manages.

---

### Additional Sections

#### Interface MemoryManagerMXBean

**All Superinterfaces:** PlatformManagedObject

**All Known Subinterfaces:** GarbageCollectorMXBean

,

GarbageCollectorMXBean

```java
public interface
MemoryManagerMXBean

extends
PlatformManagedObject
```

The management interface for a memory manager.
A memory manager manages one or more memory pools of the
Java virtual machine.

A Java virtual machine has one or more memory managers.
An instance implementing this interface is
an

MXBean

that can be obtained by calling
the

ManagementFactory.getMemoryManagerMXBeans()

method or
from the

platform MBeanServer

method.

The

ObjectName

for uniquely identifying the MXBean for
a memory manager within an MBeanServer is:

java.lang:type=MemoryManager

,name=

manager's name

It can be obtained by calling the

PlatformManagedObject.getObjectName()

method.

**Since:** 1.5
**See Also:** ManagementFactory.getPlatformMXBeans(Class)

,

MemoryMXBean

,

JMX Specification.

,

Ways to Access MXBeans

public interface

MemoryManagerMXBean

extends

PlatformManagedObject

The management interface for a memory manager.
A memory manager manages one or more memory pools of the
Java virtual machine.

A Java virtual machine has one or more memory managers.
An instance implementing this interface is
an

MXBean

that can be obtained by calling
the

ManagementFactory.getMemoryManagerMXBeans()

method or
from the

platform MBeanServer

method.

The

ObjectName

for uniquely identifying the MXBean for
a memory manager within an MBeanServer is:

java.lang:type=MemoryManager

,name=

manager's name

It can be obtained by calling the

PlatformManagedObject.getObjectName()

method.

A Java virtual machine has one or more memory managers.
An instance implementing this interface is
an

MXBean

that can be obtained by calling
the

ManagementFactory.getMemoryManagerMXBeans()

method or
from the

platform MBeanServer

method.

The

ObjectName

for uniquely identifying the MXBean for
a memory manager within an MBeanServer is:

java.lang:type=MemoryManager

,name=

manager's name

It can be obtained by calling the

PlatformManagedObject.getObjectName()

method.

The

ObjectName

for uniquely identifying the MXBean for
a memory manager within an MBeanServer is:

java.lang:type=MemoryManager

,name=

manager's name

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

[]

getMemoryPoolNames

()

Returns the name of memory pools that this memory manager manages.

String

getName

()

Returns the name representing this memory manager.

boolean

isValid

()

Tests if this memory manager is valid in the Java virtual
machine.

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

[]

getMemoryPoolNames

()

Returns the name of memory pools that this memory manager manages.

String

getName

()

Returns the name representing this memory manager.

boolean

isValid

()

Tests if this memory manager is valid in the Java virtual
machine.

- Methods declared in interface java.lang.management.

PlatformManagedObject

getObjectName

---

#### Method Summary

Returns the name of memory pools that this memory manager manages.

Returns the name representing this memory manager.

Tests if this memory manager is valid in the Java virtual
machine.

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

Returns the name representing this memory manager.

**Returns:** the name of this memory manager.

- isValid

```java
boolean isValid()
```

Tests if this memory manager is valid in the Java virtual
machine. A memory manager becomes invalid once the Java virtual
machine removes it from the memory system.

**Returns:** true

if the memory manager is valid in the
Java virtual machine;

false

otherwise.

- getMemoryPoolNames

```java
String
[] getMemoryPoolNames()
```

Returns the name of memory pools that this memory manager manages.

**Returns:** an array of

String

objects, each is
the name of a memory pool that this memory manager manages.

Method Detail

- getName

```java
String
getName()
```

Returns the name representing this memory manager.

**Returns:** the name of this memory manager.

- isValid

```java
boolean isValid()
```

Tests if this memory manager is valid in the Java virtual
machine. A memory manager becomes invalid once the Java virtual
machine removes it from the memory system.

**Returns:** true

if the memory manager is valid in the
Java virtual machine;

false

otherwise.

- getMemoryPoolNames

```java
String
[] getMemoryPoolNames()
```

Returns the name of memory pools that this memory manager manages.

**Returns:** an array of

String

objects, each is
the name of a memory pool that this memory manager manages.

---

#### Method Detail

getName

```java
String
getName()
```

Returns the name representing this memory manager.

**Returns:** the name of this memory manager.

---

#### getName

String

getName()

Returns the name representing this memory manager.

isValid

```java
boolean isValid()
```

Tests if this memory manager is valid in the Java virtual
machine. A memory manager becomes invalid once the Java virtual
machine removes it from the memory system.

**Returns:** true

if the memory manager is valid in the
Java virtual machine;

false

otherwise.

---

#### isValid

boolean isValid()

Tests if this memory manager is valid in the Java virtual
machine. A memory manager becomes invalid once the Java virtual
machine removes it from the memory system.

getMemoryPoolNames

```java
String
[] getMemoryPoolNames()
```

Returns the name of memory pools that this memory manager manages.

**Returns:** an array of

String

objects, each is
the name of a memory pool that this memory manager manages.

---

#### getMemoryPoolNames

String

[] getMemoryPoolNames()

Returns the name of memory pools that this memory manager manages.

---

