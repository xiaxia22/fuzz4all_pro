# Class VirtualMachineDescriptor

**Source:** `jdk.attach\com\sun\tools\attach\VirtualMachineDescriptor.html`

### Class Description

```java
public class
VirtualMachineDescriptor

extends
Object
```

Describes a Java virtual machine.

A

VirtualMachineDescriptor

is a container class used to
describe a Java virtual machine. It encapsulates an identifier that identifies
a target virtual machine, and a reference to the

AttachProvider

that should be used
when attempting to attach to the virtual machine. The identifier is
implementation-dependent but is typically the process identifier (or pid)
environments where each Java virtual machine runs in its own operating system
process.

A

VirtualMachineDescriptor

also has a

displayName

.
The display name is typically a human readable string that a tool might
display to a user. For example, a tool that shows a list of Java
virtual machines running on a system might use the display name rather
than the identifier. A

VirtualMachineDescriptor

may be
created without a

display name

. In that case the identifier is
used as the

display name

.

VirtualMachineDescriptor

instances are typically created by
invoking the

VirtualMachine.list()

method. This returns the complete list of descriptors to describe the
Java virtual machines known to all installed

attach providers

.

**Since:** 1.6

---

### Field Details

*No entries found.*

### Constructor Details

#### public VirtualMachineDescriptor​(
AttachProvider
provider,

String
id,

String
displayName)

Creates a virtual machine descriptor from the given components.

**Parameters:**
- provider

- The AttachProvider to attach to the Java virtual machine.
- id

- The virtual machine identifier.
- displayName

- The display name.

**Throws:**
- NullPointerException

- If any of the arguments are

null

---

#### public VirtualMachineDescriptor​(
AttachProvider
provider,

String
id)

Creates a virtual machine descriptor from the given components.

This convenience constructor works as if by invoking the
three-argument constructor as follows:

new

VirtualMachineDescriptor

(provider, id, id);

That is, it creates a virtual machine descriptor such that
the

display name

is the same as the virtual machine
identifier.

**Parameters:**
- provider

- The AttachProvider to attach to the Java virtual machine.
- id

- The virtual machine identifier.

**Throws:**
- NullPointerException

- If

provider

or

id

is

null

.

---

### Method Details

#### public
AttachProvider
provider()

Return the

AttachProvider

that this descriptor references.

**Returns:**
- The

AttachProvider

that this descriptor references.

---

#### public
String
id()

Return the identifier component of this descriptor.

**Returns:**
- The identifier component of this descriptor.

---

#### public
String
displayName()

Return the

display name

component of this descriptor.

**Returns:**
- The display name component of this descriptor.

---

#### public int hashCode()

Returns a hash-code value for this VirtualMachineDescriptor. The hash
code is based upon the descriptor's components, and satifies
the general contract of the

Object.hashCode

method.

**Overrides:**
- hashCode

in class

Object

**Returns:**
- A hash-code value for this descriptor.

**See Also:**
- Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### public boolean equals​(
Object
ob)

Tests this VirtualMachineDescriptor for equality with another object.

If the given object is not a VirtualMachineDescriptor then this
method returns

false

. For two VirtualMachineDescriptors to
be considered equal requires that they both reference the same
provider, and their

identifiers

are equal.

This method satisfies the general contract of the

Object.equals

method.

**Overrides:**
- equals

in class

Object

**Parameters:**
- ob

- The object to which this object is to be compared

**Returns:**
- true

if, and only if, the given object is
a VirtualMachineDescriptor that is equal to this
VirtualMachineDescriptor.

**See Also:**
- Object.hashCode()

,

HashMap

---

#### public
String
toString()

Returns the string representation of the

VirtualMachineDescriptor

.

**Overrides:**
- toString

in class

Object

**Returns:**
- a string representation of the object.

---

### Additional Sections

#### Class VirtualMachineDescriptor

java.lang.Object

