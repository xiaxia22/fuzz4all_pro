# Class MemoryUsage

**Source:** `java.management\java\lang\management\MemoryUsage.html`

### Class Description

```java
public class
MemoryUsage

extends
Object
```

A

MemoryUsage

object represents a snapshot of memory usage.
Instances of the

MemoryUsage

class are usually constructed
by methods that are used to obtain memory usage
information about individual memory pool of the Java virtual machine or
the heap or non-heap memory of the Java virtual machine as a whole.

A

MemoryUsage

object contains four values:

Describes the MemoryUsage object content

Value

Description

init

represents the initial amount of memory (in bytes) that
the Java virtual machine requests from the operating system
for memory management during startup. The Java virtual machine
may request additional memory from the operating system and
may also release memory to the system over time.
The value of

init

may be undefined.

used

represents the amount of memory currently used (in bytes).

committed

represents the amount of memory (in bytes) that is
guaranteed to be available for use by the Java virtual machine.
The amount of committed memory may change over time (increase
or decrease). The Java virtual machine may release memory to
the system and

committed

could be less than

init

.

committed

will always be greater than
or equal to

used

.

max

represents the maximum amount of memory (in bytes)
that can be used for memory management. Its value may be undefined.
The maximum amount of memory may change over time if defined.
The amount of used and committed memory will always be less than
or equal to

max

if

max

is defined.
A memory allocation may fail if it attempts to increase the
used memory such that

used > committed

even
if

used <= max

would still be true (for example,
when the system is low on virtual memory).

Below is a picture showing an example of a memory pool:

```java
+----------------------------------------------+
+//////////////// | +
+//////////////// | +
+----------------------------------------------+

|--------|
init
|---------------|
used
|---------------------------|
committed
|----------------------------------------------|
max
```

MXBean Mapping

MemoryUsage

is mapped to a

CompositeData

with attributes as specified in the

from

method.

**Since:** 1.5

---

### Field Details

*No entries found.*

### Constructor Details

#### public MemoryUsage​(long init,
long used,
long committed,
long max)

Constructs a

MemoryUsage

object.

**Parameters:**
- init

- the initial amount of memory in bytes that
the Java virtual machine allocates;
or

-1

if undefined.
- used

- the amount of used memory in bytes.
- committed

- the amount of committed memory in bytes.
- max

- the maximum amount of memory in bytes that
can be used; or

-1

if undefined.

**Throws:**
- IllegalArgumentException

- if

- the value of

init

or

max

is negative
but not

-1

; or
- the value of

used

or

committed

is negative;
or
- used

is greater than the value of

committed

;
or
- committed

is greater than the value of

max

max

if defined.

---

### Method Details

#### public long getInit()

Returns the amount of memory in bytes that the Java virtual machine
initially requests from the operating system for memory management.
This method returns

-1

if the initial memory size is undefined.

**Returns:**
- the initial size of memory in bytes;

-1

if undefined.

---

#### public long getUsed()

Returns the amount of used memory in bytes.

**Returns:**
- the amount of used memory in bytes.

---

#### public long getCommitted()

Returns the amount of memory in bytes that is committed for
the Java virtual machine to use. This amount of memory is
guaranteed for the Java virtual machine to use.

**Returns:**
- the amount of committed memory in bytes.

---

#### public long getMax()

Returns the maximum amount of memory in bytes that can be
used for memory management. This method returns

-1

if the maximum memory size is undefined.

This amount of memory is not guaranteed to be available
for memory management if it is greater than the amount of
committed memory. The Java virtual machine may fail to allocate
memory even if the amount of used memory does not exceed this
maximum size.

**Returns:**
- the maximum amount of memory in bytes;

-1

if undefined.

---

#### public
String
toString()

Returns a descriptive representation of this memory usage.

**Overrides:**
- toString

in class

Object

**Returns:**
- a string representation of the object.

---

#### public static
MemoryUsage
from​(
CompositeData
cd)

Returns a

MemoryUsage

object represented by the
given

CompositeData

. The given

CompositeData

must contain the following attributes:

The attributes and the types the given CompositeData contains

Attribute Name

Type

init

java.lang.Long

used

java.lang.Long

committed

java.lang.Long

max

java.lang.Long

**Parameters:**
- cd

-

CompositeData

representing a

MemoryUsage

**Returns:**
- a

MemoryUsage

object represented by

