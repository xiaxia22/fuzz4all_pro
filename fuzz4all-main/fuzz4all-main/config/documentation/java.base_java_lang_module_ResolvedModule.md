# Class ResolvedModule

**Source:** `java.base\java\lang\module\ResolvedModule.html`

### Class Description

```java
public final class
ResolvedModule

extends
Object
```

A module in a graph of

resolved modules

.

ResolvedModule

defines the

configuration

method to get the configuration that the resolved module is in. It defines
the

reference

method to get the reference to the
module's content.

**Since:** 9
**See Also:** Configuration.modules()

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### public
Configuration
configuration()

Returns the configuration that this resolved module is in.

**Returns:**
- The configuration that this resolved module is in

---

#### public
ModuleReference
reference()

Returns the reference to the module's content.

**Returns:**
- The reference to the module's content

---

#### public
String
name()

Returns the module name.

This convenience method is the equivalent to invoking:

```java
reference().descriptor().name()
```

**Returns:**
- The module name

---

#### public
Set
<
ResolvedModule
> reads()

Returns the set of resolved modules that this resolved module reads.

**Returns:**
- A possibly-empty unmodifiable set of resolved modules that
this resolved module reads

---

#### public int hashCode()

Computes a hash code for this resolved module.

The hash code is based upon the components of the resolved module
and satisfies the general contract of the

Object.hashCode

method.

**Overrides:**
- hashCode

in class

Object

**Returns:**
- The hash-code value for this resolved module

**See Also:**
- Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### public boolean equals​(
Object
ob)

Tests this resolved module for equality with the given object.

If the given object is not a

ResolvedModule

then this
method returns

false

. Two

ResolvedModule

objects are
equal if they are in the same configuration and have equal references
to the module content.

This method satisfies the general contract of the

Object.equals

method.

**Overrides:**
- equals

in class

Object

**Parameters:**
- ob

- the object to which this object is to be compared

**Returns:**
- true

if, and only if, the given object is a module
reference that is equal to this module reference

**See Also:**
- Object.hashCode()

,

HashMap

---

#### public
String
toString()

Returns a string describing this resolved module.

**Overrides:**
- toString

in class

Object

**Returns:**
- A string describing this resolved module

---

### Additional Sections

#### Class ResolvedModule

java.lang.Object

- java.lang.module.ResolvedModule

java.lang.module.ResolvedModule

```java
public final class
ResolvedModule

extends
Object
```

A module in a graph of

resolved modules

.

ResolvedModule

defines the

configuration

method to get the configuration that the resolved module is in. It defines
the

reference

method to get the reference to the
module's content.

**Since:** 9
**See Also:** Configuration.modules()

public final class

ResolvedModule

extends

Object

A module in a graph of

resolved modules

.

ResolvedModule

defines the

configuration

method to get the configuration that the resolved module is in. It defines
the

reference

method to get the reference to the
module's content.

ResolvedModule

defines the

configuration

method to get the configuration that the resolved module is in. It defines
the

reference

method to get the reference to the
module's content.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Configuration

configuration

()

Returns the configuration that this resolved module is in.

boolean

equals

​(

Object

ob)

Tests this resolved module for equality with the given object.

int

hashCode

()

Computes a hash code for this resolved module.

String

name

()

Returns the module name.

Set

<

ResolvedModule

>

reads

()

Returns the set of resolved modules that this resolved module reads.

ModuleReference

reference

()

Returns the reference to the module's content.

String

toString

()

Returns a string describing this resolved module.

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

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Configuration

configuration

()

Returns the configuration that this resolved module is in.

boolean

equals

​(

Object

ob)

Tests this resolved module for equality with the given object.

int

hashCode

()

Computes a hash code for this resolved module.

String

name

()

Returns the module name.

Set

<

ResolvedModule

>

reads

()

Returns the set of resolved modules that this resolved module reads.

ModuleReference

reference

()

Returns the reference to the module's content.

String

toString

()

Returns a string describing this resolved module.

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

Returns the configuration that this resolved module is in.

Tests this resolved module for equality with the given object.

Computes a hash code for this resolved module.

Returns the module name.

Returns the set of resolved modules that this resolved module reads.

Returns the reference to the module's content.

Returns a string describing this resolved module.

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

============ METHOD DETAIL ==========

- Method Detail

- configuration

```java
public
Configuration
configuration()
```

Returns the configuration that this resolved module is in.

**Returns:** The configuration that this resolved module is in

- reference

```java
public
ModuleReference
reference()
```

Returns the reference to the module's content.

**Returns:** The reference to the module's content

- name

```java
public
String
name()
```

Returns the module name.

This convenience method is the equivalent to invoking:

```java
reference().descriptor().name()
```

**Returns:** The module name

- reads

```java
public
Set
<
ResolvedModule
> reads()
```

Returns the set of resolved modules that this resolved module reads.

**Returns:** A possibly-empty unmodifiable set of resolved modules that
this resolved module reads

- hashCode

```java
public int hashCode()
```

Computes a hash code for this resolved module.

The hash code is based upon the components of the resolved module
and satisfies the general contract of the

Object.hashCode

method.

**Overrides:** hashCode

in class

Object
**Returns:** The hash-code value for this resolved module
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

- equals

```java
public boolean equals​(
Object
ob)
```