- com.sun.tools.attach.VirtualMachineDescriptor

com.sun.tools.attach.VirtualMachineDescriptor

```java
public class
VirtualMachineDescriptor

extends
Object
```

Describes a Java virtual machine.

A

VirtualMachineDescriptor

is a container class used to
describe a Java virtual machine. It encapsulates an identifier that identifies
a target virtual machine, and a reference to the

AttachProvider

that should be used
when attempting to attach to the virtual machine. The identifier is
implementation-dependent but is typically the process identifier (or pid)
environments where each Java virtual machine runs in its own operating system
process.

A

VirtualMachineDescriptor

also has a

displayName

.
The display name is typically a human readable string that a tool might
display to a user. For example, a tool that shows a list of Java
virtual machines running on a system might use the display name rather
than the identifier. A

VirtualMachineDescriptor

may be
created without a

display name

. In that case the identifier is
used as the

display name

.

VirtualMachineDescriptor

instances are typically created by
invoking the

VirtualMachine.list()

method. This returns the complete list of descriptors to describe the
Java virtual machines known to all installed

attach providers

.

**Since:** 1.6

public class

VirtualMachineDescriptor

extends

Object

Describes a Java virtual machine.

A

VirtualMachineDescriptor

is a container class used to
describe a Java virtual machine. It encapsulates an identifier that identifies
a target virtual machine, and a reference to the

AttachProvider

that should be used
when attempting to attach to the virtual machine. The identifier is
implementation-dependent but is typically the process identifier (or pid)
environments where each Java virtual machine runs in its own operating system
process.

A

VirtualMachineDescriptor

also has a

displayName

.
The display name is typically a human readable string that a tool might
display to a user. For example, a tool that shows a list of Java
virtual machines running on a system might use the display name rather
than the identifier. A

VirtualMachineDescriptor

may be
created without a

display name

. In that case the identifier is
used as the

display name

.

VirtualMachineDescriptor

instances are typically created by
invoking the

VirtualMachine.list()

method. This returns the complete list of descriptors to describe the
Java virtual machines known to all installed

attach providers

.

A

VirtualMachineDescriptor

is a container class used to
describe a Java virtual machine. It encapsulates an identifier that identifies
a target virtual machine, and a reference to the

AttachProvider

that should be used
when attempting to attach to the virtual machine. The identifier is
implementation-dependent but is typically the process identifier (or pid)
environments where each Java virtual machine runs in its own operating system
process.

A

VirtualMachineDescriptor

also has a

displayName

.
The display name is typically a human readable string that a tool might
display to a user. For example, a tool that shows a list of Java
virtual machines running on a system might use the display name rather
than the identifier. A

VirtualMachineDescriptor

may be
created without a

display name

. In that case the identifier is
used as the

display name

.

VirtualMachineDescriptor

instances are typically created by
invoking the

VirtualMachine.list()

method. This returns the complete list of descriptors to describe the
Java virtual machines known to all installed

attach providers

.

VirtualMachineDescriptor

instances are typically created by
invoking the

VirtualMachine.list()

method. This returns the complete list of descriptors to describe the
Java virtual machines known to all installed

attach providers

.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

VirtualMachineDescriptor

​(

AttachProvider

provider,

String

id)

Creates a virtual machine descriptor from the given components.

VirtualMachineDescriptor

​(

AttachProvider

provider,

String

id,

String

displayName)

Creates a virtual machine descriptor from the given components.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

String

displayName

()

Return the

display name

component of this descriptor.

boolean

equals

​(

Object

ob)

Tests this VirtualMachineDescriptor for equality with another object.

int

hashCode

()

Returns a hash-code value for this VirtualMachineDescriptor.

String

id

()

Return the identifier component of this descriptor.

AttachProvider

provider

()

Return the

AttachProvider

that this descriptor references.

String

toString

()

Returns the string representation of the

VirtualMachineDescriptor