cd

if

cd

is not

null

;

null

otherwise.

**Throws:**
- IllegalArgumentException

- if

cd

does not
represent a

MemoryUsage

with the attributes described
above.

---

### Additional Sections

#### Class MemoryUsage

java.lang.Object

- java.lang.management.MemoryUsage

java.lang.management.MemoryUsage

```java
public class
MemoryUsage

extends
Object
```

A

MemoryUsage

object represents a snapshot of memory usage.
Instances of the

MemoryUsage

class are usually constructed
by methods that are used to obtain memory usage
information about individual memory pool of the Java virtual machine or
the heap or non-heap memory of the Java virtual machine as a whole.

A

MemoryUsage

object contains four values:

Describes the MemoryUsage object content

Value

Description

init

represents the initial amount of memory (in bytes) that
the Java virtual machine requests from the operating system
for memory management during startup. The Java virtual machine
may request additional memory from the operating system and
may also release memory to the system over time.
The value of

init

may be undefined.

used

represents the amount of memory currently used (in bytes).

committed

represents the amount of memory (in bytes) that is
guaranteed to be available for use by the Java virtual machine.
The amount of committed memory may change over time (increase
or decrease). The Java virtual machine may release memory to
the system and

committed

could be less than

init

.

committed

will always be greater than
or equal to

used

.

max

represents the maximum amount of memory (in bytes)
that can be used for memory management. Its value may be undefined.
The maximum amount of memory may change over time if defined.
The amount of used and committed memory will always be less than
or equal to

max

if

max

is defined.
A memory allocation may fail if it attempts to increase the
used memory such that

used > committed

even
if

used <= max

would still be true (for example,
when the system is low on virtual memory).

Below is a picture showing an example of a memory pool:

```java
+----------------------------------------------+
+//////////////// | +
+//////////////// | +
+----------------------------------------------+

|--------|
init
|---------------|
used
|---------------------------|
committed
|----------------------------------------------|
max
```

MXBean Mapping

MemoryUsage

is mapped to a

CompositeData

with attributes as specified in the

from

method.

**Since:** 1.5

public class

MemoryUsage

extends

Object

A

MemoryUsage

object represents a snapshot of memory usage.
Instances of the

MemoryUsage

class are usually constructed
by methods that are used to obtain memory usage
information about individual memory pool of the Java virtual machine or
the heap or non-heap memory of the Java virtual machine as a whole.

A

MemoryUsage

object contains four values:

Describes the MemoryUsage object content

Value

Description

init

represents the initial amount of memory (in bytes) that
the Java virtual machine requests from the operating system
for memory management during startup. The Java virtual machine
may request additional memory from the operating system and
may also release memory to the system over time.
The value of

init

may be undefined.

used

represents the amount of memory currently used (in bytes).

committed

represents the amount of memory (in bytes) that is
guaranteed to be available for use by the Java virtual machine.
The amount of committed memory may change over time (increase
or decrease). The Java virtual machine may release memory to
the system and

committed

could be less than

init

.

committed

will always be greater than
or equal to

used

.

max

represents the maximum amount of memory (in bytes)
that can be used for memory management. Its value may be undefined.
The maximum amount of memory may change over time if defined.
The amount of used and committed memory will always be less than
or equal to

max

if

max

is defined.
A memory allocation may fail if it attempts to increase the
used memory such that

used > committed

even
if

used <= max

would still be true (for example,
when the system is low on virtual memory).

Below is a picture showing an example of a memory pool:

```java
+----------------------------------------------+
+//////////////// | +
+//////////////// | +
+----------------------------------------------+

|--------|
init
|---------------|
used
|---------------------------|
committed
|----------------------------------------------|
max
```

MXBean Mapping

MemoryUsage

is mapped to a

CompositeData

with attributes as specified in the

from

method.

A

MemoryUsage

object contains four values:

Describes the MemoryUsage object content

Value

Description

init

represents the initial amount of memory (in bytes) that
the Java virtual machine requests from the operating system
for memory management during startup. The Java virtual machine
may request additional memory from the operating system and
may also release memory to the system over time.
The value of

init

may be undefined.

used

represents the amount of memory currently used (in bytes).

committed

represents the amount of memory (in bytes) that is
guaranteed to be available for use by the Java virtual machine.
The amount of committed memory may change over time (increase
or decrease). The Java virtual machine may release memory to
the system and

