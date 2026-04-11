# Class Bootstrap

**Source:** `jdk.jdi\com\sun\jdi\Bootstrap.html`

### Class Description

```java
public class
Bootstrap

extends
Object
```

Initial class that provides access to the default implementation
of JDI interfaces. A debugger application uses this class to access the
single instance of the

VirtualMachineManager

interface.

**Since:** 1.3

---

### Field Details

*No entries found.*

### Constructor Details

#### public Bootstrap()

*No description found.*

---

### Method Details

#### public static
VirtualMachineManager
virtualMachineManager()

Returns the virtual machine manager.

May throw an unspecified error if initialization of the

VirtualMachineManager

fails or if the virtual machine manager
is unable to locate or create any

Connectors

.

**Throws:**
- SecurityException

- if a security manager has been
installed and it denies

JDIPermission

("

virtualMachineManager

") or other unspecified
permissions required by the implementation.

---

### Additional Sections

#### Class Bootstrap

java.lang.Object

- com.sun.jdi.Bootstrap

com.sun.jdi.Bootstrap

```java
public class
Bootstrap

extends
Object
```

Initial class that provides access to the default implementation
of JDI interfaces. A debugger application uses this class to access the
single instance of the

VirtualMachineManager

interface.

**Since:** 1.3

public class

Bootstrap

extends

Object

Initial class that provides access to the default implementation
of JDI interfaces. A debugger application uses this class to access the
single instance of the

VirtualMachineManager

interface.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

Bootstrap

()

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

VirtualMachineManager

virtualMachineManager

()

Returns the virtual machine manager.

- Methods declared in class java.lang.

Object

clone

,

equals

,

finalize

,

getClass

,

hashCode

,

notify

,

notifyAll

,

toString

,

wait

,

wait

,

wait

Constructor Summary

Constructors

Constructor

Description

Bootstrap

()

---

#### Constructor Summary

Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

VirtualMachineManager

virtualMachineManager

()

Returns the virtual machine manager.

- Methods declared in class java.lang.

Object

clone

,

equals

,

finalize

,

getClass

,

hashCode

,

notify

,

notifyAll

,

toString

,

wait

,

wait

,

wait

---

#### Method Summary

Returns the virtual machine manager.

Methods declared in class java.lang.

Object

clone

,

equals

,

finalize

,

getClass

,

hashCode

,

notify

,

notifyAll

,

toString

,

wait

,

wait

,

wait

---

#### Methods declared in class java.lang. Object

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- Bootstrap

```java
public Bootstrap()
```

============ METHOD DETAIL ==========

- Method Detail

- virtualMachineManager

```java
public static
VirtualMachineManager
virtualMachineManager()
```

Returns the virtual machine manager.

May throw an unspecified error if initialization of the

VirtualMachineManager

fails or if the virtual machine manager
is unable to locate or create any

Connectors

.

**Throws:** SecurityException

- if a security manager has been
installed and it denies

JDIPermission

("

virtualMachineManager

") or other unspecified
permissions required by the implementation.

Constructor Detail

- Bootstrap

```java
public Bootstrap()
```

---

#### Constructor Detail

Bootstrap

```java
public Bootstrap()
```

---

#### Bootstrap

public Bootstrap()

Method Detail

- virtualMachineManager

```java
public static
VirtualMachineManager
virtualMachineManager()
```

Returns the virtual machine manager.

May throw an unspecified error if initialization of the

VirtualMachineManager

fails or if the virtual machine manager
is unable to locate or create any

Connectors

.

**Throws:** SecurityException

- if a security manager has been
installed and it denies

JDIPermission

("

virtualMachineManager

") or other unspecified
permissions required by the implementation.

---

#### Method Detail

virtualMachineManager

```java
public static
VirtualMachineManager
virtualMachineManager()
```

Returns the virtual machine manager.

May throw an unspecified error if initialization of the

VirtualMachineManager

fails or if the virtual machine manager
is unable to locate or create any

Connectors

.

**Throws:** SecurityException

- if a security manager has been
installed and it denies

JDIPermission

("

virtualMachineManager

") or other unspecified
permissions required by the implementation.

---

#### virtualMachineManager

public static

VirtualMachineManager

virtualMachineManager()

Returns the virtual machine manager.

May throw an unspecified error if initialization of the

VirtualMachineManager

fails or if the virtual machine manager
is unable to locate or create any

Connectors

.

May throw an unspecified error if initialization of the

VirtualMachineManager

fails or if the virtual machine manager
is unable to locate or create any

Connectors

.

---