Tests this resolved module for equality with the given object.

If the given object is not a

ResolvedModule

then this
method returns

false

. Two

ResolvedModule

objects are
equal if they are in the same configuration and have equal references
to the module content.

This method satisfies the general contract of the

Object.equals

method.

**Overrides:** equals

in class

Object
**Parameters:** ob

- the object to which this object is to be compared
**Returns:** true

if, and only if, the given object is a module
reference that is equal to this module reference
**See Also:** Object.hashCode()

,

HashMap

- toString

```java
public
String
toString()
```

Returns a string describing this resolved module.

**Overrides:** toString

in class

Object
**Returns:** A string describing this resolved module

Method Detail

- configuration

```java
public
Configuration
configuration()
```

Returns the configuration that this resolved module is in.

**Returns:** The configuration that this resolved module is in

- reference

```java
public
ModuleReference
reference()
```

Returns the reference to the module's content.

**Returns:** The reference to the module's content

- name

```java
public
String
name()
```

Returns the module name.

This convenience method is the equivalent to invoking:

```java
reference().descriptor().name()
```

**Returns:** The module name

- reads

```java
public
Set
<
ResolvedModule
> reads()
```

Returns the set of resolved modules that this resolved module reads.

**Returns:** A possibly-empty unmodifiable set of resolved modules that
this resolved module reads

- hashCode

```java
public int hashCode()
```

Computes a hash code for this resolved module.

The hash code is based upon the components of the resolved module
and satisfies the general contract of the

Object.hashCode

method.

**Overrides:** hashCode

in class

Object
**Returns:** The hash-code value for this resolved module
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

- equals

```java
public boolean equals​(
Object
ob)
```

Tests this resolved module for equality with the given object.

If the given object is not a

ResolvedModule

then this
method returns

false

. Two

ResolvedModule

objects are
equal if they are in the same configuration and have equal references
to the module content.

This method satisfies the general contract of the

Object.equals

method.

**Overrides:** equals

in class

Object
**Parameters:** ob

- the object to which this object is to be compared
**Returns:** true

if, and only if, the given object is a module
reference that is equal to this module reference
**See Also:** Object.hashCode()

,

HashMap

- toString

```java
public
String
toString()
```

Returns a string describing this resolved module.

**Overrides:** toString

in class

Object
**Returns:** A string describing this resolved module

---

#### Method Detail

configuration

```java
public
Configuration
configuration()
```

Returns the configuration that this resolved module is in.

**Returns:** The configuration that this resolved module is in

---

#### configuration

public

Configuration

configuration()

Returns the configuration that this resolved module is in.

reference

```java
public
ModuleReference
reference()
```

Returns the reference to the module's content.

**Returns:** The reference to the module's content

---

#### reference

public

ModuleReference

reference()

Returns the reference to the module's content.

name

```java
public
String
name()
```

Returns the module name.

This convenience method is the equivalent to invoking:

```java
reference().descriptor().name()
```

**Returns:** The module name

---

#### name

public

String

name()

Returns the module name.

This convenience method is the equivalent to invoking:

```java
reference().descriptor().name()
```

reference().descriptor().name()

reads

```java
public
Set
<
ResolvedModule
> reads()
```

Returns the set of resolved modules that this resolved module reads.

**Returns:** A possibly-empty unmodifiable set of resolved modules that
this resolved module reads

---

#### reads

public

Set

<

ResolvedModule

> reads()

Returns the set of resolved modules that this resolved module reads.

hashCode

```java
public int hashCode()
```

Computes a hash code for this resolved module.

The hash code is based upon the components of the resolved module
and satisfies the general contract of the

Object.hashCode

method.

**Overrides:** hashCode

in class

Object
**Returns:** The hash-code value for this resolved module
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### hashCode

public int hashCode()

Computes a hash code for this resolved module.

The hash code is based upon the components of the resolved module
and satisfies the general contract of the

Object.hashCode

method.

The hash code is based upon the components of the resolved module
and satisfies the general contract of the

Object.hashCode

method.

equals

```java
public boolean equals​(
Object
ob)
```

Tests this resolved module for equality with the given object.

If the given object is not a

ResolvedModule

then this
method returns

false

. Two

ResolvedModule

objects are
equal if they are in the same configuration and have equal references
to the module content.

This method satisfies the general contract of the

Object.equals

method.

**Overrides:** equals

in class

Object
**Parameters:** ob

- the object to which this object is to be compared
**Returns:** true

if, and only if, the given object is a module
reference that is equal to this module reference
**See Also:** Object.hashCode()

,

HashMap

---

#### equals

public boolean equals​(

Object

ob)

Tests this resolved module for equality with the given object.

If the given object is not a

ResolvedModule

then this
method returns

false

. Two

ResolvedModule

objects are
equal if they are in the same configuration and have equal references
to the module content.

This method satisfies the general contract of the

Object.equals

method.

If the given object is not a

ResolvedModule

then this
method returns

false

. Two

ResolvedModule

objects are
equal if they are in the same configuration and have equal references
to the module content.

This method satisfies the general contract of the

Object.equals

method.

toString

```java
public
String
toString()
```

Returns a string describing this resolved module.

**Overrides:** toString

in class

Object
**Returns:** A string describing this resolved module

---

#### toString

public

String

toString()

Returns a string describing this resolved module.

---