.

- Methods declared in class java.lang.

Object

clone

,

finalize

,

getClass

,

notify

,

notifyAll

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

VirtualMachineDescriptor

​(

AttachProvider

provider,

String

id)

Creates a virtual machine descriptor from the given components.

VirtualMachineDescriptor

​(

AttachProvider

provider,

String

id,

String

displayName)

Creates a virtual machine descriptor from the given components.

---

#### Constructor Summary

Creates a virtual machine descriptor from the given components.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

String

displayName

()

Return the

display name

component of this descriptor.

boolean

equals

​(

Object

ob)

Tests this VirtualMachineDescriptor for equality with another object.

int

hashCode

()

Returns a hash-code value for this VirtualMachineDescriptor.

String

id

()

Return the identifier component of this descriptor.

AttachProvider

provider

()

Return the

AttachProvider

that this descriptor references.

String

toString

()

Returns the string representation of the

VirtualMachineDescriptor

.

- Methods declared in class java.lang.

Object

clone

,

finalize

,

getClass

,

notify

,

notifyAll

,

wait

,

wait

,

wait

---

#### Method Summary

Return the

display name

component of this descriptor.

Tests this VirtualMachineDescriptor for equality with another object.

Returns a hash-code value for this VirtualMachineDescriptor.

Return the identifier component of this descriptor.

Return the

AttachProvider

that this descriptor references.

Returns the string representation of the

VirtualMachineDescriptor

.

Methods declared in class java.lang.

Object

clone

,

finalize

,

getClass

,

notify

,

notifyAll

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

- VirtualMachineDescriptor

```java
public VirtualMachineDescriptor​(
AttachProvider
provider,

String
id,

String
displayName)
```

Creates a virtual machine descriptor from the given components.

**Parameters:** provider

- The AttachProvider to attach to the Java virtual machine.
**Parameters:** id

- The virtual machine identifier.
**Parameters:** displayName

- The display name.
**Throws:** NullPointerException

- If any of the arguments are

null

- VirtualMachineDescriptor

```java
public VirtualMachineDescriptor​(
AttachProvider
provider,

String
id)
```

Creates a virtual machine descriptor from the given components.

This convenience constructor works as if by invoking the
three-argument constructor as follows:

new

VirtualMachineDescriptor

(provider, id, id);

That is, it creates a virtual machine descriptor such that
the

display name

is the same as the virtual machine
identifier.

**Parameters:** provider

- The AttachProvider to attach to the Java virtual machine.
**Parameters:** id

- The virtual machine identifier.
**Throws:** NullPointerException

- If

provider

or

id

is

null

.

============ METHOD DETAIL ==========

- Method Detail

- provider

```java
public
AttachProvider
provider()
```

Return the

AttachProvider

that this descriptor references.

**Returns:** The

AttachProvider

that this descriptor references.

- id

```java
public
String
id()
```

Return the identifier component of this descriptor.

**Returns:** The identifier component of this descriptor.

- displayName

```java
public
String
displayName()
```

Return the

display name

component of this descriptor.

**Returns:** The display name component of this descriptor.

- hashCode

```java
public int hashCode()
```

Returns a hash-code value for this VirtualMachineDescriptor. The hash
code is based upon the descriptor's components, and satifies
the general contract of the

Object.hashCode

method.

**Overrides:** hashCode

in class

Object
**Returns:** A hash-code value for this descriptor.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

- equals

```java
public boolean equals​(
Object
ob)
```

Tests this VirtualMachineDescriptor for equality with another object.

If the given object is not a VirtualMachineDescriptor then this
method returns

false

. For two VirtualMachineDescriptors to
be considered equal requires that they both reference the same
provider, and their

identifiers

are equal.

This method satisfies the general contract of the

Object.equals

method.

**Overrides:** equals

in class

Object
**Parameters:** ob

- The object to which this object is to be compared
**Returns:** true

