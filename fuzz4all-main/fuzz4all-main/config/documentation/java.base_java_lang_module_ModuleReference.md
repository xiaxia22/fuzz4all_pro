# Class ModuleReference

**Source:** `java.base\java\lang\module\ModuleReference.html`

### Class Description

```java
public abstract class
ModuleReference

extends
Object
```

A reference to a module's content.

A module reference is a concrete implementation of this class that
implements the abstract methods defined by this class. It contains the
module's descriptor and its location, if known. It also has the ability to
create a

ModuleReader

in order to access the module's content, which
may be inside the Java run-time system itself or in an artifact such as a
modular JAR file.

**Since:** 9
**See Also:** ModuleFinder

,

ModuleReader

---

### Field Details

*No entries found.*

### Constructor Details

#### protected ModuleReference​(
ModuleDescriptor
descriptor,

URI
location)

Constructs a new instance of this class.

**Parameters:**
- descriptor

- The module descriptor
- location

- The module location or

null

if not known

---

### Method Details

#### public final
ModuleDescriptor
descriptor()

Returns the module descriptor.

**Returns:**
- The module descriptor

---

#### public final
Optional
<
URI
> location()

Returns the location of this module's content, if known.

This URI, when present, can be used as the

location

value of a

CodeSource

so that a module's classes can be
granted specific permissions when loaded by a

SecureClassLoader

.

**Returns:**
- The location or an empty

Optional

if not known

---

#### public abstract
ModuleReader
open()
throws
IOException

Opens the module content for reading.

**Returns:**
- A

ModuleReader

to read the module

**Throws:**
- IOException

- If an I/O error occurs
- SecurityException

- If denied by the security manager

---

### Additional Sections

#### Class ModuleReference

java.lang.Object

- java.lang.module.ModuleReference

java.lang.module.ModuleReference

```java
public abstract class
ModuleReference

extends
Object
```

A reference to a module's content.

A module reference is a concrete implementation of this class that
implements the abstract methods defined by this class. It contains the
module's descriptor and its location, if known. It also has the ability to
create a

ModuleReader

in order to access the module's content, which
may be inside the Java run-time system itself or in an artifact such as a
modular JAR file.

**Since:** 9
**See Also:** ModuleFinder

,

ModuleReader

public abstract class

ModuleReference

extends

Object

A reference to a module's content.

A module reference is a concrete implementation of this class that
implements the abstract methods defined by this class. It contains the
module's descriptor and its location, if known. It also has the ability to
create a

ModuleReader

in order to access the module's content, which
may be inside the Java run-time system itself or in an artifact such as a
modular JAR file.

A module reference is a concrete implementation of this class that
implements the abstract methods defined by this class. It contains the
module's descriptor and its location, if known. It also has the ability to
create a

ModuleReader

in order to access the module's content, which
may be inside the Java run-time system itself or in an artifact such as a
modular JAR file.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

ModuleReference

​(

ModuleDescriptor

descriptor,

URI

location)

Constructs a new instance of this class.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

ModuleDescriptor

descriptor

()

Returns the module descriptor.

Optional

<

URI

>

location

()

Returns the location of this module's content, if known.

abstract

ModuleReader

open

()

Opens the module content for reading.

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

Modifier

Constructor

Description

protected

ModuleReference

​(

ModuleDescriptor

descriptor,

URI

location)

Constructs a new instance of this class.

---

#### Constructor Summary

Constructs a new instance of this class.

Method Summary

All Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

ModuleDescriptor

descriptor

()

Returns the module descriptor.

Optional

<

URI

>

location

()

Returns the location of this module's content, if known.

abstract

ModuleReader

open

()

Opens the module content for reading.

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

Returns the module descriptor.

Returns the location of this module's content, if known.

Opens the module content for reading.

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

- ModuleReference

```java
protected ModuleReference​(
ModuleDescriptor
descriptor,

URI
location)
```

Constructs a new instance of this class.

**Parameters:** descriptor

- The module descriptor
**Parameters:** location

- The module location or

null

if not known

============ METHOD DETAIL ==========

- Method Detail

- descriptor

```java
public final
ModuleDescriptor
descriptor()
```

Returns the module descriptor.

**Returns:** The module descriptor

- location

```java
public final
Optional
<
URI
> location()
```

Returns the location of this module's content, if known.

This URI, when present, can be used as the

location

value of a

CodeSource

so that a module's classes can be
granted specific permissions when loaded by a

SecureClassLoader

.

**Returns:** The location or an empty

Optional

if not known

- open

```java
public abstract
ModuleReader
open()
throws
IOException
```

Opens the module content for reading.

**Returns:** A

ModuleReader

to read the module
**Throws:** IOException

- If an I/O error occurs
**Throws:** SecurityException

- If denied by the security manager

Constructor Detail

- ModuleReference

```java
protected ModuleReference​(
ModuleDescriptor
descriptor,

URI
location)
```

Constructs a new instance of this class.

**Parameters:** descriptor

- The module descriptor
**Parameters:** location

- The module location or

null

if not known

---

#### Constructor Detail

ModuleReference

```java
protected ModuleReference​(
ModuleDescriptor
descriptor,

URI
location)
```

Constructs a new instance of this class.

**Parameters:** descriptor

- The module descriptor
**Parameters:** location

- The module location or

null

if not known

---

#### ModuleReference

protected ModuleReference​(

ModuleDescriptor

descriptor,

URI

location)

Constructs a new instance of this class.

Method Detail

- descriptor

```java
public final
ModuleDescriptor
descriptor()
```

Returns the module descriptor.

**Returns:** The module descriptor

- location

```java
public final
Optional
<
URI
> location()
```

Returns the location of this module's content, if known.

This URI, when present, can be used as the

location

value of a

CodeSource

so that a module's classes can be
granted specific permissions when loaded by a

SecureClassLoader

.

**Returns:** The location or an empty

Optional

if not known

- open

```java
public abstract
ModuleReader
open()
throws
IOException
```

Opens the module content for reading.

**Returns:** A

ModuleReader

to read the module
**Throws:** IOException

- If an I/O error occurs
**Throws:** SecurityException

- If denied by the security manager

---

#### Method Detail

descriptor

```java
public final
ModuleDescriptor
descriptor()
```

Returns the module descriptor.

**Returns:** The module descriptor

---

#### descriptor

public final

ModuleDescriptor

descriptor()

Returns the module descriptor.

location

```java
public final
Optional
<
URI
> location()
```

Returns the location of this module's content, if known.

This URI, when present, can be used as the

location

value of a

CodeSource

so that a module's classes can be
granted specific permissions when loaded by a

SecureClassLoader

.

**Returns:** The location or an empty

Optional

if not known

---

#### location

public final

Optional

<

URI

> location()

Returns the location of this module's content, if known.

This URI, when present, can be used as the

location

value of a

CodeSource

so that a module's classes can be
granted specific permissions when loaded by a

SecureClassLoader

.

This URI, when present, can be used as the

location

value of a

CodeSource

so that a module's classes can be
granted specific permissions when loaded by a

SecureClassLoader

.

open

```java
public abstract
ModuleReader
open()
throws
IOException
```

Opens the module content for reading.

**Returns:** A

ModuleReader

to read the module
**Throws:** IOException

- If an I/O error occurs
**Throws:** SecurityException

- If denied by the security manager

---

#### open

public abstract

ModuleReader

open()
throws

IOException

Opens the module content for reading.

---