committed

could be less than

init

.

committed

will always be greater than
or equal to

used

.

max

represents the maximum amount of memory (in bytes)
that can be used for memory management. Its value may be undefined.
The maximum amount of memory may change over time if defined.
The amount of used and committed memory will always be less than
or equal to

max

if

max

is defined.
A memory allocation may fail if it attempts to increase the
used memory such that

used > committed

even
if

used <= max

would still be true (for example,
when the system is low on virtual memory).

Below is a picture showing an example of a memory pool:

```java
+----------------------------------------------+
+//////////////// | +
+//////////////// | +
+----------------------------------------------+

|--------|
init
|---------------|
used
|---------------------------|
committed
|----------------------------------------------|
max
```

MXBean Mapping

MemoryUsage

is mapped to a

CompositeData

with attributes as specified in the

from

method.

+----------------------------------------------+
+//////////////// | +
+//////////////// | +
+----------------------------------------------+

|--------|
init
|---------------|
used
|---------------------------|
committed
|----------------------------------------------|
max

---

#### MXBean Mapping

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

MemoryUsage

​(long init,
long used,
long committed,
long max)

Constructs a

MemoryUsage

object.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

static

MemoryUsage

from

​(

CompositeData

cd)

Returns a

MemoryUsage

object represented by the
given

CompositeData

.

long

getCommitted

()

Returns the amount of memory in bytes that is committed for
the Java virtual machine to use.

long

getInit

()

Returns the amount of memory in bytes that the Java virtual machine
initially requests from the operating system for memory management.

long

getMax

()

Returns the maximum amount of memory in bytes that can be
used for memory management.

long

getUsed

()

Returns the amount of used memory in bytes.

String

toString

()

Returns a descriptive representation of this memory usage.

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

wait

,

wait

,

wait

Constructor Summary

Constructors

Constructor

Description

MemoryUsage

​(long init,
long used,
long committed,
long max)

Constructs a

MemoryUsage

object.

---

#### Constructor Summary

Constructs a

MemoryUsage

object.

Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

static

MemoryUsage

from

​(

CompositeData

cd)

Returns a

MemoryUsage

object represented by the
given

CompositeData

.

long

getCommitted

()

Returns the amount of memory in bytes that is committed for
the Java virtual machine to use.

long

getInit

()

Returns the amount of memory in bytes that the Java virtual machine
initially requests from the operating system for memory management.

long

getMax

()

Returns the maximum amount of memory in bytes that can be
used for memory management.

long

getUsed

()

Returns the amount of used memory in bytes.

String

toString

()

Returns a descriptive representation of this memory usage.

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

wait

,

wait

,

wait

---

#### Method Summary

Returns a

MemoryUsage

object represented by the
given

CompositeData

.

Returns the amount of memory in bytes that is committed for
the Java virtual machine to use.

Returns the amount of memory in bytes that the Java virtual machine
initially requests from the operating system for memory management.

Returns the maximum amount of memory in bytes that can be
used for memory management.

Returns the amount of used memory in bytes.

Returns a descriptive representation of this memory usage.

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

wait

,

wait

,

wait

---

#### Methods declared in class java.lang. Object

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- MemoryUsage

```java
public MemoryUsage​(long init,
long used,
long committed,
long max)
```

Constructs a

MemoryUsage

object.

**Parameters:** init

- the initial amount of memory in bytes that
the Java virtual machine allocates;
or

-1

if undefined.
**Parameters:** used

- the amount of used memory in bytes.
**Parameters:** committed

- the amount of committed memory in bytes.
**Parameters:** max

- the maximum amount of memory in bytes that
can be used; or

-1

if undefined.
**Throws:** IllegalArgumentException

- if

- the value of

init

or

max

is negative
but not

-1

; or
- the value of

used

or

committed

is negative;
or
- used

is greater than the value of

committed

;
or
- committed

is greater than the value of

max

max

if defined.

============ METHOD DETAIL ==========

- Method Detail

- getInit

```java
public long getInit()
```

Returns the amount of memory in bytes that the Java virtual machine
initially requests from the operating system for memory management.
This method returns

-1

if the initial memory size is undefined.

**Returns:** the initial size of memory in bytes;

-1

if undefined.

- getUsed

```java
public long getUsed()
```

Returns the amount of used memory in bytes.

**Returns:** the amount of used memory in bytes.