if, and only if, the given object is
a VirtualMachineDescriptor that is equal to this
VirtualMachineDescriptor.
**See Also:** Object.hashCode()

,

HashMap

- toString

```java
public
String
toString()
```

Returns the string representation of the

VirtualMachineDescriptor

.

**Overrides:** toString

in class

Object
**Returns:** a string representation of the object.

Constructor Detail

- VirtualMachineDescriptor

```java
public VirtualMachineDescriptor​(
AttachProvider
provider,

String
id,

String
displayName)
```

Creates a virtual machine descriptor from the given components.

**Parameters:** provider

- The AttachProvider to attach to the Java virtual machine.
**Parameters:** id

- The virtual machine identifier.
**Parameters:** displayName

- The display name.
**Throws:** NullPointerException

- If any of the arguments are

null

- VirtualMachineDescriptor

```java
public VirtualMachineDescriptor​(
AttachProvider
provider,

String
id)
```

Creates a virtual machine descriptor from the given components.

This convenience constructor works as if by invoking the
three-argument constructor as follows:

new

VirtualMachineDescriptor

(provider, id, id);

That is, it creates a virtual machine descriptor such that
the

display name

is the same as the virtual machine
identifier.

**Parameters:** provider

- The AttachProvider to attach to the Java virtual machine.
**Parameters:** id

- The virtual machine identifier.
**Throws:** NullPointerException

- If

provider

or

id

is

null

.

---

#### Constructor Detail

VirtualMachineDescriptor

```java
public VirtualMachineDescriptor​(
AttachProvider
provider,

String
id,

String
displayName)
```

Creates a virtual machine descriptor from the given components.

**Parameters:** provider

- The AttachProvider to attach to the Java virtual machine.
**Parameters:** id

- The virtual machine identifier.
**Parameters:** displayName

- The display name.
**Throws:** NullPointerException

- If any of the arguments are

null

---

#### VirtualMachineDescriptor

public VirtualMachineDescriptor​(

AttachProvider

provider,

String

id,

String

displayName)

Creates a virtual machine descriptor from the given components.

VirtualMachineDescriptor

```java
public VirtualMachineDescriptor​(
AttachProvider
provider,

String
id)
```

Creates a virtual machine descriptor from the given components.

This convenience constructor works as if by invoking the
three-argument constructor as follows:

new

VirtualMachineDescriptor

(provider, id, id);

That is, it creates a virtual machine descriptor such that
the

display name

is the same as the virtual machine
identifier.

**Parameters:** provider

- The AttachProvider to attach to the Java virtual machine.
**Parameters:** id

- The virtual machine identifier.
**Throws:** NullPointerException

- If

provider

or

id

is

null

.

---

#### VirtualMachineDescriptor

public VirtualMachineDescriptor​(

AttachProvider

provider,

String

id)

Creates a virtual machine descriptor from the given components.

This convenience constructor works as if by invoking the
three-argument constructor as follows:

new

VirtualMachineDescriptor

(provider, id, id);

That is, it creates a virtual machine descriptor such that
the

display name

is the same as the virtual machine
identifier.

This convenience constructor works as if by invoking the
three-argument constructor as follows:

new

VirtualMachineDescriptor

(provider, id, id);

That is, it creates a virtual machine descriptor such that
the

display name

is the same as the virtual machine
identifier.

That is, it creates a virtual machine descriptor such that
the

display name

is the same as the virtual machine
identifier.

Method Detail

- provider

```java
public
AttachProvider
provider()
```

Return the

AttachProvider

that this descriptor references.

**Returns:** The

AttachProvider

that this descriptor references.

- id

```java
public
String
id()
```

Return the identifier component of this descriptor.

**Returns:** The identifier component of this descriptor.

- displayName

```java
public
String
displayName()
```

Return the

display name

component of this descriptor.

**Returns:** The display name component of this descriptor.

- hashCode