- getCommitted

```java
public long getCommitted()
```

Returns the amount of memory in bytes that is committed for
the Java virtual machine to use. This amount of memory is
guaranteed for the Java virtual machine to use.

**Returns:** the amount of committed memory in bytes.

- getMax

```java
public long getMax()
```

Returns the maximum amount of memory in bytes that can be
used for memory management. This method returns

-1

if the maximum memory size is undefined.

This amount of memory is not guaranteed to be available
for memory management if it is greater than the amount of
committed memory. The Java virtual machine may fail to allocate
memory even if the amount of used memory does not exceed this
maximum size.

**Returns:** the maximum amount of memory in bytes;

-1

if undefined.

- toString

```java
public
String
toString()
```

Returns a descriptive representation of this memory usage.

**Overrides:** toString

in class

Object
**Returns:** a string representation of the object.

- from

```java
public static
MemoryUsage
from​(
CompositeData
cd)
```

Returns a

MemoryUsage

object represented by the
given

CompositeData

. The given

CompositeData

must contain the following attributes:

The attributes and the types the given CompositeData contains

Attribute Name

Type

init

java.lang.Long

used

java.lang.Long

committed

java.lang.Long

max

java.lang.Long

**Parameters:** cd

-

CompositeData

representing a

MemoryUsage
**Returns:** a

MemoryUsage

object represented by

cd

if

cd

is not

null

;

null

otherwise.
**Throws:** IllegalArgumentException

- if

cd

does not
represent a

MemoryUsage

with the attributes described
above.

Constructor Detail

- MemoryUsage

```java
public MemoryUsage​(long init,
long used,
long committed,
long max)
```

Constructs a

MemoryUsage

object.

**Parameters:** init

- the initial amount of memory in bytes that
the Java virtual machine allocates;
or

-1

if undefined.
**Parameters:** used

- the amount of used memory in bytes.
**Parameters:** committed

- the amount of committed memory in bytes.
**Parameters:** max

- the maximum amount of memory in bytes that
can be used; or

-1

if undefined.
**Throws:** IllegalArgumentException

- if

- the value of

init

or

max

is negative
but not

-1

; or
- the value of

used

or

committed

is negative;
or
- used

is greater than the value of

committed

;
or
- committed

is greater than the value of

max

max

if defined.

---

#### Constructor Detail

MemoryUsage

```java
public MemoryUsage​(long init,
long used,
long committed,
long max)
```

Constructs a

MemoryUsage

object.

**Parameters:** init

- the initial amount of memory in bytes that
the Java virtual machine allocates;
or

-1

if undefined.
**Parameters:** used

- the amount of used memory in bytes.
**Parameters:** committed

- the amount of committed memory in bytes.
**Parameters:** max

- the maximum amount of memory in bytes that
can be used; or

-1

if undefined.
**Throws:** IllegalArgumentException

- if

- the value of

init

or

max

is negative
but not

-1

; or
- the value of

used

or

committed

is negative;
or
- used

is greater than the value of

committed

;
or
- committed

is greater than the value of

max

max

if defined.

---

#### MemoryUsage

public MemoryUsage​(long init,
long used,
long committed,
long max)

Constructs a

MemoryUsage

object.

the value of

init

or

max

is negative
but not

-1

; or

the value of

used

or

committed

is negative;
or

used

is greater than the value of

committed

;
or

committed

is greater than the value of

max

max

if defined.

Method Detail

- getInit

```java
public long getInit()
```

Returns the amount of memory in bytes that the Java virtual machine
initially requests from the operating system for memory management.
This method returns

-1

if the initial memory size is undefined.

**Returns:** the initial size of memory in bytes;

-1

if undefined.

- getUsed

```java
public long getUsed()
```

Returns the amount of used memory in bytes.

**Returns:** the amount of used memory in bytes.

- getCommitted

```java
public long getCommitted()
```

Returns the amount of memory in bytes that is committed for
the Java virtual machine to use. This amount of memory is
guaranteed for the Java virtual machine to use.

**Returns:** the amount of committed memory in bytes.

- getMax

```java
public long getMax()
```

Returns the maximum amount of memory in bytes that can be
used for memory management. This method returns

-1

if the maximum memory size is undefined.

This amount of memory is not guaranteed to be available
for memory management if it is greater than the amount of
committed memory. The Java virtual machine may fail to allocate
memory even if the amount of used memory does not exceed this
maximum size.

**Returns:** the maximum amount of memory in bytes;

-1

if undefined.

- toString

```java
public
String
toString()
```

Returns a descriptive representation of this memory usage.

**Overrides:** toString

in class

Object
**Returns:** a string representation of the object.

- from

```java
public static
MemoryUsage
from​(
CompositeData
cd)
```

Returns a

MemoryUsage

object represented by the
given

CompositeData

. The given

CompositeData

must contain the following attributes:

The attributes and the types the given CompositeData contains

Attribute Name

Type

init

java.lang.Long

used

java.lang.Long

committed

java.lang.Long

max

java.lang.Long

**Parameters:** cd

-

CompositeData

representing a

MemoryUsage
**Returns:** a

MemoryUsage

object represented by

cd

if

cd

is not

null

;

null

otherwise.
**Throws:** IllegalArgumentException

- if

cd

does not
represent a

MemoryUsage

with the attributes described
above.

---

#### Method Detail

getInit

```java
public long getInit()
```

Returns the amount of memory in bytes that the Java virtual machine
initially requests from the operating system for memory management.
This method returns

-1

if the initial memory size is undefined.

**Returns:** the initial size of memory in bytes;

-1

if undefined.

---

#### getInit

public long getInit()

Returns the amount of memory in bytes that the Java virtual machine
initially requests from the operating system for memory management.
This method returns

-1

if the initial memory size is undefined.

getUsed

```java
public long getUsed()
```

Returns the amount of used memory in bytes.

**Returns:** the amount of used memory in bytes.

---

#### getUsed

public long getUsed()

Returns the amount of used memory in bytes.

getCommitted

```java
public long getCommitted()
```

Returns the amount of memory in bytes that is committed for
the Java virtual machine to use. This amount of memory is
guaranteed for the Java virtual machine to use.

**Returns:** the amount of committed memory in bytes.

---

#### getCommitted

public long getCommitted()

Returns the amount of memory in bytes that is committed for
the Java virtual machine to use. This amount of memory is
guaranteed for the Java virtual machine to use.

getMax

```java
public long getMax()
```

Returns the maximum amount of memory in bytes that can be
used for memory management. This method returns

-1

if the maximum memory size is undefined.

This amount of memory is not guaranteed to be available
for memory management if it is greater than the amount of
committed memory. The Java virtual machine may fail to allocate
memory even if the amount of used memory does not exceed this
maximum size.

**Returns:** the maximum amount of memory in bytes;

-1

if undefined.

---

#### getMax

public long getMax()

Returns the maximum amount of memory in bytes that can be
used for memory management. This method returns

-1

if the maximum memory size is undefined.

This amount of memory is not guaranteed to be available
for memory management if it is greater than the amount of
committed memory. The Java virtual machine may fail to allocate
memory even if the amount of used memory does not exceed this
maximum size.

This amount of memory is not guaranteed to be available
for memory management if it is greater than the amount of
committed memory. The Java virtual machine may fail to allocate
memory even if the amount of used memory does not exceed this
maximum size.

toString

```java
public
String
toString()
```

Returns a descriptive representation of this memory usage.

**Overrides:** toString

in class

Object
**Returns:** a string representation of the object.

---

#### toString

public

String

toString()

Returns a descriptive representation of this memory usage.

from

```java
public static
MemoryUsage
from​(
CompositeData
cd)
```

Returns a

MemoryUsage

object represented by the
given

CompositeData

. The given

CompositeData

must contain the following attributes:

The attributes and the types the given CompositeData contains

Attribute Name

Type

init

java.lang.Long

used

java.lang.Long

committed

java.lang.Long

max

java.lang.Long

**Parameters:** cd

-

CompositeData

representing a

MemoryUsage
**Returns:** a

MemoryUsage

object represented by

cd

if

cd

is not

null

;

null

otherwise.
**Throws:** IllegalArgumentException

- if

cd

does not
represent a

MemoryUsage

with the attributes described
above.

---

#### from

public static

MemoryUsage

from​(

CompositeData

cd)

Returns a

MemoryUsage

object represented by the
given

CompositeData

. The given

CompositeData

must contain the following attributes:

The attributes and the types the given CompositeData contains

Attribute Name

Type

init

java.lang.Long

used

java.lang.Long

committed

java.lang.Long

max

java.lang.Long

---