```java
public int hashCode()
```

Returns a hash-code value for this VirtualMachineDescriptor. The hash
code is based upon the descriptor's components, and satifies
the general contract of the

Object.hashCode

method.

**Overrides:** hashCode

in class

Object
**Returns:** A hash-code value for this descriptor.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

- equals

```java
public boolean equals​(
Object
ob)
```

Tests this VirtualMachineDescriptor for equality with another object.

If the given object is not a VirtualMachineDescriptor then this
method returns

false

. For two VirtualMachineDescriptors to
be considered equal requires that they both reference the same
provider, and their

identifiers

are equal.

This method satisfies the general contract of the

Object.equals

method.

**Overrides:** equals

in class

Object
**Parameters:** ob

- The object to which this object is to be compared
**Returns:** true

if, and only if, the given object is
a VirtualMachineDescriptor that is equal to this
VirtualMachineDescriptor.
**See Also:** Object.hashCode()

,

HashMap

- toString

```java
public
String
toString()
```

Returns the string representation of the

VirtualMachineDescriptor

.

**Overrides:** toString

in class

Object
**Returns:** a string representation of the object.

---

#### Method Detail

provider

```java
public
AttachProvider
provider()
```

Return the

AttachProvider

that this descriptor references.

**Returns:** The

AttachProvider

that this descriptor references.

---

#### provider

public

AttachProvider

provider()

Return the

AttachProvider

that this descriptor references.

id

```java
public
String
id()
```

Return the identifier component of this descriptor.

**Returns:** The identifier component of this descriptor.

---

#### id

public

String

id()

Return the identifier component of this descriptor.

displayName

```java
public
String
displayName()
```

Return the

display name

component of this descriptor.

**Returns:** The display name component of this descriptor.

---

#### displayName

public

String

displayName()

Return the

display name

component of this descriptor.

hashCode

```java
public int hashCode()
```

Returns a hash-code value for this VirtualMachineDescriptor. The hash
code is based upon the descriptor's components, and satifies
the general contract of the

Object.hashCode

method.

**Overrides:** hashCode

in class

Object
**Returns:** A hash-code value for this descriptor.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### hashCode

public int hashCode()

Returns a hash-code value for this VirtualMachineDescriptor. The hash
code is based upon the descriptor's components, and satifies
the general contract of the

Object.hashCode

method.

equals

```java
public boolean equals​(
Object
ob)
```

Tests this VirtualMachineDescriptor for equality with another object.

If the given object is not a VirtualMachineDescriptor then this
method returns

false

. For two VirtualMachineDescriptors to
be considered equal requires that they both reference the same
provider, and their

identifiers

are equal.

This method satisfies the general contract of the

Object.equals

method.

**Overrides:** equals

in class

Object
**Parameters:** ob

- The object to which this object is to be compared
**Returns:** true

if, and only if, the given object is
a VirtualMachineDescriptor that is equal to this
VirtualMachineDescriptor.
**See Also:** Object.hashCode()

,

HashMap

---

#### equals

public boolean equals​(

Object

ob)

Tests this VirtualMachineDescriptor for equality with another object.

If the given object is not a VirtualMachineDescriptor then this
method returns

false

. For two VirtualMachineDescriptors to
be considered equal requires that they both reference the same
provider, and their

identifiers

are equal.

This method satisfies the general contract of the

Object.equals

method.

If the given object is not a VirtualMachineDescriptor then this
method returns

false

. For two VirtualMachineDescriptors to
be considered equal requires that they both reference the same
provider, and their

identifiers

are equal.

This method satisfies the general contract of the

Object.equals

method.

toString

```java
public
String
toString()
```

Returns the string representation of the

VirtualMachineDescriptor

.

**Overrides:** toString

in class

Object
**Returns:** a string representation of the object.

---

#### toString

public

String

toString()

Returns the string representation of the

VirtualMachineDescriptor

.

---

